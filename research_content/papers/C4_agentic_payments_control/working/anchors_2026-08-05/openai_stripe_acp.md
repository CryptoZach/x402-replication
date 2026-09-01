Source-URL: https://stripe.com/blog/developing-an-open-standard-for-agentic-commerce ; https://openai.com/index/buy-it-in-chatgpt/ (live; bot-walled) ; https://github.com/agentic-commerce-protocol/agentic-commerce-protocol (MAINTAINERS.md)
Access-time: 2026-08-05T10:37:00Z (Stripe), 2026-08-05T10:41:00Z (repo)
Capture-method: WebFetch of the Stripe blog; `gh api` for the repository metadata and MAINTAINERS.md (base64-decoded); curl of the OpenAI post returned HTTP 403 to scripted clients.

---

## Stripe blog (verbatim)

"Instant Checkout is powered by the Agentic Commerce Protocol (ACP), a new open standard codeveloped by Stripe and OpenAI"

Publication: September 29, 2025.

## ACP repository governance (THE CHANGE)

The 2026-07-02 capture recorded a `governance.md` reading "OpenAI and Stripe are the Founding Maintainers of ACP", with a Technical Steering Committee framed as transitional.

That file no longer exists under that name. The repository root now carries `MAINTAINERS.md`, whose complete body is (verbatim):

# Maintainers

Below are the current maintainers of the Agentic Commerce Protocol.

## Lead maintainers

- OpenAI
- Stripe
- Meta

Repository description (verbatim, GitHub API): "The Agentic Commerce Protocol (ACP) is an interaction model and open standard for connecting buyers, their AI agents, and businesses to complete purchases seamlessly. The specification is currently maintained by OpenAI and Stripe."

---

Verdict 2026-08-05: CONTRADICTED (governance currency). Two changes since 2026-07-02: the governance file was renamed to MAINTAINERS.md and dropped the "Founding Maintainers" framing, and a third lead maintainer, Meta, was added. ACP remains outside a foundation, so the paper's larger contrast with AP2's FIDO donation still holds, but the paper's Section 2.4 parenthetical "still under its founding maintainers' governance as of mid-2026" is no longer accurate: the maintainer set is no longer the founding pair. Note the repository's own one-line description still says "maintained by OpenAI and Stripe" and now contradicts its MAINTAINERS.md; cite the file, not the description.
