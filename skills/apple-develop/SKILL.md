---
name: apple-develop
description: Use Apple's current guidance as an iterative design and engineering inquiry, then apply the resulting platform semantics through implementation on iOS, iPadOS, macOS, visionOS, and Apple web or hybrid surfaces. Use when designing, reviewing, implementing, or debugging Apple-platform experiences; choosing native patterns, controls, materials, navigation, accessibility behavior, frameworks, or web-content carriers; or testing whether a product decision actually fits Apple's platform model.
metadata:
  version: "1.0.0"
  author: "D. Silas (R-Lucas-AI)"
  license: "MIT"
  tags: "apple-development,ios,ipad-os,macos,visionos,semantic-search,design"
---

# Apple Develop

## Purpose

Prevent attractive but semantically wrong design, and implement it correctly on Apple platforms. Apple Developer Search is the mandatory inquiry surface: ask with product intent, observe the semantically selected result set on the Apple Search page, open the relevant documentation, videos, sample code, and current-WWDC material, then refine the question when the set exposes a gap. Treat this ranked official corpus as Apple's answer to the question; do not require a separate generated-prose panel. Model the experience before styling it, choose the web/hybrid carrier by boundary rather than habit, and require visual and behavioral evidence before calling the work complete.

This skill is an independent community project and is not affiliated with or endorsed by Apple Inc. It requires a callable browser surface capable of submitting a question on Apple Developer Search and exposing the rendered result set. If that surface is unavailable, report the inquiry as incomplete rather than implying that it occurred.

Read the references:

- Read `references/design-gates.md` for every design or review task.
- Read `references/apple-developer-inquiry.md` whenever current Apple guidance could materially affect a design, API, framework, accessibility, privacy, or platform decision.
- Read `references/apple-search-evaluation.md` when changing this skill, evaluating Apple Search behavior, or running a regression set against realistic Apple-platform questions.
- Read `references/official-source-map.md` before selecting an Apple control, material, icon, template, or platform measurement, and before WebKit/hybrid implementation.
- Read `references/webkit-hybrid.md` when the task involves embedding web content in an Apple app, JS↔Native communication, or hybrid debugging.
- For web content authoring so Safari Reader / Reading List work well, read the Safari web-content section in `references/official-source-map.md` and apply semantic HTML, metadata, media, and offline guidance appropriate to the project.
- Read `references/spatial-design-visionos.md` and `references/spatial-input-visionos.md` for visionOS, spatial layout, gaze/hand input, glass windows, ornaments, or translating screen UI into space.
- For motion and interaction physics (springs, velocity, interruptibility, momentum), apply current Apple motion guidance and verify the result on the target platform. A compatible motion-design skill may supplement this workflow, but is not required.

## Design workflow

### 0. Run an Apple design inquiry

Before committing to a platform pattern or framework, turn the product problem into a concrete question for Apple Developer Search. Include the user's job, target platform and OS floor, important constraints, and the decision you need to make. Ask about the problem, not a guessed API name or a bag of keywords.

Submit the real question on the rendered Apple Search page. A successful first step is an observable, question-specific result set whose categories can include documentation, videos, sample code, and current-WWDC material. Judge success by semantic relevance and useful coverage, not by whether the page produces a prose summary, an `Answer` tab, an AI notice, or a `Sources` block.

Choose the smallest inquiry level that can resolve the decision:

- `Quick`: one narrow component, API, availability, or version question. Verify the answer in at least one current official source; no full design contract is required.
- `Standard`: a product decision with meaningful platform, accessibility, privacy, state, or framework tradeoffs. Use one intent-rich question, focused follow-ups as needed, and a compact decision record.
- `Deep`: a new interaction model, architecture boundary, high-impact AI/privacy decision, cross-platform behavior, or unresolved contradiction. Inspect multiple official source families, compare alternatives, and record uncertainties and verification gates.

Use this loop:

`Ask → inspect ranked result set → open relevant results → identify gaps → re-ask → compare → decide`

Capture each round in the result-set ledger from `references/apple-developer-inquiry.md`. Normalize duplicate URLs, preserve rank and content type, and mark which items were actually opened. The first result set is a routing hypothesis, not the conclusion. Check whether its top results reflect the product model, confuse two stages or concepts, assume a newer deployment target, omit accessibility/privacy/user control, or over-index on one framework.

