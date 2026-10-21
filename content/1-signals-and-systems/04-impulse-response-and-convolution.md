---
title: "Lecture 4 — Impulse response and convolution"
description: "h[n] = T(δ[n]); signals as sums of shifted impulses; LTI ⇔ convolution ⇔ described by h; flip, shift, multiply, add; properties, causality and stability from h; table, matrix and sum methods; finite, infinite and mixed cases."
tags: [lecture, midterm-1, systems, convolution]
lecture: 4
---

*Lecture 4 · Mon Aug 31, 2026 · notes + slides "Convolution and impulse response" · prev: [[1-signals-and-systems/03-system-properties|Lecture 3]] · next: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]]*

> [!abstract] In one breath
> - Impulse response $h[n] = T(\delta[n])$; every signal is $\sum_k x[k]\,\delta[n-k]$.
> - LTI ⇔ output is $y = x * h = \sum_k x[k]\,h[n-k]$ ⇔ $h$ describes the system.
> - Causal ⇔ $h[n] = 0$ for $n < 0$; stable ⇔ $\sum\lvert h[n]\rvert < \infty$.

## 1. Impulse response

> [!key] Impulse response (eq. 1)
> $$
> h[n] = T(\delta[n]).
> $$

- Difference system $y_1[n] = x[n] - x[n-1]$ (Lecture 3): $h_1[n] = \delta[n] - \delta[n-1]$.
- Width-3 median $y_2[n] = \operatorname{median}\{x[n], x[n-1], x[n-2]\}$: $h_2[n] = 0$ (every window holds one $1$, two $0$s).

### 1.1 Signals as linear combination of impulses

Each sample is an impulse at $k$ with height $x[k]$. Slide 4:
$$
\begin{aligned}
x[n] &= \cos\!\left(\tfrac{\pi}{4}n\right)\big(u[n] - u[n-8]\big) = \Big\{\underset{\uparrow}{1},\ \tfrac{\sqrt2}{2},\ 0,\ -\tfrac{\sqrt2}{2},\ -1,\ -\tfrac{\sqrt2}{2},\ 0,\ \tfrac{\sqrt2}{2}\Big\} \\
&= \delta[n] + \tfrac{\sqrt2}{2}\delta[n-1] - \tfrac{\sqrt2}{2}\delta[n-3] - \delta[n-4] - \tfrac{\sqrt2}{2}\delta[n-5] + \tfrac{\sqrt2}{2}\delta[n-7].
\end{aligned}
$$
Notes (eq. 5), sine version: $\sin(\tfrac{\pi}{4}n)\big(u[n]-u[n-8]\big) = \tfrac{\sqrt2}{2}\delta[n-1] + \delta[n-2] + \tfrac{\sqrt2}{2}\delta[n-3] - \tfrac{\sqrt2}{2}\delta[n-5] - \delta[n-6] - \tfrac{\sqrt2}{2}\delta[n-7]$.

> [!key] Sifting (eq. 6)
> $$
> x[n] = \sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k].
> $$
> At fixed $n$ only $k = n$ survives: $x[3] = \cdots + x[3]\delta[0] + \cdots = x[3]$ (the notes' "$= \delta[3]$" is a [[0-toolkit/05-errata|typo]]).

### 1.2 System response for LTI systems

| input | output | property |
|---|---|---|
| $\delta[n]$ | $h[n]$ | definition |
| $a\,\delta[n]$ | $a\,h[n]$ | homogeneity |
| $\delta[n-k]$ | $h[n-k]$ | time-invariance |
| $\delta[n] + \delta[n-k]$ | $h[n] + h[n-k]$ | additivity |
| $\sum_k x[k]\,\delta[n-k]$ | $\sum_k x[k]\,h[n-k]$ | all three |

> [!key] LTI response (eq. 7) and the "if and only if" triangle (Fig. 1)
> $$
> y[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k], \qquad \forall n.
> $$
> **LTI** ⇔ output is a **convolution** with some $h$ ⇔ **fully described by $h$** (output known for every input).

- Difference system: LTI, so $x * (\delta[n] - \delta[n-1])$ reproduces it.
- Median: nonlinear, so $h_2 = 0$ says nothing about other inputs.

## 2. Convolution

> [!key] Convolution (eq. 8)
> $$
> x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k] = \sum_{k=-\infty}^{\infty} h[k]\,x[n-k] = h[n] * x[n].
> $$
> Commutative by $m = n - k$.

