---
name: app-ux-design
description: Stage 2 of app development — user experience design. Use when an app project needs information architecture, a screen/navigation map, user flows, wireframes, or a clickable prototype. Trigger for phrases like "map out the app structure", "design the user flow", "wireframe the screens", "make a clickable prototype", "start the UX stage", or when app-director certifies Stage 1. Not for visual styling, colors, or fonts — that's app-ui-design.
---

# App UX Design (Stage 2)

Turn the certified strategy into the app's skeleton: where everything lives, how users move, and what each screen contains — deliberately without visual style. Structure should be judged on clarity before color and polish enter. Style is Stage 3's job.

## Before anything else

Read, in this order:

1. `product/adaptations/ux-design.md` — the director's adaptation brief; it overrides defaults and carries Stage 1 debts.
2. `product/BRIEF.md` — vision and non-goals.
3. `product/research/` — especially:
   - `personas.md` — whose tasks matter;
   - `goals-metrics.md` — must/should/later priorities;
   - `platform.md` — platform conventions and size targets;
   - `innovation.md` — every relevant **adopt** verdict must appear in the design or be explicitly rejected with a reason.

If `product/` does not exist, offer either to run standalone from a quick verbal brief or to set the project up through **app-director**.

## Optional delegation

If the runtime supports agent delegation, bounded first-draft or production work may be delegated where useful.

- Follow any delegation preference recorded in BRIEF.md.
- Do not assume a particular model family, model tier, or delegation mechanism.
- The active stage agent remains responsible for UX judgment, checkpoint decisions, review of delegated output, and the canonical files under `product/ux/`.
- Keep the user checkpoint and final stage-closing judgments with the active agent.

## Phase 1 — Information architecture (`product/ux/architecture.md`)

Inventory every must- and should-feature and decide where each lives.

Choose and name the navigation model — for example tab bar, sidebar/drawer, hierarchical drill-down, single-screen + modals, wizard — and justify it against:

- target-platform conventions;
- persona context of use;
- task frequency and importance;
- feature hierarchy.

Produce a screen map as a Mermaid diagram. Keep diagrams readable; split large maps by area rather than forcing everything into one graph.

Rules of thumb:

- the most frequent persona task should be reachable in the fewest reasonable interactions;
- if features compete for prime position, must-have beats should-have;
- a screen serving no persona task should not exist;
- deferred features should not quietly acquire screens.

## Phase 2 — User flows (`product/ux/flows.md`)

Trace step-by-step paths for:

- each persona's primary task;
- first-run/onboarding;
- the core loop;
- recovery from the most likely error or empty state.

For each flow provide:

1. a Mermaid flowchart;
2. numbered narrative;
3. step count;
4. **friction notes** identifying every point where the user must type, decide, wait, grant permission, change context, or recover from uncertainty.

### Checkpoint

Present the information architecture and flows to the user **before wireframing**. Capture material reactions, revise where needed, and only then proceed.

## Phase 3 — Wireframes (`product/ux/wireframes/`)

Read `references/wireframe-kit.md`.

Create one low-fidelity HTML file per screen appearing in the approved flows, including relevant empty and error states.

Rules:

- grayscale only;
- no brand colors;
- system-default fonts only;
- no decorative imagery; use labeled placeholders where structure requires media;
- real labels/headings/key data in critical locations;
- size for the chosen platform using `platform.md`;
- annotate non-obvious behavior beneath each frame;
- keep treatment intentionally plain so review remains about structure, hierarchy, content, and interaction.

## Phase 4 — Clickable prototype (`product/ux/prototype/`)

Copy the approved wireframes into `product/ux/prototype/` and connect them using plain HTML links.

Use zero JavaScript for the baseline prototype. If an interaction cannot reasonably be represented by links, describe it in an annotation rather than faking functionality.

Two hard rules:

1. **No dead ends.** Every screen has at least one valid outgoing route.
2. **The core loop is fully walkable.** A person opening `index.html` should be able to complete the primary task without narration.

Include `index.html` as the entry point and identify the primary walkthrough.

Have the user click through it. Record hesitation, wrong expectations, confusion, or dead ends as evidence for Stage 4 rather than explaining them away.

## Figma (optional)

If a Figma integration is available and the user wants the UX work represented there, complete the filesystem artifacts first.

Before Figma actions, load and follow the available `figma-use` skill or equivalent integration guidance. Keep Figma output deliberately low-fidelity. The files under `product/ux/` remain the source of truth. Never make completion of this stage depend on Figma being connected.

## Closing the stage

1. Walk the user through the prototype and screen map.
2. Confirm relevant innovation-scan **adopt** items are represented or explicitly rejected in `architecture.md`.
3. Re-check the adaptation brief and document deliberate deviations.
4. Update `product/STATUS.md`: tick met gate items, set Stage 2 to **awaiting review**, and log unresolved questions or prototype friction.
5. Hand off to **app-director** for gate review.

The active stage agent owns the canonical contents of `product/ux/`, regardless of whether delegated agents or external tools contributed drafts.

Resist making it pretty — visual polish belongs to Stage 3.
