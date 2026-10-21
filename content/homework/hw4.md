---
title: "HW4 · All possible ROCs, BIBO stability, and system algebra"
description: "ECE 310 Homework 4 (due Sep 25) with folded solutions: inverse z for every ROC, BIBO stability ⇔ absolute summability, stability from poles and inputs that break it, h[n] from an input–output pair, pole-zero cancellations."
tags: [homework, midterm-1, z-transform, roc, stability, lccde]
---

*Homework 4 · due Fri Sep 25, 2026 (Gradescope) · Lectures 8–11 (inverse z for every ROC, transfer functions and system algebra, BIBO stability and causality) · 100 points (18 + 16 + 16 + 16 + 16 + 18) · official solutions v1.0 · prev: [[homework/hw3|HW3]] · [[homework/index|all homework]]*

> [!abstract] In one breath
> - $d$ distinct pole radii give $d+1$ ROCs; the ROC picks each term's side (#1).
> - LTI stable ⇔ $\sum\lvert h[n]\rvert < \infty$; causal: all poles inside the unit circle (#2, #3).
> - $H = Y/X$; a zero can cancel an unstable pole (#4–#6).

| # | Skill | Links |
|---|---|---|
| 1 | All ROCs and inverses | [[problems/all-possible-rocs\|all possible ROCs]] · [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]] |
| 2 | BIBO ⇔ $\sum_n \lvert h[n]\rvert < \infty$ | [[concepts/bibo-stability\|BIBO stability]] · [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 3 | Stability from poles; breaking inputs | [[problems/unbounded-outputs-and-pole-matching\|unbounded outputs, pole matching]] |
| 4 | $H = Y/X$, causal ROC | [[problems/finding-h-from-input-output-pairs\|finding h from input-output data]] |
| 5 | Cascade with cancellation | [[concepts/pole-zero-cancellation\|pole-zero cancellation]] |
| 6 | LCCDE → $H(z)$ → response | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z) ↔ response]] |

## Problem 1 — every ROC, every sequence

> [!question] Problem 1 (18 pts)
> Find all the possible ROCs for the following z-transforms and determine the associated inverse z-transform for each case.
>
> (a) $\dfrac{z^2 - z}{z^2 + 3z + 2}$
>
> (b) $\dfrac{z^3 - z}{z^2 + 3z + 2}$
>
> (c) $\dfrac{1}{\left(1-\frac13 z^{-1}\right)\left(1-\frac15 z^{-1}\right)}$

