---
title: "Lecture 5 — Difference equations and block diagrams"
description: "LCCDEs as the practical description of LTI systems: FIR versus IIR, running the recursion sample by sample (how a DSP chip filters in real time), impulse responses of recursive systems by superposition, the Lecture 5 versus Lecture 9 sign convention, scipy's lfilter, and direct-form block diagrams."
tags: [lecture, midterm-1, systems, lccde]
lecture: 5
---

*Lecture 5 · Wed Sep 2, 2026 · notes + slides "Difference equations and block diagrams" · prev: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · next: [[2-z-transform/06-the-z-transform|Lecture 6]]*

> [!abstract] In one breath
> A linear constant-coefficient difference equation (LCCDE) computes each output sample as a fixed linear combination of the current and past **inputs** and the past **outputs**. Started at rest, it is an LTI system; with only delays (no advances) it is causal. Without feedback the impulse response is simply the list of input coefficients (**FIR**). With feedback the output can ring forever (**IIR**): $y[n] = \tfrac12 y[n-1] + x[n]$ has $h[n] = (\tfrac12)^n u[n]$. An infinitely long $h$ cannot be convolved in practice, but the recursion can be run, a few multiply-adds per sample. That is exactly how DSP hardware filters in real time. Block diagrams draw the same recursion with delays, gains and adders. One warning for the whole course: Lecture 5 writes feedback on the right-hand side, Lecture 9 (and SciPy) on the left, so the feedback coefficients change sign.

## 1. Linear constant-coefficient difference equations

Lecture 5 writes an LCCDE as

$$
y[n] = \sum_{i=1}^{K} b_i\,y[n-i] + \sum_{j=0}^{M-1} c_j\,x[n-j], \qquad 0 \le K < \infty,\quad 1 \le M < \infty .
$$

- $K$ **feedback** (output) terms with constant coefficients $b_1, \dots, b_K$ at delays $1, \dots, K$;
- $M$ **input** terms with constant coefficients $c_0, \dots, c_{M-1}$ at delays $0, \dots, M-1$.

Two standing assumptions make this an LTI system:

- **Initial rest (zero initial conditions):** the system is "at rest" when the input arrives, $y[n] = 0$ before the input starts. In hardware this just means clearing the memory before the first sample. Without it the system is not even linear: in [[homework/hw2|HW2]] #1(a), $y[n] = y[n-5] + x[n] + 10x[n-1]$ with a stored $y[-5] = 1$ answers the zero input with $y[0] = 1$.
- **Constant coefficients:** $b_i, c_j$ do not depend on $n$. ($y[n-2] + 2y[n] = \cos(\frac{\pi}{6}n)\,x[n]$ from HW2 #1(b) is linear but time-varying.)

If every shift is a delay ($i \ge 1$, $j \ge 0$), $y[n]$ uses no future values and the system is **causal**. LCCDEs can also describe non-causal systems, with terms like $x[n+2]$ or $y[n+1]$.

> [!warning] Two sign conventions: Lecture 5 versus Lecture 9, exams and SciPy
> From [[2-z-transform/09-transfer-functions|Lecture 9]] on (and in every exam key), all output terms sit on the **left**:
> $$
> y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k], \qquad H(z) = \frac{\sum_k b_k z^{-k}}{1 + \sum_k a_k z^{-k}} .
> $$
> Moving the feedback across the equals sign flips its sign, and the letters swap roles:
> $$
> a_k = -\,b_k^{(\text{L5})}, \qquad b_k^{(\text{L9})} = c_k^{(\text{L5})} .
> $$
> Example: $y[n] = \tfrac12 y[n-1] + x[n]$ has $b_1 = +\tfrac12$ in Lecture 5, but $a_1 = -\tfrac12$ in Lecture 9, `lfilter([1], [1, -0.5], x)` in SciPy, and $H(z) = \dfrac{1}{1 - \frac12 z^{-1}}$. Feeding SciPy `[1, +0.5]` instead silently computes $(-\tfrac12)^n$. In Lecture 5 "$b$" means *feedback*; in Lecture 9 and SciPy "$b$" means *feedforward*.

