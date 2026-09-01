Source-URL: https://github.com/Merit-Systems/x402scan (default branch main); registry package: https://github.com/Merit-Systems/x402scan/tree/main/packages/external/facilitators ; per-facilitator entries: packages/external/facilitators/src/facilitators/*.ts ; liveness check: https://www.x402scan.com
Access-time: 2026-07-02T09:20:00Z
Capture-method: GitHub API tree listing + curl of raw.githubusercontent.com README and registry files; curl -L HEAD-equivalent of x402scan.com (HTTP 200)

Repo metadata (GitHub API): full_name "Merit-Systems/x402scan", default_branch "main", homepage "https://x402scan.com", description "x402 Ecosystem Explorer".

Liveness: curl -L https://www.x402scan.com returned HTTP 200 on 2026-07-02.

packages/external/facilitators/README.md (verbatim extracts):

"# facilitators"

"The `facilitators` package offers a unified, drop-in configuration for all x402 facilitators"

"> As of January 2026, the auto facilitator has been deprecated. Please use any of the other facilitators shown below."

Main repo README.md (verbatim extracts):

"- **facilitators/** - Shared facilitator configuration"

"If you know of another facilitator that is not listed, you can add it to [`facilitators/config.ts`](https://github.com/Merit-Systems/x402scan/blob/main/facilitators/config.ts) and the dashboard will automatically update."

"2. Add the facilitator configuration to the `_FACILITATORS` array in `facilitators/config.ts`:"

Registry contents as of 2026-07-02 (GitHub API tree, machine-readable per-facilitator TypeScript entries under packages/external/facilitators/src/facilitators/): 402104.ts, anyspend.ts, aurracloud.ts, auto.ts, bitrefill.ts, cascade.ts, codenut.ts, coinbase.ts, corbits.ts, daydreams.ts, dexter.ts, figment.ts, fluxa.ts, heurist.ts, index.ts, meridian.ts, mogami.ts, openfacilitator.ts, openmid.ts, openx402.ts, payai.ts, polymer.ts, primer.ts, questflow.ts, relai.ts, thirdweb.ts, treasure.ts, ultravioletadao.ts, virtuals.ts, x402jobs.ts, x402rs.ts, xecho.ts.

Each entry carries facilitator id, metadata (name, docsUrl), facilitator endpoint URL, and per-network settlement addresses with tokens and dateOfFirstTransaction (see thirdweb.ts capture in thirdweb_facilitator.md).

Note: the main README's add-a-facilitator instructions still point to a top-level facilitators/config.ts, but the current tree has no top-level facilitators/ directory; the live machine-readable registry is the packages/external/facilitators package (npm package name "facilitators"). Historical registry path facilitators/config.ts appears to have been restructured into per-facilitator files.
