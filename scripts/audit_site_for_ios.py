#!/usr/bin/env python3
import argparse
import html
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title_parts = []
        self.metas = []
        self.links = []
        self.forms = 0
        self.anchors = []
        self._anchor = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            self.metas.append(attrs_dict)
        elif tag == "link":
            self.links.append(attrs_dict)
        elif tag == "form":
            self.forms += 1
        elif tag == "a":
            self._anchor = {"href": attrs_dict.get("href", ""), "text": ""}

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "a" and self._anchor is not None:
            self._anchor["text"] = " ".join(self._anchor["text"].split())
            self.anchors.append(self._anchor)
            self._anchor = None

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)
        if self._anchor is not None:
            self._anchor["text"] += data

    @property
    def title(self):
        return " ".join("".join(self.title_parts).split())


def read_target(target, timeout):
    path = pathlib.Path(target).expanduser()
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace"), str(path), "local file"

    parsed = urllib.parse.urlparse(target)
    if not parsed.scheme:
        target = "https://" + target
    request = urllib.request.Request(
        target,
        headers={
            "User-Agent": "ios-app-dev-skills-site-audit/1.0",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        body = response.read(2_000_000).decode(charset, errors="replace")
        status = getattr(response, "status", "unknown")
        final_url = response.geturl()
    return body, final_url, f"HTTP {status}"


def rel_contains(link, value):
    rel = link.get("rel", "").lower()
    return value in re.split(r"\s+", rel)


def meta_content(parser, key, value):
    value = value.lower()
    for meta in parser.metas:
        if meta.get(key, "").lower() == value:
            return meta.get("content", "")
    return ""


def find_anchor(parser, *needles):
    results = []
    for anchor in parser.anchors:
        haystack = f"{anchor.get('text', '')} {anchor.get('href', '')}".lower()
        if any(needle in haystack for needle in needles):
            results.append(anchor)
    return results


def bullet(flag, text):
    return f"- [{'x' if flag else ' '}] {text}"


def summarize(target, final_url, status, body, parser):
    lower_body = body.lower()
    links = parser.links
    manifest = next((link for link in links if rel_contains(link, "manifest")), None)
    apple_icon = next((link for link in links if rel_contains(link, "apple-touch-icon")), None)
    icon = next((link for link in links if rel_contains(link, "icon")), None)
    viewport = meta_content(parser, "name", "viewport")
    theme_color = meta_content(parser, "name", "theme-color")
    description = meta_content(parser, "name", "description")
    privacy = find_anchor(parser, "privacy")
    terms = find_anchor(parser, "terms", "tos")
    support = find_anchor(parser, "support", "contact", "help")
    delete_account = find_anchor(
        parser,
        "delete account",
        "account deletion",
        "delete my account",
    )
    auth_signals = ["login", "log in", "sign in", "signup", "sign up", "oauth"]
    payment_signals = ["checkout", "payment", "subscribe", "subscription", "stripe", "paypal"]
    permission_signals = ["camera", "microphone", "location", "notification", "upload", "file"]
    auth_found = any(signal in lower_body for signal in auth_signals) or parser.forms > 0
    payments_found = any(signal in lower_body for signal in payment_signals)
    permissions_found = [signal for signal in permission_signals if signal in lower_body]
    wrapper_risks = []
    if not viewport:
        wrapper_risks.append("No viewport meta tag found.")
    if not privacy:
        wrapper_risks.append("No visible privacy link found.")
    if not terms:
        wrapper_risks.append("No visible terms link found.")
    if not support:
        wrapper_risks.append("No visible support/contact/help link found.")
    if len(body) < 10_000 and not auth_found and not payments_found:
        wrapper_risks.append("Page appears lightweight or content-only; a thin wrapper may be weak.")

    native_value = [
        "Native onboarding and account/settings shell.",
        "Offline, network-error, retry, and empty states.",
        "Universal links or deep links for primary routes.",
        "Native support, privacy, terms, and account deletion route.",
    ]
    if auth_found:
        native_value.append("Hardened session persistence and OAuth return handling.")
    if payments_found:
        native_value.append("Payment policy review and native subscription decision.")
    if permissions_found:
        native_value.append(
            "Permission prompts and denial states for: "
            + ", ".join(sorted(set(permissions_found)))
            + "."
        )

    lines = [
        "# Site-to-iOS Audit",
        "",
        f"- Target: `{target}`",
        f"- Final URL: `{final_url}`",
        f"- Status: {status}",
        f"- Title: {html.escape(parser.title) if parser.title else 'Missing'}",
        f"- Description: {html.escape(description) if description else 'Missing'}",
        "",
        "## App Readiness Signals",
        "",
        bullet(bool(viewport), f"Viewport meta present{': `' + viewport + '`' if viewport else ''}."),
        bullet(bool(manifest), f"Web manifest present{': `' + manifest.get('href', '') + '`' if manifest else ''}."),
        bullet(bool(apple_icon), f"Apple touch icon present{': `' + apple_icon.get('href', '') + '`' if apple_icon else ''}."),
        bullet(bool(icon), f"Generic icon present{': `' + icon.get('href', '') + '`' if icon else ''}."),
        bullet(bool(theme_color), f"Theme color present{': `' + theme_color + '`' if theme_color else ''}."),
        bullet(bool(privacy), "Privacy link visible."),
        bullet(bool(terms), "Terms link visible."),
        bullet(bool(support), "Support/contact/help link visible."),
        bullet(bool(delete_account), "Account deletion link visible."),
        bullet(auth_found, "Authentication or form flow detected."),
        bullet(payments_found, "Payment/subscription language detected."),
        "",
        "## Wrapper Risk",
        "",
    ]
    if wrapper_risks:
        lines.extend(f"- {risk}" for risk in wrapper_risks)
    else:
        lines.append("- No basic wrapper blockers detected by static HTML audit.")
    lines.extend(
        [
            "",
            "## Suggested Native Value",
            "",
            *[f"- {item}" for item in native_value],
            "",
            "## Next Steps",
            "",
            "- Fill `templates/site-to-ios/SITE_TO_IOS_PLAN.md`.",
            "- Choose Capacitor remote, Capacitor bundled, native shell, or native rebuild.",
            "- Verify App Store 4.2 risk with rendered iPhone QA, not only this static audit.",
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Audit a website for iOS app conversion readiness.")
    parser.add_argument("target", help="URL or local HTML file")
    parser.add_argument("--out", help="Write markdown audit to this path")
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    try:
        body, final_url, status = read_target(args.target, args.timeout)
    except (OSError, urllib.error.URLError, UnicodeError) as exc:
        print(f"failed to read target: {exc}", file=sys.stderr)
        return 2

    site_parser = SiteParser()
    site_parser.feed(body)
    report = summarize(args.target, final_url, status, body, site_parser)

    if args.out:
        pathlib.Path(args.out).write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
