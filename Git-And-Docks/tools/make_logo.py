"""Generates the animated Arkomiko logo (dark and light) from the Halfomania font.

Needs fontTools (pip install fonttools) and Halfomania installed for the current Windows user.
Run: python Git-And-Docks/tools/make_logo.py
"""
import os
import random
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\halfomania_regular.ttf")
TEXT = "Arkomiko"
W, H = 1000, 260
TEXT_W = 760

THEMES = {
    "dark": {
        "stops": ["#FFC7EC", "#FF8FC8", "#B983FF", "#FFC7EC"],
        "stroke": "#FFC7EC",
        "glow": "#FF8FC8",
        "petals": ["#FFC7EC", "#FFB3DE", "#E9C6FF"],
        "shine": "#FFFFFF",
    },
    "light": {
        "stops": ["#F06BB5", "#E0479E", "#8E4FE0", "#F06BB5"],
        "stroke": "#B03A86",
        "glow": "#F9A8D4",
        "petals": ["#F7A6CF", "#F28DC2", "#C9A3F2"],
        "shine": "#FFFFFF",
    },
}

PETAL = "M0 -6L-3 -11C-9 -10 -11 -2 -7 5C-4 10 0 12 0 12C0 12 4 10 7 5C11 -2 9 -10 3 -11Z"


def glyph_paths():
    font = TTFont(FONT)
    cmap, gs, hmtx = font.getBestCmap(), font.getGlyphSet(), font["hmtx"]
    total = sum(hmtx[cmap[ord(c)]][0] for c in TEXT)
    s = TEXT_W / total

    # First pass: bounds in font units, to centre the word vertically.
    bp = BoundsPen(gs)
    x = 0
    for c in TEXT:
        g = cmap[ord(c)]
        gs[g].draw(TransformPen(bp, (1, 0, 0, 1, x, 0)))
        x += hmtx[g][0]
    xmin, ymin, xmax, ymax = bp.bounds
    ox = (W - (xmax - xmin) * s) / 2 - xmin * s
    oy = H / 2 + (ymax + ymin) / 2 * s  # baseline so that the bbox is centred

    paths, x = [], 0
    for c in TEXT:
        g = cmap[ord(c)]
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, ox + x * s, oy)))
        paths.append(pen.getCommands())
        x += hmtx[g][0]
    return paths


def petals(rng, colors):
    out, css = [], []
    for i in range(12):
        x = rng.uniform(30, W - 30)
        scale = rng.uniform(0.7, 1.4)
        dur = rng.uniform(7, 12)
        delay = -rng.uniform(0, dur)  # negative: petals are already mid-air on load
        dx1, dx2 = rng.uniform(-60, 60), rng.uniform(-90, 90)
        rot = rng.choice([-1, 1]) * rng.uniform(220, 520)
        css.append(
            f"@keyframes f{i}{{0%{{transform:translate(0,-30px) rotate(0deg) scale({scale:.2f});opacity:0}}"
            f"12%{{opacity:.85}}50%{{transform:translate({dx1:.0f}px,{H / 2:.0f}px) rotate({rot / 2:.0f}deg) scale({scale:.2f})}}"
            f"88%{{opacity:.85}}100%{{transform:translate({dx2:.0f}px,{H + 30}px) rotate({rot:.0f}deg) scale({scale:.2f});opacity:0}}}}"
            f".p{i}{{animation:f{i} {dur:.1f}s linear {delay:.1f}s infinite}}"
        )
        out.append(
            f'<g transform="translate({x:.0f} 0)"><path class="petal p{i}" d="{PETAL}" '
            f'fill="{colors[i % len(colors)]}"/></g>'
        )
    return "\n    ".join(out), "".join(css)


def build(theme, paths):
    t = THEMES[theme]
    rng = random.Random(7)  # same petal layout in both themes
    petal_svg, petal_css = petals(rng, t["petals"])
    stops = "".join(
        f'<stop offset="{i / (len(t["stops"]) - 1):.2f}" stop-color="{c}"/>' for i, c in enumerate(t["stops"])
    )
    defs = "\n    ".join(f'<path id="g{i}" d="{d}"/>' for i, d in enumerate(paths))
    # letters fill in one by one after their outline has been drawn
    fills = "\n    ".join(
        f'<use href="#g{i}" class="fill" style="animation-delay:{1.3 + 0.08 * i:.2f}s"/>' for i in range(len(paths))
    )
    strokes = "\n    ".join(
        f'<path d="{d}" class="stroke" pathLength="1" style="animation-delay:{0.12 * i:.2f}s"/>'
        for i, d in enumerate(paths)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Arkomiko">
  <title>Arkomiko</title>
  <style>
    .petal{{transform-box:fill-box;transform-origin:center;opacity:0}}
    {petal_css}
    .stroke{{fill:none;stroke:{t["stroke"]};stroke-width:2.5;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:1;animation:draw 1.6s cubic-bezier(.6,.1,.3,1) both}}
    @keyframes draw{{to{{stroke-dashoffset:0}}}}
    .fill{{fill:url(#grad);opacity:0;animation:show 1s ease-out both}}
    @keyframes show{{to{{opacity:1}}}}
    .glow{{opacity:0;animation:glow 4s ease-in-out 2.4s infinite both}}
    @keyframes glow{{0%,100%{{opacity:.25}}50%{{opacity:.6}}}}
    .shine{{animation:shine 7s ease-in-out 2.6s infinite both}}
    @keyframes shine{{0%{{transform:translateX(-300px)}}35%,100%{{transform:translateX({W + 300}px)}}}}
    @media (prefers-reduced-motion:reduce){{
      .stroke,.fill,.glow,.shine,.petal{{animation:none}}
      .stroke{{stroke-dashoffset:0}}.fill{{opacity:1}}.glow{{opacity:.35}}.shine,.petal{{display:none}}
    }}
  </style>
  <defs>
    {defs}
    <linearGradient id="grad" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="0" spreadMethod="repeat">
      {stops}
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="{W} 0" dur="8s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="shineGrad" x1="0" x2="1">
      <stop offset="0" stop-color="{t["shine"]}" stop-opacity="0"/>
      <stop offset=".5" stop-color="{t["shine"]}" stop-opacity=".75"/>
      <stop offset="1" stop-color="{t["shine"]}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="clip">
      {"".join(f'<use href="#g{i}"/>' for i in range(len(paths)))}
    </clipPath>
    <filter id="blur" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>
  </defs>
  <g>
    {petal_svg}
  </g>
  <g class="glow" filter="url(#blur)" fill="{t["glow"]}">
    {"".join(f'<use href="#g{i}"/>' for i in range(len(paths)))}
  </g>
  <g>
    {fills}
  </g>
  <g clip-path="url(#clip)">
    <rect class="shine" x="0" y="-40" width="140" height="{H + 80}" fill="url(#shineGrad)" transform="skewX(-20)"/>
  </g>
  <g>
    {strokes}
  </g>
</svg>
"""


if __name__ == "__main__":
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
    os.makedirs(out_dir, exist_ok=True)
    paths = glyph_paths()
    for theme in THEMES:
        with open(os.path.join(out_dir, f"logo-{theme}.svg"), "w", encoding="utf-8", newline="\n") as f:
            f.write(build(theme, paths))
    print("ok", [len(p) for p in paths])
