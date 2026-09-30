---
title: "Step response"
description: "g[n] = h[n] * u[n], the running sum of the impulse response; h[n] = g[n] − g[n−1]; y = g * (x[n] − x[n−1]). What a step response does and does not say about stability."
tags: [concept, systems, convolution, midterm-1]
aliases: ["step response", "unit step response", "g[n]", "s[n]"]
---

> [!key] Definition and the three identities
> The step response of an LTI system is its output for $x[n]=u[n]$:
> $$
> g[n]=h[n]*u[n]=\sum_{k=-\infty}^{n}h[k]\qquad(\text{the running sum of } h),
> $$
> $$
> h[n]=g[n]-g[n-1],\qquad y[n]=g[n]*\big(x[n]-x[n-1]\big),\qquad G(z)=\frac{H(z)}{1-z^{-1}}.
> $$
> All three follow from $\delta[n]=u[n]-u[n-1]$ ([[concepts/unit-step|unit step]]); the middle one is [[homework/hw2|HW2]] #3.

**Worked examples.** [[0-midterm-1/past-exams/fall-2019|FA2019 #3b]]: $h=\frac12\delta[n+1]+\delta[n]+\frac12\delta[n-1]$, so $g[n]=\frac12u[n+1]+u[n]+\frac12u[n-1]$ (sum the shifted steps). [[0-midterm-1/past-exams/fall-2023|FA2023 #4]] runs it backwards: the step response is $\delta[n]+\delta[n-1]$, so $h[n]=g[n]-g[n-1]=\delta[n]-\delta[n-2]$, i.e. $h=\{\underset{\uparrow}{1},\,0,\,-1\}$.

**Causal and stable: $g[n]\to H(1)$.** The running sum converges to $\sum_n h[n]=H(1)$, the DC gain. For $h=(\frac12)^nu[n]$: $g[n]=\big(2-(\frac12)^n\big)u[n]\to H(1)=\frac{1}{1-1/2}=2$.

```python
import numpy as np
from scipy.signal import lfilter
u = np.ones(8)                        # u[n] on n = 0..7
print(lfilter([1], [1, -0.5], u))     # h = (1/2)^n u[n]: stable, g[n] -> H(1) = 2
print(lfilter([1], [1, 1], u))        # h = (-1)^n u[n]: bounded g, UNSTABLE system
```

```text
[1.        1.5       1.75      1.875     1.9375    1.96875   1.984375
 1.9921875]
[1. 0. 1. 0. 1. 0. 1. 0.]
```

> [!trap]
> - **A bounded step response does not prove stability.** $h=(-1)^nu[n]$ (pole at $z=-1$, not summable) has $g=\{1,0,1,0,\dots\}$. Stability needs *every* bounded input to give a bounded output ([[concepts/bibo-stability|BIBO stability]]).
> - **An unbounded step response does prove instability** ($u[n]$ is a bounded input): $H=\frac{z^{-1}}{1-z^{-1}}$ gives $y=n\,u[n]$ ([[0-midterm-1/past-exams/spring-2021|SP2021 #1d]] T); $\frac{z+1}{z-1}$ gives $(2n+1)u[n]$ ([[homework/hw4|HW4]] #3c). A pole at $z=1$ resonates with the step ([[concepts/marginal-stability|marginal stability]]).
> - **Dividing by $1-z^{-1}$ adds only a pole at $z=1$** (or cancels a zero of $H$ there), so a pole of $G$ at $\frac12$ must already be a pole of $H$ ([[0-midterm-1/past-exams/fall-2019|FA2019 #1h]] T).
> - $g$ is a **running sum**, not the sum of the whole $h$; keep the unit steps that say where each piece starts.

**Where it appears.** [[homework/hw2|HW2]] #3 (express $y$ through $g$), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §2.2.3 ($u[n]*(-\frac34)^nu[n]$ is a step response), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1 ($u[n]*u[n]=(n+1)u[n]$); [[0-midterm-1/past-exams/fall-2019|FA2019 #3b, #1h]], [[0-midterm-1/past-exams/fall-2023|FA2023 #4]], [[0-midterm-1/past-exams/spring-2021|SP2021 #1d]]. Problem family: [[problems/finding-h-from-input-output-pairs]].

**Related.** [[concepts/unit-step|unit step]] · [[concepts/impulse-response|impulse response]] · [[concepts/convolution|convolution]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/transfer-function|transfer function]]

### Sources for this page
HW2 #3 (official solution); Lecture 4 §2.2.3; Lecture 11 §1.2.1; FA2019 #3 and #1h, FA2023 #4, SP2021 #1d, HW4 #3c. Checked in `verify/concepts/verify_glossary_time.py` and `verify_systems.py`; the snippet was run as shown.