For each $n$:
1. **Flip** one signal: $h[-k]$.
2. **Shift** right by $n$: $h[-(k-n)] = h[n-k]$.
3. **Multiply**: $z_n[k] = x[k]\,h[n-k]$.
4. **Sum**: $y[n] = \sum_k z_n[k]$.

Repeat 2–4 for every $n$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 548" width="640" height="548" role="img" aria-label="Flip and shift: computing y[2] for the notes' example by overlaying x[k] and h[2-k]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="10.0" y1="100.0" x2="460.0" y2="100.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,100.0 455.0,96.2 455.0,103.8" fill="currentColor"/><text x="460.0" y="118.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="32.0" x2="150.6" y2="108.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="97.0" x2="30.0" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="97.0" x2="70.2" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="97.0" x2="110.4" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="97.0" x2="150.6" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="97.0" x2="190.8" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="97.0" x2="231.0" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="97.0" x2="271.2" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="97.0" x2="311.4" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="97.0" x2="351.6" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="97.0" x2="391.8" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="97.0" x2="432.0" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">x[k] = {3, 1, 0, 3, 1, 1},  x[0] = 3</text><circle cx="30.0" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="110.4" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="150.6" y1="100.0" x2="150.6" y2="46.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="150.6" cy="46.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="150.6" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">3</text><line x1="190.8" y1="100.0" x2="190.8" y2="82.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="82.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="190.8" y="73.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><circle cx="231.0" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="271.2" y1="100.0" x2="271.2" y2="46.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="271.2" cy="46.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="271.2" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">3</text><line x1="311.4" y1="100.0" x2="311.4" y2="82.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="311.4" cy="82.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="311.4" y="73.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><line x1="351.6" y1="100.0" x2="351.6" y2="82.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="351.6" cy="82.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="351.6" y="73.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><circle cx="391.8" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="10.0" y1="214.0" x2="460.0" y2="214.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,214.0 455.0,210.2 455.0,217.8" fill="currentColor"/><text x="460.0" y="232.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="164.0" x2="150.6" y2="240.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="211.0" x2="30.0" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="211.0" x2="70.2" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="211.0" x2="110.4" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="211.0" x2="150.6" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="207.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="211.0" x2="190.8" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="211.0" x2="231.0" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="211.0" x2="271.2" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="211.0" x2="311.4" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="211.0" x2="351.6" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="211.0" x2="391.8" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="211.0" x2="432.0" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="150.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">h[k] = {2, −1, 1},  h[0] = −1</text><circle cx="30.0" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="110.4" y1="214.0" x2="110.4" y2="178.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="110.4" cy="178.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="110.4" y="169.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">2</text><line x1="150.6" y1="214.0" x2="150.6" y2="232.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="150.6" cy="232.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="150.6" y="250.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−1</text><line x1="190.8" y1="214.0" x2="190.8" y2="196.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="196.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="190.8" y="187.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><circle cx="231.0" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="271.2" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="311.4" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="351.6" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="391.8" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="10.0" y1="328.0" x2="460.0" y2="328.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,328.0 455.0,324.1 455.0,331.9" fill="currentColor"/><text x="460.0" y="346.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="278.0" x2="150.6" y2="354.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="325.0" x2="30.0" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="325.0" x2="70.2" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="325.0" x2="110.4" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="325.0" x2="150.6" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="321.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="325.0" x2="190.8" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="325.0" x2="231.0" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="325.0" x2="271.2" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="325.0" x2="311.4" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="325.0" x2="351.6" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="325.0" x2="391.8" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="325.0" x2="432.0" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="264.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">① flip:  h[−k]</text><circle cx="30.0" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="110.4" y1="328.0" x2="110.4" y2="310.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="110.4" cy="310.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="110.4" y="301.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><line x1="150.6" y1="328.0" x2="150.6" y2="346.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="150.6" cy="346.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="150.6" y="364.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−1</text><line x1="190.8" y1="328.0" x2="190.8" y2="292.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="292.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="190.8" y="283.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">2</text><circle cx="231.0" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="271.2" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="311.4" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="351.6" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="391.8" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="10.0" y1="470.0" x2="460.0" y2="470.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,470.0 455.0,466.1 455.0,473.9" fill="currentColor"/><text x="460.0" y="488.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="402.0" x2="150.6" y2="478.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="467.0" x2="30.0" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="467.0" x2="70.2" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="467.0" x2="110.4" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="467.0" x2="150.6" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="467.0" x2="190.8" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="467.0" x2="231.0" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="463.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="467.0" x2="271.2" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="467.0" x2="311.4" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="467.0" x2="351.6" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="467.0" x2="391.8" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="467.0" x2="432.0" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="390.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">② shift by n = 2:  h[2−k], laid over x[k]</text><circle cx="30.0" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="110.4" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="150.6" y1="470.0" x2="150.6" y2="416.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="150.6" cy="416.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><line x1="190.8" y1="470.0" x2="190.8" y2="452.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="190.8" cy="452.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><circle cx="231.0" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="271.2" y1="470.0" x2="271.2" y2="416.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="271.2" cy="416.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><line x1="311.4" y1="470.0" x2="311.4" y2="452.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="311.4" cy="452.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><line x1="351.6" y1="470.0" x2="351.6" y2="452.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="351.6" cy="452.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><circle cx="391.8" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="190.8" y1="470.0" x2="190.8" y2="452.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="452.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="199.8" y="456.0" text-anchor="start" fill="currentColor" style="font-size:12px;">1</text><line x1="231.0" y1="470.0" x2="231.0" y2="488.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="231.0" cy="488.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="240.0" y="492.0" text-anchor="start" fill="currentColor" style="font-size:12px;">−1</text><line x1="271.2" y1="470.0" x2="271.2" y2="434.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="271.2" cy="434.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="280.2" y="438.0" text-anchor="start" fill="currentColor" style="font-size:12px;">2</text><rect x="174.7" y="404.0" width="112.6" height="96.0" rx="0" fill="var(--hi)" fill-opacity="0.08" stroke="none" stroke-width="1.4"/><text x="478.0" y="176.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">the sequence we</text><text x="478.0" y="192.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">slide (the shorter one)</text><text x="478.0" y="290.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">mirror image about k = 0:</text><text x="478.0" y="306.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">h[1] now sits at k = −1</text><text x="478.0" y="414.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">③ multiply where both</text><text x="478.0" y="430.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">are nonzero, ④ add:</text><text x="478.0" y="452.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">k = 1:  1 · 1 = 1</text><text x="478.0" y="470.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">k = 2:  0 · (−1) = 0</text><text x="478.0" y="488.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">k = 3:  3 · 2 = 6</text><text x="478.0" y="516.0" text-anchor="start" fill="var(--accent)" style="font-size:15px;font-weight:700;">y[2] = 7</text><circle cx="26.0" cy="536.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><text x="36.0" y="540.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;" opacity="0.85">x[k]</text><circle cx="90.0" cy="536.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="100.0" y="540.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;" opacity="0.85">h[2−k]</text></svg><figcaption><strong>y[2] for the notes' example: flip h, slide it right by 2, multiply with x[k], add: 1·1 + 0·(−1) + 3·2 = 7.</strong> Sliding by n = −1, …, 6 gives {6, −1, 2, 7, −1, 4, 0, 1}.</figcaption></figure>

