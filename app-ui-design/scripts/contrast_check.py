#!/usr/bin/env python3
"""WCAG contrast checker for App Studio tokens.json.

Usage:
    python3 scripts/contrast_check.py path/to/tokens.json

Checks every entry in "contrast_pairs" against every mode in "semantic".

Exit codes:
    0 — all declared pairs pass in all modes
    1 — one or more contrast checks fail
    2 — usage, file, or schema error

No dependencies beyond the Python standard library.
"""

import json
import sys


def resolve(value, primitives):
    """Resolve a semantic color value to a hex color."""
    if isinstance(value, str) and value.startswith("#"):
        return value

    color = primitives.get("color", {}).get(value)
    if color is None:
        raise KeyError(f"'{value}' is neither a hex value nor a color primitive")

    return color


def srgb_channel(c8):
    c = c8 / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color):
    h = hex_color.lstrip("#")

    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)

    if len(h) != 6:
        raise ValueError(f"bad hex color: {hex_color!r}")

    try:
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError as exc:
        raise ValueError(f"bad hex color: {hex_color!r}") from exc

    return (
        0.2126 * srgb_channel(r)
        + 0.7152 * srgb_channel(g)
        + 0.0722 * srgb_channel(b)
    )


def ratio(fg_hex, bg_hex):
    l1, l2 = sorted((luminance(fg_hex), luminance(bg_hex)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    try:
        with open(sys.argv[1], encoding="utf-8") as handle:
            tokens = json.load(handle)

        primitives = tokens["primitives"]
        modes = tokens["semantic"]
        pairs = tokens["contrast_pairs"]

    except (OSError, json.JSONDecodeError, KeyError) as exc:
        print(
            "Cannot read tokens file "
            f"({exc}). Expected keys: primitives, semantic, contrast_pairs."
        )
        return 2

    failures = 0

    for mode_name, mapping in modes.items():
        print(f"\n== {mode_name} ==")

        for pair in pairs:
            try:
                fg_name = pair["fg"]
                bg_name = pair["bg"]
                minimum = float(pair.get("min", 4.5))

                fg = resolve(mapping[fg_name], primitives)
                bg = resolve(mapping[bg_name], primitives)
                contrast_ratio = ratio(fg, bg)

            except (KeyError, TypeError, ValueError) as exc:
                fg_name = pair.get("fg", "?")
                bg_name = pair.get("bg", "?")
                print(f"  ERROR {fg_name} on {bg_name}: {exc}")
                failures += 1
                continue

            passed = contrast_ratio >= minimum

            if not passed:
                failures += 1

            mark = "PASS" if passed else "FAIL"

            print(
                f"  {mark}  "
                f"{fg_name} ({fg}) on {bg_name} ({bg}): "
                f"{contrast_ratio:.2f} (min {minimum})"
            )

    if failures == 0:
        print("\nAll pairs pass.")
        return 0

    print(f"\n{failures} failure(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
