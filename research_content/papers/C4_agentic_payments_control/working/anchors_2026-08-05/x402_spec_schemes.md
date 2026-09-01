Source-URL: https://raw.githubusercontent.com/coinbase/x402/main/specs/schemes/exact/scheme_exact_evm.md ; https://raw.githubusercontent.com/coinbase/x402/main/specs/schemes/exact/scheme_exact_svm.md ; https://api.github.com/repos/coinbase/x402/commits?path=specs/schemes/exact/scheme_exact_evm.md
Access-time: 2026-08-05T10:29:00Z (EVM, commit history), 2026-08-05T10:44:00Z (SVM)
Capture-method: WebFetch of the raw spec files and the GitHub commits API; curl of the SVM spec (HTTP 200, 8972 bytes).

---

## exact-EVM: THREE asset transfer methods (this is the material change)

The current exact-EVM scheme documents three settlement methods, not one:

1. EIP-3009, via `transferWithAuthorization`
2. Permit2, via `permitWitnessTransferFrom` through the x402ExactPermit2Proxy
3. ERC-7710, via smart contract delegation through `redeemDelegations`

Summary-table label for EIP-3009 (verbatim): "Recommended (Simplest, truly gasless)"

Default-selection rule (verbatim): "If no `assetTransferMethod` is specified in the payload, the implementation should prioritize `eip3009` (if compatible) and then `permit2`."

## Dating the change (GitHub commits API, committer dates)

- Permit2 added: 2026-01-08, "Feature: Add Permit2 Support to Exact EVM Scheme (#769)"
- ERC-7710 added: 2026-03-13, "Add spec for ERC-7710 support to the exact_evm scheme (#732)"
- Python Permit2 + gas-sponsorship extensions: 2026-03-19 (#1686)

## exact-SVM (verbatim excerpts)

"3. SPL Token or Token-2022 TransferChecked"

"the `extra` field in the requirements contains a **feePayer** which is the public address of the identity that will pay the fee for the transaction. This is typically the facilitator."

---

Verdict 2026-08-05: CONFIRMED as to the mechanics the paper describes, with a MATERIAL currency change. Both non-EIP-3009 transfer methods were merged into the spec BEFORE the paper's May 2026 concentration window (Permit2 on 2026-01-08; ERC-7710 on 2026-03-13), not after it. EIP-3009 remains the recommended default, so the paper's Section 2.1 description of the dominant path stays accurate, but the paper's coverage statistic is computed over EIP-3009 `AuthorizationUsed` events and the spec has admitted two settlement paths that emit no such event since January 2026. See the HALT-3 disposition in the register and the Meridian capture (meridian_docs.md) for the operator-level in-window evidence.
