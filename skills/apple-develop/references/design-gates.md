# Design Gates

Run these gates in order. A later gate cannot rescue a failed earlier gate.

## 1. Intent gate

- Is the user job stated without visual adjectives?
- Is the primary content identified?
- Is the artifact interactive UI or static communication?
- Are platform, device class, and context known?

## 2. Semantic gate

- Does every visible control have one clear responsibility?
- Are navigation, action, selection, status, metadata, and decoration distinct?
- Does the chosen Apple pattern match the actual behavior?
- Are separate concepts represented separately?
- Would removing an element reduce comprehension or capability? If not, remove it.

## 3. Content gate

- Is the reading order obvious?
- Is the title distinct from pagination, state, and metadata?
- Has low-value metadata been removed or deferred?
- Do real long strings, Chinese text, numbers, missing images, and empty content work?
- Does static output avoid fake affordances?

## 4. Spatial gate

- Is content on the primary plane and chrome on a control/navigation plane?
- Is spacing systematic rather than patched locally?
- Do safe areas, sidebars, toolbars, sheets, and overlays preserve usable content space?
- Does the layout adapt rather than merely shrink?
- Are touch or pointer targets appropriate to the target platform?
- For spatial input, does the effective target include its clear targeting region, and do adjacent hover regions remain distinct?

## 5. Platform gate

- Was the relevant HIG component page checked?
- Was an official UI kit or template inspected when measurements matter?
- Are SF Symbols, typography, materials, and control states used according to platform conventions?
- Is the platform/version recorded?

## 6. Accessibility gate

- Does text scale or wrap without loss?
- Is contrast sufficient in light/dark and active/inactive states?
- Is meaning available without relying on color alone?
- Do controls have accessible names, roles, states, focus, and keyboard behavior where applicable?
- Is motion optional or nonessential?
- Can every essential spatial action be completed without relying on gaze, hover, two hands, large movement, or a custom gesture alone?
- Does hover only preview responsiveness, with explicit activation required for consequential actions?

## 7. Visual evidence gate

- Inspect at target size.
- Inspect at the smallest supported size.
- Inspect at thumbnail or glance size for cards and series.
- Compare all peer screens/cards together for rhythm and consistency.
- Verify empty, loading, error, selected, disabled, and destructive states when relevant.
- Capture a screenshot or rendered artifact; do not rely on DOM or test output alone.

## 8. Release gate

- Static, syntax, and behavior checks pass.
- No placeholder, internal English object name, test label, emoji icon, or debug artifact is visible.
- No unsupported claim of HIG compliance remains.
- The change is reversible and the decision is recorded.
- Human aesthetic review is requested only for genuine preference choices, not unresolved semantic errors.
