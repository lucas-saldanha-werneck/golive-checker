# https://www.edf.org/

**Status:** Ready, with warnings (Installation code is in the page source; Google Tag Manager container; GA4 measurement ID)
**Checked:** 2026-11-20 09:07 UTC in 6.9s
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

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: NonprofitOrganization; DonateAction: yes. |
| WARN | Donate page readable without JavaScript | https://give.edf.org/page/web-donate?page_id=e8b8f91b-1127-4e66-9c2f-b868edb21004&session_id=40fa8fdf-0f36-420b-a8ea-3acb73e3ea9a&page_id=e8b8f91b-1127-4e66-9c2f-b868edb21004&session_id=40fa8fdf-0f36-420b-a8ea-3acb73e3ea9a returns HTTP 200 but no form, checkout link or install code in the HTML; agents that do not run JavaScript see no way to give. |

## Summary (AI, from the facts above)

The page https://www.edf.org/ loaded with HTTP 200 in the headless browser. The FundraiseUp widget script loads at runtime for account AQBHBSYR, and one checkout-style link was found (?form=eoy-match-web). The install code is not in the server HTML. It is inserted by a JavaScript file from assets.edfcdn.org, not by a tag manager. No Google Tag Manager container was found. No GA4 measurement ID was seen sending hits, though it may load after consent. The donate page at give.edf.org returns HTTP 200 but its HTML has no form, checkout link, or install code, so it needs JavaScript to show a way to give. The browser did not click any link, so this check does not show whether the checkout works. Verdict: ready with warnings.

### Risks

- **medium** Install code not in page source: The FundraiseUp code is added by JavaScript at runtime, not in the server HTML. The vendor asks for the code in the global head and a page source check to confirm it. _(checks: fu_code_in_source)_
- **medium** No Google Tag Manager container found: Checkout events such as donation, open, and close are not confirmed to reach GA4 because no GTM container was seen. _(checks: gtm_container)_
- **medium** No GA4 measurement ID seen: No GA4 property was seen loading or sending hits. It may load only after consent, so this is not confirmed. _(checks: ga4)_
- **low** Donate page needs JavaScript: The give.edf.org donate page returns HTML with no form, checkout link, or install code. Agents that do not run JavaScript cannot see a way to give. _(checks: donate_no_js)_
- **low** No consent tool detected: No known consent tool was found. Visitors in the EU and UK may need one because vendor cookies are set. _(checks: consent_banner)_

### Next steps

- [customer] Add the FundraiseUp installation code to the global head of the website so it appears in the page source, then confirm it in the page source. _(checks: fu_code_in_source)_
- [customer] Set up a Google Tag Manager container on the website, or confirm that GA4 is already loaded and sending donation events. _(checks: gtm_container, ga4)_
- [customer] Confirm whether a cookie consent tool is needed for EU and UK visitors and set one up if so. _(checks: consent_banner)_
- [customer] Make the give.edf.org donate page show its donation form or a checkout link in the server HTML, so it can be read without JavaScript. _(checks: donate_no_js)_
- [onboarding_team] Check the FundraiseUp and GA4 dashboard settings with the customer, then re-run this check after the customer changes the site. _(checks: fu_code_in_source, gtm_container, ga4, donate_no_js)_

### Draft email to the customer

**Subject:** A few fixes for your donation setup on edf.org

```text
Hi there,

Thanks for working with us on your online donation setup. We checked https://www.edf.org/ and the donate page at give.edf.org. The donation widget loads, and we found a donation link. There are a few fixes that only your team can make on the website:

1. Add the FundraiseUp installation code to the global head of the site, so it appears in the page source. Right now it is added by a script at load time.
2. Set up a Google Tag Manager container, or confirm that Google Analytics 4 is sending donation events.
3. Confirm whether you need a cookie consent tool for EU and UK visitors, and set one up if so.
4. Make the give.edf.org donate page show its donation form or a checkout link in the page HTML, so it can be read without JavaScript.

Once these changes are live, reply to this email and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.edf.org/
- fu_code_in_source: https://cdn.fundraiseup.com/widget/AQBHBSYR
- fu_code_in_source: https://assets.edfcdn.org/assets/global/dist/js/utilities.min.js?v=2026112002
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AQBHBSYR
- donate_no_js: https://give.edf.org/page/web-donate?page_id=e8b8f91b-1127-4e66-9c2f-b868edb21004&session_id=40fa8fdf-0f36-420b-a8ea-3acb73e3ea9a&page_id=e8b8f91b-1127-4e66-9c2f-b868edb21004&session_id=40fa8fdf-0f36-420b-a8ea-3acb73e3ea9a
