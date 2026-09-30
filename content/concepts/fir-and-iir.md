---
title: "FIR and IIR systems"
description: "Finite vs. infinite impulse response: the Lecture 9 test on H(z), why every FIR system is BIBO stable, and why a feedback term does not by itself make a system IIR (the recursive moving average)."
tags: [concept, lccde, stability, systems, midterm-1]
aliases: ["FIR", "IIR", "finite impulse response", "infinite impulse response", "moving average", "FIR filter", "IIR filter"]
---

> [!key] Definitions and the test
> - **FIR:** $h[n]$ has finitely many nonzero samples. An [[concepts/lccde|LCCDE]] without feedback, $y[n]=\sum_j c_j\,x[n-j]$, has $h[n]=\sum_j c_j\,\delta[n-j]$: the coefficients *are* the impulse response. $H(z)$ is a polynomial in $z^{-1}$ (and $z$), so its only poles sit at $z=0$ (causal) or $z=\infty$ (non-causal).
> - **IIR:** infinitely many nonzero samples. That requires at least one **finite, nonzero pole that no zero cancels**.
> - **Test (Lecture 9, Fig. 1):** write $H(z)$, cancel common factors, and look for a remaining pole with $0<\lvert p\rvert<\infty$. One exists: IIR. None: FIR.
> - **FIR $\Rightarrow$ BIBO stable, always:** $\sum\lvert h[n]\rvert$ is a finite sum of finite numbers.

**Moving average (Lecture 5).** $y[n]=\frac1L\sum_{i=0}^{L-1}x[n-i]$ has $h[n]=\frac1L\big(u[n]-u[n-L]\big)$. The same system can be computed with two additions per sample instead of $L$, using feedback: $y[n]=y[n-1]+\frac1L\big(x[n]-x[n-L]\big)$. It is **still FIR**: in
$$
H(z)=\frac{1-z^{-L}}{L\,(1-z^{-1})}=\frac1L\sum_{k=0}^{L-1}z^{-k}
$$
the zero of $1-z^{-L}$ at $z=1$ cancels the pole.

```python
import numpy as np
from scipy.signal import lfilter
L = 4                                 # y[n] = y[n-1] + (x[n] - x[n-L]) / L
b = np.r_[1/L, np.zeros(L - 1), -1/L]
a = [1, -1]
d = np.zeros(10); d[0] = 1
print(lfilter(b, a, d))               # a feedback term, yet a FINITE impulse response
```

```text
[0.25 0.25 0.25 0.25 0.   0.   0.   0.   0.   0.  ]
```

**On the exam ([[0-midterm-1/past-exams/fall-2025|FA2025 #4]]).** The modified moving average $y[n]=\frac1L\sum_{k=0}^{L-1}x[n-Sk]$ with $L=3$, $S=4$ has $h[n]=\frac13\big(\delta[n]+\delta[n-4]+\delta[n-8]\big)$, and for every $L$, $S$ it is FIR, hence BIBO stable ($\sum\lvert h\rvert=1$): part (c) is True.

> [!trap]
> - **Feedback does not guarantee IIR**: the recursive moving average above is FIR. Always cancel first.
> - **Cancellation does not guarantee FIR either**: [[homework/hw4|HW4]] #6 has $H=\frac{1+0.5z^{-1}}{(1+0.5z^{-1})^2}=\frac{1}{1+0.5z^{-1}}$, still IIR with $h=(-\frac12)^nu[n]$.
> - "An LSI system with a finite-length impulse response can be BIBO stable or unstable" is **False** ([[0-midterm-1/past-exams/fall-2019|FA2019 #1e]]): FIR is always stable.
> - **FIR is not the same as causal**: $h=\frac12\delta[n+1]+\delta[n]+\frac12\delta[n-1]$ ([[0-midterm-1/past-exams/fall-2019|FA2019 #3]]) is FIR and non-causal (pole at $\infty$, ROC $0<\lvert z\rvert<\infty$).
> - **Poles at $z=0$ do not make a system IIR**: $z^{-3}=1/z^3$ is just $\delta[n-3]$.
> - **IIR is not the same as unstable**: $(\frac12)^nu[n]$ is IIR and stable.

**Where it appears.** [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] §1.1–1.2 (moving average, first IIR example), [[2-z-transform/09-transfer-functions|Lecture 9]] §1.2 (Fig. 1); [[homework/hw3|HW3]] #3a (an FIR $H_1(z)$ with ROC $z\neq0$), [[homework/hw4|HW4]] #6; [[0-midterm-1/past-exams/fall-2025|FA2025 #4]], [[0-midterm-1/past-exams/fall-2019|FA2019 #1e]]. Problem family: [[problems/lccde-to-transfer-function-and-response]]. Try it: [[demos/difference-equation-simulator]].

**Related.** [[concepts/lccde|LCCDE]] · [[concepts/impulse-response|impulse response]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/block-diagram|block diagram]] · [[concepts/transfer-function|transfer function]]

### Sources for this page
Lecture 5 §1.1–1.2 (Eqs. 2–7); Lecture 9 §1.2 and Fig. 1; HW3 #3a, HW4 #6; FA2025 #4, FA2019 #1e and #3. Checked in `verify/concepts/verify_glossary_time.py` and `verify_systems.py`; the snippet was run as shown.
