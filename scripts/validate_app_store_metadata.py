#!/usr/bin/env python3
import pathlib
import sys

LIMITS = {
    "name.txt": 30,
    "subtitle.txt": 30,
    "keywords.txt": 100,
    "promotional_text.txt": 170,
}

def clean(text: str) -> str:
    return text.rstrip("\n")

def words(text: str) -> set[str]:
    out = set()
    for raw in text.replace(",", " ").replace(":", " ").replace("-", " ").split():
        token = "".join(ch.lower() for ch in raw if ch.isalnum())
        if token:
            out.add(token)
    return out

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_app_store_metadata.py <metadata-locale-dir>")
        return 2
    root = pathlib.Path(sys.argv[1])
    failures = []
    values = {}
    for filename, limit in LIMITS.items():
        path = root / filename
        if not path.exists():
            failures.append(f"missing {path}")
            continue
        value = clean(path.read_text(encoding="utf-8"))
        values[filename] = value
        if len(value) > limit:
            failures.append(f"{filename} is {len(value)} chars, limit {limit}")
    keywords = values.get("keywords.txt", "")
    if ", " in keywords:
        failures.append("keywords.txt contains spaces after commas")
    repeated = (words(values.get("name.txt", "")) | words(values.get("subtitle.txt", ""))) & set(
        token.strip().lower() for token in keywords.split(",") if token.strip()
    )
    if repeated:
        failures.append(f"keywords repeat name/subtitle words: {', '.join(sorted(repeated))}")
    if failures:
        print("metadata validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("metadata validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

