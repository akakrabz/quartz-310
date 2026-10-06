---
title: "LCCDE ⇄ transfer function ⇄ response"
description: "Recipe for the long z-domain problem on every midterm: difference equation to H(z) and back, poles, zeros, ROC, FIR or IIR, then the output y[n] = Z⁻¹{H(z)X(z)} with pole–zero cancellations. Three fresh practice problems and an lfilter check."
tags: [problem-family, problem, midterm-1, lccde, z-transform, roc, stability]
family_frequency: "7 of 7 exams"
typical_points: "15–20"
lectures: [5, 9, 10, 11]
---

*Problem family · on 7 of 7 past midterms · typically 15–20 pts · uses [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · concepts: [[concepts/lccde]], [[concepts/transfer-function]], [[concepts/poles-and-zeros]], [[concepts/fir-and-iir]], [[concepts/pole-zero-cancellation]]*

> [!abstract] In one breath
> Put every $y$ term on the left and every $x$ term on the right; then $H(z)$ is "$x$-side coefficients over $y$-side coefficients" in powers of $z^{-1}$. Factor for poles and zeros, let the words (causal, stable) fix the ROC, and get outputs from $Y(z)=H(z)X(z)$: **cancel before you expand**, because the exam input is almost always chosen to kill one pole.

## What it looks like on the exam

A causal system is given as a difference equation (or as $H(z)$, or through one input–output pair), and the parts walk down a fixed ladder: (a) $H(z)$, poles, zeros, ROC; (b) the response to a specific input; (c) stable? FIR or IIR? (d) the other direction, $H(z)\to$ LCCDE. It is one of the two or three biggest problems on every recent exam (15–20 points).

| where | given → asked | key result |
|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #6]] (16 pts) | $y[n]=\tfrac43y[n-1]+\tfrac43y[n-2]+x[n]-x[n-2]$ → $H$, poles, zeros, ROC; $y$ for $x=3\delta[n]+2\delta[n-1]$ | $H=\dfrac{1-z^{-2}}{(1-2z^{-1})(1+\frac23z^{-1})}$, $\lvert z\rvert>2$; $x$ cancels $-\tfrac23$: $y=3(2)^nu[n]-3(2)^{n-2}u[n-2]$ |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #8a,b]] (20 pts) | $H\to$ LCCDE; all outputs for $x=\delta[n]+\tfrac32\delta[n-1]$ | $y[n]+y[n-1]-\tfrac34y[n-2]=2x[n]-3x[n-1]$; $x$ cancels $-\tfrac32$ → two outputs |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #6]] (15 pts) | causal; input $\{1,\tfrac13\}$ gives output $\{1,\tfrac12\}$ → $H$, $h$, LCCDE | $H=\dfrac{1+\frac12z^{-1}}{1+\frac13z^{-1}}$, $y[n]=-\tfrac13y[n-1]+x[n]+\tfrac12x[n-1]$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #6b]] | $H\to$ LCCDE | $y[n]-\tfrac52y[n-1]+y[n-2]=x[n]-x[n-1]$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #7]] (20 pts) | $H=\dfrac{1-3z^{-1}+2z^{-2}}{1+\frac34z^{-1}-\frac14z^{-2}}$ causal → poles, zeros, ROC; $y$ for $u[n]$; stable? | poles $\tfrac14,-1$; zeros $1,2$; $\lvert z\rvert>1$; $y=-\tfrac75(\tfrac14)^nu[n]+\tfrac{12}{5}(-1)^nu[n]$; unstable |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #5]] (20 pts) | $y[n]=y[n-1]+\tfrac34y[n-2]+x[n]-4x[n-2]$ → $H$; $y$ for $x=2\delta[n]-3\delta[n-1]$; stable? | poles $\tfrac32,-\tfrac12$, zeros $\pm2$; $x$ cancels $\tfrac32$: $y=2(-\tfrac12)^nu[n]-8(-\tfrac12)^{n-2}u[n-2]$; unstable |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #6c]] | $H\to$ LCCDE | $y[n]=\tfrac34y[n-1]-\tfrac18y[n-2]+x[n]-2x[n-1]$ (the key's typo repeats $y[n-1]$) |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #6]] | $y[n]=2y[n-3]-x[n]+x[n-3]$ → $h[0..4]$ | $-1,0,0,-1,0$ (the key's $1,0,0,3,0$ is a sign error) |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #10]] (12 pts) | causal $H=\dfrac{1-2z^{-1}}{(1-\frac12z^{-1})(1-\frac14z^{-1})}$ → ROC, stable?, LCCDE | $\lvert z\rvert>\tfrac12$, stable, $y[n]=\tfrac34y[n-1]-\tfrac18y[n-2]+x[n]-2x[n-1]$ |
| [[homework/hw4\|HW4 #6]] | $y[n]=x[n]+0.5x[n-1]-y[n-1]-0.25y[n-2]$ → $H$, $h$, $y$ for $(-1)^nu[n]$ | a factor cancels: $H=\dfrac{1}{1+0.5z^{-1}}$, $h=(-\tfrac12)^nu[n]$, $y=[2(-1)^n-(-\tfrac12)^n]u[n]$ |
| [[2-z-transform/09-transfer-functions\|Lecture 9]] | notes Exercise 1: $y[n]=\tfrac12y[n-1]+x[n]$; slides Exercises 1–3 (same drill, other numbers) | $H=\dfrac{1}{1-\frac12z^{-1}}$, $h=(\tfrac12)^nu[n]$ |
| [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|Lecture 10]] | notes Exercise 1: $y[n]=2y[n-1]+3y[n-2]+x[n]-3x[n-1]+x[n-2]+4x[n-3]$ (improper) | $h=\tfrac59\delta[n]-\tfrac43\delta[n-1]+\tfrac{7}{36}3^nu[n]+\tfrac14(-1)^nu[n]$ |

## The recipe

> [!recipe] LCCDE ⇄ $H(z)$ ⇄ $y[n]$
> **LCCDE → $H(z)$**
> 1. **Standard form (Lecture 9):** every $y$ term on the left, every $x$ term on the right,
> $$
> y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k] .
> $$
> A term $+c\,y[n-1]$ on the *right* of the given equation becomes $a_1 = -c$.
> 2. **Transform term by term** ($y[n-k]\to z^{-k}Y(z)$, zero initial conditions) and divide:
> $$
> H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_k b_k z^{-k}}{1+\sum_k a_k z^{-k}} .
> $$
> 3. **Factor** numerator and denominator: zeros $q_k$, poles $p_k$. Rewriting in positive powers of $z$ shows any extra poles or zeros at $z=0$. **Cancel** common factors and say so.
> 4. **ROC from the words:** causal → $\lvert z\rvert>\max\lvert p_k\rvert$; stable $\iff$ the ROC contains $\lvert z\rvert=1$; causal *and* stable $\iff$ every remaining pole is inside the unit circle.
> 5. **FIR or IIR:** after cancelling, any pole away from $z=0$ → IIR; none → FIR. A feedback term alone does not make a system IIR (Practice 3).
>
> **$H(z)$ → LCCDE:** multiply out the factored denominator, cross-multiply $Y(z)\big(1+\sum a_kz^{-k}\big) = X(z)\sum b_kz^{-k}$, replace $z^{-k}Y(z)\to y[n-k]$, $z^{-k}X(z)\to x[n-k]$, and solve for $y[n]$ if they ask for a recursion.
>
> **Response to an input**
> 6. $Y(z) = H(z)X(z)$, ROC at least ROC$_H\cap$ROC$_X$. **Cancel first:** an input zero on a pole of $H$, or a zero of $H$ on a pole of $X$.
> 7. If $Y$ is improper, divide, or keep the numerator as delays: $Y = (c_0+c_1z^{-1}+\dots)\,G(z)$ gives $y[n] = c_0\,g[n]+c_1\,g[n-1]+\dots$ For a finite input, $y[n] = \sum_k x[k]\,h[n-k]$ is often fastest.
> 8. PFE the rest and invert with the ROC (causal system and right-sided input → right-sided output).
>
> **Checks.** Re-read the coefficient signs (step 1). Run the recursion by hand for $y[0], y[1]$ and compare with your formula; for a causal output $y[0] = Y(\infty)$; for a stable system driven by $u[n]$ the output settles to $H(1)$.

