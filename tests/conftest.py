"""Small hand-made captures. The snippet text is the vendor's real install code
(as seen on live customer sites) with a fake account ID."""

import pytest

SNIPPET = """<script>(function(w,d,s,n,a){if(!w[n]){var l='call,catch,on,once,set,then,track'
.split(','),i,o=function(n){return'function'==typeof n?o.l.push([arguments])&&o
:function(){return o.l.push([n,arguments])&&o}},t=d.getElementsByTagName(s)[0],
j=d.createElement(s);j.async=!0;j.src='https://cdn.fundraiseup.com/widget/'+a;
t.parentNode.insertBefore(j,t);o.s=Date.now();o.v=4;o.h=w.location.href;o.l=[];
for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o}
})(window,document,'script','FundraiseUp','{ID}');</script>"""

GTM_HEAD = "<script>(function(w,d,s,l,i){})(window,document,'script','dataLayer','GTM-ABC1234');</script>"


def snippet(account="ABCDEFGH"):
    return SNIPPET.replace("{ID}", account)


def make_cap(raw_head="", raw_body="", rendered_extra="", requests=(), failed=(), console=(), status=200,
             error=None, globals_=None, load_ms=2100, url="https://example.org/"):
    raw = f"<!doctype html><html><head><title>t</title>{raw_head}</head><body>{raw_body}</body></html>"
    rendered = raw.replace("</body>", rendered_extra + "</body>")
    return {
        "url": url, "final_url": url, "status": status, "error": error,
        "raw_html": raw, "rendered_html": rendered,
        "requests": [dict(r) for r in requests], "failed_requests": [dict(f) for f in failed],
        "console": [dict(c) for c in console], "page_errors": [],
        "globals": globals_ or {"FundraiseUp": "undefined", "google_tag_manager": [], "dataLayer": None},
        "timing": {"load_ms": load_ms, "dom_content_loaded_ms": 900, "check_seconds": 6.2},
    }


def req(url, status=200, type_="script"):
    return {"url": url, "status": status, "type": type_}


WIDGET = "https://cdn.fundraiseup.com/widget/ABCDEFGH"
GTM_JS = "https://www.googletagmanager.com/gtm.js?id=GTM-ABC1234"
GA4_HIT = "https://region1.google-analytics.com/g/collect?v=2&tid=G-TEST12345&en=page_view"
ONETRUST = "https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"


@pytest.fixture
def good_cap():
    return make_cap(
        raw_head=GTM_HEAD + '<link rel="stylesheet" href="/a.css">' + snippet(),
        raw_body='<a href="/donate?form=spring2026">Donate</a>',
        requests=[req("https://example.org/"), req(GTM_JS), req(WIDGET), req("https://static.fundraiseup.com/x.js"), req(GA4_HIT, 204, "fetch"), req(ONETRUST)],
        globals_={"FundraiseUp": "object", "google_tag_manager": ["GTM-ABC1234", "G-TEST12345"], "dataLayer": 12},
    )
