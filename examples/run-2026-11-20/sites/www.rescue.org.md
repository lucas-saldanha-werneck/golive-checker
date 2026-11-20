# https://www.rescue.org/

**Status:** Ready, with warnings (Installation code is in the page source)
**Checked:** 2026-11-20 08:56 UTC in 7.0s
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
| PASS | Page load under 6 s | load event at 2.6s |

## Summary (AI, from the facts above)

The page https://www.rescue.org/ loaded in a headless browser with HTTP 200 and no load error. The FundraiseUp widget script loads at runtime from account AFGSSTXA. The installation code is not in the server HTML and is not in the page source. It is inserted by a JavaScript file at runtime. Vendor docs ask for the code in the global head and a check of the page source, so this needs a fix. The browser found three checkout links with '?form=' (donate, evergreen-crisis-ftr, evergreen-crisis-w). The browser did not click these links. No console errors, no failed requests, and no other donation tools were recorded. The page load event was at 2.6 seconds. Overall verdict: ready with warnings.

### Risks

- **medium** Installation code is not in page source: The FundraiseUp code is not in the server HTML. It is added by a JavaScript file at runtime. Vendor docs ask for the code in the global head and confirmation by viewing the page source. Check that the widget still loads after any change to the site's JavaScript. _(checks: fu_code_in_source)_

### Next steps

- [customer] Add the FundraiseUp installation code for account AFGSSTXA to the global head of the site, so it appears in the page source. _(checks: fu_code_in_source)_
- [onboarding_team] After the customer updates the site, re-run this check and confirm the code appears in the page source and in the head. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm with the customer that the three checkout links (donate, evergreen-crisis-ftr, evergreen-crisis-w) go to the intended FundraiseUp forms. _(checks: fu_checkout_links)_

### Draft email to the customer

**Subject:** One fix needed for your donation widget

```text
Hello,

We checked your website, https://www.rescue.org/, for the online donation widget. The widget loads on your page, and we found three donation links that point to checkout forms. The page loads without errors.

One fix is needed. The widget code is not in your page source. It is added later by a JavaScript file. Please add the widget installation code for account AFGSSTXA to the global head section of your website, so it appears in the page source. Once it is added, you can view the page source to confirm it is there.

Please let us know when the change is live. We will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.rescue.org/
- fu_code_in_source: https://cdn.fundraiseup.com/widget/AFGSSTXA
- fu_code_in_source: https://www.rescue.org/sites/default/files/js/js_7FJZD1Rmf6kTOo6GC90du9gqdSyoYe8B7R2muiqtwOU.js?scope=header&delta=1&language=en&theme=x&include=eJxljlsOgzAMBC8E-BLcwzLEoSEPIycgevs2AVVq-7Pa8ViyDRUK9GSFiR90ONHcscVZYswtJYGRRIUxuORR2f55uyej5DLjvlX53hdFo-5gGGsfa63G0syTiMeJMsOHsvG4tr
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AFGSSTXA
- consent_banner: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js?did=3b1085ba-2b42-4c13-bc5b-9aa9908e2ea6&data-document-language=true
