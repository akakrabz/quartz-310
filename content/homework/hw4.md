---
title: "HW4 · All possible ROCs, BIBO stability, and system algebra"
description: "Worked solutions to ECE 310 Homework 4 (Fall 2026): inverse z-transforms for every possible ROC, the proof that BIBO stability is equivalent to absolute summability, stability of causal systems from their poles with bounded inputs that break the unstable ones, h[n] from an input-output pair, a cascade whose unstable pole is cancelled, and an LCCDE with a hidden pole-zero cancellation."
tags: [homework, midterm-1, z-transform, roc, stability, lccde]
---

*Homework 4 · due Fri Sep 25, 2026 (Gradescope) · Lectures 8–11 (inverse z for every ROC, transfer functions and system algebra, BIBO stability and causality) · 100 points (18 + 16 + 16 + 16 + 16 + 18) · official solutions v1.0 · prev: [[homework/hw3|HW3]] · [[homework/index|all homework]]*

> [!abstract] What HW4 trains
> HW4 is the homework closest to the second half of a Midterm 1: find every ROC and the sequence that goes with each (#1), know *why* stability means $\sum\lvert h[n]\rvert<\infty$ (#2), decide stability from pole radii and break an unstable system with a bounded input (#3), recover $h[n]$ from an input-output pair (#4), and see a pole cancelled by a zero in a cascade (#5) and inside an LCCDE (#6). You have solved this set before, so use the folded answers to re-test yourself.

| # | skill | problem family · lecture |
|---|---|---|
| 1 | all possible ROCs and the inverse for each; an improper $X(z)$ with a cancelling factor | [[problems/all-possible-rocs\|all possible ROCs]] · [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]] |
| 2 | proof: BIBO stable ⇔ $\sum_n \lvert h[n]\rvert < \infty$ | [[concepts/bibo-stability\|BIBO stability]] · [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 3 | stability of causal systems from pole radii; a bounded input that breaks each unstable one | [[problems/unbounded-outputs-and-pole-matching\|unbounded outputs, pole matching]] · [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 4 | $H = Y/X$, the causal ROC, $h[n]$, stability | [[problems/finding-h-from-input-output-pairs\|finding h from input-output data]] · [[2-z-transform/09-transfer-functions\|L9]] |
| 5 | cascade = product of transfer functions; a pole cancelled by a zero | [[concepts/pole-zero-cancellation\|pole-zero cancellation]] · [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 6 | LCCDE → $H(z)$ (hidden cancellation) → $h[n]$ → response | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z) ↔ response]] · [[2-z-transform/09-transfer-functions\|L9]] |

> [!tip] What the rubric rewarded (the exam grades the same way)
> - #1 (6 per part): full credit needs **every** valid ROC with its sequence. A correct PFE with incomplete ROC cases earned 4/6; correct poles alone, 2/6.
> - #2 (8 + 8): sufficiency and necessity are graded separately. An "if and only if" needs both directions.
> - #3 (4 per part): 3 points for the verdict *with* pole/ROC reasoning, 1 point for a bounded input that really produces an unbounded output ($\delta[n]$ fails in (c), $u[n]$ fails in (d)).
> - #4: 5 for $H(z)$, 5 for $h[n]$, 3 for poles/ROC, 2 for the verdict, 1 for the justification. Later parts are graded against *your* $H(z)$, so write it down.
> - #5: right verdicts for $h_1$ and $h_2$ but a wrong one for the cascade earned only 2/8 of the stability points.

## Problem 1 — every ROC, every sequence

> [!question] Problem 1 (18 pts)
> Find all the possible ROCs for the following z-transforms and determine the associated inverse z-transform for each case.
>
> (a) $\dfrac{z^2 - z}{z^2 + 3z + 2}$
>
> (b) $\dfrac{z^3 - z}{z^2 + 3z + 2}$
>
> (c) $\dfrac{1}{\left(1-\frac13 z^{-1}\right)\left(1-\frac15 z^{-1}\right)}$

> [!recipe] All possible ROCs in four steps
> 1. Write $X(z)$ in powers of $z^{-1}$, cancel common factors, and split off any improper part (long division, or a pure factor $z^{k}$).
> 2. PFE: $X(z) = \sum_k \dfrac{A_k}{1-p_k z^{-1}}$, with $A_k = \left(1-p_k z^{-1}\right)X(z)$ evaluated at $z = p_k$ (cover-up).
> 3. The ROCs are the annuli between consecutive distinct pole radii: $d$ distinct radii give $d+1$ ROCs.
> 4. In each annulus, a pole *inside* the annulus gives a right-sided term $A_k p_k^{n}u[n]$; a pole *outside* gives a left-sided term $-A_k p_k^{n}u[-n-1]$.

