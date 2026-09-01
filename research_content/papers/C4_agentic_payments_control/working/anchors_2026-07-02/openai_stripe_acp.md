# Anchor D6 capture: OpenAI and Stripe Agentic Commerce Protocol (ACP)

Source-URL: https://stripe.com/blog/developing-an-open-standard-for-agentic-commerce ; https://openai.com/index/buy-it-in-chatgpt/ (via Wayback snapshot http://web.archive.org/web/20260625123158/https://openai.com/index/buy-it-in-chatgpt/) ; https://github.com/agentic-commerce-protocol/agentic-commerce-protocol (repo metadata via api.github.com; governance doc via raw.githubusercontent.com docs/governance.md) ; https://www.agenticcommerce.dev/
Access-time: 2026-07-02T09:13:00Z through 2026-07-02T09:16:00Z (UTC, approx)
Capture-method: curl with browser user agent for Stripe blog (HTTP 200), agenticcommerce.dev (HTTP 200), Wayback snapshot of the OpenAI page (HTTP 200; live openai.com returned 403 to WebFetch), GitHub REST API, and raw governance.md; verbatim text extracted.

## 1. Stripe launch blog

Page metadata (verbatim):

```
<title>: Developing an open standard for agentic commerce
datePublished: 2025-09-29T00:00-06:00
```

Body (verbatim):

> Instant Checkout is powered by the Agentic Commerce Protocol (ACP), a new open standard codeveloped by Stripe and OpenAI that enables programmatic commerce flows between buyers, AI agents, and businesses. It provides a blueprint for how businesses can make their checkouts agent-ready so that customers using AI agents, such as ChatGPT, can buy products directly from where they're discovering them. The ACP specification is available for businesses and AI agents to implement starting today.

## 2. OpenAI announcement (Wayback snapshot of 2026-06-25)

Verbatim extract:

> OpenAI September 29, 2025 Product Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol

Page title: "Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol | OpenAI"

## 3. GitHub repo (api.github.com, retrieved 2026-07-02)

```
description: The Agentic Commerce Protocol (ACP) is an interaction model and open standard for connecting buyers, their AI agents, and businesses to complete purchases seamlessly. The specification is currently maintained by OpenAI and Stripe.
homepage: https://agenticcommerce.dev
created: 2025-09-29T04:09:29Z
pushed: 2026-06-15T23:51:12Z
org: agentic-commerce-protocol
```

## 4. Governance doc (docs/governance.md on main, retrieved 2026-07-02, verbatim)

> ## The Founding Maintainers
>
> OpenAI and Stripe are the Founding Maintainers of ACP. Their role is to steward the early growth of the protocol and its governance structures.

> The TSC is the central governing body responsible for the protocol's evolution,

> TSC seats are appointed by the Founding Maintainers (OpenAI and Stripe) based on the following criteria:

## 5. agenticcommerce.dev (verbatim extract)

> Agentic Commerce Protocol An open standard for programmatic commerce flows between buyers, AI agents, and businesses. Read the docs Open source ACP is open source and community-designed under the Apache 2.0 license.

## Notes

- Launched September 29, 2025 (Stripe blog datePublished; OpenAI page dateline; GitHub org repo created 2025-09-29).
- Stewardship as of 2026-07-02: still OpenAI and Stripe as Founding Maintainers governing via a Technical Steering Committee; NOT donated to an external foundation or standards body (contrast AP2, donated to the FIDO Alliance 2026-04-28). Governance doc frames Founding Maintainer authority as transitional.