> [!trap] Where the points go
> - **Signs when you move terms.** $y[n]=\tfrac34y[n-1]-\tfrac18y[n-2]+\dots$ has denominator $1-\tfrac34z^{-1}+\tfrac18z^{-2}$. Two official keys slip here: SP2021 #6 (sign of $x[n]$ lost) and SP2023 #6c (the $z^{-2}$ term written as $y[n-1]$); see [[0-toolkit/05-errata|errata]].
> - **Lecture 5 vs Lecture 9 notation.** Lecture 5 writes $y[n]=\sum_i b_i\,y[n-i]+\sum_j c_j\,x[n-j]$: there $b_i$ are the **feedback** coefficients, on the right-hand side, with no sign flip. Lecture 9 (and `scipy.signal.lfilter(b, a, x)`) uses $a_k$ on the left, so $a_k=-b_i$, and $b_k$ are the **input** coefficients. Same letter, different job.
> - **Missing the cancellation.** FA2025 #6b: $X(z)=3+2z^{-1}=3(1+\tfrac23z^{-1})$ kills the pole at $-\tfrac23$, so only the $2^n$ mode survives. SP2023 #5b: $2-3z^{-1}$ kills the *unstable* pole $\tfrac32$, leaving a bounded output from an unstable system. Expanding before cancelling costs time and usually a sign.
> - **Improper $Y(z)$.** Cover-up alone is incomplete. $\dfrac{1-z^{-2}}{1-2z^{-1}}$ is improper in $z^{-1}$: cover-up gives the right $A=\tfrac34$, but misses the polynomial part $\tfrac14+\tfrac12z^{-1}$, i.e. $\tfrac14\delta[n]+\tfrac12\delta[n-1]$. Use delays ($g[n]-g[n-2]$) or long division.
> - **ROC of the output after cancellation.** ROC$_Y$ is *at least* the intersection and grows when a boundary pole cancels: SP2021 #7 gives ROC$_Y$ $\lvert z\rvert>1$, not $1<\lvert z\rvert<4$.
> - **Causal is not stable.** An LCCDE run forward from rest is causal; it is stable only if every remaining pole is inside $\lvert z\rvert=1$ (SP2023 #5c, FA2023 #7c: "No").
> - **Zeros at the origin.** In positive powers, $\dfrac{1+2z^{-1}}{1+\frac16z^{-1}-\frac16z^{-2}} = \dfrac{z(z+2)}{(z+\frac12)(z-\frac13)}$ has a zero at $z=0$ too. $\dfrac{1-z^{-2}}{(1-2z^{-1})(1+\frac23z^{-1})}$ does not: the $z^2$ cancels.

## Practice problems

> [!question] Practice 1 — the full ladder
> A causal LTI system satisfies
> $$
> y[n] = -\tfrac16\,y[n-1] + \tfrac16\,y[n-2] + x[n] + 2x[n-1] .
> $$
> (a) Find $H(z)$, its poles, zeros and ROC. Is the system BIBO stable? FIR or IIR? (b) Find $h[n]$. (c) Find the step response ($x[n]=u[n]$).

> [!success]- Solution
> **(a)** Standard form $y[n]+\tfrac16y[n-1]-\tfrac16y[n-2] = x[n]+2x[n-1]$, so
> $$
> H(z) = \frac{1+2z^{-1}}{1+\frac16z^{-1}-\frac16z^{-2}} = \frac{1+2z^{-1}}{(1+\frac12z^{-1})(1-\frac13z^{-1})} = \frac{z(z+2)}{(z+\frac12)(z-\frac13)} .
> $$
> Poles $-\tfrac12,\ \tfrac13$; zeros $-2,\ 0$. Causal → ROC $\lvert z\rvert>\tfrac12$, which contains the unit circle: **stable**. Uncancelled poles away from the origin: **IIR**.
>
> **(b)** Cover-up at $z^{-1}=-2$ and $z^{-1}=3$: $A=\dfrac{1-4}{1+\frac23}=-\tfrac95$, $\ B=\dfrac{1+6}{1+\frac32}=\tfrac{14}{5}$ (check $A+B=1=h[0]$ ✓):
> $$
> h[n] = -\tfrac95\left(-\tfrac12\right)^n u[n] + \tfrac{14}{5}\left(\tfrac13\right)^n u[n] .
> $$
>
> **(c)** $X(z) = \dfrac{1}{1-z^{-1}}$, $\lvert z\rvert>1$, so $Y(z) = \dfrac{1+2z^{-1}}{(1+\frac12z^{-1})(1-\frac13z^{-1})(1-z^{-1})}$, ROC $\lvert z\rvert>1$. Cover-up:
> $$
> \begin{aligned}
> A &= \frac{1-4}{(1+\frac23)(1+2)} = -\tfrac35,\\
> B &= \frac{1+6}{(1+\frac32)(1-3)} = -\tfrac75,\\
> C &= \frac{1+2}{(1+\frac12)(1-\frac13)} = 3,
> \end{aligned}
> $$
> $$
> y[n] = \left[-\tfrac35\left(-\tfrac12\right)^n - \tfrac75\left(\tfrac13\right)^n + 3\right]u[n] .
> $$
> Checks: $y[0] = -\tfrac35-\tfrac75+3 = 1$, and the recursion gives $y[0]=1$, $y[1] = -\tfrac16+1+2 = \tfrac{17}{6}$ ✓ (formula: $\tfrac{3}{10}-\tfrac{7}{15}+3=\tfrac{17}{6}$ ✓). The output settles to $C = H(1) = \dfrac{3}{1} = 3$ ✓.

Checking (c) with `lfilter`, which runs the Lecture 9 form with `a[0] = 1` from initial rest:

```python
import numpy as np
from scipy.signal import lfilter

# Practice 1: y[n] + (1/6)y[n-1] - (1/6)y[n-2] = x[n] + 2x[n-1]   (Lecture 9 form, a[0] = 1)
b, a = [1, 2], [1, 1/6, -1/6]
n = np.arange(8)
y = lfilter(b, a, np.ones(8))                       # x[n] = u[n], initial rest
closed = -(3/5)*(-1/2)**n - (7/5)*(1/3)**n + 3      # the PFE answer
print(np.round(y, 4))
print(np.allclose(y, closed))
```

```text
[1.     2.8333 2.6944 3.0231 2.9452 3.013  2.9887 3.004 ]
True
```

> [!question] Practice 2 — the other direction, and an input that kills a pole
> A causal LTI system has
> $$
> H(z) = \frac{1+z^{-1}}{(1-\frac12z^{-1})(1+3z^{-1})} .
> $$
> (a) Write the LCCDE as a recursion for $y[n]$. (b) Poles, zeros, ROC; is it stable? (c) Find the output for $x[n] = 2\delta[n]+6\delta[n-1]$. (d) Find $h[n]$ and compare with (c).

> [!success]- Solution
> **(a)** $(1-\tfrac12z^{-1})(1+3z^{-1}) = 1+\tfrac52z^{-1}-\tfrac32z^{-2}$, so $Y(z)\big(1+\tfrac52z^{-1}-\tfrac32z^{-2}\big) = X(z)(1+z^{-1})$:
> $$
> y[n] = -\tfrac52\,y[n-1] + \tfrac32\,y[n-2] + x[n] + x[n-1] .
> $$
> **(b)** Poles $\tfrac12$ and $-3$; zeros $-1$ and $0$ ($H = \frac{z(z+1)}{(z-\frac12)(z+3)}$). Causal → ROC $\lvert z\rvert>3$, which excludes the unit circle: **not stable**.
>
> **(c)** $X(z) = 2+6z^{-1} = 2(1+3z^{-1})$: its zero sits on the pole $-3$.
> $$
> Y(z) = \frac{2(1+z^{-1})}{1-\frac12z^{-1}} = -4 + \frac{6}{1-\frac12 z^{-1}},\qquad \lvert z\rvert>\tfrac12,
> $$
> $$
> y[n] = -4\delta[n] + 6\left(\tfrac12\right)^n u[n] = \{\underset{\uparrow}{2},\ 3,\ \tfrac32,\ \tfrac34,\dots\}\quad(\text{starts at } n=0).
> $$
> Bounded, although the system is unstable.
>
> **(d)** Cover-up: $A = \dfrac{1+2}{1+6} = \tfrac37$ at $\tfrac12$, $\ B = \dfrac{1-\frac13}{1+\frac16} = \tfrac47$ at $-3$:
> $$
> h[n] = \tfrac37\left(\tfrac12\right)^n u[n] + \tfrac47(-3)^n u[n] ,
> $$
> which is unbounded. So the bounded input $\delta[n]$ gives an unbounded output while the bounded input $2\delta[n]+6\delta[n-1]$ does not: $y = 2h[n]+6h[n-1]$ and the $(-3)^n$ terms cancel exactly. This is the [[problems/unbounded-outputs-and-pole-matching|pole-matching]] family in miniature.

> [!question] Practice 3 — feedback, but FIR
> $y[n] = y[n-1] + x[n] - x[n-3]$, at rest. Find $H(z)$ and $h[n]$. FIR or IIR? Stable? What is the output for $x[n]=u[n]$?

> [!success]- Solution
> $$
> H(z) = \frac{1-z^{-3}}{1-z^{-1}} = \frac{(1-z^{-1})(1+z^{-1}+z^{-2})}{1-z^{-1}} = 1+z^{-1}+z^{-2} .
> $$
> The pole at $z=1$ is cancelled by one of the three zeros of $1-z^{-3}$ (the cube roots of unity $1,\ e^{\pm j2\pi/3}$). So $h[n] = \delta[n]+\delta[n-1]+\delta[n-2]$: **FIR** despite the feedback term, and **stable** ($\sum\lvert h\rvert = 3$). This is a 3-point running sum written recursively, the trick from [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]]. For $x=u[n]$: $y[n] = u[n]+u[n-1]+u[n-2] = \{\underset{\uparrow}{1},\ 2,\ 3,\ 3,\ 3,\dots\}$, bounded. A test that only asks "is there a $y[n-k]$ term?" gets this wrong.

