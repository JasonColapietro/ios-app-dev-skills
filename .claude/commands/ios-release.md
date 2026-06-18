---
description: Prepare archive, upload, TestFlight, and App Review submission for an iOS app.
---

# /ios-release

Input: `$ARGUMENTS` - app project path, scheme, version/build, or release brief.

Use the `ios-app-store-release` skill.

## Flow

1. Confirm exact app, bundle ID, version, build, signing mode, and account.
2. Run preflight and metadata validation.
3. Confirm worktree and no secrets staged.
4. Archive and export.
5. Upload to App Store Connect.
6. Wait for processing and attach build.
7. Submit only after explicit user confirmation.

Never print private keys or commit signing artifacts.