## 2. Running the recursion: how a filter works in real time

Take $y[n] = \tfrac12 y[n-1] + x[n]$ with $x[n] = \delta[n]$, at rest ($y[-1] = 0$). Each new output needs one stored number:

| $n$ | $x[n]$ | stored $y[n-1]$ | $y[n] = \tfrac12 y[n-1] + x[n]$ |
|---|---|---|---|
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | $\tfrac12$ |
| 2 | 0 | $\tfrac12$ | $\tfrac14$ |
| 3 | 0 | $\tfrac14$ | $\tfrac18$ |
| 4 | 0 | $\tfrac18$ | $\tfrac1{16}$ |

$$
h[n] = \Big\{\underset{\uparrow}{1},\ \tfrac12,\ \tfrac14,\ \tfrac18,\ \tfrac1{16},\ \dots\Big\} = \left(\tfrac12\right)^n u[n].
$$

The input is a single nonzero sample, yet the output never stops: the feedback keeps recirculating it.

> [!intuition] What a DSP chip actually does
> A filter running on a phone, a hearing aid or an audio interface does not compute a z-transform and does not convolve with the (possibly infinite) $h[n]$. It runs the difference equation. It keeps the last few inputs and outputs in a small circular buffer (the delay line); each time the converter delivers a new sample $x[n]$ it performs $K + M$ multiply-accumulates, outputs $y[n]$, and shifts the buffer by one. A 2nd-order section costs 5 multiplies per sample, whatever the length of its impulse response. The z-transform (Lectures 6–11) is the *design and analysis* tool that tells you what the recursion will do; the recursion is the *implementation*.

The same computation in Python: the explicit loop is the chip; `scipy.signal.lfilter(b, a, x)` runs the identical recursion in compiled code, but with the **Lecture 9** sign convention.

```python
import numpy as np
from scipy.signal import lfilter
# Notes Exercise 1 (Lecture 5 form): y[n] = 1/4 y[n-1] - x[n] + 1/2 x[n-2]
x = np.zeros(6); x[0] = 1                     # x = delta[n], n = 0..5
y = np.zeros(6)                               # initial rest: nothing stored yet
for n in range(6):                            # one new sample at a time, like a DSP chip
    y[n] = 0.25*(y[n-1] if n >= 1 else 0) - x[n] + 0.5*(x[n-2] if n >= 2 else 0)
b, a = [-1, 0, 0.5], [1, -0.25]               # scipy / Lecture 9 form: feedback sign flipped
h = lfilter(b, a, x)
n = np.arange(6)
print("loop   :", y)
print("lfilter:", h)
print("closed form matches:", np.allclose(h, -(0.25**n) + 0.5*0.25**(n-2.0)*(n >= 2)))
```

```text
loop   : [-1.         -0.25        0.4375      0.109375    0.02734375  0.00683594]
lfilter: [-1.         -0.25        0.4375      0.109375    0.02734375  0.00683594]
closed form matches: True
```

The closed form it matches is derived in §4.

## 3. FIR systems: no feedback ($K = 0$)

With no feedback terms the impulse response is read straight off the input coefficients:

$$
h[n] = \sum_{j=0}^{M-1} c_j\,\delta[n-j] = \{\underset{\uparrow}{c_0},\ c_1,\ \dots,\ c_{M-1}\}.
$$

It has finite length (**F**inite **I**mpulse **R**esponse) and the LCCDE *is* the convolution sum of [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]. The standard example is the length-$L$ **moving average**

$$
y[n] = \frac1L\sum_{i=0}^{L-1} x[n-i], \qquad h[n] = \frac1L\big(u[n] - u[n-L]\big).
$$

The notes point out a cheaper way to compute the same output: the sum at time $n$ shares $L-1$ terms with the sum at time $n-1$, so

