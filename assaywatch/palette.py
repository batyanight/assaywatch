"""The one place a colour is chosen. Everything that renders reads from here.

`report.py`'s HTML, `figures.py`'s SVG and the website all show the same six
statuses and the same five calls, and before this module each picked its own
hexes. Changing a colour meant finding every literal; the website would have
added 218 more pages of them.

HOW THESE WERE CHOSEN, because "it looked right" is not a reason that survives a
change. Each set was run through the `dataviz` skill's validator
(`scripts/validate_palette.js`), which checks five things against the surface it
will be drawn on: an OKLCH lightness band, a chroma floor so nothing reads as
grey by accident, separation between adjacent pairs under simulated colour-vision
deficiency, separation under normal vision, and contrast against the background.

    LIGHT  (surface #fcfcfb)  all checks pass
    DARK   (surface #1a1a19)  all checks pass

One warning stands in LIGHT and is accepted deliberately: `stable` teal against
`watch` amber separate by only dE 7.6 under protanopia, inside the 6-8 band the
validator permits ONLY where a second, non-colour encoding carries the same
information. That condition is met everywhere these are used -- a status is
always written out in words beside its colour, in the report tables, the figure
legends and the site's status chips. Colour is never the only carrier. If a
future surface shows a status as a bare swatch, that surface is wrong, not this
palette.

`NEUTRAL` is deliberately grey and deliberately outside the validated set: it
marks the three statuses that are NOT a verdict (`insufficient data`, `no recent
data`, `no data`), where reading as "no colour" is the correct signal. Including
it in the categorical check fails the chroma floor, which is the validator
agreeing with its purpose rather than objecting to it.
"""

from __future__ import annotations

#: Statuses that are a verdict, in severity order. The grey ones are not here.
VERDICTS = ("declining", "low coverage", "watch", "stable")

#: No verdict: the tool declined to judge. See `drift.STATUS_ORDER` and `NO_DATA`.
NEUTRAL = "#5f6368"
NEUTRAL_DARK = "#9aa0a6"

STATUS_LIGHT = {
    "declining": "#b3261e",
    "low coverage": "#8a4b9c",
    "watch": "#b26a00",
    "stable": "#007d5c",
    "insufficient data": NEUTRAL,
    "no recent data": NEUTRAL,
    "no data": NEUTRAL,
}

STATUS_DARK = {
    "declining": "#c8584f",
    "low coverage": "#9f6dc2",
    "watch": "#b57800",
    "stable": "#269c79",
    "insufficient data": NEUTRAL_DARK,
    "no recent data": NEUTRAL_DARK,
    "no data": NEUTRAL_DARK,
}

#: The per-record call (`score.Call`). `detect` and `stable` share a colour on
#: purpose: both mean "this works", one per record and one per assay.
CALL_LIGHT = {
    "detect": "#007d5c",
    "reduced": "#b26a00",
    "fail": "#b3261e",
    "no_amplicon": NEUTRAL,
    "indeterminate": NEUTRAL,
}

CALL_DARK = {
    "detect": "#269c79",
    "reduced": "#b57800",
    "fail": "#c8584f",
    "no_amplicon": NEUTRAL_DARK,
    "indeterminate": NEUTRAL_DARK,
}

#: Chip backgrounds. A status chip is small bold text ON the colour, which is a
#: different contrast question from a mark drawn BESIDE text, so it gets its own
#: values rather than reusing the chart palette. Measured with the `dataviz`
#: validator's `contrast()`: in light mode white text clears 4.5:1 on every chart
#: colour, so the chips are the chart colours. In dark mode they do not -- black
#: text on `declining` reaches only 4.12 and white only 4.23 -- so the dark chips
#: are a lighter step of each hue carrying dark text, which clears 4.5:1 on all
#: five. Chart marks are unaffected; only the chips move.
CHIP_LIGHT = dict(STATUS_LIGHT)
CHIP_LIGHT_INK = "#ffffff"

CHIP_DARK = {
    "declining": "#d9776d",
    "low coverage": "#9f6dc2",
    "watch": "#b57800",
    "stable": "#269c79",
    "insufficient data": NEUTRAL_DARK,
    "no recent data": NEUTRAL_DARK,
    "no data": NEUTRAL_DARK,
}
CHIP_DARK_INK = "#17181a"

SURFACE_LIGHT = "#fcfcfb"
SURFACE_DARK = "#1a1a19"

#: Ink, for text drawn inside a figure. Never a series colour: a value or a label
#: wears text ink and the mark beside it carries the identity.
INK_LIGHT = "#202124"
INK_MUTED_LIGHT = "#5f6368"
INK_DARK = "#e8eaed"
INK_MUTED_DARK = "#9aa0a6"

#: Recessive grid and axis lines.
GRID_LIGHT = "#e5e7e9"
GRID_DARK = "#35373a"


def status_colour(status: str, dark: bool = False) -> str:
    table = STATUS_DARK if dark else STATUS_LIGHT
    return table.get(status, NEUTRAL_DARK if dark else NEUTRAL)


def call_colour(call: str, dark: bool = False) -> str:
    table = CALL_DARK if dark else CALL_LIGHT
    return table.get(call, NEUTRAL_DARK if dark else NEUTRAL)


def css_variables() -> str:
    """The palette as CSS custom properties, light with a dark override.

    The dark block is written twice on purpose: once under the media query for a
    reader whose system is dark, and once under an explicit attribute, because
    MkDocs Material lets a reader override the system setting and then neither
    branch of a media query alone is right.
    """

    def block(
        statuses: dict[str, str], calls: dict[str, str], surface: str, ink: str, muted: str, grid: str
    ) -> str:
        lines = [f"  --aw-status-{k.replace(' ', '-')}: {v};" for k, v in statuses.items()]
        lines += [f"  --aw-call-{k}: {v};" for k, v in calls.items()]
        chips = CHIP_DARK if surface == SURFACE_DARK else CHIP_LIGHT
        ink_on_chip = CHIP_DARK_INK if surface == SURFACE_DARK else CHIP_LIGHT_INK
        lines += [f"  --aw-chip-{k.replace(' ', '-')}: {v};" for k, v in chips.items()]
        lines.append(f"  --aw-chip-ink: {ink_on_chip};")
        lines += [
            f"  --aw-surface: {surface};",
            f"  --aw-ink: {ink};",
            f"  --aw-ink-muted: {muted};",
            f"  --aw-grid: {grid};",
        ]
        return "\n".join(lines)

    light = block(STATUS_LIGHT, CALL_LIGHT, SURFACE_LIGHT, INK_LIGHT, INK_MUTED_LIGHT, GRID_LIGHT)
    dark = block(STATUS_DARK, CALL_DARK, SURFACE_DARK, INK_DARK, INK_MUTED_DARK, GRID_DARK)
    return (
        "/* Generated by assaywatch.palette.css_variables(); edit the module, not this file. */\n"
        f":root {{\n{light}\n}}\n\n"
        f'[data-md-color-scheme="slate"] {{\n{dark}\n}}\n'
    )
