#!/usr/bin/env python3
"""C4 Figure 2: the count-versus-value monopolist flip, May 2026.

Paired horizontal bars per facilitator (count share vs value share), two
panels:
  Base   -- Table 2 (corrected split; Meridian at its external-seller leg);
  Solana -- Table 3 (top five by count; facilitators outside the five add
            approximately 172 USD in May and are omitted per the printed caption).

The flip is designed to read without the numbers: on Base, Coinbase owns the
count layer while Meridian owns the value layer; on Solana, Dexter carries
counts while Coinbase carries dollars. Values are exactly as printed in
PAPER.md; the committed data/*.json files transcribe the two tables verbatim
and the script asserts the two shares sum sensibly before drawing.

Reads ONLY committed inputs by repo-relative path; deterministic output
(fixed figsize/dpi; PDF CreationDate suppressed).

Run from anywhere:
    python3 research_content/papers/C4_agentic_payments_control/working/exhibits_2026-07-03/fig2_count_value_flip.py
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
FIG = HERE / "figures"

# Paul Tol bright qualitative palette (colorblind-safe): blue = count, red = value.
C_COUNT, C_VALUE = "#4477AA", "#EE6677"


def load_panel(fname):
    d = json.loads((DATA / fname).read_text())
    facs = d["facilitators"]
    # sanity guard: shares are percentages that sum to roughly 100 (rounding + top-five/all-others).
    csum = sum(f["count_share"] for f in facs)
    vsum = sum(f["value_share"] for f in facs)
    assert 95.0 <= csum <= 101.0, f"{fname}: count shares sum {csum} outside plausible range"
    assert 95.0 <= vsum <= 101.0, f"{fname}: value shares sum {vsum} outside plausible range"
    return d


def draw(ax, panel, title, flip_pair):
    facs = panel["facilitators"]
    names = [f["name"] for f in facs]
    counts = [f["count_share"] for f in facs]
    values = [f["value_share"] for f in facs]
    n = len(facs)
    # top-to-bottom in printed order: printed row 0 sits at the top.
    y = np.arange(n)[::-1]
    h = 0.38

    ax.barh(y + h / 2 + 0.01, counts, height=h, color=C_COUNT, label="Count share")
    ax.barh(y - h / 2 - 0.01, values, height=h, color=C_VALUE, label="Value share")

    for yi, c, v in zip(y, counts, values):
        ax.text(c + 1.0, yi + h / 2 + 0.01, f"{c:.1f}%", va="center", ha="left", fontsize=7, color="0.25")
        ax.text(v + 1.0, yi - h / 2 - 0.01, f"{v:.1f}%", va="center", ha="left", fontsize=7, color="0.25")

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8.5)
    # bold the two facilitators whose rank flips between the metrics
    for lbl in ax.get_yticklabels():
        if lbl.get_text() in flip_pair:
            lbl.set_fontweight("bold")
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of May 2026 (percent)", fontsize=8.5)
    ax.set_title(title, fontsize=10, loc="left")
    ax.grid(True, axis="x", color="0.90", lw=0.6)
    ax.set_axisbelow(True)


def main():
    base = load_panel("table2_base_may2026.json")
    sol = load_panel("table3_solana_may2026.json")

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.0, 4.6))
    draw(axL, base, "Base (corrected split)", flip_pair={"Coinbase (CDP)", "Meridian (mrdn)"})
    draw(axR, sol, "Solana (top five by count)", flip_pair={"Dexter", "Coinbase"})

    handles, labels = axL.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper right", fontsize=8.5, frameon=False,
               bbox_to_anchor=(0.995, 0.985))

    fig.suptitle("Figure 2. The count-versus-value monopolist flip, May 2026", fontsize=12, x=0.5, y=0.985)
    fig.text(0.5, 0.925,
             "The count leader and the value leader are different operators on both chains "
             "(Base: Coinbase vs Meridian; Solana: Dexter vs Coinbase).",
             ha="center", fontsize=8.5, color="0.30")

    fig.tight_layout(rect=(0, 0, 1, 0.90))
    FIG.mkdir(exist_ok=True)
    png = FIG / "fig2_count_value_flip.png"
    pdf = FIG / "fig2_count_value_flip.pdf"
    fig.savefig(png, dpi=200)
    fig.savefig(pdf, metadata={"CreationDate": None})  # suppress PDF timestamp -> deterministic
    plt.close(fig)

    print(f"wrote {png.name} and {pdf.name}")
    for panel in (base, sol):
        print(f"{panel['panel']} panel (facilitator: count_share / value_share, as printed):")
        for f in panel["facilitators"]:
            print(f"   {f['name']:<16} {f['count_share']:>5.1f}% / {f['value_share']:>5.1f}%")


if __name__ == "__main__":
    main()
