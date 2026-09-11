# WCAG 2.2 AA Audit Guide

Use this during **app-design-testing** to audit at prototype fidelity.

For each applicable criterion record one of:

- PASS
- FAIL
- N-A — because ...
- DEFERRED TO BUILD — because ...

Provide evidence for failures and for passes that depend on an inspected artifact or interaction. Criteria requiring real application behavior or assistive-technology interaction belong in the build-stage debt section rather than receiving speculative passes.

## Evidence expectations

Automated tooling is useful but incomplete. Also use keyboard inspection, focus reasoning, semantic inspection, color-independence review, zoom/reflow testing, and consideration of non-visual use. Never report behavior as observed unless it was actually exercised.

# Perceivable

## 1.1.1 — Non-text Content
Meaningful images/icons have an accessible text alternative planned; decorative content is explicitly decorative.

## 1.3.1 — Info and Relationships
Visual relationships are also represented structurally. For HTML prototypes inspect heading hierarchy, lists, groups, form labels, tables, and control relationships.

## 1.3.4 — Orientation
Nothing requires one orientation unless essential to function. If the prototype cannot demonstrate behavior, record implementation verification rather than assuming pass.

## 1.3.5 — Identify Input Purpose
Forms collecting common user information should plan appropriate input purpose/autocomplete semantics.

## 1.4.1 — Use of Color
For every place color conveys status, selection, error, progress, category, or required action, confirm another cue exists such as text, icon, shape, label, weight, or position.

## 1.4.3 / 1.4.11 — Contrast
Where Stage 3 generated design tokens, resolve the installed sibling skill and run:

```bash
python3 <app-ui-design-skill-path>/scripts/contrast_check.py product/ui/tokens.json
```

Do not assume the script lives under `product/`. Also inspect rendered foreground/background combinations absent from `contrast_pairs`.

## 1.4.4 — Resize Text
Where live browser inspection is available, test at 200% zoom. Look for lost content/function, overlap, clipped labels, hidden navigation, or unusable dialogs.

## 1.4.10 — Reflow
For responsive/web prototypes, inspect approximately a 320 CSS-pixel viewport where applicable. Vertical-content screens should not require horizontal scrolling merely to read or operate content.

## 1.4.12 — Text Spacing
Check that increased line/paragraph/letter/word spacing does not cause content loss or overlap. Fixed-height text containers are a warning sign.

# Operable

## 2.1.1 / 2.1.2 — Keyboard Accessible / No Keyboard Trap
Where a browser prototype is usable, conduct a keyboard-only pass. Check focusability, activation, ability to move away, and absence of traps. For native targets, carry real keyboard/switch behavior into implementation testing where needed.

## 2.4.3 — Focus Order
Focus order should follow intended reading/interaction sequence. Inspect actual tab order where available.

## 2.4.4 — Link Purpose
Links/buttons should make sense from label and context. Prefer `View clip` to `Click here`.

## 2.4.6 — Headings and Labels
Headings describe sections; input labels explain expected input without depending solely on visual proximity.

## 2.4.7 / 2.4.11 — Focus Visible / Not Obscured
A visible focus treatment exists wherever focus navigation applies, and sticky/overlay UI does not obscure the focused element.

## 2.5.1 / 2.5.2 — Pointer Gestures / Cancellation
Complex gestures have simpler equivalents unless essential; actions should generally commit on release so accidental activation can be cancelled.

## 2.5.5 / 2.5.8 — Target Size
Check the smallest controls against applicable platform guidance and WCAG 2.2 minimum target-size requirements. Do not treat platform recommendations and WCAG as identical standards.

## 2.5.7 — Dragging Movements
Anything requiring dragging has a non-drag alternative unless dragging is essential.

# Understandable

## 3.1.1 — Language of Page
HTML prototypes define the primary language with `lang`; native designs document intended language semantics.

## 3.2.1 / 3.2.2 — On Focus / On Input
Focus or changing a value should not unexpectedly navigate, submit, or radically change context.

## 3.2.3 / 3.2.4 — Consistent Navigation / Identification
Recurring navigation and repeated functions remain consistent in order, iconography, labels, and behavior. Cross-reference overlapping design-review findings rather than duplicate them.

## 3.3.1 / 3.3.3 — Error Identification / Suggestion
Errors say what is wrong, where, and how to correct it where known. Do not rely on color alone.

## 3.3.2 — Labels or Instructions
Inputs have persistent labels or adequate instructions; placeholder text is not the sole label.

## 3.3.7 — Redundant Entry
Flows do not unnecessarily ask for the same information again during the same process.

## 3.3.8 — Accessible Authentication
Authentication does not unnecessarily require memorization, transcription, or cognitive puzzles where password managers, copy/paste, platform authentication, or autofill can avoid them.

# Robust

## 4.1.2 — Name, Role, Value
HTML prototypes prefer native interactive elements. Custom widgets documented in `components.md` specify intended role, accessible name, and relevant state/value semantics.

## 4.1.3 — Status Messages
Toasts, confirmations, loading completion, validation updates, and other meaningful status changes are documented for programmatic announcement during implementation. Prototype design alone cannot prove this behavior.

# Build-stage accessibility debts

Carry relevant items into STATUS.md rather than pretending Stage 4 proved them:

- real VoiceOver/TalkBack/screen-reader traversal;
- native accessible names, roles, values;
- dynamic focus management and restoration;
- status announcements/live regions;
- real reduced-motion behavior;
- timing adjustability where applicable;
- real-device target-size verification;
- dynamic text behavior in production layouts;
- switch-control or alternative-input behavior where relevant.

A successful design-stage audit means accessibility risks were addressed at the fidelity available. It does not certify the shipped product.

# Severity mapping

- **P0 Critical** — no operable path for a user group through a core task, essential control lacks usable identity, or critical information is available only through an inaccessible channel.
- **P1 Major** — serious contrast/focus/keyboard/error-recovery barrier on an important path.
- **P2 Moderate** — meaningful but recoverable barriers on secondary paths.
- **P3 Minor** — low-impact issues that improve quality without materially blocking understanding or operation.

Severity is based on impact and context, not merely the WCAG criterion number.
