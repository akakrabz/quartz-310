---
title: "Practice drills — randomized and autograded"
description: "Ten autograded drills with fresh random variants, hints after a wrong attempt and worked solutions: convolution, system properties, partial fractions, z-transforms and ROCs, stability from the ROC, unbounded outputs, DTFT values, the response to sinusoids, magnitude–phase–group delay of linear-phase filters, and True/False."
tags: [demo, practice, z-transform, dtft, frequency-response]
---

*Interactive practice for Units 1–3, in the spirit of PrairieLearn / TheorieLearn · each drill links back to its lecture and recipe · pairs with [[problems/index|the problem families]] and the past exams ([[exams/midterm-1/past-exams/index|Midterm 1]], [[exams/midterm-2/past-exams/index|Midterm 2]])*

> [!abstract] In one breath
> Pick a drill, press **New variant** for fresh numbers, answer, **Submit**. A wrong answer gets a hint, a second wrong answer a sharper one, and **Show worked solution** walks through the method step by step, with links to the lecture it comes from. Because every variant is new, you practise the method rather than memorizing an answer. The strip at the top keeps score the way the exams do: only your **first** submission of a variant earns points, and True/False is +2 / −1 / 0. Everything runs in your browser and nothing is saved, so reloading starts from zero.

<div class="ece-demo">
<iframe src="/static/demos/drills/" title="ECE 310 practice drills — randomized and autograded" loading="lazy" style="height:900px"></iframe>
</div>

