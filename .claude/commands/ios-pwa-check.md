---
description: Inspect PWA and mobile-web readiness before turning a site into an app.
---

# /ios-pwa-check

Input: `$ARGUMENTS` - URL, web repo, or mobile-readiness request.

Use the `site-to-ios-app` skill.

Check the web surface before native work:

- viewport and safe-area behavior;
- manifest, icons, theme color, display mode, and installability;
- route depth and auth boundaries;
- mobile navigation, keyboard, forms, media, and payments;
- privacy, terms, support, and account deletion links.

Output web blockers that should be fixed before `/ios-capacitor-wrap` or
`/ios-native-shell`.
