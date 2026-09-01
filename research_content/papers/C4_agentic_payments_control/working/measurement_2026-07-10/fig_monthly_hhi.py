#!/usr/bin/env python3
"""D6 item 4 figure (audit-only candidate): Base monthly HHI series, count and value layers.

Two panels, 2025-10 through 2026-06:
  top    -- count HHI (transfer basis): raw and mrdn-corrected;
  bottom -- value HHI: raw and mrdn-corrected, with the corrected line gapped in
            2025-11 (Meridian's 48-transfer first month fails the pairing-structure
            check and is labeled raw-only rather than silently corrected).

May 2026, the anchored concentration snapshot of record, is highlighted; June is a
complete labeled month that enters no concentration claim (PAPER.md Section 3.5).

House conventions per the exhibits build: reads ONLY the committed derived series;
deterministic output (fixed figsize/dpi; PDF CreationDate suppressed); the printed
May HHIs are re-asserted before anything is drawn. NOT wired into PAPER.md; the
wiring pass owns figure numbering and placement.

Run from anywhere:
    python3 research_content/papers/C4_agentic_payments_control/working/measurement_2026-07-10/fig_monthly_hhi.py
"""
import json
import warnings
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "derived/monthly_hhi_series.json"
FIG = HERE / "figures"

C_RAW, C_CORR, C_MAY = "#BBBBBB", "#4477AA", "#EE6677"


def main():
    series = json.loads(SRC.read_text())["series"]
    months = [s["m"] for s in series]
    x = list(range(len(months)))
    may = months.index("2026-05")

    raw_c = [s["raw"]["hhi_count"] for s in series]
    raw_v = [s["raw"]["hhi_value"] for s in series]
    corr_c = [s["mrdn_corrected"]["hhi_count"] if s["mrdn_corrected"] else float("nan") for s in series]
    corr_v = [s["mrdn_corrected"]["hhi_value"] if s["mrdn_corrected"] else float("nan") for s in series]

    # Guard: the printed May readings (PAPER.md Section 4.2) reproduce.
    assert raw_c[may] == 5965 and raw_v[may] == 5621
    assert corr_c[may] == 6009 and corr_v[may] == 4040

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.2, 6.4), sharex=True,
                                   gridspec_kw={"hspace": 0.14})

    for ax, raw, corr, label in ((ax1, raw_c, corr_c, "Count HHI (transfer basis)"),
                                 (ax2, raw_v, corr_v, "Value HHI")):
        ax.plot(x, raw, color=C_RAW, lw=1.5, marker="o", ms=4, label="Raw")
        ax.plot(x, corr, color=C_CORR, lw=1.9, marker="D", ms=4.5,
                label="Meridian-corrected (Table 2 method)")
        ax.axvline(may, color=C_MAY, lw=0.9, ls=":", alpha=0.8)
        ax.set_ylim(2000, 7200)
        ax.set_ylabel(label)
        ax.grid(True, which="major", axis="y", color="0.88", lw=0.6)

    ax1.legend(loc="lower left", fontsize=8, frameon=False)
    ax1.annotate("May 2026: anchored snapshot\n6,009 count / 4,040 value (corrected)",
                 xy=(may, corr_c[may]), xytext=(may - 3.1, 2500),
                 fontsize=7.5, ha="left", va="bottom",
                 arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
    nov = months.index("2025-11")
    ax2.annotate("Nov 2025: corrected series gapped\n(pairing unvalidated; raw-only label)",
                 xy=(nov, raw_v[nov]), xytext=(nov + 0.4, 6650),
                 fontsize=7.5, ha="left", va="top",
                 arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
    ax2.annotate("value-layer leader changes four times\n(coinbase, virtuals, payAI, mrdn)",
                 xy=(months.index("2026-03"), corr_v[months.index("2026-03")]),
                 xytext=(0.2, 2450), fontsize=7.5, ha="left", va="bottom",
                 arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))

    ax2.set_xticks(x)
    ax2.set_xticklabels(months, rotation=45, ha="right", fontsize=8)
    ax2.set_xlabel("Month (Base, registry-facilitator set; June labeled, no concentration claim)")

    fig.suptitle("Base monthly concentration: both layers stay above 2,700 on every reading",
                 fontsize=12, y=0.965)
    fig.text(0.5, 0.925,
             "Count-layer leadership is stable (Coinbase 8 of 9 months); value-layer leadership "
             "churns while the HHI never de-concentrates.",
             ha="center", fontsize=8.5, color="0.30")
    with warnings.catch_warnings():
        # annotations extend beyond the shared axes; tight_layout still lays out correctly.
        warnings.simplefilter("ignore", UserWarning)
        fig.tight_layout(rect=(0, 0, 1, 0.915))
    FIG.mkdir(exist_ok=True)
    png = FIG / "monthly_hhi_series.png"
    pdf = FIG / "monthly_hhi_series.pdf"
    fig.savefig(png, dpi=200)
    fig.savefig(pdf, metadata={"CreationDate": None})
    plt.close(fig)
    print(f"wrote {png.name} and {pdf.name}")


if __name__ == "__main__":
    main()
