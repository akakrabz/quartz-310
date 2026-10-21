---
title: "Python demos — the course notebooks in four snippets"
description: "Runnable numpy/scipy snippets from the ECE 310 demo notebooks: convolution with index bookkeeping, LCCDEs with lfilter, partial fractions with residuez, a bounded input with unbounded output."
tags: [demo, convolution, lccde, z-transform, stability, midterm-1]
---

*Demo · Python companions to [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/09-transfer-functions|Lecture 9]] and [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

> [!abstract] In one breath
> - Course notebooks (`ece310-demos-main`, numpy + scipy + matplotlib) cut down to short snippets, each shown with its real output.
> - Use them to check hand work; the exam allows no calculator.
> - Later notebooks (DTFT, DFT, sampling, filters): [[supplements/demo-notebooks]].

## 1. Convolution with start-index bookkeeping

`np.convolve` starts at index 0. True start = start of $x$ + start of $h$; length $L_x + L_h - 1$. [[exams/midterm-1/past-exams/fall-2025|FA2025 #3a]] ([[problems/finite-length-convolution]]):

```python
import numpy as np
x, nx = np.array([1, 2, 3, 0, -1, -2, -3]), 0
h, nh = np.array([1, 0, 1]), -2                 # arrow on the last 1
y = np.convolve(x, h)
ny = nx + nh
n = np.arange(ny, ny + len(y))
print("n:", n)
print("y:", y)
print("y[0] =", y[n == 0][0], "  length", len(y), "=", len(x), "+", len(h), "- 1")
```

```text
n: [-2 -1  0  1  2  3  4  5  6]
y: [ 1  2  4  2  2 -2 -4 -2 -3]
y[0] = 4   length 9 = 7 + 3 - 1
```

## 2. LCCDE: a loop, then `lfilter`

`lfilter(b, a, x)` uses the Lecture 9 form $y[n] + \sum_k a_k\,y[n-k] = \sum_k b_k\,x[n-k]$: feedback coefficients change sign ([[exams/midterm-1/past-exams/fall-2025|FA2025 #6]], [[concepts/lccde]]).

```python
import numpy as np
from scipy.signal import lfilter
N = 8
x = np.zeros(N); x[0] = 1                  # δ[n], at rest
y = np.zeros(N)
for n in range(N):
    y1 = y[n-1] if n >= 1 else 0
    y2, x2 = (y[n-2], x[n-2]) if n >= 2 else (0, 0)
    y[n] = 4/3*y1 + 4/3*y2 + x[n] - x2
b = [1, 0, -1]
a = [1, -4/3, -4/3]                        # signs flipped
h = lfilter(b, a, x)
print(np.round(y, 4))
print(np.round(h, 4), " same:", np.allclose(y, h))
```

```text
[ 1.      1.3333  2.1111  4.5926  8.9383 18.0412 35.9726 72.0183]
[ 1.      1.3333  2.1111  4.5926  8.9383 18.0412 35.9726 72.0183]  same: True
```

The pole at 2 makes this causal system unstable.

## 3. Partial fractions with `residuez`

$$
H(z) = \sum_k \frac{R_k}{1 - P_k z^{-1}} + \sum_k K_k z^{-k}
$$

`R` = $A_k$, `P` = poles, `K` = long-division terms. It ignores the ROC: each term's side is your call ([[concepts/partial-fraction-expansion]], [[problems/all-possible-rocs]]).

```python
import numpy as np
from scipy.signal import residuez
np.set_printoptions(precision=5, suppress=True)
R, P, K = residuez([2, -1], [1, -7/3, 2/3])          # Lecture 8, Exercise 1
print("L8:  R =", R, " P =", P, " K =", K)
R, P, K = residuez([1, -3, 1, 4], [1, -2, -3])       # Lecture 10, improper
print("L10: R =", R, " P =", P, " K =", K)
print("compare: 9/5 =", 9/5, " 7/36 =", round(7/36, 5), " 5/9 =", round(5/9, 5))
```

```text
L8:  R = [0.2 1.8]  P = [0.33333 2.     ]  K = []
L10: R = [0.25    0.19444]  P = [-1.  3.]  K = [ 0.55556 -1.33333]
compare: 9/5 = 1.8  7/36 = 0.19444  5/9 = 0.55556
```

## 4. A bounded input with an unbounded output

[[exams/midterm-1/past-exams/spring-2021|SP2021 #5]]: $H(z) = 3z^{-1}/(1+z^{-2})$, poles $\pm j$. Inputs at the pole angle $\tfrac{\pi}{2}$ grow like $n$ ([[concepts/marginal-stability]]).

```python
import numpy as np
from scipy.signal import lfilter
b, a = [0, 3], [1, 0, 1]                  # poles ±j
n = np.arange(4000)
inputs = {"u[n]": np.ones(n.size), "(-1)^n u[n]": (-1.0)**n,
          "cos(pi n/2) u[n]": np.cos(np.pi*n/2), "j^n u[n]": 1j**n}
for name, x in inputs.items():
    y = lfilter(b, a, x)
    print(f"{name:17s} max|y| over n<400: {np.max(np.abs(y[:400])):7.1f}"
          f"   over n<4000: {np.max(np.abs(y)):7.1f}")
```

```text
u[n]              max|y| over n<400:     3.0   over n<4000:     3.0
(-1)^n u[n]       max|y| over n<400:     3.0   over n<4000:     3.0
cos(pi n/2) u[n]  max|y| over n<400:   600.0   over n<4000:  6000.0
j^n u[n]          max|y| over n<400:   600.0   over n<4000:  6000.0
```

> [!trap]
> - `tf2zpk` reads coefficients as powers of $z$; pad `b` and `a` to equal length.
> - Pole lists ignore cancellation: cancel common factors before judging stability ([[concepts/pole-zero-cancellation]]).
> - `lfilter` runs forward: it checks only the causal ROC.

## Related
[[demos/pole-zero-and-roc-explorer]] · [[demos/convolution-explorer]] · [[demos/difference-equation-simulator]] · [[concepts/convolution]] · [[concepts/bibo-stability]] · [[supplements/demo-notebooks]] · [[demos/index|all demos]]

### Sources for this page
Course notebooks `demo_convolution`, `demo_difference_equations`, `demo_pfe_residuez`, `demo_stability`; Lectures 8, 10, 11 notes; FA2025 #3a, #6; SP2021 #5 keys.