> [!success]- Solution (a)
> $$
> X(z) = \frac{1-z^{-1}}{1+3z^{-1}+2z^{-2}} = \frac{1-z^{-1}}{\left(1+z^{-1}\right)\left(1+2z^{-1}\right)} = \frac{-2}{1+z^{-1}} + \frac{3}{1+2z^{-1}},
> $$
> $A_1 = \left.\dfrac{1-z^{-1}}{1+2z^{-1}}\right|_{z^{-1}=-1} = \dfrac{2}{-1} = -2$, $A_2 = \left.\dfrac{1-z^{-1}}{1+z^{-1}}\right|_{z^{-1}=-\frac12} = \dfrac{3/2}{1/2} = 3$. Poles $-1$, $-2$; zeros $0$, $1$. Pole inside the ROC's inner circle → right-sided; outside its outer circle → left-sided.
>
> | ROC | pole $-1$ | pole $-2$ | $x[n]$ |
> |---|---|---|---|
> | $\lvert z\rvert < 1$ | left | left | $2(-1)^n u[-n-1] - 3(-2)^n u[-n-1]$ |
> | $1 < \lvert z\rvert < 2$ | right | left | $-2(-1)^n u[n] - 3(-2)^n u[-n-1]$ |
> | $\lvert z\rvert > 2$ | right | right | $-2(-1)^n u[n] + 3(-2)^n u[n]$ |
>
> The fourth combination needs $\lvert z\rvert < 1$ and $\lvert z\rvert > 2$: empty.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 270" width="640" height="270" role="img" aria-label="The three possible ROCs for HW4 problem 1(a)" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M146.0,118.0 A36.0,36.0 0 1 0 74.0,118.0 A36.0,36.0 0 1 0 146.0,118.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="10.0" y1="118.0" x2="208.0" y2="118.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="214.0,118.0 208.0,114.7 208.0,121.3" fill="currentColor"/><line x1="110.0" y1="218.0" x2="110.0" y2="20.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="110.0,14.0 106.7,20.0 113.3,20.0" fill="currentColor"/><text x="212.0" y="134.0" text-anchor="end" fill="currentColor" style="font-size:11px;">Re</text><text x="116.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:11px;">Im</text><circle cx="110.0" cy="118.0" r="36.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><circle cx="110.0" cy="118.0" r="72.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><line x1="68.0" y1="112.0" x2="80.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="68.0" y1="124.0" x2="80.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="32.0" y1="112.0" x2="44.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="32.0" y1="124.0" x2="44.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="110.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="146.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="110.0" y="242.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| &lt; 1</text><text x="110.0" y="258.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms left-sided</text><path d="M394.0,118.0 A72.0,72.0 0 1 0 250.0,118.0 A72.0,72.0 0 1 0 394.0,118.0 Z M358.0,118.0 A36.0,36.0 0 1 0 286.0,118.0 A36.0,36.0 0 1 0 358.0,118.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="222.0" y1="118.0" x2="420.0" y2="118.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="426.0,118.0 420.0,114.7 420.0,121.3" fill="currentColor"/><line x1="322.0" y1="218.0" x2="322.0" y2="20.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="322.0,14.0 318.7,20.0 325.3,20.0" fill="currentColor"/><circle cx="322.0" cy="118.0" r="36.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><circle cx="322.0" cy="118.0" r="72.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><line x1="280.0" y1="112.0" x2="292.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="280.0" y1="124.0" x2="292.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="244.0" y1="112.0" x2="256.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="244.0" y1="124.0" x2="256.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="322.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="358.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="322.0" y="242.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">1 &lt; |z| &lt; 2</text><text x="322.0" y="258.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">two-sided</text><path d="M434.0,18.0 H634.0 V218.0 H434.0 Z M606.0,118.0 A72.0,72.0 0 1 0 462.0,118.0 A72.0,72.0 0 1 0 606.0,118.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="434.0" y1="118.0" x2="632.0" y2="118.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="638.0,118.0 632.0,114.7 632.0,121.3" fill="currentColor"/><line x1="534.0" y1="218.0" x2="534.0" y2="20.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="534.0,14.0 530.7,20.0 537.3,20.0" fill="currentColor"/><circle cx="534.0" cy="118.0" r="36.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><circle cx="534.0" cy="118.0" r="72.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><line x1="492.0" y1="112.0" x2="504.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="492.0" y1="124.0" x2="504.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="456.0" y1="112.0" x2="468.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="456.0" y1="124.0" x2="468.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="534.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="570.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="534.0" y="242.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| &gt; 2</text><text x="534.0" y="258.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms right-sided</text><text x="38.0" y="106.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">−2</text><text x="74.0" y="106.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">−1</text></svg><figcaption><strong>Two pole radii (1 and 2) → three annuli → three sequences.</strong> Zeros play no role in choosing the ROC.</figcaption></figure>

> [!success]- Solution (b)
> Cancel $(z+1)$:
> $$
> X(z) = \frac{z(z-1)(z+1)}{(z+1)(z+2)} = \frac{z(z-1)}{z+2} = \frac{z-1}{1+2z^{-1}} = \frac{z}{1+2z^{-1}} - \frac{1}{1+2z^{-1}} .
> $$
> One finite pole ($-2$) → two ROCs. $\dfrac{z}{1+2z^{-1}} \leftrightarrow (-2)^{n+1}u[n+1]$ or $-(-2)^{n+1}u[-n-2]$.
>
> - ROC $2 < \lvert z\rvert < \infty$: $x[n] = (-2)^{n+1}u[n+1] - (-2)^n u[n] = \delta[n+1] - 3(-2)^n u[n]$.
> - ROC $\lvert z\rvert < 2$: $x[n] = -(-2)^{n+1}u[-n-2] + (-2)^n u[-n-1] = -\tfrac12\delta[n+1] + 3(-2)^n u[-n-2]$.
>
> Long division: $\dfrac{z-1}{1+2z^{-1}} = z - 3 + 6z^{-1} - 12z^{-2} + \cdots$.

