---
name: site-to-ios-app
description: "Use when converting any website, web app, PWA, SaaS dashboard, content site, or marketplace into an iOS app using the public Suede-originated site-to-iOS workflow. Covers URL audit, App Store 4.2 wrapper-risk checks, Capacitor or native-shell strategy, native value requirements, iOS build scaffolding, screenshots, metadata, privacy, and release gating."
---

# Site to iOS App

## Principle

Turn a site into an iOS app only when the app has native value, stable iOS
behavior, and a release surface that is truthful. A raw web page in a frame is
not enough for an App Store-quality product.

This is the public Suede site-to-iOS workflow: audit first, choose the least
risky shell or native strategy, add iOS-specific value, and run an "impeccable"
ship gate before release.

## Start Here

Read `references/site-to-ios-runbook.md` before scaffolding or changing an
iOS wrapper.

If a URL is available, run the public audit helper:

```bash
python3 scripts/audit_site_for_ios.py https://example.com --out SITE_TO_IOS_AUDIT.md
```

Use `templates/site-to-ios/SITE_TO_IOS_PLAN.md` as the conversion artifact.

## Strategy Decision

Choose one route and write down why:

- Capacitor remote shell: live site remains the product surface and web deploys
  should update most content and behavior.
- Capacitor bundled shell: static/SPA assets are packaged into the binary and
  updates require App Store release unless paired with live APIs.
- Native SwiftUI shell with WebView: native navigation, settings, auth, push,
  share, error, and account surfaces wrap a site view.
- Full native rebuild: use when the site is mostly content, has weak mobile UX,
  or carries high wrapper rejection risk.

Use `ios-capacitor-shell` for Capacitor implementation details. Use
`ios-swiftui-product` when the app needs a native architecture or native shell.
Use `ios-aso-launch` and `ios-app-store-release` for screenshots, metadata, and
release gates.

## App Store 4.2 Gate

Block or redesign the app when it is only a bookmark, content mirror, or
unmodified website. Add native value before release:

- iOS-native onboarding, empty states, errors, offline, and retry.
- Native settings with support, privacy, terms, account deletion, restore, and
  notification controls where applicable.
- Universal links or deep links.
- Share sheet, widgets, push notifications, camera/media/file pickers, Apple
  Wallet, StoreKit, or other native capabilities only when they serve the app.
- Safe-area, keyboard, navigation, dark/light mode, and dynamic type handling.

## Conversion Flow

1. Audit the URL, responsive behavior, PWA assets, auth, payments, privacy,
   support, route depth, and mobile performance.
2. Pick the conversion strategy and write a `SITE_TO_IOS_PLAN.md`.
3. Scaffold or adapt the project using the repo's package manager and iOS
   project conventions.
4. Configure bundle ID, display name, app icon, launch screen, associated
   domains, Info.plist usage strings, and entitlements.
5. Implement native value and failure states before visual polish.
6. Run web build and `cap sync ios` for Capacitor shells.
7. Test on simulator or device across first launch, auth, deep links, tabs,
   keyboard, payments, offline, backgrounding, and account flows.
8. Produce App Store screenshots, metadata, privacy answers, and review notes.
9. Run the ship gate. Do not submit unless the user explicitly delegates public
   release and confirms the exact app, bundle ID, version, build, and account.

## Completion Bar

Do not call the app release-ready until:

- the iOS project builds on a named simulator, device, or CI target,
- every native plugin and entitlement is justified by actual behavior,
- the web route or bundle strategy is documented,
- the App Store 4.2 risk has a mitigation,
- screenshots and metadata match implemented features,
- privacy answers match the actual SDKs, cookies, analytics, and account flows,
- no secrets, signing material, or private account identifiers are committed.
