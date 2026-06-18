---
name: ios-aso-launch
description: "Use when creating or reviewing App Store Optimization for iOS apps: keyword research, competitor scans, App Store name/subtitle/keyword fields, screenshots, promotional text, descriptions, localization keyword fields, launch measurement, and slash commands such as /ios-keyword, /ios-screens, and /ios-grade."
---

# iOS ASO Launch

## Rule

Search language belongs in the App Store keyword surfaces. Product
differentiation belongs in screenshots, the description body, and promo text.

## Workflow

1. Search the App Store landscape for the user's seed phrase.
2. Pick one target keyword with real intent and low enough competition.
3. Write name, subtitle, and keyword field under strict App Store limits.
4. Create outcome-first screenshots. Screenshot #1 sells the result; #2 sells
   the differentiator.
5. Put claims through a feature-truth check. Never advertise missing features.
6. Use localization keyword fields for extra reach when relevant.
7. Set a 2-4 week measurement plan for rankings, impressions, conversion, and
   promo text/caption iteration.

Read `references/app-store-aso.md` for the exact rules.

## Hard Limits

- App name: 30 characters.
- Subtitle: 30 characters.
- Keyword field: 100 characters, comma-separated, no spaces after commas.
- Promotional text: 170 characters.

## Output Artifacts

- `aso/keywords.md`
- `aso/aso-doc.md`
- `fastlane/metadata/<locale>/name.txt`
- `fastlane/metadata/<locale>/subtitle.txt`
- `fastlane/metadata/<locale>/keywords.txt`
- `fastlane/metadata/<locale>/description.txt`
- `fastlane/metadata/<locale>/promotional_text.txt`
- screenshot title plan and ordered screenshot assets.

