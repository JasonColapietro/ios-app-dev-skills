---
description: Plan iOS deep links, universal links, and associated domains for a web-to-app build.
---

# /ios-deeplinks

Input: `$ARGUMENTS` - URL routes, bundle ID, domain, or existing iOS project.

Use the `site-to-ios-app`, `ios-capacitor-shell`, and `ios-swiftui-product`
skills.

Map the app route strategy:

- primary universal-link domains;
- route-to-screen mapping;
- fallback web URLs;
- associated domains entitlement;
- `apple-app-site-association` requirements;
- app launch behavior from links, notifications, share sheet, and QR codes.

Output the route map, entitlement changes, site file requirements, and tests.
