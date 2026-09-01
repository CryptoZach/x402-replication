Source-URL: https://docs.mrdn.finance/ ; https://docs.mrdn.finance/llms.txt ; https://docs.mrdn.finance/api-reference/endpoint/settle-payment ; archived in-window snapshot https://web.archive.org/web/20260518032039/https://docs.mrdn.finance/api-reference/endpoint/settle-payment
Access-time: 2026-08-05T10:30:00Z (overview), 2026-08-05T10:48:00Z (llms.txt), 2026-08-05T10:52:00Z (May snapshot)
Capture-method: WebFetch of the docs overview; curl of llms.txt (HTTP 200, 7031 bytes); curl of the Wayback snapshot dated 2026-05-18 (HTTP 200, 360113 bytes) with tag-stripped text extraction.

---

## 1. Anchors that re-verify unchanged

Payment flow string (verbatim, source arrows preserved):
"Payer Wallet → Meridian Facilitator → Settlement / Bridge → Recipient"

Fee card (verbatim): heading "Built-in Fee Management", body "Platform and treasury fee accounting handled inside the facilitator."

MRDN token program (verbatim, from llms.txt): "[Tokenomics](https://docs.mrdn.finance/tokenomics.md): $MRDN token distribution, emissions, and cashback mechanics"

The token-program anchor is CONFIRMED. An initial WebFetch of the docs overview did not surface it; the docs index at llms.txt carries it verbatim, and the Wayback CDX shows the /tokenomics page captured on 2026-01-24 and 2026-04-20, so it is long-standing rather than new.

## 2. Non-EIP-3009 settlement paths (THE HALT-3 EVIDENCE)

Current docs index (verbatim, from llms.txt):

"[Non-EIP-3009 payments](https://docs.mrdn.finance/ai-skills/non-eip-3009.md): Step-by-step Meridian integration guide for Permit2-based payment chains"

"[Settle x402 Payment](https://docs.mrdn.finance/api-reference/endpoint/settle-payment.md): Settle an x402 payment with organization-specific authentication. This endpoint supports standard exact EIP-3009 EVM payloads, Circle Gateway batched payloads, and the Permit2 payload used on non-EIP-3009 EVM networks."

"[Execute ERC-20 Permit](https://docs.mrdn.finance/api-reference/endpoint/permit.md): Submit a signed EIP-2612 permit and have the facilitator's signer execute `transferWithPermit` on the Meridian Proxy Facilitator contract."

"[Overview](https://docs.mrdn.finance/api-reference/payment-types/circle-gateway.md): Gas-free, batched USDC nanopayments routed through Circle's Gateway API"

## 3. IN-WINDOW confirmation, archived snapshot dated 2026-05-18

This is the decisive point: the snapshot falls INSIDE the paper's May 2026 concentration window, and already carries the non-EIP-3009 paths. Verbatim from that snapshot:

"For MegaETH, the recommended flow is now Permit2, not the forwarder. New integrations should keep payTo pointed at the facilitator, set paymentRequirements.asset to the ERC-20 token address, approve Permit2 0x000000000022D473030F116dDEE9F6B43aC78BA3, and sign with x402ExactPermit2Proxy 0x402085c248EeA27D92E8b30b2C58ed07f9E20001."

"The USDm forwarder is deprecated and should be kept only for legacy EIP-3009 clients."

"When paymentRequirements.extra.name === "GatewayWalletBatched", this endpoint forwards the request to Circle's Gateway API instead of settling on-chain."

The May snapshot's endpoint navigation already lists "Execute ERC-20 Permit" and the batched "Nanopayments Gateway" group.

---

Verdict 2026-08-05: CONFIRMED as to every anchor the paper cites Meridian for, and HALT-3 TRIGGERED on a separate and more serious point.

The paper's largest value-layer operator (Meridian, 57.2 percent of May value) documented, inside the measurement window, at least three settlement paths that do not emit an EIP-3009 `AuthorizationUsed` event: Permit2, an EIP-2612 `transferWithPermit` path, and Circle Gateway batched settlement. The Gateway path is the consequential one, because it "forwards the request to Circle's Gateway API instead of settling on-chain": a payment routed that way produces no on-chain settlement event on the measured chain at all, so it is absent from BOTH the numerator and the denominator of the coverage statistic, and is not detectable as a gap by the census method.

Scope limits stated honestly. The Permit2 instructions quoted above are network-specific to MegaETH, and the forwarder-adapter discussion is BSC; neither is a chain the paper measures (Base, Polygon, Solana). The Gateway-batched routing is described by payload type rather than by network in the extracted text, so its availability on the measured chains is not established by this capture either way. What this capture establishes is EXISTENCE in-window, not MAGNITUDE on the measured chains. Magnitude is a measurement question that this audit-only pass cannot answer and that the coverage claim depends on. See the register HALT-3 disposition and ANCHOR_SPEC item S-1.