### 2.1 Properties of convolution and impulse response

> [!key] Properties (eqs. 9–17)
> - **Commutative:** $x * h_1 * h_2 = x * h_2 * h_1 = h_1 * h_2 * x = \cdots$ (cascade order irrelevant).
> - **Associative:** $(x * h_1) * h_2 = x * (h_1 * h_2)$.
> - **Distributive:** $x * (h_1 + h_2) = x * h_1 + x * h_2$.
> - **Identity:** $x[n] * \delta[n] = x[n]$; also $x[n] * \delta[n-k] = x[n-k]$.
> - **Causality:** LTI causal ⇔ $h[n] = 0$ for $n < 0$.
> - **Stability:** LTI BIBO stable ⇔ $\sum_{n=-\infty}^{\infty} \lvert h[n]\rvert < \infty$.
> - **Start, end, length:** $x$ on $[n_s, n_e]$ (length $N$), $h$ on $[m_s, m_e]$ (length $M$) ⇒ $y$ on $[n_s + m_s,\ n_e + m_e]$, length $N + M - 1$.

> [!question] Lecture exercise: prove absolute summability ⇒ BIBO stable.

> [!success]- Answer
> $S = \sum_k \lvert h[k]\rvert < \infty$, $\lvert x[n]\rvert < \beta$:
> $$
> \lvert y[n]\rvert = \Big\lvert \sum_k h[k]\,x[n-k] \Big\rvert \le \sum_k \lvert h[k]\rvert\,\lvert x[n-k]\rvert < \beta\,S \quad\text{for every } n .
> $$
> Converse (real $h$): if $\sum_k \lvert h[k]\rvert = \infty$, the bounded input $x[n] = \operatorname{sgn}(h[-n])$ gives $y[0] = \sum_k \lvert h[k]\rvert = \infty$.

