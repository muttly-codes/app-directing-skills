---
name: app-design-testing
description: Stage 4 of app development — testing and evaluating the design before build. Use when an app project needs usability testing, persona-based walkthroughs, an accessibility/WCAG audit, heuristic evaluation, visual/design-system consistency review, or a prioritized pre-build fix list — or when app-director certifies Stage 3. Trigger for phrases like "test the prototype", "is this usable", "usability test", "accessibility check", "a11y audit", "review the design", "find UX problems", or "start the testing stage".
---

# App Design Testing & Evaluation (Stage 4)

Find the design's problems while they are still cheap. Evaluate through three lenses, in descending order of authority:

1. **Usability** — can representative humans complete the important tasks?
2. **Accessibility** — can people with disabilities perceive, understand, and operate the design?
3. **Design review** — is the interface internally consistent and faithful to its own system?

The real product is not three reports; it is one evidence-aware, prioritized fix list.

## Before anything else

Read:

1. `product/adaptations/design-testing.md` — overrides defaults and carries Stage 3 debts.
2. `product/ux/flows.md` — usability tasks come from certified flows.
3. `product/ui/prototype/`, or `product/ux/prototype/` if Stage 3 was deliberately skipped.
4. `product/research/personas.md` — defines representative users.
5. `product/ui/components.md`, `tokens.json`, `tokens.css`, and `responsive.md` where present.
6. `product/STATUS.md` — especially previously observed friction and carried debts.

Standalone use is allowed against any prototype/design the user supplies, but first establish the primary audience, primary tasks, target platform, and what artifact is actually available.

## Establish inspection capability

Determine what you can genuinely inspect.

### Live browser interaction

If browser automation is available and the prototype can be opened, use it where appropriate to walk tasks, exercise keyboard navigation, test zoom/reflow, inspect labels/focus behavior, and capture screenshots. Do not assume a particular browser-tool name; follow the active integration's instructions.

### Figma inspection

If relevant material lives in Figma and an integration is available, load and follow `figma-use` or equivalent guidance, then inspect screenshots, design context, variables, or components as supported.

### Static inspection only

If live browser/design-tool inspection is unavailable, work from prototype HTML, project artifacts, and user-provided evidence. State the limitation. Never imply you observed rendered or assistive-technology behavior you did not actually inspect.

## Optional delegation

If the runtime supports agent delegation, bounded tasks may be delegated, especially independent persona walkthroughs, consistency sweeps, or first-draft organization of already-gathered findings.

Follow any delegation preference in BRIEF.md. Do not assume a particular model family, tier, or agent API.

The active stage agent remains responsible for evidence validity, provenance, severity, consolidation, the must-fix recommendation, and the canonical contents of `product/testing/`.

## Lens 1 — Usability

Outputs:

- `product/testing/usability-plan.md`
- `product/testing/findings.md`

### Plan

Derive roughly 3–6 tasks from certified flows. Include first-run/onboarding, the core loop, each important persona task, and an important recovery/error path where relevant.

For each task define:

- goal-phrased scenario;
- observable success criterion;
- what to observe: wrong turns, hesitation, backtracking, confusion, abandonment, incorrect assumptions.

Do not reveal the intended steps in the task wording.

Write a short session script: introduction, think-aloud instruction, reminder that the design is being tested rather than the participant, tasks in order, neutral prompts, and wrap-up questions.

### Real-user sessions

Real-user evidence is strongest. Recommend it whenever practical. The user may conduct sessions and provide notes/recordings; convert those into structured findings without overstating what was observed.

### Persona walkthroughs

Persona walkthroughs are a fallback and useful pre-pass. Simulate the persona against the actual prototype.

If agent delegation is available, independent walkthroughs may be assigned by persona. Give each only the persona, task scenarios, and prototype artifacts — not intended flows or design rationale. Require the route taken, hesitation, ambiguity, failures, dead ends, misunderstood labels, missing states, and completion result.

### Evidence provenance

Every finding must state provenance, for example:

- `[observed: P3]`
- `[walkthrough: Casual Creator]`
- `[prototype inspection]`
- `[user-reported]`

Synthetic walkthrough findings are hypotheses, not equivalent to human observation.

Each finding should include title, what happened, task/persona/participant, evidence, provenance, affected screen/path, severity, and suggested fix where reasonably clear.

## Lens 2 — Accessibility (`product/testing/accessibility-audit.md`)

Read `references/wcag-audit.md` and audit against WCAG 2.2 AA at the fidelity the current prototype genuinely supports.

For each criterion record:

- PASS
- FAIL
- N-A — because ...
- DEFERRED TO BUILD — because ...

Use evidence wherever possible. Do not claim that a design-stage audit proves the shipped application accessible.

Where supported, perform keyboard navigation, focus-order reasoning, color-independence review, zoom/reflow inspection, semantic HTML inspection, target-size inspection, contrast verification, error-state review, and non-visual-use reasoning.

For Stage 3 tokens, run the sibling skill's checker using the actual installed path to `app-ui-design/scripts/contrast_check.py` against `product/ui/tokens.json`. Also inspect rendered combinations absent from `contrast_pairs`.

Every accessibility failure becomes a finding. Carry implementation-only checks such as real screen-reader traversal into STATUS.md as build-stage debt.

## Lens 3 — Design review (`product/testing/design-review.md`)

### Token fidelity

Look for hardcoded screen colors, unauthorized type sizes, off-scale spacing, components bypassing semantic tokens, and appearance-mode inconsistencies.

### Component fidelity

Look for elements that should use an established component but were hand-built differently, inconsistent anatomy, and missing states.

### Heuristic sweep

Review against the classic usability heuristics:

1. visibility of system status;
2. match to real-world language;
3. user control and freedom;
4. consistency and standards;
5. error prevention;
6. recognition rather than recall;
7. flexibility and efficiency;
8. minimalist/relevant presentation;
9. useful error recognition and recovery;
10. appropriate help/guidance.

Every violation should identify the affected screen, component, or flow. Do not manufacture issues just to fill every heuristic.

Where the project supports both light and dark modes, perform relevant checks in both.

## Consolidate findings

The final section of `product/testing/findings.md` must combine all three lenses into one prioritized list. Merge duplicate symptoms that share one underlying problem while preserving evidence from each lens.

### Severity

- **P0 Critical** — blocks a core task, excludes a user group from an essential capability, or creates an unacceptable accessibility barrier.
- **P1 Major** — serious errors/friction on a core task, major accessibility compromise, or unreliable important flow.
- **P2 Moderate** — meaningful secondary-task friction, recoverable accessibility/usability problems, or user-visible design inconsistency.
- **P3 Minor** — primarily cosmetic/low-impact; does not materially block understanding or task completion.

Within a level, rank using participant/persona impact, recurrence, likelihood, and downstream cost. Repeated synthetic findings do not automatically outweigh severe observed evidence.

End with:

- **Must fix before build**
- **May be fixed during build**
- **Accepted/deferred debt**

Fix actual defects in the canonical Stage 2/3 artifacts rather than merely describing fixes in the report.

## Closing the stage

1. Present the consolidated findings and recommendation.
2. Agree on the must-fix set.
3. Apply or coordinate corrections in `product/ux/` and `product/ui/`.
4. Re-test/re-inspect enough to verify the fixes.
5. Update findings with verification status.
6. Update STATUS.md: tick met gates, set Stage 4 to **awaiting review**, and record deferred debts/accepted risks.
7. Hand off to **app-director**.

Testing should be adversarial toward the design and fair toward the people using it. Zero meaningful findings are possible, but should prompt a check that the testing was deep and representative enough rather than a forced invention of defects.
