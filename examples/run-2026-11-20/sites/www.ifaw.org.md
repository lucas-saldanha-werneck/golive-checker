# https://www.ifaw.org/

**Status:** Ready, with warnings (Code is in <head>, last script; Widget not held back by the consent tool; GA4 measurement ID)
**Checked:** 2026-11-20 08:55 UTC in 8.6s
**Account ID(s):** AWMWZJRX

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.ifaw.org/ |
| PASS | Installation code is in the page source | account ID(s): AWMWZJRX |
| WARN | Code is in <head>, last script | In <head>, but 3 <script> tag(s) follow it. Docs recommend it as the last script. |
| PASS | One account ID on the page | AWMWZJRX |
| PASS | Widget script loads | HTTP 200, 11 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| WARN | Widget not held back by the consent tool | The widget script was inserted by Usercentrics, so it depends on consent settings. It loaded in this run; confirm it is set as strictly necessary, or visitors who decline cookies may not get the checkout. |
| PASS | Donate links open the checkout | 1 '?form=' link(s): join |
| PASS | Google Tag Manager container | GTM-W7GRNP |
| WARN | GA4 measurement ID | No GA4 property seen loading or sending hits (may load only after consent). |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| PASS | Cookie consent tool | Usercentrics |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 4.2s |

## Summary (AI, from the facts above)

Page https://www.ifaw.org/ loaded (HTTP 200). FundraiseUp code with account ID AWMWZJRX is in the page source and the widget script loaded in this run. No blockers were found. Three warnings: the code is in head but 3 other script tags follow it, the widget is inserted by the Usercentrics consent tool, and no GA4 measurement ID was seen. The browser did not click anything. One donate link with a ?form= parameter was found (join). This does not confirm the checkout works.

### Risks

- **low** FundraiseUp code is not the last script in head: The FundraiseUp snippet is in head, but 3 script tags follow it. The vendor docs recommend it as the last script. _(checks: fu_in_head)_
- **medium** Widget depends on cookie consent settings: The widget script was inserted by Usercentrics. If visitors decline cookies, the widget may be held back and the checkout may not load for them. It loaded in this run. _(checks: fu_consent_gated)_
- **low** No GA4 measurement ID seen: No GA4 property was seen loading or sending hits. It may load only after consent, so this run could not confirm it. _(checks: ga4)_

### Next steps

- [onboarding_team] Confirm with the customer whether they use Google Analytics 4 and, if so, which measurement ID they expect to see on the page. _(checks: ga4)_
- [onboarding_team] Check the Usercentrics settings with the customer to confirm the FundraiseUp widget script is set as strictly necessary, then re-run this check. _(checks: fu_consent_gated)_
- [customer] Ask your web developer to move the FundraiseUp snippet so it is the last script inside the head section of the page. _(checks: fu_in_head)_

### Draft email to the customer

**Subject:** Next steps for your FundraiseUp setup on ifaw.org

```text
Hello,

We checked your page at https://www.ifaw.org/. The FundraiseUp code is installed and the widget loaded. We found three items to fix or confirm.

Please do the following:

1. Ask your web developer to move the FundraiseUp snippet so it is the last script inside the head section of the page.

2. Confirm that the FundraiseUp widget is set as strictly necessary in your cookie consent tool (Usercentrics). This keeps the donation widget working for visitors who decline cookies.

3. If you use Google Analytics 4, send us your measurement ID so we can confirm it appears on the page.

Thank you. Please reply with any questions.

Best regards,
Onboarding Team
```

## Evidence

- page_reachable: https://www.ifaw.org/
- fu_code_in_source: tion.href;o.l=[]; for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AWMWZJRX');</script> <!-- End Fundraise Up --> <script src=https://www.f
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AWMWZJRX
- fu_consent_gated: https://web.cmp.usercentrics.eu/ui/v/4.34.0/WebSdk.lib.fb4e0364.js
- consent_banner: https://web.cmp.usercentrics.eu/ui/loader.js
