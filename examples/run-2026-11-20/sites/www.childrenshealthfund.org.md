# https://www.childrenshealthfund.org/

**Status:** Ready, with warnings (Google Tag Manager container)
**Checked:** 2026-11-20 08:55 UTC in 9.7s
**Account ID(s):** AVVHNSHB

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.childrenshealthfund.org/ |
| PASS | Installation code is in the page source | account ID(s): AVVHNSHB |
| PASS | Code is in <head>, last script | Found in <head> with no scripts after it. |
| PASS | One account ID on the page | AVVHNSHB |
| PASS | Widget script loads | HTTP 200, 24 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| INFO | Donate links open the checkout | No '?form=' links on this page. Fine if the page uses Elements or overlays instead. |
| WARN | Google Tag Manager container | No GTM container. Checkout events (donation, open, close) reach GA4 through a GTM container template. |
| PASS | GA4 measurement ID | G-SXWX7Z8RFC |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 5.2s |

## Summary (AI, from the facts above)

The page https://www.childrenshealthfund.org/ loaded with HTTP 200 in the headless browser. The FundraiseUp installation code is in the page source with account ID AVVHNSHB. The code is in the head with no scripts after it. The widget script loaded from cdn.fundraiseup.com with HTTP 200. No console errors were recorded. The page has no Google Tag Manager container, so checkout events may not reach GA4 through a GTM template. GA4 measurement ID G-SXWX7Z8RFC was found. No Meta Pixel was seen. No cookie consent tool was detected. No other donation tool was found. The load event was at 5.2 seconds. The browser did not click any donate button, so checkout behavior was not tested. No '?form=' donate links were found on this page.

### Risks

- **medium** No Google Tag Manager container: No GTM container was found on the page. Checkout events (donation, open, close) reach GA4 through a GTM container template, so those events may not be tracked. _(checks: gtm_container)_
- **low** No cookie consent tool detected: No known consent tool was detected. Consent is needed for EU and UK visitors, and vendor cookies need a consent setup. _(checks: consent_banner)_

### Next steps

- [customer] Add a Google Tag Manager container to the website, or confirm with the onboarding team how checkout events should reach GA4. _(checks: gtm_container)_
- [customer] Install a cookie consent tool if the site has EU or UK visitors, and set up consent for vendor cookies. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer which donate links or overlays the site uses, since no '?form=' links were found on the page. _(checks: fu_checkout_links)_
- [onboarding_team] Re-run this check after the customer makes changes to confirm the results. _(checks: gtm_container, consent_banner)_

### Draft email to the customer

**Subject:** Next steps for your donation platform setup

```text
Hello,

We checked your website at https://www.childrenshealthfund.org/. The donation widget is installed correctly and loads without errors. Your GA4 measurement ID was also found.

To finish setup, please do the following:

1. Add a Google Tag Manager container to your website. This lets donation events, such as opening and completing a donation, reach your GA4 reports.
2. If you have visitors in the EU or UK, install a cookie consent tool and set up consent for vendor cookies.

Once these changes are live, reply to this email and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.childrenshealthfund.org/
- fu_code_in_source: on.href;o.l=[]; for(i=0;i<8;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AVVHNSHB');</script> <!-- End Fundraise Up --> <style> .e-con.e-p
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AVVHNSHB
