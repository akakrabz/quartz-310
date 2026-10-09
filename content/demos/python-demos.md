---
title: "Python demos — the course notebooks in eight snippets"
description: "Short, runnable numpy/scipy snippets adapted from the ECE 310 demo notebooks: convolution with index bookkeeping, LCCDEs with lfilter, partial fractions with residuez, poles and stability with tf2zpk, and a bounded input that produces an unbounded output. Each one is shown with its real output."
tags: [demo, convolution, lccde, z-transform, stability, midterm-1]
---

*Demo · Python companions to [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/08-inverse-z-transform|Lecture 8]] and [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · adapted from the course notebooks*

The course repository (`ece310-demos-main`) ships Jupyter notebooks. Five of them cover Midterm 1 material: `demo_signals.ipynb`, `demo_convolution.ipynb`, `demo_difference_equations.ipynb`, `demo_pfe_residuez.ipynb` and `demo_stability.ipynb`. They need **numpy, scipy and matplotlib**. The repository's `requirements.txt` also lists scikit-image, which the later notebooks use. The audio cells in `demo_signals` and `demo_stability` also read `resources/handel.wav` from the repository. The remaining notebooks (DTFT, DFT, sampling, filtering, filter design) are for after the midterm; see [[supplements/demo-notebooks]].

The snippets below are the notebooks' ideas cut down to numpy and scipy only, with no plotting. Each one runs as-is and was run for this page, with its output pasted underneath. The exam allows no calculator, so treat these as a way to **check your hand work tonight**, not to replace it.

> [!tip] Running them
> Paste a block into a notebook cell or a file and run `python3 file.py`. The printed output should match the block under it. Your numpy version may format arrays slightly differently.

## 1. A signal is an array plus an $n$ axis

numpy arrays have no idea where $n=0$ is, so keep the time axis next to the values (this is what `demo_signals.ipynb` does). $\delta[n-2]$ is 1 where `n == 2`: a shift to the **right** by 2. Every sequence on an exam needs its $n=0$ marker, and every array needs its `n` ([[1-signals-and-systems/01-digital-signals|Lecture 1]], [[concepts/kronecker-delta]], [[concepts/unit-step]]).

```python
import numpy as np
n = np.arange(-4, 7)                     # the time axis: n = -4, ..., 6
delta = (n == 0).astype(int)             # δ[n]
u = (n >= 0).astype(int)                 # u[n]
print("n           ", n)
print("δ[n-2]      ", (n == 2).astype(int))
print("u[n]-u[n-3] ", u - (n >= 3))      # 1 at n = 0, 1, 2
print("(1/2)^n u[n]", np.round(0.5**n * u, 3))
```

```text
n            [-4 -3 -2 -1  0  1  2  3  4  5  6]
δ[n-2]       [0 0 0 0 0 0 1 0 0 0 0]
u[n]-u[n-3]  [0 0 0 0 1 1 1 0 0 0 0]
(1/2)^n u[n] [0.    0.    0.    0.    1.    0.5   0.25  0.125 0.062 0.031 0.016]
```

## 2. Convolution with start-index bookkeeping

`np.convolve` returns the right numbers but always starts them at index 0. The true first index of $y = x * h$ is the sum of the first indices of $x$ and $h$, and the length is $L_x + L_h - 1$. This is [[exams/midterm-1/past-exams/fall-2025|FA2025 #3a]]: $h = \{1, 0, \underset{\uparrow}{1}\}$ starts at $n=-2$, so $y$ starts at $n=-2$ and $y[0]=4$, as in the key ([[problems/finite-length-convolution]], [[concepts/convolution]]).

```python
import numpy as np
x, nx = np.array([1, 2, 3, 0, -1, -2, -3]), 0   # FA2025 #3a: x starts at n = 0
h, nh = np.array([1, 0, 1]), -2                 # h = {1, 0, 1} with the arrow on the last 1
y = np.convolve(x, h)                           # np.convolve knows nothing about n ...
ny = nx + nh                                    # ... the first index of y is nx + nh
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

## 3. Impulse response of an LCCDE: a loop, then `lfilter`

This follows `demo_difference_equations.ipynb`. The loop runs the recursion exactly as the exam writes it ([[exams/midterm-1/past-exams/fall-2025|FA2025 #6]]), starting from rest. `lfilter(b, a, x)` implements the [[2-z-transform/09-transfer-functions|Lecture 9]] form $y[n] + \sum_k a_k\,y[n-k] = \sum_k b_k\,x[n-k]$, so the feedback coefficients **change sign** when they move to the left side: $+\tfrac43$ in the recursion becomes $-\tfrac43$ in `a`. [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] writes the recursion with the opposite sign convention, and mixing them up costs points. The samples roughly double each step because of the pole at 2, so this causal system is unstable ([[concepts/lccde]], [[problems/lccde-to-transfer-function-and-response]]).

```python
import numpy as np
from scipy.signal import lfilter
N = 8
x = np.zeros(N); x[0] = 1                  # x = δ[n], system initially at rest
y = np.zeros(N)
for n in range(N):                         # FA2025 #6: y[n] = 4/3 y[n-1] + 4/3 y[n-2] + x[n] - x[n-2]
    y1 = y[n-1] if n >= 1 else 0
    y2, x2 = (y[n-2], x[n-2]) if n >= 2 else (0, 0)
    y[n] = 4/3*y1 + 4/3*y2 + x[n] - x2
b = [1, 0, -1]                             # x-side: 1·x[n] + 0·x[n-1] - 1·x[n-2]
a = [1, -4/3, -4/3]                        # y-side moved to the LEFT, so the signs flip
h = lfilter(b, a, x)
print(np.round(y, 4))
print(np.round(h, 4), " same:", np.allclose(y, h))
```

```text
[ 1.      1.3333  2.1111  4.5926  8.9383 18.0412 35.9726 72.0183]
[ 1.      1.3333  2.1111  4.5926  8.9383 18.0412 35.9726 72.0183]  same: True
```

## 4. Partial fractions with `residuez`

This follows `demo_pfe_residuez.ipynb`. `R, P, K = residuez(b, a)` means

$$
H(z) = \sum_k \frac{R_k}{1 - P_k z^{-1}} + \sum_k K_k z^{-k},
$$

so `R` holds the $A_k$, `P` the poles $p_k$, and `K` the long-division coefficients $C_k$ of [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (`K` is empty for a proper $H$). The poles come out in no particular order, so match each `R` with its `P`. [[2-z-transform/08-inverse-z-transform|Lecture 8]], Exercise 1 gives $A = \tfrac15$ at $\tfrac13$ and $A = \tfrac95$ at 2. The Lecture 10 example gives $C_0 = \tfrac59$, $C_1 = -\tfrac43$, $A = \tfrac14$ at $-1$ and $A = \tfrac{7}{36}$ at 3.

`residuez` knows nothing about the ROC: whether each term becomes $A p^n u[n]$ or $-A p^n u[-n-1]$ is still your call ([[problems/all-possible-rocs]]). For a repeated pole it returns one term per power. The notebook's second example, `residuez([1], [1, -2, 1])`, gives `R = [0, 1]` with `P = [1, 1]`, meaning $\frac{0}{1-z^{-1}} + \frac{1}{(1-z^{-1})^2}$ ([[concepts/partial-fraction-expansion]]).

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

## 5. Poles, zeros, and "is the causal system stable?"

`demo_stability.ipynb` draws pole-zero plots with `tf2zpk`. That function reads the coefficients as powers of $z$, not $z^{-1}$. Padding `b` and `a` with zeros to the same length makes the two readings agree (the notebook's Butterworth `b` and `a` already have equal length). A causal system has ROC $|z| > \max|p_k|$, so it is stable exactly when every pole is inside the unit circle ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]], [[concepts/poles-and-zeros]], [[concepts/bibo-stability]]).

The last line is a trap. `tf2zpk` still lists the pole at 2, but the zero at 2 cancels it, and the [[exams/midterm-1/past-exams/fall-2019|FA2019 #10(d)]] cascade is **stable**: the key marks "unstable" False. Cancel common factors before you judge ([[concepts/pole-zero-cancellation]]).

```python
import numpy as np
from scipy.signal import tf2zpk
def poles_zeros(b, a):
    L = max(len(b), len(a))                 # tf2zpk reads coefficients as powers of z:
    b = np.r_[b, np.zeros(L - len(b))]      # pad b and a to equal length so that
    a = np.r_[a, np.zeros(L - len(a))]      # "powers of z^-1" means the same H(z)
    z, p, k = tf2zpk(b, a)
    return np.round(z, 4), np.round(p, 4)
cases = {"HW3 #4": ([1, -3], [1, 1/6, -1/3]), "FA2025 #6": ([1, 0, -1], [1, -4/3, -4/3]),
         "FA2019 #10": ([1, -2], np.convolve(np.convolve([1, -1/2], [1, -1/4]), [1, -2]))}
for name, (b, a) in cases.items():
    z, p = poles_zeros(b, a)
    print(f"{name:10s} zeros {z}  poles {p}  causal & stable: {np.all(np.abs(p) < 1)}")
```

```text
HW3 #4     zeros [3. 0.]  poles [-0.6667  0.5   ]  causal & stable: True
FA2025 #6  zeros [-1.  1.]  poles [ 2.     -0.6667]  causal & stable: False
FA2019 #10 zeros [2. 0. 0.]  poles [2.   0.5  0.25]  causal & stable: False
```

## 6. Check a closed-form $h[n]$ against `lfilter`

The quickest way to catch a PFE slip is to run `lfilter` on $\delta[n]$ and compare a dozen samples with your formula. Here is the Lecture 10 answer

$$
h[n] = \tfrac59\delta[n] - \tfrac43\delta[n-1] + \tfrac{7}{36}(3)^n u[n] + \tfrac14(-1)^n u[n].
$$

`lfilter` runs forward in time, so this only checks the **causal** ROC. For the other ROCs use the [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] ([[concepts/inverse-z-transform]], [[concepts/impulse-response]]).

```python
import numpy as np
from scipy.signal import lfilter
n = np.arange(12)
d = (n == 0).astype(float)                                  # δ[n]
h_py = lfilter([1, -3, 1, 4], [1, -2, -3], d)               # Lecture 10, causal
h_cf = 5/9*(n == 0) - 4/3*(n == 1) + 7/36*3.0**n + 1/4*(-1.0)**n
print("lfilter    :", np.round(h_py[:8], 6))
print("closed form:", np.round(h_cf[:8], 6))
print("max relative error:", np.max(np.abs(h_py - h_cf) / np.abs(h_py)))
```

```text
lfilter    : [  1.  -1.   2.   5.  16.  47. 142. 425.]
closed form: [  1.  -1.   2.   5.  16.  47. 142. 425.]
max relative error: 1.1102230246251565e-16
```

## 7. A bounded input with an unbounded output (marginal stability)

[[exams/midterm-1/past-exams/spring-2021|SP2021 #5]] has $H(z) = 3z^{-1}/(1+z^{-2})$ with poles $\pm j$ on the unit circle, so $h[n] = 3\sin(\tfrac{\pi}{2}n)u[n]$ is bounded but not absolutely summable. Every input below is bounded by 1. $u[n]$ and $(-1)^n u[n]$ oscillate at angles 0 and $\pi$, away from the poles, and give bounded outputs. $\cos(\tfrac{\pi}{2}n)u[n]$ and $j^n u[n]$ oscillate at the pole angle $\tfrac{\pi}{2}$ and grow in proportion to $n$. In the z-domain this is a double pole on the unit circle ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1). The results agree with the key: these inputs give unbounded outputs ([[concepts/marginal-stability]], [[problems/unbounded-outputs-and-pole-matching]]).

```python
import numpy as np
from scipy.signal import lfilter
b, a = [0, 3], [1, 0, 1]                  # SP2021 #5: H(z) = 3z^-1/(1 + z^-2), poles ±j
n = np.arange(4000)
inputs = {"u[n]": np.ones(n.size), "(-1)^n u[n]": (-1.0)**n,
          "cos(pi n/2) u[n]": np.cos(np.pi*n/2), "j^n u[n]": 1j**n}
for name, x in inputs.items():            # every input is bounded by 1
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

## 8. One coefficient away from unstable

This is the experiment in `demo_stability.ipynb`. The notebook's second-order Butterworth low-pass has poles at $\pm 0.4142j$. Changing one denominator coefficient, `a[2]`, from 0.1716 to 1.01 moves them to $\pm 1.005j$, just outside the unit circle. The impulse response then grows like $1.005^n$. That is invisible over the first hundred samples, but it reaches about 138 near $n=1000$ and about $1.8\times10^6$ near $n=3000$; the notebook plays the filtered audio and you can hear it blow up. Stability is decided by where the poles are, not by how reasonable the coefficients look ([[concepts/bibo-stability]], [[problems/parameters-for-stability]]).

```python
import numpy as np
from scipy.signal import butter, lfilter
b, a = butter(2, 0.5)                      # the low-pass filter of demo_stability.ipynb
a1 = a.copy(); a1[2] = 1.01                # nudge one feedback coefficient
d = np.r_[1.0, np.zeros(2999)]             # δ[n]
for name, aa in (("a ", a), ("a1", a1)):
    h = lfilter(b, aa, d)
    print(name, "|poles| =", np.round(np.abs(np.roots(aa)), 4),
          "  max|h| for n in [0,100), [1000,1100), [2900,3000):",
          [f"{np.max(np.abs(h[k:k+100])):.3g}" for k in (0, 1000, 2900)])
```

```text
a  |poles| = [0.4142 0.4142]   max|h| for n in [0,100), [1000,1100), [2900,3000): ['0.586', '0', '0']
a1 |poles| = [1.005 1.005]   max|h| for n in [0,100), [1000,1100), [2900,3000): ['0.954', '138', '1.76e+06']
```

(The stable filter's "0" is $0.4142^{1000}$, which is far below the smallest number a float can hold.)

## Why no DSP chip ever computes a z-transform at run time

$X(z) = \sum_n x[n]z^{-n}$ adds up **every** sample, past and future. Nothing that runs while the samples are still arriving can compute it, and nothing needs to. The z-transform is a pencil-and-paper tool: it turns convolution into multiplication so that you can find $H(z)$, its poles, the ROC, the stability verdict and a closed form for $h[n]$. What runs in a phone, a DSP chip, or inside `lfilter` is the difference equation itself:

$$
y[n] = -\sum_{k=1}^{N} a_k\,y[n-k] + \sum_{k=0}^{M} b_k\,x[n-k].
$$

That costs a handful of multiply-adds per output sample, plus a memory of the last few inputs and outputs. For FA2025 #6 it is two multiplications (by $\tfrac43$) and three additions per sample. The z-domain answers the design questions: is it stable, and what does it do. The recursion does the work. This is also why the anti-causal half of a two-sided system ([[problems/two-sided-systems-as-recursions|FA2025 #7(b)]]) can only be run backwards over stored data, never in real time.

## Related

[[demos/pole-zero-and-roc-explorer]] · [[demos/convolution-explorer]] · [[demos/difference-equation-simulator]] · [[concepts/convolution]] · [[concepts/lccde]] · [[concepts/partial-fraction-expansion]] · [[concepts/bibo-stability]] · [[concepts/marginal-stability]] · [[supplements/demo-notebooks]] · [[demos/index|all demos]]

### Sources for this page

Course notebooks `demo_signals.ipynb`, `demo_convolution.ipynb`, `demo_difference_equations.ipynb`, `demo_pfe_residuez.ipynb` and `demo_stability.ipynb` (ece310-demos-main); Lecture 8 notes (Exercise 1), Lecture 10 notes (Exercise 1), Lecture 11 notes (§1.2.1); HW3 #4; past Midterm 1 keys FA2025 #3a, #6, #7; SP2021 #5; FA2019 #10. Every snippet was run with numpy 2.4 / scipy 1.17 and its output pasted verbatim.
