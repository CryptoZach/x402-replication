#!/usr/bin/env python3
"""D6 item 2: organic-only HHI sensitivity (May 2026, Base and Solana).

Recomputes the May concentration readings excluding the identified pipeline flows:
  - Base: Meridian (mrdn), the validated proxy pipeline of PAPER.md Section 5,
    excluded from both the count and the value layer;
  - Solana: the relai small-cardinality cluster (19 buyers, 18 sellers,
    roughly $22 thousand; PAPER.md Section 4.2), reported both ways (in and out).

Derivation discipline (the D3 HALT-1 guard pattern): the script FIRST asserts that
the printed Table 2 and Table 3 values reproduce from the committed store (the
phase-1 May facilitator volume result, the merged attribution CSV, and the phase-2
Solana May split), and only then computes the exclusions from the store's
per-facilitator rows, never from the printed "all others" lump. Any assertion
failure aborts (a finding, not a styling problem).

Inputs (committed; repo-relative):
  handoff/workflow_runs/agentic_payments_phase1_2026-06-11/results/p1_base_may_fac_volume.result.json
  handoff/workflow_runs/agentic_payments_polygon_acquisition_2026-06-11/x402_facilitator_attribution_merged_2026-06-11.csv
  handoff/workflow_runs/agentic_payments_phase2_2026-06-11/results/p2_solana_may_split.result.json
  ../exhibits_2026-07-03/data/table2_base_may2026.json   (printed-share crosscheck)
  ../exhibits_2026-07-03/data/table3_solana_may2026.json (printed-share crosscheck)

Output: derived/hhi_sensitivity_may2026.json plus a printed summary.

Run from anywhere:
    python3 research_content/papers/C4_agentic_payments_control/working/measurement_2026-07-10/derive_hhi_sensitivity.py
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
RUNS = REPO / "handoff/workflow_runs"
P1 = RUNS / "agentic_payments_phase1_2026-06-11/results/p1_base_may_fac_volume.result.json"
MAP = RUNS / "agentic_payments_polygon_acquisition_2026-06-11/x402_facilitator_attribution_merged_2026-06-11.csv"
P2S = RUNS / "agentic_payments_phase2_2026-06-11/results/p2_solana_may_split.result.json"
T2 = HERE.parent / "exhibits_2026-07-03/data/table2_base_may2026.json"
T3 = HERE.parent / "exhibits_2026-07-03/data/table3_solana_may2026.json"
OUT = HERE / "derived/hhi_sensitivity_may2026.json"

# Meridian proxy-settlement correction of record (PAPER.md Section 5; phase-2 validation):
# external-seller leg across 11,088 paired payments.
MRDN_CORR_N = 11088
MRDN_CORR_USD = 373610.22

# Printed anchors (PAPER.md Section 4.2 as printed at v0.7).
PRINTED = {
    "base_raw_hhi_count": 5965,
    "base_raw_hhi_value": 5621,
    "base_corr_hhi_count": 6009,
    "base_corr_hhi_value": 4040,
    "base_corr_total_n": 3030230,   # Table 2 payments column sum
    "base_corr_total_usd": 652882,  # corrected May Base volume (Section 5)
    "base_raw_total_n": 3041318,    # Table 1 May payments
    "base_raw_total_usd": 1030242,  # Table 1 May USD (raw)
    "solana_hhi_count": 4203,
    "solana_hhi_value": 4915,
    "solana_total_n": 799769,
    # Table 2 as printed: facilitator -> (payments, usd_rounded)
    "table2": {
        "coinbase": (2290425, 168516),
        "fluxa": (488686, 56584),
        "payAI": (178083, 11064),
        "mrdn": (11088, 373610),
        "relai": (11996, 28997),
    },
    # Table 3 as printed: facilitator -> (payments, usdc_rounded, buyers, sellers)
    "table3": {
        "dexter": (414665, 20218, 2900, 7458),
        "coinbase": (307766, 89294, 75478, 84),
        "payAI": (36962, 2470, 361, 90),
        "corbits": (23566, 154, 309, 29),
        "relai": (15639, 22066, 19, 18),
    },
}


def rows_of(path):
    d = json.loads(Path(path).read_text())
    return d.get("result", {}).get("rows", d.get("rows", []))


def hhi(shares):
    return sum((100.0 * s) ** 2 for s in shares)


def hhi_of(agg, n_idx, u_idx):
    tn = sum(v[n_idx] for v in agg.values())
    tu = sum(v[u_idx] for v in agg.values())
    return (hhi(v[n_idx] / tn for v in agg.values()),
            hhi(v[u_idx] / tu for v in agg.values()), tn, tu)


def main():
    # --- Base May per-facilitator rows from the committed store ---
    name = {}
    with open(MAP) as f:
        for r in csv.DictReader(f):
            if r["network"] == "base":
                name[r["address"].lower()] = r["name_x402scan"] or r["name_hashed"]
    raw = {}
    for r in rows_of(P1):
        g = name.get(r["submitter"].lower())
        assert g, f"unmapped submitter in committed store: {r['submitter']}"
        a = raw.setdefault(g, [0, 0.0])
        a[0] += r["n"]
        a[1] += r["usd"]

    # --- Guard 1: raw pre-correction reproduces (Table 1 May totals; printed raw HHIs) ---
    rc, rv, rn, ru = hhi_of(raw, 0, 1)
    assert rn == PRINTED["base_raw_total_n"], f"raw total {rn} != printed {PRINTED['base_raw_total_n']}"
    assert round(ru) == PRINTED["base_raw_total_usd"], f"raw usd {ru} != printed {PRINTED['base_raw_total_usd']}"
    assert round(rc) == PRINTED["base_raw_hhi_count"], f"raw count HHI {rc} != printed"
    assert round(rv) == PRINTED["base_raw_hhi_value"], f"raw value HHI {rv} != printed"

    # --- Guard 2: the corrected split reproduces Table 2 as printed ---
    corr = {k: list(v) for k, v in raw.items()}
    corr["mrdn"] = [MRDN_CORR_N, MRDN_CORR_USD]
    cc, cv, cn, cu = hhi_of(corr, 0, 1)
    assert cn == PRINTED["base_corr_total_n"], f"corrected total {cn} != printed"
    assert round(cu) == PRINTED["base_corr_total_usd"], f"corrected usd {cu} != printed"
    assert round(cc) == PRINTED["base_corr_hhi_count"], f"corrected count HHI {cc} != printed"
    assert round(cv) == PRINTED["base_corr_hhi_value"], f"corrected value HHI {cv} != printed"
    for g, (pn, pu) in PRINTED["table2"].items():
        assert corr[g][0] == pn, f"Table 2 {g} payments {corr[g][0]} != printed {pn}"
        assert round(corr[g][1]) == pu, f"Table 2 {g} usd {corr[g][1]} != printed {pu}"
    t2 = json.loads(T2.read_text())
    display = {"Coinbase (CDP)": "coinbase", "fluxa": "fluxa", "payAI": "payAI",
               "Meridian (mrdn)": "mrdn", "relai": "relai",
               "Dexter": "dexter", "Coinbase": "coinbase", "corbits": "corbits"}
    for row in t2["facilitators"]:
        g = display.get(row["name"])
        if g in corr:
            assert round(100 * corr[g][0] / cn, 1) == row["count_share"], f"{g} count share vs exhibits data"
            assert round(100 * corr[g][1] / cu, 1) == row["value_share"], f"{g} value share vs exhibits data"

    # --- Guard 3: Solana split reproduces Table 3 as printed ---
    sol = {r["name"]: [r["transfers"], r["usdc"], r["buyers"], r["sellers"]] for r in rows_of(P2S)}
    sc, sv, sn, su = hhi_of(sol, 0, 1)
    assert sn == PRINTED["solana_total_n"], f"solana total {sn} != printed"
    assert round(sc) == PRINTED["solana_hhi_count"], f"solana count HHI {sc} != printed"
    assert round(sv) == PRINTED["solana_hhi_value"], f"solana value HHI {sv} != printed"
    for g, (pn, pu, pb, ps) in PRINTED["table3"].items():
        assert sol[g][0] == pn and round(sol[g][1]) == pu, f"Table 3 {g} row mismatch"
        assert sol[g][2] == pb and sol[g][3] == ps, f"Table 3 {g} buyers/sellers mismatch"
    below5 = su - sum(sol[g][1] for g in PRINTED["table3"])
    assert round(below5) == 172, f"below-top-five residual {below5} != the approximately 172 USD caption"
    t3 = json.loads(T3.read_text())
    for row in t3["facilitators"]:
        g = display.get(row["name"], row["name"])
        assert round(100 * sol[g][0] / sn, 1) == row["count_share"], f"{g} solana count share vs exhibits data"
        assert round(100 * sol[g][1] / su, 1) == row["value_share"], f"{g} solana value share vs exhibits data"

    # --- Exclusions (from per-facilitator store rows, never the printed lump) ---
    base_ex = {k: v for k, v in corr.items() if k != "mrdn"}
    bxc, bxv, bxn, bxu = hhi_of(base_ex, 0, 1)
    sol_ex = {k: v for k, v in sol.items() if k != "relai"}
    sxc, sxv, sxn, sxu = hhi_of(sol_ex, 0, 1)

    def top(agg, idx, total):
        g = max(agg, key=lambda k: agg[k][idx])
        return {"facilitator": g, "share_pct": round(100 * agg[g][idx] / total, 1)}

    out = {
        "_provenance": {
            "derivation": "derive_hhi_sensitivity.py (D6 item 2)",
            "inputs": [str(P1.relative_to(REPO)), str(MAP.relative_to(REPO)),
                       str(P2S.relative_to(REPO)), str(T2.relative_to(REPO)), str(T3.relative_to(REPO))],
            "guards": "printed Table 2/3 values, raw and corrected HHIs, and exhibits data shares all asserted before exclusions",
            "exclusion_rule": "Base: drop mrdn (validated proxy pipeline) from the corrected split; Solana: drop relai (small-cardinality cluster) from the full split",
        },
        "base_may2026": {
            "raw": {"hhi_count": round(rc), "hhi_value": round(rv), "n": rn, "usd": round(ru)},
            "corrected": {"hhi_count": round(cc), "hhi_value": round(cv), "n": cn, "usd": round(cu)},
            "pipeline_excluded": {
                "hhi_count": round(bxc), "hhi_value": round(bxv), "n": bxn, "usd": round(bxu),
                "top_count": top(base_ex, 0, bxn), "top_value": top(base_ex, 1, bxu),
                "value_shares_pct": {g: round(100 * v[1] / bxu, 1) for g, v in
                                     sorted(base_ex.items(), key=lambda kv: -kv[1][1])[:5]},
            },
        },
        "solana_may2026": {
            "as_printed": {"hhi_count": round(sc), "hhi_value": round(sv), "n": sn, "usd": round(su)},
            "relai_excluded": {
                "hhi_count": round(sxc), "hhi_value": round(sxv), "n": sxn, "usd": round(sxu),
                "top_count": top(sol_ex, 0, sxn), "top_value": top(sol_ex, 1, sxu),
                "value_shares_pct": {g: round(100 * v[1] / sxu, 1) for g, v in
                                     sorted(sol_ex.items(), key=lambda kv: -kv[1][1])[:5]},
            },
        },
        "store_observation_not_applied": (
            "relai on Base is itself mostly self-hop: 9,818 of its 11,996 May transfers route to a "
            "registry address, so its external-seller leg is 2,178 transfers / 14,493 USD against the "
            "raw 11,996 / 28,997 printed in Table 2. Per-facilitator corrections beyond Meridian remain "
            "deferred per PAPER.md Section 11; recorded here as a store observation only."
        ),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(REPO)}")
    print(f"Base   raw {round(rc)}/{round(rv)}  corrected {round(cc)}/{round(cv)}  "
          f"mrdn-excluded {round(bxc)}/{round(bxv)} (n={bxn:,}, usd={bxu:,.0f})")
    print(f"Solana printed {round(sc)}/{round(sv)}  relai-excluded {round(sxc)}/{round(sxv)} "
          f"(n={sxn:,}, usd={sxu:,.0f})")


if __name__ == "__main__":
    main()