### 2.2 Computing the convolution of two signals

#### 2.2.1 Shift-and-overlap method

$x[n] = \{\underset{\uparrow}{3}, 1, 0, 3, 1, 1\}$, $h[n] = \{2, \underset{\uparrow}{-1}, 1\}$. Support first: start $0 + (-1) = -1$, end $5 + 1 = 6$, length $6 + 3 - 1 = 8$. Flip the shorter; blanks are $0$ (zero extension). Table 1:

| | $k=-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | output |
|---|---|---|---|---|---|---|---|---|---|
| $x[k]$ | | | 3 | 1 | 0 | 3 | 1 | 1 | |
| $h[-1-k]$ | 1 | −1 | 2 | | | | | | $y[-1] = 2\cdot 3 = 6$ |
| $h[-k]$ | | 1 | −1 | 2 | | | | | $y[0] = -3 + 2 = -1$ |
| $h[1-k]$ | | | 1 | −1 | 2 | | | | $y[1] = 3 - 1 + 0 = 2$ |
| $h[2-k]$ | | | | 1 | −1 | 2 | | | $y[2] = 1 - 0 + 6 = 7$ |
| $h[3-k]$ | | | | | 1 | −1 | 2 | | $y[3] = 0 - 3 + 2 = -1$ |
| $h[4-k]$ | | | | | | 1 | −1 | 2 | $y[4] = 3 - 1 + 2 = 4$ |
| $h[5-k]$ | | | | | | | 1 | −1 | $y[5] = 1 - 1 = 0$ |
| $h[6-k]$ | | | | | | | | 1 | $y[6] = 1$ |

$$
y[n] = \{6,\ \underset{\uparrow}{-1},\ 2,\ 7,\ -1,\ 4,\ 0,\ 1\}.
$$

Quick check: $\sum_n y[n] = \big(\sum_n x[n]\big)\big(\sum_n h[n]\big)$, here $18 = 9 \cdot 2$; it does not check the arrow.

> [!question] Slide 10: convolve $x[n] = \{\underset{\uparrow}{1}, 2, 0, -4, -1\}$ with $h[n] = \{-2, \underset{\uparrow}{0}, 1\}$.

