---
description: Grade iOS implementation plus App Store readiness and emit PASS/BLOCK.
---

# /ios-grade

Input: `$ARGUMENTS` - app project path.

Use `ios-app-factory`, `ios-swiftui-product`, and `ios-aso-launch`.

## Scorecard

Grade 100 points total:

- 50 implementation: build, core flow, onboarding, monetization, persistence,
  settings, error handling, tests, design.
- 50 ASO/release: keyword research, metadata limits, screenshots, icon, privacy,
  reviewer notes, launch measurement.

Automatic BLOCK:

- build fails,
- metadata exceeds limits,
- keyword field repeats name/subtitle words or uses trademarks,
- screenshots missing,
- privacy truth unknown,
- secrets committed,
- metadata claims missing features.

Write a scorecard and list concrete fixes to reach PASS.

