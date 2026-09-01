# Anchor D5 capture: Google Agent Payments Protocol (AP2)

Source-URL: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol (launch announcement); https://ap2-protocol.org/ (protocol docs); https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/ (stewardship transfer)
Access-time: 2026-07-02T09:11:00Z through 2026-07-02T09:14:00Z (UTC, approx)
Capture-method: curl with browser user agent (HTTP 200 for both Google pages; verbatim text extracted from HTML and JSON-LD) plus WebFetch for ap2-protocol.org (AI-extracted quotes).

## 1. Launch announcement (Google Cloud blog)

Page metadata (verbatim from HTML/JSON-LD):

```
<title>: Announcing Agent Payments Protocol (AP2) | Google Cloud Blog
JSON-LD headline: Announcing Agent Payments Protocol (AP2)
On-page H1: Powering AI commerce with the new Agent Payments Protocol (AP2)
datePublished: 2025-09-16
authors (JSON-LD): Stavan Parikh; Rao Surapaneni
publisher: Google Cloud
```

Launch sentence (verbatim from page body):

> Today, Google announced the Agent Payments Protocol (AP2), an open protocol developed with leading payments and technology companies to securely initiate and transact agent-led payments across platforms. The protocol can be used as an extension of the Agent2Agent (A2A) protocol and Model Context Protocol (MCP).

Mandates definition (verbatim from page body):

> How it works: Establishing trust via mandates and verifiable credentials AP2 builds trust by using Mandates—tamper-proof, cryptographically-signed digital contracts that serve as verifiable proof of a user's instructions. These mandates are signed by verifiable credentials (VCs) and act as the foundational evidence for every transaction. Mandates address the two primary ways a user will shop with an agent: Real-time purchases (human present ): When you ask an agent, "Find me new white running shoes," your request is captured in an initial Intent Mandate.

## 2. Protocol documentation site (ap2-protocol.org, via WebFetch extraction)

- Site title: "AP2 - Agent Payments Protocol Documentation"
- Mandate types in the current docs: Checkout Mandate ("Captures the reference to the specific items and purchase details negotiated between the agent and the merchant") and Payment Mandate ("Authorizes a payment against a specific payment instrument, and is shared with the Credential Provider, Networks and the Merchant Payment Processor").
- Governance note quoted by the docs: "Standardization of the specification will continue within the Agentic Authentication Technical and Payments Technical Working Groups in FIDO."

## 3. Stewardship transfer (blog.google)

Page metadata (verbatim):

```
<title>: Google donates Agent Payments Protocol to FIDO Alliance
datePublished: 2026-04-28T13:00:00+00:00
```

Subtitle (verbatim from page body):

> We're donating Agent Payments Protocol to the FIDO Alliance to support the future of secure, agentic payments.

## Notes

- Launch: Google, September 16, 2025, with 60+ partners.
- The launch blog describes Intent Mandate, Cart Mandate, and Payment Mandate; the current docs (post v0.2) present Checkout Mandate and Payment Mandate. "Mandates" remains the protocol's term for structured, signed payment authorizations in both versions.
- Stewardship moved from Google to the FIDO Alliance on April 28, 2026.
