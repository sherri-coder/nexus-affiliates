# Nexus affiliates site

Target: https://affiliates.elevateops360.com/

Static site. Vercel serves `public/` (see `vercel.json`; no build command).

## Files
- `public/index.html`: the affiliate program page
- `public/sales-kit.html`: formatted sales kit (generated from the markdown)
- `public/affiliate_sales_kit.md`: sales kit source
- `public/nexus_affiliate_kit.zip`: public download of the page and kit

## Editing
If you change `affiliate_sales_kit.md` or `index.html`, regenerate `sales-kit.html` and the zip so the three stay in sync.

## Status
Enrollment is closed until real tracking, application and payout systems are configured. Confirm checkout pricing before opening enrollment. Keep internal economics and launch notes out of `public/`.
