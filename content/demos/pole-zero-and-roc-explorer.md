---
title: "Demo — Pole-zero plot and every possible ROC"
description: "Type H(z) in powers of z⁻¹ (or pick a homework or past-exam preset) and see its poles and zeros, every valid ROC, causality and BIBO stability for each, the partial-fraction coefficients, and h[n] as a formula and a stem plot."
tags: [demo, z-transform, roc, stability, midterm-1]
---

*Demo · pairs with [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] and [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · concepts: [[concepts/region-of-convergence]], [[concepts/partial-fraction-expansion]], [[concepts/bibo-stability]], [[concepts/pole-zero-cancellation]]*

<div class="ece-demo">
<iframe src="/static/demos/pole-zero-roc/" title="Pole-zero plot and ROC explorer — interactive demo" loading="lazy" style="height:1500px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/pole-zero-roc/) if the frame is cramped on your screen.

**How to type $H(z)$.** Give the coefficients of $z^{0}, z^{-1}, z^{-2}, \dots$ of the numerator (b) and the denominator (a, with $a[0]=1$), separated by commas. These are exactly the numbers in the [[2-z-transform/09-transfer-functions|Lecture 9]] form $y[n] + \sum_{k\ge1} a_k\,y[n-k] = \sum_{k\ge0} b_k\,x[n-k]$ and in `scipy.signal.lfilter(b, a, x)`. For example $H(z) = \dfrac{2 - z^{-1}}{1 - \frac73 z^{-1} + \frac23 z^{-2}}$ is b = `2, -1`, a = `1, -7/3, 2/3`. A product of factors also works: a = `(1, -1/3)(1, -2)` means $(1-\tfrac13 z^{-1})(1-2z^{-1})$. Fractions, `sqrt(2)/2` and `exp(j*pi/4)` are accepted.

> [!exam] Why this is worth ten minutes tonight
> Inverse z-transform, PFE and all-possible-ROCs problems appear on **7/7** past Midterm 1 exams, and so do unbounded-output, pole-matching and cancellation questions. Parameters-for-stability questions appear on 3/7. Every exercise below is a real homework or exam problem, and the demo's numbers match the keys (errata in [[0-toolkit/05-errata]]). The recipes are in [[problems/all-possible-rocs]] and [[problems/unbounded-outputs-and-pole-matching]].

## What to try

1. **Every ROC of one $H(z)$, from [[0-midterm-1/past-exams/fall-2023|FA2023 #6]].** Pick *FA2023 #6*. The poles at $\tfrac12$ and $2$ give three buttons: $|z|<\tfrac12$, $\tfrac12<|z|<2$ and $|z|>2$. Click through them and watch the last column of the partial-fraction table. The coefficients never change ($A = \tfrac13$ at $\tfrac12$, $A = \tfrac23$ at $2$); only the side each pole goes to changes. A pole on or inside the ROC's inner circle contributes $A\,p^n u[n]$, and a pole on or outside its outer circle contributes $-A\,p^n u[-n-1]$. That is the whole [[problems/all-possible-rocs|all-possible-ROCs recipe]]. *Lecture 8, Exercise 1* is the same computation; the notes give its all-right-sided and all-left-sided answers, and the demo adds the third (two-sided) one.
2. **Two poles give three ROCs, not four: [[0-midterm-1/past-exams/fall-2019|FA2019 #7]].** Type b = `2, -(1/2 + exp(j*pi/3))`, a = `(1, -exp(j*pi/3))(1, -1/2)`. That is $\frac{1}{1-e^{j\pi/3}z^{-1}} + \frac{1}{1-\frac12 z^{-1}}$ over a common denominator, so both $A$'s are 1. Only $|z|<\tfrac12$, $\tfrac12<|z|<1$ and $|z|>1$ appear. Making the pole at $\tfrac12$ left-sided and the pole at $e^{j\pi/3}$ right-sided would need $|z|<\tfrac12$ and $|z|>1$ at the same time. That region is empty, which is the key's "fourth combination".
3. **Stability comes from the ROC: [[0-midterm-1/past-exams/fall-2025|FA2025 #7]] and [[0-midterm-1/past-exams/spring-2025|SP2025 #8]].** Pick *FA2025 #7*. The causal choice $|z|>2$ is unstable, but the annulus $\tfrac23<|z|<2$ contains the unit circle, so that system is BIBO stable. Its impulse response $h[n] = -\tfrac54\left(-\tfrac23\right)^n u[n] - \tfrac94(-2)^n u[-n-1]$ decays in both directions in the stem plot. In the exam, the sentence "the system is BIBO stable" is what picks the ROC. Part (b) then runs the anti-causal piece as a backward recursion ([[problems/two-sided-systems-as-recursions]]). *SP2025 #8* is the same story with $\tfrac12<|z|<\tfrac32$. Then pick *HW4 #1(a)*: its pole at $-1$ lies **on** the unit circle, so no ROC can contain $|z|=1$ and none of the three systems is stable. The "This ROC" card highlights the matching row of the Lecture 11 table each time.
4. **Complex poles become a cosine: Lecture 8, Exercise 2 and [[0-midterm-1/past-exams/spring-2021|SP2021 #5]].** Pick *Lecture 8, Exercise 2*. The poles are $e^{\pm j\pi/3}$ with $A_1=A_2=\tfrac32$, and the demo folds the pair into $3\cos\left(\tfrac{\pi}{3}n\right)u[n]$. *SP2021 #5* ($3z^{-1}/(1+z^{-2})$) has $A = \mp\tfrac32 j$ at $p=\pm j$. The phase $-\tfrac{\pi}{2}$ turns the cosine into $3\sin\left(\tfrac{\pi}{2}n\right)u[n]$. Both systems have their poles on $|z|=1$, so the stem plot neither decays nor grows. They are marginally stable ([[concepts/marginal-stability]]): only an input that oscillates at a pole's angle makes the output grow.
5. **Improper $H(z)$: divide first ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]).** Pick *Lecture 10*. The numerator degree (3) is at least the denominator degree (2), so the demo long-divides first, giving $C_0=\tfrac59$ and $C_1=-\tfrac43$. Cover-up on the remainder then gives $A_1=\tfrac{7}{36}$ at 3 and $A_2=\tfrac14$ at $-1$. Now select the innermost ROC. It reads $0<|z|<1$, not $|z|<1$, because $C_1z^{-1}$ puts a pole at $z=0$. That $h[n]$ is left-sided but has samples at $n=0$ and $n=1$, so it is non-causal: row 4 of the Lecture 11 table, not the anti-causal row 2.
6. **Pole-zero cancellation removes an ROC: SP2025 #8, [[0-midterm-1/past-exams/fall-2019|FA2019 #10(d)]] and FA2025 #6.** Pick *SP2025 #8 — output Y(z)*. The input's zero at $-\tfrac32$ cancels the pole of $H$ there (⊗ on the plot), so only two outputs are possible instead of three. *FA2019 #10(d)* shows why the key answers False: cascading the stable $H$ with the unstable $2^n u[n]$ gives a stable system, because $H$'s zero at 2 cancels that pole. *FA2025 #6* cancels $-\tfrac23$ and leaves an improper remainder: $y[n] = \tfrac34\delta[n] + \tfrac32\delta[n-1] + \tfrac94(2)^n u[n]$, which is the key's $3(2)^n u[n] - 3(2)^{n-2}u[n-2]$ written another way. Finally, change the SP2025 numerator to `(2, -3)(1, 1.5001)`. The demo warns about a near-cancellation and keeps all three ROCs: a cancellation is either exact or it doesn't happen. See [[concepts/pole-zero-cancellation]] and [[problems/unbounded-outputs-and-pole-matching]].
7. **Pick the parameter that makes it stable: [[0-midterm-1/past-exams/spring-2025|SP2025 #7]].** The causal system $y[n] = -\tfrac32y[n-1] + y[n-2] + x[n] - \alpha^2x[n-2]$ becomes a = `1, 3/2, -1` once every $y$ term is moved to the left side (note the sign flips). Its poles are $-2$ and $\tfrac12$. With b = `1, 0, -4` ($\alpha=\pm2$), the zero at $-2$ cancels the unstable pole and the causal ROC $|z|>\tfrac12$ is stable. With b = `1, 0, 4` ($\alpha=\pm2j$) nothing cancels and the causal system is unstable. See [[problems/parameters-for-stability]].
8. **A repeated pole.** Pick *Repeated pole*. The demo refuses to print simple-pole $A_k$, because a double pole needs an $n\,p^n u[n]$ term (Lecture 7's differentiation property). It still lists the ROCs, decides causality and stability, and plots $h[n] = (n+1)\left(\tfrac12\right)^n u[n]$ numerically.

## What the demo is (and isn't)

It handles $H(z) = B(z^{-1})/A(z^{-1})$ with **no positive powers of $z$**, in the same form as `lfilter`. If $a[0]\ne1$, it divides through first. A time advance such as HW4 #1(b), which is $z\cdot\frac{1-z^{-1}}{1+2z^{-1}}$ after its own cancellation, can't be typed. Analyze the $z^{-1}$ part and shift $h[n]$ one sample to the left. For the same reason, the third row of the Lecture 11 table ($|p_{\max}|<|z|<\infty$: right-sided but non-causal) never lights up.

The arithmetic is floating point, not exact:

- **Roots** come from Aberth–Ehrlich iteration with a Newton polish. A number is shown as a fraction when one with denominator ≤ 64 matches it to $10^{-9}$, so "7/36" is how 0.19444… is displayed, not exact arithmetic.
- **Cancellation** happens when a pole and a zero agree to $10^{-7}$ (relative). Within $10^{-3}$ you get a warning instead, and the pole stays. Roots within $10^{-4}$ of each other are treated as repeated, and poles within $10^{-2}$ trigger a warning that the $A_k$ are ill-conditioned.

Some other limits:

- **Closed form.** $h[n]$ is written out only for distinct poles, using the Lecture 8 PFE plus the Lecture 10 polynomial part. With a repeated pole, the ROCs, causality and stability are still right, but $h[n]$ is computed numerically: the contour-integral inverse z-transform that Lecture 8 lets us skip by hand, evaluated with the trapezoid rule on a circle inside the ROC.
- **Stem plot.** It covers $-15\le n\le15$ and shows $\mathrm{Re}\,h[n]$ when $h$ is complex (FA2025 #8(b), whose poles $\tfrac34$, $j$, $e^{j2/3}$ have no conjugate partners). A growing sequence dwarfs its early samples. Tick "scale to $-5\le n\le5$" to see them, or read the values table.
- **ROCs** are built from the poles **after** cancellation. That is why the ROC of a cascade or of an output $Y(z)=H(z)X(z)$ can be larger than the intersection of the individual ROCs (Lecture 11: "at least the intersection").
- **Stable** means BIBO stable for the system with that ROC: the unit circle lies strictly inside the ROC. A pole on $|z|=1$ always means unstable. A causal system whose poles on the circle are all simple is labelled marginally stable.
- **Frequency response.** It is not a frequency-response (DTFT) tool, because the DTFT is not on Midterm 1.

Every preset's $A_k$ and $C_k$ were checked against `scipy.signal.residuez`. Every causal $h[n]$ was checked against `scipy.signal.lfilter`. Every ROC's $h[n]$ was checked against an independent numerical inverse z-transform and against the identity $\sum_k a_k h[n-k] = b[n]$. The [[demos/python-demos|Python demos]] do the same computations in a few lines each.

## Related

[[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros]] · [[concepts/partial-fraction-expansion]] · [[concepts/inverse-z-transform]] · [[concepts/sided-sequences]] · [[concepts/causality]] · [[concepts/bibo-stability]] · [[concepts/marginal-stability]] · [[concepts/pole-zero-cancellation]] · [[concepts/transfer-function]] · [[problems/all-possible-rocs]] · [[problems/lccde-to-transfer-function-and-response]] · [[demos/index|all demos]]

### Sources for this page

Lecture 8 notes (PFE procedure, Exercises 1 and 2); Lecture 10 notes (improper expressions, Exercise 1); Lecture 11 notes (Table 1 on ROC shape vs. causality and stability, §1.2.1 on marginal stability); HW3 #4 and HW4 #1 with official solutions; past Midterm 1 keys: FA2025 #6, #7, #8; SP2025 #7, #8; FA2023 #6; SP2021 #5; FA2019 #7, #10. Numbers were verified with numpy/scipy.
