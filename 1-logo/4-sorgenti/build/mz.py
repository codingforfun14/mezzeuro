"""Helpers for the mezzeuro logo concepts: outlined type via CoreText, path transforms, SVG output."""
import json
import math
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "ctpaths.swift")
BIN = os.path.join(HERE, ".cache", "ctpaths")

_cache = {}
_TOK = re.compile(r"[MLQCZ]|-?\d+(?:\.\d+)?")
_NPTS = {"M": 1, "L": 1, "Q": 2, "C": 3, "Z": 0}


def _ensure_bin():
    if not os.path.exists(BIN) or os.path.getmtime(BIN) < os.path.getmtime(SRC):
        os.makedirs(os.path.dirname(BIN), exist_ok=True)
        subprocess.run(["swiftc", "-O", SRC, "-o", BIN], check=True)


def shape(font, size, text, tracking=0.0):
    """Glyph outlines + metrics for `text` set in `font` (PostScript name) at `size`."""
    key = (font, float(size), text, float(tracking))
    if key not in _cache:
        _ensure_bin()
        res = subprocess.run([BIN, font, str(size), text, str(tracking)], capture_output=True, text=True)
        if res.returncode != 0:
            raise RuntimeError(res.stderr.strip())
        _cache[key] = json.loads(res.stdout)
    return _cache[key]


def f(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def xform(d, fn):
    """Map every point of an absolute M/L/Q/C/Z path through fn(x, y) -> (x, y)."""
    toks, out, i = _TOK.findall(d), [], 0
    while i < len(toks):
        cmd = toks[i]
        i += 1
        pts = []
        for _ in range(_NPTS[cmd]):
            pts.append(fn(float(toks[i]), float(toks[i + 1])))
            i += 2
        out.append(cmd + " ".join(f"{f(x)} {f(y)}" for x, y in pts))
    return "".join(out)


def affine(d, s=1.0, dx=0.0, dy=0.0):
    return xform(d, lambda x, y: (x * s + dx, y * s + dy))


def points(d):
    toks = _TOK.findall(d)
    nums = [float(t) for t in toks if t not in _NPTS]
    return list(zip(nums[0::2], nums[1::2]))


def subpaths(d):
    """Point lists (anchors and control points) per subpath of an absolute M/L/Q/C/Z path."""
    out, cur = [], None
    toks, i = _TOK.findall(d), 0
    while i < len(toks):
        cmd = toks[i]
        i += 1
        if cmd == "M":
            cur = []
            out.append(cur)
        for _ in range(_NPTS[cmd]):
            cur.append((float(toks[i]), float(toks[i + 1])))
            i += 2
    return out


def signed_area(pts):
    return 0.5 * sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))


def outer_is_ccw(d):
    """True if the largest subpath winds counter-clockwise on screen (negative area in SVG coordinates)."""
    areas = [signed_area(p) for p in subpaths(d) if len(p) > 2]
    return max(areas, key=abs) < 0


def bbox(d):
    pts = points(d)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return [min(xs), min(ys), max(xs), max(ys)]


def text(font, size, s, x=0.0, y=0.0, tracking=0.0):
    """Outlined text with its baseline-left at (x, y). Returns (d, ink_bbox)."""
    info = shape(font, size, s, tracking)
    parts, bb = [], [math.inf, math.inf, -math.inf, -math.inf]
    for g in info["glyphs"]:
        if not g["d"]:
            continue
        gx = x + g["x"]
        parts.append(affine(g["d"], 1, gx, y))
        b = g["bbox"]
        bb = [min(bb[0], gx + b[0]), min(bb[1], y + b[1]), max(bb[2], gx + b[2]), max(bb[3], y + b[3])]
    return "".join(parts), bb


def text_fit(font, s, x, baseline, height=None, width=None, tracking_em=0.0, ref="ink"):
    """Set text so its ink height (or width) matches; baseline-left ink edge at x. Returns (d, bbox)."""
    probe = 1000.0
    d0, b0 = text(font, probe, s, tracking=tracking_em * probe)
    if height is not None:
        k = height / (b0[3] - b0[1]) if ref == "ink" else height / shape(font, probe, s)[ref]
    else:
        k = width / (b0[2] - b0[0])
    d = affine(d0, k, x - b0[0] * k, baseline)
    return d, bbox_scaled(b0, k, x - b0[0] * k, baseline)


def bbox_scaled(b, k, dx, dy):
    return [b[0] * k + dx, b[1] * k + dy, b[2] * k + dx, b[3] * k + dy]


def arc_text(font, size, s, cx, cy, r, where="top", tracking=0.0):
    """Text along a circle of radius r (baseline radius). top: reads clockwise over the top, letters point out;
    bottom: reads left-to-right under the centre, letters point in."""
    gl = [g for g in shape(font, size, s, tracking)["glyphs"] if g["d"]]
    left = gl[0]["x"] + gl[0]["bbox"][0]
    right = gl[-1]["x"] + gl[-1]["bbox"][2]
    mid = (left + right) / 2
    parts = []
    for g in gl:
        gc = (g["bbox"][0] + g["bbox"][2]) / 2
        t = (g["x"] + gc - mid) / r
        if where == "top":
            phi, rot = -math.pi / 2 + t, t
        else:
            phi, rot = math.pi / 2 - t, -t
        px, py = cx + r * math.cos(phi), cy + r * math.sin(phi)
        c, sn = math.cos(rot), math.sin(rot)

        def fn(x, y, gc=gc, px=px, py=py, c=c, sn=sn):
            u = x - gc
            return (px + u * c - y * sn, py + u * sn + y * c)

        parts.append(xform(g["d"], fn))
    return "".join(parts)


# ---- primitives (absolute paths) -------------------------------------------------------------

def circle(cx, cy, r, ccw=False):
    sw = 0 if ccw else 1
    return (f"M{f(cx - r)} {f(cy)}A{f(r)} {f(r)} 0 1 {sw} {f(cx + r)} {f(cy)}"
            f"A{f(r)} {f(r)} 0 1 {sw} {f(cx - r)} {f(cy)}Z")


def ring(cx, cy, r_out, r_in):
    """Annulus as one path (outer clockwise, inner counter-clockwise) - works with nonzero and evenodd."""
    return circle(cx, cy, r_out) + circle(cx, cy, r_in, ccw=True)


def rect(x, y, w, h, ccw=False):
    if ccw:
        return f"M{f(x)} {f(y)}V{f(y + h)}H{f(x + w)}V{f(y)}Z"
    return f"M{f(x)} {f(y)}H{f(x + w)}V{f(y + h)}H{f(x)}Z"


def half_disc(cx, cy, r, side="lower"):
    """Half disc cut by the horizontal diameter."""
    sweep = 0 if side == "lower" else 1
    return f"M{f(cx - r)} {f(cy)}A{f(r)} {f(r)} 0 0 {sweep} {f(cx + r)} {f(cy)}Z"


def svg(w, h, body, title="mezzeuro"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" width="{f(w)}" height="{f(h)}" '
            f'role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>\n')


def path(d, fill="#111111", evenodd=False, ident=None):
    fr = ' fill-rule="evenodd"' if evenodd else ""
    i = f' id="{ident}"' if ident else ""
    return f'<path{i} fill="{fill}"{fr} d="{d}"/>'


def write(fname, content):
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(content)
    return fname
