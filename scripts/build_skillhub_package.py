#!/usr/bin/env python3
"""Build a SkillHub.cn-compatible package from the canonical Codex skill."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "apple-develop"
DESTINATION = ROOT / ".dist" / "skillhub" / "apple-develop"

PLATFORM_FIELDS = """slug: apple-develop
displayName: Apple Develop - Apple 开发设计与工程研究
summary: 先向 Apple Developer Search 提交完整产品问题，再阅读语义排序的官方文档、视频、示例代码和 WWDC 内容，检查版本与证据缺口后形成平台决策。
version: 1.0.0
"""


def main() -> int:
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    shutil.copytree(SOURCE, DESTINATION)

    skill_path = DESTINATION / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit("SKILL.md is missing YAML frontmatter")
    text = text.replace("---\n", "---\n" + PLATFORM_FIELDS, 1)
    skill_path.write_text(text, encoding="utf-8")
    print(DESTINATION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
