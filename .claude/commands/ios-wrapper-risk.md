---
description: Check whether a website-to-iOS plan is likely to be rejected as a thin wrapper.
---

# /ios-wrapper-risk

Input: `$ARGUMENTS` - URL, app plan, existing shell, or App Review concern.

Use the `site-to-ios-app`, `ios-capacitor-shell`, and `ios-swiftui-product`
skills.

Grade the App Store 4.2 risk:

- what the app does beyond opening a website;
- native onboarding, settings, support, account deletion, offline, errors, and
  navigation;
- device features that serve the product instead of decorating it;
- whether payments, auth, or account flows work cleanly on iOS;
- what must be rebuilt before submission.

Output `LOW`, `MEDIUM`, or `HIGH` wrapper risk with concrete fixes.
