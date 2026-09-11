# Default Stage Gates

These are starting points. At init, edit them for the project: delete items that do not apply, add project-specific ones, and keep small projects' gates small. A gate item must be checkable by reading an artifact — if you cannot point at where it would be satisfied, rewrite it.

## Stage 1 — Research & Strategy (app-research-strategy)

Artifacts: `product/research/market.md`, `personas.md`, `goals-metrics.md`, `platform.md`, `innovation.md`

- [ ] Competitor landscape covers the credible alternatives (including "do nothing"/non-app solutions), each with strengths, weaknesses, pricing.
- [ ] A specific gap/positioning statement exists: what this app does that the landscape does not, and for whom.
- [ ] 2–4 personas grounded in evidence gathered (not just the interview hunches restated), each with goals, frustrations, and context of use.
- [ ] Core feature set chosen and prioritized (must/should/later), traceable to personas and the gap.
- [ ] Success metrics defined and measurable, consistent with BRIEF.md.
- [ ] Platform decision made with rationale (or the pre-fixed decision sanity-checked against the evidence).
- [ ] Innovation scan completed: emerging UI/UX and technology directions relevant to this category, with 2–3 concrete edge opportunities, each marked adopt / watch / ignore with reasoning.

## Stage 2 — UX Design (app-ux-design)

Artifacts: `product/ux/architecture.md`, `flows.md`, `wireframes/`, `prototype/`

- [ ] Information architecture maps every must-have feature to a location; navigation model named and justified.
- [ ] User flows exist for each persona's primary task and the critical paths (first-run/onboarding, core loop, recovery from the most likely error), with step counts and friction notes.
- [ ] Wireframes cover every screen appearing in the flows — low-fidelity, content-real.
- [ ] Clickable prototype connects the core-loop screens; a stranger could complete the primary task without narration.
- [ ] At least one innovation-scan opportunity is reflected, or its rejection is recorded.

## Stage 3 — UI Design (app-ui-design)

Artifacts: `product/ui/direction.md`, `tokens.json`, `tokens.css`, `components.md`, `responsive.md`, plus styled prototype.

- [ ] A visual direction was chosen from genuinely explored alternatives, with rationale tied to brand/audience.
- [ ] Design tokens exist as data, not only prose.
- [ ] Every required text/background and functional non-text pair in the token system passes the declared WCAG contrast threshold.
- [ ] Component inventory covers the elements the wireframes actually use, with relevant states.
- [ ] Responsive/adaptive rules are defined for the size classes the platform implies.
- [ ] Styled prototype or representative styled key screens demonstrate the system on real screens.

## Stage 4 — Testing & Evaluation (app-design-testing)

Artifacts: `product/testing/usability-plan.md`, `findings.md`, `accessibility-audit.md`, `design-review.md`

- [ ] Usability test plan has concrete tasks derived from Stage 2 flows, a script, and success criteria per task.
- [ ] Usability findings exist — real-user evidence where practical, otherwise clearly labeled persona-based walkthrough hypotheses — each with severity and provenance.
- [ ] Accessibility audit against WCAG 2.2 AA is completed at the fidelity the prototype supports, with pass/fail/N-A/deferred status and fixes/debts filed.
- [ ] Design review checked consistency against tokens/components and flagged deviations.
- [ ] Findings are consolidated into one prioritized fix list with a recommendation of what must be fixed before build vs. can wait.

## Stage 5 — Post-Launch & Iteration (app-post-launch)

Artifacts: `product/post-launch/analytics-plan.md`, `feedback-log.md`, `update-roadmap.md`

- [ ] Analytics plan defines events, funnels, and drop-off points that measure the BRIEF's success metrics, small enough to actually instrument.
- [ ] Feedback intake is defined: sources, triage rubric, provenance, and a log format.
- [ ] Update roadmap exists with a focused next cycle, each item traceable to data, feedback, debt, prior strategy, or an explicitly labeled bet.
- [ ] The loop closes: the roadmap points back to app-director for the next cycle's mini-brief and stage re-entry.

## Cross-cutting (apply at every gate)

- [ ] Output still serves BRIEF.md — no silent scope drift.
- [ ] The stage's adaptation brief was honored, or deviations were justified in the artifact.
- [ ] Open questions and carried-over debts are written down in STATUS.md, not lost in conversation.