> [!success]- Solution (a) — two poles, three ROCs
> Divide top and bottom by $z^2$ and factor:
> $$
> X(z) = \frac{1-z^{-1}}{1+3z^{-1}+2z^{-2}} = \frac{1-z^{-1}}{\left(1+z^{-1}\right)\left(1+2z^{-1}\right)} = \frac{-2}{1+z^{-1}} + \frac{3}{1+2z^{-1}},
> $$
> with $A_1 = \left.\dfrac{1-z^{-1}}{1+2z^{-1}}\right|_{z^{-1}=-1} = \dfrac{2}{-1} = -2$ and $A_2 = \left.\dfrac{1-z^{-1}}{1+z^{-1}}\right|_{z^{-1}=-\frac12} = \dfrac{3/2}{1/2} = 3$. Poles at $z=-1$ and $z=-2$ (radii 1 and 2); zeros at $z=0$ and $z=1$.
>
> | ROC | pole $-1$ | pole $-2$ | $x[n]$ |
> |---|---|---|---|
> | $\lvert z\rvert < 1$ | left | left | $2(-1)^n u[-n-1] - 3(-2)^n u[-n-1]$ |
> | $1 < \lvert z\rvert < 2$ | right | left | $-2(-1)^n u[n] - 3(-2)^n u[-n-1]$ |
> | $\lvert z\rvert > 2$ | right | right | $-2(-1)^n u[n] + 3(-2)^n u[n]$ |
>
> **Answer.** The three rows above. The fourth combination (pole $-1$ left-sided, pole $-2$ right-sided) would need $\lvert z\rvert < 1$ and $\lvert z\rvert > 2$ at once. That set is empty, so it is not an answer.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 270" width="640" height="270" role="img" aria-label="The three possible ROCs for HW4 problem 1(a)" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M146.0,118.0 A36.0,36.0 0 1 0 74.0,118.0 A36.0,36.0 0 1 0 146.0,118.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="10.0" y1="118.0" x2="208.0" y2="118.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="214.0,118.0 208.0,114.7 208.0,121.3" fill="currentColor"/><line x1="110.0" y1="218.0" x2="110.0" y2="20.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="110.0,14.0 106.7,20.0 113.3,20.0" fill="currentColor"/><text x="212.0" y="134.0" text-anchor="end" fill="currentColor" style="font-size:11px;">Re</text><text x="116.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:11px;">Im</text><circle cx="110.0" cy="118.0" r="36.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><circle cx="110.0" cy="118.0" r="72.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><line x1="68.0" y1="112.0" x2="80.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="68.0" y1="124.0" x2="80.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="32.0" y1="112.0" x2="44.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="32.0" y1="124.0" x2="44.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="110.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="146.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="110.0" y="242.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| &lt; 1</text><text x="110.0" y="258.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms left-sided</text><path d="M394.0,118.0 A72.0,72.0 0 1 0 250.0,118.0 A72.0,72.0 0 1 0 394.0,118.0 Z M358.0,118.0 A36.0,36.0 0 1 0 286.0,118.0 A36.0,36.0 0 1 0 358.0,118.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="222.0" y1="118.0" x2="420.0" y2="118.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="426.0,118.0 420.0,114.7 420.0,121.3" fill="currentColor"/><line x1="322.0" y1="218.0" x2="322.0" y2="20.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="322.0,14.0 318.7,20.0 325.3,20.0" fill="currentColor"/><circle cx="322.0" cy="118.0" r="36.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><circle cx="322.0" cy="118.0" r="72.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><line x1="280.0" y1="112.0" x2="292.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="280.0" y1="124.0" x2="292.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="244.0" y1="112.0" x2="256.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="244.0" y1="124.0" x2="256.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="322.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="358.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="322.0" y="242.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">1 &lt; |z| &lt; 2</text><text x="322.0" y="258.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">two-sided</text><path d="M434.0,18.0 H634.0 V218.0 H434.0 Z M606.0,118.0 A72.0,72.0 0 1 0 462.0,118.0 A72.0,72.0 0 1 0 606.0,118.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="434.0" y1="118.0" x2="632.0" y2="118.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="638.0,118.0 632.0,114.7 632.0,121.3" fill="currentColor"/><line x1="534.0" y1="218.0" x2="534.0" y2="20.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="534.0,14.0 530.7,20.0 537.3,20.0" fill="currentColor"/><circle cx="534.0" cy="118.0" r="36.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><circle cx="534.0" cy="118.0" r="72.0" fill="none" stroke="currentColor" stroke-width="1.0" stroke-dasharray="4 3" opacity="0.6"/><line x1="492.0" y1="112.0" x2="504.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="492.0" y1="124.0" x2="504.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="456.0" y1="112.0" x2="468.0" y2="124.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="456.0" y1="124.0" x2="468.0" y2="112.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="534.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="570.0" cy="118.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="534.0" y="242.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| &gt; 2</text><text x="534.0" y="258.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms right-sided</text><text x="38.0" y="106.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">−2</text><text x="74.0" y="106.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">−1</text></svg><figcaption><strong>Two poles on different circles (|z| = 1 and |z| = 2) → three annuli → three sequences.</strong> Each pole's term is right-sided if the ROC lies outside that pole and left-sided if inside. The zeros (○ at 0 and 1) play no role in choosing the ROC.</figcaption></figure>

