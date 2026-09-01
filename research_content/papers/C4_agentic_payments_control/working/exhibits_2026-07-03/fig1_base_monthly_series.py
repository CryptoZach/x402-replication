#!/usr/bin/env python3
"""C4 Figure 1: Base registry-facilitator monthly series (boom, bust, rebuild).

Two panels from the committed base monthly store:
  top    -- payments and distinct buyers on a shared log y axis
            (the 1.42M-to-64.3M payments span and the 14.6k-to-175k buyer
            span both warrant log scale);
  bottom -- average payment size (USD) on a linear y axis.

Reads ONLY committed inputs by repo-relative path; deterministic output
(fixed figsize/dpi; PDF CreationDate suppressed so no timestamp lands in the
image). Every plotted value is asserted against PAPER.md Table 1 as printed
before anything is drawn (HALT-1 guard: a source-vs-printed disagreement is a
finding, not a styling problem, and aborts the build).

Run from anywhere:
    python3 research_content/papers/C4_agentic_payments_control/working/exhibits_2026-07-03/fig1_base_monthly_series.py
"""

import json
import warnings
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[4]  # exhibits_2026-07-03 -> working -> C4_.. -> papers -> research_content -> repo root
BASE_MONTHLY = REPO_ROOT / "handoff/workflow_runs/agentic_payments_june_refresh_2026-07-03/results/base_monthly.json"
FIG = HERE / "figures"

# Table-1 months (the paper prints 2025-10 through 2026-06 final; earlier 2025
# micro-scale months live only in the replication archive).
MONTHS = ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02",
          "2026-03", "2026-04", "2026-05", "2026-06"]

# PAPER.md Table 1 as printed (line 125-133): the of-record surface. Payments,
# USD (raw, rounded), distinct buyers, and avg $/payment (rounded to 2 dp).
PRINTED_T1 = {
    "2025-10": {"payments": 4065328,  "usd": 3965328,  "buyers": 175237, "avg": 0.98},
    "2025-11": {"payments": 64264312, "usd": 27884714, "buyers": 118767, "avg": 0.43},
    "2025-12": {"payments": 43037218, "usd": 3265946,  "buyers": 46800,  "avg": 0.08},
    "2026-01": {"payments": 12130123, "usd": 1203956,  "buyers": 14588,  "avg": 0.10},
    "2026-02": {"payments": 1419951,  "usd": 2066780,  "buyers": 22649,  "avg": 1.46},
    "2026-03": {"payments": 1820877,  "usd": 2276725,  "buyers": 14845,  "avg": 1.25},
    "2026-04": {"payments": 2304609,  "usd": 1938922,  "buyers": 38631,  "avg": 0.84},
    "2026-05": {"payments": 3041318,  "usd": 1030242,  "buyers": 110766, "avg": 0.34},
    "2026-06": {"payments": 5826498,  "usd": 687524,   "buyers": 48343,  "avg": 0.12},
}

# Paul Tol bright qualitative palette (colorblind-safe).
C_PAY, C_BUY, C_AVG = "#4477AA", "#EE6677", "#228833"


def load_source():
    """Load the committed base monthly store, keyed by 'YYYY-MM'.

    Rows are JSON objects with keys m/transfers/usd/buyers/sellers.
    """
    raw = json.loads(BASE_MONTHLY.read_text())
    out = {}
    for row in raw["rows"]:
        ym = row["m"][:7]  # '2025-10-01' -> '2025-10'
        out[ym] = row
    return out


def crosscheck(src):
    """HALT-1 guard: assert every source value matches PAPER.md Table 1 as printed."""
    checks = []
    for m in MONTHS:
        s, p = src[m], PRINTED_T1[m]
        # exact integer matches
        assert s["transfers"] == p["payments"], f"{m} payments {s['transfers']} != printed {p['payments']}"
        assert s["buyers"] == p["buyers"],       f"{m} buyers {s['buyers']} != printed {p['buyers']}"
        # printed USD is the raw value rounded to the nearest dollar
        assert round(s["usd"]) == p["usd"],      f"{m} usd round({s['usd']}) != printed {p['usd']}"
        # avg $/payment = usd/transfers, rounds to the printed 2-dp figure
        avg = s["usd"] / s["transfers"]
        assert round(avg, 2) == p["avg"],        f"{m} avg round({avg},2) != printed {p['avg']}"
        checks.append((m, s["transfers"], s["buyers"], round(avg, 4), p["avg"]))
    return checks


def thousands(x, _pos):
    if x >= 1_000_000:
        return f"{x/1_000_000:g}M"
    if x >= 1_000:
        return f"{x/1_000:g}k"
    return f"{x:g}"


