# Innovation & Technology Scan

## Why this exists

Most apps are designed against conventions their designers absorbed earlier, so they risk launching dated and converging on the same patterns as competitors. Scanning what is emerging in interaction design, platform capabilities, accessibility, and adjacent technology gives the product a chance to feel current and to claim a useful distinguishing edge before it becomes table stakes.

The scan is about the app's best chance of succeeding, not novelty for its own sake.

## Method

1. **Search fresh.** Use live web research at project time rather than memory. Prefer current platform release notes, major developer-conference announcements, design-system changelogs, recent teardowns, and credible trend analyses.
2. **Sweep the relevant areas below**, weighted by the app's category and the adaptation brief.
3. **Assess maturity honestly.** Mark each finding as shipping-and-stable, shipping-but-immature, announced-not-shipped, or speculative. A v1 dependency on a speculative capability requires director/user approval.
4. **Filter through the personas and gap.** A trend matters only if it serves this app's users or strengthens positioning. "Everyone is adding X" is a reason to examine X, not adopt it.

## Areas to sweep

- **Interaction paradigms** — changes in how users express intent: voice/natural language, AI-assisted or generative UI, gesture/spatial input, ambient/proactive patterns, evolving navigation conventions.
- **Platform capabilities** — relevant new OS/browser APIs and surfaces: widgets, live activities, intents/shortcuts, on-device ML, offline/sync primitives, interoperability/share surfaces, sensors and form factors.
- **AI integration** — where models genuinely improve the category versus where they add cost or gimmickry; on-device vs cloud trade-offs for cost, privacy, latency, and reliability.
- **Visual & motion direction** — changing aesthetic conventions, design-system evolutions, motion/haptics as meaning rather than decoration.
- **Accessibility & inclusive technology** — new assistive capabilities and expectations; underserved users can represent a legitimate product edge.
- **Distribution & business mechanics** — store-policy changes, pricing norms, alternative distribution, and category monetization changes.
- **Frontend/build technology** — when relevant to web or cross-platform targets, assess framework/runtime direction and capability gaps that materially change what a small team can ship.

## Output format for `innovation.md`

```markdown
# Innovation & Technology Scan — [app name]
_Scanned [date]. Sources cited inline; revisit before Stage 3 if the scan has materially aged._

## Relevant currents
[Per relevant area: concise bullets of what's emerging, each with source and maturity rating. Omit irrelevant areas rather than padding.]

## Edge opportunities
### 1. [Name the opportunity]
- **What:** [pattern/capability and how this app would use it]
- **Why us:** [fit with personas/gap; why competitors have not absorbed it]
- **Maturity & risk:** [honest assessment]
- **Verdict:** adopt / watch (trigger: ...) / ignore (because ...)

## What we deliberately ignore
[Trends examined and rejected, one line each, so they are not re-litigated later.]
```
