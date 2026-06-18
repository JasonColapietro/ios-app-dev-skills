---
name: ios-app-store-release
description: "Use when preparing, archiving, uploading, or submitting iOS apps through App Store Connect. Covers xcodebuild archive/export, Fastlane deliver, altool/transporter fallback, TestFlight, review submission, App Privacy, export compliance, release safety, and slash commands such as /ios-release and /ios-grade."
---

# iOS App Store Release

## Safety Boundary

Uploading or submitting to App Store Connect is an outward release action. Do it
only when the user explicitly delegates that action and confirms the exact app,
bundle ID, version, build number, and account.

## Workflow

1. Identify the app target, scheme, bundle ID, version, build, and signing mode.
2. Run `scripts/ios_preflight.sh` or equivalent local checks.
3. Verify metadata, screenshots, legal URLs, privacy answers, and reviewer notes.
4. Archive with `xcodebuild archive`.
5. Export with `xcodebuild -exportArchive` using app-store-connect export options.
6. Upload with Fastlane, altool, notarytool/transporter, or Xcode Organizer.
7. Wait for processing before attaching a build or submitting review.
8. Submit only after final confirmation.

Read `references/release-runbook.md` before performing release work.

## Credential Rules

- Use environment variables and local keychain/account state.
- Do not print raw API keys, `.p8` contents, certificates, provisioning
  profiles, or tokens.
- Do not commit generated `.ipa`, `.xcarchive`, profiles, or private key files.

## Common Release Checks

- Release build compiles.
- `PrivacyInfo.xcprivacy` exists when required APIs are used.
- `ITSAppUsesNonExemptEncryption` is correctly set.
- App icon catalog is configured.
- Device family and orientations match App Store metadata.
- IAP products referenced by the binary exist or gracefully hide when missing.

