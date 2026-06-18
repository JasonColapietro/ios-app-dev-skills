---
description: Turn any website or web app into an iOS app plan and build path.
---

# /ios-site-app

Input: `$ARGUMENTS` - URL, app name, existing repo path, or site-to-iOS request.

Use the `site-to-ios-app`, `ios-capacitor-shell`, `ios-swiftui-product`,
`ios-aso-launch`, and `ios-app-store-release` skills.

## Flow

1. Identify the URL, target user, core job, login, payments, and sensitive
   permissions.
2. Run `scripts/audit_site_for_ios.py` when a URL or HTML file is available.
3. Fill `templates/site-to-ios/SITE_TO_IOS_PLAN.md`.
4. Choose Capacitor remote, Capacitor bundled, native SwiftUI shell, or full
   native rebuild.
5. Add native value before treating the app as App Store-ready.
6. Build and test on simulator or device.
7. Produce screenshots, metadata, privacy answers, and review notes.
8. Output PASS/BLOCK. Do not submit publicly without explicit user confirmation.

Output the strategy, artifact paths, build commands, wrapper-risk assessment,
and exact remaining blockers.
