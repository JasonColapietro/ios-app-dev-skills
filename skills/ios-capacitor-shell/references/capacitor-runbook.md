# Capacitor iOS Shell Runbook

## Inspect

```bash
test -f package.json && cat package.json
test -f capacitor.config.* && ls capacitor.config.*
find ios -maxdepth 4 -name Info.plist -o -name "*.entitlements"
```

Check whether the app bundles local web assets or redirects/loads a live URL.

## Sync

```bash
pnpm install
pnpm build
npx cap sync ios
```

Substitute the repo's package manager only when the lockfile confirms it.

## Native Vs Web Routing

Native binary changes:

- Info.plist,
- entitlements,
- associated domains,
- Capacitor plugin code,
- signing,
- icon/splash,
- app display name,
- native permissions.

Web-deployed changes:

- React/Next/Vue app code,
- web auth nonce logic,
- CSS/layout/content,
- remote API calls,
- route behavior when shell loads a live site.

## Sign In With Apple Bridge

Confirm:

- requested nonce and backend verification match,
- native presentation context is wired,
- associated domain/service ID/bundle ID are aligned,
- plugin patch survives install and sync.

