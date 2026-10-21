---
title: "Lecture 3 — Discrete-time systems: linearity, time-invariance, causality, stability"
description: "What a discrete-time system is, and how to prove or disprove the four properties of every Midterm 1 property table: linearity, time-invariance (shift test), causality, BIBO stability."
tags: [lecture, midterm-1, systems]
lecture: 3
---

*Lecture 3 · Fri Aug 28, 2026 · notes + slides "Discrete-time systems" · prev: [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] · next: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]*

> [!abstract] In one breath
> - A system is any rule $T$ with $y[n] = T(x[n])$.
> - Four yes/no properties: linear (superposition), time-invariant (shift in ⇒ same shift out), causal (no future inputs), BIBO stable (bounded in ⇒ bounded out).
> - Prove for *every* input; disprove with *one* counterexample.

## 1. Discrete-time systems

> [!key] Discrete-time system
> Any computational process mapping a discrete-time input $x[n]$ to a discrete-time output $y[n]$. With operator $T$:
> $$
> x[n] \overset{T}{\longmapsto} y[n], \qquad y[n] = T(x[n]).
> $$
> "$x[n]$ maps to $y[n]$ by $T$"; "$y[n]$ is a function of $x[n]$ described by $T$".

Examples (notes, slides):

- $y[n] = x[n] - x[n-1]$: present minus previous sample; detects fast changes.
- $y[n] = \operatorname{median}\{x[n], x[n-1], x[n-2]\}$: running median.
- $y[n] = \text{HalfCenterCrop}(x[n])$, $\text{SnapchatFilter}(x[n])$: image operations.

**Systems are not just filters**: photo editing, speech recognition, trading algorithms, recommendation systems, de-noising filters all qualify.

## 2. Linearity, time-invariance, causality, and stability

LTI (linear, time-invariant) systems are the course's focus ([[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]); non-linear, time-varying and non-causal systems still appear in practice.

### 2.1 Linearity

> [!key] Linearity
> $T$ is **linear** if and only if
> $$
> \begin{aligned}
> T(a\,x[n]) &= a\,T(x[n]) &&\text{(homogeneity)}\\
> T(x_1[n] + x_2[n]) &= T(x_1[n]) + T(x_2[n]) &&\text{(additivity)}
> \end{aligned}
> $$
> or, equivalently, **superposition**: $T(a\,x_1[n] + b\,x_2[n]) = a\,T(x_1[n]) + b\,T(x_2[n])$ for all inputs and all $a, b$.

> [!recipe] Proving or disproving linearity
> - **Prove:** name $v[n] = a\,x_1[n] + b\,x_2[n]$, write $T(v[n])$ from the formula, regroup into $a\,T(x_1[n]) + b\,T(x_2[n])$.
> - **Disprove:** break homogeneity or additivity with one concrete input. First test: zero input must give zero output ($a = 0$); next try $a = -1$ or $a = 2$.

> [!question] Notes Exercises 1–2 and slides: linear?
> (E1) $y[n] = x[n] - x[n-1]$ (E2) $y[n] = (x[n])^p$, $p > 0$ (S1) $y[n] = \tfrac12 x[n] + \tfrac12 x[n-1]$ (S2) $y[n] = x[n] + 1$

> [!success]- Answers
> **E1, linear.** With $v[n] = a\,x_1[n] + b\,x_2[n]$:
> $$
> \begin{aligned}
> T(v[n]) &= v[n] - v[n-1] = \big(a\,x_1[n] + b\,x_2[n]\big) - \big(a\,x_1[n-1] + b\,x_2[n-1]\big)\\
> &= a\big(x_1[n] - x_1[n-1]\big) + b\big(x_2[n] - x_2[n-1]\big)\\
> &= a\,T(x_1[n]) + b\,T(x_2[n]). \ \checkmark
> \end{aligned}
> $$
> **E2, nonlinear.** $T(a\,x[n]) = a^p (x[n])^p = a^p\,T(x[n]) \neq a\,T(x[n])$ for $p \neq 1$.
> **S1, linear** (as E1). **S2, nonlinear:** $T(a\,x[n]) = a\,x[n] + 1 \ne a\,x[n] + a$; $x = 0$ gives $y = 1$ (affine).

