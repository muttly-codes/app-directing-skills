# Templates

Fill these with real content; delete sections that genuinely do not apply rather than leaving placeholders. Keep BRIEF.md under roughly two pages — it is the document everyone re-reads, so brevity is a feature.

## `product/BRIEF.md`

```markdown
# [App name / working title] — Project Brief

## Vision
[One paragraph: what this is, for whom, and why it should exist.]

## Problem & audience hunch
[The problem being solved; who has it; how they cope today. Marked as hunch until Stage 1 verifies.]

## The one thing
[The single capability this app must do brilliantly.]

## Goals & success metrics
- [Goal] — measured by [metric + target + when]

## Non-goals (v1)
- [Explicitly out of scope, even if requested]

## Platform & technical constraints
[Fixed decisions vs. open questions, and why. Stack preferences, device capabilities needed.]

## Business model
[Paid/freemium/subscription/free/portfolio/personal — and pricing instinct if commercial.]

## Resources & time-frame
[Who, hours/week, external deadlines, budget for paid assets/services/testing.]
[Delegation preference, only if the user explicitly stated one — e.g. "delegate bounded drafting/research where appropriate" or "keep all work in the primary agent". Leave unstated otherwise.]

## Taste & references
[Admired apps, hated patterns, fixed opinions (name, tone, colors, must-not-exist features).]

## Tensions resolved
[Conflicts surfaced in the interview and which side won, e.g. "simplicity beats power-user parity".]

## Sign-off
- [date] — Brief approved by [user]. Alignment certified.

## Changelog
- [date] — [amendment + reason]
```

## `product/STATUS.md`

```markdown
# Project Status

**Project:** [name] · **Brief certified:** [date]
**Current stage:** [n — name] · **Last gate review:** [date or —]

## Time-frame (estimates, not deadlines)
| Stage | Estimate | Assumes |
|---|---|---|
| 1 Research & Strategy | [e.g. 1–2 wks] | [e.g. ~10 hrs/wk] |
| ... | | |

## Stage tracker
| # | Stage | Skill | State | Certified |
|---|---|---|---|---|
| 1 | Research & Strategy | app-research-strategy | not started / in progress / awaiting review / certified / returned | [date] |
| 2 | UX Design | app-ux-design | ... | |
| 3 | UI Design | app-ui-design | ... | |
| 4 | Testing & Evaluation | app-design-testing | ... | |
| 5 | Post-Launch & Iteration | app-post-launch | ... | |

## Gate checklists
### Stage 1 — Research & Strategy
- [ ] [gate items — see stage-gates.md, edited for this project]
### Stage 2 — UX Design
- [ ] ...
[...all five stages...]

## Open questions & carried-over debts
- [item — which stage owns it]

## Decisions & overrides log
- [date] — [decision / user override + one-line reason]
```

## `product/adaptations/<stage>.md`

```markdown
# Adaptation brief — [stage name]
_Written by app-director on [date]. This overrides the stage skill's defaults._

## Project context in three lines
[What the app is, who it is for, where the project stands — enough that the stage skill needs no other summary.]

## Do
[Project-specific instructions: what to emphasize, known inputs to start from, decisions already made that must be respected, effort ceilings, format preferences.]

## Don't
[Defaults of the stage skill to skip or reduce for this project, and why.]

## Carried-over debts
[Conditions from the previous gate review this stage must absorb.]

## Gate reminder
[The 2–3 gate items most at risk for this project, so the skill optimizes for them from the start.]
```

## STATUS.md — triage log entry

```markdown
### Triage — [date]
**Trigger:** [what prompted this]
**Diagnosis:** [where the stall actually originated]
**Agreed with user:** [yes — brief note on any disagreement resolved]
**Resume point:** [which stage skill picks up, and what stays as-is]
```

## STATUS.md — refresh log entry

```markdown
### Refresh — [date]
**Trigger:** [platform/OS change, dated design, competitive shift, periodic check, etc.]
**Areas checked:** [which stages/artifacts were reviewed against current reality]
**Findings:** [still holds / needs a light touch / needs to reopen — per area, briefly]
**Action taken:** [light-touch fixes made directly, or which stage(s) reopened and handed off]
```
