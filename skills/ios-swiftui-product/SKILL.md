---
name: ios-swiftui-product
description: "Use when designing, implementing, reviewing, or repairing native SwiftUI iOS apps. Covers SwiftUI architecture, XcodeGen projects, Swift packages, StoreKit, Sign in with Apple, SwiftData/local persistence, screenshot/demo harnesses, UI state, release/debug boundaries, and app-development quality gates."
---

# iOS SwiftUI Product

## Architecture Preference

Prefer a testable core module plus a thin SwiftUI app shell:

- core package: networking, models, parsing, generation/polling, persistence,
  StoreKit abstractions, deterministic tests;
- SwiftUI target: navigation, views, environment injection, UI state, visuals.

Read `references/native-patterns.md` for implementation guidance.

## Product Surface Checklist

- First-run onboarding or empty state.
- Core feature with loading, success, error, and retry states.
- History or library.
- Saved set, watchlist, favorites, or comparable retention hook.
- Settings with restore, support, privacy, terms, and manage subscription.
- Review prompt only after successful user value.
- Debug-only demo harness for screenshots, guarded out of Release builds.

## Release Boundaries

- Keep preview/demo bypasses behind DEBUG flags or launch arguments that do not
  ship in Release behavior.
- Ensure StoreKit and Sign in with Apple flows do not leak test-only shortcuts.
- Verify backgrounding, cancellation, duplicate taps, and charge/refund paths.

