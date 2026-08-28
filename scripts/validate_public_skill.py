#!/usr/bin/env python3
"""Minimal, dependency-free validation for the public repository."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "apple-develop" / "SKILL.md"
PRIVATE_PATTERNS = (
    r"/Users/",
    r"silasd",
    r"D\.Silas diary",
    r"DIARY_API_TOKEN",
    r"SAFARI_READING_STANDARD",
)


def main() -> int:
    errors: list[str] = []
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    for field in ("name:", "description:", "version:", "author:", "license:"):
        if field not in text:
            errors.append(f"SKILL.md missing {field}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".json", ".txt"} and path.name not in {"LICENSE", ".gitignore"}:
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for pattern in PRIVATE_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                errors.append(f"private pattern {pattern!r} in {path.relative_to(ROOT)}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: public skill structure and privacy scan")
    return 0


if __name__ == "__main__":
    sys.exit(main())
