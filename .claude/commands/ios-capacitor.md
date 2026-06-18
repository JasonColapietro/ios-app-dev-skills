---
description: Inspect, fix, sync, or release a Capacitor iOS shell around a web app.
---

# /ios-capacitor

Input: `$ARGUMENTS` - shell path or bug/release request.

Use the `ios-capacitor-shell` skill.

First determine whether the requested fix ships through web deploy or native
binary rebuild. Then:

- use the repo lockfile package manager,
- run build and `cap sync ios`,
- verify native plugins and entitlements,
- test auth bridges,
- release only when native changes require it.

Output which channel ships the fix: web deploy, native rebuild, or both.

