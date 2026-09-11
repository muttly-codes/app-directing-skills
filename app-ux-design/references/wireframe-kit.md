# Wireframe Kit

Conventions for low-fidelity HTML wireframes used by **app-ux-design**.

The discipline matters more than aesthetics: grayscale keeps reviews about structure; real labels keep reviews about content; links keep the prototype honest.

## Palette — the whole palette

`#000` text · `#333` primary actions · `#666` secondary text · `#999` borders/dividers · `#ccc` disabled/inactive · `#eee` fills/surfaces · `#fff` background.

Dashed `#999` borders mark placeholder imagery/media. **No other colors.** If emphasis is needed, use weight, size, hierarchy, spacing, or a filled `#333` block.

## Base stylesheet

Put this in `wireframes/wire.css` and link it from every screen. Reuse it unchanged in `prototype/` unless a project-specific adaptation explicitly requires a structural adjustment.

```css
* { box-sizing: border-box; margin: 0; font-family: -apple-system, system-ui, sans-serif; color: #000; }
body { background: #ddd; display: flex; flex-direction: column; align-items: center; gap: 24px; padding: 24px; }
.frame { width: 375px; min-height: 700px; background: #fff; border: 2px solid #333;
         display: flex; flex-direction: column; }
.frame > header, .frame > footer { padding: 12px 16px; border-bottom: 1px solid #999; font-weight: 700; }
.frame > footer { border-bottom: 0; border-top: 1px solid #999; margin-top: auto; }
main { flex: 1; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.btn { display: block; padding: 12px; text-align: center; border: 1px solid #333;
       text-decoration: none; font-weight: 600; }
.btn.primary { background: #333; color: #fff; }
.btn[aria-disabled="true"] { border-color: #ccc; color: #ccc; }
.placeholder { border: 2px dashed #999; background: #eee; color: #666;
               display: flex; align-items: center; justify-content: center; min-height: 120px; }
.list-item { padding: 12px; border: 1px solid #999; display: flex; justify-content: space-between; }
.tabbar { display: flex; border-top: 1px solid #999; }
.tabbar a { flex: 1; padding: 12px 0; text-align: center; text-decoration: none; color: #666; }
.tabbar a.active { color: #000; font-weight: 700; border-top: 2px solid #000; }
.note { width: 375px; font-size: 13px; color: #444; background: #f5f5f5;
        border-left: 3px solid #999; padding: 8px 12px; }
input, textarea, select { padding: 12px; border: 1px solid #999; font-size: 16px; width: 100%; }
```

Adjust `.frame` width for non-phone targets according to `platform.md`. Typical wireframe starting references are approximately 375px phone, 768px tablet, 1200px desktop/web. These are not exact device requirements; follow project-specific platform decisions.

## File conventions

- One screen per file.
- Use kebab-case filenames named for the screen, not the feature: `clip-list.html`, `clip-list-empty.html`, `settings.html`.
- Put the screen title in an HTML comment and as a visible label above the frame.
- Variant states are separate files suffixed `-empty`, `-error`, `-loading`, only where they appear in an approved flow or materially affect the UX.
- Put one or more `.note` blocks directly beneath the frame for non-obvious behavior.

Annotations explain behavior the static wireframe cannot show. They are not a substitute for missing screens or unclear structure.

## Prototype linking rules

- Every interactive element that navigates is an `<a>` or contains one.
- Use zero JavaScript for the baseline prototype.
- If an interaction cannot be represented using a link, document it in a `.note` instead of pretending to implement it.
- **No dead ends:** every screen has at least one outgoing route; back navigation counts.
- `index.html` is the prototype entry point and should identify the primary walkthrough.
- Use relative links so the prototype works directly from disk without a local server.

## What this kit deliberately does not provide

This kit does not define brand colors, final typography, animation styling, shadows, final icons, illustration, photography, or polished component styling. Those belong to **app-ui-design**.
