#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CODEX_SKILLS="${CODEX_HOME:-$HOME/.codex}/skills"
CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"

mkdir -p "$CODEX_SKILLS" "$CLAUDE_HOME/skills" "$CLAUDE_HOME/commands"

cp -R "$ROOT"/skills/* "$CODEX_SKILLS/"
cp -R "$ROOT"/skills/* "$CLAUDE_HOME/skills/"
cp -R "$ROOT"/.claude/commands/* "$CLAUDE_HOME/commands/"

echo "Installed iOS app dev skills:"
echo "  Codex:  $CODEX_SKILLS"
echo "  Claude: $CLAUDE_HOME/skills and $CLAUDE_HOME/commands"

