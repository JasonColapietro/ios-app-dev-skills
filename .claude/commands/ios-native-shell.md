---
description: Design a native SwiftUI shell for an existing website or web app.
---

# /ios-native-shell

Input: `$ARGUMENTS` - URL, product brief, shell repo path, or native-shell ask.

Use the `site-to-ios-app` and `ios-swiftui-product` skills.

Prefer a native shell when a raw web wrapper would be weak:

- native tab/navigation model;
- onboarding and empty states;
- settings with support, privacy, terms, account deletion, and restore when
  relevant;
- WebView only where the site remains the correct product surface;
- native error, offline, loading, retry, share, and deep-link behavior;
- DEBUG-only demo states for screenshots.

Output an architecture plan, file map, build command, and App Review rationale.
