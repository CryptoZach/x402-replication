# C4 exhibits (2026-07-03): two store-reproducible figures

Two figures for the C4 agentic-payments paper (AFA 2027 generative-AI special
session). Both reproduce from the committed measurement store with zero live
queries. This directory is the build package; PAPER.md is NOT edited here (figure
wiring happens at the later render/judgment pass; see `captions_and_placement.md`).

Built 2026-07-03 (session/41277, BULK-EXECUTOR, dispatch
`handoff/dispatch/c4_exhibits_build_2026-07-03.md`).

## Contents

```
fig1_base_monthly_series.py     Figure 1 build script (reads the committed base monthly store)
fig2_count_value_flip.py        Figure 2 build script (reads the two transcribed table files)
data/table2_base_may2026.json   Table 2 (Base, corrected) transcribed verbatim from PAPER.md
data/table3_solana_may2026.json Table 3 (Solana, top five) transcribed verbatim from PAPER.md
figures/fig1_base_monthly_series.{png,pdf}
figures/fig2_count_value_flip.{png,pdf}
```

## Reproduce

From the repo root (scripts resolve their own paths; run from anywhere):

```
python3 research_content/papers/C4_agentic_payments_control/working/exhibits_2026-07-03/fig1_base_monthly_series.py
python3 research_content/papers/C4_agentic_payments_control/working/exhibits_2026-07-03/fig2_count_value_flip.py
```

Output is deterministic: fixed figsize and dpi, no timestamps embedded (the PDF
CreationDate is suppressed). Verified 2026-07-03: re-running both scripts produces
byte-identical PNG and PDF for both figures (stronger than the acceptance bar of
byte-stable-except-library-metadata). matplotlib 3.10.8, numpy 2.4.3.

## Data provenance

### Figure 1 input

- **Path:** `handoff/workflow_runs/agentic_payments_june_refresh_2026-07-03/results/base_monthly.json`
  (committed; the June-final interim-refresh run archive, ai_workflow_log row 9).
- **Extraction method:** the script reads the JSON rows directly (keys
  m / transfers / usd / buyers / sellers), filters to the Table-1 months
  (2025-10 through 2026-06 final), and computes average payment size as usd/transfers.
- **Months plotted:** 2025-10, 2025-11, 2025-12, 2026-01, 2026-02, 2026-03,
  2026-04, 2026-05, 2026-06 (the nine months printed in PAPER.md Table 1; earlier
  2025 micro-scale months live in the replication archive and are omitted from the paper table too).

### Figure 2 input

- **Paths:** `data/table2_base_may2026.json` and `data/table3_solana_may2026.json`
  (committed here; each transcribed VERBATIM from the printed PAPER.md table named in its
  `_provenance` field). These are the of-record surface for the May 2026 snapshot, which
  remains May-anchored (the corrected Meridian split and the top-five Solana caption).
- **Extraction method:** the script reads count_share and value_share as printed; the raw
  payments / usd columns are carried in the JSON for cross-check but not plotted.

## Cross-checks against the printed tables (HALT-1 discipline)

Every plotted value is asserted against PAPER.md as printed BEFORE anything is drawn; a
source-vs-printed disagreement aborts the build (it is a finding, not a styling problem).

### Figure 1 (vs PAPER.md Table 1, lines 125-133)

`fig1_base_monthly_series.py` asserts, for all nine months: payments == printed exactly;
distinct buyers == printed exactly; round(raw usd) == printed USD (raw) column;
round(usd/transfers, 2) == printed Avg $/payment. Verified pass 2026-07-03:

| Month | Payments | Distinct buyers | Computed avg | Printed avg |
|---|---|---|---|---|
| 2025-10 | 4,065,328 | 175,237 | 0.9754 | 0.98 |
| 2025-11 | 64,264,312 | 118,767 | 0.4339 | 0.43 |
| 2025-12 | 43,037,218 | 46,800 | 0.0759 | 0.08 |
| 2026-01 | 12,130,123 | 14,588 | 0.0993 | 0.10 |
| 2026-02 | 1,419,951 | 22,649 | 1.4555 | 1.46 |
| 2026-03 | 1,820,877 | 14,845 | 1.2503 | 1.25 |
| 2026-04 | 2,304,609 | 38,631 | 0.8413 | 0.84 |
| 2026-05 | 3,041,318 | 110,766 | 0.3387 | 0.34 |
| 2026-06 | 5,826,498 | 48,343 | 0.1180 | 0.12 |

USD (raw) is plotted only through the average; the raw column itself (3,965,328 ... 687,524)
also matches the store to the rounded dollar, checked in the same assertion.

### Figure 2 (vs PAPER.md Table 2 line 145 and Table 3 line 162)

The two data files transcribe the printed count share and value share verbatim; the script
guards that each panel's count shares and value shares each sum to a plausible ~100 percent
(Base 100.0 / 100.0; Solana top-five 99.8 count / 99.8 value, the residual being the
approximately 172 USD of omitted sub-top-five facilitators noted in the Table 3 caption).
Plotted values, exactly as printed:

- Base: Coinbase (CDP) 75.6 / 25.8; fluxa 16.1 / 8.7; payAI 5.9 / 1.7; Meridian (mrdn) 0.4 / 57.2; relai 0.4 / 4.4; all others 1.6 / 2.2.
- Solana: Dexter 51.8 / 15.0; Coinbase 38.5 / 66.5; payAI 4.6 / 1.8; corbits 2.9 / 0.1; relai 2.0 / 16.4.

## Annotation-scope note (Figure 1)

The dispatch listed three candidate annotations "only if factual and printed-table-consistent":
November grind peak, February trough, and the 2026-03-04 rebate activation. The first two are
directly readable from Table 1 (the Base payments maximum and minimum) and are annotated. The
rebate activation is a POLYGON event (Polygon Labs 2026a; the $1M gas-subsidy program, PAPER.md
line 204 and 393) and does not drive the Base series shape; annotating it on a Base-only chart
would misattribute the Base rebuild, so it is deliberately omitted from Figure 1. If a Polygon
fleet exhibit is built later, the rebate date belongs there.

## Alt text

- **Figure 1.** Two stacked line panels of the Base registry-facilitator monthly series,
  October 2025 through June 2026. The top panel, on a logarithmic count axis, shows payments
  rising to a November 2025 peak of 64.3 million (labeled the machine-grind era, 541 events per
  distinct buyer), falling to a February 2026 trough of 1.42 million, then rebuilding through
  June; distinct buyers track a similar but shallower path from about 175,000 down to roughly
  14,600 and back toward 110,000 in May before easing. The bottom panel plots average payment
  size in US dollars on a linear axis: 0.98 dollars in October, collapsing to 0.08 by December
  in the dust-value grind era, recovering to a 1.46-dollar February high as residual usage turns
  more substantive, then declining to 0.12 by June as sub-dime micropayment traffic returns.

- **Figure 2.** Two horizontal paired-bar panels of May 2026 facilitator shares, count share in
  blue and value share in red, showing the count-versus-value monopolist flip. In the Base panel
  (corrected split), Coinbase holds a 75.6 percent count share but only a 25.8 percent value share,
  while Meridian holds a 0.4 percent count share but a 57.2 percent value share: the count leader and
  the value leader are different operators, and their bars invert. In the Solana panel (top five by
  count), Dexter leads counts at 51.8 percent but holds 15.0 percent of value, while Coinbase holds
  38.5 percent of counts and 66.5 percent of value: the same flip replicates with different operators.
  The flipping pair in each panel is bold in the axis labels.
