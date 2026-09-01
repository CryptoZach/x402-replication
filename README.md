# Replication package: Who Controls Agentic Payments?

Facilitator Concentration, Subsidy Pipelines, and Settlement Accountability in x402.
Zachary Zukowski, Tokenization Systems. Paper dated 2026-08-31.

Every number printed in the paper reproduces from what is here, plus public on-chain data.
`MANIFEST.txt` carries a sha256 and a byte count for every file, so a reader can verify they
received what was deposited, and a citation can pin to bytes rather than to a branch.

## What is here

    exhibits/          the figure build scripts and their committed input tables
    anchors/           dated captures of every external anchor cited
    measurement store  the census, the concentration series and the recompute scripts
    figures/           the three figures as published

## How to reproduce

The identification strategy is stated in full in Section 3.1 of the paper: the settlement
fingerprint is what selects x402 payments out of general USDC transfer activity, and it is
printed precisely rather than described. Section 3.4 states the buyer-cardinality classifier and
Section 5 states the proxy-settlement correction. With those three, the queries here regenerate
the series against Dune's public tables.

Measured cost of the original full measurement: approximately 60 credits of a 4,000-credit
period. Reproducing it is cheap on purpose. That is one of the paper's claims.

## Why the external anchors are captured here rather than linked

Two anchors are bot-walled to automated clients and have weak or absent public archival cover;
one has never been captured by the Internet Archive. For those, this package ships the dated
capture rather than relying on a URL that may not resolve for you. Anchors in this market move
weekly, which Section 9 treats as a measurement problem in its own right.

## What is deliberately not here

The orchestration and capture-attestation apparatus that produced the paper is withheld. That
boundary is Appendix A.5's, not a new one, and none of it bears on the measurement: every number
reproduces from the artifacts here regardless of how the sessions that produced them were
orchestrated.

The conversation record is not withheld either. It is Appendix C of the paper itself, all 43
sessions, in the submitted PDF.

## Provenance

Assembled by `scripts/build_c4_replication_package.py` from a single git ref, by an ENUMERATED
include list rather than by redacting a repository. A denylist that misses something leaks it; a
whitelist that misses something merely omits it, and an omission is recoverable. The assembler
refuses to write this package if any staged byte carries a withheld-matter token, and that gate
has caught a real one.
