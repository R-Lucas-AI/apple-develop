# Spatial Design for visionOS

Use this reference only for visionOS or genuinely spatial interaction. Do not treat it as a universal glassmorphism guide.

## Verified sources

- Apple Figma Community file `1253443272911187215`, opened locally as **Apple Design Resources - visionOS**.
- File URL: https://www.figma.com/community/file/1253443272911187215
- Local file inspected: `nVch4B6NliUts7r5iqjPbT`.
- Resource description updated January 21, 2025; cover identifies it as visionOS 2 UI Kit.
- WWDC23 **Design for spatial user interfaces**: https://developer.apple.com/videos/play/wwdc2023/10076/
- HIG **Designing for visionOS**: https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos

The Figma resource requires the latest SF Symbols and is governed by the Apple Design Resources license.

## Resource anatomy

The official file contains dedicated pages for examples, alerts, app icons, backgrounds, buttons, checkboxes and toggles, color pickers, drop-downs, gestures, inputs, keyboards, lists, menus, navigation bars, notifications, page controls, pickers, progress indicators, search tokens, segmented controls, share sheets, sidebars, sliders, system activities, tab bars, toolbars, tooltips, window controls, colors, materials, typography, and license.

Its style vocabulary includes:

- Text: `Primary`, `Secondary`, `Tertiary`.
- Controls: `Idle`, `Hover`, `Pinch`, `Selected`, `Disabled`.
- Views: `Recessed Material View`, `Thin`, `Regular`, `Thicker`.
- Windows: `Glass`, `Glass - Keyboard`, and glass specular stroke.
- Effects: `Blur`, `Blur + Shadow Big`, `Blur + Shadow Small`, `Recessed`, `Recessed - Highlights only`.

Typography uses semantic styles: `XLTitle1`, `XLTitle2`, `LargeTitle`, `Title1–3`, `Headline`, `Body`, `Callout`, `Subheadline`, `Footnote`, `Caption1–2`.

## Core principles

### Preserve familiarity, adapt to space

Reuse established Apple component semantics so people can transfer knowledge from screen-based platforms. Adapt placement, material, feedback, and depth for spatial input; do not invent a new control language simply because the canvas is three-dimensional.

### Design for comfort and safety

- Keep important content within the comfortable field of view.
- Prefer wider canvases over taller ones because horizontal neck movement is generally easier than vertical movement.
- Keep primary content near the center.
- Avoid forcing repeated head, neck, or body movement.
- Keep motion restrained and provide a stable frame of reference.

### Design for gaze and hand input

- Provide at least a `60pt` targeting region for every interactive element.
- A standard visible button can be `44pt` if it has at least `8pt` of clear targeting space around it.
- When placing standard buttons in a row, use `16pt` spacing to preserve the 60pt targets.
- A visually small `28pt` control remains usable only when its effective targeting region is 60pt.
- Separate adjacent hover regions by about `4pt` so gaze feedback does not merge.
- Give a whole custom control a coherent hover shape; do not make people guess which subpart is interactive.
- System components already support gaze, hand, direct touch, voice, keyboard, and trackpad feedback; prefer them.

### Use concentric geometry

Nested rounded elements must feel concentric. Use this relationship:

```text
outer radius = inner radius + inset/padding
```

Use continuous corners and preserve the relationship across nested containers. A random shared radius is not the same as concentric geometry.

## Materials, color, and legibility

- Use the system glass window so the interface adapts to environmental light and remains anchored in the surrounding space.
- Avoid large opaque window backgrounds; they can feel heavy and constricting.
- Use darker material to separate structural regions such as a sidebar or to increase input contrast.
- Use lighter material to elevate interactive elements such as buttons.
- Avoid stacking light materials because contrast and legibility degrade.
- Prefer white text and symbols on glass when environmental color is unpredictable.
- If color is essential, apply it to a background or whole button rather than a small foreground detail.
- Prefer system colors because they dynamically adapt for contrast on glass.

Glass is an environmental and spatial material, not decoration. It communicates placement, depth, light response, and the possibility of content behind the window.

## Typography and vibrancy

- Use semantic text styles rather than isolated numeric sizes.
- Spatial text uses slightly heavier weights for distance legibility: body is heavier than its iOS counterpart; headings use stronger weights.
- Use the two extra-large title styles only when the wide spatial layout supports them.
- Avoid small or light custom typography even when the window can grow arbitrarily large.
- Use vibrancy to reinforce hierarchy on material:
  - primary for standard text and symbols
  - secondary for descriptive text, footnotes, and subtitles
  - tertiary for lower-priority supporting information

Do not flatten vibrancy hierarchy into three arbitrary opacity values outside the system material context.

## Component measurements observed in the official file

### Buttons

- Text buttons: Large `52pt`, Regular `44pt`, Small `32pt` high.
- Symbol buttons: Extra Large `64pt`, Large `52pt`, Regular `44pt`, Small `32pt`, Mini `28pt`.
- Button states include disabled, selected, hover, idle with platter, idle without platter; symbol buttons also include hover + dwell.
- Platter/no-platter is a contextual distinction, not a decorative toggle.

### Navigation bars

- Navigation bar height: `92pt` in the inspected kit.
- It carries hierarchy navigation, title, search, avatar, or trailing actions.
- It does not absorb unrelated page status or content metadata.

### Page controls

- Page controls are `28pt` high in the kit.
- They represent a flat ordered list of peer pages.
- They do not represent chapters, hierarchy, episode naming, or arbitrary progress metadata.

### Segmented controls

- Main segmented control height: `44pt`.
- The kit shows 2–5 segments with a single selected segment and enabled/disabled states.
- Use it for closely related choices affecting the same object, state, or view.

## Spatial structure patterns

### Window

Use a glass window as the primary content canvas. Window controls and content belong to a coherent spatial object rather than a pile of floating panels.

### Tab bar and sidebar

- Place the visionOS tab bar vertically at the leading edge, outside or attached to the window.
- Keep it lightweight; avoid more than about six top-level destinations.
- Let gaze expansion reveal labels without permanently stealing content space.
- Put subordinate navigation in a sidebar inside the window, adjacent to the tab bar.

### Ornament

- Use an ornament for persistent controls or a toolbar that benefits from depth and remains available across content.
- Prefer borderless buttons inside a clearly interactive ornament container.
- A bottom ornament can overlap the window edge by about `20pt` to feel attached without obscuring content.
- Hide or expand an ornament only when attention is focused on a single content experience.
- Do not add an ornament merely to make a flat design look spatial.

### Menus and popovers

- Allow menus and popovers to extend outside the window and appear near the person's gaze.
- Mark the invoking button as selected so the relationship remains obvious.
- In this platform context, reserve the white button background for selection rather than ordinary idle decoration.

### Modal views

- Center modal content and keep it at the active Z position.
- Push and dim the parent window to prevent interaction and clarify focus.
- Stack subsequent modals forward with another dimming layer.
- Prefer push navigation inside a modal for nested views rather than uncontrolled Z-axis stacking.
- Keep close and back actions in the established leading/top position.

## Translation gate

Before borrowing a visionOS rule, answer:

1. Does the destination use gaze/hand input or a 60pt spatial target?
2. Does environmental light pass through a spatial window?
3. Does Z depth carry navigation or modal meaning?
4. Can the person reposition the window in space?
5. Is hover feedback a primary discoverability mechanism?

If most answers are no, translate the underlying principle—legibility, hierarchy, target size, focus, or familiarity—rather than copying the glass, ornament, or measurements.
