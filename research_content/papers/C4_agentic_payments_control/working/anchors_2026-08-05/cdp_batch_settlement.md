Source-URL: https://www.x402.org/writing/x402-batch-settlement
Access-time: 2026-08-05T10:34:00Z
Capture-method: WebFetch of the live protocol blog post.

---

Verbatim, current page:

"The buyer opens a session by committing funds (for example an EVM escrow or channel)."
"Every HTTP interaction includes a cryptographic voucher, a cumulative 'I owe you' that increments with usage."
"The seller settles onchain in bulk. Many logical payments are compressed into a single transaction."

Publication: May 11, 2026. Authors: Cam Whiteside (Cloudflare), Carson Roscoe, Conner Swenberg, Josh Nickerson, Philippe d'Argent (Coinbase).

---

Verdict 2026-08-05: CONFIRMED, unchanged in substance. All three design elements the paper describes (session-start escrow pre-funding, per-call signed vouchers, single bulk on-chain redemption) re-verify, as does the observability consequence the paper draws from them, that many logical payments compress into one transaction. The page's phrasing differs from the sentences quoted in the 2026-07-02 register, but those were quotations of the PAPER's prose being checked against the source, not quotations of the source, so this is not a source change.