> [!success]- Answer
> Start $0 + (-1) = -1$, length $5 + 3 - 1 = 7$: $y[n] = \{-2,\ \underset{\uparrow}{-4},\ 1,\ 10,\ 2,\ -4,\ -1\}$. Sum check: $-2 \cdot (-1) = 2$ ✓.

#### 2.2.2 Matrix-vector multiplication

Columns of $\mathbf{H}$ are shifted copies of $h$ (Toeplitz: constant diagonals); each row is one flipped, shifted $h$ (eqs. 18–20):
$$
\underbrace{\begin{bmatrix} 6\\ -1\\ 2\\ 7\\ -1\\ 4\\ 0\\ 1 \end{bmatrix}}_{\mathbf{y}}
=
\underbrace{\begin{bmatrix}
2 & 0 & 0 & 0 & 0 & 0\\
-1 & 2 & 0 & 0 & 0 & 0\\
1 & -1 & 2 & 0 & 0 & 0\\
0 & 1 & -1 & 2 & 0 & 0\\
0 & 0 & 1 & -1 & 2 & 0\\
0 & 0 & 0 & 1 & -1 & 2\\
0 & 0 & 0 & 0 & 1 & -1\\
0 & 0 & 0 & 0 & 0 & 1
\end{bmatrix}}_{\mathbf{H}\ (8\times 6)}
\underbrace{\begin{bmatrix} 3\\ 1\\ 0\\ 3\\ 1\\ 1 \end{bmatrix}}_{\mathbf{x}}
$$

- Or $\mathbf{y} = \mathbf{X}\mathbf{h}$ with an $8\times 3$ matrix from $x$ (eq. 21).
- The matrix gives values only: label the first row $n = n_s + m_s = -1$ yourself.

#### 2.2.3 Directly applying the convolution sum

Steps $u[k]$ ⇒ $k \ge 0$, $u[n-k]$ ⇒ $k \le n$; no surviving $k$ ⇒ $y[n] = 0$. Then the geometric sum (eq. 22) $\sum_{k=0}^{n} a^k = \frac{1 - a^{n+1}}{1 - a}$ ([[0-toolkit/02-geometric-series|geometric series]]).

**Notes:** $x[n] = u[n]$, $h[n] = (-\tfrac34)^n u[n]$:
$$
\begin{aligned}
y[n] &= \sum_{k} \left(-\tfrac34\right)^k u[k]\,u[n-k] = \sum_{k=0}^{n}\left(-\tfrac34\right)^k\\
&= \frac{1 - (-\frac34)^{n+1}}{\frac74} = \left(\frac47 - \frac47\left(-\frac34\right)^{n+1}\right)u[n].
\end{aligned}
$$

> [!question] Slide 12: $x[n] = (\tfrac12)^n u[n]$, $h[n] = (-\tfrac34)^n u[n]$.

> [!success]- Answer
> For $n \ge 0$, factor out $(-\frac34)^n$; $(\frac12)^k(-\frac34)^{-k} = (-\frac23)^k$:
> $$
> \begin{aligned}
> y[n] &= \left(-\tfrac34\right)^n \sum_{k=0}^{n} \left(-\tfrac23\right)^k = \frac35\left(-\frac34\right)^n\left(1 - \left(-\frac23\right)^{n+1}\right)u[n] \\
> &= \left[\frac35\left(-\frac34\right)^n + \frac25\left(\frac12\right)^n\right]u[n].
> \end{aligned}
> $$
> Check: $y[0] = 1$, $y[1] = -\tfrac34 + \tfrac12 = -\tfrac14$ ✓.

### 2.3 Cases for computing convolution

1. Two finite: table or matrix.
2. Two infinite: the convolution sum.
3. Finite with infinite: write the finite one as impulses; $h[n] * a\,\delta[n-k] = a\,h[n-k]$.

