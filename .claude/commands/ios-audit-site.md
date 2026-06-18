---
description: Audit any website for App Store-ready iOS conversion.
---

# /ios-audit-site

Input: `$ARGUMENTS` - URL, local HTML file, app name, or site-to-iOS brief.

Use the `site-to-ios-app` skill.

Run the public site audit path before recommending a build strategy:

- inspect viewport, responsive behavior, manifest, icons, privacy, terms,
  support, account deletion, auth, payments, and route depth;
- run `scripts/audit_site_for_ios.py` when a URL or HTML file is available;
- identify the core iOS app job and the native value needed to avoid a thin
  wrapper;
- output PASS/BLOCK plus the next best `/ios-*` command to run.

Default output artifact: `SITE_TO_IOS_AUDIT.md`.
