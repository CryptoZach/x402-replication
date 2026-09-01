Source-URL: https://docs.mrdn.finance/
Access-time: 2026-07-02T09:14:00Z
Capture-method: curl -sL of live docs page (verbatim strings grep-verified in raw HTML) plus WebFetch extraction for the MEXC third-party article

VERBATIM STRINGS present in the raw HTML of docs.mrdn.finance (extracted from the embedded MDX/JS payload of the rendered docs):

[Flow comparison diagram labels]
"Traditional x402: Payer Wallet → Recipient Wallet (immediate transfer)" (label pair as rendered)
"Payer Wallet → Recipient Wallet (immediate transfer)"
"Payer Wallet → Meridian Facilitator → Settlement / Bridge → Recipient"

[Feature card]
Card title: "Built-in Fee Management" (icon: percentage)
Card body: "Platform and treasury fee accounting handled inside the facilitator."

[Sibling feature cards on the same overview page]
"Organization Management": "Multi-user organizations with shared payment infrastructure."
"Enhanced Security": "Organization-scoped access control with API key management."

[Tokenomics card linking /tokenomics]
"MRDN token distribution, emissions, and cashback mechanics" (icon: coins, href: /tokenomics)

THIRD-PARTY CASHBACK DESCRIPTION (MEXC Learn, "What is Meridian (MRDN)? Complete Guide to the AI Agent Payment Infrastructure", published October 28, 2025; URL: https://www.mexc.com/learn/article/what-is-meridian-mrdn-complete-guide-to-the-ai-agent-payment-infrastructure/1; quotes obtained via WebFetch model extraction because direct curl returned a 513 byte bot-block stub):

"Users receive cashback rewards paid in MRDN tokens calculated based on total payment amounts processed through the Meridian network."
"The initial cashback rate of 2% decreases exponentially with cumulative transaction volume, following a continuous decay model."
"MRDN's primary utility is delivering cashback rewards to network participants."
"Users receive 2% initial cashback on payments processed through Meridian, paid in MRDN tokens."
"Unlike traditional wallet-to-wallet transfers, Meridian implements a proxy facilitator model where payments flow through an intermediary layer, creating isolated receiver balances with built-in fee management and withdrawal controls."

VERIFIER NOTE (authored): On the docs page the fee phrase appears as the card heading "Built-in Fee Management", title case, with the body sentence above; the lowercase running-text phrase "built-in fee management" appears verbatim in the MEXC third-party description. web.archive.org holds a docs.mrdn.finance snapshot of 2026-02-16 (http://web.archive.org/web/20260216012033/https://docs.mrdn.finance/).