Map the question to the decision dimensions that can change the outcome, such as interaction semantics, framework/API, privacy, accessibility, failure behavior, implementation examples, and platform/version. Do not require every dimension for every question. Re-ask only for a named missing or contradictory dimension; do not generate several synonymous queries merely to increase recall.

Stop when the decision-changing uncertainties are resolved, every implementation-changing claim has at least one current official anchor, and another question would only return substantially the same evidence. If the submitted question or its rendered result set cannot be observed on the Apple Search page, the inquiry is incomplete; diagnose the browser surface and report the blocker. Do not bypass the question step with a general web search or a preselected documentation URL.

See `references/apple-developer-inquiry.md` for question construction, follow-up lenses, evidence handling, and stopping rules.

### 1. Establish the design contract

Write a compact contract before editing:

- `User job`: what the person is trying to accomplish.
- `Primary content`: what deserves attention before interface chrome.
- `Platform and context`: iOS, iPadOS, macOS, visionOS, responsive web, or static communication artifact.
- `Surface`: the exact screen, component, state, or card series in scope.
- `Success signal`: observable behavior or visual outcome.
- `Do-not-change`: data, workflow, brand, or product boundaries to preserve.

Do not treat "looks Apple-like" as a user job.

### 2. Model content and space

List each visible item and give it exactly one primary role:

- content
- navigation
- action
- selection
- status
- metadata
- decoration

Then define the spatial hierarchy:

1. primary content plane
2. navigation and control plane
3. transient overlay plane
4. ambient or decorative plane

Keep controls elevated from content without turning content into chrome. Remove anything whose role cannot be stated in one short phrase.

### 3. Map intent to a platform pattern

Create a semantic mapping before drawing or coding:

| Intent | Candidate pattern | Evidence | State/behavior | Why it fits |
| --- | --- | --- | --- | --- |

Use the Apple inquiry findings, then consult the cited HIG pages and official Design Resources. Prefer a native pattern when its semantics match. Do not copy a component merely because its material, radius, or animation looks appealing.

Reject a mapping when one visual object combines unrelated meanings. Chapter title, episode label, pagination, and selection state are separate concepts unless the product model proves otherwise.

### 4. Define content hierarchy before visual tokens

Use real or representative content. Specify:

- reading order
- title and body relationship
- metadata that can be removed or deferred
- truncation and long-content behavior
- empty, loading, error, selected, disabled, and destructive states
- localization and Dynamic Type or text-scaling risk

Only then choose typography, spacing, color, radius, materials, and imagery.

### 5. Use official resources deliberately

Use the inquiry to locate the relevant official material, then read the source itself. Use official Apple UI kits, templates, SF Symbols, fonts, and HIG pages as measurement and behavior references. Record:

- source URL or local artifact
- inquiry question and result-set evidence that led to it, when applicable
- platform/version
- publication or update date when visible, stable/beta status, API availability, and whether a newer source supersedes it
- component or template name
- extracted semantic rule
- extracted measurement, if relevant
- license or reuse boundary

Community files may inspire composition, but they do not override platform semantics. Never infer behavior from a screenshot alone.

### 6. Implement one coherent pass

Keep a pass reviewable: one component family, hierarchy problem, or flow at a time. Preserve product contracts and user data. Reuse an existing project design system before introducing new tokens.

For static cards or images, do not add fake buttons, toolbars, page controls, or glass panels unless they communicate real state or interaction in the publishing context. A static artifact may borrow hierarchy and visual language without pretending to be an app screen.

### 7. Verify with evidence

Run every applicable check in `references/design-gates.md`.

Minimum evidence:

- static or syntax checks
- real content and edge states
- desktop and mobile, or target platform sizes
- screenshot or rendered artifact inspected at full size and thumbnail size
- semantic scan for meaningless controls, mixed concepts, internal labels, and fake interaction
- accessibility checks appropriate to the platform

Do not say "visually verified" without viewing the result. Test passing does not prove design correctness.

For hybrid surfaces, additionally verify: navigation and UI delegate separation, configuration ownership, cookie/identity policy, and the Web Inspector strategy.

### 8. Record the decision

For each durable decision, record:

- problem
- inquiry question(s) and unresolved assumptions
- official source or product evidence
- chosen pattern
- rejected alternative and why
- verification evidence
- remaining uncertainty

