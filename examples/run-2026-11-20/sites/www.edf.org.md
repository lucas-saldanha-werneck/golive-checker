# https://www.edf.org/

**Status:** Ready, with warnings (Installation code is in the page source; Google Tag Manager container; GA4 measurement ID)
**Checked:** 2026-11-20 08:55 UTC in 7.2s
**Account ID(s):** AQBHBSYR

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.edf.org/ |
| WARN | Installation code is in the page source | Widget loads at runtime but the code is not in the server HTML. Inserted by: JavaScript from https://assets.edfcdn.org/assets/global/dist/js/utilities.min.js?v=2026112002 (not a tag manager). Vendor docs ask for the code in the global <head> and confirm it by viewing the page source. |
| PASS | One account ID on the page | AQBHBSYR |
| PASS | Widget script loads | HTTP 200, 24 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 1 '?form=' link(s): eoy-match-web |
| WARN | Google Tag Manager container | No GTM container. Checkout events (donation, open, close) reach GA4 through a GTM container template. |
| WARN | GA4 measurement ID | No GA4 property seen loading or sending hits (may load only after consent). |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 2.4s |

## Summary (AI, from the facts above)

The page https://www.edf.org/ loaded with HTTP 200 in the headless browser. The FundraiseUp widget for account AQBHBSYR loads at runtime from cdn.fundraiseup.com with HTTP 200. The installation code is not in the server HTML. It is inserted by JavaScript from assets.edfcdn.org (utilities.min.js), not by a tag manager. No GTM container was found. No GA4 measurement ID was seen loading or sending hits, though GA4 may load only after consent. No Meta Pixel was seen. No cookie consent tool was detected. One donate link was found with the form parameter eoy-match-web. The browser did not click any link, so the checkout was not tested. No other donation tool was found. The page loaded in 2.4 seconds. The verdict is ready with warnings and no blockers.

### Risks

- **medium** Install code is not in the page source: The widget is added by JavaScript at runtime from a site script, not in the global head. Vendor docs ask for the code in the head and a page source check. _(checks: fu_code_in_source)_
- **medium** No Google Tag Manager container found: Checkout events such as donation, open, and close do not reach GA4 through a GTM container template as recorded. _(checks: gtm_container)_
- **medium** No GA4 measurement ID seen: No GA4 property was seen loading or sending hits. It may load only after consent, so this needs confirmation. _(checks: ga4)_
- **low** No cookie consent tool detected: No known consent tool was found. EU and UK visitors need one for vendor cookies. _(checks: consent_banner)_

### Next steps

- [onboarding_team] Confirm with the customer whether GA4 loads only after consent, and check the GA4 property in the dashboard for the measurement ID. _(checks: ga4)_
- [onboarding_team] Confirm with the customer whether they use a tag manager and whether a GTM container is set up for checkout events. _(checks: gtm_container)_
- [customer] Ask your web team to place the FundraiseUp install code in the global head of the page instead of loading it through the site script, then view the page source to confirm it is there. _(checks: fu_code_in_source)_
- [customer] Ask your web team to add a cookie consent tool for EU and UK visitors and set up the vendor cookies to respect it. _(checks: consent_banner)_
- [onboarding_team] Re-run this check after the customer makes changes and test the donate link with the checkout in a normal browser. _(checks: fu_checkout_links, fu_code_in_source)_

### Draft email to the customer

**Subject:** A few fixes before your donation page is ready

```text
Hello,

Thank you for working with us to launch your donation page. We checked https://www.edf.org/ and found a few items to fix.

Please ask your web team to:

1. Place the donation widget code in the global head of the page, not added by a site script. After the change, view the page source to confirm the code is there.

2. Add a cookie consent tool for visitors in the EU and UK, and set up the donation vendor cookies to respect it.

Once these are done, let us know and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.edf.org/
- fu_code_in_source: https://cdn.fundraiseup.com/widget/AQBHBSYR
- fu_code_in_source: https://assets.edfcdn.org/assets/global/dist/js/utilities.min.js?v=2026112002
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AQBHBSYR
