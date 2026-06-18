---
description: Review iOS auth flows for App Store, web shell, and native app readiness.
---

# /ios-auth-check

Input: `$ARGUMENTS` - app path, login URL, auth provider, or review issue.

Use the `site-to-ios-app`, `ios-capacitor-shell`, and `ios-swiftui-product`
skills.

Check auth from the iOS user's point of view:

- login, logout, session refresh, and account deletion;
- Sign in with Apple requirements when third-party login is present;
- web auth callback handling;
- private browser/session behavior;
- reviewer account needs;
- screenshots and metadata that mention accounts or subscriptions.

Output PASS/BLOCK, exact user flows tested or still needed, and review-note
requirements.
