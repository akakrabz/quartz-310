---
title: "Demo — Difference-equation simulator (recursion, poles, stability, resonance)"
description: "Enter the a and b coefficients of a causal LCCDE and an input. The demo runs the recursion sample by sample, draws the poles, zeros and ROC, and says whether the system is stable, marginally stable or unstable, and whether this particular output stays bounded."
tags: [demo, lccde, stability, z-transform, midterm-1]
---

*Demo · pairs with [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/09-transfer-functions|Lecture 9]] and [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · recipes: [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]], [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]] · concepts: [[concepts/lccde]], [[concepts/bibo-stability]], [[concepts/marginal-stability]]*

<div class="ece-demo">
<iframe src="/static/demos/difference-equation/" title="Difference-equation simulator — interactive demo" loading="lazy" style="height:1450px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/difference-equation/) if the frame is cramped on your screen.

The equation is in the course's standard form (Lecture 9), $y[n] + \sum_{k\ge1} a_k\,y[n-k] = \sum_{k\ge0} b_k\,x[n-k]$, with $a_0 = 1$. It is causal and starts at rest, with zero initial conditions. These are the same `b, a` you would pass to `scipy.signal.lfilter(b, a, x)`. Fields accept exact values such as `1/3`, `sqrt(2)/2` and `exp(j*pi/4)`, or a product of factors such as `(1, -3/4)(1, -j)`, which the demo multiplies out. It shows:

- $x[n]$ and $y[n]$ for $0 \le n \le N$;
- the poles (×) and zeros (○) of $H(z)$, the input's own poles (◇) and zeros (□), and the causal ROC;
- a two-part verdict: is the **system** BIBO stable, and is **this output** bounded;
- a "real time" table that evaluates the recursion for the first six samples.

## What to try

