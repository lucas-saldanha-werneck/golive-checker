# https://www.rescue.org/

**Status:** Ready, with warnings (Installation code is in the page source)
**Checked:** 2026-11-20 09:07 UTC in 7.7s
**Account ID(s):** AFGSSTXA

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.rescue.org/ |
| WARN | Installation code is in the page source | Widget loads at runtime but the code is not in the server HTML. Inserted by: JavaScript from https://www.rescue.org/sites/default/files/js/js_7FJZD1Rmf6kTOo6GC90du9gqdSyoYe8B7R2muiqtwOU.js?scope=header&delta=1&lan (not a tag manager). Vendor docs ask for the code in the global <head> and confirm it by viewing the page source. |
| PASS | One account ID on the page | AFGSSTXA |
| PASS | Widget script loads | HTTP 200, 14 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 3 '?form=' link(s): donate, evergreen-crisis-ftr, evergreen-crisis-w |
| PASS | Google Tag Manager container | GTM-5JH3VLS |
| PASS | GA4 measurement ID | G-DDZCWB8N2Y, G-MCH4QLVDRD |
| PASS | Meta Pixel | loaded, pixel id(s): 412981725737143 |
| PASS | Cookie consent tool | OneTrust |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 2.9s |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: NGO; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://www.rescue.org/?form=donate&ms=ws_resq_top_nav_btn_fy27_q1_mmus_oct returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://www.rescue.org/ loaded in a headless browser with HTTP 200 and no load error. The FundraiseUp widget script loads at runtime with account ID AFGSSTXA, but the installation code is not in the server HTML. It is inserted by a JavaScript file, not by a tag manager. Vendor docs ask for the code in the global head and confirm it by viewing the page source. The verdict is ready with warnings. No blockers were recorded. The browser did not click anything, so the checkout was not tested. Three checkout-form links were found: donate, evergreen-crisis-ftr, and evergreen-crisis-w. Other checks passed: GTM container GTM-5JH3VLS, GA4 IDs G-DDZCWB8N2Y and G-MCH4QLVDRD, Meta Pixel 412981725737143, OneTrust consent, no other donation tool, and page load at 2.9 s.

### Risks

- **medium** Widget code is not in the page source: The FundraiseUp code is added at runtime by a JavaScript file. It is not in the server HTML and not in the global head. The vendor asks for the code in the head and a page-source check to confirm it. _(checks: fu_code_in_source)_

### Next steps

- [customer] Add the FundraiseUp installation snippet for account AFGSSTXA to the global head of the site template so it appears in the page source. _(checks: fu_code_in_source)_
- [onboarding_team] After the customer confirms the change, re-run this check and confirm the snippet appears in the page source. _(checks: fu_code_in_source)_

### Draft email to the customer

**Subject:** One fix needed for your donation widget on rescue.org

```text
Hello,

Thank you for working with us to set up online donations. Our check of https://www.rescue.org/ found that the donation widget loads, but its installation code is not in the page source.

Please do the following:

1. Add the FundraiseUp installation snippet for account AFGSSTXA to the global head section of your site template. The snippet should be in the server-delivered HTML, not added later by JavaScript.
2. View the page source and confirm the snippet appears inside the head section.
3. Reply to let us know when this is done.

Once you confirm, we will run the check again.

Thank you,

Onboarding Team
```

## Evidence

- page_reachable: https://www.rescue.org/
- fu_code_in_source: https://cdn.fundraiseup.com/widget/AFGSSTXA
- fu_code_in_source: https://www.rescue.org/sites/default/files/js/js_7FJZD1Rmf6kTOo6GC90du9gqdSyoYe8B7R2muiqtwOU.js?scope=header&delta=1&language=en&theme=x&include=eJxljlsOgzAMBC8E-BLcwzLEoSEPIycgevs2AVVq-7Pa8ViyDRUK9GSFiR90ONHcscVZYswtJYGRRIUxuORR2f55uyej5DLjvlX53hdFo-5gGGsfa63G0syTiMeJMsOHsvG4tr
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AFGSSTXA
- consent_banner: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js?did=3b1085ba-2b42-4c13-bc5b-9aa9908e2ea6&data-document-language=true
- donate_no_js: https://www.rescue.org/?form=donate&ms=ws_resq_top_nav_btn_fy27_q1_mmus_oct
