---
name: app-ui-design
description: Stage 3 of app development — user interface and visual design. Use when an app project needs a visual direction, color palette, typography, branding application, design tokens, a component library/design system, dark mode, responsive or adaptive layout rules, or a styled prototype — or when app-director certifies Stage 2. Trigger for phrases like "make it look good", "pick colors and fonts", "design system", "style the prototype", "apply my brand", or "start the UI stage". Not for screen structure or user flows — that's app-ux-design.
---

# App UI Design (Stage 3)

Give the grayscale skeleton a face — chosen deliberately from alternatives, encoded as data rather than scattered decisions, and verified for accessibility rather than eyeballed. The output is a compact design system applied to real screens, ready for Stage 4 and implementation.

## Before anything else

Read, in this order:

1. `product/adaptations/ui-design.md` — overrides defaults and carries Stage 2 debts.
2. `product/BRIEF.md` — especially Taste & references and any established brand rules.
3. `product/research/personas.md` and `product/research/innovation.md` — audience and relevant **adopt** visual/motion directions.
4. `product/ux/` — certified wireframes and prototype.

If the app must match an established brand, treat its palette, typography, and identity rules as constraints. Stage 2 owns structure: style the approved UX rather than silently redesigning it. If styling exposes a genuine structural problem, escalate it to **app-director**.

If an appropriate frontend-design or visual-design skill is available, consult it during Phase 1 for distinctive, non-generic direction. This stage's project contract remains authoritative.

## Optional delegation

If the runtime supports agent delegation, bounded first-draft or production work may be delegated.

- Follow any delegation preference in BRIEF.md.
- Do not assume a specific model family, model tier, or agent API.
- The active stage agent remains responsible for visual judgment, synthesis, accessibility verification, consistency, and the canonical contents of `product/ui/`.
- User-facing visual-direction selection remains interactive.

## Phase 1 — Visual direction (`product/ui/direction.md`)

Develop **2–3 genuinely distinct directions**, not minor variations of one idea.

For each provide:

- short name;
- rationale tied to personas, positioning, and brand;
- indicative palette;
- typography direction;
- density/spacing character;
- relevant motion/surface characteristics;
- one key certified wireframe screen styled in that direction, saved as e.g. `direction-a.html`.

Present the alternatives to the user. Record the selected direction, reasoning, rejected alternatives, and any deliberate blend in `direction.md`. Do not choose silently on the user's behalf.

## Phase 2 — Design tokens

Outputs:

- `product/ui/tokens.json`
- `product/ui/tokens.css`

Read `references/tokens-guide.md`.

Use its three-tier structure:

- **Primitives** — raw values such as color ramps, type scale, spacing, radii, elevation.
- **Semantic tokens** — meaning-based aliases such as `text-primary`, `surface`, `accent`, `danger`.
- **Modes** — light/dark or other project-required semantic mappings over the same primitives.

Components and screens consume semantic tokens rather than raw palette values.

### Contrast verification

Run:

```bash
python3 scripts/contrast_check.py product/ui/tokens.json
```

If validation fails, fix the relevant primitive or semantic mapping and re-run. Do not lower a valid threshold merely to pass the checker. Paste the passing output into `direction.md` as gate evidence.

The active stage agent is responsible for ensuring `contrast_pairs` covers the combinations the UI actually renders.

## Phase 3 — Components (`product/ui/components.md`)

Inventory only interface elements present in the certified wireframes: buttons, navigation, rows, cards, inputs, dialogs, menus, status elements, and so on.

For each component document:

- purpose;
- anatomy;
- semantic tokens consumed;
- size/density rules where relevant;
- accessibility considerations;
- states relevant to the platform, such as default, hover, focus, pressed, disabled, loading, error, selected.

Focus states are required wherever keyboard, switch, directional, or comparable focus navigation applies.

Where motion communicates state or causality, specify trigger, approximate timing, and reduced-motion alternative. Motion should communicate behavior rather than decorate it.

## Phase 4 — Responsive & adaptive rules (`product/ui/responsive.md`)

Define behavior required by the device/size contexts in `platform.md`.

Cover relevant rules such as:

- navigation transformations;
- single-to-multi-column changes;
- list-to-grid behavior;
- pinned vs scrolling regions;
- modal/sheet/dialog adaptation;
- minimum target sizes;
- type and spacing scaling;
- orientation where relevant;
- Dynamic Type or equivalent;
- 200% zoom for web;
- reduced-motion behavior.

Use native adaptive-layout concepts for native apps rather than forcing web breakpoint logic everywhere.

## Phase 5 — Styled prototype (`product/ui/prototype/`)

Copy the certified Stage 2 prototype and apply the approved visual system.

Requirements:

- link `tokens.css`;
- use semantic tokens for screen styling;
- no hardcoded palette hex values in individual screen files;
- preserve Stage 2 navigation and flow behavior;
- do not casually change layout structure;
- preserve the core loop.

At minimum, fully style core-loop screens, representative components, and required appearance modes. If long-tail screens remain wireframes, identify them explicitly.

## Figma (optional)

If a Figma integration is available and the user wants the design system there, complete filesystem artifacts first. Load and follow the available `figma-use` or equivalent integration guidance. Prefer variables/tokens before themes, then components/variants, then representative screens.

The canonical project artifacts remain under `product/ui/`. Do not make completion depend on Figma.

## Closing the stage

1. Walk the user through the styled prototype and relevant appearance modes.
2. Confirm the visual direction still works at scale.
3. Confirm relevant Stage 1 innovation **adopt** decisions are incorporated or explicitly rejected.
4. Confirm `scripts/contrast_check.py` passes against final `tokens.json`.
5. Re-check the adaptation brief and record deliberate deviations.
6. Update STATUS.md: tick met gates, set Stage 3 to **awaiting review**, log unresolved questions.
7. Hand off to **app-director** for gate review.

The active stage agent owns the canonical contents of `product/ui/` regardless of delegated or external-tool contributions.

The system is done when the certified wireframes' actual needs are covered, consistently applied, and required contrast checks pass — not when the component catalogue rivals a major framework.
