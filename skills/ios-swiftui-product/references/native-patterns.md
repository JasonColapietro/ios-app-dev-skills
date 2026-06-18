# SwiftUI Product Patterns

## Core Package Pattern

Use a Swift package for non-UI behavior:

- API clients,
- DTOs and domain models,
- generation or polling state machines,
- StoreKit/product mapping,
- persistence adapters,
- parsing/scoring logic,
- tests.

This makes `swift test` useful and prevents UI previews from becoming the only
test surface.

## SwiftUI Shell Pattern

Use SwiftUI for:

- navigation,
- view composition,
- environment injection,
- local UI state,
- accessibility and layout,
- screenshot/demo states.

Avoid putting network state machines directly in view bodies.

## App Review Risk Checks

- Hide unloaded or unavailable IAP rows.
- Include Restore Purchases when paid features exist.
- Do not mention providers or vendors in user-visible copy unless intended.
- Add `PrivacyInfo.xcprivacy` when required-reason APIs are used.
- Use `#if DEBUG` around preview-only helpers that should not compile into
  Release.
- Avoid false provenance, ownership, or verification claims until implemented.

## Screenshot Harness

Create a DEBUG-only mode like:

```text
-uiDemo -uiScreen home|history|paywall|settings
```

The harness should seed local deterministic data and never require production
credentials.

