---
name: app-post-launch
description: Stage 5 of app development — post-launch measurement and iteration. Use when a launched or launching app needs an analytics/instrumentation plan, event tracking design, funnel and drop-off analysis, user-feedback or review triage, or an evidence-backed update roadmap for the next cycle — or when app-director certifies Stage 4 and launch approaches. Trigger for phrases like "what should I track", "set up analytics events", "users are complaining about X", "triage my reviews", "plan the next update", "what do I build next", or "start post-launch".
---

# App Post-Launch & Iteration (Stage 5)

Launch is where assumptions begin meeting reality. Earlier stages produced hypotheses about the gap, personas, feature priorities, flows, platform, success metrics, and design. This stage builds the machinery that tests those hypotheses against actual behavior and feedback, then turns the evidence into the next product cycle.

It operates in two modes:

1. **Pre-launch setup** — ideally before release so instrumentation and feedback intake exist from the first cohort.
2. **Recurring post-launch triage** — revisited whenever meaningful analytics, reviews, support feedback, or market changes accumulate.

## Before anything else

Read:

1. `product/adaptations/post-launch.md` — the director's adaptation brief and carried debts.
2. `product/BRIEF.md` and `product/research/goals-metrics.md` — Stage 1 success metrics are the spine of the analytics plan; instrument them rather than casually replacing them.
3. `product/ux/flows.md` — funnels are certified flows with measurement attached.
4. `product/research/market.md` — especially category pain points and competitor complaints.
5. `product/STATUS.md` — carried debts, accepted risks, and unresolved questions.
6. Existing post-launch artifacts/data if any: analytics exports, dashboards, reviews, support messages, crash reports, roadmaps.

If the app is already launched but has no `product/` structure, establish at minimum what success means, the primary user, the core task, what data exists, and what feedback channels exist. If iteration will continue, recommend a lightweight retroactive brief through **app-director**.

## Optional delegation

If the runtime supports agent delegation, bounded work may be delegated for large-volume review clustering, event normalization, first-pass theme extraction, or drafting tables from already-validated findings.

Follow any delegation preference in BRIEF.md. Do not assume a particular model family, tier, agent API, or connector.

The active stage agent remains responsible for evidence quality, provenance, prioritization, interpreting contradictions, evaluating kill criteria, distinguishing evidence from bets, choosing the next re-entry stage, and owning `product/post-launch/`.

## Part 1 — Analytics plan (`product/post-launch/analytics-plan.md`)

Keep the plan tool-agnostic so it survives a switch between analytics providers.

### Metric → instrumentation map

For every Stage 1 success metric define:

- the behavior representing the metric;
- events/measurements that calculate it;
- where the result will be read;
- measurement period/cohort where relevant;
- known limitations.

Do not collect data merely because the analytics platform makes it easy.

### Event taxonomy

Prefer stable, descriptive, implementation-independent event names using past tense, snake_case, and verb + object where appropriate, e.g.:

- `signed_up`
- `created_reel`
- `imported_clip`
- `completed_export`

One conceptual action should have one canonical name. Renames after launch are migrations.

Keep the catalogue small enough to implement and maintain. For each event document event name, purpose, precise firing condition, properties/types, relevant funnel/metric, and status (planned/implemented/verified/deprecated).

### Funnels

Translate important Stage 2 flows into ordered event sequences, especially onboarding, the core loop, and any conversion flow tied directly to success metrics.

For each step state the product question the funnel answers. Funnels should answer decisions, not merely visualize events.

### Privacy and data minimization

Collect the minimum needed to answer agreed product questions.

Default toward:

- no unnecessary PII;
- no sensitive content in event properties;
- coarse data where precision adds little value;
- short, justified retention where practical.

Document consent/platform requirements, retention expectations, and intentionally excluded data. Verify current legal/platform policy when certainty matters rather than relying on memory.

### Instrumentation anti-patterns

Check for undocumented events, duplicate conceptual events, ambiguous firing semantics, critical metrics dependent on unreliable client-only firing, unused properties retained indefinitely, names tied too closely to temporary UI wording, and analytics with no decision attached.

## Part 2 — Feedback intake and triage (`product/post-launch/feedback-log.md`)

Identify the feedback channels that genuinely exist: store reviews, support email, in-app feedback, support systems, community forums, social channels, beta groups, direct interviews, and so on. Record an appropriate checking cadence for each.

