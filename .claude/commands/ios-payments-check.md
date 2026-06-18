---
description: Review payment, subscription, checkout, and IAP risk for iOS release.
---

# /ios-payments-check

Input: `$ARGUMENTS` - app path, checkout URL, monetization plan, or payment risk.

Use the `site-to-ios-app`, `ios-capacitor-shell`, `ios-swiftui-product`, and
`ios-app-store-release` skills.

Check payment truth before submission:

- digital goods vs physical goods/service classification;
- StoreKit/IAP requirements and restore behavior;
- web checkout risk in a shell;
- subscription copy, pricing, trial, cancellation, and support links;
- failed purchase states;
- metadata and screenshots that mention paid features.

Output payment risk, required implementation changes, and review-note language.
