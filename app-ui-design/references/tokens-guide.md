# Design Tokens Guide

This file defines the token architecture used by **app-ui-design** and the schema expected by `scripts/contrast_check.py`.

## Structure: three tiers

### 1. Primitives

Raw ingredients: color ramps, modular type scale, spacing scale, radii, and elevation/shadow levels. Primitives have no opinion about where they are used.

### 2. Semantic tokens

Meaning-based aliases such as `text-primary`, `text-secondary`, `surface`, `surface-raised`, `accent`, `on-accent`, `border`, `danger`, `success`.

Screens and components reference semantic tokens **only**. This indirection makes appearance modes and later rebranding cheaper.

### 3. Modes

Modes provide different semantic mappings over the same primitives. Common modes are `light` and `dark`. Dark mode is not a simple inversion: raised surfaces may get lighter, accents may need a different primitive for contrast, and pure black/white may be unnecessarily harsh.

## `tokens.json` schema

`scripts/contrast_check.py` expects this structure:

```json
{
  "primitives": {
    "color": {
      "gray-50": "#fafafa",
      "gray-900": "#171717",
      "blue-500": "#2563eb"
    },
    "type": {
      "scale": { "xs": 12, "sm": 14, "base": 16, "lg": 20, "xl": 25, "2xl": 31 },
      "family": { "ui": "system-ui", "display": "system-ui" }
    },
    "space": [4, 8, 12, 16, 24, 32, 48],
    "radius": { "sm": 4, "md": 8, "full": 9999 }
  },
  "semantic": {
    "light": {
      "text-primary": "gray-900",
      "text-secondary": "gray-600",
      "surface": "gray-50",
      "surface-raised": "#ffffff",
      "accent": "blue-600",
      "on-accent": "#ffffff",
      "border": "gray-300",
      "border-input": "gray-500",
      "danger": "red-600",
      "on-danger": "#ffffff"
    },
    "dark": {
      "text-primary": "gray-100",
      "text-secondary": "gray-400",
      "surface": "gray-900",
      "surface-raised": "gray-800",
      "accent": "blue-400",
      "on-accent": "gray-950",
      "border": "gray-800",
      "border-input": "gray-500",
      "danger": "red-400",
      "on-danger": "gray-950"
    }
  },
  "contrast_pairs": [
    { "fg": "text-primary", "bg": "surface", "min": 4.5 },
    { "fg": "text-primary", "bg": "surface-raised", "min": 4.5 },
    { "fg": "text-secondary", "bg": "surface", "min": 4.5 },
    { "fg": "on-accent", "bg": "accent", "min": 4.5 },
    { "fg": "on-danger", "bg": "danger", "min": 4.5 },
    { "fg": "border-input", "bg": "surface", "min": 3.0 }
  ]
}
```

The example is structural; a real project must define every primitive referenced by its semantic mappings.

## Semantic values

Semantic colors may reference primitive names or raw hex values. Prefer primitives when the value is part of the reusable system; raw values are acceptable where another abstraction adds no value.

## Contrast pairs

`contrast_pairs` declares foreground/background combinations that the real interface renders and that require verification. The checker evaluates every declared pair in every semantic mode.

Typical minimum ratios:

- `4.5` — normal text;
- `3.0` — large text where WCAG permits it;
- `3.0` — non-text UI elements whose visibility is required to operate or understand the control.

Keep decorative and functional borders separate when they have different accessibility obligations. Rendering a pair you did not declare creates a blind spot; declaring unused pairs creates needless work.

## Running the checker

```bash
python3 scripts/contrast_check.py product/ui/tokens.json
```

The script checks every declared pair, evaluates every semantic mode, prints ratio vs minimum, exits `0` when all pass, `1` when checks fail, and `2` on file/schema errors.

## `tokens.css`

Generate from `tokens.json`. Expose semantic tokens as custom properties rather than forcing screens to know primitive names.

```css
:root {
  --text-primary: #171717;
  --surface: #fafafa;
  --space-1: 4px;
  --space-2: 8px;
  --text-base: 16px;
}

@media (prefers-color-scheme: dark) {
  :root {
    --text-primary: #f5f5f5;
    --surface: #171717;
  }
}
```

Where the prototype supports manual appearance switching, also provide `.light` and `.dark` overrides consistent with the same semantic mappings.

## Native targets

For native targets, `tokens.json` remains the design-system source of truth. Mirror it into the platform's idiom at build time, such as Swift asset-catalog colors/`Color` extensions or Compose theme objects. Record required mirrors in `components.md`.

## Choosing values — quick heuristics

- **Type:** a modest modular scale around 1.2–1.33 over a 16px base is often enough; 3–6 sizes suit many apps.
- **Color:** one useful accent hue generally does more work than several competing accents; build the neutral ramp first. Never encode important meaning through color alone.
- **Spacing:** use the defined scale consistently. Repeated off-scale values mean either design drift or a scale that genuinely needs revision.
- **Elevation:** two or three levels are enough for most apps; if everything is raised, elevation no longer communicates hierarchy.