**Notes (eqs. 23–24):** $x[n] = \{\underset{\uparrow}{1}, 0, 2, 0, -3\} = \delta[n] + 2\delta[n-2] - 3\delta[n-4]$, $h[n] = \sin^3(\frac{\pi}{4}n)\,u[n]$:
$$
\begin{aligned}
y[n] &= h[n] + 2h[n-2] - 3h[n-4] \\
&= \sin^3\!\left(\tfrac{\pi}{4}n\right)u[n] + 2\sin^3\!\left(\tfrac{\pi}{4}(n-2)\right)u[n-2] - 3\sin^3\!\left(\tfrac{\pi}{4}(n-4)\right)u[n-4].
\end{aligned}
$$

> [!question] Slides 14–16: (a) $x[n] = \{-2, 0, \underset{\uparrow}{0}, 3, 0, 1\}$, $h[n] = e^{-n}u[n]$; (b) $x[n] = \{-3, 6, 2, \underset{\uparrow}{0}, 1, 1\}$, $h[n] = \{1, \underset{\uparrow}{-1}\}$; (c) $x[n] = u[n]$, $h[n] = (\tfrac23)^{n-2}u[n-4]$.

> [!success]- Answers
> (a) $x = -2\delta[n+2] + 3\delta[n-1] + \delta[n-3]$: $y[n] = -2e^{-(n+2)}u[n+2] + 3e^{-(n-1)}u[n-1] + e^{-(n-3)}u[n-3]$.
> (b) Start $-3 + (-1) = -4$: $y[n] = \{-3,\ 9,\ -4,\ -2,\ \underset{\uparrow}{1},\ 0,\ -1\}$. Sum check: $7 \cdot 0 = 0$ ✓.
> (c) $u[k-4]\,u[n-k]$ keeps $4 \le k \le n$; $y[n] = 0$ for $n < 4$; with $m = k - 4$:
> $$
> y[n] = \left(\tfrac23\right)^{2}\sum_{m=0}^{n-4}\left(\tfrac23\right)^{m} = \frac49\cdot\frac{1-(\frac23)^{n-3}}{\frac13} = \frac43\left(1 - \left(\frac23\right)^{n-3}\right)u[n-4].
> $$
> Check: $y[4] = \tfrac49 = h[4]$ ✓.

> [!trap] Convolution traps
> - $h[n]$ describes a system only if it is LTI.
> - Bounded $h$ can still be unstable: $h = u[n]$. Finite-length $h$ is always stable.
> - Write the start index $n_s + m_s$ first; the matrix gives values only.
> - $h[n-4]$ shifts **every** $n$, including the step: $u[n-4]$, not $u[n]$.

> [!exam] Where Lecture 4 shows up (densest lecture on Midterm 1)
> Finite convolution on 7 of 7 exams (points lost on the arrow); infinite or mixed on 5 of 7 (closed form); finding $h$ from input–output pairs on 7 of 7; LTI-triangle and stability T/F.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(a)(b)(f), #3]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #3, #4]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(a), #3, #4]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(d)(e), #3, #4]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(a), #3, #4]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #2]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(b)(e), #3, #4]]
> Recipes: [[problems/finite-length-convolution|finite]] · [[problems/infinite-length-convolution|infinite]] · [[problems/finding-h-from-input-output-pairs|finding h]] · [[exams/midterm-1/true-false-bank|T/F bank]]

## Related

[[concepts/impulse-response|impulse response]] · [[concepts/convolution|convolution]] · [[concepts/lti-system|LTI system]] · [[concepts/step-response|step response]] · [[concepts/causality|causality]] · [[concepts/bibo-stability|BIBO stability]] · [[demos/convolution-explorer|convolution explorer]] · [[homework/hw2|HW2]] · unit: [[1-signals-and-systems/index|Unit 1]]

### Sources for this page

Snyder, Lecture 4 notes (§1–2.3, Fig. 1, Table 1) and slides with in-class annotations (Aug 31, 2026); past exams above.
