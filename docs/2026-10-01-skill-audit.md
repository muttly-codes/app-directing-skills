# Skill audit: 2026-10-01

This note records an audit of the six skills in this suite, and the two corrections it led to. A combined note covering the ReelWrangler repo is at `muttly-codes/ReelWrangler`, in `docs/notes/2026-10-01-instruction-file-audit.md`.

## What changed

1. **`app-ui-design/SKILL.md`: the contrast-check command.**
   - **Before:** `python3 scripts/contrast_check.py product/ui/tokens.json`. This could not work from any single folder. `scripts/` is relative to the skill's folder, while `product/ui/tokens.json` is relative to the project root.
   - **After:** run from the project root, using the skill's actual installed path: `python3 <path-to-app-ui-design>/scripts/contrast_check.py product/ui/tokens.json`. This matches what `app-design-testing/SKILL.md` already said.
2. **`app-post-launch/SKILL.md`: the example event names.**
   - **Before:** `created_reel`, `imported_clip`, `completed_export`, which came from the ReelWrangler project.
   - **Why it mattered:** the suite is meant for any kind of app, and agents tend to copy examples closely, so these steered unrelated projects toward video-app event names.
   - **After:** neutral examples from different kinds of app (`signed_up`, `created_project`, `sent_invite`, `completed_checkout`), labelled as illustrative. The naming convention itself is unchanged: past tense, snake_case, verb + object.

## Checked and left alone

- **The repeated "Optional delegation" sections.** All six skills carry one. The copies agree and set a deliberate rule that the skills work with any AI provider.
- **The trigger phrases in each skill's `description`.** They decide when a skill gets used.
- **The hard integrity rules.** Examples: "never imply you observed behavior you didn't inspect", "no dead ends", "don't lower a valid threshold to pass the checker". Each states a real constraint.
- **The provider-neutral, Codex-compatible stance described in `README.md`.**

The writing style was already in good shape. There was no shouting, no step-by-step reasoning prompts and no formatting bans.

## Follow-up

Some environments have older installed copies of these skills; Claude's `anthropic-skills:app-*` copies are one example. Their descriptions differ from the ones in this repo. Reinstall from this repo if it is the canonical version.
