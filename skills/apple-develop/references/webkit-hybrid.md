# WebKit / Hybrid Reference

This reference summarizes reusable WebKit and hybrid-app decision rules. Treat current official Apple documentation as authoritative when these notes conflict or when platform behavior changes.

## 1. Three carriers for web content in Apple apps

| Carrier | When to use | Boundaries / notes |
| --- | --- | --- |
| `SFSafariViewController` | In-app browser-like experience without deep customization. WWDC22 default. | Clear boundary, no deep control; share cookies/state with Safari. |
| `WKWebView` | Content changes frequently; web tech expresses layout/styling better; the app must interact with the content. iOS 8+, macOS 10.10+, visionOS 1+. | In-app web runtime boundary. Governance entry is `WKWebViewConfiguration`, not the view. |
| WebKit for SwiftUI (`WebView` / `WebPage`) | Deployment floor is iOS/iPadOS/macOS/Catalyst/visionOS 26+; navigation should be an auditable state machine. | `WebPage` load API returns an `AsyncSequence` of navigation events; `currentNavigationEvent` replaced by `navigations`. Fast-evolving; verify each needed capability against the current docs. |

`UIWebView` is deprecated: App Store rejects new apps since 2020-04 and updates since 2020-12.

## 2. Selection is boundary selection, not control selection

Core question: who owns the boundary, who owns the state, who owns the actions?

1. Default to `SFSafariViewController` unless deep interaction, controlled content, or a communication protocol is required.
2. Choose `WKWebView` only when the app must interact with the web content or the content is app-controlled.
3. Choose WebKit for SwiftUI when the OS floor allows it and navigation must be observable as events.
4. Write the selection decision with reasons and rollback; never bury the choice in code.

## 3. WKWebView key points

- `WKWebViewConfiguration` coordinates processes and configuration: user agent, app-bound domains, HTTPS upgrades, preferences, custom URL scheme handlers, website data store, media playback, viewport behavior.
- `WKNavigationDelegate` manages navigation (allow/deny, navigation action/response). `WKUIDelegate` presents native UI from web content (alerts, context menus, camera/mic permission). Keep the two responsibilities separate.
- `WKUserContentController` adds scripts and message handlers; `WKScriptMessageHandler` receives JS messages; `evaluateJavaScript` runs JS from native.
- `WKWebsiteDataStore` / `WKHTTPCookieStore` manage cookies, caches, and site data. Cookie is the identity boundary of a hybrid app; login-state mismatches, unclear cache policy, and multi-webview/multi-account privacy boundaries are the common failure modes.
- Web Inspector (Safari Developer Tools) inspects iOS/iPadOS devices, simulators, and in-app inspectable content: DOM, JS debugging, page loading timeline. No Web Inspector strategy means no maintainable hybrid app.

## 4. JS ↔ Native protocol design

- JS → Native: event / intent reporting.
- Native → JS: state injection / command dispatch / UI update.
- Bidirectional traffic requires: request IDs, version, error codes, permissions, timeouts, and logs.
- Red lines: no arbitrary string concatenation; no schema-less messages; no unauthorized permission calls; no audit-less handlers.

## 5. Security and permissions checklist

- app-bound domains
- HTTPS upgrade
- custom URL scheme scope
- cookie and `WebsiteDataStore` policy
- camera / microphone / download / file access
- production inspectable-content policy

## 6. Red lines

- Do not introduce `WKWebView` merely to open a page; that exposes the whole app permission boundary to web content.
- Do not run three web carriers in one app without an explicit division-of-responsibility table.
- Do not ship hybrid without an observability / Web Inspector strategy.
- Do not skip the decision record: selection, reasons, and rollback path.

## 7. Selection checklist

- [ ] Is the web content app-controlled?
- [ ] Is bidirectional JS ↔ Native communication required?
- [ ] Is navigation interception required?
- [ ] Is a custom URL scheme needed for local resources?
- [ ] Is the minimum OS version ≥ iOS 26?
- [ ] Is there a simpler `SFSafariViewController` solution?
- [ ] Is the selection rationale and rollback written down?

## 8. Official anchors

- WKWebView: https://developer.apple.com/documentation/webkit/wkwebview
- WebKit for SwiftUI: https://developer.apple.com/documentation/webkit/webkit-for-swiftui
- WebView (SwiftUI struct): https://developer.apple.com/documentation/WebKit/WebView-swift.struct
- Replacing UIWebView: https://developer.apple.com/documentation/webkit/replacing-uiwebview-in-your-app
- Updating Apps that Use Web Views: https://developer.apple.com/news?id=12232019b
- What's new in WKWebView (WWDC22): https://developer.apple.com/videos/play/wwdc2022/10049/
- iOS & iPadOS 26 Release Notes: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26-release-notes
