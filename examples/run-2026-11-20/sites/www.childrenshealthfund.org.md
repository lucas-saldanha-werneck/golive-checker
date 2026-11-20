# https://www.childrenshealthfund.org/

**Status:** Ready, with warnings (Google Tag Manager container; Page load under 6 s)
**Checked:** 2026-11-20 09:07 UTC in 19.6s
**Account ID(s):** AVVHNSHB

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.childrenshealthfund.org/ |
| PASS | Installation code is in the page source | account ID(s): AVVHNSHB |
| PASS | Code is in <head>, last script | Found in <head> with no scripts after it. |
| PASS | One account ID on the page | AVVHNSHB |
| PASS | Widget script loads | HTTP 200, 26 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| INFO | Donate links open the checkout | No '?form=' links on this page. Fine if the page uses Elements or overlays instead. |
| WARN | Google Tag Manager container | No GTM container. Checkout events (donation, open, close) reach GA4 through a GTM container template. |
| PASS | GA4 measurement ID | G-SXWX7Z8RFC |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 10.6s |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://www.childrenshealthfund.org/donation/ returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://www.childrenshealthfund.org/ loaded with HTTP 200 in a headless browser. The FundraiseUp install code is in the page source once, in the head, with no scripts after it. The widget script loaded from cdn.fundraiseup.com with account ID AVVHNSHB and no console errors. No '?form=' donate links were found on this page, and the browser did not click anything, so the checkout itself was not tested. No Google Tag Manager container was found, so checkout events are not routed through GTM. GA4 measurement ID G-SXWX7Z8RFC was found. The page load event took 10.6 seconds, above the 6 second target. The donate page at /donation/ returns readable content without JavaScript. Overall status: ready with warnings.

### Risks

- **medium** No Google Tag Manager container: No GTM container was found on the page. The checklist notes that checkout events (donation, open, close) reach GA4 through a GTM container template. Without it, those events may not be recorded in GA4 from this page. _(checks: gtm_container)_
- **medium** Slow page load: The load event fired at 10.6 seconds. The check target is under 6 seconds. Slow pages can lower donation completion. _(checks: page_speed)_
- **low** No cookie consent tool detected: No known consent tool was detected. Visitors from the EU or UK may need one, and vendor cookies need a consent setup. _(checks: consent_banner)_

### Next steps

- [onboarding_team] Confirm with the customer whether their GA4 setup uses a GTM container, and check whether donation events are arriving in GA4. _(checks: gtm_container, ga4)_
- [customer] Ask your web developer to review the page load time, which measured 10.6 seconds, and reduce it below 6 seconds. _(checks: page_speed)_
- [onboarding_team] Manually click the donate buttons on the live page to confirm the FundraiseUp checkout opens, since the headless check did not click anything. _(checks: fu_checkout_links, fu_widget_loads)_
- [customer] If you have visitors from the EU or UK, tell us which cookie consent tool you use, or ask your web developer about adding one. _(checks: consent_banner)_
- [onboarding_team] Re-run this check after the customer makes changes to confirm the results. _(checks: page_speed, gtm_container)_

### Draft email to the customer

**Subject:** Next steps for your donation page setup

```text
Hello,

Thank you for working with us to set up donations on your website. Your FundraiseUp code is installed correctly on https://www.childrenshealthfund.org/, and the donation widget loads without errors.

A few items need your attention:

1. Page speed: The home page took about 10.6 seconds to load. Please ask your web developer to bring this under 6 seconds.

2. Google Tag Manager: We did not find a Google Tag Manager container on the page. If you use GTM with your Google Analytics, please let us know. If not, we can help you decide next steps.

3. Cookie consent: If you have visitors in the EU or UK, please tell us which cookie consent tool you use, or ask your web developer about adding one.

Please reply with any questions. We will follow up after these items are reviewed.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.childrenshealthfund.org/
- fu_code_in_source: on.href;o.l=[]; for(i=0;i<8;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AVVHNSHB');</script> <!-- End Fundraise Up --> <style> .e-con.e-p
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AVVHNSHB
- donate_no_js: https://www.childrenshealthfund.org/donation/
