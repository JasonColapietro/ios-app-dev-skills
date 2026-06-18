# Public-Safe Proprietary iOS Method

This repository publishes the public-safe layer of a proprietary iOS App Factory
method: repeatable agent skills, slash commands, checklists, and scripts that can
turn a keyword, website, or product concept into an App Store-ready native app
path. It does not publish private credentials, unreleased source code, Apple
account internals, revenue data, certificates, provisioning profiles, or App
Store Connect tokens.

## Method Stack

| Phase | Skill combo | Output |
| --- | --- | --- |
| Market wedge | `ios-app-factory` + `ios-aso-launch` | Keyword thesis, competitor angle, metadata draft |
| Native product | `ios-swiftui-product` | SwiftUI architecture, state model, QA path |
| Web-to-app | `site-to-ios-app` + `ios-capacitor-shell` | App Store-safe shell or native rewrite plan |
| Screenshot capture | `ios-screenshot-taker` + `/ios-shot` | Deterministic simulator captures for named app states |
| Store creative | `ios-aso-launch` + `/ios-screens` | Screenshot order, captions, feature truth, keyword fit |
| Release gate | `ios-app-store-release` + `/ios-grade` | Build, metadata, privacy, secrets, and submission readiness |
| Launch loop | `ios-app-factory` + release notes | Version updates, review-safe copy, measurement loop |

## Operating Pattern

```text
keyword or site
  -> app thesis
  -> SwiftUI app or Capacitor shell
  -> screenshot-state hooks
  -> simulator capture
  -> ASO metadata and screenshot framing
  -> release preflight
  -> App Store Connect upload only when explicitly delegated
```

## Screenshot Taker Role

The screenshot taker is the evidence step. It builds the app, boots a named
simulator, installs the `.app`, launches deterministic states, and captures PNGs
with `xcrun simctl`. Those raw captures then become framed App Store assets.

Example:

```bash
scripts/take_ios_screenshots.sh \
  --workspace MyApp.xcworkspace \
  --scheme MyApp \
  --device "iPhone 15 Pro Max" \
  --output AppStore-Screenshots/raw \
  --screens home,detail,paywall \
  --app-args "--ui-testing"
```

## Public Boundary

The method is designed to be shareable on GitHub. Public outputs may mention app
names, public App Store links, public bundle IDs, generic workflow steps, and
sanitized scripts. Public outputs must not include private Apple credentials,
key material, account-only screenshots, private phone numbers, private support
credentials, real customer data, or unreleased claims.

See [App Store submissions and approved apps](app-store-submissions.md) for the
current public showcase snapshot.