Convert repeated corrections into a gate or reference rule, not another isolated note.

## Development decisions (Apple web / hybrid)

Before embedding web content, choose the carrier by boundary, not by habit:

1. `SFSafariViewController` is the default for in-app browser-like experiences without deep customization.
2. `WKWebView` only when content changes frequently, web tech expresses layout/styling better, and the app must interact with the content. Its governance entry is `WKWebViewConfiguration`, not the view.
3. WebKit for SwiftUI (`WebView` / `WebPage`) when the deployment floor is iOS/iPadOS/macOS/visionOS 26+ and navigation events should be an auditable `AsyncSequence` state machine.

Never default to WKWebView merely to open a page; a web view exposes the app's permission boundary to web content.

- Protocolize all JS↔Native communication: JS→Native is event/intent reporting; Native→JS is state injection/command dispatch. Bidirectional traffic needs request IDs, version, error codes, permissions, timeouts, and logs.
- Keep navigation control (`WKNavigationDelegate`) and native UI responses (`WKUIDelegate`) as separate responsibilities.
- Treat cookies and cache as system state (`WKWebsiteDataStore`, `WKHTTPCookieStore`): Cookie is the hybrid identity boundary.
- Make the Web Inspector strategy part of the architecture: inspectable content, DOM/JS debugging, page loading timeline.
- Record every carrier/architecture decision with reasons and rollback; do not bury selection judgment in code.

See `references/webkit-hybrid.md` for the three-carrier table, security checklist, red lines, and official anchors.

## Non-negotiable rules

- Start from user intent and content, not material effects.
- Do not treat Apple Search ranking as self-validating; open and read the official results before making a claim.
- Do not claim an Apple inquiry occurred unless the question was submitted on Apple Developer Search and the resulting ranked set was observed on that page.
- Do not replace a missing Apple Search inquiry with direct documentation search. The search result set routes the investigation; the opened official items supply the evidence.
- Do not ask only keyword or API-name questions when a product-intent question would expose the actual design tradeoff.
- Do not stop after the first answer when it misunderstood the product model, omitted a decision-changing constraint, or lacks an official source anchor.
- Do not equate more queries or more results with better evidence. Re-query only when it can resolve a named gap, and stop when the evidence set is materially stable.
- Do not count duplicate thumbnail/title links as separate evidence; normalize result URLs before assessing coverage.
- Do not use an old WWDC session as current implementation authority without checking availability, later documentation, and the target OS.
- Give every control a real action, selection, navigation, or state responsibility.
- Keep unrelated concepts in separate components.
- Use page controls only for ordered peer pages and keep chapter/episode labels separate.
- Use segmented controls for closely related choices that affect the same object, state, or view.
- Use SF Symbols semantically; do not invent decorative glyph systems casually.
- Keep Liquid Glass and other materials primarily in navigation/control layers unless official guidance and context support another use.
- Prefer system familiarity, legibility, and accessibility over novelty.
- Treat human aesthetic approval as a gate, not as a substitute for semantic correctness.
- Do not transfer visionOS glass, hover, ornament, or spatial measurements to iOS, macOS, web, or static media without proving that the destination has the same interaction and environmental constraints.
- Never trigger a consequential action from hover alone; require explicit activation and keep hover, pressed, selected, disabled, and dwell states distinct.
- Do not introduce `WKWebView` just to display a page; choose the simplest carrier whose boundary fits.
- Do not run three web carriers in one app without an explicit division-of-responsibility table.
- Do not build JS↔Native bridges with arbitrary string concatenation, schema-less messages, or unauthorized permission calls.
- Do not ship a hybrid surface without a Web Inspector / observability strategy.
- Keep every hybrid selection decision in a reviewable decision record.

## Required output during design work

Match the output to the inquiry level.

For `Quick`, state the question, the relevant returned item, the answer derived from opening it, and any version caveat.

For `Standard` or `Deep`, before implementation state:

1. inquiry level, submitted Apple Search question(s), observed result categories and top relevant items, opened official anchors, and remaining uncertainty
2. design contract
3. content/space hierarchy
4. semantic component mapping
5. smallest pass
6. verification plan

After implementation, report the evidence and remaining risk. If the source, behavior, or target platform is unclear, stop before broad styling and resolve the model first.
