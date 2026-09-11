---
name: app-research-strategy
description: Stage 1 of app development — research and strategy. Use when an app project needs market research, competitor analysis, user personas, target-audience definition, goals and success metrics, platform selection, or a scan of emerging UI/UX and technology trends. Trigger for phrases like "research the market for my app", "who are my competitors", "define my users", "which platform should I build for", "start the research stage", or when app-director certifies a project for Stage 1.
---

# App Research & Strategy (Stage 1)

Turn an aligned idea into an evidence-backed strategy. The brief begins with hunches; this stage replaces those hunches with evidence — confirming, refining, or breaking them. A broken hunch is a useful outcome here because this is the cheapest point in the project to be wrong.

## Before anything else

Read, in this order:

1. `product/adaptations/research-strategy.md` — the director's adaptation brief. It overrides this skill's defaults.
2. `product/BRIEF.md` — the certified vision. Every conclusion should either serve it or explicitly challenge it.
3. `product/STATUS.md` — contains the project-specific gate checklist.

If these files do not exist, the project skipped app-director. Offer either to run standalone from a quick verbal brief or to set the project up properly through **app-director**.

## Optional delegation

If the runtime supports agent delegation, bounded evidence gathering or first-draft work may be delegated where it improves speed or parallelism.

- Follow any delegation preference recorded in `product/BRIEF.md`.
- Do not assume a specific model family, model tier, or delegation API.
- The active stage agent remains responsible for source quality, synthesis, judgment, interactive decisions, and the canonical files under `product/research/`.
- Do not delegate Wave 2's interactive synthesis with the user.

Delegated work must be reviewed critically before it becomes part of the stage output.

## Research evidence standard

Use live external research for current claims about competitors, pricing, platform availability, recent updates, policies, and technology trends.

Prefer, in order where practical:

1. primary sources and official platform documentation;
2. official app/store listings and product pages;
3. recent credible reviews, comparison sources, and release notes;
4. community/review evidence for user complaints and lived experience.

Distinguish source facts from your synthesis and cite sources inline in the research artifacts.

## The five tracks

Outputs go in `product/research/`.

### Wave 1 — evidence gathering

Run these independently; parallelize if the runtime supports parallel delegated research, otherwise run sequentially:

- Track A — Market & competitors → `market.md`
- Track B — Audience evidence → feeds `personas.md`
- Track E — Innovation & technology scan → `innovation.md`

Give delegated tracks only the relevant adaptation constraints and the BRIEF problem statement. Require sourced findings.

### Wave 2 — synthesis with the user

Do inline and do not delegate:

- Track C — Goals, features & success metrics → `goals-metrics.md`
- Track D — Platform selection → `platform.md`
- Finish `personas.md` using Track B evidence.

## Track A — Market & competitors (`product/research/market.md`)

Search the real market: app stores, product directories, review sites, forums/Reddit, comparison sources, and credible non-app alternatives.

For each meaningful competitor, respecting any adaptation cap and defaulting to roughly 4–7:

- what it is;
- platform(s);
- pricing;
- standout strengths;
- recurring complaints;
- recency of meaningful updates where relevant.

Mine low-star reviews and community complaints as usability evidence, but do not treat anecdotes as representative without qualification.

Include the strongest non-app alternative — spreadsheet, paper, manual service, or simply doing nothing — because it may be the real competitor.

End with a **gap statement**: 2–4 sentences naming what the landscape fails to do for a specific kind of user and why this app could own that gap.

If honest research finds no meaningful gap, say so and flag it for app-director.

## Track B — Audience and personas (`product/research/personas.md`)

Gather evidence of how real people experience the problem through competitor reviews, community discussions, search phrasing, and any real users or sources named in the adaptation brief.

Write 2–4 personas only if the evidence supports them.

Each persona should include:

- name;
- one-line identity;
- context of use;
- goals;
- frustrations with current solutions;
- a representative quote or paraphrased sentiment traceable to observed evidence;
- what would make them switch;
- which BRIEF assumptions they confirm or contradict.

Do not invent personas from stereotype. Every substantive claim should trace to observed evidence or be explicitly labeled as an inference.

## Track C — Goals, features & metrics (`product/research/goals-metrics.md`)

Work interactively with the user.

Translate BRIEF goals, persona needs, and the gap statement into:

- **must** — v1 fails without it;
- **should** — v1 is materially weaker without it;
- **later** — explicitly deferred.

Every must-have must trace to a persona need or the identified gap. Features that trace only to novelty belong in later unless the user deliberately chooses otherwise.

For each BRIEF goal, define a measurable success proxy, target, and measurement point. Prefer metrics that can actually be instrumented in Stage 5.

## Track D — Platform selection (`product/research/platform.md`)

If the adaptation brief fixes the platform, perform a sanity-check rather than reopening the decision by default.

Evaluate whether audience devices, required capabilities, distribution channel, maintenance burden, economics, and the user's skills support that choice. Escalate only if the evidence materially fights it.

If open, compare viable candidates such as native iOS/Android, cross-platform frameworks, web/PWA, and desktop against this project's actual needs.

Recommend one option, identify the runner-up, and state what trigger would justify revisiting the decision.

## Track E — Innovation & technology scan (`product/research/innovation.md`)

Read `references/innovation-scan.md`.

The aim is to avoid designing against conventions that are already stale and to identify a useful edge — interaction pattern, platform capability, accessibility advance, or technology direction that competitors have not fully absorbed.

For each relevant current, cite sources and assess maturity honestly.

Produce 2–3 **edge opportunities**, each marked:

- **adopt** — design for it in Stages 2–3;
- **watch** — record the trigger for reconsideration;
- **ignore** — record why it does not fit.

Write this file as a direct input to app-ux-design and app-ui-design.

## Closing the stage

1. Present a concise synthesis: gap statement, personas in one line each, must-list, platform call, and edge opportunities.
2. Discuss anything contentious, especially assumptions the evidence broke.
3. Update `product/STATUS.md`: tick gate items believed met, set Stage 1 to **awaiting review**, and log open questions.
4. Hand off to **app-director** for gate review.

Do not gold-plate. When every project-specific gate item is honestly met, stop. Research past the point of decision is often procrastination with citations.