$$
y[n] = y[n-1] + \frac1L\big(x[n] - x[n-L]\big),
$$

two additions per sample instead of $L$.

> [!trap] Feedback usually means IIR, but not always
> The notes' rule is "$K = 0$: FIR; $K > 0$: IIR". The recursive moving average above has a feedback term and still has the *finite* impulse response $\frac1L(u[n] - u[n-L])$: its feedback pole at $z = 1$ is cancelled by a zero ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[concepts/pole-zero-cancellation|pole-zero cancellation]]). For exam problems, "feedback ⇒ IIR" is the intended reading unless something cancels. What is always true: an FIR system is **always BIBO stable**, because $\sum\lvert h[n]\rvert$ is a finite sum of finite numbers.

## 4. IIR systems: feedback ($K > 0$)

**Slides Example 1: $y[n] = \tfrac13 y[n-1] + x[n]$.** By inspection, exactly as in §2: $h[0] = \tfrac13 h[-1] + \delta[0] = 1$ (at rest, $h[-1] = 0$), $h[1] = \tfrac13$, $h[2] = \tfrac19$, … so $h[n] = (\tfrac13)^n u[n]$. In general, $y[n] = a\,y[n-1] + x[n]$ has $h[n] = a^n u[n]$.

With more than one input term, inspection gets messy. The notes' trick uses linearity and time-invariance: split the system into its feedback part and its input part.

> [!recipe] Impulse response of a first-order recursion with several input terms
> 1. **Feedback part alone:** replace all input terms by a single new input $z[n]$: $\hat y[n] = b_1\,\hat y[n-1] + z[n]$. Its impulse response is $\hat h[n] = b_1^{\,n}\,u[n]$.
> 2. **Input part:** with $x[n] = \delta[n]$, the original input terms produce $z[n] = \sum_j c_j\,\delta[n-j]$.
> 3. **Superpose:** $h[n] = z[n] * \hat h[n] = \sum_j c_j\,\hat h[n-j]$. Shift the step along with the exponential.

**Notes Exercise 1: $y[n] = \tfrac14 y[n-1] - x[n] + \tfrac12 x[n-2]$.** Step 1: $\hat h[n] = (\tfrac14)^n u[n]$. Step 2: $z[n] = -\delta[n] + \tfrac12\delta[n-2]$. Step 3:

$$
h[n] = -\hat h[n] + \tfrac12\hat h[n-2] = -\left(\tfrac14\right)^n u[n] + \tfrac12\left(\tfrac14\right)^{n-2} u[n-2].
$$

First samples: $-1,\ -\tfrac14,\ \tfrac{7}{16},\ \tfrac{7}{64},\ \dots$, matching the loop and `lfilter` in §2.

> [!question] Slides Example 2: find $h[n]$ for $y[n] = \tfrac13 y[n-1] + x[n] - 3x[n-1] + x[n-2]$.

> [!success]- Answer (annotated slides)
> $\hat h[n] = (\tfrac13)^n u[n]$ and $z[n] = \delta[n] - 3\delta[n-1] + \delta[n-2]$, so
> $$
> h[n] = \left(\tfrac13\right)^n u[n] - 3\left(\tfrac13\right)^{n-1}u[n-1] + \left(\tfrac13\right)^{n-2}u[n-2].
> $$
> Samples: $h[0] = 1$, $h[1] = \tfrac13 - 3 = -\tfrac83$, and for $n \ge 2$ all three terms are on: $(\tfrac13)^n(1 - 9 + 9) = (\tfrac13)^n$, so $h[2] = \tfrac19$, $h[3] = \tfrac1{27}$, …

For second-order feedback ($y[n-2]$ terms) this trick needs the impulse response of a 2nd-order recursion, which is exactly what the z-transform and partial fractions deliver in [[2-z-transform/09-transfer-functions|Lecture 9]]. Until then you can always run the recursion by hand for a few samples:

> [!question] [[exams/midterm-1/past-exams/spring-2021|SP2021 #6]]: a causal LTI system at rest satisfies $y[n] = 2y[n-3] - x[n] + x[n-3]$. Find $h[0]$, $h[1]$, $h[3]$, $h[4]$.

> [!success]- Answer (the official key gets the sign wrong)
> Run $h[n] = 2h[n-3] - \delta[n] + \delta[n-3]$ with $h[n] = 0$ for $n < 0$:
> $h[0] = 2\cdot 0 - 1 + 0 = -1$, $h[1] = 0$, $h[2] = 0$, $h[3] = 2h[0] - 0 + 1 = -1$, $h[4] = 2h[1] = 0$ (and later $h[6] = -2$, $h[9] = -4$).
> The key writes $h[0] = 1$ and $h[3] = 3$: those are the values for $+x[n]$ instead of $-x[n]$. In Lecture 9 form, $H(z) = \dfrac{-1 + z^{-3}}{1 - 2z^{-3}}$. Listed in [[0-toolkit/05-errata|errata]].

## 5. Block diagrams

Three building blocks draw any LCCDE:

- the **delay** $z^{-1}$: in $x[n]$, out $x[n-1]$ (the name $z^{-1}$ will make sense in [[2-z-transform/06-the-z-transform|Lecture 6]]);
- the **gain** (coefficient) $c$: in $x[n]$, out $c\,x[n]$;
- the **adder**: in $x_1[n]$ and $x_2[n]$, out $x_1[n] + x_2[n]$.

The notes' example $y[n] = \tfrac12 y[n-1] + \tfrac12 y[n-2] + 3x[n] - 2x[n-1] + x[n-2]$ in **direct form I**, one delay line for the inputs and one for the outputs:

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img" aria-label="Direct form I block diagram of y[n] = 1/2 y[n-1] + 1/2 y[n-2] + 3x[n] - 2x[n-1] + x[n-2]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="14.0" y="61.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="50.0" y1="56.0" x2="96.0" y2="56.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="96.0" cy="56.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><line x1="96.0" y1="56.0" x2="156.0" y2="56.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="156.0" y="43.0" width="40.0" height="26.0" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.4"/><text x="176.0" y="61.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">3</text><line x1="196.0" y1="56.0" x2="242.0" y2="56.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="249.0,56.0 242.0,52.1 242.0,59.9" fill="currentColor"/><circle cx="262.0" cy="56.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="256.0" y1="56.0" x2="268.0" y2="56.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="262.0" y1="50.0" x2="262.0" y2="62.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="275.0" y1="56.0" x2="362.0" y2="56.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="369.0,56.0 362.0,52.1 362.0,59.9" fill="currentColor"/><circle cx="382.0" cy="56.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="376.0" y1="56.0" x2="388.0" y2="56.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="382.0" y1="50.0" x2="382.0" y2="62.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="395.0" y1="56.0" x2="548.0" y2="56.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="548.0" cy="56.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><line x1="548.0" y1="56.0" x2="599.0" y2="56.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="606.0,56.0 599.0,52.1 599.0,59.9" fill="currentColor"/><text x="612.0" y="61.0" text-anchor="start" fill="var(--accent2)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">y[n]</text><line x1="96.0" y1="56.0" x2="96.0" y2="97.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="74.0" y="97.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="96.0" y="116.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="96.0" y1="125.0" x2="96.0" y2="156.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="96.0,162.0 92.7,156.0 99.3,156.0" fill="currentColor"/><circle cx="96.0" cy="166.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="86.0" y="186.0" text-anchor="end" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n−1]</text><line x1="96.0" y1="166.0" x2="156.0" y2="166.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="156.0" y="153.0" width="40.0" height="26.0" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.4"/><text x="176.0" y="171.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">−2</text><line x1="96.0" y1="166.0" x2="96.0" y2="207.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="74.0" y="207.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="96.0" y="226.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="96.0" y1="235.0" x2="96.0" y2="266.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="96.0,272.0 92.7,266.0 99.3,266.0" fill="currentColor"/><circle cx="96.0" cy="276.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="86.0" y="296.0" text-anchor="end" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n−2]</text><line x1="96.0" y1="276.0" x2="156.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="156.0" y="263.0" width="40.0" height="26.0" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.4"/><text x="176.0" y="281.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">1</text><line x1="196.0" y1="166.0" x2="242.0" y2="166.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="249.0,166.0 242.0,162.2 242.0,169.8" fill="currentColor"/><circle cx="262.0" cy="166.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="256.0" y1="166.0" x2="268.0" y2="166.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="262.0" y1="160.0" x2="262.0" y2="172.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="196.0" y1="276.0" x2="262.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><line x1="262.0" y1="276.0" x2="262.0" y2="185.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,179.0 258.7,185.0 265.3,185.0" fill="currentColor"/><line x1="262.0" y1="153.0" x2="262.0" y2="75.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,69.0 258.7,75.0 265.3,75.0" fill="currentColor"/><line x1="548.0" y1="56.0" x2="548.0" y2="97.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="526.0" y="97.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="548.0" y="116.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="548.0" y1="125.0" x2="548.0" y2="156.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="548.0,162.0 544.7,156.0 551.3,156.0" fill="currentColor"/><circle cx="548.0" cy="166.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="558.0" y="186.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n−1]</text><line x1="548.0" y1="166.0" x2="488.0" y2="166.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="448.0" y="153.0" width="40.0" height="26.0" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="var(--accent2)" stroke-width="1.4"/><text x="468.0" y="171.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">½</text><line x1="548.0" y1="166.0" x2="548.0" y2="207.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="526.0" y="207.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="548.0" y="226.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="548.0" y1="235.0" x2="548.0" y2="266.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="548.0,272.0 544.7,266.0 551.3,266.0" fill="currentColor"/><circle cx="548.0" cy="276.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="558.0" y="296.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n−2]</text><line x1="548.0" y1="276.0" x2="488.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="448.0" y="263.0" width="40.0" height="26.0" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="var(--accent2)" stroke-width="1.4"/><text x="468.0" y="281.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">½</text><line x1="448.0" y1="166.0" x2="402.0" y2="166.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="395.0,166.0 402.0,162.2 402.0,169.8" fill="currentColor"/><circle cx="382.0" cy="166.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="376.0" y1="166.0" x2="388.0" y2="166.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="382.0" y1="160.0" x2="382.0" y2="172.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="448.0" y1="276.0" x2="382.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><line x1="382.0" y1="276.0" x2="382.0" y2="185.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="382.0,179.0 378.7,185.0 385.3,185.0" fill="currentColor"/><line x1="382.0" y1="153.0" x2="382.0" y2="75.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="382.0,69.0 378.7,75.0 385.3,75.0" fill="currentColor"/><text x="179.0" y="318.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">feedforward: current and past inputs</text><text x="465.0" y="318.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12.5px;font-weight:600;">feedback: past outputs</text><text x="320.0" y="346.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">y[n] = ½ y[n−1] + ½ y[n−2] + 3x[n] − 2x[n−1] + x[n−2]</text></svg><figcaption><strong>Direct form I: two delay lines, a column of gains, and adders.</strong> The left delay line stores x[n−1] and x[n−2] and feeds the gains 3, −2, 1 (the input coefficients); the right one stores the past outputs y[n−1] and y[n−2] and feeds them back through the gains ½, ½. Each gain on a delayed input is one term of the right-hand side; each gain on a delayed output is one feedback term. Per output sample the hardware does five multiplications and four additions, then shifts both delay lines by one.</figcaption></figure>

