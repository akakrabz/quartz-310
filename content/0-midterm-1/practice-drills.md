---
title: "Practice drills — randomized and autograded"
description: "Seven autograded Midterm 1 drills with fresh random variants, hints after a wrong attempt, worked solutions and exam-style scoring: convolution, system properties, partial fractions, z-transforms and ROCs, stability from the ROC, unbounded outputs, and True/False."
tags: [midterm-1, exam, demo]
---

*Midterm 1 · interactive practice in the spirit of PrairieLearn / TheorieLearn · pairs with [[0-midterm-1/index|the survival guide]], [[problems/index|the exam problem families]] and [[0-midterm-1/past-exams/index|the past exams]]*

> [!abstract] In one breath
> Pick a drill, press **New variant** for fresh numbers, answer, **Submit**. A wrong answer gets a hint, a second wrong answer a sharper one, and **Show worked solution** walks through the method the exam keys use. The strip at the top keeps score like the exam: only your **first** submission of a variant earns points, and True/False is +2 / −1 / 0. Everything runs in your browser and nothing is saved — reloading starts from zero.

<div class="ece-demo">
<iframe src="/static/demos/drills/" title="ECE 310 practice drills — randomized and autograded" loading="lazy" style="height:900px"></iframe>
</div>

[Open the drills in their own tab](/static/demos/drills/) — roomier, and the better choice on a phone (the tabs become a drop-down). Each drill also has its own address: [convolution](/static/demos/drills/#conv), [system properties](/static/demos/drills/#props), [PFE](/static/demos/drills/#pfe), [z-transform & ROC](/static/demos/drills/#zroc), [ROC → stable/causal](/static/demos/drills/#rocsc), [unbounded outputs](/static/demos/drills/#poles), [True/False](/static/demos/drills/#tf).

## How to use it on exam day

> [!recipe] A 45-minute warm-up
> 1. **True/False** — one pass through all 42 statements, skipping whenever you would guess (that is what the −1 is for). Reread the reason of every miss.
> 2. **System properties** — ten systems, first try only. The one-line reasons are the arguments you write on the exam.
> 3. **Convolution** — three variants, writing the start index down *before* computing any sample.
> 4. **PFE & inverse z** and **ROC → stable/causal** — until two in a row are fully right, including a two-sided ROC.
> 5. **Unbounded outputs** — three variants; say the reason out loud before submitting.
> 6. **z-transform & ROC** — until you stop losing the "z = 0 / z = ∞" point.

Answers are checked tolerantly: `9/4`, `-5/4`, `2.25`, `−1.25` (either minus sign), spaces and braces are all accepted. For lists, use commas (`2, -1, 0, 5`) or spaces (`{2 -1 0 5}`).

## The drills

### 1 · Finite-length convolution

You get $x[n]$ (3–5 samples, entries $-3,\dots,3$) and $h[n]$ (2–3 samples), each written the exam way with an arrow under the $n=0$ sample — the arrow can sit anywhere, so either sequence may start at a negative index (an index table is shown too). Enter $y[n] = x[n]*h[n]$ from its first to its last non-zero sample, plus the index where it starts. Points: 6 for the samples, 2 for the start index.

> [!key] Bookkeeping that decides half the points
> First index of $y$ = first index of $x$ + first index of $h$; length $L_x + L_h - 1$; first sample $x_{\text{first}}\,h_{\text{first}}$, last sample $x_{\text{last}}\,h_{\text{last}}$ — two free checks before any real work.

The worked solution shows the shift-and-add table (one row per input sample: a scaled, shifted copy of $h$) and the same numbers as the matrix product $y = Hx$ that the exam keys write out.

> [!trap] The keys slip here too
> The SP2025 #4(a) key boxes a wrong answer although its own matrix is right — see [[0-toolkit/05-errata|the errata page]]. Trust the bookkeeping rule (and the sum check $\sum y = \sum x\cdot\sum h$), not a copied box.

Exam record: 7/7 past exams ([[0-midterm-1/past-exams/fall-2025|FA2025 #3a]], [[0-midterm-1/past-exams/spring-2025|SP2025 #4a]], [[0-midterm-1/past-exams/spring-2021|SP2021 #2]], [[0-midterm-1/past-exams/fall-2019|FA2019 #4]], …). Recipe: [[problems/finite-length-convolution|finite-length convolution]]. Theory: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[concepts/convolution|convolution]]. For the sliding picture, use [[demos/convolution-explorer|the convolution explorer]].

### 2 · System properties

A deck of **45 systems**: every row of the seven past-exam property tables, the clipping and windowing systems of HW1 #5–6, the three systems of HW2 #1, and the Lecture 3 examples. Tick Linear / Time-invariant / Causal / BIBO stable; each box is worth one point, as on the exam (three systems × four boxes = 12 points). Every box comes back with a one-line reason. The deck runs through all 45 before repeating.

> [!trap] The ones people miss
> $y[n] = \dfrac{x[n]}{\lvert n\rvert + 1}$ **is** stable (the gain never exceeds 1), but $y[n] = \ln\lvert x[n]\rvert$ is **not** ($x[n] = 0$ is a bounded input); $y[n] = x[n]/x[2]$ is No on all four; $x[n]*u[n+1]$ is non-causal *and* unstable; anything with $x[0]$, $x[3]$ or $x[\lvert n\rvert]$ fails time-invariance **and** causality.

The answers are the official keys (checked numerically by the scripts behind [[0-midterm-1/system-property-bank|the system-property bank]], which gives every system with its proof). Recipe: [[problems/classifying-system-properties|classifying system properties]]. Theory: [[1-signals-and-systems/03-system-properties|Lecture 3]], [[concepts/linearity|linearity]], [[concepts/time-invariance|time-invariance]], [[concepts/causality|causality]], [[concepts/bibo-stability|BIBO stability]].

### 3 · Partial fractions and the inverse z-transform

$$
H(z) = \frac{b_0 + b_1 z^{-1}}{(1 - p_1 z^{-1})(1 - p_2 z^{-1})}
$$

with two distinct poles from $\{\pm\tfrac14, \pm\tfrac13, \pm\tfrac12, \pm\tfrac23, \pm\tfrac32, \pm 2, \pm 3\}$. **(a)** Find $A_1, A_2$ in $H(z) = \dfrac{A_1}{1-p_1z^{-1}} + \dfrac{A_2}{1-p_2z^{-1}}$ (2 + 2 points, exact fractions). **(b)** For the stated ROC — causal, anti-causal, or the annulus between the poles — pick $h[n]$ from four options (3 points). The wrong options are the classic mistakes: the answer for a different ROC, the two sides swapped in the annulus, a left-sided term without its minus sign, $u[-n]$ instead of $u[-n-1]$, residues attached to the wrong poles. **(c)** Is that system BIBO stable? (1 point).

> [!key] Cover-up, pairing, stability
> $A_k = \bigl[(1 - p_k z^{-1})H(z)\bigr]_{z = p_k}$, and $A_1 + A_2 = b_0$ is a free check. A pole inside the ROC's inner edge gives $A\,p^n u[n]$; a pole outside its outer edge gives $-A\,p^n u[-n-1]$. Stable $\iff$ the ROC contains $\lvert z\rvert = 1$.

Checking a hand computation takes a few lines of Python — here with FA2025 #7:

```python
from scipy.signal import residuez
# FA2025 #7:  H(z) = (1 - z^-1) / ((1 + 2 z^-1)(1 + (2/3) z^-1))
b = [1, -1]
a = [1, 8/3, 4/3]                     # (1 + 2z^-1)(1 + (2/3)z^-1) multiplied out
r, p, k = residuez(b, a)
for rr, pp in zip(r, p):
    print(f"pole {pp.real:+.4f}   residue A = {rr.real:+.4f}")
print("direct term:", k)
```

```text
pole -0.6667   residue A = -1.2500
pole -2.0000   residue A = +2.2500
direct term: []
```

So $A = \tfrac94$ at $z=-2$ and $A = -\tfrac54$ at $z = -\tfrac23$; the stable ROC $\tfrac23 < \lvert z\rvert < 2$ gives $h[n] = -\tfrac94(-2)^n u[-n-1] - \tfrac54\left(-\tfrac23\right)^n u[n]$, exactly the FA2025 key.

Exam record: 7/7 past exams ask for an inverse transform, all possible ROCs, or both ([[0-midterm-1/past-exams/fall-2025|FA2025 #7]], [[0-midterm-1/past-exams/spring-2025|SP2025 #8]], [[0-midterm-1/past-exams/fall-2019|FA2019 #7]], …). Recipe: [[problems/all-possible-rocs|inverse z, PFE and all possible ROCs]]; the anti-causal half as a recursion: [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]]. Theory: [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[concepts/partial-fraction-expansion|partial-fraction expansion]], [[concepts/inverse-z-transform|inverse z-transform]].

### 4 · z-transform and ROC of a signal

Five signal families, as on the exams: a shifted right-sided exponential $A\,a^n u[n-k]$ (the shift $k$ can be negative), a left-sided $C\,a^n u[-n-1]$, a left-sided sequence that stops at a positive index, $C\,a^n u[-n+k]$ (the SP2025 #5b type), a right-sided plus a left-sided term (whose ROC is sometimes **empty**), and a short finite sequence with the arrow. **(a)** Choose the ROC's shape from a menu that distinguishes $\lvert z\rvert > r$ from $r < \lvert z\rvert < \infty$ and $\lvert z\rvert < r$ from $0 < \lvert z\rvert < r$ (the keys do: FA2025 #5a is "$1 < \lvert z\rvert < \infty$", SP2025 #5b is "$0 < \lvert z\rvert < 3$"), and type the radii — 3 points, 2 if only the $z = 0$ / $z = \infty$ part is off. **(b)** Pick $X(z)$ among four options built from real mistakes: a missing factor $a^k$, the shift in the wrong direction, the pole at $1/a$ instead of $a$, the dropped minus sign of the left-sided pair, an off-by-one power, or "does not exist" when the ROC is not actually empty — 3 points.

> [!key] The pairs and the two special points
> $a^n u[n] \leftrightarrow \dfrac{1}{1 - a z^{-1}}$, ROC $\lvert z\rvert > \lvert a\rvert$; $\ -a^n u[-n-1] \leftrightarrow \dfrac{1}{1 - a z^{-1}}$, ROC $\lvert z\rvert < \lvert a\rvert$; $\ x[n-k] \leftrightarrow z^{-k}X(z)$. Samples at $n > 0$ exclude $z = 0$; samples at $n < 0$ exclude $z = \infty$.

Exam record: 6/7 past exams ([[0-midterm-1/past-exams/fall-2025|FA2025 #5]], [[0-midterm-1/past-exams/spring-2025|SP2025 #5]], [[0-midterm-1/past-exams/fall-2024|FA2024 #5]], [[0-midterm-1/past-exams/fall-2023|FA2023 #5]], [[0-midterm-1/past-exams/spring-2021|SP2021 #4]], [[0-midterm-1/past-exams/fall-2019|FA2019 #5]]). Recipe: [[problems/z-transform-with-roc|z-transform with ROC]]. Theory: [[2-z-transform/06-the-z-transform|Lecture 6]], [[2-z-transform/07-z-transform-properties|Lecture 7]], [[concepts/z-transform-pairs|z-transform pairs]], [[concepts/region-of-convergence|ROC]], [[concepts/sided-sequences|sided sequences]].

### 5 · Stability and causality from the ROC

$H(z)$ has two to four poles — real ones, sometimes a pair $\pm jr$ hidden in a factor $(1 + r^2 z^{-2})$ — and often a zero, which has nothing to do with the ROC (a deliberate distractor). You are told one fact: *the system is causal*, *BIBO stable*, or *$h[n]$ is left-sided / right-sided / two-sided*. **(a)** Pick the ROC among all the rings the pole circles allow (2 points), then say **(b)** stable? and **(c)** causal? (1 point each). The worked solution tabulates every possible ROC with its sidedness and stability — the "all possible ROCs" question of [[0-midterm-1/past-exams/fall-2019|FA2019 #7]].

> [!key] Read everything off the ring
> Causal (for $H$ written in powers of $z^{-1}$) $\iff$ ROC outside the outermost pole. Left-sided $\iff$ inside the innermost pole. Two-sided $\iff$ a ring between two poles. BIBO stable $\iff$ the ring contains $\lvert z\rvert = 1$. So "causal **and** stable" $\iff$ every pole inside the unit circle.

Recipe: [[problems/all-possible-rocs|all possible ROCs]], [[problems/parameters-for-stability|parameters for stability]]. Theory: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]], [[concepts/poles-and-zeros|poles and zeros]], [[concepts/bibo-stability|BIBO stability]], [[concepts/causality|causality]].

### 6 · Unbounded outputs: pole matching

A **causal** $H(z)$ with poles on the unit circle — at $1$, $-1$, $\pm j$, $e^{\pm j\pi/4}$, $e^{\pm j\pi/3}$, $e^{\pm j2\pi/3}$, or the FA2025 trap $e^{j2/3}$ — sometimes with a pole inside, sometimes with one **outside** the unit circle, sometimes with a zero. Five or six bounded inputs follow ($u[n]$, $(-1)^n u[n]$, $j^n u[n]$, $e^{j\omega n}u[n]$, $\cos(\omega n)u[n]$, $\sin(\omega n)u[n]$, $(2/3)^n u[n]$, $\delta[n] - p\,\delta[n-1]$, $a^n u[n] - p\,a^{n-1}u[n-1]$); tick the ones whose output is unbounded. One point per input, like FA2025 #8 and SP2025 #6. Every input comes back with its reason: which poles meet, which zero cancels what.

> [!key] The whole rule
> $Y(z) = H(z)X(z)$. After cancelling common factors, $y[n]$ is unbounded $\iff$ $Y$ has a pole **outside** the unit circle or a **repeated** pole **on** it. So: an input pole landing on one of $H$'s unit-circle poles resonates (growth like $n$); an input whose zero sits exactly on $H$'s outside pole rescues the output (FA2025 #8a ii and v).

> [!trap] $e^{j2/3}$ is not $e^{j2\pi/3}$
> In [[0-midterm-1/past-exams/fall-2025|FA2025 #8b]] the pole is $e^{j2/3}$ — angle $2/3$ rad $\approx 38^\circ$, not $120^\circ$ — so $\cos(\tfrac{2\pi}{3}n)u[n]$ gives a **bounded** output (key: False). The drill plants this trap regularly.

The same check in Python, on FA2025 #8b:

```python
import numpy as np
from scipy.signal import lfilter
# FA2025 #8b: causal H(z) = 1 / ((1 - (3/4)z^-1)(1 - j z^-1)(1 - e^{j2/3} z^-1))
a = np.poly([0.75, 1j, np.exp(2j / 3)])
n = np.arange(4000)
inputs = {"j^n u[n]": 1j ** n, "sin(pi n/2) u[n]": np.sin(np.pi * n / 2),
          "cos(2 pi n/3) u[n]": np.cos(2 * np.pi * n / 3)}
for name, x in inputs.items():
    y = lfilter([1], a, x.astype(complex))
    print(f"{name:19s} max|y|, n < 1000: {np.abs(y[:1000]).max():7.1f}   n < 4000: {np.abs(y).max():7.1f}")
```

```text
j^n u[n]            max|y|, n < 1000:   917.2   n < 4000:  3665.6
sin(pi n/2) u[n]    max|y|, n < 1000:   458.8   n < 4000:  1832.3
cos(2 pi n/3) u[n]  max|y|, n < 1000:     2.6   n < 4000:     2.6
```

Four times the length, four times the peak: linear growth for the two resonant inputs, a flat bound for the trap input.

Exam record: 7/7 past exams ([[0-midterm-1/past-exams/fall-2025|FA2025 #8]], [[0-midterm-1/past-exams/spring-2025|SP2025 #6]], [[0-midterm-1/past-exams/spring-2021|SP2021 #5]], …). Recipe: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]]. Theory: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]], [[concepts/marginal-stability|marginal stability]], [[concepts/pole-zero-cancellation|pole-zero cancellation]].

### 7 · True/False rapid fire

All **42** True/False statements from the seven past exams (the two DTFT statements of SP2023 left out), one at a time, with the official answer and a one-line reason after you commit. Scoring is the exam's: **+2** right, **−1** wrong, **0** skipped — so the right move on a coin-flip is Skip. Each statement is answered once; the deck runs through all 42 before reshuffling. Keyboard: `T`, `F`, `S`, then `N` for the next one.

> [!tip] Where the points go
> Most of the 42 turn on four facts: LTI systems are the only ones $h[n]$ describes; BIBO stable $\iff \sum\lvert h[n]\rvert < \infty$ (bounded $h$ is not enough, FIR is always enough); stable $\iff$ the ROC contains the unit circle; poles can cancel (in sums, cascades, and against input zeros). One statement, FA2025 #1(d), is keyed True under the reading "left-sided = extends to $-\infty$" — $\delta[n]$ is the pedantic exception.

The full list with longer explanations, grouped by topic: [[0-midterm-1/true-false-bank|True/False bank]]. Background: [[concepts/lti-system|LTI systems]], [[concepts/bibo-stability|BIBO stability]], [[concepts/pole-zero-cancellation|pole-zero cancellation]].

## Scoring

| drill | points per variant | partial credit |
|---|---|---|
| Convolution | 8 | samples 6, start index 2 |
| System properties | 4 | 1 per box, no penalty |
| PFE & inverse $z$ | 8 | $A_1$ 2, $A_2$ 2, $h[n]$ 3, stability 1 |
| z-transform & ROC | 6 | ROC 3 (2 for a $0$/$\infty$ slip, 1 for the right shape with a wrong radius), $X(z)$ 3 |
| ROC → stable / causal | 4 | ROC 2, stable 1, causal 1 |
| Unbounded outputs | 5–6 | 1 per input |
| True/False | 2 | +2 right, −1 wrong, 0 skipped |

"Correct" counts variants that were fully right on the first submission. Opening the worked solution before submitting scores that variant as a blank. The strip shows the running total and, underneath, the current drill.

## How the drills were checked

Every generator was run over 600 random seeds in Node (about 47 000 checks): convolution outputs against the direct sum $\sum_k x[k]\,h[n-k]$; every PFE by recombining $A_1/(1-p_1z^{-1}) + A_2/(1-p_2z^{-1})$ exactly and by summing the chosen $h[n]$ against $H(z)$ inside the ROC (no distractor may pass); every ROC by probing where the actual series $\sum x[n]z^{-n}$ converges, including $z = 0$ and $z = \infty$; stability and causality from a numerically built $h[n]$; unbounded outputs by simulating $y = h * x$. A sample of variants was re-checked independently in Python — `np.convolve`, `scipy.signal.residuez`, partial sums, and, for the pole drill, an exact simulation in rational arithmetic (so a cancelled unstable pole stays cancelled). The property and True/False answers were compared line by line with the verified keys, the test suite was confirmed to catch deliberately planted bugs, and a headless browser clicked through every drill (wrong answer, right answer, worked solution) in light and dark mode and at phone width.

## Related

[[0-midterm-1/true-false-bank|True/False bank]] · [[0-midterm-1/system-property-bank|System-property bank]] · [[0-midterm-1/cheat-sheet|Cheat sheet]] · [[problems/index|Exam problem families]] · [[demos/index|All demos]] · [[demos/pole-zero-and-roc-explorer|Pole-zero and ROC explorer]]

### Sources for this page

Past Midterm 1 exams and keys FA2025, SP2025, FA2024, FA2023, SP2023, SP2021, FA2019 (True/False statements, property tables, convolution, z-transform, PFE and pole-matching problems, grading rules); HW1 #5–6 and HW2 #1 with official solutions; Lecture 3 slides and notes (property examples); Lecture 6–8 notes (pairs, properties, cover-up); Lecture 11 notes (stability and causality from the ROC). Answer keys as verified in `verify/exams/`; drill tests in `verify/drills/`.
