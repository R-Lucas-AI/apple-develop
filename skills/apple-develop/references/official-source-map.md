# Official Apple Source Map

Use current official sources because platform guidance and resources change.

## Starting points

- Apple Developer Search: https://developer.apple.com/search/
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- HIG foundations: https://developer.apple.com/design/human-interface-guidelines/foundations
- Layout: https://developer.apple.com/design/human-interface-guidelines/layout
- Apple Design Resources: https://developer.apple.com/design/resources/
- SF Symbols: https://developer.apple.com/sf-symbols/
- Designing for visionOS: https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos
- Design for spatial user interfaces (WWDC23): https://developer.apple.com/videos/play/wwdc2023/10076/
- Design for spatial input (WWDC23): https://developer.apple.com/videos/play/wwdc2023/10073/

## Component routing

Search the HIG for the exact component before implementing it. Common routes:

- navigation bars, tab bars, sidebars, toolbars
- buttons, menus, popovers, sheets, alerts
- lists and tables
- search fields
- segmented controls
- page controls
- typography, color, materials, icons, images
- accessibility, writing, privacy, motion
- spatial layout for visionOS

For visionOS work, also inspect the current Apple Design Resources file rather than relying on screenshots or old measurements. The official Figma Community resource `1253443272911187215` is the Apple visionOS design library; verify its update date and platform version before extracting components.

For gaze, pinch, direct touch, hover, dwell, or custom gestures, use the WWDC23 spatial-input session for interaction rationale and the current visionOS UI kit for state names and geometry. Do not infer behavior from the Figma state thumbnails alone.

Useful direct pages:

- Page controls: https://developer.apple.com/design/human-interface-guidelines/page-controls
- Segmented controls: https://developer.apple.com/design/human-interface-guidelines/segmented-controls

## WebKit / hybrid starting points

- WebKit documentation: https://developer.apple.com/documentation/webkit
- WKWebView: https://developer.apple.com/documentation/webkit/wkwebview
- WebKit for SwiftUI: https://developer.apple.com/documentation/webkit/webkit-for-swiftui
- SFSafariViewController HIG: https://developer.apple.com/design/human-interface-guidelines/safari-view-controller
- What's new in WKWebView (WWDC22): https://developer.apple.com/videos/play/wwdc2022/10049/

## Safari 网页内容（web content authoring）

网页阅读 / Reader / Reading List 相关任务的官方入口：

- Safari Web Content Guide（总纲、兼容性、viewport、Web App 配置、离线存储）: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/
- Safari HTML Reference（Supported Meta Tags / Attributes / HTML Tags；figure/figcaption/alt 官方示例）: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariHTMLRef/Introduction.html
- Safari HTML5 Audio and Video Guide（iOS 播放策略、媒体格式、playsinline）: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/Introduction/Introduction.html
- Reading List（SSReadingList API）: https://developer.apple.com/documentation/safariservices/ssreadinglist
- Readability.js（Safari Reader 识别机制的开源参考实现）: https://github.com/mozilla/readability

Safari Reader 没有公开的「开关式」规范。将 Readability 等开源实现作为启发式参考，而不是 Apple 的正式兼容性契约；优先采用语义化正文结构、准确元数据、可访问媒体和稳健的渐进增强。

## Resource order

1. Current product implementation and real content.
2. Detect an available browser surface and choose `Quick`, `Standard`, or `Deep` inquiry depth.
3. Submit the intent-rich question through Apple Developer Search and inspect the semantically ranked documentation, video, sample-code, and current-WWDC results. This step is mandatory.
4. Open and read the decision-relevant official items returned by the search.
5. Current HIG page for the relevant platform and pattern.
6. Official Apple UI kit or template for the target OS version.
7. SF Symbols application and official symbol guidance.
8. Apple design videos or developer sessions for behavior that static docs do not explain.
9. Community design files only for secondary composition research.

Apple Developer Search is the mandatory semantic-routing layer. The observed result set identifies the official material to investigate; opening and reading those items supplies the evidence. A general web search or a preselected documentation URL is not a substitute for asking the product question on Apple Search.

## Evidence record

For every borrowed rule or measurement, record:

```text
Source:
Platform/version:
Component/template:
Rule or measurement:
Applied to:
Verification:
Reuse/license boundary:
```

Do not assume the newest OS design is the correct target. Match the product's deployment target and context. Do not copy Apple or community assets into distributable work without checking the applicable license.
