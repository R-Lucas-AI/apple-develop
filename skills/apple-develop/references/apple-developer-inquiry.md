# Apple Developer Inquiry

Use this workflow when current Apple guidance could change a design or engineering decision. The goal is to ask a real product question on Apple Developer Search, use its semantically ranked official result set to route the investigation, read the relevant items, and translate the evidence into a product decision.

Treat Apple Developer Search as an intent-aware entry into Apple's knowledge base, not as a keyword index and not as a requirement to obtain generated prose. Its answer is the question-specific collection and ordering of documentation, videos, sample code, and current-WWDC material. The result set chooses where to look; the opened official items provide the evidence.

## Submit the question first

Do not begin with a probe keyword such as `Xcode`. Enter the real question in the Apple Search field and submit it on the rendered page. Confirm three observable facts:

1. the field or URL contains the intended question
2. the page returns a non-empty result set
3. the leading items or category mix are plausibly related to the intent rather than merely sharing one word

The category tabs and returned items are the answer surface. Record the visible categories, the top relevant items, their types, and why they appear to address the question. A prose answer, `Answer` tab, AI notice, or `Sources` block may exist in some variants, but none is a completion requirement.

If submission fails or no results render, try one clean browser session or an official localized route and repeat once. Network/API inspection is diagnostic only; success must be observed on the rendered Apple Search page.

## Keep a result-set ledger

Record enough page evidence to reproduce each inquiry without copying the entire page:

```text
Question:
Apple Search URL:
Observed at:
Locale/browser:
Target platform and OS floor:
Decision dimensions:

Rank | Type | Title | Canonical URL | Why relevant | Opened
```

Preserve the rendered order. Normalize URLs by removing fragments, tracking parameters, and duplicate presentation links; a video thumbnail and title pointing to the same canonical URL are one result. `Why relevant` is a short judgment based on the title and snippet, not a claim that the source proves anything. Mark `Opened` only after reading the destination page or transcript.

For each opened item, add:

```text
Published/updated:
Platform/version:
Stable or beta:
Availability/deprecation:
Decision-changing evidence:
Product interpretation:
```

## Choose inquiry depth

Use the least expensive level that still covers the risk.

| Level | Use when | Minimum evidence | Output |
| --- | --- | --- | --- |
| `Quick` | One API, component, availability, deployment, or version fact | Verify the answer in one current official source | Question, anchor, answer, caveat |
| `Standard` | A product decision has meaningful state, accessibility, privacy, platform, or framework tradeoffs | One intent-rich question, focused follow-ups when a named gap remains, and official anchors for every implementation-changing claim | Compact decision table and verification plan |
| `Deep` | New interaction model, architecture boundary, consequential AI/privacy behavior, cross-platform system, or contradictory guidance | Multiple relevant official source families, explicit alternative comparison, failure states, and unresolved uncertainty | Full design contract, decision record, and release gates |

Escalate when the answer reveals a decision-changing gap. De-escalate or stop when further questioning would only restate evidence. Never require a full design contract for a narrow lookup.

## Form the first question

Ask about the product intent before naming a presumed solution. Include only context that changes the answer:

- what the person is trying to do
- target Apple platform and deployment floor
- the product's content or state model
- constraints such as provenance, privacy, offline behavior, latency, accessibility, or user control
- the concrete decision or tradeoff under review

Useful shape:

> I'm designing [experience] for [platform/version]. People need to [job]. The product must preserve [constraint] and avoid [failure]. Which Apple design guidance and frameworks should shape this interaction, and what tradeoffs should I evaluate?

Do not begin with a list of guessed framework names unless the task is specifically an API lookup. A broad keyword query often hides the semantic question that should be tested.

## Inspect the answer

Extract four things before acting:

1. **Interpretation** — what do the ranking and category mix imply about how Apple matched the user's intent?
2. **Candidates** — which returned items are likely to change the design or engineering decision?
3. **Evidence** — what do the opened HIG pages, documentation, videos, sample code, or release notes actually say?
4. **Gaps** — what important constraint, state, platform difference, or failure mode is absent from the set or the opened material?

Open and read the official anchors for every decision-changing claim. Distinguish:

- sourced Apple guidance
- the search answer's synthesis or inference
- your product-specific judgment

Never infer a rule from a title or snippet alone. Open the result and distinguish what the official material says from your product-specific judgment. If the returned set lacks a usable anchor, refine the question or carry the point forward as uncertainty.

## Check decision coverage

Derive only the dimensions that can change this decision. Common dimensions are:

- interaction semantics and user control
- framework or API boundary
- privacy, permission, and data handling
- accessibility and alternative input
- failure, offline, loading, and recovery behavior
- implementation example or sample code
- platform, deployment floor, availability, and migration

