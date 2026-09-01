Source-URL: https://portal.thirdweb.com/payments/x402/facilitator (primary docs); corroborating registry entry: https://raw.githubusercontent.com/Merit-Systems/x402scan/main/packages/external/facilitators/src/facilitators/thirdweb.ts
Access-time: 2026-07-02T09:22:30Z
Capture-method: curl of portal.thirdweb.com page (512KB HTML, tags stripped via python regex); curl of raw.githubusercontent.com registry file

thirdweb docs, page "x402 Facilitator" (verbatim, source punctuation preserved):

"x402 Facilitator The facilitator is a service that handles verifying and submitting x402 payments. It uses your own server wallet and leverages EIP-7702 to submit transactions gaslessly. The thirdweb facilitator is compatible with any x402 backend and middleware libraries like x402-hono , x402-next , and more."

"How It Works Verification - Validates payment signatures and requirements Settlement - Submits the payment transaction on-chain Gasless - Uses EIP-7702 for gasless transactions Your Wallet - Uses your own server wallet for receiving payments You can view all transactions processed by your facilitator in your project dashboard."

Configuration (verbatim from code sample comments): "// Required: Your server wallet address that will execute transactions // get it from your project dashboard serverWalletAddress: "0x1234567890123456789012345678901234567890" ,"

Chain support (verbatim): "Chain and token support The thirdweb x402 client/server stack supports payments on 170+ EVM chains ."

x402scan registry entry for thirdweb (Merit-Systems/x402scan, packages/external/facilitators/src/facilitators/thirdweb.ts, fetched 2026-07-02): facilitator URL 'https://api.thirdweb.com/v1/payments/x402'; docsUrl 'https://portal.thirdweb.com/payments/x402/facilitator'; addresses on Network.BASE list ten distinct settlement addresses (0x80c08de1a05df2bd633cf520754e40fde3c794d3 dateOfFirstTransaction 2025-10-07; 0xaaca1ba9d2627cbc0739ba69890c30f95de046e4, 0xa1822b21202a24669eaf9277723d180cd6dae874, 0xec10243b54df1a71254f58873b389b7ecece89c2, 0x052aaae3cad5c095850246f8ffb228354c56752a, 0x91ddea05f741b34b63a7548338c90fc152c8631f, 0xea52f2c6f6287f554f9b54c5417e1e431fe5710e, 0x3a5ca1c6aa6576ae9c1c0e7fa2b4883346bc5aa0, 0x7e20b62bf36554b704774afb0fcc0ae8f899213b, 0xd88a9a58806b895ff06744082c6a20b9d7184b0f, all dateOfFirstTransaction 2025-11-20) plus one Network.POLYGON address (0x80c08de1a05df2bd633cf520754e40fde3c794d3, 2025-10-07).

Notes:
- thirdweb's own docs describe settlement executed from each customer's OWN server wallet ("your server wallet address that will execute transactions", obtained from the customer's project dashboard), i.e., per-customer/per-project submitter wallets, not a single operator-owned submitter set.
- thirdweb publishes no list of its facilitator submitter addresses in its docs; the address list above is x402scan's empirically observed set (with first-transaction dates), consistent with "no public submitter set" published by the operator.