> [!success]- Solution (c)
> $$
> \begin{aligned}
> X(z) &= \frac{A_1}{1-\frac13 z^{-1}} + \frac{A_2}{1-\frac15 z^{-1}} = \frac{5/2}{1-\frac13 z^{-1}} - \frac{3/2}{1-\frac15 z^{-1}},\\
> A_1 &= \frac{1}{1-\frac15\cdot 3} = \frac52,\qquad A_2 = \frac{1}{1-\frac13\cdot 5} = -\frac32 .
> \end{aligned}
> $$
> | ROC | pole $\frac13$ | pole $\frac15$ | $x[n]$ |
> |---|---|---|---|
> | $\lvert z\rvert < \frac15$ | left | left | $-\tfrac52\left(\tfrac13\right)^n u[-n-1] + \tfrac32\left(\tfrac15\right)^n u[-n-1]$ |
> | $\frac15 < \lvert z\rvert < \frac13$ | left | right | $-\tfrac52\left(\tfrac13\right)^n u[-n-1] - \tfrac32\left(\tfrac15\right)^n u[n]$ |
> | $\lvert z\rvert > \frac13$ | right | right | $\tfrac52\left(\tfrac13\right)^n u[n] - \tfrac32\left(\tfrac15\right)^n u[n]$ |