## Where to go next

- Concepts: [[concepts/lccde|LCCDE]], [[concepts/transfer-function|transfer function]], [[concepts/poles-and-zeros|poles and zeros]], [[concepts/fir-and-iir|FIR and IIR]], [[concepts/pole-zero-cancellation|pole–zero cancellation]], [[concepts/partial-fraction-expansion|PFE]], [[concepts/system-algebra|system algebra]].
- Lectures: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] (LCCDEs, block diagrams), [[2-z-transform/09-transfer-functions|Lecture 9]] (LCCDE → $H$), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (improper $H$), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] (stability from the ROC).
- Related families: [[problems/all-possible-rocs|all possible ROCs]] (the PFE step), [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]], [[problems/parameters-for-stability|parameters for stability]], [[problems/finding-h-from-input-output-pairs|finding h from input–output pairs]] (FA2024 #6).
- Try it: [[demos/difference-equation-simulator|difference-equation simulator]] (type the coefficients, watch $h[n]$ and the step response), [[demos/pole-zero-and-roc-explorer|pole–zero and ROC explorer]], [[demos/practice-drills|practice drills]].

### Sources for this page

Lecture 5 notes (LCCDE form, running sum), Lecture 9 notes and slides (LCCDE → $H(z)$, FIR vs IIR, Exercises 1–3), Lecture 10 notes (improper $H$, Exercise 1), Lecture 11 notes (stability from the ROC); HW4 #6 with solution; past midterms FA2025 #6, SP2025 #8, FA2024 #6, FA2023 #6b and #7, SP2023 #5 and #6c, SP2021 #6, FA2019 #10. Practice problems are new; every number is checked in `verify/problems/lccde_practice.py`.
