# App Store Release Runbook

## Preflight

```bash
bash scripts/ios_preflight.sh
python3 scripts/validate_app_store_metadata.py fastlane/metadata/en-US
git status --short
```

Confirm:

- clean or understood worktree,
- no secrets staged,
- build number is unique,
- version number is intentional,
- screenshots exist,
- review notes are current,
- App Privacy answers match the SDKs in the binary.

## Archive

```bash
xcodebuild archive \
  -project App.xcodeproj \
  -scheme App \
  -configuration Release \
  -archivePath build/App.xcarchive \
  -allowProvisioningUpdates \
  CODE_SIGN_STYLE=Automatic
```

Use `-workspace` instead of `-project` when the app has a workspace.

## Export

```bash
xcodebuild -exportArchive \
  -archivePath build/App.xcarchive \
  -exportPath build/export \
  -exportOptionsPlist ExportOptions.plist \
  -allowProvisioningUpdates
```

## Upload Options

Fastlane:

```bash
fastlane deliver --skip_binary_upload false --force
```

altool fallback:

```bash
xcrun altool --upload-app \
  --type ios \
  --file build/export/App.ipa \
  --apiKey "$APP_STORE_CONNECT_API_KEY_ID" \
  --apiIssuer "$APP_STORE_CONNECT_ISSUER_ID"
```

## Submission Gate

Do not submit while:

- build is still processing,
- screenshots or privacy are incomplete,
- IAP products are missing and visible in the UI,
- metadata claims unavailable features,
- user has not explicitly confirmed submission.