> [!success]- Solution (b) — cancel first, then handle the improper part
> Factor and cancel the common $(z+1)$:
> $$
> X(z) = \frac{z(z-1)(z+1)}{(z+1)(z+2)} = \frac{z(z-1)}{z+2} = \frac{z-1}{1+2z^{-1}} = \frac{z}{1+2z^{-1}} - \frac{1}{1+2z^{-1}} .
> $$
> After the cancellation the only finite pole is $z=-2$; the numerator's degree exceeds the denominator's, so there is also a pole at $z=\infty$. One finite pole radius gives **two** ROCs. The factor $z$ is a one-sample advance: $\dfrac{z}{1+2z^{-1}} \leftrightarrow (-2)^{n+1}u[n+1]$ (right-sided) or $-(-2)^{n+1}u[-n-2]$ (left-sided).
>
> **Answer.**
> - ROC $2 < \lvert z\rvert < \infty$: $x[n] = (-2)^{n+1}u[n+1] - (-2)^n u[n] = \delta[n+1] - 3(-2)^n u[n]$.
> - ROC $\lvert z\rvert < 2$: $x[n] = -(-2)^{n+1}u[-n-2] + (-2)^n u[-n-1] = -\tfrac12\delta[n+1] + 3(-2)^n u[-n-2]$.
>
> Check the first case by long division: $\dfrac{z-1}{1+2z^{-1}} = z - 3 + 6z^{-1} - 12z^{-2} + \cdots$, i.e. $x = \{1,\ \underset{\uparrow}{-3},\ 6,\ -12,\ \dots\}$ ✓.

> [!trap] Two ways to get 1(b) wrong
> - **Not cancelling $(z+1)$.** A cancelled factor is not a pole: there is no ROC boundary at $\lvert z\rvert = 1$ and no third case. (Keeping it anyway, its PFE coefficient comes out $0$.)
> - **Writing "$\lvert z\rvert > 2$" for the right-sided case.** That sequence has $x[-1] = 1$, so it is not causal and $z=\infty$ is excluded: $2 < \lvert z\rvert < \infty$.

> [!success]- Solution (c) — already factored
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
>
> **Answer.** The three rows. Only the last is causal, and only the last contains $\lvert z\rvert = 1$ (it would be the stable choice if this were an $H(z)$). Check: causal $x[0] = \tfrac52 - \tfrac32 = 1 = X(\infty)$ ✓.