[Open the drills in their own tab](/static/demos/drills/). It is roomier, and the better choice on a phone, where the tabs become a drop-down. Each drill also has its own address: [convolution](/static/demos/drills/#conv), [system properties](/static/demos/drills/#props), [PFE](/static/demos/drills/#pfe), [z-transform & ROC](/static/demos/drills/#zroc), [ROC → stable/causal](/static/demos/drills/#rocsc), [unbounded outputs](/static/demos/drills/#poles), [DTFT values](/static/demos/drills/#dtftv), [sinusoidal response](/static/demos/drills/#sinr), [magnitude & phase](/static/demos/drills/#magph), [True/False](/static/demos/drills/#tf).

## How to use the drills

A drill works best right after its lecture and its recipe page: you have just seen the method, and a few fresh variants show whether you can run it alone. Work on paper first, then type the answer. When the hint is needed, read it, close it in your head, and redo the variant before opening the worked solution. A miss you understand is worth more than a lucky hit.

> [!recipe] A study session (about 45 minutes)
> 1. **One method, three variants.** Pick the drill for the lecture you are on. Do three variants in a row and write the key step (the start index, the cover-up, the factored $e^{-jM\omega}$) before any arithmetic.
> 2. **Hint, then redo.** After a wrong answer, use hint 1 and try the *same* variant again. Hint 2 and the worked solution are for when you are stuck, and then a *new* variant tells you whether it stuck.
> 3. **Mix.** Finish with two variants of an older drill. The Unit 2 drills (PFE, ROCs, stability) feed straight into Unit 3: $H_d(\omega)$ exists only when the ROC contains the unit circle.
> 4. **True/False** — a short pass, reading the reason after every statement, including the ones you got right.

> [!note] Exam relevance
> Every drill comes from a problem type that appears on past midterms (the exam record is under each drill below), and the strip uses the exams' first-try scoring. Treat the score as feedback on the method, not as a grade.

Answers are checked tolerantly: `9/4`, `-5/4`, `2.25`, `−1.25` (either minus sign), spaces and braces are all accepted. For lists, use commas (`2, -1, 0, 5`) or spaces (`{2 -1 0 5}`). The Unit 3 drills also read `π` or `pi`, `√3` or `sqrt(3)`, products such as `3√2/2` and `2pi/3`, and degrees (`60°`). Angles are compared modulo $2\pi$, so $-\pi$ and $\pi$ are the same answer, and decimals are accepted to about three digits.

## The drills

### 1 · Finite-length convolution

You get $x[n]$ (3–5 samples, entries $-3,\dots,3$) and $h[n]$ (2–3 samples), each written the exam way with an arrow under the $n=0$ sample — the arrow can sit anywhere, so either sequence may start at a negative index (an index table is shown too). Enter $y[n] = x[n]*h[n]$ from its first to its last non-zero sample, plus the index where it starts. Points: 6 for the samples, 2 for the start index.

> [!key] Bookkeeping that decides half the points
> First index of $y$ = first index of $x$ + first index of $h$; length $L_x + L_h - 1$; first sample $x_{\text{first}}\,h_{\text{first}}$, last sample $x_{\text{last}}\,h_{\text{last}}$ — two free checks before any real work.

The worked solution shows the shift-and-add table (one row per input sample: a scaled, shifted copy of $h$) and the same numbers as the matrix product $y = Hx$ that the exam keys write out.

> [!trap] The keys slip here too
> The SP2025 #4(a) key boxes a wrong answer although its own matrix is right — see [[0-toolkit/05-errata|the errata page]]. Trust the bookkeeping rule (and the sum check $\sum y = \sum x\cdot\sum h$), not a copied box.

Exam record: 7/7 past exams ([[exams/midterm-1/past-exams/fall-2025|FA2025 #3a]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #4a]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #2]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #4]], …). Recipe: [[problems/finite-length-convolution|finite-length convolution]]. Theory: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[concepts/convolution|convolution]]. For the sliding picture, use [[demos/convolution-explorer|the convolution explorer]].

### 2 · System properties

A deck of **45 systems**: every row of the seven past-exam property tables, the clipping and windowing systems of HW1 #5–6, the three systems of HW2 #1, and the Lecture 3 examples. Tick Linear / Time-invariant / Causal / BIBO stable; each box is worth one point, as on the exam (three systems × four boxes = 12 points). Every box comes back with a one-line reason. The deck runs through all 45 before repeating.

> [!trap] The ones people miss
> $y[n] = \dfrac{x[n]}{\lvert n\rvert + 1}$ **is** stable (the gain never exceeds 1), but $y[n] = \ln\lvert x[n]\rvert$ is **not** ($x[n] = 0$ is a bounded input); $y[n] = x[n]/x[2]$ is No on all four; $x[n]*u[n+1]$ is non-causal *and* unstable; anything with $x[0]$, $x[3]$ or $x[\lvert n\rvert]$ fails time-invariance **and** causality.

The answers are the official keys (checked numerically by the scripts behind [[exams/midterm-1/system-property-bank|the system-property bank]], which gives every system with its proof). Recipe: [[problems/classifying-system-properties|classifying system properties]]. Theory: [[1-signals-and-systems/03-system-properties|Lecture 3]], [[concepts/linearity|linearity]], [[concepts/time-invariance|time-invariance]], [[concepts/causality|causality]], [[concepts/bibo-stability|BIBO stability]].

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

Exam record: 7/7 past exams ask for an inverse transform, all possible ROCs, or both ([[exams/midterm-1/past-exams/fall-2025|FA2025 #7]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #7]], …). Recipe: [[problems/all-possible-rocs|inverse z, PFE and all possible ROCs]]; the anti-causal half as a recursion: [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]]. Theory: [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[concepts/partial-fraction-expansion|partial-fraction expansion]], [[concepts/inverse-z-transform|inverse z-transform]].

### 4 · z-transform and ROC of a signal

Five signal families, as on the exams: a shifted right-sided exponential $A\,a^n u[n-k]$ (the shift $k$ can be negative), a left-sided $C\,a^n u[-n-1]$, a left-sided sequence that stops at a positive index, $C\,a^n u[-n+k]$ (the SP2025 #5b type), a right-sided plus a left-sided term (whose ROC is sometimes **empty**), and a short finite sequence with the arrow. **(a)** Choose the ROC's shape from a menu that distinguishes $\lvert z\rvert > r$ from $r < \lvert z\rvert < \infty$ and $\lvert z\rvert < r$ from $0 < \lvert z\rvert < r$ (the keys do: FA2025 #5a is "$1 < \lvert z\rvert < \infty$", SP2025 #5b is "$0 < \lvert z\rvert < 3$"), and type the radii — 3 points, 2 if only the $z = 0$ / $z = \infty$ part is off. **(b)** Pick $X(z)$ among four options built from real mistakes: a missing factor $a^k$, the shift in the wrong direction, the pole at $1/a$ instead of $a$, the dropped minus sign of the left-sided pair, an off-by-one power, or "does not exist" when the ROC is not actually empty — 3 points.

> [!key] The pairs and the two special points
> $a^n u[n] \leftrightarrow \dfrac{1}{1 - a z^{-1}}$, ROC $\lvert z\rvert > \lvert a\rvert$; $\ -a^n u[-n-1] \leftrightarrow \dfrac{1}{1 - a z^{-1}}$, ROC $\lvert z\rvert < \lvert a\rvert$; $\ x[n-k] \leftrightarrow z^{-k}X(z)$. Samples at $n > 0$ exclude $z = 0$; samples at $n < 0$ exclude $z = \infty$.

Exam record: 6/7 past exams ([[exams/midterm-1/past-exams/fall-2025|FA2025 #5]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #5]], [[exams/midterm-1/past-exams/fall-2024|FA2024 #5]], [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]]). Recipe: [[problems/z-transform-with-roc|z-transform with ROC]]. Theory: [[2-z-transform/06-the-z-transform|Lecture 6]], [[2-z-transform/07-z-transform-properties|Lecture 7]], [[concepts/z-transform-pairs|z-transform pairs]], [[concepts/region-of-convergence|ROC]], [[concepts/sided-sequences|sided sequences]].

### 5 · Stability and causality from the ROC

$H(z)$ has two to four poles — real ones, sometimes a pair $\pm jr$ hidden in a factor $(1 + r^2 z^{-2})$ — and often a zero, which has nothing to do with the ROC (a deliberate distractor). You are told one fact: *the system is causal*, *BIBO stable*, or *$h[n]$ is left-sided / right-sided / two-sided*. **(a)** Pick the ROC among all the rings the pole circles allow (2 points), then say **(b)** stable? and **(c)** causal? (1 point each). The worked solution tabulates every possible ROC with its sidedness and stability — the "all possible ROCs" question of [[exams/midterm-1/past-exams/fall-2019|FA2019 #7]].

> [!key] Read everything off the ring
> Causal $\iff$ ROC outside the outermost pole **and** $H$ proper in $z^{-1}$ (numerator degree ≤ denominator degree, so the ROC includes $\infty$). Left-sided $\iff$ inside the innermost pole. Two-sided $\iff$ a ring between two poles. BIBO stable $\iff$ the ring contains $\lvert z\rvert = 1$. So "causal **and** stable" $\iff$ every pole inside the unit circle.

Recipe: [[problems/all-possible-rocs|all possible ROCs]], [[problems/parameters-for-stability|parameters for stability]]. Theory: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]], [[concepts/poles-and-zeros|poles and zeros]], [[concepts/bibo-stability|BIBO stability]], [[concepts/causality|causality]].

### 6 · Unbounded outputs: pole matching

A **causal** $H(z)$ with poles on the unit circle — at $1$, $-1$, $\pm j$, $e^{\pm j\pi/4}$, $e^{\pm j\pi/3}$, $e^{\pm j2\pi/3}$, or the FA2025 trap $e^{j2/3}$ — sometimes with a pole inside, sometimes with one **outside** the unit circle, sometimes with a zero. Five or six bounded inputs follow ($u[n]$, $(-1)^n u[n]$, $j^n u[n]$, $e^{j\omega n}u[n]$, $\cos(\omega n)u[n]$, $\sin(\omega n)u[n]$, $(2/3)^n u[n]$, $\delta[n] - p\,\delta[n-1]$, $a^n u[n] - p\,a^{n-1}u[n-1]$); tick the ones whose output is unbounded. One point per input, like FA2025 #8 and SP2025 #6. Every input comes back with its reason: which poles meet, which zero cancels what.

> [!key] The whole rule
> $Y(z) = H(z)X(z)$. After cancelling common factors, $y[n]$ is unbounded $\iff$ $Y$ has a pole **outside** the unit circle or a **repeated** pole **on** it. So: an input pole landing on one of $H$'s unit-circle poles resonates (growth like $n$); an input whose zero sits exactly on $H$'s outside pole rescues the output (FA2025 #8a ii and v).

> [!trap] $e^{j2/3}$ is not $e^{j2\pi/3}$
> In [[exams/midterm-1/past-exams/fall-2025|FA2025 #8b]] the pole is $e^{j2/3}$ — angle $2/3$ rad $\approx 38^\circ$, not $120^\circ$ — so $\cos(\tfrac{2\pi}{3}n)u[n]$ gives a **bounded** output (key: False). The drill plants this trap regularly.

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

Exam record: 7/7 past exams ([[exams/midterm-1/past-exams/fall-2025|FA2025 #8]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #6]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #5]], …). Recipe: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]]. Theory: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]], [[concepts/marginal-stability|marginal stability]], [[concepts/pole-zero-cancellation|pole-zero cancellation]].

### 7 · DTFT values straight from $x[n]$

A short integer sequence with the arrow somewhere inside it (sometimes the symmetric, centred kind of [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2 #3]]). Find **(a)** $X_d(0)$, **(b)** $X_d(\pi)$, **(c)** $\int_{-\pi}^{\pi} X_d(\omega)\,d\omega$ and **(d)** $\int_{-\pi}^{\pi} \lvert X_d(\omega)\rvert^2\,d\omega$, the last two as multiples of $\pi$. Two points each. None of them needs $X_d(\omega)$ in closed form.

> [!key] Four facts, four numbers
> $X_d(0) = \sum_n x[n]$, since every $e^{-j0n} = 1$. $X_d(\pi) = \sum_n (-1)^n x[n]$, since $e^{-j\pi n} = (-1)^n$. The inverse DTFT at $n = 0$ gives $\int_{-\pi}^{\pi} X_d(\omega)\,d\omega = 2\pi\,x[0]$, and Parseval gives $\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega = 2\pi\sum_n \lvert x[n]\rvert^2$.

> [!trap] The sign pattern follows $n$, not the list
> In $X_d(\pi)$ the sample under the arrow always gets $+$, and so does every even $n$, negative ones included. Starting the alternation at the first entry of the list gives the wrong answer whenever the sequence starts at an odd index. The drill recognizes this slip, and the "forgot the $2\pi$" slip in (c) and (d), and says so.

The worked solution is one table ($n$, $x[n]$, $(-1)^n$, $(-1)^n x[n]$, $\lvert x[n]\rvert^2$) plus the four identities. Exam record: FA2019 MT2 #3 asks (a)–(c) for $x[n] = \{1, -3, 5, \underset{\uparrow}{-7}, 5, -3, 1\}$ (key: $-1$, $-25$, $-14\pi$), and [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2 #2]] asks $X_d(0)$ and $X_d(\pi)$; [[homework/hw5|HW5 #2]] asks all four. Part (d) is Parseval's relation from Lecture 14. Recipe: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]]. Theory: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]], [[concepts/dtft|DTFT]], [[concepts/dtft-properties|DTFT properties]].

### 8 · A real LTI system driven by a sum of sinusoids

The system comes either as a short real FIR $h[n]$ (two or three taps, symmetric or antisymmetric, the arrow under the first tap or the next one) or as a formula. The formulas come from the course: $\lvert H_d(\omega)\rvert = \cos^2\omega$, $\angle H_d(\omega) = \sin\omega$ (the Lecture 15 concept check), $2j\,e^{-j\omega}\sin\omega$ (Lecture 16, Exercise 1), $2e^{-j3\omega}\cos 3\omega$ (SP2023 MT2 #5), and a few like them. The input is a constant, plus a cosine or a sine at $\tfrac{\pi}{3}$, $\tfrac{\pi}{2}$ or $\tfrac{2\pi}{3}$, plus $(-1)^n$. Write the output as $y[n] = c_0 + B\cos(\omega_1 n + \varphi) + c_2(-1)^n$ and enter $c_0$, $B$, $\varphi$ and $c_2$, two points each.

> [!key] One frequency at a time
> A constant is the frequency $\omega = 0$ and $(-1)^n = \cos(\pi n)$ is $\omega = \pi$: they come out multiplied by $H_d(0)$ and $H_d(\pi)$, which are real for a real $h[n]$. A cosine keeps its frequency: $A\cos(\omega_1 n + \theta) \to A\lvert H_d(\omega_1)\rvert\cos(\omega_1 n + \theta + \angle H_d(\omega_1))$. A sine becomes a cosine first: $\sin\alpha = \cos(\alpha - \tfrac{\pi}{2})$.

> [!trap] A negative real factor is a phase of π
> In $H_d(\omega) = e^{-j2\omega}(1 + 2\cos\omega)$ the factor $1 + 2\cos\omega$ is negative for $\lvert\omega\rvert > \tfrac{2\pi}{3}$. There the magnitude is $-(1 + 2\cos\omega)$ and the phase is $-2\omega \pm \pi$. The worked solution writes every system as $R(\omega)e^{j\psi(\omega)}$ with $R$ real and handles the sign explicitly.

The checker compares the phasor $Be^{j\varphi}$, so $\varphi + 2\pi$, degrees and even $(-B, \varphi + \pi)$ are accepted. Now and then the cosine sits on a zero of $H_d$ and is blocked completely; then any phase counts. Where it appears: [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2 #7]], [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2 #4]] and [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2 #4]], the Lecture 15 slides' examples, and HW6 #6–7. [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2 #6]] and [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2 #4]] use a system whose $h[n]$ is not real, so test $H_d(-\omega) = H_d^*(\omega)$ before using the real-system rule; the recipe shows what to do when the test fails. Recipe: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]]. Theory: [[3-fourier-analysis/15-frequency-response|Lecture 15]], [[concepts/frequency-response|frequency response]], [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]]. To watch it happen, set the same system in the [[demos/frequency-response-explorer|frequency-response explorer]] and move ω₀.

### 9 · Magnitude, phase and group delay of a linear-phase FIR

A symmetric or antisymmetric $h[n]$ with two to five taps and the arrow anywhere, plus one frequency $\omega_0$. The statement gives the template, $H_d(\omega) = e^{-jM\omega}A(\omega)$ (symmetric) or $j\,e^{-jM\omega}A(\omega)$ (antisymmetric) with $A$ real. Find **(a)** the group delay $M$, **(b)** $A(\omega_0)$ with its sign, **(c)** $\lvert H_d(\omega_0)\rvert$ and **(d)** $\angle H_d(\omega_0)$ as a principal value. Two points each.

> [!key] Factor, then read off
> The centre is $M = \tfrac{\text{first index} + \text{last index}}{2}$, a half-integer for an even number of taps. Pairing the taps about it gives $h[M-m]e^{-j\omega(M-m)} + h[M+m]e^{-j\omega(M+m)} = e^{-jM\omega}\cdot 2h[M-m]\cos(m\omega)$, or $\cdot\,2j\,h[M-m]\sin(m\omega)$ for antisymmetric taps. Then $\lvert H_d\rvert = \lvert A\rvert$, and $\angle H_d = -M\omega$ ($+\tfrac{\pi}{2}$ for the $j$), plus $\pi$ where $A < 0$. The group delay is $M$, because the π jumps change the phase but not its slope.

The targeted messages catch the usual slips: $-M$ instead of $M$, the centre counted from the first tap instead of from $n = 0$, a negative "magnitude", and a forgotten $\pi$ or $\tfrac{\pi}{2}$. Exam record: the factoring is [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2 #3]] itself, and sketches of such filters are SP2021 MT2 #2 (from the formula), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2 #5]], [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2 #3]] (the magnitude only) and [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2 #3]]. Recipe: [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]]. Theory: [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]], [[concepts/magnitude-and-phase-response|magnitude and phase response]], [[concepts/group-delay|group delay]].

### 10 · True/False rapid fire

All **42** True/False statements from the seven past exams (the two DTFT statements of SP2023 left out), one at a time, with the official answer and a one-line reason after you commit. Scoring is the exam's: **+2** right, **−1** wrong, **0** skipped — a guess with success probability $p$ is worth $3p-1$, so a coin flip ($+0.5$) beats skipping; skip only when you are worse than one-in-three. Each statement is answered once; the deck runs through all 42 before reshuffling. Keyboard: `T`, `F`, `S`, then `N` for the next one.

> [!tip] Where the points go
> Most of the 42 turn on four facts: LTI systems are the only ones $h[n]$ describes; BIBO stable $\iff \sum\lvert h[n]\rvert < \infty$ (bounded $h$ is not enough, FIR is always enough); stable $\iff$ the ROC contains the unit circle; poles can cancel (in sums, cascades, and against input zeros). One statement, FA2025 #1(d), is keyed True under the reading "left-sided = extends to $-\infty$" — $\delta[n]$ is the pedantic exception.

The full list with longer explanations, grouped by topic: [[exams/midterm-1/true-false-bank|True/False bank]]. Background: [[concepts/lti-system|LTI systems]], [[concepts/bibo-stability|BIBO stability]], [[concepts/pole-zero-cancellation|pole-zero cancellation]].

## Scoring

| drill | points per variant | partial credit |
|---|---|---|
| Convolution | 8 | samples 6, start index 2 |
| System properties | 4 | 1 per box, no penalty |
| PFE & inverse $z$ | 8 | $A_1$ 2, $A_2$ 2, $h[n]$ 3, stability 1 |
| z-transform & ROC | 6 | ROC 3 (2 for a $0$/$\infty$ slip, 1 for the right shape with a wrong radius), $X(z)$ 3 |
| ROC → stable / causal | 4 | ROC 2, stable 1, causal 1 |
| Unbounded outputs | 5–6 | 1 per input |
| DTFT values | 8 | 2 each: $X_d(0)$, $X_d(\pi)$, $\int X_d\,d\omega$, $\int\lvert X_d\rvert^2 d\omega$ |
| Sinusoidal response | 8 | 2 each: $c_0$, $B$, $\varphi$ (needs the right $B$), $c_2$ |
| Magnitude & phase | 8 | 2 each: $M$, $A(\omega_0)$, $\lvert H_d(\omega_0)\rvert$, $\angle H_d(\omega_0)$ |
| True/False | 2 | +2 right, −1 wrong, 0 skipped |

"Correct" counts variants that were fully right on the first submission. Opening the worked solution before submitting scores that variant as a blank. The strip shows the running total and, underneath, the current drill.

## How the drills were checked

Every generator was run over 600 random seeds in Node (about 47 000 checks): convolution outputs against the direct sum $\sum_k x[k]\,h[n-k]$; every PFE by recombining $A_1/(1-p_1z^{-1}) + A_2/(1-p_2z^{-1})$ exactly and by summing the chosen $h[n]$ against $H(z)$ inside the ROC (no distractor may pass); every ROC by probing where the actual series $\sum x[n]z^{-n}$ converges, including $z = 0$ and $z = \infty$; stability and causality from a numerically built $h[n]$; unbounded outputs by simulating $y = h * x$. A sample of variants was re-checked independently in Python — `np.convolve`, `scipy.signal.residuez`, partial sums, and, for the pole drill, an exact simulation in rational arithmetic (so a cancelled unstable pole stays cancelled). The property and True/False answers were compared line by line with the verified keys, the test suite was confirmed to catch deliberately planted bugs, and a headless browser clicked through every drill (wrong answer, right answer, worked solution) in light and dark mode and at phone width.

The three Unit 3 drills have their own test, `verify/INT_drills_test.js`: 2,500 seeds per drill and about 167,000 checks, re-running the seven older drills as well. For every variant the generator's answer must pass its own checker, and the stored answers must agree with numbers computed independently in the test. For *DTFT values* those come from the DTFT sum at $0$ and $\pi$ and from trapezoid quadrature of $X_d$ and $\lvert X_d\rvert^2$ over one period, which is exact for these short sequences. For *Sinusoidal response* the output is computed by direct convolution of $h[n]$ with the two-sided input (or from the test's own copy of each formula) and compared with $c_0 + B\cos(\omega_1 n + \varphi) + c_2(-1)^n$ at sixteen samples. For *Magnitude & phase* the test computes $H_d(\omega_0) = \sum h[n]e^{-j\omega_0 n}$, recovers $A(\omega_0)$ from it, and checks the group delay $M$ at five random frequencies. Each answer field is also perturbed, and the checker must then mark exactly that part wrong. Alternative spellings ($\pi$ or `pi`, degrees, $+2\pi$, decimals, `sqrt`) must be accepted.

## Related

[[exams/midterm-1/true-false-bank|True/False bank]] · [[exams/midterm-1/system-property-bank|System-property bank]] · [[problems/index|Problem families]] · [[demos/index|All demos]] · [[demos/pole-zero-and-roc-explorer|Pole-zero and ROC explorer]] · [[demos/frequency-response-explorer|Frequency-response explorer]] · [[3-fourier-analysis/index|Unit 3 overview]]

### Sources for this page

Past Midterm 1 exams and keys FA2025, SP2025, FA2024, FA2023, SP2023, SP2021, FA2019 (True/False statements, property tables, convolution, z-transform, PFE and pole-matching problems, grading rules); HW1 #5–6 and HW2 #1 with official solutions; Lecture 3 slides and notes (property examples); Lecture 6–8 notes (pairs, properties, cover-up); Lecture 11 notes (stability and causality from the ROC). Unit 3 drills: Lecture 13 notes (inverse DTFT), Lecture 14 notes (Parseval), Lecture 15 notes and slides (sinusoidal response, concept check), Lecture 16 notes (Exercises 1–2, group delay); HW5 #2; past Midterm 2 keys FA2019 #3 and #7, SP2021 #2–3, SP2023 #5–6, FA2023 #2 and #4, FA2024 #3–4, SP2025 #3–4. Answer keys as verified in `verify/exams/`; drill tests in `verify/drills/`, `verify/INT_drills_test.js` and `verify/REV_R6_drills.py`.
