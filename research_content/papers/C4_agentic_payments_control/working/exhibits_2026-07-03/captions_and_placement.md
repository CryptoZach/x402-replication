# C4 figures: proposed captions and manuscript placement

**As-of:** 2026-07-03T00:00:00Z (build session/41277, BULK-EXECUTOR)
**Subject-paths:** research_content/papers/C4_agentic_payments_control/PAPER.md
**For:** the later render/judgment pass that wires the two figures into PAPER.md. This memo
does NOT edit PAPER.md; it proposes caption text and placement for that pass. Re-verify the
Table 1/2/3 values against the CURRENT manuscript before wiring (the concentration snapshot is
May-anchored and stable, but confirm no re-measurement pass has advanced the tables).

Both figures build from `working/exhibits_2026-07-03/` and reproduce from the committed store;
provenance and cross-checks are in that directory's `README.md`.

---

## Figure 1 (Base monthly series)

- **Placement:** Section 4.1 ("Monthly series: boom, bust, rebuild"), immediately after Table 1
  (PAPER.md line 133) and before the paragraph beginning "The shape documents a boom, bust, and
  rebuild" (line 135). The figure is the visual companion to that table and that paragraph.
- **Source line (house standard):** "Base registry-facilitator submitted USDC transfers,
  2025-10 through 2026-06 final. Reproduces from the committed measurement store (Appendix B);
  build script working/exhibits_2026-07-03/fig1_base_monthly_series.py."
- **Proposed caption:**

> **Figure 1. Base monthly series: boom, bust, rebuild.** Registry-facilitator submitted USDC
> transfers on Base, October 2025 through June 2026. Top panel: payments and distinct buyers on a
> logarithmic count axis. Payments peak in November 2025 at 64.3 million (the memecoin and
> leaderboard grind era, 541 events per distinct buyer), fall to a February 2026 trough of 1.42
> million, then rebuild through June. Bottom panel: average payment size, which collapses to 0.08
> dollars in the December dust-value grind, recovers to a 1.46-dollar February high as residual
> usage turns more substantive, and settles at 0.12 dollars by June as sub-dime micropayment
> traffic returns. June 2026 is a complete calendar month in this series but is excluded from all
> concentration claims, which remain anchored to the validated May 2026 snapshot.

## Figure 2 (count-versus-value flip)

- **Placement:** Section 4.2 ("May 2026 snapshot: two layers, two monopolists"), after Table 3
  (PAPER.md line 170) and before or alongside the paragraph beginning "Cross-chain May totals"
  (line 174). It sits below both tables so the reader meets the numbers first, then the picture.
- **Source line (house standard):** "May 2026 facilitator shares. Base from Table 2 (corrected
  split); Solana from Table 3 (top five by count). Build script
  working/exhibits_2026-07-03/fig2_count_value_flip.py."
- **Proposed caption:**

> **Figure 2. The count-versus-value monopolist flip, May 2026.** Paired horizontal bars of count
> share (blue) and value share (red) per facilitator. Base panel: the corrected split, with
> Meridian measured at its external-seller leg (Section 5). Coinbase owns the message layer at a
> 75.6 percent count share but a 25.8 percent value share, while Meridian owns the value layer at a
> 0.4 percent count share but a 57.2 percent value share; the two operators' rank positions swap
> entirely between the metrics. Solana panel: the top five facilitators by count (facilitators
> outside the five contribute approximately 172 dollars in May and are omitted). The flip replicates
> with different operators, Dexter carrying counts (51.8 percent) and Coinbase carrying dollars
> (66.5 percent), evidence that the flip is structural to the market rather than an artifact of one
> operator's design.

---

## Notes for the wiring pass

1. **Figure numbering.** The paper is currently table-only; if any figure is added earlier than
   Section 4, renumber. As of this build the two figures are the only figures, so Figure 1 and
   Figure 2 are correct.
2. **Rebate annotation deliberately absent from Figure 1.** The 2026-03-04 Polygon gas-rebate
   activation is a Polygon-layer event and does not drive the Base series; it is not annotated on the
   Base chart (README annotation-scope note). Do not add it during wiring.
3. **Format.** PDF is the vector form for the manuscript build; PNG is for the site and quick review.
   Both are in `figures/`.
4. **Re-measurement dependency.** Phase C (the May-to-July re-measurement pass) may extend Tables 1
   to 4 and move the concentration anchor to a fresher full month. If that lands before wiring,
   rebuild both figures against the refreshed store and printed tables (the scripts self-check against
   the printed values and will abort on any mismatch, so a stale figure cannot wire silently).
