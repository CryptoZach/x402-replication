Source-URL: https://a16zcrypto.com/posts/article/ai-agent-payments-honest-number/
Access-time: 2026-07-02T09:14:00Z
Capture-method: curl -sL of live page; text extracted from raw HTML; dates from embedded JSON-LD

Primary source located: a16z crypto, "The honest number behind AI agent payments", by Noah Levine. JSON-LD datePublished: 2026-03-11T17:00:48Z; dateModified: 2026-06-23T17:25:26Z.

VERBATIM EXCERPTS (extracted from raw HTML):

[Opening: the three numbers]
AI agents are starting to buy things. But how much? The numbers are inconsistent. Bloomberg reported that AI agents made $24 million in payments over a 30-day period, citing data from x402.org . Allium ’s onchain data shows roughly $3 million over the same period. Filter out wash trades and the estimate shrinks further. The gap tells you how early-stage even the measurement infrastructure is.

[The strict-filter figure and its owner]
Lucas Shin, an analyst at Artemis Analytics, built a wash trading filter for x402 volume, flagging wallets that repeatedly transacted with themselves or cycled funds between addresses. Applied over the same 30-day period, the adjusted number is $1.6 million. $24 million reported. $3 million onchain. $1.6 million after removing wash trades.

[Framing]
$1.6 million is not a big number. But the infrastructure being built around it is.

[Data provenance endnote]
I pulled the data for this article from Allium , an onchain analytics provider with an x402 endpoint. Total research cost: $0.47.

VERIFIER NOTE (authored): The $3 million 30-day figure is Allium onchain data as pulled and reported by a16z crypto ("Allium's onchain data shows roughly $3 million over the same period."; data pulled from agents.allium.so). The $1.6 million strict-filter figure is attributed to Lucas Shin of Artemis Analytics (wash trading filter), not to Allium. No Allium-published research post carrying either estimate was found on allium.so or its research hub; the phrase "real agentic volume" does not appear in the a16z article. Bloomberg's $24 million headline figure (citing x402.org) is the number both estimates deflate.
