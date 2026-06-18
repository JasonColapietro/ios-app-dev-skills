---
description: Run the full iOS app factory workflow from idea or keyword to release-ready gate.
---

# /ios-ship-app

Input: `$ARGUMENTS` - app idea, seed keyword, or existing app path.

Use the `ios-app-factory`, `ios-swiftui-product`, `ios-aso-launch`, and
`ios-app-store-release` skills.

## Flow

1. Parse the app idea, target user, platform constraints, and whether this is a
   new native app or existing project.
2. Run keyword research and pause for target keyword approval.
3. Create or adapt the native SwiftUI architecture.
4. Plan monetization. Prefer free v1 when IAP setup blocks validation.
5. Produce visual direction, icon spec, and screenshot plan.
6. Write ASO metadata and validate character limits.
7. Write privacy/legal/reviewer-note checklist.
8. Run the ship gate and produce PASS/BLOCK.
9. If PASS, prepare release commands. Do not submit without explicit user
   confirmation.

Output a concise execution report with artifact paths and remaining manual
touchpoints.