**On the exam:** [[0-midterm-1/past-exams/fall-2023|FA2023 #6(a)]] is this problem ($H = \frac{1-z^{-1}}{(1-\frac12 z^{-1})(1-2z^{-1})}$: three ROCs in a table, the fourth combination empty); [[0-midterm-1/past-exams/fall-2019|FA2019 #7]] does it with poles $e^{j\pi/3}$ and $\tfrac12$; [[0-midterm-1/past-exams/fall-2025|FA2025 #7]] and [[0-midterm-1/past-exams/spring-2025|SP2025 #8]] then ask for the one stable ROC. Recipe: [[problems/all-possible-rocs|all possible ROCs]].

## Problem 2 — BIBO stable if and only if absolutely summable

> [!question] Problem 2 (16 pts)
> Show that an LSI system with unit pulse response $h[n]$ is BIBO stable if and only if $h[n]$ is absolutely summable, i.e. $\sum_{n=-\infty}^{\infty}\lvert h[n]\rvert < B < \infty$.

(LSI, "linear shift-invariant", is the older name for LTI.)

> [!success]- Solution — two directions
> **Sufficiency ($\sum\lvert h\rvert \le B$ ⇒ BIBO stable).** Let $\lvert x[n]\rvert \le M$ for all $n$. Then for every $n$
> $$
> \lvert y[n]\rvert = \Big\lvert \sum_{k=-\infty}^{\infty} h[k]\,x[n-k]\Big\rvert \le \sum_{k=-\infty}^{\infty}\lvert h[k]\rvert\,\lvert x[n-k]\rvert \le M\sum_{k=-\infty}^{\infty}\lvert h[k]\rvert \le MB < \infty ,
> $$
> a bound that does not depend on $n$: every bounded input gives a bounded output.
>
> **Necessity (BIBO stable ⇒ $\sum\lvert h\rvert < \infty$), by contrapositive.** Suppose $\sum_k\lvert h[k]\rvert = \infty$. Choose the input that lines every term up:
> $$
> x[n] = \begin{cases}\dfrac{h^{*}[-n]}{\lvert h[-n]\rvert}, & h[-n]\neq0\\[6pt] 0, & h[-n]=0\end{cases}
> \qquad\big(\text{for real } h:\ x[n] = \operatorname{sgn}(h[-n])\big).
> $$
> It is bounded, $\lvert x[n]\rvert \le 1$, yet at $n=0$
> $$
> y[0] = \sum_{k} h[k]\,x[-k] = \sum_{k}\frac{h[k]\,h^{*}[k]}{\lvert h[k]\rvert} = \sum_{k}\lvert h[k]\rvert = \infty .
> $$
> A bounded input with an unbounded output, so the system is not BIBO stable.
>
> **Answer.** Both directions together: **BIBO stable ⇔ $\sum_n\lvert h[n]\rvert < \infty$** (for LTI systems).

> [!warning] Small gap in the key: complex h[n]
> The key takes $x[n] = \operatorname{sgn}(h[-n]) = h[-n]/\lvert h[-n]\rvert$ and then uses $h[k]\operatorname{sgn}(h[k]) = \lvert h[k]\rvert$, which holds only for real $h$. The course does use complex systems (Problem 3(d) below), so take the conjugate as above. Example: for $h[n] = j^n u[n]$ the key's input gives $y[0] = \sum_k j^{2k} = 1 - 1 + 1 - \cdots$, which stays bounded, while the conjugated input gives $\sum_k 1 = \infty$.

> [!trap] The proof needs LTI, and "bounded h" is not enough
> Both directions use $y = x*h$, which is true only for LTI systems. And a bounded $h$ is not absolutely summable in general: $h[n] = u[n]$ is bounded by 1 and unstable (its step response is $(n+1)u[n]$).

**On the exam:** no past exam asks for the proof, but its hypotheses are True/False staples: "absolutely summable $h$ ⇒ stable, regardless of whether $S$ is LSI" ([[0-midterm-1/past-exams/spring-2025|SP2025 #1(b)]], False: needs LTI), "bounded $h$ ⇒ stable" ([[0-midterm-1/past-exams/fall-2025|FA2025 #1(a)]], False), "unstable ⇒ $h$ unbounded" ([[0-midterm-1/past-exams/fall-2019|FA2019 #1(c)]], False), and "the moving average is always stable" ([[0-midterm-1/past-exams/fall-2025|FA2025 #4(c)]], True: FIR, so $\sum\lvert h\rvert$ is a finite sum). All collected in the [[0-midterm-1/true-false-bank|T/F bank]].

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

> [!key] The rule used four times
> Causal ⇒ the ROC is everything outside the largest pole. Stable ⇔ the ROC contains the unit circle. So a causal system is stable ⇔ **every pole (after cancellation) has $\lvert p\rvert < 1$**. A pole *on* the unit circle ("marginally stable") is **not** BIBO stable. To break an unstable system, feed it a bounded input whose pole lands on a system pole that lies on or outside the unit circle.

> [!success]- Solution (a) — poles 2 and 3
> $z^2-5z+6 = (z-2)(z-3)$: poles at $2$ and $3$. The causal ROC $\lvert z\rvert > 3$ misses the unit circle, so the system is **NOT BIBO stable**.
>
> In powers of $z^{-1}$: $H(z) = \dfrac{1-4z^{-1}}{\left(1-2z^{-1}\right)\left(1-3z^{-1}\right)} = \dfrac{2}{1-2z^{-1}} - \dfrac{1}{1-3z^{-1}}$, so $h[n] = \left(2^{n+1}-3^{n}\right)u[n]$. The key's $\delta[n] + 4(2)^{n-1}u[n-1] - 3^n u[n-1]$ is the same sequence.
>
> **Bounded input:** $x[n] = \delta[n]$ gives $y[n] = h[n]$, which grows like $-3^n$. Here $h$ itself is unbounded, so the simplest input works ($u[n]$ works too).

> [!success]- Solution (b) — poles ±j/3
> $z^2 = -\tfrac19$ gives poles $z = \pm\tfrac{j}{3}$, both of magnitude $\tfrac13$. The causal ROC $\lvert z\rvert > \tfrac13$ contains the unit circle: **BIBO stable**. The zero at $z=7$ is irrelevant; zeros never decide stability.
>
> Concretely, $h = \{\underset{\uparrow}{0},\ 1,\ -7,\ -\tfrac19,\ \tfrac79,\ \dots\}$ and $\sum_n\lvert h[n]\rvert = 8\sum_{m\ge0}\left(\tfrac19\right)^m = 9$.

> [!success]- Solution (c) — a pole on the unit circle
> Single pole at $z=1$. The causal ROC $\lvert z\rvert > 1$ only touches the unit circle and does not contain it: **NOT BIBO stable** (marginally stable).
>
> $H(z) = \dfrac{1+z^{-1}}{1-z^{-1}} = \dfrac{1}{1-z^{-1}} + \dfrac{z^{-1}}{1-z^{-1}}$ gives $h[n] = u[n] + u[n-1] = \{\underset{\uparrow}{1},\ 2,\ 2,\ 2,\ \dots\}$: **bounded**, but not absolutely summable.
>
> **Bounded input:** $x[n] = u[n]$, whose pole sits on the system's pole: $y[n] = \sum_{k=0}^{n}h[k] = (2n+1)u[n]$, unbounded.

> [!trap] δ[n] is not a valid answer in 3(c)
> The impulse response $u[n]+u[n-1]$ is bounded, so $x = \delta[n]$ gives a bounded output. The input has to *hit the pole*: an input pole at $z=1$ turns the system's pole into a double pole, and $n\cdot1^n$ grows.

> [!success]- Solution (d) — poles on the unit circle, and a zero that blocks the obvious input
> $z^2 = -j = e^{-j\pi/2}$ gives $z = e^{-j\pi/4}$ and $z = e^{j3\pi/4}$, both with $\lvert z\rvert = 1$. The causal ROC $\lvert z\rvert > 1$ excludes the unit circle: **NOT BIBO stable** (marginally stable).
>
> **Bounded real input:** match a pole's angle. $x[n] = \cos\!\left(\tfrac{\pi}{4}n\right)u[n] = \tfrac12\left(e^{j\pi n/4}+e^{-j\pi n/4}\right)u[n]$ has a pole at $e^{-j\pi/4}$, which doubles the system pole there, and the output grows linearly: $y[n] = C\,(n+1)\,e^{-j\pi n/4} + (\text{bounded})$ with $\lvert C\rvert = \tfrac12\sin\tfrac{\pi}{8} \approx 0.19$. The input $\cos\!\left(\tfrac{3\pi}{4}n\right)u[n]$ works as well (it hits $e^{j3\pi/4}$).
>
> Two inputs that do **not** work: $u[n]$ (the zero at $z=1$ cancels its pole, so the output stays bounded) and $\delta[n]$ ($h[n]$ is a bounded oscillation).

> [!warning] Imprecise line in the key, 3(d)
> The key says the output "picks up a term proportional to $n\cos\!\left(\tfrac{\pi}{4}n+\varphi\right)$". Because $H(z)$ has the complex coefficient $j$, the output is complex and only the $e^{-j\pi n/4}$ half of the cosine resonates: the growing part is $C(n+1)e^{-j\pi n/4}$ (checked numerically, $\lvert y[n]\rvert \approx 0.19\,n$). The verdict and the input are right.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="Pole-zero plots of the four HW4 problem 3 systems with their causal ROCs" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M8.0,32.0 H156.0 V200.0 H8.0 Z M130.0,116.0 A48.0,48.0 0 1 0 34.0,116.0 A48.0,48.0 0 1 0 130.0,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="8.0" y1="116.0" x2="154.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="160.0,116.0 154.0,112.7 154.0,119.3" fill="currentColor"/><line x1="82.0" y1="200.0" x2="82.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="82.0,28.0 78.7,34.0 85.3,34.0" fill="currentColor"/><circle cx="82.0" cy="116.0" r="16.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="109.0" y1="111.0" x2="119.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="121.0" x2="119.0" y2="111.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="125.0" y1="111.0" x2="135.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="125.0" y1="121.0" x2="135.0" y2="111.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="82.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="146.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="12.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(a)</text><text x="82.0" y="220.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;font-weight:600;">NOT stable</text><path d="M166.0,32.0 H314.0 V200.0 H166.0 Z M263.3,116.0 A23.3,23.3 0 1 0 216.7,116.0 A23.3,23.3 0 1 0 263.3,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="166.0" y1="116.0" x2="312.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="318.0,116.0 312.0,112.7 312.0,119.3" fill="currentColor"/><line x1="240.0" y1="200.0" x2="240.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="240.0,28.0 236.7,34.0 243.3,34.0" fill="currentColor"/><circle cx="240.0" cy="116.0" r="70.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="235.0" y1="87.7" x2="245.0" y2="97.7" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="235.0" y1="97.7" x2="245.0" y2="87.7" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="235.0" y1="134.3" x2="245.0" y2="144.3" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="235.0" y1="144.3" x2="245.0" y2="134.3" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="170.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(b)</text><text x="240.0" y="220.0" text-anchor="middle" fill="var(--accent)" style="font-size:12px;font-weight:600;">stable</text><path d="M324.0,32.0 H472.0 V200.0 H324.0 Z M448.0,116.0 A50.0,50.0 0 1 0 348.0,116.0 A50.0,50.0 0 1 0 448.0,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="324.0" y1="116.0" x2="470.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="476.0,116.0 470.0,112.7 470.0,119.3" fill="currentColor"/><line x1="398.0" y1="200.0" x2="398.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="398.0,28.0 394.7,34.0 401.3,34.0" fill="currentColor"/><circle cx="398.0" cy="116.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="443.0" y1="111.0" x2="453.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="443.0" y1="121.0" x2="453.0" y2="111.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="348.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="328.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(c)</text><text x="398.0" y="220.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;font-weight:600;">NOT stable (marginal)</text><path d="M482.0,32.0 H630.0 V200.0 H482.0 Z M606.0,116.0 A50.0,50.0 0 1 0 506.0,116.0 A50.0,50.0 0 1 0 606.0,116.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><line x1="482.0" y1="116.0" x2="628.0" y2="116.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="634.0,116.0 628.0,112.7 628.0,119.3" fill="currentColor"/><line x1="556.0" y1="200.0" x2="556.0" y2="34.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="556.0,28.0 552.7,34.0 559.3,34.0" fill="currentColor"/><circle cx="556.0" cy="116.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.85"/><line x1="586.4" y1="146.4" x2="596.4" y2="156.4" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="586.4" y1="156.4" x2="596.4" y2="146.4" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="515.6" y1="75.6" x2="525.6" y2="85.6" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="515.6" y1="85.6" x2="525.6" y2="75.6" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="606.0" cy="116.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="486.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">(d)</text><text x="556.0" y="220.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;font-weight:600;">NOT stable (marginal)</text><text x="306.0" y="132.0" text-anchor="end" fill="currentColor" style="font-size:11px;" opacity="0.85">zero at 7 →</text></svg><figcaption><strong>Causal ⇒ ROC outside the largest pole; stable ⇔ that region contains the unit circle (dashed).</strong> (a) poles 2, 3 (drawn at a smaller scale). (b) poles ±j/3, well inside. (c) pole at 1 and (d) poles e<sup>−jπ/4</sup>, e<sup>j3π/4</sup> sit on the unit circle: the ROC |z| &gt; 1 only touches it, so these are marginally stable, which still means NOT BIBO stable. Scales differ between panels.</figcaption></figure>

> [!trap] Match the pole's angle exactly
> An input resonates only if its pole lands *exactly* on a system pole. [[0-midterm-1/past-exams/fall-2025|FA2025 #8(b)]] has a pole at $e^{j2/3}$ (angle $\tfrac23$ rad, not $\tfrac{2\pi}{3}$), so $\cos\!\left(\tfrac{2\pi}{3}n\right)u[n]$ gives a *bounded* output there.

**On the exam:** [[0-midterm-1/past-exams/spring-2023|SP2023 #7]] (causal $H = \frac{z-3}{z-4}$: a bounded input with unbounded output, an unbounded input with bounded output, a bounded pair) and [[0-midterm-1/past-exams/fall-2025|FA2025 #8]] (which inputs give bounded or unbounded outputs) are this problem in other clothes; [[0-midterm-1/past-exams/fall-2023|FA2023 #7(c)]] (pole at $-1$, break it with $(-1)^n u[n]$) and [[0-midterm-1/past-exams/spring-2021|SP2021 #5]] (poles $\pm j$) put the poles on the unit circle as in (c) and (d). Recipe: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]].

## Problem 4 — h[n] from one input-output pair

> [!question] Problem 4 (16 pts)
> The input $x[n] = 2^{n}\big(u[n] - 3u[n-1]\big)$ to an unknown LSI system produces the output $y[n] = \left(3^{n} - 2^{n}\right)u[n]$. Determine the unit pulse response $h[n]$ assuming the system is causal. Is the system BIBO stable?

> [!success]- Solution — divide the transforms, then let causality pick the ROC
> **Input.** $x[n] = 2^n u[n] - 3\cdot2^n u[n-1] = 2^n u[n] - 6\cdot2^{n-1}u[n-1]$, i.e. $x = \{\underset{\uparrow}{1},\ -4,\ -8,\ -16,\ \dots\}$:
> $$
> X(z) = \frac{1}{1-2z^{-1}} - \frac{6z^{-1}}{1-2z^{-1}} = \frac{1-6z^{-1}}{1-2z^{-1}},\qquad \lvert z\rvert > 2 .
> $$
> **Output.**
> $$
> \begin{aligned}
> Y(z) &= \frac{1}{1-3z^{-1}} - \frac{1}{1-2z^{-1}} = \frac{\left(1-2z^{-1}\right)-\left(1-3z^{-1}\right)}{\left(1-3z^{-1}\right)\left(1-2z^{-1}\right)}\\
> &= \frac{z^{-1}}{\left(1-3z^{-1}\right)\left(1-2z^{-1}\right)},\qquad \lvert z\rvert > 3 .
> \end{aligned}
> $$
> **Transfer function.** The factor $\left(1-2z^{-1}\right)$ cancels, and the input's zero at $z=6$ becomes a pole of $H$:
> $$
> H(z) = \frac{Y(z)}{X(z)} = \frac{z^{-1}}{\left(1-3z^{-1}\right)\left(1-6z^{-1}\right)} = \frac{-\frac13}{1-3z^{-1}} + \frac{\frac13}{1-6z^{-1}},
> $$
> with $A_1 = \left.\dfrac{z^{-1}}{1-6z^{-1}}\right|_{z^{-1}=\frac13} = \dfrac{1/3}{-1} = -\tfrac13$ and $A_2 = \left.\dfrac{z^{-1}}{1-3z^{-1}}\right|_{z^{-1}=\frac16} = \dfrac{1/6}{1/2} = \tfrac13$. Causal, so the ROC is $\lvert z\rvert > 6$ and both terms are right-sided.
>
> **Answer.** $h[n] = \tfrac13\left(6^{n} - 3^{n}\right)u[n]$, ROC $\lvert z\rvert > 6$; **not BIBO stable** (the ROC excludes the unit circle; $h[n]$ grows like $6^n$).

> [!note] Why the problem says "causal"
> $H(z)$ has poles at 3 and 6, so three ROCs are conceivable. The two-sided choice $3 < \lvert z\rvert < 6$, $h[n] = -\tfrac13\, 3^{n}u[n] - \tfrac13\, 6^{n}u[-n-1]$, **also** maps this $x$ to this $y$: its ROC overlaps $X$'s on $3<\lvert z\rvert<6$, and the zero of $X$ at $z=6$ removes that pole from $Y$. The stable choice $\lvert z\rvert < 3$ does not: it would output $-3^{n}u[-n-1] - 2^{n}u[n]$. So no stable LTI system produces this pair.

**On the exam:** [[0-midterm-1/past-exams/spring-2023|SP2023 #6]] (given $X(z)$ and $Y(z)$ of a causal, stable system: find $H$, $h$ and the LCCDE) and [[0-midterm-1/past-exams/spring-2021|SP2021 #7]] (given $x$ and $Y$: find $X$, $H$, the ROC of $Y$, $h$, stability) are this problem; [[0-midterm-1/past-exams/fall-2024|FA2024 #6]] identifies $H$ from a finite input-output pair. Recipe: [[problems/finding-h-from-input-output-pairs|finding h from input-output data]].

## Problem 5 — a cascade that is stable although one stage is not

> [!question] Problem 5 (16 pts)
> Two systems with unit-pulse responses
> $$
> h_1[n] = 2u[n] - 2\left(\tfrac12\right)^{n}u[n],\qquad h_2[n] = \delta[n] - 3\left(\tfrac14\right)^{n}u[n-1]
> $$
> are in serial connection. (a) For each of the individual systems, as well as for the overall system, determine whether it is BIBO stable. (b) Determine the unit pulse response of the overall system.

> [!success]- Solution (a) — each stage, then the product
> **$h_1$:** $h_1[n] \to 2$, so $\sum_n\lvert h_1[n]\rvert = \infty$: **not stable**. In the z-domain
> $$
> H_1(z) = \frac{2}{1-z^{-1}} - \frac{2}{1-\frac12 z^{-1}} = \frac{z^{-1}}{\left(1-z^{-1}\right)\left(1-\frac12 z^{-1}\right)},\qquad \lvert z\rvert > 1,
> $$
> with a pole on the unit circle.
>
> **$h_2$:** $\sum_n\lvert h_2[n]\rvert = 1 + 3\sum_{n\ge1}\left(\tfrac14\right)^n = 1 + 3\cdot\dfrac{1/4}{3/4} = 2 < \infty$: **stable**. Writing $3\left(\tfrac14\right)^n u[n-1] = \tfrac34\left(\tfrac14\right)^{n-1}u[n-1]$,
> $$
> H_2(z) = 1 - \frac{\frac34 z^{-1}}{1-\frac14 z^{-1}} = \frac{1-z^{-1}}{1-\frac14 z^{-1}},\qquad \lvert z\rvert > \tfrac14 .
> $$
> Note the **zero at $z=1$** (equivalently $\sum_n h_2[n] = H_2(1) = 0$).
>
> **Cascade:** $H = H_1H_2$, and the zero of $H_2$ cancels the pole of $H_1$:
> $$
> H(z) = \frac{z^{-1}}{\left(1-z^{-1}\right)\left(1-\frac12 z^{-1}\right)}\cdot\frac{1-z^{-1}}{1-\frac14 z^{-1}} = \frac{z^{-1}}{\left(1-\frac12 z^{-1}\right)\left(1-\frac14 z^{-1}\right)} .
> $$
> Both stages are causal, so the cascade is causal with ROC $\lvert z\rvert > \tfrac12$, which contains the unit circle.
>
> **Answer.** $h_1$ not stable, $h_2$ stable, **overall system BIBO stable**.

> [!success]- Solution (b) — PFE of the cancelled form
> $$
> H(z) = \frac{A}{1-\frac12 z^{-1}} + \frac{B}{1-\frac14 z^{-1}},
> $$
> $$
> A = \left.\frac{z^{-1}}{1-\frac14 z^{-1}}\right|_{z^{-1}=2} = \frac{2}{1/2} = 4,\qquad
> B = \left.\frac{z^{-1}}{1-\frac12 z^{-1}}\right|_{z^{-1}=4} = \frac{4}{-1} = -4 .
> $$
> **Answer.** $h[n] = h_1[n]*h_2[n] = 4\left[\left(\tfrac12\right)^{n} - \left(\tfrac14\right)^{n}\right]u[n]$, with $\sum_n\lvert h[n]\rvert = 4\left(2-\tfrac43\right) = \tfrac83$.

> [!trap] Stable overall does not mean every internal signal is bounded
> With $h_1$ first, the bounded input $u[n]$ makes the intermediate signal grow like $2n$, even though the final output settles at $H(1) = \tfrac83$. With $h_2$ first, every signal stays bounded. The input-output map is the same in either order ($H_1H_2 = H_2H_1$), and that map is what "BIBO stable" describes.

**On the exam:** the cancellation is a True/False staple: "if $h_1$ or $h_2$ is unstable, the cascade must be unstable" ([[0-midterm-1/past-exams/fall-2019|FA2019 #1(d)]], False) and "a cascade of two unstable systems cannot be stable" ([[0-midterm-1/past-exams/spring-2021|SP2021 #1(c)]], False); [[0-midterm-1/past-exams/fall-2019|FA2019 #10(d)]] cascades a stable $H$ (zero at 2) with $2^n u[n]$ and asks whether the result is unstable (False, the zero cancels the pole). Concept: [[concepts/pole-zero-cancellation|pole-zero cancellation]].

## Problem 6 — an LCCDE with a hidden cancellation

> [!question] Problem 6 (18 pts)
> Consider the following difference equation (LCCDE), with zero initial conditions:
> $$
> y[n] = x[n] + 0.5\,x[n-1] - y[n-1] - 0.25\,y[n-2],\qquad n = 0, 1, 2, \dots
> $$
> (a) Find the transfer function and its ROC. (b) Find the impulse response of the system. (c) Determine the output $y[n]$ for the input $x[n] = (-1)^n u[n]$.

> [!success]- Solution (a) — the denominator is a perfect square
> Standard form: $y[n] + y[n-1] + \tfrac14 y[n-2] = x[n] + \tfrac12 x[n-1]$. Taking z-transforms,
> $$
> H(z) = \frac{1+\frac12 z^{-1}}{1+z^{-1}+\frac14 z^{-2}} = \frac{1+\frac12 z^{-1}}{\left(1+\frac12 z^{-1}\right)^{2}} = \frac{1}{1+\frac12 z^{-1}} .
> $$
> The recursion runs forward from rest, so the system is causal.
>
> **Answer.** $H(z) = \dfrac{1}{1+\frac12 z^{-1}}$, **ROC: $\lvert z\rvert > \tfrac12$** (stable).

> [!success]- Solution (b)
> **Answer.** $h[n] = \left(-\tfrac12\right)^{n}u[n]$.
>
> The second-order recursion is secretly first order: one of the two poles at $-\tfrac12$ is cancelled by the zero at $-\tfrac12$.

> [!success]- Solution (c) — PFE of Y(z)
> $X(z) = \dfrac{1}{1+z^{-1}}$ with $\lvert z\rvert > 1$, so
> $$
> Y(z) = \frac{1}{\left(1+\frac12 z^{-1}\right)\left(1+z^{-1}\right)} = \frac{A}{1+\frac12 z^{-1}} + \frac{B}{1+z^{-1}},
> $$
> $$
> A = \left.\frac{1}{1+z^{-1}}\right|_{z^{-1}=-2} = -1,\qquad B = \left.\frac{1}{1+\frac12 z^{-1}}\right|_{z^{-1}=-1} = 2,
> $$
> with ROC $\lvert z\rvert > 1$, so both terms are right-sided.
>
> **Answer.** $y[n] = \left[2(-1)^{n} - \left(-\tfrac12\right)^{n}\right]u[n]$.
>
> Check against the recursion: $y[0] = 1$ and $y[1] = -1 + \tfrac12 - 1 = -\tfrac32$; the formula gives $2-1 = 1$ and $-2+\tfrac12 = -\tfrac32$ ✓.

> [!trap] Factor before you expand
> Skipping the cancellation leaves a PFE with a repeated pole at $-\tfrac12$ plus the input pole, three coefficients instead of two (the repeated-pole one comes out $0$). Legal, but slow and error-prone under exam time pressure.

**On the exam:** LCCDE → $H(z)$ → response is worth 15–20 points on every exam: [[0-midterm-1/past-exams/fall-2025|FA2025 #6]] (an input that cancels a pole), [[0-midterm-1/past-exams/spring-2025|SP2025 #8]], [[0-midterm-1/past-exams/spring-2023|SP2023 #5]] (the input $2\delta[n]-3\delta[n-1]$ cancels the unstable pole), [[0-midterm-1/past-exams/fall-2019|FA2019 #10]]. Recipe: [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]].

## Checking it in Python

`residuez` gives the PFE of Problem 1(a); `lfilter` on an impulse only ever produces the **right-sided** (causal) inverse, so the other two ROCs are yours to write down.

```python
import numpy as np
from scipy import signal

# HW4 #1(a): X(z) = (1 - z^-1)/(1 + 3z^-1 + 2z^-2)
b, a = [1, -1], [1, 3, 2]
r, p, k = signal.residuez(b, a)    # X = sum r_i/(1 - p_i z^-1) + k
print("A_k:", r, " p_k:", p, " k:", k)

n = np.arange(6)
x = signal.lfilter(b, a, (n == 0).astype(float))   # RIGHT-sided inverse
print(x)
print(-2 * (-1.0)**n + 3 * (-2.0)**n)              # the |z| > 2 answer
```

```text
A_k: [-2.  3.]  p_k: [-1. -2.]  k: []
[  1.  -4.  10. -22.  46. -94.]
[  1.  -4.  10. -22.  46. -94.]
```

Problem 3 in a few lines: for a causal system, stable ⇔ the largest pole magnitude is below 1. The denominators are written in powers of $z$, which is exactly what `np.roots` expects.

```python
import numpy as np

# denominators of HW4 #3 in powers of z (what np.roots expects)
dens = {"a": [1, -5, 6], "b": [1, 0, 1/9],
        "c": [1, -1], "d": [1, 0, 1j]}
for name, den in dens.items():
    p = np.roots(den)
    rmax = np.abs(p).max()
    verdict = "stable" if rmax < 1 - 1e-9 else "NOT stable"
    print(name, np.round(p, 4), "max|p| =", round(rmax, 4), verdict)
```

```text
a [3. 2.] max|p| = 3.0 NOT stable
b [-0.+0.3333j  0.-0.3333j] max|p| = 0.3333 stable
c [1.] max|p| = 1.0 NOT stable
d [ 0.7071-0.7071j -0.7071+0.7071j] max|p| = 1.0 NOT stable
```

(Check for cancellations first: a pole that a zero cancels does not count.)

## Related

[[concepts/region-of-convergence|region of convergence]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/partial-fraction-expansion|partial fraction expansion]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/causality|causality]] · [[concepts/transfer-function|transfer function]] · [[concepts/system-algebra|system algebra]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/lccde|LCCDE]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · prev: [[homework/hw3|HW3]]

### Sources for this page

- ECE 310 Fall 2026 Homework 4 (due Sep 25) and the official HW4 solutions, version 1.0 (Mia and Ethan), including the grading rubric quoted above.
- Lecture notes 8–11 (inverse z-transform, transfer functions parts 1 and 2, BIBO stability and causality).
- Past Midterm 1 exams cited in the "On the exam" lines (FA2025, SP2025, FA2024, FA2023, SP2023, SP2021, FA2019).
- Every answer on this page was re-derived and checked numerically (partial sums of the z-transform at test points inside each ROC, `lfilter` and direct convolution sums against the closed forms, `residuez` for the PFEs, long simulations for the bounded and unbounded outputs).
