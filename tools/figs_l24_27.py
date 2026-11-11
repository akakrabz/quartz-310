#!/usr/bin/env python3
"""Figures for Lectures 24-27: STFT, FFT, butterfly diagrams, fast convolution, filter design.

Usage:  python3 -B tools/figs_l24_27.py OUTDIR

Writes OUTDIR/<name>.html, each a single-line <figure class="ece-fig"> block, to be inlined
where a page has the marker <!-- fig:<name> --> (tools/assemble.py does this when OUTDIR is
tools/figs). Needs numpy only. Strokes use currentColor and the CSS variables --accent,
--accent2, --hi, --muted and --paper (quartz/styles/custom.scss), so the figures follow the
light and dark themes. Every plotted curve is computed here, nothing is traced.
"""
import math
import os
import sys

import numpy as np

SANS = "font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif"
MATH = "font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;"
INK, ACC, ACC2, HI, MUTED, PAPER = ("currentColor", "var(--accent)", "var(--accent2)",
                                    "var(--hi)", "var(--muted)", "var(--paper)")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
PI = math.pi


def f(v):
    return f"{v:.1f}"


def sub(s):
    return str(s).translate(SUB)


def W(lower, upper, neg=False):
    """Twiddle factor W_lower^upper as SVG text content."""
    return (("−" if neg else "") + f'W<tspan dy="4" style="font-size:9px">{lower}</tspan>'
            f'<tspan dy="-10" style="font-size:9px">{upper}</tspan>')


ZINV = 'z<tspan dy="-5" style="font-size:9px">−1</tspan>'


class Fig:
    def __init__(self, name, w, h, label, size=13):
        self.name, self.w, self.h, self.label, self.size = name, w, h, label, size
        self.out = []
        self.mid = "ah-" + name

    def line(self, x1, y1, x2, y2, c=INK, w=1.5, dash=None, arrow=False, op=None, both=False):
        s = f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{c}" stroke-width="{w}"'
        if dash:
            s += f' stroke-dasharray="{dash}"'
        if op is not None:
            s += f' opacity="{op}"'
        if arrow or both:
            s += f' marker-end="url(#{self.mid})"'
        if both:
            s += f' marker-start="url(#{self.mid})"'
        self.out.append(s + ' stroke-linecap="round"/>')

    def text(self, x, y, s, anchor="middle", c=INK, size=None, math=False, bold=False, halo=False):
        st = f"font-size:{size or self.size}px;"
        if math:
            st += MATH
        if bold:
            st += "font-weight:600;"
        if halo:
            st += f"paint-order:stroke;stroke:{PAPER};stroke-width:3.5px;stroke-linejoin:round;"
        self.out.append(f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anchor}" fill="{c}" style="{st}">{s}</text>')

    def dot(self, x, y, r=3.0, c=INK):
        self.out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{r}" fill="{c}"/>')

    def rect(self, x, y, w, h, fill="none", stroke=INK, sw=1.2, rx=0, fop=None):
        s = f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}"'
        if rx:
            s += f' rx="{rx}"'
        if fop is not None:
            s += f' fill-opacity="{fop}"'
        s += ' stroke="none"/>' if stroke is None else f' stroke="{stroke}" stroke-width="{sw}"/>'
        self.out.append(s)

    def path(self, d, c=INK, w=1.6, fill="none", fop=None, dash=None):
        s = f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linejoin="round"'
        if fop is not None:
            s += f' fill-opacity="{fop}"'
        if dash:
            s += f' stroke-dasharray="{dash}"'
        self.out.append(s + "/>")

    def flow(self, x1, y1, x2, y2, label=None, off=(0, -9), anchor="middle", c=INK, t=0.5,
             w=1.6, math=True, lc=None, size=None, lt=None):
        """A signal-flow branch: a line with an arrowhead at fraction t and an optional gain label."""
        self.line(x1, y1, x2, y2, c=c, w=w)
        dx, dy = x2 - x1, y2 - y1
        n = math_hypot(dx, dy)
        ux, uy = dx / n, dy / n
        mx, my = x1 + dx * t, y1 + dy * t
        s = 5.0
        tip = (mx + ux * s, my + uy * s)
        b1 = (mx - ux * s - uy * s * 0.75, my - uy * s + ux * s * 0.75)
        b2 = (mx - ux * s + uy * s * 0.75, my - uy * s - ux * s * 0.75)
        self.out.append(f'<path d="M{f(tip[0])},{f(tip[1])} L{f(b1[0])},{f(b1[1])} L{f(b2[0])},{f(b2[1])} Z" fill="{c}"/>')
        if label is not None:
            if lt is not None:
                mx, my = x1 + dx * lt, y1 + dy * lt
            self.text(mx + off[0], my + off[1], label, anchor=anchor, c=lc or c, math=math,
                      size=size or self.size, halo=True)

    def html(self, caption):
        defs = (f'<defs><marker id="{self.mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
                f'fill="context-stroke"/></marker></defs>')
        return self.name, (
            f'<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img" aria-label="{self.label}" '
            f'style="{SANS};font-size:{self.size}px">' + defs + "".join(self.out)
            + f"</svg><figcaption>{caption}</figcaption></figure>\n")

    def vtext(self, x, y, s, **kw):
        """Text rotated to read bottom-to-top (axis labels)."""
        self.text(x, y, s, **kw)
        self.out[-1] = self.out[-1].replace("<text ", f'<text transform="rotate(-90 {f(x)} {f(y)})" ', 1)


def math_hypot(a, b):
    return math.hypot(a, b) or 1.0


