---
name: ios-capacitor-shell
description: "Use when inspecting, fixing, building, or releasing a Capacitor iOS shell around a live web app. Covers native-vs-web change routing, cap sync, package-manager lockfiles, iOS plugins, entitlements, Sign in with Apple bridges, App Store wrapper risk, and release checks."
---

# iOS Capacitor Shell

## First Question

Determine whether the change is web-delivered or binary-delivered:

- web/JS/CSS/content change: deploy the web app.
- native plugin/entitlement/Info.plist/capacitor config change: rebuild and
  resubmit the iOS binary.

Read `references/capacitor-runbook.md` before modifying a shell.

## Wrapper Risk

Thin wrappers can be rejected under App Store Guideline 4.2. A shell needs
native value, stable auth, polished iOS behavior, and reliable offline/failure
states. Do not present a raw web page as a finished native app.

## Build Rule

Use the package manager locked by the repo. If the repo has `pnpm-lock.yaml`,
use pnpm. If plugin patches are installed by pnpm, npm install can silently
drop them.

## Completion Checks

- `cap sync ios` succeeds.
- Native plugins are present after sync.
- Entitlements and associated domains match the app's capabilities.
- Login/auth bridge works on device or simulator.
- Web fixes have actually been deployed if the shell loads a remote URL.

