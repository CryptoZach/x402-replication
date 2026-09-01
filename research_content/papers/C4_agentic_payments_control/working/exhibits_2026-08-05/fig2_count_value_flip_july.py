#!/usr/bin/env python3
"""C4 Figure 2 rebuild for July 2026 snapshot (Phase 2 Option A).

Assert-before-draw against the July tables as they will be printed.
Does NOT edit PAPER.md or the May exhibit inputs; writes PNG/PDF under this run's figures/.
"""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

HERE = Path(__file__).resolve().parent
# REPRODUCIBLE FROM THE REPO, which it was not. This pointed at working/derived/, a directory
# that exists in no commit: `git ls-tree origin/main -- working/derived` returns nothing, so a
# clean checkout could not rebuild this figure at all and the failure was a FileNotFoundError
# rather than anything a reader would connect to a missing input. The two JSONs it needs are
# committed BESIDE this script. The derived/ path is kept as the first choice so an
# environment that has one still uses it, and the script now falls back to its own directory.
DATA = HERE.parent / "derived"
if not DATA.is_dir():
    DATA = HERE
FIG = HERE
C_COUNT, C_VALUE = "#4477AA", "#EE6677"


def load_panel(fname):
    d = json.loads((DATA / fname).read_text())
    facs = d["facilitators"]
    csum = sum(f["count_share"] for f in facs)
    vsum = sum(f["value_share"] for f in facs)
    assert 95.0 <= csum <= 101.0, f"{fname}: count shares sum {csum} outside plausible range"
    assert 95.0 <= vsum <= 101.0, f"{fname}: value shares sum {vsum} outside plausible range"
    if d["panel"] == "Base":
        assert d["hhi_count"] == 6512 and d["hhi_value"] == 4700, d
        assert d["month"] == "2026-07"
    if d["panel"] == "Solana":
        assert d["hhi_count"] == 4071 and d["hhi_value"] == 3831, d
        assert d["month"] == "2026-07"
    return d


def draw(ax, panel, title, flip_pair):
    facs = panel["facilitators"]
    names = [f["name"] for f in facs]
    counts = [f["count_share"] for f in facs]
    values = [f["value_share"] for f in facs]
    n = len(facs)
    y = np.arange(n)[::-1]
    h = 0.38
    # THE LEGEND NAMES THE UNIT, because a figure is read out of order. "Count share" and
    # "Value share" are the paper's own vocabulary and are defined in the body, but a reader
    # who lands on this exhibit first has to already know it to see the flip. Naming the unit
    # in the legend makes the figure self-sufficient without changing one word of the paper's
    # terminology, which is the contribution and stays as it is.
    ax.barh(y + h / 2 + 0.01, counts, height=h, color=C_COUNT,
            label="Share of payments (count share)")
    ax.barh(y - h / 2 - 0.01, values, height=h, color=C_VALUE,
            label="Share of dollars (value share)")
    for yi, c, v in zip(y, counts, values):
        ax.text(c + 1.0, yi + h / 2 + 0.01, f"{c:.1f}%", va="center", ha="left", fontsize=7, color="0.25")
        ax.text(v + 1.0, yi - h / 2 - 0.01, f"{v:.1f}%", va="center", ha="left", fontsize=7, color="0.25")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8.5)
    for lbl in ax.get_yticklabels():
        if lbl.get_text() in flip_pair:
            lbl.set_fontweight("bold")
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of July 2026 (percent)", fontsize=8.5)
    ax.set_title(title, fontsize=10, loc="left")
    ax.grid(True, axis="x", color="0.90", lw=0.6)
    ax.set_axisbelow(True)


def main():
    base = load_panel("table2_base_july2026.json")
    sol = load_panel("table3_solana_july2026.json")
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.0, 4.6))
    draw(axL, base, "Base (corrected split, Option A)", flip_pair={"Coinbase (CDP)", "Meridian (mrdn)"})
    draw(axR, sol, "Solana (top five by count)", flip_pair={"Dexter", "payAI"})
    handles, labels = axL.get_legend_handles_labels()
    # THE LEGEND MOVES INSIDE THE PANEL, because naming the units made it wider and a figure-level
    # legend at upper right then ran over the subtitle, hiding the end of "Solana: Dexter vs
    # payAI)". Both panels are empty in their lower right (the small-share rows carry almost no
    # ink past x=20), so the legend sits there instead of competing with the title block.
    axL.legend(handles, labels, loc="lower right", fontsize=8.5, frameon=True,
               framealpha=0.9, edgecolor="0.85", borderpad=0.6)
    fig.suptitle("Figure 2. The count-versus-value monopolist flip, July 2026", fontsize=12, x=0.5, y=0.985)
    fig.text(0.5, 0.925,
             "The count leader and the value leader are different operators on both chains "
             "(Base: Coinbase vs Meridian; Solana: Dexter vs payAI).",
             ha="center", fontsize=8.5, color="0.30")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    png = FIG / "fig2_count_value_flip_july.png"
    pdf = FIG / "fig2_count_value_flip_july.pdf"
    fig.savefig(png, dpi=200)
    fig.savefig(pdf, metadata={"CreationDate": None})
    plt.close(fig)
    print(f"wrote {png.name} and {pdf.name}")
    for panel in (base, sol):
        print(f"{panel['panel']} panel:")
        for f in panel["facilitators"]:
            print(f"   {f['name']:<16} {f['count_share']:>5.1f}% / {f['value_share']:>5.1f}%")


if __name__ == "__main__":
    main()
