# iOS Screenshot Capture Runbook

## Capture Plan

Start with a short plan:

1. Device classes required by the listing.
2. Screens or states to capture.
3. Launch arguments or seeded data needed to reach each state.
4. Output folder and naming convention.
5. Whether the result is raw captures, framed store screenshots, or both.

For Apple listings, prioritize the largest required iPhone device first. Add iPad
only when the app supports iPad or the listing requires iPad-specific assets.

## Recommended Command

From a project root that contains an Xcode project or workspace:

```bash
path/to/ios-app-dev-skills/scripts/take_ios_screenshots.sh \
  --workspace MyApp.xcworkspace \
  --scheme MyApp \
  --device "iPhone 15 Pro Max" \
  --output AppStore-Screenshots/raw \
  --screens home,detail,paywall \
  --app-args "--ui-testing"
```

Use `--project` instead of `--workspace` for a plain Xcode project. Use
`--bundle-id` only when the script cannot detect the bundle ID from the built
`.app`.

## App Hooks

The cleanest app hook is a launch-argument router:

```swift
let arguments = ProcessInfo.processInfo.arguments
if let index = arguments.firstIndex(of: "--screenshot-state"),
   arguments.indices.contains(index + 1) {
    appState.routeForScreenshot(arguments[index + 1])
}
```

Keep screenshot states stable and demo-safe. Avoid production accounts and real
personal data.

## QA Checks

- File dimensions match the device that was captured.
- Status bar, keyboard, permissions, and loading states are intentional.
- Every screenshot opens locally and is not black, blank, or stale.
- App Store copy does not claim features absent from the captured app.
- Raw simulator screenshots are separated from final framed marketing exports.
