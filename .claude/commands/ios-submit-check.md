---
description: Run the final PASS/BLOCK check before App Store upload or review submission.
---

# /ios-submit-check

Input: `$ARGUMENTS` - app project, archive path, version/build, or release brief.

Use `ios-app-store-release`, `ios-aso-launch`, `ios-screenshot-taker`,
`ios-swiftui-product`, and `site-to-ios-app` when the app came from a site.

Block submission until:

- release build passes;
- bundle ID, version, build, signing, and account are identified;
- metadata passes limits and feature truth;
- screenshots exist and match the actual app;
- privacy answers and review notes are ready;
- no secrets or signing artifacts are staged;
- the user explicitly delegates upload or submission.

Output `PASS` or `BLOCK`, exact blockers, and the next command to run.
