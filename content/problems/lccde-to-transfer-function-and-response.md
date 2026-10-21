---
title: "LCCDE ⇄ transfer function ⇄ response"
description: "The long z-domain problem on every midterm: difference equation to H(z) and back, poles, zeros, ROC, FIR or IIR, then y[n] = Z⁻¹{H(z)X(z)} with pole–zero cancellations."
tags: [problem-family, problem, midterm-1, lccde, z-transform, roc, stability]
family_frequency: "7 of 7 exams"
typical_points: "15–20"
lectures: [5, 9, 10, 11]
---

*Problem family · 7 of 7 past midterms · 15–20 points · [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

## What it looks like on the exam

A causal system as an LCCDE, an $H(z)$ or an input–output pair; the parts walk a fixed ladder: (a) $H(z)$, poles, zeros, ROC; (b) the response to an input, usually chosen to cancel a pole; (c) stable? FIR or IIR? (d) $H(z)\to$ LCCDE.

| where | given → asked | key result |
|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #6]] (16 pts) | $y[n]=\tfrac43y[n-1]+\tfrac43y[n-2]+x[n]-x[n-2]$ → $H$, poles, zeros, ROC; $y$ for $x=3\delta[n]+2\delta[n-1]$ | $H=\dfrac{1-z^{-2}}{(1-2z^{-1})(1+\frac23z^{-1})}$, $\lvert z\rvert>2$; $x$ cancels $-\tfrac23$: $y=3(2)^nu[n]-3(2)^{n-2}u[n-2]$ |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #8a,b]] (20 pts) | $H\to$ LCCDE; all outputs for $x=\delta[n]+\tfrac32\delta[n-1]$ | $y[n]+y[n-1]-\tfrac34y[n-2]=2x[n]-3x[n-1]$; $x$ cancels $-\tfrac32$ → two outputs |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #6]] (15 pts) | causal; $\{1,\tfrac13\}\mapsto\{1,\tfrac12\}$ → $H$, $h$, LCCDE | $H=\dfrac{1+\frac12z^{-1}}{1+\frac13z^{-1}}$, $y[n]=-\tfrac13y[n-1]+x[n]+\tfrac12x[n-1]$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #6b]] | $H\to$ LCCDE | $y[n]-\tfrac52y[n-1]+y[n-2]=x[n]-x[n-1]$ |
| FA2023 #7 (20 pts) | $H=\dfrac{1-3z^{-1}+2z^{-2}}{1+\frac34z^{-1}-\frac14z^{-2}}$ causal → poles, zeros, ROC; $y$ for $u[n]$; stable? | poles $\tfrac14,-1$; zeros $1,2$; $\lvert z\rvert>1$; $y=-\tfrac75(\tfrac14)^nu[n]+\tfrac{12}{5}(-1)^nu[n]$; unstable |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #5]] (20 pts) | $y[n]=y[n-1]+\tfrac34y[n-2]+x[n]-4x[n-2]$ → $H$; $y$ for $x=2\delta[n]-3\delta[n-1]$; stable? | poles $\tfrac32,-\tfrac12$, zeros $\pm2$; $x$ cancels $\tfrac32$: $y=2(-\tfrac12)^nu[n]-8(-\tfrac12)^{n-2}u[n-2]$; unstable |
| SP2023 #6c | $H\to$ LCCDE | $y[n]=\tfrac34y[n-1]-\tfrac18y[n-2]+x[n]-2x[n-1]$ (key's typo repeats $y[n-1]$) |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #6]] | $y[n]=2y[n-3]-x[n]+x[n-3]$ → $h[0..4]$ | $-1,0,0,-1,0$ (key's $1,0,0,3,0$ is a sign error) |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #10]] (12 pts) | causal $H=\dfrac{1-2z^{-1}}{(1-\frac12z^{-1})(1-\frac14z^{-1})}$ → ROC, stable?, LCCDE | $\lvert z\rvert>\tfrac12$, stable, $y[n]=\tfrac34y[n-1]-\tfrac18y[n-2]+x[n]-2x[n-1]$ |
| [[homework/hw4\|HW4 #6]] | $y[n]=x[n]+0.5x[n-1]-y[n-1]-0.25y[n-2]$ → $H$, $h$, $y$ for $(-1)^nu[n]$ | $H=\dfrac{1}{1+0.5z^{-1}}$, $h=(-\tfrac12)^nu[n]$, $y=[2(-1)^n-(-\tfrac12)^n]u[n]$ |
| Lecture 9 | Exercise 1: $y[n]=\tfrac12y[n-1]+x[n]$ | $H=\dfrac{1}{1-\frac12z^{-1}}$, $h=(\tfrac12)^nu[n]$ |
| Lecture 10 | Exercise 1: $y[n]=2y[n-1]+3y[n-2]+x[n]-3x[n-1]+x[n-2]+4x[n-3]$ | $h=\tfrac59\delta[n]-\tfrac43\delta[n-1]+\tfrac{7}{36}3^nu[n]+\tfrac14(-1)^nu[n]$ |

## The recipe

> [!recipe] LCCDE ⇄ $H(z)$ ⇄ $y[n]$
> 1. **Standard form, then divide:** $y$ terms left, $x$ terms right ($+c\,y[n-1]$ on the right becomes $a_1=-c$):
> $$
> y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k],\qquad H(z) = \frac{\sum_k b_k z^{-k}}{1+\sum_k a_k z^{-k}} .
> $$
> 2. **Factor and cancel:** zeros, poles; positive powers of $z$ show those at $z=0$.
> 3. **ROC from the words:** causal → $\lvert z\rvert>\max\lvert p_k\rvert$; stable iff ROC contains $\lvert z\rvert=1$. Remaining pole away from 0 → IIR, else FIR.
> 4. **$H\to$ LCCDE:** cross-multiply $Y(z)\big(1+\sum a_kz^{-k}\big) = X(z)\sum b_kz^{-k}$, replace $z^{-k}Y\to y[n-k]$.
> 5. **Response:** $Y=HX$; **cancel first**; improper: divide, or keep the numerator as delays ($y=c_0g[n]+c_1g[n-1]+\dots$); PFE, invert with the ROC.
> 6. **Check:** recursion by hand for $y[0]$, $y[1]$; $y[0]=Y(\infty)$; stable system driven by $u[n]$ settles to $H(1)$.

> [!trap] Where the points go
> - **Signs when moving terms.** Two keys slip: SP2021 #6, SP2023 #6c ([[0-toolkit/05-errata|errata]]).
> - **Lecture 5 vs 9.** Lecture 5's $b_i$ are feedback coefficients on the right; Lecture 9's $a_k=-b_i$ sit on the left.
> - **Missed cancellation.** FA2025 #6b: $3+2z^{-1}$ kills $-\tfrac23$; SP2023 #5b: $2-3z^{-1}$ kills the unstable $\tfrac32$.
> - **Improper $Y$:** cover-up misses the polynomial part ($\dfrac{1-z^{-2}}{1-2z^{-1}}$: $A=\tfrac34$ plus $\tfrac14\delta[n]+\tfrac12\delta[n-1]$).
> - **ROC and stability.** Causal ≠ stable (SP2023 #5c, FA2023 #7c); ROC$_Y$ grows when a boundary pole cancels (SP2021 #7: $\lvert z\rvert>1$).

## Practice problems

> [!question] Practice 1 — the full ladder
> Causal: $y[n] = -\tfrac16\,y[n-1] + \tfrac16\,y[n-2] + x[n] + 2x[n-1]$. (a) $H(z)$, poles, zeros, ROC; stable? FIR/IIR? (b) $h[n]$. (c) Step response.

> [!success]- Solution
> **(a)**
> $$
> H(z) = \frac{1+2z^{-1}}{(1+\frac12z^{-1})(1-\frac13z^{-1})} = \frac{z(z+2)}{(z+\frac12)(z-\frac13)} .
> $$
> Poles $-\tfrac12,\ \tfrac13$; zeros $-2,\ 0$; $\lvert z\rvert>\tfrac12$: stable, IIR.
> **(b)** $A=-\tfrac95$, $B=\tfrac{14}{5}$:
> $$
> h[n] = -\tfrac95\left(-\tfrac12\right)^n u[n] + \tfrac{14}{5}\left(\tfrac13\right)^n u[n] .
> $$
> **(c)** Cover-up on $Y=H\cdot\frac{1}{1-z^{-1}}$: $-\tfrac35$, $-\tfrac75$, $3$:
> $$
> y[n] = \left[-\tfrac35\left(-\tfrac12\right)^n - \tfrac75\left(\tfrac13\right)^n + 3\right]u[n] .
> $$
> Check: $y[0]=1$, $y[1]=\tfrac{17}{6}$, limit $H(1)=3$ ✓.

> [!question] Practice 2 — the other direction, and an input that kills a pole
> Causal $H(z) = \dfrac{1+z^{-1}}{(1-\frac12z^{-1})(1+3z^{-1})}$. (a) LCCDE. (b) Poles, zeros, ROC; stable? (c) Output for $x=2\delta[n]+6\delta[n-1]$. (d) $h[n]$; compare.

> [!success]- Solution
> **(a)** $y[n] = -\tfrac52\,y[n-1] + \tfrac32\,y[n-2] + x[n] + x[n-1]$.
> **(b)** Poles $\tfrac12$, $-3$; zeros $-1$, $0$; $\lvert z\rvert>3$: not stable.
> **(c)** $X=2(1+3z^{-1})$ cancels $-3$:
> $$
> Y(z) = \frac{2(1+z^{-1})}{1-\frac12z^{-1}} = -4 + \frac{6}{1-\frac12 z^{-1}},\qquad y[n] = -4\delta[n] + 6\left(\tfrac12\right)^n u[n].
> $$
> **(d)** $h[n] = \tfrac37\left(\tfrac12\right)^n u[n] + \tfrac47(-3)^n u[n]$, unbounded; in (c) the $(-3)^n$ terms cancel.

> [!question] Practice 3 — feedback, but FIR
> $y[n] = y[n-1] + x[n] - x[n-3]$, at rest. $H(z)$, $h[n]$; FIR or IIR? Stable? Output for $u[n]$?

> [!success]- Solution
> $$
> H(z) = \frac{1-z^{-3}}{1-z^{-1}} = 1+z^{-1}+z^{-2} .
> $$
> FIR and stable despite the feedback term. $y=u[n]+u[n-1]+u[n-2]=\{\underset{\uparrow}{1},\ 2,\ 3,\ 3,\dots\}$.

## Related

[[concepts/lccde|LCCDE]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/pole-zero-cancellation|pole–zero cancellation]] · [[problems/all-possible-rocs|all possible ROCs]] · [[problems/unbounded-outputs-and-pole-matching|pole matching]] · [[demos/difference-equation-simulator|difference-equation simulator]]

### Sources for this page

Lectures 5, 9, 10, 11 notes and slides; HW4 #6 with solution; past Midterm 1 exams FA2019–FA2025 with keys. Practice problems are new.
