# https://www.nature.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 6.1s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.nature.org/en-us/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| WARN | Google Tag Manager container | No GTM container. Checkout events (donation, open, close) reach GA4 through a GTM container template. |
| WARN | GA4 measurement ID | No GA4 property seen loading or sending hits (may load only after consent). |
| PASS | Meta Pixel | loaded, pixel id(s): not seen |
| PASS | Cookie consent tool | OneTrust |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 1.8s |

## Summary (AI, from the facts above)

The page https://www.nature.org/ loaded in the headless browser. It returned HTTP 200 and redirected to https://www.nature.org/en-us/. No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded. The FundraiseUp global object is undefined. No checkout form links were found. The browser did not click anything, so checkout and donate buttons were not tested. No Google Tag Manager container was seen. No GA4 measurement ID was seen loading or sending hits, though GA4 may load only after consent. A Meta Pixel loaded, but no pixel ID was seen. OneTrust cookie consent was found. No other donation tool was found on the page. The page loaded in 1.8 seconds. Verdict: not installed, because the installation code is missing.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The FundraiseUp global object is undefined. _(checks: fu_code_in_source)_
- **medium** No Google Tag Manager container found: No GTM container was seen. Checkout events such as donation, open, and close reach GA4 through a GTM container template, so these events may not be tracked. _(checks: gtm_container)_
- **medium** No GA4 measurement ID seen: No GA4 property was seen loading or sending hits. GA4 may load only after consent, so this was not confirmed. _(checks: ga4)_

### Next steps

- [onboarding_team] Confirm with the customer whether the FundraiseUp installation code was added to the site, and ask for the account ID if it was. _(checks: fu_code_in_source)_
- [customer] Add the FundraiseUp installation code to every page that should show a donation form, in the head section of the page. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm with the customer whether a Google Tag Manager container and a GA4 property exist, and check whether GA4 loads only after cookie consent. _(checks: gtm_container, ga4)_
- [onboarding_team] Re-run this check after the customer confirms changes to the site. _(checks: fu_code_in_source, gtm_container, ga4)_

### Draft email to the customer

**Subject:** Next steps for your FundraiseUp setup on nature.org

```text
Hello,

Thank you for working with us to set up online donations. We checked https://www.nature.org/en-us/ and found that the FundraiseUp installation code is not on the page yet.

Please do the following:

1. Add the FundraiseUp installation code to the head section of each page that should show a donation form. We will send you the code snippet and your account ID.
2. Let us know if you already have a Google Tag Manager container and a GA4 property. If you do, please send the container ID and the GA4 measurement ID.

Once the code is added, reply to this email and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.nature.org/en-us/
- consent_banner: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js
