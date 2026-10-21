---
title: "Lecture 5 — Difference equations and block diagrams"
description: "LCCDEs as descriptions of LTI systems: FIR (no feedback) versus IIR (feedback), impulse responses of recursions by superposition, the Lecture 5 versus Lecture 9 sign convention, and direct-form I block diagrams."
tags: [lecture, midterm-1, systems, lccde]
lecture: 5
---

*Lecture 5 · Wed Sep 2, 2026 · notes + slides "Difference equations and block diagrams" · prev: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · next: [[2-z-transform/06-the-z-transform|Lecture 6]]*

> [!abstract] In one breath
> - An LCCDE makes each output a fixed linear combination of current/past inputs and past outputs; at rest it is LTI.
> - No feedback: $h[n]$ = the input coefficients (FIR). Feedback: $h[n]$ can ring forever (IIR), yet the recursion is cheap to run.
> - Block diagrams draw the recursion with delays, gains, adders.

## 1. Linear constant-coefficient difference equations

> [!key] LCCDE (Lecture 5 form)
> $$
> y[n] = \sum_{i=1}^{K} b_i\,y[n-i] + \sum_{j=0}^{M-1} c_j\,x[n-j], \qquad 0 \le K < \infty,\quad 1 \le M < \infty .
> $$
> - $K$ **feedback** (output) terms, coefficients $b_1, \dots, b_K$ at delays $1, \dots, K$.
> - $M$ **input** terms, coefficients $c_0, \dots, c_{M-1}$ at delays $0, \dots, M-1$.

- **Zero initial conditions** ("at rest"): $y[n] = 0$ before the input arrives; in hardware, clear the memory first. Assumed throughout.
- All shifts non-negative ⇒ no future values ⇒ **causal**. Non-causal LCCDEs have terms like $x[n+2]$ or $y[n+1]$.

> [!trap] Sign conventions and FIR/IIR
> - From [[2-z-transform/09-transfer-functions|Lecture 9]] on (and in exam keys, SciPy): $y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k]$.
> - So $a_k = -\,b_k^{(\text{L5})}$ and $b_k^{(\text{L9})} = c_k^{(\text{L5})}$: in Lecture 5 "$b$" is feedback, in Lecture 9 feedforward.
> - $y[n] = \tfrac12 y[n-1] + x[n]$: $b_1 = +\tfrac12$ here, $a_1 = -\tfrac12$ and `lfilter([1], [1, -0.5], x)` there.
> - "Feedback ⇒ IIR" can fail when a pole is cancelled: the recursive moving average below is FIR ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).

### 1.1 Finite impulse response systems

$K = 0$ ⇒ **FIR**:

$$
h[n] = \sum_{j=0}^{M-1} c_j\,\delta[n-j] = \{\underset{\uparrow}{c_0},\ c_1,\ \dots,\ c_{M-1}\}.
$$