Do not impose a fixed quota by category. A narrow symbol lookup may need one current documentation page; a new AI interaction may require HIG, privacy, accessibility, framework, and sample-code evidence. When a necessary dimension is absent, name it before writing a follow-up.

## Re-ask with purpose

Each follow-up should resolve a named uncertainty, challenge an assumption, or compare alternatives. Useful lenses include:

- **Correct the model:** “Don't treat this primarily as [misread concept]. [Product distinction] must remain true. How does that change the interaction?”
- **User control:** “Which parts should remain explicitly user-controlled rather than inferred, rewritten, or triggered automatically?”
- **Accessibility:** “How should this behave with VoiceOver, Switch Control, reduced motion, larger text, or alternative input?”
- **Privacy and provenance:** “What must stay visible, reversible, permissioned, or recoverable?”
- **Platform and version:** “Which recommendations depend on [OS version], and what is the supported fallback?”
- **Framework boundary:** “Compare [A] and [B] for this exact boundary. What capabilities, permission surfaces, or ownership models differ?”
- **Failure states:** “What should happen when the network, model, transcription, navigation, or synchronization is wrong or unavailable?”

Do not repeat the first question with synonyms. A follow-up must change the evidence or sharpen the decision.

After a follow-up, compare the two ledgers: note new canonical URLs, disappeared results, meaningful rank changes, and which missing dimension was filled. If the evidence set is materially unchanged, stop rather than producing more paraphrases. Multi-query expansion can increase retrieval volume without improving end-to-end decisions once reranking, reading time, and context limits apply.

## Compare and decide

Build a compact decision table:

| Product requirement | Apple guidance or framework | Official anchor | Product interpretation | Confidence / gap |
| --- | --- | --- | --- | --- |

Prefer current sources that match the deployment target. Resolve contradictions by checking version, platform, publication/update date, and whether one source is design guidance while another is API capability. Generated answers, forum posts, and community artifacts cannot override current official documentation.

Treat freshness as a decision gate, not metadata decoration. For implementation-changing evidence, identify the target OS and Xcode version, whether the source describes beta software, the API availability range, and whether a later documentation update or current sample supersedes an older WWDC implementation. Older sessions can still support durable rationale, but not current API syntax or availability without corroboration.

The final recommendation must say:

- what Apple guidance supports
- what remains a product judgment rather than an Apple rule
- which alternative was rejected and why
- how the decision will be verified in the real artifact
- what uncertainty remains

## Completion gate and recovery

Stop the inquiry when:

- decision-changing claims have current official anchors
- the product model and platform/version assumptions are explicit
- relevant accessibility, privacy, user-control, and failure-state gaps are addressed
- remaining uncertainty is recorded and another question would only repeat existing evidence

Do not impose a fixed number of rounds. A component lookup may need one answer plus source verification; a new interaction model may need several focused follow-ups.

The inquiry is complete only when all of these are true:

1. the question was entered and submitted on Apple Developer Search (`https://developer.apple.com/search/` or an official localized equivalent)
2. the question-specific result set was visibly rendered on that page
3. its categories, ranking, and relevant items were inspected
4. the decision-relevant official items were opened and read

Merely opening the Apple Search page, reading indexed page text, observing the input field, or finding the same topic through a search engine does not satisfy this gate.

Before starting, detect which browser surfaces are callable. Use a browser that can submit the real question, render the result set, and expose its interactive state. If the first browser stalls or cannot expose the resulting page, try one clean session or official localized route. Browser recovery may include checking visible DOM state, waiting for the result list, checking for a sign-in or script error, switching Apple locale, or switching from an in-app browser to an available external browser.

If no available browser can submit the question and produce an observable result set, stop the Apple inquiry and record the failure:

```text
Inquiry level: Standard
Apple Search URL: https://developer.apple.com/search/
Question submitted: [exact question, or "no" if submission was impossible]
Result set observed on page: no
Browser surfaces attempted: [surfaces]
Locales and account state attempted: [routes; signed in/out]
Failure state observed: [timeout, sign-in, script error, empty result region, or other visible state]
Inquiry status: incomplete
Next requirement: restore a browser surface that can submit the question and expose the result set
```

Direct official documentation is opened after the Apple Search result set routes the investigation. It cannot replace the initial question-and-result step.

Never invent returned results or imply that an Apple Search inquiry occurred when the question was not submitted and observed on the rendered page.

When validating or changing this workflow, read `apple-search-evaluation.md` and use `scripts/check_inquiry_trace.py` for objective trace checks. The script does not judge semantic relevance; inspect that manually on the rendered page.