### Connected data sources

If an authorized connector/integration is available for a relevant source, it may be used to gather real evidence. Before accessing customer or teammate communications, identify the source and intended search and obtain any authorization required by the integration. Do not access private communication sources merely because a connector exists.

### Feedback log

Maintain an append-oriented structured log with fields such as:

- date;
- source/source reference;
- verbatim quote or faithful summary;
- theme;
- severity;
- frequency;
- persona/audience relevance;
- status;
- notes.

When substantially identical feedback recurs, increase the theme's frequency and preserve source references rather than creating duplicates solely to inflate volume.

### Severity

- **P0** — crash, data loss, security/privacy incident, core task impossible for a meaningful user group, catastrophic purchase/account failure.
- **P1** — serious failure on a core task, major accessibility barrier, severe reliability/performance problem.
- **P2** — meaningful but recoverable friction, secondary feature failure, repeated confusion.
- **P3** — wish, minor polish issue, low-impact preference, edge-case annoyance.

Do not equate emotional wording with high severity.

### Triage

Prioritize themes using severity, frequency, affected persona/task, strategic importance, behavioral evidence, and confidence. Target-persona relevance matters but does not override security, privacy, data-loss, accessibility, platform-policy, or comparable obligations.

### Feedback versus analytics

Feedback describes what users noticed, felt, expected, or reported. Analytics describes behavior at scale within what was instrumented. Neither automatically explains causation.

Contradictions should trigger investigation rather than automatic dismissal of either source.

When raw reviews/support feedback arrive, preserve provenance, cluster themes, distinguish symptoms from proposed solutions, extract concise representative evidence, update counts, and note affected tasks/personas where identifiable.

## Part 3 — Update roadmap (`product/post-launch/update-roadmap.md`)

Use the highest-priority feedback themes, meaningful funnel drop-offs, Stage 1's deferred later list, STATUS.md debts, innovation **watch** items, reliability/accessibility issues, and deliberate strategic opportunities.

### Shape the cycle

Prefer a focused named cycle, generally with a small number of coherent items rather than a backlog dump.

Each item must trace to at least one of:

- measured behavior;
- feedback evidence;
- known debt;
- previously deferred strategy;
- an explicit product bet.

### Product bets

A deliberate bet is allowed. Label it as a **bet** and define the hypothesis, why it is worth testing, expected cost, what supports it, and what would cause abandonment. Do not disguise intuition as data.

### Traceability

For each roadmap item record the item, evidence/rationale, expected outcome, success signal, stage to revisit, and priority.

Challenge untraceable additions. "While we're doing this, we may as well..." is often scope creep.

### Explicit non-actions

Maintain a short list of meaningful requests deliberately declined, with reason and reconsideration trigger where relevant. This prevents recurring re-litigation.

### Kill-criteria check

Return to BRIEF.md's failure criteria. State whether evidence suggests the app is comfortably above the threshold, uncertain/too early, trending toward it, or at/beyond it. Include uncertainty and do not manufacture either optimism or premature failure from noisy early data.

## Closing the loop

### First Stage 5 completion

1. Confirm the analytics plan traces to Stage 1 metrics.
2. Confirm feedback intake/triage are defined.
3. Confirm an initial roadmap structure exists even if live data is not yet available.
4. Update STATUS.md: tick met Stage 5 gates, set Stage 5 to **awaiting review**, and record launch/instrumentation debts.
5. Hand off to **app-director** for gate review.

### Recurring visits

When new analytics or feedback arrives, append/update evidence, re-read relevant funnels, re-rank themes, revise roadmap priorities where warranted, check innovation-watch triggers and kill criteria, and record material decisions. Do not rewrite historical evidence to make the current roadmap look inevitable.

### Re-entering the cycle

Identify which earlier stage owns each substantial change:

- minor visual polish → Stage 3 `app-ui-design`
- interaction-flow problem → Stage 2 `app-ux-design`
- new audience/positioning → Stage 1 `app-research-strategy`
- accessibility/usability validation after redesign → Stage 4 `app-design-testing`

Return the next cycle to **app-director** for a mini-brief and revised gates.

Iteration is the same product-development loop again — smaller, faster, and better informed. If reality has materially diverged from the certified BRIEF.md, escalate to app-director for alignment review rather than optimizing against a brief nobody believes anymore.