Finite length; usable directly in the convolution sum ([[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]). FIR is always BIBO stable ($\sum\lvert h[n]\rvert$ is a finite sum).

Length-$L$ **moving average**:

$$
y[n] = \frac1L\sum_{i=0}^{L-1} x[n-i], \qquad h[n] = \frac1L\big(u[n] - u[n-L]\big).
$$

Recursive form (reuses the sum at $n-1$): two additions per sample instead of $L$:

$$
y[n] = y[n-1] + \frac1L\big(x[n] - x[n-L]\big).
$$

### 1.2 Infinite impulse response systems

$K > 0$ ⇒ **IIR**: feedback keeps the output going after the input stops. $y[n] = \tfrac12 y[n-1] + x[n]$, $x[n] = \delta[n]$, at rest:

| $n$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $y[n] = \tfrac12 y[n-1] + x[n]$ | 1 | $\tfrac12$ | $\tfrac14$ | $\tfrac18$ | $\tfrac1{16}$ |

$$
h[n] = \Big\{\underset{\uparrow}{1},\ \tfrac12,\ \tfrac14,\ \tfrac18,\ \tfrac1{16},\ \dots\Big\} = \left(\tfrac12\right)^n u[n].
$$

Infinite $h$: no convolution sum in practice, but the recursion runs easily in code or hardware.

> [!question] Slides Example 1: $h[n]$ of $y[n] = \tfrac13 y[n-1] + x[n]$

> [!success]- Answer
> $h[0] = \tfrac13 h[-1] + \delta[0] = 1$, $h[1] = \tfrac13$, $h[2] = \tfrac19$, … so $h[n] = (\tfrac13)^n u[n]$. In general $y[n] = a\,y[n-1] + x[n]$ has $h[n] = a^n u[n]$.

> [!recipe] Impulse response of a first-order recursion with several input terms (linearity + time-invariance)
> 1. **Feedback part:** replace the input terms by one input $z[n]$: $\hat y[n] = b_1\,\hat y[n-1] + z[n]$, so $\hat h[n] = b_1^{\,n}\,u[n]$.
> 2. **Input part:** with $x[n] = \delta[n]$, $z[n] = \sum_j c_j\,\delta[n-j]$.
> 3. **Superpose:** $h[n] = z[n] * \hat h[n] = \sum_j c_j\,\hat h[n-j]$; shift the step with the exponential.

> [!question] Exercise 1 (notes): $h[n]$ of $y[n] = \tfrac14 y[n-1] - x[n] + \tfrac12 x[n-2]$

> [!success]- Answer
> $\hat h[n] = (\tfrac14)^n u[n]$; $z[n] = -\delta[n] + \tfrac12\delta[n-2]$:
> $$
> h[n] = -\hat h[n] + \tfrac12\hat h[n-2] = -\left(\tfrac14\right)^n u[n] + \tfrac12\left(\tfrac14\right)^{n-2} u[n-2].
> $$
> First samples: $-1,\ -\tfrac14,\ \tfrac{7}{16},\ \tfrac{7}{64},\ \dots$

> [!question] Slides Example 2: $h[n]$ of $y[n] = \tfrac13 y[n-1] + x[n] - 3x[n-1] + x[n-2]$

> [!success]- Answer
> $\hat h[n] = (\tfrac13)^n u[n]$, $z[n] = \delta[n] - 3\delta[n-1] + \delta[n-2]$:
> $$
> h[n] = \left(\tfrac13\right)^n u[n] - 3\left(\tfrac13\right)^{n-1}u[n-1] + \left(\tfrac13\right)^{n-2}u[n-2].
> $$
> $h[0] = 1$, $h[1] = \tfrac13 - 3 = -\tfrac83$; for $n \ge 2$: $(\tfrac13)^n(1 - 9 + 9) = (\tfrac13)^n$, so $h[2] = \tfrac19$, $h[3] = \tfrac1{27}$, …

Second-order feedback needs the z-transform and partial fractions ([[2-z-transform/09-transfer-functions|Lecture 9]]); until then, iterate by hand.

## 2. Block diagrams

- **Delay** $z^{-1}$: $x[n] \to x[n-1]$ (notation explained in [[2-z-transform/06-the-z-transform|Lecture 6]]).
- **Gain** $c$: $x[n] \to c\,x[n]$.
- **Adder**: $x_1[n], x_2[n] \to x_1[n] + x_2[n]$.

Notes example, **direct form I** (one delay line for inputs, one for outputs): $y[n] = \tfrac12 y[n-1] + \tfrac12 y[n-2] + 3x[n] - 2x[n-1] + x[n-2]$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img" aria-label="Direct form I block diagram of y[n] = 1/2 y[n-1] + 1/2 y[n-2] + 3x[n] - 2x[n-1] + x[n-2]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="14.0" y="61.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="50.0" y1="56.0" x2="96.0" y2="56.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="96.0" cy="56.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><line x1="96.0" y1="56.0" x2="156.0" y2="56.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="156.0" y="43.0" width="40.0" height="26.0" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.4"/><text x="176.0" y="61.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">3</text><line x1="196.0" y1="56.0" x2="242.0" y2="56.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="249.0,56.0 242.0,52.1 242.0,59.9" fill="currentColor"/><circle cx="262.0" cy="56.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="256.0" y1="56.0" x2="268.0" y2="56.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="262.0" y1="50.0" x2="262.0" y2="62.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="275.0" y1="56.0" x2="362.0" y2="56.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="369.0,56.0 362.0,52.1 362.0,59.9" fill="currentColor"/><circle cx="382.0" cy="56.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="376.0" y1="56.0" x2="388.0" y2="56.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="382.0" y1="50.0" x2="382.0" y2="62.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="395.0" y1="56.0" x2="548.0" y2="56.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="548.0" cy="56.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><line x1="548.0" y1="56.0" x2="599.0" y2="56.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="606.0,56.0 599.0,52.1 599.0,59.9" fill="currentColor"/><text x="612.0" y="61.0" text-anchor="start" fill="var(--accent2)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">y[n]</text><line x1="96.0" y1="56.0" x2="96.0" y2="97.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="74.0" y="97.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="96.0" y="116.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="96.0" y1="125.0" x2="96.0" y2="156.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="96.0,162.0 92.7,156.0 99.3,156.0" fill="currentColor"/><circle cx="96.0" cy="166.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="86.0" y="186.0" text-anchor="end" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n−1]</text><line x1="96.0" y1="166.0" x2="156.0" y2="166.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="156.0" y="153.0" width="40.0" height="26.0" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.4"/><text x="176.0" y="171.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">−2</text><line x1="96.0" y1="166.0" x2="96.0" y2="207.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="74.0" y="207.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="96.0" y="226.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="96.0" y1="235.0" x2="96.0" y2="266.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="96.0,272.0 92.7,266.0 99.3,266.0" fill="currentColor"/><circle cx="96.0" cy="276.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="86.0" y="296.0" text-anchor="end" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n−2]</text><line x1="96.0" y1="276.0" x2="156.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="156.0" y="263.0" width="40.0" height="26.0" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.4"/><text x="176.0" y="281.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">1</text><line x1="196.0" y1="166.0" x2="242.0" y2="166.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="249.0,166.0 242.0,162.2 242.0,169.8" fill="currentColor"/><circle cx="262.0" cy="166.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="256.0" y1="166.0" x2="268.0" y2="166.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="262.0" y1="160.0" x2="262.0" y2="172.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="196.0" y1="276.0" x2="262.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><line x1="262.0" y1="276.0" x2="262.0" y2="185.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,179.0 258.7,185.0 265.3,185.0" fill="currentColor"/><line x1="262.0" y1="153.0" x2="262.0" y2="75.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,69.0 258.7,75.0 265.3,75.0" fill="currentColor"/><line x1="548.0" y1="56.0" x2="548.0" y2="97.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="526.0" y="97.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="548.0" y="116.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="548.0" y1="125.0" x2="548.0" y2="156.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="548.0,162.0 544.7,156.0 551.3,156.0" fill="currentColor"/><circle cx="548.0" cy="166.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="558.0" y="186.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n−1]</text><line x1="548.0" y1="166.0" x2="488.0" y2="166.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="448.0" y="153.0" width="40.0" height="26.0" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="var(--accent2)" stroke-width="1.4"/><text x="468.0" y="171.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">½</text><line x1="548.0" y1="166.0" x2="548.0" y2="207.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="526.0" y="207.0" width="44.0" height="28.0" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="548.0" y="226.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic">z<tspan dy="-6" style="font-size:10px">−1</tspan></text><line x1="548.0" y1="235.0" x2="548.0" y2="266.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="548.0,272.0 544.7,266.0 551.3,266.0" fill="currentColor"/><circle cx="548.0" cy="276.0" r="3.6" fill="currentColor" stroke="none" stroke-width="1.4"/><text x="558.0" y="296.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n−2]</text><line x1="548.0" y1="276.0" x2="488.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="448.0" y="263.0" width="40.0" height="26.0" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="var(--accent2)" stroke-width="1.4"/><text x="468.0" y="281.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">½</text><line x1="448.0" y1="166.0" x2="402.0" y2="166.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="395.0,166.0 402.0,162.2 402.0,169.8" fill="currentColor"/><circle cx="382.0" cy="166.0" r="13.0" fill="var(--paper, none)" stroke="currentColor" stroke-width="1.5"/><line x1="376.0" y1="166.0" x2="388.0" y2="166.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="382.0" y1="160.0" x2="382.0" y2="172.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="448.0" y1="276.0" x2="382.0" y2="276.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><line x1="382.0" y1="276.0" x2="382.0" y2="185.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="382.0,179.0 378.7,185.0 385.3,185.0" fill="currentColor"/><line x1="382.0" y1="153.0" x2="382.0" y2="75.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="382.0,69.0 378.7,75.0 385.3,75.0" fill="currentColor"/><text x="179.0" y="318.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">feedforward: current and past inputs</text><text x="465.0" y="318.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12.5px;font-weight:600;">feedback: past outputs</text><text x="320.0" y="346.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">y[n] = ½ y[n−1] + ½ y[n−2] + 3x[n] − 2x[n−1] + x[n−2]</text></svg><figcaption><strong>Direct form I (notes Fig. 4).</strong> The left delay line feeds past inputs through the gains 3, −2, 1; the right one feeds past outputs back through the gains ½, ½.</figcaption></figure>

