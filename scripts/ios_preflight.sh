#!/usr/bin/env bash
set -u

fail=0

check_cmd() {
  if command -v "$1" >/dev/null 2>&1; then
    printf "ok: %s -> %s\n" "$1" "$(command -v "$1")"
  else
    printf "missing: %s\n" "$1"
    fail=1
  fi
}

check_cmd xcodebuild
check_cmd xcrun
check_cmd git

if command -v fastlane >/dev/null 2>&1; then
  printf "ok: fastlane -> %s\n" "$(command -v fastlane)"
else
  printf "warn: fastlane not found; use xcodebuild/xcrun fallback or install fastlane\n"
fi

if command -v xcodegen >/dev/null 2>&1; then
  printf "ok: xcodegen -> %s\n" "$(command -v xcodegen)"
else
  printf "warn: xcodegen not found; needed only for XcodeGen templates\n"
fi

if git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "git root: $(git rev-parse --show-toplevel)"
  echo "git status:"
  git status --short
else
  echo "warn: not inside a git repo"
fi

for var in APP_IDENTIFIER TEAM_ID APP_STORE_CONNECT_API_KEY_ID APP_STORE_CONNECT_ISSUER_ID APP_STORE_CONNECT_API_KEY_PATH; do
  if [ -n "${!var:-}" ]; then
    echo "ok: $var is set"
  else
    echo "warn: $var is not set"
  fi
done

exit "$fail"

