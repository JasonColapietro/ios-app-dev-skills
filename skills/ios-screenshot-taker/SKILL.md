---
name: ios-screenshot-taker
description: "Use when capturing deterministic iOS simulator screenshots for App Store, TestFlight, QA, launch pages, or marketing decks. Covers xcodebuild build, simulator boot/install/launch, seeded demo states, xcrun simctl screenshots, required App Store device classes, public-safe output handling, and slash commands such as /ios-shot and /ios-screens."
---

# iOS Screenshot Taker

## Principle

Capture real app states, not imagined UI. The screenshot set should be
repeatable from a clean simulator and should map each image to a named product
state, device class, locale, and store-listing purpose.

## Workflow

1. Identify the Xcode project or workspace, scheme, bundle ID, simulator device,
   app version, build number, and target screenshot states.
2. Confirm the app can launch with deterministic demo data or safe seeded state.
3. Run `scripts/take_ios_screenshots.sh` from this repository when available, or
   follow the same `xcodebuild` and `xcrun simctl` sequence manually.
4. Capture one named PNG per app state and keep filenames sortable.
5. Hand the raw captures to `ios-aso-launch` or the app-store screenshot editor
   for marketing framing, captions, and required export sizes.

Read `references/screenshot-runbook.md` before doing non-trivial capture work.

## State Contract

Prefer launch arguments that the app can recognize, for example:

```text
--ui-testing --screenshot-state home
--ui-testing --screenshot-state detail
--ui-testing --screenshot-state paywall
```

If the app has no screenshot-state router, use the safest available path:
seed local demo data, launch the app, navigate manually once, then document any
manual steps in the output.

## Public-Safe Defaults

- Do not capture private user accounts, unreleased customer data, tokens, API
  keys, internal dashboards, private App Store Connect screens, or support
  contact details.
- Do not commit oversized raw screenshot folders unless the repository is meant
  to store release assets.
- Downscale README/showcase images and keep the original store-resolution files
  in the app release folder.
- Do not claim App Store approval from screenshot files alone; verify live Apple
  lookup or App Store Connect state separately.

## Required Output

Report:

- capture command used,
- simulator device and iOS runtime,
- app path or bundle ID,
- output directory,
- screenshot files produced,
- missing states or manual steps,
- whether the captures are raw QA screenshots or framed store assets.
