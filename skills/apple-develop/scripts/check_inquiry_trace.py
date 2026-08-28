#!/usr/bin/env python3
"""Check objective completeness of an observed Apple Search inquiry trace."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


def canonical_url(value: str) -> str:
    parts = urlsplit(value.strip())
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_inquiry_trace.py TRACE.json", file=sys.stderr)
        return 2

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors: list[str] = []

    for field in ("question", "searchUrl", "observedAt", "locale", "browser"):
        if not data.get(field):
            errors.append(f"missing {field}")

    if data.get("observedOnPage") is not True:
        errors.append("observedOnPage must be true")

    results = data.get("results")
    if not isinstance(results, list) or not results:
        errors.append("results must be a non-empty list")
        results = []

    seen_urls: set[str] = set()
    opened = 0
    freshness_checked = 0
    for index, result in enumerate(results, start=1):
        prefix = f"results[{index}]"
        for field in ("rank", "type", "title", "url", "whyRelevant"):
            if result.get(field) in (None, ""):
                errors.append(f"{prefix} missing {field}")
        if isinstance(result.get("rank"), int) and result["rank"] < 1:
            errors.append(f"{prefix} rank must be positive")
        if result.get("url"):
            url = canonical_url(result["url"])
            if url in seen_urls:
                errors.append(f"{prefix} duplicates canonical URL {url}")
            seen_urls.add(url)
        if result.get("opened") is True:
            opened += 1
            if result.get("freshnessChecked") is True:
                freshness_checked += 1

    if results and opened == 0:
        errors.append("at least one result must be opened")

    required = set(data.get("requiredDimensions") or [])
    covered = set(data.get("coveredDimensions") or [])
    if not required:
        errors.append("requiredDimensions must name decision-changing dimensions")
    unknown_covered = covered - required
    if unknown_covered:
        errors.append("coveredDimensions contains undeclared dimensions: " + ", ".join(sorted(unknown_covered)))

    version_sensitive = bool(data.get("targetPlatform") or data.get("targetOSFloor") or "version" in required)
    if version_sensitive and opened and freshness_checked == 0:
        errors.append("version-sensitive inquiry needs freshnessChecked on an opened result")

    for index, follow_up in enumerate(data.get("followUps") or [], start=1):
        if not follow_up.get("question") or not follow_up.get("namedGap"):
            errors.append(f"followUps[{index}] needs question and namedGap")
        elif follow_up["namedGap"] not in required:
            errors.append(f"followUps[{index}] namedGap is not in requiredDimensions")
        if follow_up.get("materialChange") not in (True, False):
            errors.append(f"followUps[{index}] materialChange must be boolean")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    missing = sorted(required - covered)
    print("PASS")
    print(f"results={len(results)} opened={opened} unique_urls={len(seen_urls)}")
    print("missing_dimensions=" + (", ".join(missing) if missing else "none"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
