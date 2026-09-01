#!/usr/bin/env python3
"""D6 item 3: registry-coverage-by-month series, Base, 2025-10 through 2026-06.

Monthly share of Base `AuthorizationUsed` events attributed to the registry set,
in both June readings PAPER.md Section 3.3 defines:
  - fleet-in-denominator: registry / (registry + non-registry);
  - fleet-set-aside:      registry / (registry + non-registry - fleet), where fleet
    is the coordinated fifteen-address non-registry metering fleet of Sections 3.3/7.

Inputs:
  - handoff/workflow_runs/agentic_payments_june_refresh_2026-07-03/results/base_auth_monthly.json
    (committed June-refresh store, query_id 7877472: monthly AuthorizationUsed events split
    registry / non-registry; closed months are stable, so the store is not re-queried)
  - results/fleet15_auth_monthly.result.json (this run: the fleet's own monthly events; the
    query returned exactly one row, 2026-06, so the fleet did not exist before June)

Guards: the two printed June readings (43 percent fleet-in, 96 percent fleet-set-aside)
reproduce; the fleet's June events match the committed top-submitter store sum (7,033,614).
Note: the printed 92.3 percent May coverage anchor (Section 3.3) is a TRAILING-30-DAY
window measured at the census date, not a calendar month, so it is not asserted here;
the calendar-May fleet-in reading is 89.5 percent.

Output: derived/coverage_by_month.json plus a printed summary.

Run from anywhere:
    python3 research_content/papers/C4_agentic_payments_control/working/measurement_2026-07-10/derive_coverage_series.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
STORE = REPO / "handoff/workflow_runs/agentic_payments_june_refresh_2026-07-03/results/base_auth_monthly.json"
FLEET = HERE / "results/fleet15_auth_monthly.result.json"
OUT = HERE / "derived/coverage_by_month.json"

MONTHS = ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02",
          "2026-03", "2026-04", "2026-05", "2026-06"]


def rows_of(path):
    d = json.loads(Path(path).read_text())
    return d.get("result", {}).get("rows", d.get("rows", []))


def main():
    cov = {}
    for r in rows_of(STORE):
        m = r["m"][:7]
        cov.setdefault(m, {})["reg" if r["is_registry"] == 1 else "non"] = r

    fleet_rows = rows_of(FLEET)
    fleet = {r["m"][:7]: r for r in fleet_rows}
    # The fleet query covered 2025-04 through 2026-06 and returned June only.
    assert set(fleet) == {"2026-06"}, f"fleet active months: {sorted(fleet)}"
    assert fleet["2026-06"]["auth_events"] == 7033614, fleet["2026-06"]["auth_events"]
    assert fleet["2026-06"]["submitters_active"] == 15

    series = []
    for m in MONTHS:
        reg = cov[m]["reg"]["auth_events"]
        non = cov[m]["non"]["auth_events"]
        fl = fleet.get(m, {}).get("auth_events", 0)
        fleet_in = 100.0 * reg / (reg + non)
        fleet_aside = 100.0 * reg / (reg + non - fl)
        series.append({
            "m": m,
            "registry_auth_events": reg,
            "non_registry_auth_events": non,
            "fleet_auth_events": fl,
            "coverage_fleet_in_denominator_pct": round(fleet_in, 2),
            "coverage_fleet_set_aside_pct": round(fleet_aside, 2),
            "registry_authorizers": cov[m]["reg"]["authorizers"],
            "non_registry_authorizers": cov[m]["non"]["authorizers"],
        })

    jun = series[-1]
    assert jun["m"] == "2026-06"
    # Guard: the two printed June readings reproduce (PAPER.md Section 3.3: 43 and 96 percent).
    assert round(jun["coverage_fleet_in_denominator_pct"]) == 43, jun
    assert round(jun["coverage_fleet_set_aside_pct"]) == 96, jun

    out = {
        "_provenance": {
            "derivation": "derive_coverage_series.py (D6 item 3)",
            "numerator_denominator_store": str(STORE.relative_to(REPO)) + " (committed; closed months stable; not re-queried)",
            "fleet_store": "results/fleet15_auth_monthly.result.json (this run; June-only, so the fleet-set-aside reading differs from fleet-in only in 2026-06)",
            "definitions": "PAPER.md Section 3.3: fleet-in-denominator and fleet-set-aside; events are Base USDC AuthorizationUsed",
            "printed_anchor_notes": [
                "June readings printed in Section 3.3 (43 / 96 percent) asserted and reproduced",
                "the 92.3 percent May anchor is a trailing-30-day window at the census date, not calendar May; calendar-May fleet-in is 89.53 percent (not a contradiction; different window)",
            ],
        },
        "series": series,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(REPO)}")
    for s in series:
        print(f"  {s['m']}  fleet-in {s['coverage_fleet_in_denominator_pct']:6.2f}%   "
              f"fleet-aside {s['coverage_fleet_set_aside_pct']:6.2f}%   "
              f"(reg {s['registry_auth_events']:,} / non-reg {s['non_registry_auth_events']:,})")


if __name__ == "__main__":
    main()