**On the exam:** [[exams/midterm-1/past-exams/fall-2023|FA2023 #6(a)]]: three ROCs in a table, fourth combination empty.

## Problem 2 — BIBO stable if and only if absolutely summable

> [!question] Problem 2 (16 pts)
> Show that an LSI system with unit pulse response $h[n]$ is BIBO stable if and only if $h[n]$ is absolutely summable, i.e. $\sum_{n=-\infty}^{\infty}\lvert h[n]\rvert < B < \infty$.

> [!success]- Solution
> **Sufficiency.** $\lvert x[n]\rvert \le M$:
> $$
> \begin{aligned}
> \lvert y[n]\rvert &= \Big\lvert \sum_{k=-\infty}^{\infty} h[k]\,x[n-k]\Big\rvert \le \sum_{k=-\infty}^{\infty}\lvert h[k]\rvert\,\lvert x[n-k]\rvert\\
> &\le M\sum_{k=-\infty}^{\infty}\lvert h[k]\rvert \le MB < \infty .
> \end{aligned}
> $$
> **Necessity (contrapositive).** If $\sum_k\lvert h[k]\rvert = \infty$, take
> $$
> x[n] = \begin{cases}\dfrac{h^{*}[-n]}{\lvert h[-n]\rvert}, & h[-n]\neq0\\[6pt] 0, & h[-n]=0\end{cases}
> \qquad\big(\text{for real } h:\ x[n] = \operatorname{sgn}(h[-n])\big).
> $$
> $\lvert x[n]\rvert \le 1$, yet
> $$
> y[0] = \sum_{k} h[k]\,x[-k] = \sum_{k}\frac{h[k]\,h^{*}[k]}{\lvert h[k]\rvert} = \sum_{k}\lvert h[k]\rvert = \infty .
> $$
> Both directions use $y = x*h$, so LTI is required.

> [!warning] Small gap in the key: complex h[n]
> The key's $x[n] = \operatorname{sgn}(h[-n])$ works only for real $h$. For $h[n] = j^n u[n]$ it gives $y[0] = \sum_k j^{2k} = 1 - 1 + 1 - \cdots$ (bounded); the conjugated input gives $\sum_k 1 = \infty$.

**On the exam:** T/F staples, e.g. "bounded $h$ ⇒ stable" ([[exams/midterm-1/past-exams/fall-2025|FA2025 #1(a)]], False); see the [[exams/midterm-1/true-false-bank|T/F bank]].

## Problem 3 — stable or not, and how to break it

> [!question] Problem 3 (16 pts)
> Determine whether each of the following transfer functions represents a BIBO stable causal system:
>
> (a) $H(z) = \dfrac{z(z-4)}{z^2-5z+6}$
>
> (b) $H(z) = \dfrac{z-7}{z^2+1/9}$
>
> (c) $H(z) = \dfrac{z+1}{z-1}$
>
> (d) $H(z) = \dfrac{z-1}{z^2+j}$
>
> For each case in which the system is determined to be unstable, find a bounded real-valued input that will produce an unbounded output.

> [!key] Rule
> Causal system stable ⇔ every pole (after cancellation) has $\lvert p\rvert < 1$. A pole on the unit circle is not BIBO stable. Break it with a bounded input whose pole lands on that system pole.

> [!success]- Solution (a)
> Poles $2$, $3$; ROC $\lvert z\rvert > 3$: **NOT stable**. $H(z) = \dfrac{1-4z^{-1}}{\left(1-2z^{-1}\right)\left(1-3z^{-1}\right)} = \dfrac{2}{1-2z^{-1}} - \dfrac{1}{1-3z^{-1}}$, $h[n] = \left(2^{n+1}-3^{n}\right)u[n]$. Input $\delta[n]$ suffices.

> [!success]- Solution (b)
> Poles $\pm\tfrac{j}{3}$; ROC $\lvert z\rvert > \tfrac13$: **stable**. $h = \{\underset{\uparrow}{0},\ 1,\ -7,\ -\tfrac19,\ \tfrac79,\ \dots\}$, $\sum_n\lvert h[n]\rvert = 8\sum_{m\ge0}\left(\tfrac19\right)^m = 9$.

> [!success]- Solution (c)
> Pole $1$; ROC $\lvert z\rvert > 1$ excludes the unit circle: **NOT stable**. $h[n] = u[n] + u[n-1] = \{\underset{\uparrow}{1},\ 2,\ 2,\ 2,\ \dots\}$ is bounded, so $\delta[n]$ fails. Input $u[n]$: $y[n] = \sum_{k=0}^{n}h[k] = (2n+1)u[n]$.

> [!success]- Solution (d)
> $z^2 = -j = e^{-j\pi/2}$: poles $e^{-j\pi/4}$, $e^{j3\pi/4}$ on the unit circle: **NOT stable**.
>
> Input $x[n] = \cos\!\left(\tfrac{\pi}{4}n\right)u[n] = \tfrac12\left(e^{j\pi n/4}+e^{-j\pi n/4}\right)u[n]$: $y[n] = C\,(n+1)\,e^{-j\pi n/4} + (\text{bounded})$, $\lvert C\rvert = \tfrac12\sin\tfrac{\pi}{8} \approx 0.19$. $\cos\!\left(\tfrac{3\pi}{4}n\right)u[n]$ also works. $u[n]$ fails (zero at $z=1$); $\delta[n]$ fails.
>
> (The key's "$n\cos\!\left(\tfrac{\pi}{4}n+\varphi\right)$" is imprecise: $H$ is complex, so only the $e^{-j\pi n/4}$ half resonates.)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="Pole-zero plots of the four HW4 problem 3 systems with their causal ROCs" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M8.0,32.0 H156.0 V200.0 H8.0 Z M130.0,116.0 A48.0,48.0 0 1 0 34.0,116.0 A48.0,48.0 0 1 0 130.0,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="8.0" y1="116.0" x2="154.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="160.0,116.0 154.0,112.7 154.0,119.3" fill="currentColor"/><line x1="82.0" y1="200.0" x2="82.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="82.0,28.0 78.7,34.0 85.3,34.0" fill="currentColor"/><circle cx="82.0" cy="116.0" r="16.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="109.0" y1="111.0" x2="119.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="121.0" x2="119.0" y2="111.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="125.0" y1="111.0" x2="135.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="125.0" y1="121.0" x2="135.0" y2="111.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="82.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="146.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="12.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(a)</text><text x="82.0" y="220.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;font-weight:600;">NOT stable</text><path d="M166.0,32.0 H314.0 V200.0 H166.0 Z M263.3,116.0 A23.3,23.3 0 1 0 216.7,116.0 A23.3,23.3 0 1 0 263.3,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="166.0" y1="116.0" x2="312.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="318.0,116.0 312.0,112.7 312.0,119.3" fill="currentColor"/><line x1="240.0" y1="200.0" x2="240.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="240.0,28.0 236.7,34.0 243.3,34.0" fill="currentColor"/><circle cx="240.0" cy="116.0" r="70.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="235.0" y1="87.7" x2="245.0" y2="97.7" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="235.0" y1="97.7" x2="245.0" y2="87.7" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="235.0" y1="134.3" x2="245.0" y2="144.3" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="235.0" y1="144.3" x2="245.0" y2="134.3" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="170.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(b)</text><text x="240.0" y="220.0" text-anchor="middle" fill="var(--accent)" style="font-size:12px;font-weight:600;">stable</text><path d="M324.0,32.0 H472.0 V200.0 H324.0 Z M448.0,116.0 A50.0,50.0 0 1 0 348.0,116.0 A50.0,50.0 0 1 0 448.0,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="324.0" y1="116.0" x2="470.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="476.0,116.0 470.0,112.7 470.0,119.3" fill="currentColor"/><line x1="398.0" y1="200.0" x2="398.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="398.0,28.0 394.7,34.0 401.3,34.0" fill="currentColor"/><circle cx="398.0" cy="116.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="443.0" y1="111.0" x2="453.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="443.0" y1="121.0" x2="453.0" y2="111.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="348.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="328.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(c)</text><text x="398.0" y="220.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;font-weight:600;">NOT stable (marginal)</text><path d="M482.0,32.0 H630.0 V200.0 H482.0 Z M606.0,116.0 A50.0,50.0 0 1 0 506.0,116.0 A50.0,50.0 0 1 0 606.0,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="482.0" y1="116.0" x2="628.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="634.0,116.0 628.0,112.7 628.0,119.3" fill="currentColor"/><line x1="556.0" y1="200.0" x2="556.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="556.0,28.0 552.7,34.0 559.3,34.0" fill="currentColor"/><circle cx="556.0" cy="116.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="586.4" y1="146.4" x2="596.4" y2="156.4" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="586.4" y1="156.4" x2="596.4" y2="146.4" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="515.6" y1="75.6" x2="525.6" y2="85.6" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="515.6" y1="85.6" x2="525.6" y2="75.6" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="606.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="486.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(d)</text><text x="556.0" y="220.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;font-weight:600;">NOT stable (marginal)</text><text x="306.0" y="132.0" text-anchor="end" fill="currentColor" style="font-size:11px;" opacity="0.85">zero at 7 →</text></svg><figcaption><strong>Causal ⇒ ROC outside the largest pole; stable ⇔ it contains the unit circle (dashed).</strong> Poles on the circle (c, d): not BIBO stable.</figcaption></figure>

**On the exam:** [[exams/midterm-1/past-exams/fall-2025|FA2025 #8(b)]]: pole at $e^{j2/3}$ (not $\tfrac{2\pi}{3}$), so $\cos\!\left(\tfrac{2\pi}{3}n\right)u[n]$ gives a bounded output.

## Problem 4 — h[n] from one input-output pair

> [!question] Problem 4 (16 pts)
> The input $x[n] = 2^{n}\big(u[n] - 3u[n-1]\big)$ to an unknown LSI system produces the output $y[n] = \left(3^{n} - 2^{n}\right)u[n]$. Determine the unit pulse response $h[n]$ assuming the system is causal. Is the system BIBO stable?

> [!success]- Solution
> $x[n] = 2^n u[n] - 6\cdot2^{n-1}u[n-1]$:
> $$
> X(z) = \frac{1}{1-2z^{-1}} - \frac{6z^{-1}}{1-2z^{-1}} = \frac{1-6z^{-1}}{1-2z^{-1}},\qquad \lvert z\rvert > 2 .
> $$
> $$
> \begin{aligned}
> Y(z) &= \frac{1}{1-3z^{-1}} - \frac{1}{1-2z^{-1}} = \frac{\left(1-2z^{-1}\right)-\left(1-3z^{-1}\right)}{\left(1-3z^{-1}\right)\left(1-2z^{-1}\right)}\\
> &= \frac{z^{-1}}{\left(1-3z^{-1}\right)\left(1-2z^{-1}\right)},\qquad \lvert z\rvert > 3 .
> \end{aligned}
> $$
> $$
> H(z) = \frac{Y(z)}{X(z)} = \frac{z^{-1}}{\left(1-3z^{-1}\right)\left(1-6z^{-1}\right)} = \frac{-\frac13}{1-3z^{-1}} + \frac{\frac13}{1-6z^{-1}},
> $$
> $A_1 = \left.\dfrac{z^{-1}}{1-6z^{-1}}\right|_{z^{-1}=\frac13} = \dfrac{1/3}{-1} = -\tfrac13$, $A_2 = \left.\dfrac{z^{-1}}{1-3z^{-1}}\right|_{z^{-1}=\frac16} = \dfrac{1/6}{1/2} = \tfrac13$. Causal: ROC $\lvert z\rvert > 6$.
>
> **Answer.** $h[n] = \tfrac13\left(6^{n} - 3^{n}\right)u[n]$; **not BIBO stable**.
>
> (The two-sided $3 < \lvert z\rvert < 6$, $h[n] = -\tfrac13\, 3^{n}u[n] - \tfrac13\, 6^{n}u[-n-1]$, also maps $x$ to $y$; no stable choice does.)

**On the exam:** [[exams/midterm-1/past-exams/spring-2021|SP2021 #7]]: given $x$ and $Y$, find $X$, $H$, ROC, $h$, stability.

## Problem 5 — a cascade that is stable although one stage is not

> [!question] Problem 5 (16 pts)
> Two systems with unit-pulse responses
> $$
> h_1[n] = 2u[n] - 2\left(\tfrac12\right)^{n}u[n],\qquad h_2[n] = \delta[n] - 3\left(\tfrac14\right)^{n}u[n-1]
> $$
> are in serial connection. (a) For each of the individual systems, as well as for the overall system, determine whether it is BIBO stable. (b) Determine the unit pulse response of the overall system.

> [!success]- Solution (a)
> **$h_1$:** $h_1[n] \to 2$: **not stable**.
> $$
> H_1(z) = \frac{2}{1-z^{-1}} - \frac{2}{1-\frac12 z^{-1}} = \frac{z^{-1}}{\left(1-z^{-1}\right)\left(1-\frac12 z^{-1}\right)},\qquad \lvert z\rvert > 1.
> $$
> **$h_2$:** $\sum_n\lvert h_2[n]\rvert = 1 + 3\sum_{n\ge1}\left(\tfrac14\right)^n = 1 + 3\cdot\dfrac{1/4}{3/4} = 2 < \infty$: **stable**.
> $$
> H_2(z) = 1 - \frac{\frac34 z^{-1}}{1-\frac14 z^{-1}} = \frac{1-z^{-1}}{1-\frac14 z^{-1}},\qquad \lvert z\rvert > \tfrac14 .
> $$
> **Cascade:** the zero of $H_2$ at $z=1$ cancels the pole of $H_1$:
> $$
> H(z) = \frac{z^{-1}}{\left(1-z^{-1}\right)\left(1-\frac12 z^{-1}\right)}\cdot\frac{1-z^{-1}}{1-\frac14 z^{-1}} = \frac{z^{-1}}{\left(1-\frac12 z^{-1}\right)\left(1-\frac14 z^{-1}\right)} .
> $$
> ROC $\lvert z\rvert > \tfrac12$: **overall BIBO stable**.

> [!success]- Solution (b)
> $$
> H(z) = \frac{A}{1-\frac12 z^{-1}} + \frac{B}{1-\frac14 z^{-1}},
> $$
> $$
> A = \left.\frac{z^{-1}}{1-\frac14 z^{-1}}\right|_{z^{-1}=2} = \frac{2}{1/2} = 4,\qquad
> B = \left.\frac{z^{-1}}{1-\frac12 z^{-1}}\right|_{z^{-1}=4} = \frac{4}{-1} = -4 .
> $$
> **Answer.** $h[n] = h_1[n]*h_2[n] = 4\left[\left(\tfrac12\right)^{n} - \left(\tfrac14\right)^{n}\right]u[n]$, $\sum_n\lvert h[n]\rvert = 4\left(2-\tfrac43\right) = \tfrac83$.

**On the exam:** "unstable stage ⇒ unstable cascade" is False ([[exams/midterm-1/past-exams/fall-2019|FA2019 #1(d)]]).

## Problem 6 — an LCCDE with a hidden cancellation

> [!question] Problem 6 (18 pts)
> Consider the following difference equation (LCCDE), with zero initial conditions:
> $$
> y[n] = x[n] + 0.5\,x[n-1] - y[n-1] - 0.25\,y[n-2],\qquad n = 0, 1, 2, \dots
> $$
> (a) Find the transfer function and its ROC. (b) Find the impulse response of the system. (c) Determine the output $y[n]$ for the input $x[n] = (-1)^n u[n]$.

> [!success]- Solution (a)
> $y[n] + y[n-1] + \tfrac14 y[n-2] = x[n] + \tfrac12 x[n-1]$:
> $$
> H(z) = \frac{1+\frac12 z^{-1}}{1+z^{-1}+\frac14 z^{-2}} = \frac{1+\frac12 z^{-1}}{\left(1+\frac12 z^{-1}\right)^{2}} = \frac{1}{1+\frac12 z^{-1}} .
> $$
> Causal: **ROC $\lvert z\rvert > \tfrac12$**.

> [!success]- Solution (b)
> $h[n] = \left(-\tfrac12\right)^{n}u[n]$.

> [!success]- Solution (c)
> $X(z) = \dfrac{1}{1+z^{-1}}$, $\lvert z\rvert > 1$:
> $$
> Y(z) = \frac{1}{\left(1+\frac12 z^{-1}\right)\left(1+z^{-1}\right)} = \frac{A}{1+\frac12 z^{-1}} + \frac{B}{1+z^{-1}},
> $$
> $$
> A = \left.\frac{1}{1+z^{-1}}\right|_{z^{-1}=-2} = -1,\qquad B = \left.\frac{1}{1+\frac12 z^{-1}}\right|_{z^{-1}=-1} = 2.
> $$
> **Answer.** $y[n] = \left[2(-1)^{n} - \left(-\tfrac12\right)^{n}\right]u[n]$. Check: $y[0] = 1$, $y[1] = -\tfrac32$.

> [!trap] Traps
> - Full credit in #1 needs every ROC; correct PFE with incomplete ROCs earned 4/6.
> - Cancel common factors first: no ROC boundary at a cancelled pole (1b, 6).
> - Right-sided 1(b) has $x[-1] = 1$: ROC $2 < \lvert z\rvert < \infty$, not $\lvert z\rvert > 2$.
> - Bounded $h$ is not enough: $u[n]$ is bounded and unstable.
> - Stable cascade: with $h_1$ first, input $u[n]$ makes the internal signal grow like $2n$.

**On the exam:** LCCDE → $H(z)$ → response on every exam, e.g. [[exams/midterm-1/past-exams/spring-2023|SP2023 #5]] (input cancels the unstable pole).

## Related

[[concepts/region-of-convergence|region of convergence]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/system-algebra|system algebra]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/lccde|LCCDE]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[homework/hw3|HW3]]

### Sources for this page

ECE 310 Fall 2026 HW4 and official solutions v1.0, including the rubric; Lecture notes 8–11 (Snyder); past Midterm 1 exams cited above.
