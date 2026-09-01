Source-URL: https://6778953.fs1.hubspotusercontent-na1.net/hubfs/6778953/Blog%20Posts/Circle%20Stablecoin%20Access%20Denial%20Policy_pdf.pdf ; https://www.circle.com/legal/usdc-terms
Access-time: 2026-08-05T10:39:00Z
Capture-method: curl of the policy PDF (HTTP 200, 94176 bytes, 2 pages) with pypdf text extraction; curl of the USDC Terms page (HTTP 200, 377849 bytes). Policy PDF byte count is IDENTICAL to the 2026-07-02 capture (94176), so the policy is unchanged at the byte level.

---

Verbatim:

"Circle has the ability to block individual addresses from sending and receiving Circle Stablecoin on every blockchain to which Circle Stablecoin is issued. In this document, this ability is referred to as "access denial." When an address is denied access, it can no longer send or receive Circle Stablecoin and all of the Circle Stablecoin controlled by that address is blocked and cannot be transferred on-chain."

"4. Reversals Circle may revert the access denial of an individual address upon formal confirmation from such duly recognized U.S. or French authorized authority..."

---

Verdict 2026-08-05: CONFIRMED, byte-identical. The freeze authority is documented as address-level access denial, and the policy's only "Reversals" provision reverses the access denial itself rather than any settled payment. This continues to support the paper's Section 7 characterization that freeze authority exists but is not a payment-reversal mechanism. Note for the replication package: the access-denial policy is served from a HubSpot CDN URL rather than a circle.com path, so the durable citation remains the Terms page, as the shipped References entry already does.
