---
description: Add or review offline, loading, error, and retry behavior for an iOS app.
---

# /ios-offline

Input: `$ARGUMENTS` - app path, site shell, URL, or resilience issue.

Use the `site-to-ios-app`, `ios-capacitor-shell`, and `ios-swiftui-product`
skills.

App Store-quality apps need failure states:

- first launch with no network;
- expired auth session;
- failed payment or unavailable checkout;
- slow media/API loading;
- back/forward navigation failure;
- retry, cached state, and support escalation.

Output required states, implementation target, and simulator/device test steps.