def main():
    src = load_source()
    checks = crosscheck(src)  # aborts on any printed-table disagreement

    payments = [src[m]["transfers"] for m in MONTHS]
    buyers = [src[m]["buyers"] for m in MONTHS]
    avg = [src[m]["usd"] / src[m]["transfers"] for m in MONTHS]
    x = list(range(len(MONTHS)))

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(8.2, 6.4), sharex=True,
        gridspec_kw={"height_ratios": [1.55, 1.0], "hspace": 0.12})

    # --- top panel: payments + distinct buyers, shared log y ---
    ax1.plot(x, payments, color=C_PAY, lw=1.9, marker="o", ms=5, label="Payments")
    ax1.plot(x, buyers, color=C_BUY, lw=1.6, marker="s", ms=4.5, ls="--", label="Distinct buyers")
    ax1.set_yscale("log")
    ax1.set_ylim(8_000, 1.2e8)
    ax1.yaxis.set_major_formatter(FuncFormatter(thousands))
    ax1.set_ylabel("Count (log scale)")
    ax1.grid(True, which="major", axis="y", color="0.88", lw=0.6)
    ax1.legend(loc="upper right", fontsize=8, frameon=False)

    # annotations: November grind peak (payments max) and February trough (payments min)
    nov = MONTHS.index("2025-11")
    feb = MONTHS.index("2026-02")
    # PLACED BELOW THE POINT, not above it. November is the payments MAXIMUM, so an offset of
    # 1.7x the peak on a log axis put the label outside the top of the axes and it was clipped.
    # Dropping to 0.45x sits it in the empty space under the peak with the arrow pointing up.
    # "grind peak" was program jargon; the label now says what the series does, and the 541
    # events per buyer beside it already carries the automation signature that word was doing.
    ax1.annotate("Nov 2025 payments peak\n64.3M payments (541 events/buyer)",
                 xy=(nov, payments[nov]), xytext=(nov - 0.45, payments[nov] * 0.095),
                 fontsize=7.5, ha="left", va="top",
                 bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.70),
                 arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
    ax1.annotate("Feb 2026 trough\n1.42M payments",
                 xy=(feb, payments[feb]), xytext=(feb - 0.05, payments[feb] * 0.20),
                 fontsize=7.5, ha="center", va="top",
                 bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.82),
                 arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))

    # --- bottom panel: average payment size, linear ---
    ax2.plot(x, avg, color=C_AVG, lw=1.9, marker="D", ms=4.5)
    ax2.fill_between(x, avg, color=C_AVG, alpha=0.10)
    # HEADROOM FOR THE LABELS, not just for the line. Every point carries a $X.XX label 6 points
    # above it, so the axis has to clear the series maximum plus the label, not the maximum. At
    # ylim 1.6 against a 1.46 high the top labels ran into the frame and the panel above it.
    ax2.set_ylim(0, 1.78)
    ax2.set_ylabel("Avg $/payment (USD)")
    ax2.grid(True, which="major", axis="y", color="0.88", lw=0.6)
    # LABELS ALTERNATE ABOVE AND BELOW THE POINT. Nine labels on a series that moves little between
    # neighbours collide horizontally when they all sit on the same side; staggering them halves the
    # crowding without moving a single value. The white bbox lifts each label off the fill and the
    # marker underneath it, which is what made the small ones (the $0.10 era) hard to read against
    # the shaded area rather than merely tight.
    # BELOW IS ONLY AVAILABLE WHEN THERE IS ROOM BELOW. A plain index alternation pushed the
    # low-value months ($0.10, $0.08, $0.12) under the axis floor, where they were clipped by the
    # frame and collided with the month ticks: the stagger fixed crowding in the middle of the
    # range and created a worse defect at the bottom of it. Side is now chosen by headroom first
    # and alternation second, so a point too close to zero always labels upward.
    FLOOR_CLEARANCE = 0.28   # data units needed under a point to fit the label inside the axes
    for i, (xi, a) in enumerate(zip(x, avg)):
        above = (i % 2 == 0) or a < FLOOR_CLEARANCE
        ax2.annotate(f"${a:.2f}", xy=(xi, a),
                     xytext=(0, 7 if above else -9), textcoords="offset points",
                     fontsize=6.8, ha="center", va="bottom" if above else "top", color="0.25",
                     bbox=dict(boxstyle="round,pad=0.14", fc="white", ec="none", alpha=0.78))

    ax2.set_xticks(x)
    ax2.set_xticklabels(MONTHS, rotation=45, ha="right", fontsize=8)
    ax2.set_xlabel("Month (Base, registry-facilitator submitted USDC transfers)")

    fig.suptitle("Figure 1. Base monthly series: boom, bust, rebuild", fontsize=12, y=0.965)
    fig.text(0.5, 0.925,
             "Payments peak Nov 2025 (machine-grind era), trough Feb 2026, then rebuild; "
             "average payment size mirrors the shift.",
             ha="center", fontsize=8.5, color="0.30")

    with warnings.catch_warnings():
        # annotations extend beyond the log axes; tight_layout still lays out correctly.
        warnings.simplefilter("ignore", UserWarning)
        fig.tight_layout(rect=(0, 0, 1, 0.915))
    FIG.mkdir(exist_ok=True)
    png = FIG / "fig1_base_monthly_series.png"
    pdf = FIG / "fig1_base_monthly_series.pdf"
    fig.savefig(png, dpi=200)
    fig.savefig(pdf, metadata={"CreationDate": None})  # suppress PDF timestamp -> deterministic
    plt.close(fig)

    print(f"wrote {png.name} and {pdf.name}")
    print("cross-check (month, payments, buyers, computed_avg, printed_avg):")
    for row in checks:
        print("  ", row)
    print("all", len(checks), "months match PAPER.md Table 1 as printed.")


if __name__ == "__main__":
    main()