> [!recipe] Block diagram ↔ LCCDE
> - **LCCDE → direct form I:** delay line on $x$ with gain $c_j$ on $x[n-j]$; delay line on $y$ with gain $b_i$ on $y[n-i]$; sum all into $y[n]$.
> - **Diagram → LCCDE:** label every delay and adder output, one equation per adder, eliminate internal labels. A gain on a delayed $y$ is feedback: same sign in Lecture 5 form, flipped in Lecture 9 form.
> - Other forms (direct form II, cascades) come later in the course.

> [!exam] On the exams
> LCCDEs return in Lecture 9 problems (LCCDE ↔ $H(z)$ ↔ response), written in the Lecture 9 sign convention. Also tested: FIR ⇒ stable; an LCCDE alone does not fix causality; recursions run backwards. Block diagrams: not tested so far.
> [[exams/midterm-1/past-exams/spring-2021|SP2021 #6]] · [[exams/midterm-1/past-exams/fall-2025|FA2025 #4, #6, #7(b)]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(a), #1(e), #10]] · [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]] · [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]]

## Related

[[concepts/lccde|LCCDE]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/block-diagram|Block diagrams]] · [[concepts/impulse-response|Impulse response]] · [[concepts/transfer-function|Transfer function]] · [[demos/difference-equation-simulator|difference-equation simulator]] · [[supplements/demo-notebooks|course demo notebooks]] · [[homework/hw2|HW2]]

### Sources for this page

Snyder, Lecture 5 notes (§1 LCCDEs, §1.1 FIR, §1.2 IIR with Exercise 1, §2 block diagrams, Fig. 4) and slides (Examples 1–2); past exams above.
