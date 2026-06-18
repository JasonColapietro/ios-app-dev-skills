---
description: Plan or build a Capacitor iOS wrapper around a website.
---

# /ios-capacitor-wrap

Input: `$ARGUMENTS` - URL, web repo path, app name, or Capacitor request.

Use the `site-to-ios-app` and `ios-capacitor-shell` skills.

Create a Capacitor path only when the site can support a real iOS app:

- choose remote shell or bundled shell and explain why;
- preserve the repo package manager and lockfile;
- configure iOS app name, bundle ID, icons, splash, associated domains, and
  native plugins;
- run web build and `cap sync ios`;
- list simulator/device tests for auth, deep links, payments, offline, and
  keyboard behavior.

Output touched files, commands, channel risk, and release gate status.