> [!recipe] Block diagram ↔ LCCDE
> - **LCCDE → diagram (direct form I):** a delay line on $x$ with one tap per input term (gain $c_j$ on $x[n-j]$), a delay line on $y$ with one tap per feedback term (gain $b_i$ on $y[n-i]$), everything summed into $y[n]$.
> - **Diagram → LCCDE:** label the output of every delay and every adder, write one equation per adder, and eliminate the internal labels. A gain on a delayed $y$ is a feedback term; its sign in the Lecture 5 form is the gain as drawn, in the Lecture 9 form it flips.
> - Running this diagram costs 5 multiplications and 4 additions per sample (§2). Other arrangements of the same blocks (direct form II, cascades) give the same $h[n]$; they come later in the course.

Iterating the example from rest gives $h = \{\underset{\uparrow}{3}, -\tfrac12, \tfrac94, \tfrac78, \tfrac{25}{16}, \dots\}$. It does not die out: one of its poles sits at $z = 1$, so this particular system is not BIBO stable ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]).

## 6. On the exam

> [!exam] Where Lecture 5 shows up
> - **LCCDE ↔ $H(z)$ ↔ response, on 7 of 7 exams (15–20 points):** [[exams/midterm-1/past-exams/fall-2025|FA2025 #6]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]], [[exams/midterm-1/past-exams/fall-2024|FA2024 #6]], [[exams/midterm-1/past-exams/fall-2023|FA2023 #6–7]], [[exams/midterm-1/past-exams/spring-2023|SP2023 #5–6]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #6]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #10]]. These are solved with the z-transform (Lecture 9), but they start and end with a difference equation written in the **Lecture 9 sign convention**: read it off $H(z)$ and do not flip signs twice. Recipe: [[problems/lccde-to-transfer-function-and-response]].
> - **FIR ⇒ stable:** [[exams/midterm-1/past-exams/fall-2025|FA2025 #4]] (the modified moving average $y[n] = \frac1L\sum_{k=0}^{L-1}x[n-Sk]$ has $h = \tfrac13(\delta[n] + \delta[n-4] + \delta[n-8])$ for $L = 3$, $S = 4$, always stable) and [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(e)]] ("an FIR system can be stable or unstable": False).
> - **An LCCDE alone does not fix the system:** [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(a)]] (True): $y[n] - \tfrac12 y[n-1] = x[n]$ is satisfied by the causal $h = (\tfrac12)^n u[n]$ *and* by the anti-causal $h = -(\tfrac12)^n u[-n-1]$. Initial rest / causality is an extra assumption; in the z-domain it is the choice of ROC.
> - **Recursions that run backwards:** an anti-causal system is still a recursion, run from the future to the past, e.g. $y_1[n-1] = -\tfrac12 y_1[n] + \tfrac98 x[n]$ in [[exams/midterm-1/past-exams/fall-2025|FA2025 #7(b)]]. See [[problems/two-sided-systems-as-recursions]].
> - Block diagrams have not been tested on the seven past exams or in HW1–HW4; know the three blocks and how to read a diagram back into an LCCDE.

## Related

- [[concepts/lccde|LCCDE]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/block-diagram|Block diagrams]] · [[concepts/impulse-response|Impulse response]] · [[concepts/transfer-function|Transfer function]]
- Try it: [[demos/difference-equation-simulator|difference-equation simulator]] (run any recursion sample by sample) · [[supplements/demo-notebooks|course demo notebooks]] (`lfilter`)
- Next: [[2-z-transform/06-the-z-transform|Lecture 6]] introduces the z-transform, which turns the recursion into the algebra $H(z) = B(z)/A(z)$ ([[2-z-transform/09-transfer-functions|Lecture 9]]).

### Sources for this page
Snyder, ECE 310 Lecture 5 notes (LCCDE definition, FIR and moving average, IIR example, Exercise 1, block-diagram elements and the direct form I example) and slides "Difference Equations and Block Diagrams" (Sep 2, 2026) with the annotated in-class deck (Examples 1–2). HW2 #1. Past Midterm 1 problems as cited; SP2021 #6 re-derived because the key's values are wrong. Every number and the Python output on this page are checked in `verify/lectures/l5_lccde.py`.
