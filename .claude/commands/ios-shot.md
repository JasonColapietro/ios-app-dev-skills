---
description: Capture deterministic iOS simulator screenshots for a project.
---

# /ios-shot

Input: `$ARGUMENTS` - app path, scheme, simulator, bundle ID, output folder, or
state list.

Use the `ios-screenshot-taker` skill. If the request asks for App Store captions,
framing, keyword fit, or upload order, also use `ios-aso-launch`.

## Flow

1. Identify the exact Xcode project or workspace, scheme, bundle ID, and device.
2. Build for iOS Simulator.
3. Boot the requested simulator and install the built `.app`.
4. Launch with deterministic screenshot-state arguments when available.
5. Capture one sorted PNG per state with `xcrun simctl io screenshot`.
6. Report produced files, missing states, and whether more framing is needed.
