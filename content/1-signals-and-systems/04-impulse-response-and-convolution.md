---
title: "Lecture 4 — Impulse response and convolution"
description: "The impulse response h[n] = T(δ[n]); why an LTI system's output is x * h (and why no other system's is); flip, shift, multiply, add; the table and matrix methods with start-index bookkeeping; infinite and mixed convolutions; causality and stability read off h[n]; and finding h from input–output pairs."
tags: [lecture, midterm-1, systems, convolution]
lecture: 4
---

*Lecture 4 · Mon Aug 31, 2026 · notes + slides "Convolution and impulse response" · prev: [[1-signals-and-systems/03-system-properties|Lecture 3]] · next: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]]*

> [!abstract] In one breath
> Feed a system the unit impulse and record what comes out: that is its **impulse response** $h[n] = T(\delta[n])$. Every input is a weighted sum of shifted impulses, $x[n] = \sum_k x[k]\,\delta[n-k]$, so if the system is linear *and* time-invariant its output is the same weighted sum of shifted impulse responses: the **convolution** $y[n] = \sum_k x[k]\,h[n-k] = x[n] * h[n]$. For an LTI system, $h[n]$ *is* the system: causal $\Leftrightarrow h[n] = 0$ for $n < 0$, BIBO stable $\Leftrightarrow \sum_n \lvert h[n]\rvert < \infty$. For a system that is not LTI, $h[n]$ tells you almost nothing. Computing convolutions (finite: table or matrix; infinite: the sum plus a geometric series; mixed: split into impulses) and working backwards from input–output pairs to $h$ are on every past Midterm 1.

## 1. The impulse response

> [!key] Impulse response
> The impulse response of a discrete-time system $T$ is its output when the input is the unit impulse (Kronecker delta):
> $$
> h[n] = T(\delta[n]).
> $$

Two systems from [[1-signals-and-systems/03-system-properties|Lecture 3]]:

- The difference system $y_1[n] = x[n] - x[n-1]$ has $h_1[n] = \delta[n] - \delta[n-1]$.
- The 3-point median $y_2[n] = \operatorname{median}\{x[n], x[n-1], x[n-2]\}$ has $h_2[n] = 0$: every window of $\delta[n]$ contains one $1$ and two $0$s, and the median of $\{1, 0, 0\}$ is $0$.

Keep $h_2 = 0$ in mind. The median filter is obviously not the "output is always zero" system, so for *this* system the impulse response is useless. §3 explains why.

## 2. Every signal is a sum of shifted impulses

Each sample of $x[n]$ is an impulse placed at $n = k$ with height $x[k]$. The slides' example, one period of a cosine:

$$
x[n] = \cos\!\left(\tfrac{\pi}{4}n\right)\big(u[n] - u[n-8]\big) = \Big\{\underset{\uparrow}{1},\ \tfrac{\sqrt2}{2},\ 0,\ -\tfrac{\sqrt2}{2},\ -1,\ -\tfrac{\sqrt2}{2},\ 0,\ \tfrac{\sqrt2}{2}\Big\}
= \delta[n] + \tfrac{\sqrt2}{2}\delta[n-1] - \tfrac{\sqrt2}{2}\delta[n-3] - \delta[n-4] - \tfrac{\sqrt2}{2}\delta[n-5] + \tfrac{\sqrt2}{2}\delta[n-7].
$$

In general (the **sifting** identity):

$$
x[n] = \sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k].
$$

At any fixed $n$ only the term with $k = n$ survives. For $n = 3$: $\sum_k x[k]\,\delta[3-k] = \cdots + x[2]\delta[1] + x[3]\delta[0] + x[4]\delta[-1] + \cdots = x[3]$. (The notes end this line with "$= \delta[3]$"; it should read $x[3]$.)

## 3. LTI systems: the output is a convolution

Build the response to an arbitrary input one step at a time, exactly as the slides do:

| input | output | property used |
|---|---|---|
| $\delta[n]$ | $h[n]$ | definition |
| $a\,\delta[n]$ | $a\,h[n]$ | homogeneity |
| $\delta[n-k]$ | $h[n-k]$ | time-invariance |
| $\delta[n] + \delta[n-k]$ | $h[n] + h[n-k]$ | additivity |
| $\sum_k x[k]\,\delta[n-k]$ | $\sum_k x[k]\,h[n-k]$ | all three |

