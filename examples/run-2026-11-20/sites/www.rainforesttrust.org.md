# https://www.rainforesttrust.org/

**Status:** Ready, with warnings (Page load under 6 s)
**Checked:** 2026-11-20 08:55 UTC in 10.7s
**Account ID(s):** ACMRCWPB

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.rainforesttrust.org/ |
| PASS | Installation code is in the page source | account ID(s): ACMRCWPB |
| PASS | Code is in <head>, last script | Found in <head> with no scripts after it. |
| PASS | One account ID on the page | ACMRCWPB |
| PASS | Widget script loads | HTTP 200, 17 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 2 '?form=' link(s): FUNAQFHNLKJ, FUNRGCCWCNJ |
| PASS | Google Tag Manager container | GTM-TQZN89M |
| PASS | GA4 measurement ID | G-MVP5KC1KV6 |
| PASS | Meta Pixel | loaded, pixel id(s): 162328464462089, 5913213552134911 |
| PASS | Cookie consent tool | CookieYes |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 6.3s |
| INFO | Console errors (any source) | 1 error(s) |

## Summary (AI, from the facts above)

The page https://www.rainforesttrust.org/ loaded with HTTP 200 in the headless browser. The FundraiseUp code is in the page source once, in the head, with account ID ACMRCWPB. The widget script loaded from the vendor host with HTTP 200. Two donate links with form IDs FUNAQFHNLKJ and FUNRGCCWCNJ were found. The browser did not click these links, so checkout behavior was not tested. Google Tag Manager (GTM-TQZN89M), GA4 (G-MVP5KC1KV6), Meta Pixel (two pixel IDs), and CookieYes were found. No other donation tool was found. The page load event took 6.3 seconds, which is over the 6 second limit. The verdict is ready with warnings. One console error was recorded: a 400 response from a resource.

### Risks

- **medium** Page load is slow: The load event finished at 6.3 seconds. The limit is 6 seconds. The verdict is ready with warnings, not blocked. _(checks: page_speed)_
- **low** One console error on the page: The browser recorded one console error: a failed resource with HTTP status 400. The source of the resource was not recorded. The FundraiseUp widget reported no console errors. _(checks: console_errors, fu_no_console_errors)_

### Next steps

- [customer] Review the page load time and reduce the load event time below 6 seconds. Check large scripts or images on the homepage. _(checks: page_speed)_
- [customer] Find the resource that returns a 400 error on the homepage and fix or remove it. _(checks: console_errors)_
- [onboarding_team] Confirm with the customer that the FundraiseUp donate links FUNAQFHNLKJ and FUNRGCCWCNJ open the correct checkout. The browser did not test this. _(checks: fu_checkout_links)_
- [onboarding_team] Re-run this check after the customer makes changes to confirm the load time and console error are resolved. _(checks: page_speed, console_errors)_

### Draft email to the customer

**Subject:** A few fixes before your donation page goes live

```text
Hello,

Thanks for setting up your FundraiseUp donation tools on rainforesttrust.org. Most of the setup looks good. The page loads, the FundraiseUp code and widget are in place, and your tracking tools were found.

Please make two fixes on your homepage:

1. Speed up the page. It currently takes about 6.3 seconds to finish loading. Please bring it under 6 seconds. Large images and extra scripts are common causes.

2. Fix one failing resource. The page returns a 400 error when loading one file. Please find that file and fix or remove it.

Once these are done, let us know and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.rainforesttrust.org/
- fu_code_in_source: .href;o.l=[]; for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','ACMRCWPB');</script> <!-- End Fundraise Up --> </head> <body> <n
- fu_widget_loads: https://cdn.fundraiseup.com/widget/ACMRCWPB
- consent_banner: https://cdn-cookieyes.com/client_data/bce0e242974d3ef4aada5386/script.js
- console_errors: Failed to load resource: the server responded with a status of 400 ()
