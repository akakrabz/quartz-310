---
title: "BIBO stability"
description: "Bounded input ⇒ bounded output. Three equivalent tests (the definition, an absolutely summable h[n], an ROC that contains the unit circle), the HW4 proof, and the T/F traps every past exam sets."
tags: [concept, stability, systems, midterm-1]
aliases: ["BIBO stable", "BIBO stability", "stability", "stable", "unstable", "bounded-input bounded-output"]
---

> [!key] Three equivalent tests
> 1. **Definition (any system).** $T$ is BIBO stable if every bounded input gives a bounded output: $\lvert x[n]\rvert\le B_x<\infty$ for all $n$ $\Rightarrow$ $\lvert y[n]\rvert\le B_y<\infty$ for all $n$.
> 2. **LTI: impulse response.** Stable $\iff$ $h$ is absolutely summable:
> $$
> \sum_{n=-\infty}^{\infty}\lvert h[n]\rvert<\infty .
> $$
> 3. **LTI: transfer function.** Stable $\iff$ the ROC of $H(z)$ contains the unit circle $\lvert z\rvert=1$. Causal (ROC $\lvert z\rvert>\lvert p_{\max}\rvert$): all poles inside, $\lvert p\rvert<1$. Anti-causal (ROC $\lvert z\rvert<\lvert p_{\min}\rvert$): all poles outside. Two-sided (ROC $a<\lvert z\rvert<b$): $a<1<b$. Poles are counted **after** cancelling common factors.

**FIR ⇒ always stable**: $\sum\lvert h[n]\rvert$ is a finite sum of finite numbers ([[concepts/fir-and-iir|FIR and IIR]]). A pole *on* the unit circle is unstable ([[concepts/marginal-stability|marginal stability]]).

> [!recipe] Which test to use
> 1. **Not LTI** (a table row such as $\lvert n\rvert x[n]$, $e^{x[n]+1}$, $x[3]x[n]$): use the definition. Prove stability by bounding $\lvert y\rvert$ with $B_x$ (Lecture 3: $\lvert x^{10}[n]+e^{x[n]}\rvert\le B_x^{10}+e^{B_x}$). Disprove it with **one** bounded input whose output is unbounded: $x[n]=1$ into $\lvert n\rvert x[n]$ gives $\lvert n\rvert$; $x[n]=0$ into $\ln\lvert x[n]\rvert$ or $x[n]/x[2]$ gives $\pm\infty$.
> 2. **LTI with $h[n]$:** sum $\lvert h[n]\rvert$. $a^nu[n]$ is summable iff $\lvert a\rvert<1$; $a^nu[-n-1]$ iff $\lvert a\rvert>1$.
> 3. **LTI with $H(z)$ or an LCCDE:** factor, cancel, locate the poles, and check that the ROC (fixed by "causal", "stable" or a given ROC) contains $\lvert z\rvert=1$.