# ------------------------------------------------------------------ Lecture 24: STFT
def fig_stft_windows():
    F = Fig("stft-windows", 680, 236, "a long signal cut into overlapping windows of length L, stride S")
    x0, x1, yb = 56, 636, 62
    # a signal whose frequency steps up four times (four "notes")
    pts, seg = [], (x1 - x0) / 4
    for i in range(0, 581):
        x = x0 + i
        note = min(3, int(i // seg))
        freq = [0.10, 0.16, 0.24, 0.34][note]
        pts.append(f"{f(x)},{f(yb - 22 * math.sin(freq * (i - note * seg)))}")
    F.path("M" + " L".join(pts), c=ACC, w=1.3)
    F.line(x0, yb + 32, x1, yb + 32, w=1, op=0.75)
    F.text(x0 - 6, yb + 36, "n = 0", size=11, c=MUTED, anchor="end")
    F.text(x1 + 6, yb + 36, "N − 1", size=11, c=MUTED, anchor="start")
    for i in range(1, 4):
        F.line(x0 + i * seg, yb - 30, x0 + i * seg, yb + 32, c=MUTED, w=0.8, dash="3 3")
    F.text(x0 + seg / 2, 22, "note 1", size=11, c=MUTED)
    F.text(x0 + 1.5 * seg, 22, "note 2", size=11, c=MUTED)
    F.text(x0 + 2.5 * seg, 22, "note 3", size=11, c=MUTED)
    F.text(x0 + 3.5 * seg, 22, "note 4", size=11, c=MUTED)
    L, S = 110, 55
    for t in range(6):
        xa, ya = x0 + t * S, 122 + 15 * t
        F.rect(xa, ya, L, 11, fill=ACC2, stroke=ACC2, sw=1, rx=2, fop=0.22)
        F.text(xa - 6, ya + 9.5, f"t = {t}", anchor="end", size=11, c=MUTED)
    F.text(x0 + 6 * S + 4, 122 + 15 * 6 + 6, "⋯", anchor="start", c=MUTED)
    # L and S dimensions
    F.line(x0, 112, x0 + L, 112, c=INK, w=1, both=True)
    F.text(x0 + L / 2, 107, "L samples", size=11)
    F.line(x0 + L + 2 * S, 122 + 15 * 2 + 5.5, x0 + L + 3 * S, 122 + 15 * 2 + 5.5, c=INK, w=1, both=True)
    F.text(x0 + L + 2.5 * S, 122 + 15 * 2 - 1, "S", size=11)
    F.text(470, 162, "each window × w[m]", anchor="start", size=12)
    F.text(470, 179, "→ one length-L DFT", anchor="start", size=12)
    F.text(470, 196, "→ one column X[t, k]", anchor="start", size=12)
    return F.html("<strong>The short-time Fourier transform cuts the signal into overlapping windows.</strong> "
                  "Window t starts at sample St and covers L samples; each window is multiplied by w[m] and "
                  "sent through its own length-L DFT. A short window says precisely <em>when</em> a note sounds, "
                  "a long window says precisely <em>which</em> frequency it has (Lecture 24, eq. 3).")


def stft_mag(x, L, S, nfft):
    w = 0.54 - 0.46 * np.cos(2 * PI * np.arange(L) / (L - 1))
    frames = [np.abs(np.fft.rfft(x[s:s + L] * w, nfft)) for s in range(0, len(x) - L + 1, S)]
    return np.array(frames)            # frames x bins


def fig_stft_tradeoff():
    fs = 2000.0
    notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
    n1 = int(0.5 * fs)
    x = np.concatenate([np.cos(2 * PI * fq * np.arange(n1) / fs) for fq in notes])
    F = Fig("stft-tradeoff", 680, 306, "spectrograms of an eight-note scale with a short and a long window")
    cols, rows, fmin, fmax, T = 64, 36, 220.0, 580.0, 4.0
    pw, ph = 280, 198
    for p, (L, S, title) in enumerate([(64, 16, "L = 64 (32 ms): good in time, blurred in frequency"),
                                       (1024, 64, "L = 1024 (0.51 s): good in frequency, blurred in time")]):
        ox, oy = 56 + p * 330, 40
        nfft = 4096
        M = stft_mag(x, L, S, nfft)
        tc = (np.arange(M.shape[0]) * S + L / 2) / fs          # frame centres, seconds
        fbin = np.arange(M.shape[1]) * fs / nfft
        G = np.zeros((rows, cols))
        for c in range(cols):
            t = (c + 0.5) * T / cols
            fr = M[int(np.argmin(np.abs(tc - t)))]
            for r in range(rows):
                lo = fmin + r * (fmax - fmin) / rows
                hi = lo + (fmax - fmin) / rows
                G[r, c] = fr[(fbin >= lo) & (fbin < hi)].max()
        dB = 20 * np.log10(G / G.max() + 1e-12)
        lev = (dB > -30).astype(int) + (dB > -18) + (dB > -9) + (dB > -3)
        cw, chh = pw / cols, ph / rows
        F.rect(ox, oy, pw, ph, stroke=INK, sw=1)
        for r in range(rows):
            c = 0
            while c < cols:
                v = lev[r, c]
                c2 = c
                while c2 < cols and lev[r, c2] == v:
                    c2 += 1
                if v:
                    F.rect(ox + c * cw, oy + ph - (r + 1) * chh, (c2 - c) * cw, chh, fill=ACC, stroke=None,
                           fop=[0, 0.14, 0.34, 0.62, 0.95][v])
                c = c2
        F.text(ox + pw / 2, oy - 12, title, size=12, bold=True)
        for tt in range(5):
            xx = ox + tt * pw / T
            F.line(xx, oy + ph, xx, oy + ph + 4, w=1)
            F.text(xx, oy + ph + 17, f"{tt}", size=11, c=MUTED)
        F.text(ox + pw / 2, oy + ph + 34, "time (s)", size=11)
        for fq in (300, 400, 500):
            yy = oy + ph - (fq - fmin) / (fmax - fmin) * ph
            F.line(ox - 4, yy, ox, yy, w=1)
            F.text(ox - 7, yy + 4, f"{fq}", anchor="end", size=11, c=MUTED)
    F.vtext(14, 40 + ph / 2, "frequency (Hz)", size=11)
    return F.html("<strong>One signal, two window lengths (computed).</strong> A C-major scale, eight notes of "
                  "0.5 s each, sampled at 2 kHz, Hamming window, darker = more energy (steps at −3, −9, −18 and "
                  "−30 dB below the peak). Left: 32 ms windows place each note change exactly but smear every "
                  "note over about ±60 Hz (main-lobe width 8π/L, i.e. 4f<sub>s</sub>/L = 125 Hz), so neighbouring "
                  "notes overlap. Right: half-second windows give thin lines 8 Hz wide, but a window that "
                  "straddles two notes shows both, so the changes are blurred over about half a second.")


# ------------------------------------------------------------------ Lecture 25: FFT
def fig_split_tree():
    F = Fig("fft-split-tree", 660, 262, "splitting a length-8 signal into even and odd samples three times")
    ys = [30, 94, 158, 222]

    def box(cx, cy, w, s, fill=None):
        F.rect(cx - w / 2, cy - 14, w, 28, fill=fill or "none", stroke=INK, sw=1.2, rx=4,
               fop=0.12 if fill else None)
        F.text(cx, cy + 4.5, s, size=13)

    box(330, ys[0], 310, "x[n] = { x₀, x₁, x₂, x₃, x₄, x₅, x₆, x₇ }")
    lv1 = [(170, "a[n] = { x₀, x₂, x₄, x₆ }"), (490, "b[n] = { x₁, x₃, x₅, x₇ }")]
    lv2 = [(90, "c = { x₀, x₄ }"), (250, "d = { x₂, x₆ }"), (410, "e = { x₁, x₅ }"), (570, "f = { x₃, x₇ }")]
    lv3 = [(55, "x₀"), (125, "x₄"), (215, "x₂"), (285, "x₆"), (375, "x₁"), (445, "x₅"), (535, "x₃"), (605, "x₇")]
    for cx, s in lv1:
        F.line(330, ys[0] + 14, cx, ys[1] - 14, w=1.2)
        box(cx, ys[1], 236, s)
    F.text(228, ys[0] + 36, "even n", size=11, c=MUTED, anchor="end")
    F.text(432, ys[0] + 36, "odd n", size=11, c=MUTED, anchor="start")
    for i, (cx, s) in enumerate(lv2):
        F.line(lv1[i // 2][0], ys[1] + 14, cx, ys[2] - 14, w=1.2)
        box(cx, ys[2], 132, s)
    for i, (cx, s) in enumerate(lv3):
        F.line(lv2[i // 2][0], ys[2] + 14, cx, ys[3] - 14, w=1.2)
        box(cx, ys[3], 48, s, fill=ACC)
    F.text(330, 256, "length-1 sequences: each one is its own DFT, so the merging can start here", size=12, c=MUTED)
    return F.html("<strong>Step 1 for N = 8: split by even and odd index until every piece has length 1.</strong> "
                  "The names a to f follow the lecture; the tree records which pairs are merged later "
                  "(c with d into A, e with f into B, A with B into X). The bottom row is the input order of the "
                  "butterfly diagram: x<sub>0</sub>, x<sub>4</sub>, x<sub>2</sub>, x<sub>6</sub>, x<sub>1</sub>, "
                  "x<sub>5</sub>, x<sub>3</sub>, x<sub>7</sub>.")


def fig_butterfly_single():
    F = Fig("butterfly-single", 660, 214, "one butterfly of the decimation-in-time FFT with its four branch weights")
    xl, xr, yt, yb = 150, 400, 62, 150
    F.flow(xl, yt, xr, yt, "1", off=(0, -9), math=False)
    F.flow(xl, yt, xr, yb, "1", off=(8, -7), t=0.25, lt=0.8, math=False)
    F.flow(xl, yb, xr, yt, W("N", "k"), off=(10, 17), t=0.25, lt=0.8, c=ACC)
    F.flow(xl, yb, xr, yb, W("N", "k", neg=True), off=(0, 21), c=HI)
    for x, y in ((xl, yt), (xl, yb), (xr, yt), (xr, yb)):
        F.dot(x, y, 3.6)
    F.text(xl - 12, yt + 5, "A[k]", anchor="end", math=True, size=15)
    F.text(xl - 12, yb + 5, "B[k]", anchor="end", math=True, size=15)
    F.text(xr + 12, yt + 5, "X[k]", anchor="start", math=True, size=15)
    F.text(xr + 12, yb + 5, "X[k + N/2]", anchor="start", math=True, size=15)
    F.line(545, yt + 2, 545, yb - 2, c=MUTED, w=1, both=True)
    F.text(553, (yt + yb) / 2 - 4, "N/2 rows apart", anchor="start", size=11, c=MUTED)
    F.text(553, (yt + yb) / 2 + 10, "in the merged DFT", anchor="start", size=11, c=MUTED)
    F.text(xl - 12, yt - 22, "upper input", anchor="end", size=11, c=MUTED)
    F.text(xl - 12, yb + 26, "lower input", anchor="end", size=11, c=MUTED)
    return F.html("<strong>One butterfly = one pair of merging equations.</strong> The upper input A[k] reaches "
                  "both outputs with weight 1. The lower input B[k] reaches the upper output with weight "
                  "W<sub>N</sub><sup>k</sup> and the lower output with weight −W<sub>N</sub><sup>k</sup>: "
                  "X[k] = A[k] + W<sub>N</sub><sup>k</sup>B[k], X[k + N/2] = A[k] − W<sub>N</sub><sup>k</sup>B[k]. "
                  "The lecture's drawing puts W<sub>N</sub><sup>k</sup> on the B[k] rail and −1 on the last "
                  "branch; the four weights are the same.")


def fig_butterfly8():
    F = Fig("butterfly-8", 680, 384, "butterfly diagram of the length-8 decimation-in-time FFT")
    cx = [110, 270, 430, 590]
    ys = [58 + 34 * r for r in range(8)]
    order = [0, 4, 2, 6, 1, 5, 3, 7]
    for s in range(1, 4):
        Ln = 2 ** s
        F.text((cx[s - 1] + cx[s]) / 2, 22, f"Stage {s} → length {Ln}", size=12, bold=True)
        for base in range(0, 8, Ln):
            for k in range(Ln // 2):
                t, b = base + k, base + k + Ln // 2
                F.line(cx[s - 1], ys[t], cx[s] - 5, ys[t], w=1.2, op=0.8, arrow=True)
                F.line(cx[s - 1], ys[t], cx[s] - 5, ys[b] - 1.2, w=1.2, op=0.8, arrow=True)
                F.line(cx[s - 1], ys[b], cx[s] - 5, ys[t] + 1.2, c=ACC, w=1.4, arrow=True)
                F.line(cx[s - 1], ys[b], cx[s] - 5, ys[b], c=HI, w=1.4, arrow=True)
    for s in range(1, 4):
        Ln = 2 ** s
        for base in range(0, 8, Ln):
            for k in range(Ln // 2):
                b = base + k + Ln // 2
                F.text(cx[s - 1] + 9, ys[b] - 7, W(Ln, k), anchor="start", c=ACC, size=12, math=True, halo=True)
    names1 = ["C[0]", "C[1]", "D[0]", "D[1]", "E[0]", "E[1]", "F[0]", "F[1]"]
    names2 = ["A[0]", "A[1]", "A[2]", "A[3]", "B[0]", "B[1]", "B[2]", "B[3]"]
    for r in range(8):
        for c in range(4):
            F.dot(cx[c], ys[r], 3.2)
        F.text(cx[0] - 12, ys[r] + 5, f"x[{order[r]}]", anchor="end", math=True, size=14)
        F.text(cx[3] + 12, ys[r] + 5, f"X[{r}]", anchor="start", math=True, size=14)
        F.text(cx[1] - 15, ys[r] - 7, names1[r], anchor="end", size=11, c=MUTED, math=True, halo=True)
        F.text(cx[2] - 15, ys[r] - 7, names2[r], anchor="end", size=11, c=MUTED, math=True, halo=True)
    yl = 340
    F.line(60, yl, 92, yl, w=1.2, op=0.8)
    F.text(98, yl + 4, "from the upper input: × 1", anchor="start", size=12)
    F.line(330, yl, 362, yl, c=ACC, w=1.6)
    F.text(368, yl + 4, "lower input → upper output: × W", anchor="start", size=12)
    F.text(98, yl + 26, "W: the label at each lower input", anchor="start", size=11, c=MUTED)
    F.line(330, yl + 22, 362, yl + 22, c=HI, w=1.6)
    F.text(368, yl + 26, "lower input → lower output: × (−W)", anchor="start", size=12)
    return F.html("<strong>Length-8 decimation-in-time FFT (Lecture 25, Figure 2).</strong> Inputs enter in the "
                  "order left by the even/odd splitting. Each stage has N/2 = 4 butterflies and doubles the DFT "
                  "length; a butterfly's two rows are half the merged length apart (1, 2, then 4 rows). The "
                  "twiddle factor's subscript is the length being merged <em>to</em>, its superscript is the "
                  "index k inside the two shorter DFTs. Three stages of N = 8 multiply-adds each: N log<sub>2</sub>N = 24.")


def partial_butterfly(name, label, stages, marks, caption, lengths=(4, 8, 16)):
    """Three columns of 16 nodes; stages[c] = butterflies (top, bottom) drawn from column c to c+1;
    marks = (column, from_row, to_row, text, t, (dx, dy)) names an edge of the stage leaving that column."""
    F = Fig(name, 660, 404, label)
    cx = [170, 330, 490]
    ys = [46 + 21 * r for r in range(16)]
    for c in range(3):
        G = lengths[c]
        F.text(cx[c], 22, f"length-{G} DFT" + ("s" if G < 16 else ""), size=12, bold=True, c=MUTED)
        for g in range(0, 16, G):
            F.rect(cx[c] - 11, ys[g] - 9, 22, ys[g + G - 1] - ys[g] + 18, fill=ACC, stroke=None, rx=8, fop=0.10)
    for c, bfs in enumerate(stages):
        for (t, b) in bfs:
            for (r0, r1) in ((t, t), (t, b), (b, t), (b, b)):
                dy = 0 if r0 == r1 else (1.2 if r1 < r0 else -1.2)
                F.line(cx[c], ys[r0], cx[c + 1] - 5, ys[r1] + dy, w=1.2, arrow=True)
    for c in range(3):
        G = lengths[c]
        for r in range(16):
            F.dot(cx[c], ys[r], 2.6)
            if c == 2:
                F.text(cx[c] + 14, ys[r] + 4, f"k = {r}" if r == 0 else f"{r}", anchor="start", size=10, c=MUTED)
            else:
                F.text(cx[c] - 21, ys[r] + 4, f"k = {r % G}" if r == 0 else f"{r % G}", anchor="end",
                       size=10, c=MUTED, halo=True)
    for (c, r0, r1, s, t, off) in marks:
        x = cx[c] + (cx[c + 1] - cx[c]) * t
        y = ys[r0] + (ys[r1] - ys[r0]) * t
        F.text(x + off[0], y + off[1], s, size=16, bold=True, c=ACC2, math=True, halo=True)
    F.text(330, 396, "the shaded groups are the separate DFTs held in each column; k counts inside a group",
           size=11, c=MUTED)
    return F.html(caption)


def fig_butterfly16_example():
    return partial_butterfly(
        "butterfly-16-example", "part of a length-16 decimation-in-time FFT with five unknown branch weights",
        stages=[[(2, 6), (11, 15)], [(4, 12), (7, 15)]],
        marks=[(0, 15, 15, "a", 0.5, (0, -7)), (1, 15, 15, "b", 0.5, (0, -7)), (0, 6, 2, "c", 0.78, (-2, -6)),
               (1, 4, 4, "d", 0.42, (0, -7)), (1, 12, 4, "e", 0.9, (-12, 6))],
        caption="<strong>Example 3: part of a length-16 DIT FFT (slide 14, redrawn).</strong> Only four butterflies "
                "are drawn. In the last stage the two rows of a butterfly are 8 apart, so that stage merges to "
                "length 16 and the middle column holds two length-8 DFTs; the stage before it merges to length 8 "
                "(rows 4 apart) from four length-4 DFTs. The small numbers are the index k inside each group.")


def fig_hw10_butterfly():
    return partial_butterfly(
        "hw10-butterfly", "the partial 16-point FFT diagram of homework 10 with branch weights a, b and c",
        stages=[[(0, 4), (10, 14)], [(0, 8), (6, 14)]],
        marks=[(1, 8, 8, "a", 0.5, (0, -7)), (1, 14, 6, "b", 0.68, (10, 6)), (0, 14, 10, "c", 0.72, (-2, 14))],
        caption="<strong>HW10 #1: part of a 16-point radix-2 DIT FFT (redrawn).</strong> The right-hand butterflies "
                "join rows 8 apart (0 with 8, 6 with 14): they merge two length-8 DFTs into the length-16 DFT. "
                "The left-hand butterflies join rows 4 apart (0 with 4, 10 with 14): they merge length-4 DFTs "
                "into length-8 DFTs. Rows are numbered 0 to 15 from the top, as in the official solution.")


# ------------------------------------------------------------------ Lecture 26: fast convolution
def fig_fastconv_pipeline():
    F = Fig("fastconv-pipeline", 680, 176, "the four steps of fast linear convolution with the FFT")

    def box(x, y, w, s, h=30):
        F.rect(x, y, w, h, fill=ACC, stroke=INK, sw=1.2, rx=4, fop=0.10)
        F.text(x + w / 2, y + h / 2 + 4.5, s, size=12)

    y1, y2 = 30, 96
    F.text(64, y1 + 13, "x[n]", anchor="end", math=True, size=14)
    F.text(64, y1 + 28, "length N", anchor="end", size=10, c=MUTED)
    F.text(64, y2 + 13, "h[n]", anchor="end", math=True, size=14)
    F.text(64, y2 + 28, "length L", anchor="end", size=10, c=MUTED)
    for y in (y1, y2):
        F.line(70, y + 15, 92, y + 15, arrow=True, w=1.3)
        box(96, y, 150, "zero-pad to length M")
        F.line(246, y + 15, 276, y + 15, arrow=True, w=1.3)
        box(280, y, 92, "M-point FFT")
    F.line(372, y1 + 15, 414, 73, arrow=True, w=1.3)
    F.line(372, y2 + 15, 414, 83, arrow=True, w=1.3)
    F.out.append(f'<circle cx="430" cy="78" r="14" fill="none" stroke="{INK}" stroke-width="1.4"/>')
    F.text(430, 83, "×", size=16)
    F.text(430, 52, "bin by bin", size=10, c=MUTED)
    F.line(444, 78, 470, 78, arrow=True, w=1.3)
    box(474, 63, 100, "inverse FFT")
    F.line(574, 78, 598, 78, arrow=True, w=1.3)
    F.text(604, 76, "x[n] ∗ h[n]", anchor="start", math=True, size=14)
    F.text(604, 92, "N + L − 1", anchor="start", size=10, c=MUTED)
    F.text(604, 104, "samples", anchor="start", size=10, c=MUTED)
    yc = 156
    F.text(171, yc, "① O(1)", size=12, c=ACC2, bold=True)
    F.text(326, yc, "② 2 · O(M log M)", size=12, c=ACC2, bold=True)
    F.text(430, yc, "③ O(M)", size=12, c=ACC2, bold=True)
    F.text(524, yc, "④ O(M log M)", size=12, c=ACC2, bold=True)
    return F.html("<strong>Fast linear convolution (Lecture 26, §2.1).</strong> Pad both sequences to a common "
                  "length M ≥ N + L − 1 (the next power of 2 for a radix-2 FFT), transform, multiply bin by bin, "
                  "transform back. The padding makes the circular convolution that the DFT product computes "
                  "equal to the linear one; the total cost is O(M log M) instead of O(N²).")


# ------------------------------------------------------------------ Lecture 27: filters
def fig_ideal_filters():
    F = Fig("ideal-filters", 680, 316, "ideal low-pass, high-pass, band-pass and band-stop frequency responses")
    pw, ph = 270, 70
    wc, wl, wu = 0.4, 0.3, 0.62          # in units of pi
    panels = [
        ("low-pass", [(-1, 0), (-wc, 0), (-wc, 1), (wc, 1), (wc, 0), (1, 0)], [(-wc, "−ω<tspan dy='3' style='font-size:9px'>c</tspan>"), (wc, "ω<tspan dy='3' style='font-size:9px'>c</tspan>")]),
        ("high-pass", [(-1, 1), (-wc, 1), (-wc, 0), (wc, 0), (wc, 1), (1, 1)], [(-wc, "−ω<tspan dy='3' style='font-size:9px'>c</tspan>"), (wc, "ω<tspan dy='3' style='font-size:9px'>c</tspan>")]),
        ("band-pass", [(-1, 0), (-wu, 0), (-wu, 1), (-wl, 1), (-wl, 0), (wl, 0), (wl, 1), (wu, 1), (wu, 0), (1, 0)],
         [(wl, "ω<tspan dy='3' style='font-size:9px'>l</tspan>"), (wu, "ω<tspan dy='3' style='font-size:9px'>u</tspan>"), (-wl, "−ω<tspan dy='3' style='font-size:9px'>l</tspan>"), (-wu, "−ω<tspan dy='3' style='font-size:9px'>u</tspan>")]),
        ("band-stop", [(-1, 1), (-wu, 1), (-wu, 0), (-wl, 0), (-wl, 1), (wl, 1), (wl, 0), (wu, 0), (wu, 1), (1, 1)],
         [(wl, "ω<tspan dy='3' style='font-size:9px'>l</tspan>"), (wu, "ω<tspan dy='3' style='font-size:9px'>u</tspan>"), (-wl, "−ω<tspan dy='3' style='font-size:9px'>l</tspan>"), (-wu, "−ω<tspan dy='3' style='font-size:9px'>u</tspan>")]),
    ]
    for i, (title, pts, ticks) in enumerate(panels):
        ox, oy = 50 + (i % 2) * 330, 44 + (i // 2) * 150
        X = lambda u: ox + (u + 1) / 2 * pw
        Y = lambda v: oy + ph - v * ph
        d = "M" + " L".join(f"{f(X(u))},{f(Y(v))}" for u, v in pts)
        F.path(d + f" L{f(X(1))},{f(Y(0))} L{f(X(-1))},{f(Y(0))} Z", c="none", w=0, fill=ACC, fop=0.16)
        F.line(X(-1) - 8, Y(0), X(1) + 12, Y(0), w=1, op=0.8, arrow=True)
        F.line(X(0), Y(0), X(0), Y(1) - 16, w=1, op=0.5)
        F.path(d, c=ACC, w=2.2)
        F.text(ox + pw / 2, oy - 22, title, size=13, bold=True)
        F.text(X(1) + 18, Y(0) + 4, "ω", anchor="start", math=True, size=13)
        F.text(X(-1) - 10, Y(1) + 4, "1", anchor="end", size=11, c=MUTED)
        for u, s in [(-1, "−π"), (0, "0"), (1, "π")] + ticks:
            F.line(X(u), Y(0) - 3, X(u), Y(0) + 3, w=1)
            F.text(X(u), Y(0) + 17, s, size=11, c=MUTED if s in ("−π", "0", "π") else INK, math=s not in ("−π", "0", "π"))
    return F.html("<strong>The four canonical ideal filters (Lecture 27, Figure 1).</strong> Each passes its "
                  "shaded band with gain 1 and removes everything else, with no transition in between. "
                  "High-pass = 1 − low-pass and band-stop = 1 − band-pass, so the right column is the left "
                  "column turned upside down. All four are real filters, so the responses are even in ω.")


def fig_ideal_lpf_sinc():
    F = Fig("ideal-lpf-sinc", 660, 232, "impulse response of the ideal low-pass filter with cutoff pi over 4")
    wc = PI / 4
    x0, y0, dx, sc = 330, 150, 16.0, 400.0
    F.line(30, y0, 632, y0, w=1, op=0.75)
    for n in range(-18, 19):
        h = wc / PI if n == 0 else math.sin(wc * n) / (PI * n)
        x, y = x0 + dx * n, y0 - sc * h
        c = HI if n < 0 else ACC
        F.line(x, y0, x, y, c=c, w=1.6)
        F.dot(x, y, 2.8, c)
    for n in (-16, -8, 0, 8, 16):
        F.line(x0 + dx * n, y0 + 28, x0 + dx * n, y0 + 32, w=1)
        F.text(x0 + dx * n, y0 + 45, f"{n}".replace("-", "−"), size=11, c=MUTED)
    F.text(646, y0 + 4, "n", math=True, size=13)
    F.text(18, y0 - 4, "⋯", size=14, c=MUTED)
    F.text(642, y0 - 14, "⋯", size=14, c=MUTED)
    F.text(x0 + 12, y0 - sc * 0.25 + 1, "h[0] = ω<tspan dy='3' style='font-size:9px'>c</tspan><tspan dy='-3'>/π = 1/4</tspan>", anchor="start", size=12)
    F.text(150, 96, "n &lt; 0: needs future inputs", size=12, c=HI)
    F.text(516, 96, "never ends: no finite sum, no LCCDE", size=12, c=ACC)
    return F.html("<strong>Impulse response of the ideal low-pass filter, ω<sub>c</sub> = π/4 (computed).</strong> "
                  "h[n] = sin(ω<sub>c</sub>n)/(πn) is zero at every multiple of π/ω<sub>c</sub> = 4 and decays only "
                  "like 1/n, in both directions: the red half makes the filter non-causal, the infinite length "
                  "makes it impossible to implement, and the slow decay makes Σ|h[n]| diverge.")


def truncated_lpf(wc, M):
    n = np.arange(M)
    m = n - (M - 1) / 2
    return np.where(m == 0, wc / PI, np.sin(wc * m) / (PI * np.where(m == 0, 1, m)))


def lpf_specs(h, grid=1 << 15):
    """Measured ripple, attenuation and band edges of a low-pass FIR filter (rad/sample)."""
    Hm = np.abs(np.fft.rfft(h, 2 * grid))
    w = np.arange(grid + 1) * PI / grid
    dH = np.diff(Hm)
    ext = np.where(np.sign(dH[1:]) != np.sign(dH[:-1]))[0] + 1           # local extrema
    first_null = ext[np.argmax(Hm[ext] < 0.02)]
    As = Hm[first_null:].max()                                           # largest stopband lobe
    dp = np.abs(Hm[:first_null] - 1)[ext[ext < first_null]].max()        # largest passband ripple
    below = np.where(Hm[:first_null] < 1 - dp)[0]
    wp = w[below[0] - 1]                                                 # leaves the ripple band
    ws = w[np.where(Hm <= As)[0][0]]                                     # first reaches the stopband level
    return dict(dp=dp, As=As, wp=wp, ws=ws, w=w, H=Hm)


SPEC_FILTER = dict(wc=7 * PI / 16, M=17)      # the filter drawn in filter-specs


def fig_filter_specs():
    F = Fig("filter-specs", 680, 346, "magnitude response in dB of a practical low-pass filter with its specifications")
    h = truncated_lpf(**SPEC_FILTER)
    sp = lpf_specs(h)
    x0, x1, yt, yb, dbt, dbb = 70, 620, 30, 280, 5.0, -45.0
    X = lambda w: x0 + w / PI * (x1 - x0)
    Y = lambda d: yt + (dbt - d) / (dbt - dbb) * (yb - yt)
    F.rect(x0, yt, x1 - x0, yb - yt, stroke=INK, sw=1)
    for d in (0, -10, -20, -30, -40):
        F.line(x0, Y(d), x1, Y(d), c=MUTED, w=0.6, dash="3 3", op=0.6)
        F.text(x0 - 8, Y(d) + 4, f"{d}".replace("-", "−"), anchor="end", size=11, c=MUTED)
    for k, s in enumerate(["0", "π/8", "π/4", "3π/8", "π/2", "5π/8", "3π/4", "7π/8", "π"]):
        F.line(X(k * PI / 8), yb, X(k * PI / 8), yb + 4, w=1)
        F.text(X(k * PI / 8), yb + 18, s, size=11, c=MUTED)
    F.text(X(PI / 2), yb + 38, "ω (rad/sample)", size=12)
    F.vtext(22, (yt + yb) / 2, "|H<tspan dy='3' style='font-size:9px'>d</tspan><tspan dy='-3'>(ω)| in dB</tspan>", size=12)
    step = 24
    dB = 20 * np.log10(np.maximum(sp["H"], 1e-6))
    pts = [f"{f(X(sp['w'][i]))},{f(Y(max(dB[i], dbb)))}" for i in range(0, len(dB), step)]
    F.path("M" + " L".join(pts), c=ACC, w=1.8)
    As_db, hi_db, lo_db = 20 * math.log10(sp["As"]), 20 * math.log10(1 + sp["dp"]), 20 * math.log10(1 - sp["dp"])
    F.line(x0, Y(hi_db), X(sp["wp"]) + 60, Y(hi_db), c=HI, w=1, dash="5 3")
    F.line(x0, Y(lo_db), X(sp["wp"]) + 60, Y(lo_db), c=HI, w=1, dash="5 3")
    F.text(X(sp["wp"]) + 66, Y(0) + 4, "passband ripple: the gain stays in 1 ± δ", anchor="start", size=11, c=HI, halo=True)
    F.line(X(sp["ws"]) - 40, Y(As_db), x1, Y(As_db), c=HI, w=1, dash="5 3")
    F.text(x1 - 6, Y(As_db) - 6, f"stopband attenuation ≈ {As_db:.0f} dB".replace("-", "−"), anchor="end", size=11, c=HI, halo=True)
    for wv in (sp["wp"], sp["ws"]):
        F.line(X(wv), yt, X(wv), yb, c=ACC2, w=1, dash="5 3")
    ya = Y(-12)
    F.line(x0 + 3, ya, X(sp["wp"]) - 3, ya, w=1, both=True)
    F.text((x0 + X(sp["wp"])) / 2, ya - 6, "passband", size=12, bold=True)
    F.line(X(sp["ws"]) + 3, ya, x1 - 3, ya, w=1, both=True)
    F.text((X(sp["ws"]) + x1) / 2, ya - 6, "stopband", size=12, bold=True)
    yt2 = Y(-33)
    F.line(X(sp["wp"]) + 2, yt2, X(sp["ws"]) - 2, yt2, w=1, both=True)
    F.text((X(sp["wp"]) + X(sp["ws"])) / 2, yt2 + 16, "transition", size=11, bold=True, halo=True)
    F.text((X(sp["wp"]) + X(sp["ws"])) / 2, yt2 + 29, "band", size=11, bold=True, halo=True)
    F.text(x1 + 8, Y(-20) + 4, "1/10", anchor="start", size=11, c=ACC2)
    F.text(x1 + 8, Y(-40) + 4, "1/100", anchor="start", size=11, c=ACC2)
    F.text(x1 + 8, Y(0) + 4, "1", anchor="start", size=11, c=ACC2)
    mn = lambda v, fmt: format(v, fmt).replace("-", "−")
    return F.html(
        "<strong>Specifications of a practical low-pass filter (after Lecture 27, Figure 2; computed).</strong> "
        f"The filter is the ideal low-pass response with ω<sub>c</sub> = 7π/16, shifted and cut to {SPEC_FILTER['M']} samples. "
        f"Measured: passband ripple δ = {sp['dp']:.3f} (the gain stays between {mn(lo_db, '+.2f')} and {mn(hi_db, '+.2f')} dB) up to "
        f"ω<sub>p</sub> = {sp['wp'] / PI:.3f}π; largest stopband lobe {sp['As']:.3f} = {mn(As_db, '.1f')} dB, reached from "
        f"ω<sub>s</sub> = {sp['ws'] / PI:.3f}π on; transition bandwidth ω<sub>s</sub> − ω<sub>p</sub> = "
        f"{(sp['ws'] - sp['wp']) / PI:.3f}π. Right-hand labels: the same gains on a linear scale.")


def ladder_df1(F, ox, oy, cs, bs, dx=92, dy=56, title=None, gmath=True):
    """Direct form I flow graph. cs = gains c0..c_{M-1}, bs = gains b1..bK; None = no branch."""
    xa, xb, xc, xd = ox, ox + dx, ox + 2 * dx, ox + 3 * dx
    F.line(xa - 46, oy, xa, oy, w=1.6)
    F.text(xa - 50, oy + 5, "x[n]", anchor="end", math=True, size=15)
    F.flow(xa, oy, xb, oy, cs[0], off=(0, -9), math=gmath)
    F.flow(xb, oy, xc, oy)
    F.flow(xc, oy, xd, oy, "1", off=(0, -9), math=False)
    F.line(xd, oy, xd + 40, oy, w=1.6, arrow=True)
    F.text(xd + 46, oy + 5, "y[n]", anchor="start", math=True, size=15)
    F.text((xb + xc) / 2, oy - 12, "v[n]", math=True, size=13, c=MUTED)
    nx = max([i for i in range(1, len(cs)) if cs[i] is not None], default=0)
    for i in range(1, len(cs)):
        y = oy + i * dy
        F.flow(xa, y - dy, xa, y, ZINV, off=(-9, 4), anchor="end")
        if cs[i] is not None:
            F.flow(xa, y, xb, y, cs[i], off=(0, -9), math=gmath)
            F.dot(xb, y)
        if i <= nx:
            F.flow(xb, y, xb, y - dy)
        F.dot(xa, y)
    ny = max([i for i in range(1, len(bs) + 1) if bs[i - 1] is not None], default=0)
    for i in range(1, len(bs) + 1):
        y = oy + i * dy
        F.flow(xd, y - dy, xd, y, ZINV, off=(9, 4), anchor="start")
        if bs[i - 1] is not None:
            F.flow(xd, y, xc, y, bs[i - 1], off=(0, -9), math=gmath)
            F.dot(xc, y)
        if i <= ny:
            F.flow(xc, y, xc, y - dy)
        F.dot(xd, y)
    for x in (xa, xb, xc, xd):
        F.dot(x, oy)
    if title:
        F.text((xa + xd) / 2, oy - 34, title, size=13, bold=True)


def ladder_df2(F, ox, oy, cs, bs, dx=92, dy=56, title=None, gmath=True):
    """Direct form II flow graph: one shared delay line carrying v[n]."""
    xl, xm, xr = ox, ox + dx, ox + 2 * dx
    F.line(xl - 46, oy, xl, oy, w=1.6)
    F.text(xl - 50, oy + 5, "x[n]", anchor="end", math=True, size=15)
    F.flow(xl, oy, xm, oy, "1", off=(0, -9), math=False)
    F.flow(xm, oy, xr, oy, cs[0], off=(0, -9), math=gmath)
    F.line(xr, oy, xr + 40, oy, w=1.6, arrow=True)
    F.text(xr + 46, oy + 5, "y[n]", anchor="start", math=True, size=15)
    F.text(xm, oy - 12, "v[n]", math=True, size=13, c=ACC2)
    depth = max(len(bs), len(cs) - 1)
    nb = max([i for i in range(1, len(bs) + 1) if bs[i - 1] is not None], default=0)
    nc = max([i for i in range(1, len(cs)) if cs[i] is not None], default=0)
    for i in range(1, depth + 1):
        y = oy + i * dy
        F.flow(xm, y - dy, xm, y, ZINV, off=(9, 4), anchor="start", c=ACC2)
        if i <= len(bs) and bs[i - 1] is not None:
            F.flow(xm, y, xl, y, bs[i - 1], off=(0, -9), math=gmath)
            F.dot(xl, y)
        if i <= nb:
            F.flow(xl, y, xl, y - dy)
        if i < len(cs) and cs[i] is not None:
            F.flow(xm, y, xr, y, cs[i], off=(0, -9), math=gmath)
            F.dot(xr, y)
        if i <= nc:
            F.flow(xr, y, xr, y - dy)
        F.dot(xm, y, c=ACC2)
    for x in (xl, xr):
        F.dot(x, oy)
    F.dot(xm, oy, c=ACC2)
    if title:
        F.text(xm, oy - 34, title, size=13, bold=True)


def csub(sym, i):
    return f'{sym}<tspan dy="3" style="font-size:9px">{i}</tspan>'


def fig_df1_general():
    F = Fig("df1-general", 660, 262, "direct form I flow graph with three feedback and four input coefficients")
    ladder_df1(F, 190, 52, [csub("c", i) for i in range(4)], [csub("b", i) for i in range(1, 4)])
    F.text(300, 252, "input half: v[n] from x", size=11, c=MUTED, anchor="end")
    F.text(356, 252, "feedback half: y[n] from v and past y", size=11, c=MUTED, anchor="start")
    return F.html("<strong>Direct form I (Lecture 27, Figure 3).</strong> y[n] = b<sub>1</sub>y[n−1] + b<sub>2</sub>y[n−2] "
                  "+ b<sub>3</sub>y[n−3] + c<sub>0</sub>x[n] + c<sub>1</sub>x[n−1] + c<sub>2</sub>x[n−2] + c<sub>3</sub>x[n−3]. "
                  "An arrowhead with a label multiplies by that gain, z<sup>−1</sup> delays by one sample, and "
                  "branches that meet at a dot are added. Left: a delay line on x[n]; right: a delay line on y[n]. "
                  "Seven multiplications, six additions, six delays.")


def fig_df2_general():
    F = Fig("df2-general", 660, 262, "direct form II flow graph of the same difference equation with three delays")
    ladder_df2(F, 238, 52, [csub("c", i) for i in range(4)], [csub("b", i) for i in range(1, 4)])
    F.text(200, 252, "feedback first: v[n] from x and past v", size=11, c=MUTED, anchor="middle")
    F.text(470, 252, "then the input coefficients on v", size=11, c=MUTED, anchor="middle")
    return F.html("<strong>Direct form II (Lecture 27, Figure 4).</strong> The same system with the two halves in the "
                  "opposite order, so that both use one delay line (highlighted), which carries the intermediate "
                  "signal v[n]: v[n] = x[n] + b<sub>1</sub>v[n−1] + b<sub>2</sub>v[n−2] + b<sub>3</sub>v[n−3], "
                  "y[n] = c<sub>0</sub>v[n] + c<sub>1</sub>v[n−1] + c<sub>2</sub>v[n−2] + c<sub>3</sub>v[n−3]. "
                  "Feedback gains b<sub>i</sub> are on the left, input gains c<sub>j</sub> on the right. "
                  "Seven multiplications, six additions, only three delays.")


def fig_df_example2():
    F = Fig("df-example2", 680, 262, "direct form I and II flow graphs of y[n] = y[n-2] - 2y[n-3] + 3x[n] - x[n-1] + 2x[n-2]")
    cs, bs = ["3", "−1", "2"], [None, "1", "−2"]
    for fn, ox, dx, title in ((ladder_df1, 80, 68, "Direct form I"), (ladder_df2, 458, 68, "Direct form II")):
        fn(F, ox, 62, cs, bs, dx=dx, title=title, gmath=False)
    return F.html("<strong>Example 2 (slides 12–13): y[n] = y[n−2] − 2y[n−3] + 3x[n] − x[n−1] + 2x[n−2].</strong> "
                  "c<sub>0</sub> = 3, c<sub>1</sub> = −1, c<sub>2</sub> = 2; b<sub>1</sub> = 0 (no branch), b<sub>2</sub> = 1, "
                  "b<sub>3</sub> = −2. Direct form I needs 2 + 3 = 5 delays, direct form II max(2, 3) = 3. "
                  "Drawn here from the Lecture 27 rules; the lecture had not yet worked this example by Nov 9.")


FIGS = [fig_stft_windows, fig_stft_tradeoff, fig_split_tree, fig_butterfly_single, fig_butterfly8,
        fig_butterfly16_example, fig_hw10_butterfly, fig_fastconv_pipeline, fig_ideal_filters,
        fig_ideal_lpf_sinc, fig_filter_specs, fig_df1_general, fig_df2_general, fig_df_example2]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for fn in FIGS:
        name, html = fn()
        assert "\n" not in html.rstrip("\n"), name
        with open(os.path.join(out, name + ".html"), "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"{name:24s} {len(html) / 1024:6.1f} kB")


if __name__ == "__main__":
    main()
