Source-URL: https://github.com/coinbase/x402 (repo, default branch main, pushed_at 2026-06-25T19:49:26Z); raw files: https://raw.githubusercontent.com/coinbase/x402/main/specs/schemes/exact/scheme_exact_evm.md ; https://raw.githubusercontent.com/coinbase/x402/main/specs/schemes/exact/scheme_exact_svm.md ; https://raw.githubusercontent.com/coinbase/x402/main/specs/x402-specification-v1.md
Access-time: 2026-07-02T09:16:30Z
Capture-method: curl of raw.githubusercontent.com files on branch main

=== specs/schemes/exact/scheme_exact_evm.md (verbatim extracts) ===

"# Scheme: `exact` on `EVM`"

"The `exact` scheme on EVM executes a transfer where the Facilitator (server) pays the gas, but the Client (user) controls the exact flow of funds via cryptographic signatures."

AssetTransferMethod table: "| **1. EIP-3009**     | Tokens with native `transferWithAuthorization` (e.g., USDC). | **Recommended** (Simplest, truly gasless).     | One-time use |" plus "2. Permit2" ("Universal Fallback") and "3. ERC-7710" ("Smart Account Option").

"If no `assetTransferMethod` is specified in the payload, the implementation should prioritize `eip3009` (if compatible) and then `permit2`."

"The `eip3009` asset transfer method uses the `transferWithAuthorization` function directly on token contracts that support it."

"- `signature`: The 65-byte signature of the `transferWithAuthorization` operation."

"Settlement is performed via the facilitator calling the `transferWithAuthorization` function on the `EIP-3009` compliant contract with the `payload.signature` and `payload.authorization` parameters from the `PAYMENT-SIGNATURE` header."

=== specs/x402-specification-v1.md (verbatim extracts; explicit EIP-712 language) ===

"| `signature`     | `string` | EIP-712 signature for authorization |"
"| `authorization` | `object` | EIP-3009 authorization parameters   |"

"The "exact" scheme uses EIP-3009 (Transfer with Authorization) to enable secure, gasless transfers of specific amounts of ERC-20 tokens."

"1. **Signature Validation**: Verify the EIP-712 signature is valid and properly signed by the payer"

"Settlement is performed by calling the `transferWithAuthorization` function on the ERC-20 contract with the signature and authorization parameters provided in the payment payload."

=== specs/schemes/exact/scheme_exact_svm.md (verbatim extracts) ===

"# Exact Payment Scheme for Solana Virtual Machine (SVM) (`exact`)"

"This scheme facilitates payments of a specific amount of an SPL token on the Solana blockchain."

"2.  **Resource Server** responds with a payment required signal containing `PaymentRequired`. Critically, the `extra` field in the requirements contains a **feePayer** which is the public address of the identity that will pay the fee for the transaction. This is typically the facilitator."

"4.  **Client** signs the transaction with their wallet. This results in a partially signed transaction (since the signature of the facilitator that will sponsor the transaction is still missing)."

"12. **Facilitator Server** provides its final signature as the `feePayer` and submits the now fully-signed transaction to the Solana network."

Facilitator Verification Rules (MUST) extracts:
"  3. SPL Token or Token-2022 TransferChecked"
"- The configured fee payer address MUST NOT appear in the `accounts` of any instruction in the transaction."
"- The fee payer MUST NOT be the `authority` for the TransferChecked instruction."
"- The TransferChecked program MUST be either `spl-token` or `token-2022`."
"- The `amount` in TransferChecked MUST equal `PaymentRequirements.amount` exactly."

Notes: spec files listed under specs/ in coinbase/x402 include x402-specification-v1.md, x402-specification-v2.md, schemes/exact/scheme_exact_evm.md, schemes/exact/scheme_exact_svm.md, schemes/upto/, and schemes/batch-settlement/ (batch_settlement.md, batch_settlement_cloudflare.md). The current EVM scheme doc (V2 era) adds Permit2 and ERC-7710 asset-transfer methods alongside EIP-3009; EIP-3009 remains the recommended default.
