# C4 June coverage-signal investigation: the 21x non-registry AuthorizationUsed jump

**As-of**: 2026-07-03T23:50:10Z (measured this session against the live Dune store)
**As-of-SHA:** auto
**Subject-paths:** research_content/papers/C4_agentic_payments_control/PAPER.md handoff/workflow_runs/agentic_payments_june_pairing_coverage_2026-07-03/
**Session:** BULK-EXECUTOR (Claude PID 4520; branch session/4520), dispatch D4 Phase 3
**Evidence:** `handoff/workflow_runs/agentic_payments_june_pairing_coverage_2026-07-03/results/june_nonregistry_*.json`; reproductions in `june_cumulative_recompute.py`.

> Reader: run `python3 scripts/claude-code-sync.py` and re-derive from the results JSON before acting. This market moves weekly.

## The signal

Non-registry Base `AuthorizationUsed` events jumped from 346,030 (May) to 7,258,237 (June), a 21.0x rise, now exceeding registry June events (5,467,211). `AuthorizationUsed` (EIP-3009) is a general gasless-USDC primitive, so the a-priori options were (a) an unregistered x402 facilitator (genuine fingerprint decay), (b) a non-x402 gasless-USDC protocol (consumer relayer / meta-transaction class), or (c) indeterminate.

Discriminator that resolves it immediately: June non-registry events-per-authorizer = 7,258,237 / 65,970 = **110**, versus May's 346,030 / 110,831 = **3.1**. May non-registry was near-1:1 organic relayer traffic; June is a machine-grind fleet. The authorizer base FELL (110,831 -> 65,970) while events rose 21x.

## Cluster enumeration (`results/june_nonregistry_top_submitters.json`)

| Cluster | Members | Events | Authorizers | Events/authorizer | Read |
|---|---|---|---|---|---|
| Uniform fleet | 15 addresses (ranks 1-15) | 7,033,614 (96.9%) | ~2,650 each | ~178 | coordinated scripted fleet |
| Organic relayer | 0x25e9775b, 0xa9236f49 | 48,090 | 24,526 / 7,777 | 1.07 / 2.81 | consumer gasless-wallet traffic (knowably not x402) |
| Micro-grind | 0x0b44230e, 0xc4405602, 0x13bfc43f | 30,441 | 51 / 9 / 38 | 224 / 1070 / 247 | tiny grind clusters |

The 15 fleet addresses are extraordinarily uniform: each 468,577 to 469,575 events (within 0.2 percent of each other), each ~2,620 to 2,690 authorizers. That uniformity is a fleet signature (compare the Polygon Facilitator fleet, Section 6: scripted workers within 0.3 percent of each other).

## Fleet classification (`results/june_nonregistry_fleet_profile.json`)

Two discriminators applied to the 15-address fleet:

1. **Transaction-target pattern (the Polygon meta-transaction discriminator, Section 3.3).** 0x833589fcd6edb6e08f4c7c32d4f71b54bda02913 (Base native USDC, Circle) receives 7,036,607 of ~7,037,060 fleet transactions (99.99 percent), from all 15 submitters. The fleet calls USDC DIRECTLY with `transferWithAuthorization` (EIP-3009); it is NOT app-mediated meta-transactions to an application contract. This is the x402 settlement fingerprint.
2. **Value profile.** 7,033,946 transfers, $102,003 total, 7,931 payers, 3,611 payees; median $0.0065, p90 $0.022, max $2,335.63. Dust-valued micro-metering, not commerce-scale payments.

### Verdict: classification (a) with the operator identity open

A coordinated 15-address fleet settling direct USDC via EIP-3009 at micro-metering scale, outside the 112-address registry. Structurally it matches the x402 settlement fingerprint (facilitator-shaped, many-to-many: 7,931 payers to 3,611 payees, direct-USDC gasless settlement), so it is a **genuine fingerprint-decay instance / coverage gap in the COUNT denominator** (option a). It is dust-valued, so it is immaterial to value and to every concentration reading (option b's "consumer metering" flavor also fits the dust value, but the many-to-many facilitator shape and direct-USDC settlement place it structurally in the settlement-fingerprint class regardless of whether its operator markets itself as x402). The OPERATOR is not identifiable from on-chain surfaces (15 unlabeled fleet addresses plus a few negligible 0x4020... helper contracts). NOT HALT-4: the structure is unambiguous; only the operator identity is open.

### Coverage impact (concentration-neutral)

- June registry share of all Base `AuthorizationUsed`: 5,467,211 / 12,725,448 = **43 percent** with the fleet counted; 5,467,211 / 5,691,834 = **96 percent** with the fleet set aside as a single coordinated metering operation.
- The paper's 92.3 percent trailing-30-day coverage figure (Section 3.3) is a spring-2026 (through-May) reading; it is now annotated with its as-of era and the June reading.
- Does NOT affect any May-anchored claim (May non-registry was only 346,030; concentration claims stay May-anchored). No HALT-3.

## Companion signal: settlement-router decline (C3)

The decoded x402 settlement-router path is shrinking: 20,576 settled events in May, 9,019 in June -> 0.70 percent of registry auth events (May) to 0.17 percent (June). The router path is a diminishing source of missed coverage, cutting the opposite way from the fleet. Section 7's "0.3 percent of Base counts" is refreshed to the May/June monthly shares.

## Paper updates applied (verified only)

- **Section 3.3:** 92.3 percent figure annotated with its May-2026 census-window as-of; June coverage reading (43 percent / 96 percent) added with the fleet context; fleet stated as entering no value or concentration claim.
- **Section 7 (fingerprint decay):** router decline (0.70 -> 0.17 percent) plus the June unregistered fleet as the coverage signal (7.0M events, 96.9 percent of non-registry, direct-USDC fingerprint, dust value, unidentifiable operator).
- **Section 11:** fingerprint-decay watch item now has the June fleet reading.
- Attribution set of record (`dbc97a9d22f7`) NOT modified. Concentration/HHI/share claims unchanged (May-anchored).

## Routed to CANONICAL-WRITER (handoff-back; no invented IDs)

The 15-address fleet is a coverage-gap and upstream registry-contribution candidate; 0x1892f72f is a confirmed small registry self-hopper. Entity identification and any ENTITY_PROFILES / registry-contribution entries are CANONICAL-WRITER work. See the closing handoff-back memo.
