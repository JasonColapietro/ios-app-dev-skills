# iOS App Dev Skills

Public-safe skills and slash commands for building, grading, packaging, and
shipping iOS apps with AI coding agents.

This package distills a real iOS app-factory workflow into reusable skills:
keyword-first product selection, native SwiftUI scaffolding, App Store
Optimization, screenshot production, release gating, App Store Connect upload,
Capacitor shell maintenance, and public Suede-originated site-to-iOS
conversion.

It intentionally does **not** include secrets, signing material, private API
keys, private repo paths, Apple account identifiers, or App Store Connect
credentials. Bring your own Apple Developer account and environment variables.

## Proven App Store Output

![App Store submission board](docs/showcase/app-store-submissions-board.png)

This public-safe pack documents the reusable layer of a proprietary iOS App
Factory method used across multiple submitted and approved apps. See
[App Store submissions and approved apps](docs/app-store-submissions.md) for the
current catalog snapshot, and [the public-safe proprietary method](docs/proprietary-ios-method.md)
for the skill combination.

## What Is Included

### Skills

- `ios-app-factory` - one-prompt iOS app pipeline from keyword to ship gate.
- `ios-swiftui-product` - native SwiftUI product architecture and QA.
- `ios-screenshot-taker` - deterministic simulator capture for named app states.
- `ios-aso-launch` - App Store keyword, metadata, screenshots, and launch ops.
- `ios-app-store-release` - archive, upload, TestFlight, and review submission.
- `ios-capacitor-shell` - Capacitor shell inspection, sync, and release logic.
- `site-to-ios-app` - turn any site into an App Store-quality iOS app path.

### Slash Commands

Claude Code slash commands live in `.claude/commands/`:

- `/ios-ship-app`
- `/ios-keyword`
- `/ios-new-app`
- `/ios-shot`
- `/ios-screens`
- `/ios-grade`
- `/ios-release`
- `/ios-capacitor`
- `/ios-site-app`

### Templates And Scripts

- `templates/fastlane/` - sanitized Fastlane App Store Connect templates.
- `templates/xcodegen/` - minimal XcodeGen project scaffold.
- `templates/app-store-metadata/` - deliver-compatible metadata files.
- `templates/release/` - export options and reviewer notes template.
- `templates/site-to-ios/` - reusable conversion plan.
- `scripts/ios_preflight.sh` - local Xcode/Fastlane/env preflight.
- `scripts/take_ios_screenshots.sh` - simulator build/install/launch screenshot capture.
- `scripts/audit_site_for_ios.py` - static site-to-iOS readiness audit.
- `scripts/validate_app_store_metadata.py` - App Store char-limit checks.
- `scripts/validate_skill_pack.py` - skill/slash-command sanity checks.
- `scripts/install.sh` - copy skills and commands into local agent folders.

## Install For Codex

```bash
git clone https://github.com/JasonColapietro/ios-app-dev-skills.git
cd ios-app-dev-skills

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Example prompts:

```text
Use $ios-app-factory to turn "AI agent rating" into a keyword-first iOS app plan.
```

```text
Use $ios-app-store-release to preflight this Xcode project for App Store upload.
```

```text
Use $ios-screenshot-taker to capture home, detail, and paywall screenshots on iPhone 15 Pro Max.
```

```text
Use $site-to-ios-app to turn https://example.com into an iOS app plan.
```

## Install For Claude Code

Project-level install:

```bash
git clone https://github.com/JasonColapietro/ios-app-dev-skills.git
cd your-ios-project

mkdir -p .claude/skills .claude/commands
cp -R ../ios-app-dev-skills/skills/* .claude/skills/
cp -R ../ios-app-dev-skills/.claude/commands/* .claude/commands/
```

Then use:

```text
/ios-ship-app ai habit tracker for guitar practice
```

```text
/ios-site-app https://example.com as an App Store-ready iOS app
```

## Public Safety

- Do not commit `.p8`, `.xcconfig` secrets, `.env`, certificates, provisioning
  profiles, API keys, or App Store Connect tokens.
- Do not publish private App Store Connect app IDs, reviewer phone numbers, or
  private support credentials in generated reports.
- Do not submit to App Review unless the user explicitly delegates that release
  action and confirms the exact app, bundle ID, version, build, and account.
- Keep release templates generic. Use environment variables for credentials.

## Workflow

```text
idea / seed keyword
  -> keyword and competitor scan
  -> native SwiftUI scaffold or site-to-iOS conversion
  -> monetization and legal truth
  -> deterministic screenshot capture
  -> screenshots and ASO metadata
  -> scorecard gate
  -> archive, upload, TestFlight, submit
  -> launch measurement loop
```

The default ship gate is:

- build succeeds,
- App Store metadata passes limits and keyword rules,
- screenshots exist and are conversion-oriented,
- no secrets are committed,
- no metadata claims unbuilt features,
- explicit human confirmation before public submission.

## Validate

```bash
python3 scripts/validate_skill_pack.py .
python3 scripts/validate_app_store_metadata.py templates/app-store-metadata
bash -n scripts/take_ios_screenshots.sh
bash scripts/ios_preflight.sh
python3 scripts/audit_site_for_ios.py https://example.com
```

## License

MIT.
