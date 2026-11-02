"""The one place a color is chosen. Everything that renders reads from here.

`report.py`'s HTML, `figures.py`'s SVG and the website all show the same six
statuses and the same five calls, and before this module each picked its own
hexes. Changing a color meant finding every literal; the website would have
added 218 more pages of them.

HOW THESE WERE CHOSEN. Four hues, one per verdict: deep red for `declining`,
violet for `low coverage`, amber for `watch`, olive for `stable`. The olive is
the one that was asked for; the other three follow from it, because the four
have to be told apart.

Every value was solved rather than picked, then run through the `dataviz`
skill's validator (`scripts/validate_palette.js`) against the surface it is
drawn on, comparing ALL pairs rather than only adjacent ones:

    LIGHT  (paper #ffffff)   worst pair dE 10.5   chip text >= 5.22:1
    DARK   (paper #15140f)   worst pair dE 12.1   chip text >= 5.77:1

THE HARD PAIR IS OLIVE AGAINST AMBER, and it is worth knowing why. Both sit in
the yellow half of the wheel, so under protanopia and deuteranopia hue barely
separates them; what separates them is lightness. In light mode Demuth-style
values work because amber is light (L 0.72) and olive is dark (L 0.53). In dark
mode both must rise, which closes that gap: a first attempt put them at dE 4.7
under protanopia, meaning two statuses that look identical to a red-green
color-blind reader. The dark olive is therefore lifted well past the amber (L
0.79 against 0.63) and shifted toward green, which is why it reads brighter
there than the light-mode olive does.

A note on an error in an earlier revision of this file: it recorded a palette
as passing when the validator had returned `relief`, its label for contrast
below 3:1, which the check treated as a pass. `relief` means "legible only with
a label beside it" -- true of a chip, false of a bar in a chart. It now counts
as a failure.

`NEUTRAL` is deliberately gray and deliberately outside the validated set: it
marks the three statuses that are NOT a verdict (`insufficient data`, `no recent
data`, `no data`), where reading as "no color" is the correct signal. Including
it in the categorical check fails the chroma floor, which is the validator
agreeing with its purpose rather than objecting to it.
"""

from __future__ import annotations

#: Statuses that are a verdict, in severity order. The gray ones are not here.
VERDICTS = ("declining", "low coverage", "watch", "stable")

#: No verdict: the tool declined to judge. See `drift.STATUS_ORDER` and `NO_DATA`.
NEUTRAL = "#6b6b6b"
NEUTRAL_DARK = "#a39d92"

STATUS_LIGHT = {
    "declining": "#861210",
    "low coverage": "#493883",
    "watch": "#c9872c",
    "stable": "#62740d",
    "insufficient data": NEUTRAL,
    "no recent data": NEUTRAL,
    "no data": NEUTRAL,
}

STATUS_DARK = {
    "declining": "#af3c3a",
    "low coverage": "#6959ae",
    "watch": "#c68206",
    "stable": "#9cc86c",
    "insufficient data": NEUTRAL_DARK,
    "no recent data": NEUTRAL_DARK,
    "no data": NEUTRAL_DARK,
}

#: The per-record call (`score.Call`). `detect` and `stable` share a color on
#: purpose: both mean "this works", one per record and one per assay.
CALL_LIGHT = {
    "detect": "#62740d",
    "reduced": "#c9872c",
    "fail": "#861210",
    "no_amplicon": NEUTRAL,
    "indeterminate": NEUTRAL,
}

CALL_DARK = {
    "detect": "#9cc86c",
    "reduced": "#c68206",
    "fail": "#af3c3a",
    "no_amplicon": NEUTRAL_DARK,
    "indeterminate": NEUTRAL_DARK,
}

#: Chips put small bold text ON the color, which is a different contrast
#: question from a mark drawn BESIDE text, so the ink is chosen per color by
#: measurement: white on the three dark ones, near-black on amber and on the
#: lifted dark olive. Everything clears 5.2:1.
CHIP_LIGHT = dict(STATUS_LIGHT)
CHIP_DARK = dict(STATUS_DARK)
CHIP_INK_ON = {"#c9872c": "#15140f", "#c68206": "#15140f", "#9cc86c": "#15140f"}
CHIP_LIGHT_INK = "#ffffff"
CHIP_DARK_INK = "#ffffff"

#: Links. Rust, so a link is never mistaken for a verdict, and underlined in
#: the stylesheet: at 2.56:1 against body text color alone would not identify
#: it, and the underline is what satisfies that requirement rather than the
#: hue. Against the page it is 6.81:1.
LINK_LIGHT = "#9c3c22"
LINK_DARK = "#e08a6a"

SURFACE_LIGHT = "#ffffff"
SURFACE_DARK = "#15140f"

#: Ink, for text drawn inside a figure. Never a series color: a value or a label
#: wears text ink and the mark beside it carries the identity.
INK_LIGHT = "#1a1a1a"
INK_MUTED_LIGHT = "#6b6b6b"
INK_DARK = "#e9e6de"
INK_MUTED_DARK = "#a39d92"

#: Recessive grid and axis lines.
GRID_LIGHT = "#e2e0dc"
GRID_DARK = "#312e27"


def status_colour(status: str, dark: bool = False) -> str:
    table = STATUS_DARK if dark else STATUS_LIGHT
    return table.get(status, NEUTRAL_DARK if dark else NEUTRAL)


def call_colour(call: str, dark: bool = False) -> str:
    table = CALL_DARK if dark else CALL_LIGHT
    return table.get(call, NEUTRAL_DARK if dark else NEUTRAL)


def css_variables() -> str:
    """The palette as CSS custom properties, light with a dark override.

    The dark block is written twice on purpose: once under the media query, for
    a reader whose system is dark, and once under an explicit attribute, so a
    future theme toggle has something to set. The media-query block is guarded
    by `:root:not([data-theme="light"])` so an explicit light choice wins over
    the system preference rather than fighting it.
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
            f"  --aw-chip-ink-{k.replace(' ', '-')}: {CHIP_INK_ON.get(v, ink_on_chip)};"
            for k, v in chips.items()
        ]
        lines += [
            f"  --aw-surface: {surface};",
            f"  --aw-ink: {ink};",
            f"  --aw-ink-muted: {muted};",
            f"  --aw-grid: {grid};",
            f"  --aw-link: {LINK_DARK if surface == SURFACE_DARK else LINK_LIGHT};",
        ]
        return "\n".join(lines)

    light = block(STATUS_LIGHT, CALL_LIGHT, SURFACE_LIGHT, INK_LIGHT, INK_MUTED_LIGHT, GRID_LIGHT)
    dark = block(STATUS_DARK, CALL_DARK, SURFACE_DARK, INK_DARK, INK_MUTED_DARK, GRID_DARK)
    return (
        "/* Generated by assaywatch.palette.css_variables(); edit the module, not this file. */\n"
        f":root {{\n{light}\n}}\n\n"
        f"@media (prefers-color-scheme: dark) {{\n"
        f'  :root:not([data-theme="light"]) {{\n{dark}\n  }}\n'
        f"}}\n"
        f'[data-theme="dark"] {{\n{dark}\n}}\n'
    )
