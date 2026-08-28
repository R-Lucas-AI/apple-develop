# Apple Develop

Apple Develop is an independent Agent Skill for design and engineering decisions on Apple platforms.

Instead of treating Apple Developer Documentation as a static keyword database, the skill starts by submitting the real product question to [Apple Developer Search](https://developer.apple.com/search/). It records the semantically ranked documentation, videos, sample code, and WWDC results, opens the decision-relevant sources, checks missing dimensions and version constraints, and asks a focused follow-up only when the evidence has a named gap.

## What it adds

- Intent-rich questions before framework selection
- A reproducible result-set ledger with canonical URLs
- Decision-dimension coverage for accessibility, privacy, failure behavior, implementation, and platform/version
- Source-depth and freshness gates
- Focused follow-ups instead of synonym-heavy multi-query expansion
- A regression rubric and an objective inquiry-trace checker
- Apple-platform design, visionOS, WebKit, and hybrid implementation guidance

## Install

Copy `skills/apple-develop` into your Agent Skills directory, or install it from this repository with a compatible skill manager.

For Codex:

```bash
mkdir -p ~/.codex/skills
cp -R skills/apple-develop ~/.codex/skills/apple-develop
```

Then invoke it explicitly with `$apple-develop`, or let a compatible agent select it automatically for Apple-platform design and implementation work.

### SkillHub.cn package

SkillHub.cn uses additional frontmatter fields that the standard Codex validator doesn't accept. Generate a platform-compatible package without changing the source skill:

```bash
python3 scripts/build_skillhub_package.py
skillhub publish .dist/skillhub/apple-develop --dry-run
```

After reviewing the dry run, remove `--dry-run` to publish from an authenticated SkillHub CLI session.

## Requirements

- A browser or browser-control tool that can submit a question on Apple Developer Search and expose the rendered result set
- Python 3 only if you want to run `scripts/check_inquiry_trace.py`

The browser interaction is part of the evidence contract. If an agent cannot observe the submitted question and rendered results, the Apple Search inquiry is incomplete.

## Validation

```bash
python3 skills/apple-develop/scripts/check_inquiry_trace.py tests/fixtures/valid-trace.json
python3 scripts/validate_public_skill.py
python3 scripts/build_skillhub_package.py
```

## 中文说明

Apple Develop 不是普通的 Apple 文档检索提示词。它要求 Agent 先在 Apple Developer Search 中提交完整产品问题，把返回的文档、视频、示例代码和 WWDC 内容视为 Apple 经过语义筛选的答案集合，再打开原文、检查版本与缺口，并仅在必要时定向追问。

国内发布包与 GitHub 源码保持一致，避免出现两个行为不同的版本。

## Independence and trademarks

This project is not affiliated with or endorsed by Apple Inc. Apple, Apple Developer, iOS, iPadOS, macOS, visionOS, Xcode, Swift, and related marks are trademarks of Apple Inc. No Apple logo or proprietary design asset is included.

## License

[MIT](LICENSE)