> [!key] The convolution sum
> The output of an LTI system with impulse response $h[n]$ to the input $x[n]$ is
> $$
> y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k] = \sum_{k=-\infty}^{\infty} h[k]\,x[n-k] = h[n] * x[n].
> $$
> The two forms are equal by the change of variables $m = n - k$: convolution is commutative.

Every row of the table used a property, so the construction works **only for LTI systems**. The notes state it as three equivalent facts (their Fig. 1):

> [!key] The "if and only if" triangle
> A system is **LTI** $\iff$ its output is the **convolution** of the input with some $h[n]$ $\iff$ it is **fully described by its impulse response** (knowing $h$, you know the output for every input).

The median filter breaks the triangle: it is nonlinear, so $h_2 = 0$ says nothing about its response to other inputs. The difference system is LTI (Lecture 3), so $y_1 = x * (\delta[n] - \delta[n-1])$ reproduces it exactly.

> [!trap] "Every system is described by its impulse response" is False
> The exams test the triangle in both directions. False: "for a system with impulse response $h[n]$, the output to any input is $y = x * h$" ([[0-midterm-1/past-exams/fall-2023|FA2023 #1(d)]]), "…is always determined using $h[n]$" ([[0-midterm-1/past-exams/fall-2024|FA2024 #1(a)]]), "the input–output relationship of an arbitrary system is completely determined by its unit pulse response" ([[0-midterm-1/past-exams/fall-2019|FA2019 #1(b)]]). True: "if the response to *any* input is fully described by the unit pulse response, the system must be LTI" ([[0-midterm-1/past-exams/spring-2023|SP2023 #1(a)]]).

## 4. Computing one output sample: flip, shift, multiply, add

With $y[n] = \sum_k x[k]\,h[n-k]$, for each output index $n$:

1. **Flip** one signal (usually the shorter): $h[-k]$.
2. **Shift** the flipped signal right by $n$: $h[-(k-n)] = h[n-k]$.
3. **Multiply** sample by sample: $z_n[k] = x[k]\,h[n-k]$.
4. **Add** the products: $y[n] = \sum_k z_n[k]$.

Repeat steps 2–4 for every $n$. The picture for the notes' example $x[n] = \{\underset{\uparrow}{3}, 1, 0, 3, 1, 1\}$, $h[n] = \{2, \underset{\uparrow}{-1}, 1\}$ at $n = 2$:

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 548" width="640" height="548" role="img" aria-label="Flip and shift: computing y[2] for the notes' example by overlaying x[k] and h[2-k]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="10.0" y1="100.0" x2="460.0" y2="100.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,100.0 455.0,96.2 455.0,103.8" fill="currentColor"/><text x="460.0" y="118.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="32.0" x2="150.6" y2="108.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="97.0" x2="30.0" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="97.0" x2="70.2" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="97.0" x2="110.4" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="97.0" x2="150.6" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="97.0" x2="190.8" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="97.0" x2="231.0" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="97.0" x2="271.2" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="97.0" x2="311.4" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="97.0" x2="351.6" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="97.0" x2="391.8" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="97.0" x2="432.0" y2="103.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">x[k] = {3, 1, 0, 3, 1, 1},  x[0] = 3</text><circle cx="30.0" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="110.4" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="150.6" y1="100.0" x2="150.6" y2="46.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="150.6" cy="46.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="150.6" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">3</text><line x1="190.8" y1="100.0" x2="190.8" y2="82.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="82.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="190.8" y="73.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><circle cx="231.0" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="271.2" y1="100.0" x2="271.2" y2="46.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="271.2" cy="46.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="271.2" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">3</text><line x1="311.4" y1="100.0" x2="311.4" y2="82.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="311.4" cy="82.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="311.4" y="73.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><line x1="351.6" y1="100.0" x2="351.6" y2="82.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="351.6" cy="82.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="351.6" y="73.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><circle cx="391.8" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="100.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="10.0" y1="214.0" x2="460.0" y2="214.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,214.0 455.0,210.2 455.0,217.8" fill="currentColor"/><text x="460.0" y="232.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="164.0" x2="150.6" y2="240.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="211.0" x2="30.0" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="211.0" x2="70.2" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="211.0" x2="110.4" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="211.0" x2="150.6" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="207.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="211.0" x2="190.8" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="211.0" x2="231.0" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="211.0" x2="271.2" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="211.0" x2="311.4" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="211.0" x2="351.6" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="211.0" x2="391.8" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="211.0" x2="432.0" y2="217.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="231.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="150.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">h[k] = {2, −1, 1},  h[0] = −1</text><circle cx="30.0" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="110.4" y1="214.0" x2="110.4" y2="178.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="110.4" cy="178.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="110.4" y="169.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">2</text><line x1="150.6" y1="214.0" x2="150.6" y2="232.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="150.6" cy="232.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="150.6" y="250.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−1</text><line x1="190.8" y1="214.0" x2="190.8" y2="196.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="196.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="190.8" y="187.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><circle cx="231.0" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="271.2" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="311.4" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="351.6" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="391.8" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="214.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="10.0" y1="328.0" x2="460.0" y2="328.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,328.0 455.0,324.1 455.0,331.9" fill="currentColor"/><text x="460.0" y="346.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="278.0" x2="150.6" y2="354.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="325.0" x2="30.0" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="325.0" x2="70.2" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="325.0" x2="110.4" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="325.0" x2="150.6" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="321.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="325.0" x2="190.8" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="325.0" x2="231.0" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="325.0" x2="271.2" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="325.0" x2="311.4" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="325.0" x2="351.6" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="325.0" x2="391.8" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="325.0" x2="432.0" y2="331.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="345.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="264.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">① flip:  h[−k]</text><circle cx="30.0" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="110.4" y1="328.0" x2="110.4" y2="310.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="110.4" cy="310.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="110.4" y="301.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><line x1="150.6" y1="328.0" x2="150.6" y2="346.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="150.6" cy="346.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="150.6" y="364.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−1</text><line x1="190.8" y1="328.0" x2="190.8" y2="292.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="292.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="190.8" y="283.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">2</text><circle cx="231.0" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="271.2" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="311.4" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="351.6" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="391.8" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="328.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="10.0" y1="470.0" x2="460.0" y2="470.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="462.0,470.0 455.0,466.1 455.0,473.9" fill="currentColor"/><text x="460.0" y="488.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">k</text><line x1="150.6" y1="402.0" x2="150.6" y2="478.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="467.0" x2="30.0" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−3</text><line x1="70.2" y1="467.0" x2="70.2" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="70.2" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="110.4" y1="467.0" x2="110.4" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="110.4" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−1</text><line x1="150.6" y1="467.0" x2="150.6" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="150.6" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">0</text><line x1="190.8" y1="467.0" x2="190.8" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="190.8" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">1</text><line x1="231.0" y1="467.0" x2="231.0" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="231.0" y="463.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="271.2" y1="467.0" x2="271.2" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="271.2" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">3</text><line x1="311.4" y1="467.0" x2="311.4" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="311.4" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="351.6" y1="467.0" x2="351.6" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="351.6" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">5</text><line x1="391.8" y1="467.0" x2="391.8" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="391.8" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">6</text><line x1="432.0" y1="467.0" x2="432.0" y2="473.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.0" y="487.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">7</text><text x="10.0" y="390.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">② shift by n = 2:  h[2−k], laid over x[k]</text><circle cx="30.0" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="70.2" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="110.4" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="150.6" y1="470.0" x2="150.6" y2="416.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="150.6" cy="416.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><line x1="190.8" y1="470.0" x2="190.8" y2="452.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="190.8" cy="452.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><circle cx="231.0" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="271.2" y1="470.0" x2="271.2" y2="416.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="271.2" cy="416.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><line x1="311.4" y1="470.0" x2="311.4" y2="452.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="311.4" cy="452.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><line x1="351.6" y1="470.0" x2="351.6" y2="452.0" stroke="var(--muted)" stroke-width="1.3" stroke-linecap="round"/><circle cx="351.6" cy="452.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><circle cx="391.8" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.0" cy="470.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="190.8" y1="470.0" x2="190.8" y2="452.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="190.8" cy="452.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="199.8" y="456.0" text-anchor="start" fill="currentColor" style="font-size:12px;">1</text><line x1="231.0" y1="470.0" x2="231.0" y2="488.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="231.0" cy="488.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="240.0" y="492.0" text-anchor="start" fill="currentColor" style="font-size:12px;">−1</text><line x1="271.2" y1="470.0" x2="271.2" y2="434.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="271.2" cy="434.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="280.2" y="438.0" text-anchor="start" fill="currentColor" style="font-size:12px;">2</text><rect x="174.7" y="404.0" width="112.6" height="96.0" rx="0" fill="var(--hi)" fill-opacity="0.08" stroke="none" stroke-width="1.4"/><text x="478.0" y="176.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">the sequence we</text><text x="478.0" y="192.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">slide (the shorter one)</text><text x="478.0" y="290.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">mirror image about k = 0:</text><text x="478.0" y="306.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.9">h[1] now sits at k = −1</text><text x="478.0" y="414.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">③ multiply where both</text><text x="478.0" y="430.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">are nonzero, ④ add:</text><text x="478.0" y="452.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">k = 1:  1 · 1 = 1</text><text x="478.0" y="470.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">k = 2:  0 · (−1) = 0</text><text x="478.0" y="488.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">k = 3:  3 · 2 = 6</text><text x="478.0" y="516.0" text-anchor="start" fill="var(--accent)" style="font-size:15px;font-weight:700;">y[2] = 7</text><circle cx="26.0" cy="536.0" r="4.2" fill="none" stroke="var(--muted)" stroke-width="1.6"/><text x="36.0" y="540.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;" opacity="0.85">x[k]</text><circle cx="90.0" cy="536.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="100.0" y="540.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;" opacity="0.85">h[2−k]</text></svg><figcaption><strong>Flip, shift, multiply, add: one output sample at a time.</strong> To get y[2] for the notes' example, mirror h about k = 0, slide the mirror image right by n = 2, multiply it sample by sample with x[k] and add the products: 1·1 + 0·(−1) + 3·2 = 7. Sliding by n = −1, 0, …, 6 instead produces the whole output {6, −1, 2, 7, −1, 4, 0, 1}, with y[−1] = 6 and y[0] = −1.</figcaption></figure>

## 5. Properties of convolution and of $h[n]$

> [!key] Convolution toolbox
> - **Commutative:** $x * h_1 * h_2 = x * h_2 * h_1 = h_1 * x * h_2 = \cdots$ In a cascade of LTI systems the order does not matter.
> - **Associative:** $(x * h_1) * h_2 = x * (h_1 * h_2)$. A cascade is one LTI system with $h = h_1 * h_2$.
> - **Distributive:** $x * (h_1 + h_2) = x * h_1 + x * h_2$. A parallel connection is one LTI system with $h = h_1 + h_2$.
> - **Identity and shift:** $x[n] * \delta[n] = x[n]$ and $x[n] * \delta[n-k] = x[n-k]$.
> - **Start, end, length:** if $x$ lives on $n_s \le n \le n_e$ (length $N$) and $h$ on $m_s \le n \le m_e$ (length $M$), then $y = x * h$ starts at $n_s + m_s$, ends at $n_e + m_e$, and has length $N + M - 1$.
> - **Causality:** an LTI system is causal $\iff h[n] = 0$ for $n < 0$ (the flipped $h$ never reaches past the present).
> - **BIBO stability:** an LTI system is stable $\iff \sum_{n=-\infty}^{\infty} \lvert h[n]\rvert < \infty$ (absolutely summable).

> [!derivation]- Why absolute summability is exactly BIBO stability (the lecture exercise)
> **If** $S = \sum_k \lvert h[k]\rvert < \infty$ and $\lvert x[n]\rvert < \beta$ for all $n$, then
> $$
> \lvert y[n]\rvert = \Big\lvert \sum_k h[k]\,x[n-k] \Big\rvert \le \sum_k \lvert h[k]\rvert\,\lvert x[n-k]\rvert < \beta\,S \quad\text{for every } n .
> $$
> **Only if:** when $\sum_k \lvert h[k]\rvert = \infty$, use the bounded input $x[n] = \operatorname{sgn}(h[-n])$ (for complex $h$: $\overline{h[-n]}/\lvert h[-n]\rvert$, and $0$ where $h[-n] = 0$). Then $y[0] = \sum_k h[k]\,x[-k] = \sum_k \lvert h[k]\rvert = \infty$.
> Consequences that the T/F questions love: a **bounded** $h$ can still be unstable ($h = u[n]$, [[0-midterm-1/past-exams/fall-2025|FA2025 #1(a)]], False); a finite-length $h$ is **always** stable ([[0-midterm-1/past-exams/fall-2019|FA2019 #1(e)]], "can be stable or unstable" is False).

## 6. Computing convolutions: the three cases

### 6a. Two finite sequences: the table (shift-and-overlap)

Notes example: $x[n] = \{\underset{\uparrow}{3}, 1, 0, 3, 1, 1\}$ and $h[n] = \{2, \underset{\uparrow}{-1}, 1\}$. **Before multiplying anything**, fix the output support: start $0 + (-1) = -1$, end $5 + 1 = 6$, length $6 + 3 - 1 = 8$. Flip the shorter sequence and slide it; each row is one value of $n$ (blank = 0, "zero extension"):

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

### 6b. Two finite sequences: the matrix method

Put shifted copies of $h$ in the columns of a matrix (a **Toeplitz** matrix: constant along each diagonal) and multiply by the vector of $x$ values. Each row is one flipped-and-shifted $h$, so this is the table in matrix form:

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

Equivalently $\mathbf{y} = \mathbf{X}\mathbf{h}$ with an $8\times 3$ matrix built from $x$ (commutativity). The matrix knows nothing about indices: the first row is $n = n_s + m_s = -1$, which you must label yourself. The exam keys use exactly this layout; see [[problems/finite-length-convolution]].

The same bookkeeping in NumPy, where `np.convolve` also returns values only:

```python
import numpy as np
x, nx = np.array([3, 1, 0, 3, 1, 1]), 0     # x[n] = {3(n=0), 1, 0, 3, 1, 1}
h, nh = np.array([2, -1, 1]), -1            # h[n] = {2, -1(n=0), 1}
y = np.convolve(x, h)                        # values only: numpy knows no indices
ny = nx + nh                                 # start index of y = sum of start indices
n = np.arange(ny, ny + len(y))               # len(y) = 6 + 3 - 1 = 8
print(dict(zip(n.tolist(), y.tolist())))
print("sum check:", y.sum(), "=", x.sum(), "*", h.sum())
```

```text
{-1: 6, 0: -1, 1: 2, 2: 7, 3: -1, 4: 4, 5: 0, 6: 1}
sum check: 18 = 9 * 2
```

> [!tip] A 10-second check for any finite convolution
> $\sum_n y[n] = \big(\sum_n x[n]\big)\big(\sum_n h[n]\big)$. Here $18 = 9 \cdot 2$. It catches most arithmetic slips; it even catches the official key of [[0-midterm-1/past-exams/spring-2025|SP2025 #4(a)]], whose boxed answer sums to 7 instead of $2 \cdot 4 = 8$ (the correct answer is $\{2, -5, \underset{\uparrow}{5}, 0, -5, 12, -4, 3\}$). It does not check the *position* of the arrow: do that with the start-index rule.

> [!question] Slides practice: convolve $x[n] = \{\underset{\uparrow}{1}, 2, 0, -4, -1\}$ with $h[n] = \{-2, \underset{\uparrow}{0}, 1\}$, and $x[n] = \{-3, 6, 2, \underset{\uparrow}{0}, 1, 1\}$ with $h[n] = \{1, \underset{\uparrow}{-1}\}$.

> [!success]- Answers (annotated slides)
> First: starts at $0 + (-1) = -1$, length $5 + 3 - 1 = 7$: $y[n] = \{-2,\ \underset{\uparrow}{-4},\ 1,\ 10,\ 2,\ -4,\ -1\}$. Sum check: $-2 \cdot (-1) = 2$ ✓.
> Second: $x$ starts at $-3$ and $h$ at $-1$, so $y$ starts at $-4$: $y[n] = \{-3,\ 9,\ -4,\ -2,\ \underset{\uparrow}{1},\ 0,\ -1\}$. Sum check: $7 \cdot 0 = 0$ ✓.

### 6c. Two infinite sequences: evaluate the sum

> [!recipe] Convolution sum with step functions
> 1. Write $y[n] = \sum_k x[k]\,h[n-k]$ with every $u[\cdot]$ kept.
> 2. Turn the steps into summation limits: $u[k]$ means $k \ge 0$, $u[n-k]$ means $k \le n$. If no $k$ survives (here: $n < 0$), $y[n] = 0$.
> 3. Pull everything that depends only on $n$ out of the sum; combine the rest into one geometric ratio $a^k$.
> 4. Use $\displaystyle\sum_{k=0}^{n} a^k = \frac{1 - a^{n+1}}{1 - a}$ ($a \ne 1$), and attach the range as a step: $u[n]$, $u[n-3]$, …

**Notes: $x[n] = u[n]$, $h[n] = (-\tfrac34)^n u[n]$.**

$$
y[n] = \sum_{k} \left(-\tfrac34\right)^k u[k]\,u[n-k] = \sum_{k=0}^{n}\left(-\tfrac34\right)^k = \frac{1 - (-\frac34)^{n+1}}{\frac74}
= \left(\frac47 - \frac47\left(-\frac34\right)^{n+1}\right)u[n].
$$

**Slides: $x[n] = (\tfrac12)^n u[n]$, $h[n] = (-\tfrac34)^n u[n]$.** For $n \ge 0$, factor $(-\frac34)^n$ out and combine $(\frac12)^k(-\frac34)^{-k} = (-\frac23)^k$:

$$
y[n] = \left(-\tfrac34\right)^n \sum_{k=0}^{n} \left(-\tfrac23\right)^k
= \frac35\left(-\frac34\right)^n\left(1 - \left(-\frac23\right)^{n+1}\right)u[n]
= \left[\frac35\left(-\frac34\right)^n + \frac25\left(\frac12\right)^n\right]u[n].
$$

Check: $y[0] = 1 = x[0]h[0]$ and $y[1] = -\tfrac34 + \tfrac12 = -\tfrac14$ ✓. The last form (a combination of the two input "modes") is what the z-transform will produce directly in [[2-z-transform/09-transfer-functions|Lecture 9]].

> [!question] Slides extra practice: $x[n] = u[n]$, $h[n] = (\tfrac23)^{n-2}u[n-4]$. And from [[0-midterm-1/past-exams/spring-2023|SP2023 #3(b)]]: $x[n] = (-\tfrac12)^n u[n]$, $h[n] = (\tfrac23)^n u[n-1]$.

> [!success]- Answers
> **Slides:** $u[k-4]\,u[n-k]$ keeps $4 \le k \le n$, so $y[n] = 0$ for $n < 4$ and, with $m = k-4$,
> $$
> y[n] = \sum_{k=4}^{n}\left(\tfrac23\right)^{k-2} = \left(\tfrac23\right)^{2}\sum_{m=0}^{n-4}\left(\tfrac23\right)^{m} = \frac49\cdot\frac{1-(\frac23)^{n-3}}{\frac13} = \frac43\left(1 - \left(\frac23\right)^{n-3}\right)u[n-4].
> $$
> Check: $y[4] = \tfrac43\cdot\tfrac13 = \tfrac49 = h[4]$ ✓, and $y[n] \to \tfrac43 = \sum_n h[n]$ ✓.
> **SP2023 #3(b):** here the step $u[n-k-1]$ from $h$ gives $0 \le k \le n-1$, so the output starts at $n = 1$:
> $$
> y[n] = \left(\tfrac23\right)^n\sum_{k=0}^{n-1}\left(-\tfrac34\right)^k = \frac47\left[\left(\frac23\right)^n - \left(-\frac12\right)^n\right]u[n-1].
> $$

### 6d. One finite and one infinite sequence: split into impulses

Write the finite one as a sum of shifted impulses and use $h[n] * a\,\delta[n-k] = a\,h[n-k]$ (linearity and time-invariance of convolution).

**Notes:** $x[n] = \{\underset{\uparrow}{1}, 0, 2, 0, -3\} = \delta[n] + 2\delta[n-2] - 3\delta[n-4]$ and $h[n] = \sin^3(\frac{\pi}{4}n)\,u[n]$:

$$
y[n] = h[n] + 2h[n-2] - 3h[n-4] = \sin^3\!\left(\tfrac{\pi}{4}n\right)u[n] + 2\sin^3\!\left(\tfrac{\pi}{4}(n-2)\right)u[n-2] - 3\sin^3\!\left(\tfrac{\pi}{4}(n-4)\right)u[n-4].
$$

**Slides:** $x[n] = \{-2, 0, \underset{\uparrow}{0}, 3, 0, 1\} = -2\delta[n+2] + 3\delta[n-1] + \delta[n-3]$ and $h[n] = e^{-n}u[n]$:

$$
y[n] = -2e^{-(n+2)}u[n+2] + 3e^{-(n-1)}u[n-1] + e^{-(n-3)}u[n-3].
$$

> [!trap] Shift every $n$, including the step
> $h[n-4]$ means replace **every** $n$: $\sin^3(\frac{\pi}{4}(n-4))\,u[n-4]$, not $\sin^3(\frac{\pi}{4}(n-4))\,u[n]$. Dropping the shifted step is the most common way to lose points on the mixed convolution. The same goes for polynomial factors: in [[0-midterm-1/past-exams/fall-2025|FA2025 #3(b)]], $x[n] = n\,u[n+1]\,u[-n+1] = \{-1, \underset{\uparrow}{0}, 1\} = -\delta[n+1] + \delta[n-1]$ and $h[n] = n(\tfrac13)^n\cos(n)$, so $y[n] = -h[n+1] + h[n-1] = -(n+1)(\tfrac13)^{n+1}\cos(n+1) + (n-1)(\tfrac13)^{n-1}\cos(n-1)$.

## 7. Working backwards: finding $h$ from input–output pairs

LTI means linear combinations and shifts of inputs produce the same combinations and shifts of outputs. So:

> [!recipe] Finding $h[n]$ from what you are given
> 1. **The input is a scaled, shifted impulse** $x = c\,\delta[n-n_0]$: then $y = c\,h[n-n_0]$, so $h[n] = \tfrac1c\,y[n+n_0]$.
> 2. **You know the step response** $g[n] = h[n] * u[n]$: since $\delta[n] = u[n] - u[n-1]$, $h[n] = g[n] - g[n-1]$ ([[homework/hw2|HW2]] #3).
> 3. **General input:** find a combination of shifted inputs that equals $\delta[n]$, e.g. $x[n] - a\,x[n-1] = \delta[n]$, and apply the *same* combination to the outputs: $h[n] = y[n] - a\,y[n-1]$.
> 4. **Cascades and parallels:** cascade $h = h_1 * h_2$ (order irrelevant), parallel $h = h_1 + h_2$; peel off the known piece.
> 5. Then answer the follow-ups from $h$: causal? ($h[n] = 0$ for $n<0$) stable? ($\sum\lvert h\rvert < \infty$)

> [!question] [[0-midterm-1/past-exams/fall-2019|FA2019 #3]]: an LTI system maps $x[n] = 2\delta[n-2]$ to $y[n] = \delta[n-1] + 2\delta[n-2] + \delta[n-3]$. Find $h[n]$, the step response, and decide whether the system is causal.

> [!success]- Answer
> Step 1 with $c = 2$, $n_0 = 2$: $h[n] = \tfrac12\,y[n+2] = \tfrac12\delta[n+1] + \delta[n] + \tfrac12\delta[n-1]$. Step response: $g = h * u = \tfrac12 u[n+1] + u[n] + \tfrac12 u[n-1]$, i.e. $\{\tfrac12, \underset{\uparrow}{\tfrac32}, 2, 2, \dots\}$ starting at $n = -1$. **Not causal**: $h[-1] = \tfrac12 \neq 0$.

More from the exams and homework (all verified):

- [[homework/hw2|HW2]] #4: $x[n] = 3^{-n}u[n]$ gives $y[n] = 5^{-n}u[n-1]$. Since $x[n] - \tfrac13 x[n-1] = \delta[n]$, $h[n] = y[n] - \tfrac13 y[n-1] = \tfrac15\delta[n-1] - \tfrac23(\tfrac15)^n u[n-2]$.
- [[0-midterm-1/past-exams/fall-2023|FA2023 #4]]: which $h$ maps $u[n]$ to $\delta[n] + \delta[n-1]$? $h[n] = g[n] - g[n-1] = \delta[n] - \delta[n-2]$.
- [[0-midterm-1/past-exams/spring-2023|SP2023 #4]]: two pairs $(x_1, y_1)$, $(x_2, y_2)$ with $x_1[n] - 3x_2[n-1] = \delta[n]$, so $h[n] = y_1[n] - 3y_2[n-1]$.
- [[0-midterm-1/past-exams/fall-2024|FA2024 #3]] (cascade, $h_2$ known): $h_1 = 2\delta[n+1]$. [[0-midterm-1/past-exams/spring-2025|SP2025 #3]] (parallel, $h_1 = \delta[n-1]$ known): $h_2 = \delta[n+1]$, so $h = \{1, \underset{\uparrow}{0}, 1\}$, not causal.

Full recipe page: [[problems/finding-h-from-input-output-pairs]].

## 8. On the exam

> [!exam] Where Lecture 4 shows up (the densest lecture on Midterm 1)
> - **Finite-length convolution, 7 of 7 exams (5–10 points):** [[0-midterm-1/past-exams/fall-2025|FA2025 #3a]], [[0-midterm-1/past-exams/spring-2025|SP2025 #4a]], [[0-midterm-1/past-exams/fall-2024|FA2024 #4a]], [[0-midterm-1/past-exams/fall-2023|FA2023 #3a]], [[0-midterm-1/past-exams/spring-2023|SP2023 #3a]], [[0-midterm-1/past-exams/spring-2021|SP2021 #2]], [[0-midterm-1/past-exams/fall-2019|FA2019 #4]]. The keys use the matrix method; the points are lost on the arrow. Write the start index first. Recipe: [[problems/finite-length-convolution]].
> - **Infinite or mixed convolution, 5 of 7:** [[0-midterm-1/past-exams/fall-2025|FA2025 #3b]], [[0-midterm-1/past-exams/spring-2025|SP2025 #4b]], [[0-midterm-1/past-exams/fall-2024|FA2024 #4b]], [[0-midterm-1/past-exams/fall-2023|FA2023 #3b]], [[0-midterm-1/past-exams/spring-2023|SP2023 #3b–c]]. Closed form required (no $\sum$ left). Recipe: [[problems/infinite-length-convolution]].
> - **Finding $h$ (or $H$) from input–output data, 7 of 7:** §7 above; later exams mix in z-transforms ([[2-z-transform/09-transfer-functions|Lecture 9]]).
> - **True/False:** the LTI triangle (§3); "a bounded $h$ means stable" (False); "the convolution of two causal signals is causal" ([[0-midterm-1/past-exams/fall-2025|FA2025 #1(b)]], True); "the parallel connection of two unstable LTI systems is always unstable" ([[0-midterm-1/past-exams/fall-2025|FA2025 #1(f)]], False: $u[n] + (\delta[n] - u[n]) = \delta[n]$); cascade order never matters for LTI systems ([[0-midterm-1/past-exams/fall-2023|FA2023 #1(e)]], True). All of them in the [[0-midterm-1/true-false-bank|T/F bank]].
> - **Property table rows** like $x[n] * u[n+1]$ or $x[n] * 2^n u[-n]$ are decided by §5: LTI by construction, causal iff $h[n] = 0$ for $n < 0$, stable iff $\sum\lvert h\rvert < \infty$.

## Related

- [[concepts/impulse-response|Impulse response]] · [[concepts/convolution|Convolution]] · [[concepts/lti-system|LTI system]] · [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/step-response|Step response]] · [[concepts/causality|Causality]] · [[concepts/bibo-stability|BIBO stability]]
- Try it: [[demos/convolution-explorer|convolution explorer]] · [[0-toolkit/02-geometric-series|geometric series]] for §6c
- Next: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] describes LTI systems by a recursion instead of by $h$, which is how infinitely long impulse responses are computed in practice.

### Sources for this page
Snyder, ECE 310 Lecture 4 notes (impulse response, sifting, LTI derivation and Fig. 1, properties, table / matrix / convolution-sum / mixed methods) and slides "Convolution and impulse response" (Aug 31, 2026) with the annotated in-class deck (worked answers to every practice problem). HW2 #3–5. Past Midterm 1 problems FA2019–FA2025 as cited. Every number on this page is checked in `verify/lectures/l4_convolution.py`.
