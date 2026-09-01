Source-URL: https://www.coinbase.com/developer-platform/discover/launches/x402 (live page 403s to non-browser clients; captured via Wayback snapshot http://web.archive.org/web/20250512161925/https://www.coinbase.com/developer-platform/discover/launches/x402)
Access-time: 2026-07-02T09:11:30Z
Capture-method: curl of web.archive.org id_ raw snapshot (timestamp 20250512161925), HTML tags stripped via python regex

Page title: "Introducing x402: a new standard for internet-native payments | Coinbase"

Verbatim body extract (source punctuation preserved):

Introducing x402: a new standard for internet-native payments
May 6, 2025
By: Erik Reppel, Nemil Dalal, Dan Kim

TL;DR: Coinbase is launching x402, a payment protocol that enables instant stablecoin payments directly over HTTP. It allows APIs, apps, and AI agents to transact seamlessly, unlocking a faster, automated internet economy.

"At Coinbase, we're addressing exactly this challenge by introducing x402 : an open standard that leverages the original HTTP "402 Payment Required" status code to embed stablecoin payments directly into web interactions."

"Erik Reppel, Head of Engineering at Coinbase Developer Platform and co-author of the x402 whitepaper , captures the vision behind this initiative: "We built x402 because the internet has always needed a native way to send and receive payments—and stablecoins finally make that possible.""

"x402 is launching alongside leading collaborators including AWS, Anthropic, Circle and NEAR , who share our belief in an open, programmable internet economy."

Flow description (verbatim): "Client (AI agent or app) requests access to an x402-enabled HTTP server with a resource that it needs (e.g. GET /api). Server replies with a 402 Payment Required status, including payment details (e.g., price, acceptable tokens). Client sends a signed payment payload using a supported token (like USDC ) through a standard HTTP header. Client retries the request, now including the X-PAYMENT header with the encoded payment payload. Payment facilitator (like the Coinbase x402 Facilitator service) verifies and settles the payment onchain, and fulfills the request. Server returns the requested data to the client, including an X-PAYMENT-RESPONSE header confirming success of the transaction."
