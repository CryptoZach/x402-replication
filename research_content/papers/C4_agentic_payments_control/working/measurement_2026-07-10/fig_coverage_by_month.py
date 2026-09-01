#!/usr/bin/env python3
"""D6 item 3 figure (audit-only candidate): Base registry coverage by month, two readings.

Single panel, 2025-10 through 2026-06: monthly share of Base USDC `AuthorizationUsed`
events attributed to the registry set, in both PAPER.md Section 3.3 readings
(fleet-in-denominator and fleet-set-aside). The two lines separate only in June 2026,
when the fifteen-address non-registry metering fleet emits 7.03M events.

House conventions per the exhibits build: reads ONLY the committed derived series by
repo-relative path; deterministic output (fixed figsize/dpi; PDF CreationDate
suppressed); the printed June anchors are re-asserted before anything is drawn.
NOT wired into PAPER.md; the wiring pass owns figure numbering and placement.

Run from anywhere:
    python3 research_content/papers/C4_agentic_payments_control/working/measurement_2026-07-10/fig_coverage_by_month.py
"""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "derived/coverage_by_month.json"
FIG = HERE / "figures"

C_IN, C_ASIDE = "#4477AA", "#EE6677"  # Paul Tol bright, as in the exhibits build


def main():
    series = json.loads(SRC.read_text())["series"]
    months = [s["m"] for s in series]
    fin = [s["coverage_fleet_in_denominator_pct"] for s in series]
    fas = [s["coverage_fleet_set_aside_pct"] for s in series]

    # Guard: the printed June readings (PAPER.md Section 3.3: 43 / 96 percent) reproduce.
    jun = series[-1]
    assert jun["m"] == "2026-06"
    assert round(jun["coverage_fleet_in_denominator_pct"]) == 43
    assert round(jun["coverage_fleet_set_aside_pct"]) == 96
    assert all(a == b for a, b in zip(fin[:-1], fas[:-1])), "readings must agree pre-June"

    x = list(range(len(months)))
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.plot(x, fas, color=C_ASIDE, lw=2.4, marker="s", ms=5.0, ls=(0, (6, 2.5)),
            label="Fleet set aside")
    ax.plot(x, fin, color=C_IN, lw=1.9, marker="o", ms=5,
            label="Fleet in denominator")
    ax.set_ylim(0, 105)
    ax.set_ylabel("Registry share of AuthorizationUsed events (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=45, ha="right", fontsize=8)
    ax.set_xlabel("Month (Base, USDC AuthorizationUsed events)")
    ax.grid(True, which="major", axis="y", color="0.88", lw=0.6)
    ax.legend(loc="lower left", fontsize=8, frameon=False)

    jx = months.index("2026-06")
    ax.annotate("June 2026: one fifteen-address non-registry fleet emits 7.03M events.\nCoverage reads 43% counting the fleet, 96% setting it aside.",
                xy=(jx, fin[jx]), xytext=(jx - 0.45, 18),
                fontsize=7.5, ha="right", va="bottom",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.82),
                arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
    feb = months.index("2026-02")
    ax.annotate("Feb-Mar 2026: registry volume troughs, while non-registry\nactivity holds near 200k to 500k EVENTS per month (not dollars)",
                xy=(feb, fin[feb]), xytext=(feb - 1.1, 55),
                fontsize=7.5, ha="left", va="top",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.82),
                arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))

    fig.suptitle("Registry coverage by month: two readings", fontsize=12, y=0.97)
    fig.text(0.5, 0.905,
             "The fingerprint-decay watch item as a series: coverage holds at 80 to 99.6 percent "
             "until the June fleet event separates the readings.",
             ha="center", fontsize=8.5, color="0.30")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    FIG.mkdir(exist_ok=True)
    png = FIG / "coverage_by_month.png"
    pdf = FIG / "coverage_by_month.pdf"
    fig.savefig(png, dpi=200)
    fig.savefig(pdf, metadata={"CreationDate": None})
    plt.close(fig)
    print(f"wrote {png.name} and {pdf.name}")


if __name__ == "__main__":
    main()