1. **Run it the way a DSP chip does.** Load $y[n] = \tfrac12 y[n-1] + x[n]$ and read the real-time table. Each new $y[n]$ uses the current input and one stored number, $y[n-1]$, so the chip needs no convolution sum and no z-transform. Switch the input to $u[n]$ to get the step response $2 - (\tfrac12)^n$ ([[concepts/step-response]]).
2. **Mind the sign flip between Lecture 5 and Lecture 9.** *Lecture 5 Exercise 1* is $y[n] = \tfrac14 y[n-1] - x[n] + \tfrac12 x[n-2]$. In standard form the feedback term moves to the left: $a = (1, -\tfrac14)$ and $b = (-1, 0, \tfrac12)$. The table reproduces the notes' answer: $h[0], h[1], h[2] = -1, -\tfrac14, \tfrac{7}{16}$.
3. **Cancel a pole, then check the answer.** *HW4 #6* has $1 + z^{-1} + \tfrac14 z^{-2} = (1 + \tfrac12 z^{-1})^2$, and the zero at $-\tfrac12$ cancels one of the two poles (drawn as a grey ⊗). The input $(-1)^n u[n]$ has a pole at $-1$ on the unit circle, but H has no pole there. So the output stays bounded and settles to $2(-1)^n$: $y[n] = [2(-1)^n - (-\tfrac12)^n]u[n]$ ([[homework/hw4|HW4 #6]]).
4. **Marginal stability means resonance with one specific input.** The *accumulator* $1/(1 - z^{-1})$ with $u[n]$ gives $y[n] = n + 1$: a bounded input and an unbounded output. Switch the input to $(-1)^n u[n]$ and the output is bounded, because the pole at $-1$ is not shared. *SP2021 #5* shows the same thing in pairs: $\cos(\pi n/2)u[n]$ resonates with the poles $\pm j$, and $\cos(\pi n/3)u[n]$ does not ([[exams/midterm-1/past-exams/spring-2021|SP2021 #5]]).
5. **The FA2025 #8b trap.** $\sin(\pi n/2)u[n]$ contains $j^n$, which shares the pole at $j$, so the output is unbounded. Now choose $\cos$ with $\omega_0 = 2/3$. The third pole is $e^{j2/3}$, at an angle of $2/3$ rad $\approx 0.21\pi$, not $2\pi/3$. The z-plane shows the ◇ nowhere near the ×, and the output is bounded (the key says False). Also try aⁿu[n] with $a$ = `j` and with $a$ = `2/3` ([[exams/midterm-1/past-exams/fall-2025|FA2025 #8]]).
6. **One complex pole, six inputs.** *SP2025 #6* has a single pole at $e^{j\pi/4}$. Predict each case first, then check: $u[n]$ bounded; $e^{j\pi n/4}u[n]$ unbounded; $e^{-j\pi n/4}u[n]$ and $e^{-j3\pi n/4}u[n]$ bounded; $\cos(\pi n/4)u[n]$ unbounded (it contains $e^{j\pi n/4}$); $4^n u[n]$ unbounded ([[exams/midterm-1/past-exams/spring-2025|SP2025 #6]]).
7. **Which pole the input cancels decides everything.** In *SP2025 #8* the input's zero at $-\tfrac32$ (□) cancels the **unstable** pole, so the output is bounded even though the system is not. In *FA2025 #6* the input cancels only the stable pole $-\tfrac23$, so $3(2)^n$ survives and the plot is clipped. In *FA2019 #10* H's zero at $2$ cancels the *input's* pole, so even $2^n u[n]$ gives a bounded output ([[exams/midterm-1/past-exams/fall-2019|FA2019 #10]], [[concepts/pole-zero-cancellation]]).
8. **Find the parameter that makes it stable (SP2025 #7).** Enter $a$ = `1, 3/2, -1` (poles $-2$ and $\tfrac12$). Then set $b = (1, 0, -\alpha^2)$ for each candidate: `1, 0, -4` for $\alpha = \pm2$, `1, 0, 4` for $\alpha = \pm j2$, and `1, 0, -1/2` for $\alpha = \tfrac{\sqrt2}{2}$. The system is stable only when the zero at $-2$ cancels the pole at $-2$ ([[problems/parameters-for-stability]]).
9. **Nudge a coefficient, lose stability.** The course notebook's Butterworth filter has poles at $\pm0.414j$. Changing $a_2$ from $0.17157$ to $1.01$ moves them to $\pm1.005j$, just outside the unit circle. The growth is slow (about ×4.4 over 300 samples), which is why the verdict comes from the poles, not from looking at the plot.

## What the demo is (and isn't)

It simulates **causal** systems that start at rest, with inputs that start at $n = 0$. This is the course's standing assumption from Lecture 5. The recursion is exactly `lfilter(b, a, x)`: direct form, divided through by $a_0$. For every preset, its output was checked against scipy for all plotted samples. Where the notes, homework or an exam key give a closed form, the output was checked against that too. Two-sided or anti-causal systems are not simulated; run those as backwards recursions ([[problems/two-sided-systems-as-recursions]]).

The **system verdict** uses the poles of $H(z)$ after pole–zero cancellation:

- **BIBO stable:** every pole is inside the unit circle.
- **Marginally stable:** simple poles on the unit circle and none outside. This is still *not* BIBO stable (Lecture 11).
- **Unstable:** a pole outside the unit circle, or a repeated pole on it.

The **output verdict** uses the poles of $Y(z) = H(z)X(z)$ after every cancellation between H and the input. The output is unbounded exactly when a pole lies outside the unit circle, or a repeated pole lies on it. This is the pole-matching rule from Lecture 11. The same rule reproduces the answer keys of FA2025 #8, SP2025 #6 and SP2021 #5(b) for every input the demo can express. The one it cannot is FA2025 #8a(ii), a sum of two exponentials.

The plot shows only $N + 1$ samples, and it can mislead in both directions. A slowly diverging output (the Butterworth example) looks almost flat over 40 samples. A bounded one can look large: SP2021 #5 with $\cos(\pi n/3)u[n]$ keeps reaching $\lvert y[n]\rvert = 6$ and never grows beyond it. Very large outputs are clipped (▲) and labelled "growing without bound". Complex signals are drawn as $\operatorname{Re}$ (stems) with $\lvert\cdot\rvert$ (dotted).

"On the unit circle" means within $10^{-9}$ of $\lvert z\rvert = 1$. Type exact values (`sqrt(2)/2`, `exp(j*pi/4)`, `1/3`) rather than rounded decimals: $0.7071$ is not $\tfrac{\sqrt2}{2}$, and a pole at $0.99998$ is, strictly, inside.

The same check in Python, for HW4 #6:

```python
import numpy as np
from scipy.signal import lfilter
n = np.arange(8)
x = (-1.0) ** n                              # (−1)^n u[n]
y = lfilter([1, 0.5], [1, 1, 0.25], x)       # HW4 #6: b = [1, 0.5], a = [1, 1, 0.25]
print(y)
print(2 * (-1.0) ** n - (-0.5) ** n)         # closed form 2(−1)^n − (−1/2)^n
```

```text
[ 1.        -1.5        1.75      -1.875      1.9375    -1.96875
  1.984375  -1.9921875]
[ 1.        -1.5        1.75      -1.875      1.9375    -1.96875
  1.984375  -1.9921875]
```

## Related

[[concepts/lccde]] · [[concepts/fir-and-iir]] · [[concepts/block-diagram]] · [[concepts/transfer-function]] · [[concepts/poles-and-zeros]] · [[concepts/pole-zero-cancellation]] · [[concepts/bibo-stability]] · [[concepts/marginal-stability]] · [[problems/lccde-to-transfer-function-and-response]] · [[problems/unbounded-outputs-and-pole-matching]] · [[problems/parameters-for-stability]] · [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] · [[demos/pole-zero-and-roc-explorer]] · [[demos/convolution-explorer]] · [[supplements/demo-notebooks|course notebooks]] (`demo_difference_equations.ipynb`, `demo_stability.ipynb`)

### Sources for this page

Lecture 5 notes §1: LCCDE form, moving average Eqs. 3–4, the $\tfrac12 y[n-1] + x[n]$ example (Eqs. 5–7) and Exercise 1. Lecture 9 (standard form and $H(z)$). Lecture 11 notes §1.2 (unstable inputs, marginal stability, resonance). HW4 #6 and its solution. Exam keys: SP2021 #5, FA2025 #6 and #8, SP2025 #6, #7 and #8, FA2019 #10. Course notebooks `demo_difference_equations.ipynb` (direct programming vs `lfilter`) and `demo_stability.ipynb` (`butter(2, 0.5)`, then `a1[2] = 1.01`).
