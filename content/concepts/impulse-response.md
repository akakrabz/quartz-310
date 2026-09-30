---
title: "Impulse response"
description: "h[n] = T{δ[n]}: for an LTI system, the whole system in one sequence. Four ways to get it (read off a formula, run an LCCDE, combine an input–output pair, difference a step response) and what it tells you."
tags: [concept, systems, convolution, midterm-1]
aliases: ["impulse response", "unit pulse response", "unit-pulse response", "unit impulse response", "UPR", "h[n]"]
---

> [!key] Definition (Lecture 4)
> $$
> h[n]=T\{\delta[n]\}
> $$
> For an [[concepts/lti-system|LTI system]]: $y=x*h$ for every input, and $H(z)=\mathcal{Z}\{h[n]\}$ is the [[concepts/transfer-function|transfer function]]. Read off $h$: **causal** $\iff h[n]=0$ for $n<0$; **stable** $\iff\sum\lvert h[n]\rvert<\infty$; **FIR** $\iff$ finitely many nonzero samples. Older exams call it the *unit pulse response*.

> [!recipe] Four ways to find $h[n]$
> 1. **Formula $y[n]=\sum_k c_k\,x[n-k]$:** the coefficients *are* $h$: $h[n]=\sum_k c_k\,\delta[n-k]$. ([[0-midterm-1/past-exams/fall-2025|FA2025 #4b]]: $L=3$, $S=4$ gives $h=\frac13(\delta[n]+\delta[n-4]+\delta[n-8])$.)
> 2. **LCCDE:** run the recursion with $x=\delta$ at initial rest (Lecture 5), or find $H(z)$ and invert it (Lecture 9). With several input terms, find $\hat h$ for the input $\delta[n]$ alone and superpose shifted copies (Lecture 5, Ex. 1).
> 3. **An input–output pair of an LTI system:** combine shifted copies of $x$ into $\delta[n]$; the same combination of shifted copies of $y$ is $h$ (HW2 #4, FA2019 #3, SP2023 #4). Or divide: $H(z)=Y(z)/X(z)$ (FA2024 #6, HW4 #4).
> 4. **The step response:** $h[n]=g[n]-g[n-1]$ ([[concepts/step-response|step response]]; FA2023 #4).

**Worked example ([[homework/hw2|HW2]] #4).** An LTI system maps $x[n]=3^{-n}u[n]$ to $y[n]=5^{-n}u[n-1]$. Because
$$
x[n]-\tfrac13x[n-1]=3^{-n}\big(u[n]-u[n-1]\big)=\delta[n],
$$
linearity and time-invariance give $h[n]=y[n]-\tfrac13y[n-1]=5^{-n}u[n-1]-\tfrac13\,5^{-(n-1)}u[n-2]=5^{-n}\big(u[n-1]-\tfrac53u[n-2]\big)$.

**From an LCCDE by machine** (Lecture 5, Ex. 1: $y[n]=\frac14y[n-1]-x[n]+\frac12x[n-2]$, closed form $h[n]=-(\frac14)^nu[n]+\frac12(\frac14)^{n-2}u[n-2]$):

```python
import numpy as np
from scipy.signal import lfilter
# Lecture 5, Exercise 1: y[n] = 1/4 y[n-1] - x[n] + 1/2 x[n-2]
b, a = [-1, 0, 0.5], [1, -0.25]     # move 1/4 y[n-1] to the left: a = [1, -1/4]
d = np.zeros(6); d[0] = 1          # delta[n] on n = 0..5
print(lfilter(b, a, d))            # h[n] by running the recursion
n = np.arange(6)
print(-0.25**n + 0.5 * 0.25**(n - 2.0) * (n >= 2))   # closed form from the notes
```

```text
[-1.         -0.25        0.4375      0.109375    0.02734375  0.00683594]
[-1.         -0.25        0.4375      0.109375    0.02734375  0.00683594]
```

> [!trap]
> - **Only LTI systems are described by $h$** ([[0-midterm-1/past-exams/fall-2024|FA2024 #1a]] F, [[0-midterm-1/past-exams/fall-2019|FA2019 #1b]] F): the median filter and $y=n\,x[n]$ both have $h=0$.
> - **Bounded $h$ is not stable $h$**: $h=u[n]$ ([[concepts/bibo-stability|BIBO stability]]).
> - **With feedback, $h$ is not the coefficient list**: $y[n]=\frac12y[n-1]+x[n]$ has $h=(\frac12)^nu[n]$, infinitely long ([[concepts/fir-and-iir|FIR and IIR]]).
> - **Undo shifts as well as scales**: if the input was $2\delta[n-2]$, then $h[n]=\frac12\,y[n+2]$ ([[0-midterm-1/past-exams/fall-2019|FA2019 #3]]: $h=\frac12\delta[n+1]+\delta[n]+\frac12\delta[n-1]$, not causal).
> - **Keep the unit steps** in pieces like $5^{-(n-1)}u[n-2]$: they say where each term starts.

**Where it appears.** [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §1, [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] §1, [[2-z-transform/09-transfer-functions|Lecture 9]] §1.1; [[homework/hw2|HW2]] #4, [[homework/hw3|HW3]] #3–#4, [[homework/hw4|HW4]] #4–#6. Problem families: [[problems/finding-h-from-input-output-pairs]] (7/7 exams: [[0-midterm-1/past-exams/fall-2025|FA2025 #4]], [[0-midterm-1/past-exams/spring-2025|SP2025 #3]], [[0-midterm-1/past-exams/fall-2024|FA2024 #3, #6]], [[0-midterm-1/past-exams/fall-2023|FA2023 #4]], [[0-midterm-1/past-exams/spring-2023|SP2023 #4, #6]], [[0-midterm-1/past-exams/spring-2021|SP2021 #7]], [[0-midterm-1/past-exams/fall-2019|FA2019 #3]]) and [[problems/lccde-to-transfer-function-and-response]].

**Related.** [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/lti-system|LTI system]] · [[concepts/convolution|convolution]] · [[concepts/step-response|step response]] · [[concepts/lccde|LCCDE]] · [[concepts/transfer-function|transfer function]] · [[concepts/inverse-z-transform|inverse z-transform]]

### Sources for this page
Lecture 4 §1 (Eq. 1, difference and median examples); Lecture 5 §1.2 and Exercise 1; Lecture 9 §1.1; HW2 #4 (official solution), HW4 #4; FA2019 #3, FA2025 #4. Checked in `verify/concepts/verify_systems.py` and `verify_glossary_time.py`; the snippet was run as shown.