**Example ([[homework/hw4|HW4]] #5).** $h_2[n]=\delta[n]-3(\tfrac14)^nu[n-1]$: $\sum\lvert h_2\rvert=1+3\cdot\frac{1/4}{1-1/4}=2$, stable. $h_1[n]=2u[n]-2(\tfrac12)^nu[n]\to2$, not summable, unstable. In series, $h_1*h_2=4\big[(\tfrac12)^n-(\tfrac14)^n\big]u[n]$ with $\sum\lvert h\rvert=4(2-\tfrac43)=\tfrac83$: **stable**, because the zero of $H_2(z)=\frac{1-z^{-1}}{1-\frac14z^{-1}}$ at $z=1$ cancels the pole of $H_1$ at $z=1$ ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).

> [!derivation]- Proof: $\sum\lvert h\rvert<\infty\iff$ BIBO stable (HW4 #2)
> **Sufficiency.** If $\lvert x[n]\rvert\le B_x$ for all $n$, the triangle inequality gives, for every $n$,
> $$
> \lvert y[n]\rvert=\Big\lvert\sum_k h[k]\,x[n-k]\Big\rvert\le\sum_k\lvert h[k]\rvert\,\lvert x[n-k]\rvert\le B_x\sum_k\lvert h[k]\rvert<\infty .
> $$
> **Necessity** (contrapositive). Suppose $\sum_k\lvert h[k]\rvert=\infty$ and choose the bounded input ($\lvert x[n]\rvert\le1$)
> $$
> x[n]=\begin{cases}h^*[-n]/\lvert h[-n]\rvert, & h[-n]\neq0\\ 0, & h[-n]=0\end{cases}\qquad(\text{real } h:\ x[n]=\operatorname{sgn}(h[-n])).
> $$
> Then $y[0]=\sum_k h[k]\,x[-k]=\sum_k h[k]\,h^*[k]/\lvert h[k]\rvert=\sum_k\lvert h[k]\rvert=\infty$: a bounded input, an unbounded output.

```python
import numpy as np
# HW4 #3: a CAUSAL system is BIBO stable iff every (uncancelled) pole has |p| < 1
dens = {"(a) z^2-5z+6": [1, -5, 6], "(b) z^2+1/9": [1, 0, 1/9],
        "(c) z-1": [1, -1], "(d) z^2+j": [1, 0, 1j]}
for name, a in dens.items():
    p = np.roots(a)
    verdict = "stable" if np.all(np.abs(p) < 1) else "NOT stable"
    print(f"{name:14s} |poles| = {np.round(np.abs(p), 3)}  {verdict}")
```

```text
(a) z^2-5z+6   |poles| = [3. 2.]  NOT stable
(b) z^2+1/9    |poles| = [0.333 0.333]  stable
(c) z-1        |poles| = [1.]  NOT stable
(d) z^2+j      |poles| = [1. 1.]  NOT stable
```

(None of the four numerators cancels a pole, so reading the denominators is enough here.)

> [!trap] The T/F statements that keep coming back
> - **Bounded $h$ does not mean stable.** $h=u[n]$ is bounded, $\sum\lvert h\rvert=\infty$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #1a]] F, [[0-midterm-1/past-exams/fall-2024|FA2024 #1b]] F, [[0-midterm-1/past-exams/fall-2019|FA2019 #1c]] F). Even $h=u[n]/(n+1)\to0$ is unstable (harmonic series).
> - **$\sum\lvert h\rvert<\infty$ is a test for LTI systems only** ([[0-midterm-1/past-exams/spring-2025|SP2025 #1b]] F): $y=n\,x[n]$ answers $\delta[n]$ with $0$, yet $x=1$ gives $y=n$.
> - **Stable system, unbounded input: the output can be bounded** ([[0-midterm-1/past-exams/fall-2025|FA2025 #1e]] F, [[0-midterm-1/past-exams/spring-2023|SP2023 #1b]] F): $h=\delta[n]-2\delta[n-1]$ turns $2^nu[n]$ into $\delta[n]$. Conversely one unbounded response to an unbounded input proves nothing ([[0-midterm-1/past-exams/fall-2019|FA2019 #1i]] F: $h=\delta[n]$ passes $3^nu[n]$).
> - **Unstable system: not every input blows up** ([[0-midterm-1/past-exams/fall-2019|FA2019 #1j]] F): $u[n]*(\delta[n]-\delta[n-1])=\delta[n]$. Unstable means *some* bounded input does.
> - **Parallel:** stable + stable is stable, since $\sum\lvert h_1+h_2\rvert\le\sum\lvert h_1\rvert+\sum\lvert h_2\rvert$ ([[0-midterm-1/past-exams/spring-2025|SP2025 #1d]], [[0-midterm-1/past-exams/fall-2024|FA2024 #1c]], [[0-midterm-1/past-exams/fall-2023|FA2023 #1c]]: all T). Unstable + unstable can be stable: $u[n]+(\delta[n]-u[n])=\delta[n]$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #1f]] F).
> - **Series:** two unstable systems can cascade to a stable one ([[0-midterm-1/past-exams/spring-2021|SP2021 #1c]] F, [[0-midterm-1/past-exams/fall-2019|FA2019 #1d]] F), e.g. $\frac{1-2z^{-1}}{1-3z^{-1}}\cdot\frac{1-3z^{-1}}{1-2z^{-1}}=1$ (both causal).
> - **Two-sided can be stable** ([[0-midterm-1/past-exams/spring-2025|SP2025 #1f]] F): $(\tfrac12)^{\lvert n\rvert}$, $\sum=3$. Stable with poles $\tfrac14$ and $3$ forces a two-sided $h$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #1c]] T).
> - **A formula without an ROC does not decide stability**: $\frac{1}{1-0.5z^{-1}}+\frac{1}{1-2z^{-1}}$ is stable with ROC $\tfrac12<\lvert z\rvert<2$ ([[0-midterm-1/past-exams/fall-2024|FA2024 #1f]] F); $\frac{1-z^{-1}}{1-2z^{-1}}$ is stable with $\lvert z\rvert<2$ ([[0-midterm-1/past-exams/spring-2021|SP2021 #1a]] F).

**Where it appears.** [[1-signals-and-systems/03-system-properties|Lecture 3]] (definition), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] ($\sum\lvert h\rvert$), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] (ROC test, marginal stability); [[homework/hw4|HW4]] #2–#5. Problem families: [[problems/classifying-system-properties]] (the Stable column, 7/7 exams), [[problems/unbounded-outputs-and-pole-matching]] (7/7), [[problems/parameters-for-stability]], [[problems/all-possible-rocs]]. Exams beyond the T/F: [[0-midterm-1/past-exams/fall-2025|FA2025 #4c, #7, #8]], [[0-midterm-1/past-exams/spring-2025|SP2025 #6–#8]], [[0-midterm-1/past-exams/fall-2024|FA2024 #8]], [[0-midterm-1/past-exams/fall-2023|FA2023 #8]], [[0-midterm-1/past-exams/spring-2023|SP2023 #7]], [[0-midterm-1/past-exams/spring-2021|SP2021 #5, #7]], [[0-midterm-1/past-exams/fall-2019|FA2019 #10]]. All T/F items: [[0-midterm-1/true-false-bank]].

**Related.** [[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]] · [[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/causality|causality]] · [[concepts/system-algebra|system algebra]] · [[demos/pole-zero-and-roc-explorer]]

### Sources for this page
Lecture 3 §2.4 and Ex. 7; Lecture 4 §2.1; Lecture 11 §1 and Table 1; HW4 #2 (official proof), #3, #5 and solutions; T/F items of all seven past Midterm 1 exams. Numbers checked in `verify/concepts/verify_glossary_time.py`, `verify_stability.py` and `verify/exams/tf_bank.py`.
