# Anchor D7 capture: Circle USDC freeze (access denial) authority

Source-URL: https://6778953.fs1.hubspotusercontent-na1.net/hubfs/6778953/Blog%20Posts/Circle%20Stablecoin%20Access%20Denial%20Policy_pdf.pdf (Circle Stablecoin Access Denial Policy, the policy PDF linked from Circle's USDC Terms) ; https://www.circle.com/legal/usdc-terms
Access-time: 2026-07-02T09:13:00Z (usdc-terms via WebFetch) and 2026-07-02T09:14:00Z (policy PDF via curl, HTTP 200, 94,176 bytes, 2 pages), UTC, approx
Capture-method: curl of the policy PDF with pypdf text extraction; curl plus WebFetch of the USDC Terms page.

## 1. Circle Stablecoin Access Denial Policy (PDF, verbatim)

> Circle Internet Financial LLC
>
> Circle Stablecoin Access Denial Policy
>
> Circle has the ability to block individual addresses from sending and receiving Circle Stablecoin on every blockchain to which Circle Stablecoin is issued. In this document, this ability is referred to as "access denial." When an address is denied access, it can no longer send or receive Circle Stablecoin and all of the Circle Stablecoin controlled by that address is blocked and cannot be transferred on-chain. It is not possible to deny access to individual Circle Stablecoin tokens. This Policy sets forth Circle's policy on access denial to individual addresses.

> 2. Policy Statement
>
> Circle will not deny access to individual addresses, other than in circumstances that strictly conform to the requirements set forth under Part 3, Policy Exceptions.

> 3. Policy Exceptions
> 1. Circle will accept and consider a request for an exception to its policy against access denial where Circle determines, in its sole discretion, that failure to grant a denial of access request presents a threat to the security, integrity, or reliability of the Circle Stablecoin network; for example, security breaches that compromise Circle Stablecoin privileged keys (e.g., minter private key) and result in unauthorized Circle Stablecoin being issued from such compromise.
> 2. Circle will block individual addresses in order to comply with a law, regulation, or legal order from a duly recognized U.S. or French authorized authority, U.S. or French court of competent jurisdiction, or other governmental authority with jurisdiction over Circle. Circle reserves all rights to object to an access denial order that presents a threat to Circle Stablecoin or that Circle determines is objectionable.

> 4. Reversals
> Circle may revert the access denial of an individual address upon formal confirmation from such duly recognized U.S. or French authorized authority, U.S. or French court of competent jurisdiction, or other governmental authority with jurisdiction over Circle that the legal obligation or court order (per Part 3, Policy Exceptions above) is lifted or no longer applicable, or that a security incident no longer requires such intervention.

> 5. Governance
> To ensure effective Circle oversight of this Policy, Circle will regularly report publicly the most up-to-date amount of access denied Circle Stablecoin tokens.

## 2. USDC Terms (circle.com/legal/usdc-terms)

Verbatim from the page (Blocklisting subsection):

> Blocklisting USDC is issued and redeemed in accordance with Circle's blocklisting policy . Circle reserves the right to block the transfer of USDC to and from an address on chain as permitted under the blocklisting policy.

Section 13 quotes (WebFetch extraction of "Blocked Addresses & Forfeited Funds"):

> Circle reserves the right to "block" certain USDC addresses and, if such addresses are Circle custodied addresses, freeze associated USDC (temporarily or permanently)

> In the event that you send USDC to a Blocked Address, or receive USDC from a Blocked Address, Circle may freeze such USDC and take steps to terminate your USDC Account.

## Notes

- The freeze capability exists and is documented by Circle as address-level access denial: a denied address can no longer send or receive USDC, and USDC at that address is blocked from on-chain transfer.
- Nothing in the policy describes reversing, clawing back, or re-crediting a completed transfer to a payer. The "Reversals" section reverses the access denial itself, not any payment. This supports the paper's characterization that the freeze authority is not a payment-reversal mechanism (the mechanism blocks future movement; it does not undo settled transfers).
