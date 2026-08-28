# Spatial Input and Hover for visionOS

Use this reference for gaze-and-pinch input, direct touch, custom gestures, hover effects, dwell, and spatial accessibility. Read it together with `spatial-design-visionos.md`.

## Sources and evidence boundary

- WWDC23 **Design for spatial input**: https://developer.apple.com/videos/play/wwdc2023/10073/
- HIG **Designing for visionOS**: https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos
- Apple Figma Community file `1253443272911187215`, visionOS 2 UI Kit, including `Gestures`, `Buttons`, `Tooltips`, and control states such as `Idle`, `Hover`, `Pinch`, `Selected`, `Disabled`, and `Hover + Dwell`.

The Developer app may not index older localized session titles reliably. Treat the canonical Apple video URL as the source of interaction rationale and the current UI kit as the source of visual states and measurements.

## Input model

### Indirect input: look, then pinch

- Design the target so gaze can identify it before the hand confirms it.
- Treat hover as pre-action feedback: it confirms what will respond if the person pinches.
- Never perform a consequential action on hover alone. Selection, purchase, deletion, navigation, and submission require an explicit activation.
- Do not expose or visualize a raw gaze cursor. Preserve the privacy and naturalness of eye targeting by responding through the control itself.
- Prefer system controls because their target expansion, hover, pinch, dwell, and accessibility behavior are already coordinated.

### Direct input: reach and touch

- Support direct touch when an element is intentionally placed within comfortable reach.
- Give direct-touch objects clear spatial boundaries and an obvious response surface.
- Do not require arm extension for frequent or primary tasks; indirect input must remain comfortable.
- Preserve the same semantic result across indirect and direct input. A button does not become a different command because it was touched instead of pinched.

### Gestures

- Start with familiar tap, drag, rotate, and scale semantics.
- Use custom gestures only when they are discoverable, reversible where possible, and materially better than a standard control.
- Provide a visible control or accessible alternative for any essential custom gesture.
- Avoid interactions that require two hands, large body movement, precise timing, or sustained posture unless the task inherently needs them.

## Hover rules

- Apply hover to the complete semantic control, not decorative sublayers.
- Match the hover shape to the control's perceived shape and content boundary.
- Keep neighboring hover regions separated so feedback does not flicker or merge; the inspected Apple kit uses about `4pt` between adjacent regions.
- Use hover to signal availability and focus, not to decorate idle content.
- Keep hover changes stable and restrained. Avoid large scale, position, depth, or brightness jumps that pull attention or create discomfort.
- Do not reveal essential labels, state, or instructions only on hover. Hover may reinforce meaning, but the interface must remain understandable without it.
- Distinguish `hover`, `pinch/pressed`, `selected`, `disabled`, and `dwell` states. They answer different questions and must not share one ambiguous appearance.

## Dwell and accessibility

- Treat dwell as an alternative activation path, not as permission to trigger ordinary hover actions.
- Ensure every interactive element has an accessible name, role, value/state, and activation behavior.
- Do not rely on color, depth, sound, motion, eye tracking, or hand tracking alone to communicate meaning.
- Support VoiceOver, Voice Control, Switch Control, Dwell Control, keyboard, and trackpad behavior wherever the platform provides them.
- Respect Reduce Motion and avoid motion coupled continuously to head or gaze movement when a stable alternative works.
- Keep text and controls legible against changing environmental content; verify high-contrast and reduced-transparency conditions where applicable.

## Target and spacing gate

- Effective interactive region: at least `60pt`.
- Standard visible control: `44pt` is acceptable with at least `8pt` clear targeting space around it.
- Standard controls in a row: use about `16pt` spacing to preserve effective target regions.
- Mini `28pt` controls are acceptable only when their effective target remains `60pt` and nearby targets do not compete.

Measure the effective target, not merely the visible platter.

## Required verification

For every spatial control, verify this state matrix:

| State or path | Required evidence |
| --- | --- |
| Idle | Meaning and availability are understandable without hover |
| Hover | Whole semantic target responds; feedback is stable |
| Pinch/press | Explicit activation feedback is distinct from hover |
| Selected | Persistent state is not confused with temporary hover |
| Disabled | Unavailable state remains legible and noninteractive |
| Dwell | Alternative activation does not create accidental actions |
| Direct touch | Same command and state model as indirect input |
| Accessibility | Named, operable, and understandable without one sensory or motor channel |

Reject the design if hover is carrying meaning that disappears for another input method.

## Translation gate

When translating to iOS, macOS, web, or static media:

- translate hover into focus/rollover feedback only on platforms that actually have a pointer or focus model;
- translate the `60pt` rule into the destination platform's target guidance rather than copying the number;
- omit hover from static artifacts;
- preserve the deeper principle: visible affordance, explicit activation, distinct persistent state, and equivalent alternative input.
