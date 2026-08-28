# Apple Search Evaluation

Use this reference when changing the Apple Search inquiry workflow or checking whether it still works on realistic tasks. Evaluate observable behavior, not whether an answer uses preferred wording.

## What to measure

Separate objective trace integrity from semantic quality.

Objective checks:

- the exact question was submitted on the rendered Apple Search page
- a non-empty ranked result set was observed
- result rank, type, title, canonical URL, and opened state were recorded
- duplicate presentation links were collapsed
- at least one decision-relevant official item was opened
- required decision dimensions and observed coverage were recorded
- implementation-changing evidence includes a version/freshness check
- every follow-up names the gap it is intended to resolve

Human/agent judgments:

- the leading results reflect the product intent rather than one shared keyword
- selected items collectively cover the dimensions that can change the decision
- opened sources actually support the extracted evidence
- version and platform assumptions match the product target
- a follow-up materially improves coverage or is correctly stopped

Run `scripts/check_inquiry_trace.py TRACE.json` for objective checks. A passing trace is necessary but does not prove semantic quality.

## Regression cases

Use a small diverse set; do not run every case for routine product work. Run at least one case from each affected class when changing the inquiry workflow.

| Class | Realistic question | Expected retrieval characteristics |
| --- | --- | --- |
| Exact symbol | For an iOS 17 app, when should I use `NavigationStack` rather than `NavigationSplitView`? | Current API/HIG material; platform and availability matter |
| Product intent | How should a voice-first iOS diary preserve original expression while allowing editable transcription? | HIG, speech, privacy/accessibility, and implementation material |
| AI/user control | An AI feature summarizes private journal entries but must never silently rewrite them. What interaction and privacy guidance applies? | Generative AI HIG, privacy, reversibility, fallback behavior |
| Accessibility | How should a custom recording control work with VoiceOver, Voice Control, larger text, and reduced motion? | Accessibility guidance plus control implementation |
| Version boundary | Compare the correct in-app web carrier for iOS 18 and an iOS 26+ deployment target. | SFSafariViewController, WKWebView, newer WebKit APIs, availability |
| Cross-platform | Which navigation model should remain shared and which should differ across iPhone, iPad, and macOS? | Platform-specific HIG and adaptive layout evidence |
| Failure behavior | What should a speech-to-text capture flow do when transcription is delayed, unavailable, or wrong? | Speech framework, loading/error/recovery, correction guidance |
| Sample implementation | Show the current Apple-supported way to index app content for semantic search, including a working sample. | Current docs, WWDC, sample code, OS/device requirements |
| Historical trap | Is a WWDC19 machine-learning interaction recommendation still valid for an iOS 27 implementation? | Durable rationale separated from current API authority |
| Hybrid security | A WKWebView needs authenticated JS-to-native messages and file uploads. What boundary and observability guidance applies? | WebKit configuration, permissions, bridge and inspector sources |

## Review rubric

Score each completed case from 0 to 2 on these dimensions:

- `Intent fidelity`: unrelated / partly aligned / clearly aligned
- `Evidence coverage`: decision-changing gaps / partial / sufficient
- `Source depth`: snippets only / some opened / all changing claims anchored
- `Freshness`: unchecked / partly checked / target-specific and current
- `Follow-up discipline`: synonym churn / useful but loose / named gap resolved or correctly stopped
- `Trace integrity`: unverifiable / incomplete / reproducible

Do not optimize only for a larger result count. Compare changes by whether they improve decision-relevant evidence without unreasonable extra queries, reading, or latency. Preserve failed and surprising cases; they are more useful for regression than hand-picked successes.

## Trace schema

```json
{
  "question": "...",
  "searchUrl": "https://developer.apple.com/search/...",
  "observedOnPage": true,
  "observedAt": "ISO-8601 timestamp",
  "locale": "zh-CN",
  "browser": "Safari",
  "targetPlatform": "iOS",
  "targetOSFloor": "17.0",
  "requiredDimensions": ["user-control", "privacy", "accessibility", "framework", "version"],
  "coveredDimensions": ["user-control", "privacy", "framework", "version"],
  "results": [
    {
      "rank": 1,
      "type": "documentation",
      "title": "Generative AI",
      "url": "https://developer.apple.com/design/human-interface-guidelines/generative-ai",
      "whyRelevant": "Addresses agency and reversible AI transformations.",
      "opened": true,
      "freshnessChecked": true
    }
  ],
  "followUps": [
    {
      "question": "...",
      "namedGap": "accessibility",
      "materialChange": true
    }
  ]
}
```
