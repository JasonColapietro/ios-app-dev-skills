---
name: ios-app-factory
description: "Use when planning, creating, or orchestrating a complete iOS app-development workflow from idea or keyword to ship gate. Covers keyword-first product selection, native SwiftUI scaffolding, monetization, screenshots, ASO metadata, legal/compliance, grading, release handoff, and slash-command orchestration such as /ios-ship-app, /ios-new-app, /ios-grade, and /ios-release."
---

# iOS App Factory

## Principle

Build the app and its App Store surface together. A useful app that nobody can
find fails; great ASO on a broken app also fails. Treat implementation and ASO
as equal halves of the product.

## Default Pipeline

1. Choose a winnable target keyword before building.
2. Scaffold native SwiftUI unless the user explicitly asks for a wrapper.
3. Build the core loop: input, processing, structured result, history, saved set.
4. Add monetization only when it does not block v1 credential or review flow.
5. Produce App Store screenshots and metadata as first-class artifacts.
6. Run the ship gate: build, metadata, screenshots, privacy, secrets, feature truth.
7. Release only after explicit user confirmation for public submission.

Read `references/factory-pipeline.md` for the detailed phase map.

## Public-Safe Defaults

- Use placeholder bundle IDs like `com.example.product`.
- Use environment variables for App Store Connect credentials.
- Do not include private account IDs, phone numbers, real API keys, certificates,
  provisioning profiles, or `.p8` files in outputs.
- For first versions, prefer a free or no-account v1 if monetization credentials
  or IAP setup would delay validation.

## Slash Commands

This skill pairs with the repository slash commands:

- `/ios-ship-app` - run the whole pipeline.
- `/ios-keyword` - keyword and competitor scan.
- `/ios-new-app` - scaffold or plan the native app.
- `/ios-screens` - screenshot capture and marketing frame.
- `/ios-grade` - ship-gate scorecard.
- `/ios-release` - archive/upload/submit checklist.

## Completion Bar

Do not call an app ship-ready until:

- the app builds on a named simulator or CI target,
- the core flow works with real or deterministic demo data,
- App Store metadata passes char limits and keyword rules,
- screenshots exist at required sizes,
- privacy/legal answers match actual SDK behavior,
- no secrets or signing assets are committed,
- the user has confirmed any outward submission action.

