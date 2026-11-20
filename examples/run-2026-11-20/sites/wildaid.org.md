# https://wildaid.org/

**Status:** Ready
**Checked:** 2026-11-20 08:55 UTC in 10.2s
**Account ID(s):** AQTMUHNH

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://wildaid.org/ |
| PASS | Installation code is in the page source | account ID(s): AQTMUHNH |
| PASS | Code is in <head>, last script | Found in <head> with no scripts after it. |
| PASS | One account ID on the page | AQTMUHNH |
| PASS | Widget script loads | HTTP 200, 21 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 2 '?form=' link(s): FUNAUWUZXNA, donate |
| PASS | Google Tag Manager container | GTM-KF7HNF4, GTM-KZW6SPR |
| PASS | GA4 measurement ID | G-M6T97S534K |
| PASS | Meta Pixel | loaded, pixel id(s): 862335194865117 |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 5.9s |
| INFO | Console errors (any source) | 3 error(s) |

## Summary (AI, from the facts above)

The page https://wildaid.org/ loaded in a headless browser with HTTP 200 in 5.9 seconds. The FundraiseUp install code is in the page source once, in the head, with no scripts after it. The widget script loads from account AQTMUHNH with no widget console errors. Two donate links were found that point to checkout forms (FUNAUWUZXNA and donate). The browser did not click these links, so checkout behavior is not verified. Google Tag Manager, GA4, and Meta Pixel were found. No known cookie consent tool was detected. The page has 3 console errors: one failed resource that could not be resolved and two 404 responses.

### Risks

- **medium** No cookie consent tool detected: No known consent tool was found on the page. Vendor cookies from GTM, GA4, Meta Pixel, and FundraiseUp may need a consent setup for EU and UK visitors. _(checks: consent_banner)_
- **low** Console errors on the page: Three errors were recorded: one resource failed to resolve and two resources returned 404. The source of these resources was not identified in the recorded data. _(checks: console_errors)_

### Next steps

- [onboarding_team] Confirm with the customer whether they need a cookie consent setup for EU and UK visitors. _(checks: consent_banner)_
- [customer] Check the page for links or files that return 404 or fail to resolve, and fix or remove them. _(checks: console_errors)_
- [onboarding_team] Open the FundraiseUp dashboard and confirm that the checkout links FUNAUWUZXNA and donate open the correct forms for this account. _(checks: fu_checkout_links)_

### Draft email to the customer

**Subject:** Next steps for your donation page on wildaid.org

```text
Hello,

We checked your donation page at https://wildaid.org/. The FundraiseUp code is installed correctly, and the widget loads on the page. Your Google Tag Manager, GA4, and Meta Pixel tags were also found.

We need a few fixes from your side:

1. Please check the page for files or links that return a 404 error or fail to load, and fix or remove them. Our check found three console errors.
2. Please tell us whether you need a cookie consent banner for visitors in the EU or UK. We did not find a consent tool on the page.

Once these are done, we can run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://wildaid.org/
- fu_code_in_source: on.href;o.l=[]; for(i=0;i<8;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AQTMUHNH');</script> <!-- End Fundraise Up --> <link rel="stylesheet" type="
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AQTMUHNH
- console_errors: Failed to load resource: net::ERR_NAME_NOT_RESOLVED
- console_errors: Failed to load resource: the server responded with a status of 404 ()
- console_errors: Failed to load resource: the server responded with a status of 404 ()
