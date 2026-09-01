#!/usr/bin/env python3
"""D6 item 4: Base per-facilitator monthly HHI series and rank persistence, 2025-10 through 2026-06.

Per month: count HHI (transfer basis, the Table 1 count) and value HHI, each in three variants:
  - raw: per-facilitator transfers and transfer-sum dollars as measured;
  - mrdn_corrected: the Table 2 method, Meridian collapsed to its external-seller leg
    (its internal-hop transfers and dollars removed), all other facilitators raw. Applied
    only in months where Meridian's proxy pairing structure validates at monthly-aggregate
    granularity (transfers = 2x AuthorizationUsed events AND internal hops = events); a
    month where the hop exists but the structure does not validate is labeled raw_only
    rather than silently corrected. Literal per-payment pairing was validated in May and
    June (PAPER.md Section 5); earlier months rest on the aggregate structure check.
  - full_hop_corrected: every facilitator's registry-recipient internal hops removed (the
    aggregate method behind the paper's corrected cumulative series). Carried as a labeled
    sensitivity variant; the May concentration snapshot of record is mrdn_corrected.

Plus a top-operator-by-layer persistence row per month (count layer and value layer).

Guards (assert before output): per-month sums reproduce the committed Table 1 store
exactly; per-month internal-hop sums reproduce the committed hop-by-month store; the May
column reproduces the printed Table 2 HHIs (raw 5,965 / 5,621; corrected 6,009 / 4,040)
and Meridian's printed legs.

Inputs: results/base_fac_monthly_2025-10_2026-06.result.json and
results/base_fac_auth_monthly_2025-10_2026-06.result.json (this run), plus the committed
base_monthly.json (Table 1 store) and aggregate_registry_internal_hop_by_month.json.

Output: derived/monthly_hhi_series.json plus a printed summary.

Run from anywhere:
    python3 research_content/papers/C4_agentic_payments_control/working/measurement_2026-07-10/derive_monthly_hhi.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
RUNS = REPO / "handoff/workflow_runs"
T1_STORE = RUNS / "agentic_payments_june_refresh_2026-07-03/results/base_monthly.json"
HOP_STORE = RUNS / "agentic_payments_june_pairing_coverage_2026-07-03/results/aggregate_registry_internal_hop_by_month.json"
TR = HERE / "results/base_fac_monthly_2025-10_2026-06.result.json"
AU = HERE / "results/base_fac_auth_monthly_2025-10_2026-06.result.json"
OUT = HERE / "derived/monthly_hhi_series.json"

MONTHS = ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02",
          "2026-03", "2026-04", "2026-05", "2026-06"]

PRINTED_MAY = {"raw_count": 5965, "raw_value": 5621, "corr_count": 6009, "corr_value": 4040,
               "mrdn_raw": (22176, 750970.72), "mrdn_ext": (11088, 373610.22)}


def rows_of(path):
    d = json.loads(Path(path).read_text())
    return d.get("result", {}).get("rows", d.get("rows", []))


def hhi(vals):
    tot = sum(vals)
    return sum((100.0 * v / tot) ** 2 for v in vals) if tot else None


def main():
    # fac[month][grp] = {int_n, ext_n, int_u, ext_u}
    fac = {}
    for r in rows_of(TR):
        m = r["m"][:7]
        g = fac.setdefault(m, {}).setdefault(r["grp"], {"int_n": 0, "ext_n": 0, "int_u": 0.0, "ext_u": 0.0})
        k = "int" if r["is_internal_hop"] == 1 else "ext"
        g[k + "_n"] += r["transfers"]
        g[k + "_u"] += r["usd"]
    auth = {}
    for r in rows_of(AU):
        auth.setdefault(r["m"][:7], {})[r["grp"]] = r

    # --- Guard 1: monthly raw sums reproduce the committed Table 1 store ---
    t1 = {r["m"][:7]: r for r in rows_of(T1_STORE)}
    for m in MONTHS:
        n = sum(v["int_n"] + v["ext_n"] for v in fac[m].values())
        u = sum(v["int_u"] + v["ext_u"] for v in fac[m].values())
        assert n == t1[m]["transfers"], f"{m} transfers {n} != Table 1 store {t1[m]['transfers']}"
        assert abs(u - t1[m]["usd"]) < 0.5, f"{m} usd {u} != Table 1 store {t1[m]['usd']}"

    # --- Guard 2: monthly internal-hop sums reproduce the committed hop store ---
    hop = {r["m"][:7]: r for r in rows_of(HOP_STORE)}
    for m in MONTHS:
        hn = sum(v["int_n"] for v in fac[m].values())
        hu = sum(v["int_u"] for v in fac[m].values())
        assert hn == hop[m]["internal_transfers"], f"{m} hops {hn} != hop store {hop[m]['internal_transfers']}"
        assert abs(hu - hop[m]["usd_internal_hop"]) < 0.5, f"{m} hop usd {hu} != hop store"

    # --- Guard 3: the May column reproduces the printed Table 2 readings ---
    may = fac["2026-05"]
    mr = may["mrdn"]
    assert (mr["int_n"] + mr["ext_n"], round(mr["int_u"] + mr["ext_u"], 2)) == PRINTED_MAY["mrdn_raw"]
    assert (mr["ext_n"], round(mr["ext_u"], 2)) == PRINTED_MAY["mrdn_ext"]

    def series_row(m):
        rows = fac[m]
        raw_n = {g: v["int_n"] + v["ext_n"] for g, v in rows.items()}
        raw_u = {g: v["int_u"] + v["ext_u"] for g, v in rows.items()}
        # mrdn pairing-structure check at monthly-aggregate granularity
        mrdn = rows.get("mrdn")
        a = auth.get(m, {}).get("mrdn", {}).get("auth_events", 0)
        if mrdn is None:
            pairing = {"present": False, "consistent": None}
        else:
            tot = mrdn["int_n"] + mrdn["ext_n"]
            pairing = {"present": True, "auth_events": a, "transfers": tot,
                       "internal_transfers": mrdn["int_n"],
                       "consistent": (tot == 2 * a and mrdn["int_n"] == a)}
        # mrdn-corrected variant (the Table 2 method)
        if mrdn is None:
            corr_n, corr_u, corr_label = dict(raw_n), dict(raw_u), "no_mrdn_flow"
        elif pairing["consistent"]:
            corr_n, corr_u = dict(raw_n), dict(raw_u)
            corr_n["mrdn"] = mrdn["ext_n"]
            corr_u["mrdn"] = mrdn["ext_u"]
            corr_label = "corrected"
        else:
            corr_n, corr_u, corr_label = None, None, "raw_only_pairing_unvalidated"
        # full-hop variant (aggregate method; every facilitator at its external legs)
        full_n = {g: v["ext_n"] for g, v in rows.items() if v["ext_n"] > 0}
        full_u = {g: v["ext_u"] for g, v in rows.items() if v["ext_u"] > 0}

        def top(d):
            g = max(d, key=d.get)
            return {"facilitator": g, "share_pct": round(100.0 * d[g] / sum(d.values()), 1)}

        return {
            "m": m,
            "facilitators_active": len(rows),
            "raw": {"hhi_count": round(hhi(raw_n.values())), "hhi_value": round(hhi(raw_u.values())),
                    "transfers": sum(raw_n.values()), "usd": round(sum(raw_u.values()), 2)},
            "mrdn_corrected": None if corr_n is None else {
                "hhi_count": round(hhi(corr_n.values())), "hhi_value": round(hhi(corr_u.values())),
                "payments": sum(corr_n.values()), "usd": round(sum(corr_u.values()), 2)},
            "mrdn_corrected_label": corr_label,
            "full_hop_corrected": {"hhi_count": round(hhi(full_n.values())), "hhi_value": round(hhi(full_u.values())),
                                   "transfers": sum(full_n.values()), "usd": round(sum(full_u.values()), 2)},
            "mrdn_pairing": pairing,
            "top_count_raw": top(raw_n),
            "top_value_raw": top(raw_u),
            "top_count_of_record": top(corr_n if corr_n else raw_n),
            "top_value_of_record": top(corr_u if corr_u else raw_u),
        }

    series = [series_row(m) for m in MONTHS]

    may_row = next(s for s in series if s["m"] == "2026-05")
    assert may_row["raw"]["hhi_count"] == PRINTED_MAY["raw_count"], may_row["raw"]
    assert may_row["raw"]["hhi_value"] == PRINTED_MAY["raw_value"], may_row["raw"]
    assert may_row["mrdn_corrected"]["hhi_count"] == PRINTED_MAY["corr_count"], may_row["mrdn_corrected"]
    assert may_row["mrdn_corrected"]["hhi_value"] == PRINTED_MAY["corr_value"], may_row["mrdn_corrected"]

    persistence = {
        "count_layer": [{"m": s["m"], **s["top_count_of_record"]} for s in series],
        "value_layer": [{"m": s["m"], **s["top_value_of_record"]} for s in series],
        "count_layer_distinct_leaders": sorted({s["top_count_of_record"]["facilitator"] for s in series}),
        "value_layer_distinct_leaders": sorted({s["top_value_of_record"]["facilitator"] for s in series}),
    }

    out = {
        "_provenance": {
            "derivation": "derive_monthly_hhi.py (D6 item 4)",
            "query_results": ["results/base_fac_monthly_2025-10_2026-06.result.json",
                              "results/base_fac_auth_monthly_2025-10_2026-06.result.json"],
            "committed_anchors": [str(T1_STORE.relative_to(REPO)), str(HOP_STORE.relative_to(REPO))],
            "count_basis": "registry-facilitator submitted USDC transfers (the Table 1 count); mrdn_corrected collapses Meridian to its external leg (the Table 2 payments basis)",
            "correction_policy": "mrdn_corrected applied only where the monthly pairing structure validates (2x-transfers and hop = events); 2025-11 fails the check (48 transfers, de minimis) and is labeled raw_only; per-payment pairing validation exists for May and June per PAPER.md Section 5",
            "june_status": "June 2026 enters the series as a complete labeled month; concentration CLAIMS remain May-anchored per PAPER.md Section 3.5",
            "guards": "Table 1 store, hop store, and printed May HHIs all asserted",
        },
        "series": series,
        "rank_persistence": persistence,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(REPO)}")
    for s in series:
        c = s["mrdn_corrected"] or s["raw"]
        lbl = "" if s["mrdn_corrected"] else " [" + s["mrdn_corrected_label"] + "]"
        print(f"  {s['m']}  raw {s['raw']['hhi_count']:>5}/{s['raw']['hhi_value']:>5}  "
              f"mrdn-corr {c['hhi_count']:>5}/{c['hhi_value']:>5}{lbl}  "
              f"top count {s['top_count_of_record']['facilitator']:9s} "
              f"top value {s['top_value_of_record']['facilitator']}")


if __name__ == "__main__":
    main()
