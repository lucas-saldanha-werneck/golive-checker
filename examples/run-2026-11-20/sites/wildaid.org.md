# https://wildaid.org/

**Status:** Ready, with warnings (Page load under 6 s)
**Checked:** 2026-11-20 09:07 UTC in 13.9s
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
| WARN | Page load under 6 s | load event at 8.9s |
| INFO | Console errors (any source) | 3 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| PASS | llms.txt published | /llms.txt found. |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://wildaid.org/?form=donate returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://wildaid.org/ loaded in a headless browser with HTTP 200. The FundraiseUp install code is in the page source once, in the head, with no scripts after it. The widget script loaded from account ID AQTMUHNH. The browser did not click anything, so the checkout itself was not tested. Two donate links with form parameters were found. The page load event took 8.9 seconds, which is over the 6 second limit and is a warning, not a blocker. Three console errors were recorded, including one failed request and two 404 responses. No known cookie consent tool was detected. The Meta Pixel, GA4, and GTM containers were found in the page. The robots.txt allows the listed AI bots, llms.txt is present, and Organization markup is present. DonateAction markup is not present.

### Risks

- **medium** Page load is slow: The load event fired at 8.9 seconds. The check limit is 6 seconds. _(checks: page_speed)_
- **low** Failed requests and 404 errors on the page: Three console errors were recorded: one name resolution failure and two 404 responses. The source of these requests was not identified. _(checks: console_errors)_
- **medium** No cookie consent tool detected: No known consent tool was found. Visitors from the EU or UK may need a consent setup because vendor cookies are set. _(checks: consent_banner)_

### Next steps

- [onboarding_team] Confirm with the customer which page elements produce the three console errors and the 404 responses, and whether the page speed issue is known. _(checks: page_speed, console_errors)_
- [onboarding_team] Confirm with the customer whether they need a cookie consent setup for EU and UK visitors. _(checks: consent_banner)_
- [onboarding_team] Test a donate link in a normal browser to confirm the checkout opens. The headless check did not click anything. _(checks: fu_checkout_links)_
- [customer] Fix the 404 and failed resource references on the page, and reduce page load time to under 6 seconds. _(checks: page_speed, console_errors)_
- [customer] Decide whether to set up a cookie consent tool for EU and UK visitors. _(checks: consent_banner)_

### Draft email to the customer

**Subject:** Next steps for your donation page at wildaid.org

```text
Hello,

Thanks for working with us to set up donations on wildaid.org. The donation widget is installed correctly and loads on your page. We found a few items to fix:

1. Reduce page load time. Your page took 8.9 seconds to finish loading. Please aim for under 6 seconds. Large images and scripts are common causes.

2. Fix broken resource links. We found three errors, including two 404 responses and one failed request. Please find the missing files or update the links that point to them.

3. Decide on cookie consent. If you have visitors in the EU or UK, you may need a cookie consent tool. Please let us know if you want help choosing one.

Once these are fixed, reply to this email and we will run the check again.

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
- donate_no_js: https://wildaid.org/?form=donate
