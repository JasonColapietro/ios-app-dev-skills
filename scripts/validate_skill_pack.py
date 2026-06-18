#!/usr/bin/env python3
import pathlib
import re
import sys

AUTH_PREFIX = "Auth" + "Key_"
PRIVATE_PREFIX = "-----BEGIN " + "PRIVATE " + "KEY-----"
GH_PREFIX = "g" + "ho_"

SENSITIVE_PATTERNS = [
    re.compile(AUTH_PREFIX + r"[A-Z0-9]+\.p8"),
    re.compile(PRIVATE_PREFIX),
    re.compile(GH_PREFIX + r"[A-Za-z0-9_]+"),
    re.compile(r"[A-Z0-9]{10}\s*/\s*issuer", re.I),
]

def validate_skill(path: pathlib.Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing frontmatter")
        return errors
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{path}: malformed frontmatter")
        return errors
    front = parts[1]
    if not re.search(r"^name:\s*[a-z0-9-]+$", front, re.M):
        errors.append(f"{path}: missing or invalid name")
    if not re.search(r"^description:\s*.+", front, re.M):
        errors.append(f"{path}: missing description")
    if "TODO" in text:
        errors.append(f"{path}: contains TODO")
    return errors

def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = []
    skill_files = sorted((root / "skills").glob("*/SKILL.md"))
    if not skill_files:
        errors.append("no skills/*/SKILL.md files found")
    for skill in skill_files:
        errors.extend(validate_skill(skill))
    command_files = sorted((root / ".claude" / "commands").glob("*.md"))
    if not command_files:
        errors.append("no .claude/commands/*.md files found")
    for path in root.rglob("*"):
        if path.is_file() and path.stat().st_size < 2_000_000:
            if path.name == "validate_skill_pack.py":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in SENSITIVE_PATTERNS:
                if pattern.search(text):
                    errors.append(f"{path}: possible secret pattern {pattern.pattern}")
    if errors:
        print("skill pack validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("skill pack validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