> [!question] Extra practice (slides): linear?
> (1) $y[n] = \lvert x[n]\rvert$ (2) $y[n] = n\,(x[n] - x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = \max\{0, x[n]\}$ (posted deck) or $x[n]\,x[0]$ (annotated deck) (5) the running median

> [!success]- Answers
> 1. Nonlinear: $T(a\,x) = \lvert a\rvert\,\lvert x[n]\rvert \neq a\,\lvert x[n]\rvert$ for $a < 0$.
> 2. **Linear**: the factor $n$ is the same for every input.
> 3. Nonlinear: $e^{a\,x[n]} \neq a\,e^{x[n]}$.
> 4. Nonlinear: $\max\{0, -x\} \neq -\max\{0, x\}$; $T(a\,x) = a^2\,x[n]\,x[0]$.
> 5. Nonlinear: windows $(1, 0, 0)$ and $(0, 1, 0)$ have median $0$, their sum $(1, 1, 0)$ median $1$.

### 2.2 Time-invariance

> [!key] Time-invariance (shift-invariance)
> $T$ is **time-invariant** if and only if, for every input and every integer $n_0$,
> $$
> \begin{gathered}
> y[n - n_0] = T(x[n - n_0]), \qquad \text{equivalently}\\
> T(x)[n-n_0] = T(x[n-n_0]), \qquad n \in \mathbb{Z}.
> \end{gathered}
> $$
> Left: system, then shift. Right: shift, then system. "LSI" on older exams = LTI.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 196" width="640" height="196" role="img" aria-label="Time-invariance compares shift-then-system with system-then-shift" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="18.0" y="57.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="56.0" y1="52.0" x2="91.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="98.0,52.0 91.0,48.1 91.0,55.9" fill="currentColor"/><rect x="100.0" y="30.0" width="96.0" height="44.0" rx="6" fill="var(--accent)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="148.0" y="57.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">T</text><line x1="196.0" y1="52.0" x2="255.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,52.0 255.0,48.1 255.0,55.9" fill="currentColor"/><text x="229.0" y="42.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><rect x="264.0" y="30.0" width="96.0" height="44.0" rx="6" fill="var(--accent2)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="312.0" y="57.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">delay n₀</text><line x1="360.0" y1="52.0" x2="393.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="400.0,52.0 393.0,48.1 393.0,55.9" fill="currentColor"/><text x="406.0" y="57.0" text-anchor="start" fill="var(--accent)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">y[n − n₀]</text><text x="18.0" y="151.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="56.0" y1="146.0" x2="91.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="98.0,146.0 91.0,142.2 91.0,149.8" fill="currentColor"/><rect x="100.0" y="124.0" width="96.0" height="44.0" rx="6" fill="var(--accent2)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="148.0" y="151.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">delay n₀</text><line x1="196.0" y1="146.0" x2="255.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,146.0 255.0,142.2 255.0,149.8" fill="currentColor"/><text x="229.0" y="136.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n − n₀]</text><rect x="264.0" y="124.0" width="96.0" height="44.0" rx="6" fill="var(--accent)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="312.0" y="151.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">T</text><line x1="360.0" y1="146.0" x2="393.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="400.0,146.0 393.0,142.2 393.0,149.8" fill="currentColor"/><text x="406.0" y="151.0" text-anchor="start" fill="var(--accent2)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">T(x[n − n₀])</text><text x="18.0" y="20.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.85">system, then shift  (“left side”)</text><text x="18.0" y="114.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.85">shift, then system  (“right side”)</text><text x="548.0" y="92.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;" opacity="0.9">equal for every</text><text x="548.0" y="108.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;" opacity="0.9">x and every n₀?</text><text x="548.0" y="128.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">⇔ time-invariant</text><line x1="510.0" y1="60.0" x2="540.0" y2="78.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="540.0" y1="136.0" x2="520.0" y2="142.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/></svg><figcaption><strong>The shift test compares two orders.</strong> Top: run the system, then delay by n₀; bottom: delay the input, then run the system — time-invariant exactly when both agree for every input and shift.</figcaption></figure>

> [!recipe] The shift test (the hardest of the four)
> 1. **Left:** write $y[n]$, replace **every** $n$ by $n - n_0$, including coefficients ($n$, $\lvert n\rvert$, $\cos(\pi n/2)$).
> 2. **Right:** apply the system to $v[n] = x[n - n_0]$. The system acts on $n$ only; $n_0$ is a constant inside $v$. If $y[n] = x[f(n)]$: left $x[f(n-n_0)]$, right $x[f(n) - n_0]$.
> 3. **Compare** for all $n$, $n_0$.

> [!question] Notes Exercises 3–5: time-invariant?
> (E3) $y[n] = x[\lvert n\rvert]$ (E4) $y[n] = x[n] - x[n-1]$ (E5) $y[n] = n\,x[3n]$

> [!success]- Answers
> **E3, time-varying.** Left $x[\lvert n-n_0\rvert]$; right $v[\lvert n\rvert] = x[\lvert n\rvert - n_0]$. At $n = 0$, $n_0 = 1$: $x[1]$ vs $x[-1]$. (The notes print $x[\lvert n\rvert - n_0\rvert]$; the stray bar is a typo.)
> **E4, time-invariant.** Left $x[(n-n_0)] - x[(n-n_0)-1]$; right $x[n-n_0] - x[n-1-n_0]$: equal.
> **E5, time-varying.** Left $(n-n_0)\,x[3n-3n_0]$; right $n\,x[3n-n_0]$. Only the argument of $x$ picks up the shift on the right.

> [!question] Slides: $y[n] = x[2n]$ with $x[n] = \{\underset{\uparrow}{2}, 4, 6, 1, 3, 5\}$, $n_0 = 1$

> [!success]- Answer
> Abstractly left $x[2n-2n_0]$, right $x[2n-n_0]$. Concretely:
> $$
> \begin{aligned}
> y[n] = x[2n] &= \{\underset{\uparrow}{2},\ 6,\ 3\} &&\text{(keeps } x[0], x[2], x[4])\\
> y[n-1] &= \{\underset{\uparrow}{0},\ 2,\ 6,\ 3\}\\
> T(x[n-1]) = x[2n-1] &= \{\underset{\uparrow}{0},\ 4,\ 1,\ 5\} &&\text{(keeps } x[-1], x[1], x[3], x[5])
> \end{aligned}
> $$
> Different: **time-varying** (different samples survive the downsampling).

> [!question] Extra practice (slides): time-invariant?
> (1) $y[n] = x[\lvert n\rvert]$ (2) $y[n] = n\,(x[n]-x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers
> 1. Time-varying (E3).
> 2. Time-varying: $y[n-n_0] = (n-n_0)\big(x[n-n_0] - x[n-n_0-1]\big)$ but $T(x[n-n_0]) = n\big(x[n-n_0] - x[n-1-n_0]\big)$.
> 3. Time-invariant: $T(v)[n] = e^{v[n]} = e^{x[n-n_0]} = y[n-n_0]$. Any memoryless function of $x[n]$ alone is TI.
> 4. Time-varying: $y[n-n_0] = x[n-n_0]\,x[0]$ but $T(x[n-n_0]) = x[n-n_0]\,x[-n_0]$.

### 2.3 Causality

> [!key] Causality
> **Causal**: the output depends only on **present or past** input and output samples; $y[n]$ never uses $x[m]$ with $m > n$.

> [!recipe] Causality check
> For each term $x[g(n)]$: is $g(n) \le n$ for **every** integer $n$, negative ones included? Any $n$ with $g(n) > n$ is a counterexample. Coefficients ($n$, $\cos(\pi n/3)$) do not select samples.

> [!question] Notes Exercise 6 and slides: causal?
> (E6) $y[n] = x[n] + x[n-2] - x[n-4]$ (S1) $y[n] = \tfrac13\big(x[n] + x[n-1] + x[n-2]\big)$ (S2) $y[n] = x[\lvert n\rvert]$

> [!success]- Answers
> **E6, S1 causal**: indices $n$, $n-2$, $n-4$ (and $n$, $n-1$, $n-2$) are all $\le n$.
> **S2 non-causal**: $y[-2] = x[2]$, a future input (harmless for $n \ge 0$).

> [!question] Extra practice (slides): causal?
> (1) $y[n] = x[\lvert n\rvert - n]$ (2) $y[n] = (n+1)\,(x[n] - x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers
> 1. Non-causal: $y[-1] = x[\lvert -1\rvert - (-1)] = x[2]$.
> 2. Causal: $x[n]$ and $x[n-1]$; the factor $(n+1)$ is irrelevant.
> 3. Causal.
> 4. Non-causal: $y[-1] = x[-1]\,x[0]$ needs the future $x[0]$.

### 2.4 Stability

> [!key] BIBO stability
> $T$ is **BIBO stable** if for **every** input with $\lvert x[n]\rvert < \beta < \infty$ for all $n$, $\lvert y[n]\rvert < \alpha < \infty$ for all $n$. $\alpha$ may depend on $\beta$, not on $n$.

> [!recipe] Stability check
> - **Stable:** assume $\lvert x[n]\rvert < \beta$; bound $\lvert y[n]\rvert$ by a constant (triangle inequality, $\lvert\sin(\cdot)\rvert \le 1$).
> - **Unstable:** **one** bounded input with unbounded output (grows as $n \to \pm\infty$, or infinite at some $n$: $\log 0$, division by $0$).

> [!question] Notes Exercise 7 and slides: BIBO stable?
> (E7) $y[n] = x^{10}[n] + e^{x[n]}$ (S1) $y[n] = \sin^2(x[n])$ (S2) $y[n] = \ln(\lvert x[n]\rvert)$

> [!success]- Answers
> **E7, stable:**
> $$
> \lvert y[n]\rvert \le \lvert x[n]\rvert^{10} + e^{\lvert x[n]\rvert} < \beta^{10} + e^{\beta} = \alpha < \infty .
> $$
> **S1, stable:** $0 \le y[n] \le 1$. **S2, unstable:** $x[n] = 0$ (or $\delta[n]$) gives $\ln 0 = -\infty$.

> [!question] Extra practice (slides): BIBO stable?
> (1) $y[n] = \dfrac{x[n]}{\lvert n\rvert + 1}$ (2) $y[n] = n\,(x[n]-x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers
> 1. Stable: $\lvert y[n]\rvert < \beta/(\lvert n\rvert + 1) \le \beta$.
> 2. **Unstable**: $x[n] = (-1)^n$ gives $\lvert y[n]\rvert = 2\lvert n\rvert \to \infty$.
> 3. Stable: $e^{x[n]} < e^{\beta}$.
> 4. Stable: $\lvert x[n]\,x[0]\rvert < \beta^2$.

### Reading the four properties off a formula

> [!recipe] A property-table row in 30 seconds
> | property | it **fails** when you see… | it **holds** for… |
> |---|---|---|
> | linear | a function of the input's value ($\lvert x\rvert$, $x^2$, $e^{x}$, $\log x$, $\sin x$, clip, max, median); a product of input samples ($x[n]\,x[n+1]$, $x[3]\,x[n]$); division by an input sample; an added constant ($x[n]+3$) | sums of input samples times fixed coefficients, even coefficients that depend on $n$; pure index maps $x[f(n)]$ |
> | time-invariant | $n$ outside the brackets ($n\,x[n]$, $\cos(\pi n/2)\,x[n]$, a window); an index map other than $n-k$ ($x[2n]$, $x[-n]$, $x[\lvert n\rvert]$); a fixed sample ($x[0]$, $x[2]$) | constant-coefficient sums of $x[n-k]$; any function of $x[n]$ alone; convolution with a fixed $h$ |
> | causal | some $n$ (try negative ones!) whose input index exceeds $n$: $x[n+1]$, $x[\lvert n\rvert]$, $x[2n]$, $x[0]$; convolution with $h[n] \ne 0$ for some $n < 0$ | only $x[n-k]$ with $k \ge 0$ |
> | BIBO stable | a multiplier that grows ($n$, $\lvert n\rvert$, $\log(\lvert n\rvert+1)$, $2^n$); $\log x$ or $1/x$ (a bounded input may be $0$); convolution with an $h$ that is not absolutely summable | bounded multipliers times bounded functions of finitely many input samples; convolution with $\sum_n \lvert h[n]\rvert < \infty$ |

> [!trap] Common misreadings
> - A factor of $n$ ($n\,x[n]$, $(0.8+0.8j)^n\,x[n]$) keeps a system **linear**; it breaks time-invariance.
> - $x[-n]$: left $x[-n+n_0]$, right $x[-n-n_0]$. Every index map other than $n-k$ is time-varying (and linear).
> - Check negative $n$: $x[2n]$ reads the past for $n < 0$ but $y[1] = x[2]$, non-causal.
> - $e^{x[n]}$ is stable; $2^n\,x[n]$ and $(0.8+0.8j)^n\,x[n]$ ($\lvert 0.8+0.8j\rvert \approx 1.13$) are not.
> - BIBO says nothing about unbounded inputs: "stable ⇒ unbounded in gives unbounded out" is False.

> [!exam] The property table — 7 of 7 past exams, 12 points
> Three systems × four yes/no boxes, graded on the boxes; plus True/False on the properties' independence. Every past row with proofs: [[exams/midterm-1/system-property-bank|system-property bank]]; recipe: [[problems/classifying-system-properties|classifying system properties]].
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(e), #2, #4]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(b), #2]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #2]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(a), #2]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(b), #2]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #3]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(f), #2]] · [[exams/midterm-1/true-false-bank|T/F bank]]

## Related

[[concepts/linearity|Linearity]] · [[concepts/time-invariance|Time-invariance]] · [[concepts/causality|Causality]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/lti-system|LTI system]] · [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · [[demos/practice-drills|practice drills]] · [[homework/hw1|HW1]] · [[homework/hw2|HW2]]

### Sources for this page

Snyder, Lecture 3 notes (§1, §2.1–2.4, Exercises 1–7) and slides with the annotated in-class deck (practice answers); past exams above.
