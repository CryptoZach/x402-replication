Source-URL: https://www.x402.org/writing/x402-batch-settlement (announcement) ; https://raw.githubusercontent.com/coinbase/x402/main/specs/schemes/batch-settlement/batch_settlement.md (scheme spec in coinbase/x402)
Access-time: 2026-07-02T09:19:00Z
Capture-method: WebFetch of x402.org announcement; curl of raw.githubusercontent.com spec file

=== Announcement: "Introducing x402 Batch Settlement: High-velocity Agentic Commerce" ===
Date: May 11, 2026. Authors: Cam Whiteside (Cloudflare), Carson Roscoe (Coinbase), Conner Swenberg (Coinbase), Josh Nickerson (Coinbase), Philippe d'Argent (Coinbase).

Verbatim extracts:
"The buyer opens a session by committing funds (for example an EVM escrow or channel)."
"Every HTTP interaction includes a cryptographic voucher, a cumulative 'I owe you' that increments with usage."
"The seller verifies these vouchers via simple signature math, with no chain lookups required during the request, and serves the resource immediately."
"The seller settles onchain in bulk. Many logical payments are compressed into a single transaction."
"Value moves onchain only when it is economically optimal, amortized across hundreds or thousands of interactions."
"Support for the batch-settlement machinery is currently available in the TypeScript and Go SDKs, with Python support in development."

=== Spec: coinbase/x402 specs/schemes/batch-settlement/batch_settlement.md (verbatim extracts) ===

"`batch-settlement` is a payment scheme in which the client provides a cryptographic payment commitment at request time, but the transfer of value is not executed synchronously during that request. The commitment is accepted, access is granted immediately, and financial settlement occurs later through a process defined by the network binding."

"For `exact` and `upto`, verification and settlement happen in a single pass: the commitment is validated, a transaction is broadcast, and value has moved. The settlement result contains an on-chain transaction hash."

"For `batch-settlement`, verification confirms the commitment is valid, but settlement stores it rather than executing a transfer. The settlement result contains a commitment identifier, but value moves later, through the network binding's redemption process."

Capital-backed model: "The client's commitment is backed by on-chain capital committed before or during the session such as pre-funded escrow, a payment channel, or a delegated authorization against a wallet balance."

Use case, escrow-backed micropayments: "An AI agent pre-funds an on-chain escrow at session start. Each sub-cent API call produces a signed voucher drawn against that balance. The provider accumulates vouchers and redeems them in a single on-chain transaction at session end, keeping per-request gas cost to zero."

Lifecycle: "1. **Commit.** The client produces a cryptographic payment commitment and attaches it to the request. ... 2. **Accumulate.** The network retains the commitment in a voucher store, channel state, account ledger, or billing system. ... 3. **Redeem.** Value is transferred out of band through an on-chain contract call, a channel close, a fiat batch invoice, or any rail the network defines."

Notes:
- Repo also contains specs/schemes/batch-settlement/batch_settlement_cloudflare.md (a Cloudflare network binding).
- Attribution nuance: the announcement is published on x402.org (the protocol's own site) and the spec lives in the coinbase/x402 repo; announcement authors are four Coinbase staff plus one Cloudflare staff member. Secondary coverage (Cointelegraph, May 2026, "Coinbase Launches x402 Batch Settlement to Advance AI Payments") frames it as Coinbase-launched. Calling it "the announced CDP batch-settlement scheme" is directionally supported (Coinbase-announced, Coinbase-spec-hosted) but the spec itself is chain-binding-generic and co-authored with Cloudflare.
- Per-payment on-chain observability removal is directly supported: exact/upto settlement results carry an on-chain transaction hash per payment; batch-settlement results carry only a commitment identifier and "Many logical payments are compressed into a single transaction."
