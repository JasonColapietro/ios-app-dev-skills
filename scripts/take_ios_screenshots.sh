#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  take_ios_screenshots.sh --scheme SCHEME [--workspace APP.xcworkspace | --project APP.xcodeproj]
                          [--device "iPhone 15 Pro Max"] [--configuration Debug]
                          [--output DIR] [--screens home,detail,paywall]
                          [--bundle-id BUNDLE_ID] [--app-args "--ui-testing"]
                          [--wait 2] [--skip-build]

Builds an iOS app for Simulator, installs it, launches named screenshot states,
and captures PNGs with xcrun simctl. It does not use App Store Connect
credentials and does not submit anything publicly.
EOF
}

SCHEME=""
WORKSPACE=""
PROJECT=""
DEVICE="iPhone 15 Pro Max"
CONFIGURATION="Debug"
OUTPUT_DIR="AppStore-Screenshots/raw"
SCREENS_CSV="home"
BUNDLE_ID=""
APP_ARGS=""
WAIT_SECONDS="2"
SKIP_BUILD=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --scheme) SCHEME="${2:-}"; shift 2 ;;
    --workspace) WORKSPACE="${2:-}"; shift 2 ;;
    --project) PROJECT="${2:-}"; shift 2 ;;
    --device) DEVICE="${2:-}"; shift 2 ;;
    --configuration) CONFIGURATION="${2:-}"; shift 2 ;;
    --output) OUTPUT_DIR="${2:-}"; shift 2 ;;
    --screens) SCREENS_CSV="${2:-}"; shift 2 ;;
    --bundle-id) BUNDLE_ID="${2:-}"; shift 2 ;;
    --app-args) APP_ARGS="${2:-}"; shift 2 ;;
    --wait) WAIT_SECONDS="${2:-}"; shift 2 ;;
    --skip-build) SKIP_BUILD=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

if [ -z "$SCHEME" ]; then
  echo "error: --scheme is required" >&2
  usage
  exit 2
fi

if [ -n "$WORKSPACE" ] && [ -n "$PROJECT" ]; then
  echo "error: use --workspace or --project, not both" >&2
  exit 2
fi

if ! command -v xcodebuild >/dev/null 2>&1; then
  echo "error: xcodebuild is not available" >&2
  exit 1
fi

if ! command -v xcrun >/dev/null 2>&1; then
  echo "error: xcrun is not available" >&2
  exit 1
fi

if [ -z "$WORKSPACE" ] && [ -z "$PROJECT" ]; then
  WORKSPACE="$(find . -maxdepth 2 -name '*.xcworkspace' -print | sort | head -n 1)"
  if [ -z "$WORKSPACE" ]; then
    PROJECT="$(find . -maxdepth 2 -name '*.xcodeproj' -print | sort | head -n 1)"
  fi
fi

BUILD_ROOT="${TMPDIR:-/tmp}/ios-screenshot-build-$SCHEME"
DERIVED_DATA="$BUILD_ROOT/DerivedData"
mkdir -p "$OUTPUT_DIR" "$BUILD_ROOT"

BUILD_ARGS=(-scheme "$SCHEME" -configuration "$CONFIGURATION" -destination "platform=iOS Simulator,name=$DEVICE" -derivedDataPath "$DERIVED_DATA")
if [ -n "$WORKSPACE" ]; then
  BUILD_ARGS=(-workspace "$WORKSPACE" "${BUILD_ARGS[@]}")
elif [ -n "$PROJECT" ]; then
  BUILD_ARGS=(-project "$PROJECT" "${BUILD_ARGS[@]}")
fi

if [ "$SKIP_BUILD" -eq 0 ]; then
  echo "building $SCHEME for $DEVICE"
  xcodebuild "${BUILD_ARGS[@]}" build
else
  echo "skipping build; using existing products under $DERIVED_DATA"
fi

APP_PATH="$(find "$DERIVED_DATA/Build/Products/$CONFIGURATION-iphonesimulator" -maxdepth 1 -name '*.app' -print | sort | head -n 1)"
if [ -z "$APP_PATH" ]; then
  echo "error: no .app found under $DERIVED_DATA/Build/Products/$CONFIGURATION-iphonesimulator" >&2
  exit 1
fi

if [ -z "$BUNDLE_ID" ]; then
  BUNDLE_ID="$(/usr/libexec/PlistBuddy -c 'Print :CFBundleIdentifier' "$APP_PATH/Info.plist")"
fi

UDID="$(DEVICE_NAME="$DEVICE" python3 - <<'PY'
import json
import os
import subprocess
import sys

name = os.environ["DEVICE_NAME"]
data = json.loads(subprocess.check_output(["xcrun", "simctl", "list", "devices", "available", "-j"]))
for runtime, devices in data.get("devices", {}).items():
    for device in devices:
        if device.get("name") == name and device.get("isAvailable", True):
            print(device["udid"])
            sys.exit(0)
sys.exit(1)
PY
)"

if [ -z "$UDID" ]; then
  echo "error: simulator not found: $DEVICE" >&2
  exit 1
fi

echo "booting simulator $DEVICE ($UDID)"
xcrun simctl boot "$UDID" >/dev/null 2>&1 || true
xcrun simctl bootstatus "$UDID" -b

echo "installing $APP_PATH"
xcrun simctl install "$UDID" "$APP_PATH"

IFS=',' read -r -a SCREENS <<< "$SCREENS_CSV"
read -r -a EXTRA_ARGS <<< "$APP_ARGS"

index=1
for raw_screen in "${SCREENS[@]}"; do
  screen="$(echo "$raw_screen" | tr -cd '[:alnum:]_.-' | tr '[:upper:]' '[:lower:]')"
  if [ -z "$screen" ]; then
    continue
  fi
  printf -v prefix "%02d" "$index"
  out="$OUTPUT_DIR/$prefix-$screen.png"

  echo "capturing $screen -> $out"
  xcrun simctl launch --terminate-running-process "$UDID" "$BUNDLE_ID" --screenshot-state "$screen" "${EXTRA_ARGS[@]}"
  sleep "$WAIT_SECONDS"
  xcrun simctl io "$UDID" screenshot "$out"
  index=$((index + 1))
done

echo "screenshots written to $OUTPUT_DIR"
