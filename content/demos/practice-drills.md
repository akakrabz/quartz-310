---
title: "Practice drills — randomized and autograded"
description: "Ten autograded drills with fresh random variants, hints and worked solutions: convolution, system properties, PFE, z-transform and ROC, stability, unbounded outputs, DTFT values, sinusoidal response, linear phase, True/False."
tags: [demo, practice, z-transform, dtft, frequency-response]
---

*Interactive practice for Units 1–3 · pairs with [[problems/index|the problem families]] and the past exams ([[exams/midterm-1/past-exams/index|Midterm 1]], [[exams/midterm-2/past-exams/index|Midterm 2]])*

> [!abstract] In one breath
> - **New variant** for fresh numbers, **Submit**; wrong answers get hints, then a worked solution.
> - Only the first submission scores, as on the exams; True/False is +2 / −1 / 0.
> - Runs in the browser; nothing is saved.

<div class="ece-demo">
<iframe src="/static/demos/drills/" title="ECE 310 practice drills — randomized and autograded" loading="lazy" style="height:900px"></iframe>
</div>

[Open the drills in their own tab](/static/demos/drills/) (better on a phone). Direct links: [convolution](/static/demos/drills/#conv), [system properties](/static/demos/drills/#props), [PFE](/static/demos/drills/#pfe), [z-transform & ROC](/static/demos/drills/#zroc), [ROC → stable/causal](/static/demos/drills/#rocsc), [unbounded outputs](/static/demos/drills/#poles), [DTFT values](/static/demos/drills/#dtftv), [sinusoidal response](/static/demos/drills/#sinr), [magnitude & phase](/static/demos/drills/#magph), [True/False](/static/demos/drills/#tf).

> [!recipe] A session (about 45 minutes)
> 1. Three variants of the drill for the current lecture; write the key step before any arithmetic.
> 2. After a wrong answer: hint 1, redo the same variant; then a new variant.
> 3. Two variants of an older drill.
> 4. A short True/False pass, reading every reason.

Answers accept fractions (`9/4`), decimals, either minus sign, lists with commas or spaces, `pi`/`π`, `sqrt(3)`/`√3`, degrees. Angles are compared modulo $2\pi$.

## The drills

| # | drill | task | key rule | recipe |
|---|---|---|---|---|
| 1 | Convolution | $y=x*h$ and its start index | start = start of $x$ + start of $h$; length $L_x+L_h-1$; $\sum y=\sum x\cdot\sum h$ | [[problems/finite-length-convolution\|finite-length convolution]] |
| 2 | System properties | 45 systems: L / TI / C / S | one bounded input with unbounded output disproves stability | [[problems/classifying-system-properties\|system properties]] |
| 3 | PFE & inverse $z$ | $A_1$, $A_2$, $h[n]$ for a given ROC, stability | $A_k = \bigl[(1 - p_k z^{-1})H(z)\bigr]_{z = p_k}$; $A_1+A_2=b_0$ | [[problems/all-possible-rocs\|all possible ROCs]] |
| 4 | z-transform & ROC | ROC shape and radii, then $X(z)$ | samples at $n>0$ exclude $z=0$; at $n<0$ exclude $z=\infty$ | [[problems/z-transform-with-roc\|z-transform with ROC]] |
| 5 | ROC → stable/causal | pick the ROC from one fact | causal: outside outermost pole; stable: ring contains $\lvert z\rvert=1$ | [[problems/parameters-for-stability\|parameters for stability]] |
| 6 | Unbounded outputs | tick inputs with unbounded output | unbounded iff $Y$ has a pole outside or a repeated pole on $\lvert z\rvert=1$ | [[problems/unbounded-outputs-and-pole-matching\|pole matching]] |
| 7 | DTFT values | $X_d(0)$, $X_d(\pi)$, $\int X_d$, $\int\lvert X_d\rvert^2$ | $\sum x$, $\sum(-1)^nx$, $2\pi x[0]$, $2\pi\sum\lvert x\rvert^2$ | [[problems/dtft-and-inverse-dtft\|DTFT family]] |
| 8 | Sinusoidal response | $c_0$, $B$, $\varphi$, $c_2$ | each frequency scaled by $\lvert H_d\rvert$, shifted by $\angle H_d$ | [[problems/lti-response-to-sinusoids\|response to sinusoids]] |
| 9 | Magnitude & phase | $M$, $A(\omega_0)$, $\lvert H_d\rvert$, $\angle H_d$ | $H_d=e^{-jM\omega}A(\omega)$; $\pi$ where $A<0$ | [[problems/magnitude-phase-and-group-delay\|magnitude, phase, group delay]] |
| 10 | True/False | 42 past-exam statements | stable ⇔ $\sum\lvert h\rvert<\infty$ ⇔ ROC contains $\lvert z\rvert=1$; poles can cancel | [[exams/midterm-1/true-false-bank\|T/F bank]] |

> [!trap]
> - $X_d(\pi)$: the sign follows $n$, not the position in the list.
> - $e^{j2/3}$ is not $e^{j2\pi/3}$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #8b]]); the pole drill plants it.
> - $\ln\lvert x[n]\rvert$ is unstable ($x=0$); $\frac{x[n]}{\lvert n\rvert+1}$ is stable.
> - A negative real amplitude is a phase of $\pi$, not a negative magnitude.
> - SP2025 #4(a)'s key boxes a wrong convolution ([[0-toolkit/05-errata|errata]]).

## Scoring

| drill | points | partial credit |
|---|---|---|
| Convolution | 8 | samples 6, start 2 |
| System properties | 4 | 1 per box |
| PFE & inverse $z$ | 8 | $A_1$ 2, $A_2$ 2, $h[n]$ 3, stability 1 |
| z-transform & ROC | 6 | ROC 3, $X(z)$ 3 |
| ROC → stable/causal | 4 | ROC 2, stable 1, causal 1 |
| Unbounded outputs | 5–6 | 1 per input |
| DTFT values, sinusoidal response, magnitude & phase | 8 | 2 per field |
| True/False | 2 | +2 / −1 / 0 |

Opening the worked solution before submitting scores the variant as blank.

## Related
[[exams/midterm-1/true-false-bank|True/False bank]] · [[exams/midterm-1/system-property-bank|System-property bank]] · [[problems/index|Problem families]] · [[demos/index|All demos]] · [[demos/frequency-response-explorer|Frequency-response explorer]]

### Sources for this page
Past Midterm 1 and 2 keys (FA2019–FA2025); HW1 #5–6, HW2 #1, HW5 #2; Lectures 3, 6–8, 11, 13–16 notes and slides.
