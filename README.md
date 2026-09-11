# App Directing Skills

A Codex-compatible App Studio skill suite for directing non-game app development from product conception through post-launch iteration.

## Skills

- `app-director` — project alignment, stage gates, triage, replanning, and refresh
- `app-research-strategy` — market research, personas, metrics, platform selection, and innovation scan
- `app-ux-design` — information architecture, flows, wireframes, and clickable prototype
- `app-ui-design` — visual direction, design tokens, components, responsive rules, and styled prototype
- `app-design-testing` — usability, accessibility, and design-system evaluation
- `app-post-launch` — analytics, feedback triage, and evidence-backed iteration roadmap

The suite uses a shared `product/` directory inside the target app project. `app-director` owns the project brief, stage status, gate reviews, and per-stage adaptation briefs; each specialist skill owns its stage artifacts.

These versions are adapted for Codex/OpenAI-style agent runtimes while keeping workflow semantics provider-neutral wherever possible.

## Codex integration note

The suite currently relies on each skill's `SKILL.md` metadata and does **not** include optional `agents/openai.yaml` files.

That omission is deliberate. `agents/openai.yaml` is Codex/OpenAI-specific UI and invocation metadata rather than part of the core workflow itself, so the portable skill definitions were kept provider-neutral during the initial migration.

If the suite is installed into Codex and current OpenAI tooling indicates that `agents/openai.yaml` would improve discovery, display names, default prompts, or other Codex-specific behaviour, those files can be added later under each skill, for example:

```text
app-director/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── ...
```

Before adding them, validate the **current** OpenAI metadata schema rather than relying on an older remembered format. The `SKILL.md` files remain the canonical workflow definitions regardless of whether Codex-specific metadata is added.
