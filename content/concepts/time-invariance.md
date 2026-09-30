---
title: "Time-invariance"
description: "Shift the input by n0 and the output shifts by n0: the formal two-sided test, the rules that decide most table rows at a glance, and why x[2n], x[|n|] and n·x[n] are time-varying."
tags: [concept, systems, midterm-1]
aliases: ["shift-invariance", "time-invariant", "shift-invariant", "time-varying", "shift-varying", "TI", "SI"]
---

> [!key] Definition (Lecture 3)
> $T$ is **time-invariant** (older exams: **shift-invariant**) iff for every input and every integer $n_0$
> $$
> x[n]\ \xrightarrow{T}\ y[n]\quad\Longrightarrow\quad x[n-n_0]\ \xrightarrow{T}\ y[n-n_0].
> $$
> Delaying the input only delays the output; the system's rule does not depend on the clock.

> [!recipe] The two-sided test
> 1. **Shift the output:** write $y[n]$ and replace *every* $n$ by $n-n_0$, inside and outside $x[\cdot]$.
> 2. **Shift the input:** feed $x_s[n]=x[n-n_0]$. Wherever the rule reads $x[f(n)]$ it now reads $x_s[f(n)]=x[f(n)-n_0]$; an $n$ standing outside $x[\cdot]$ stays $n$.
> 3. Equal for all $n$, $n_0$ and $x$: time-invariant. Otherwise time-varying (one counterexample suffices).

**Worked examples (Lecture 3).** $y=x[\lvert n\rvert]$: step 1 gives $x[\lvert n-n_0\rvert]$, step 2 gives $x[\lvert n\rvert-n_0]$: different, so **time-varying**. $y=n\,x[3n]$: $(n-n_0)\,x[3n-3n_0]$ versus $n\,x[3n-n_0]$: time-varying. A concrete counterexample for $y=x[2n]$: $\delta[n]\mapsto\delta[2n]=\delta[n]$, but $\delta[n-1]\mapsto\delta[2n-1]=0$ for every $n$, not $\delta[n-1]$.

| form of the system | TI? | examples from exams and homework |
|---|---|---|
| function of $x[n-k]$ values only, no explicit $n$ | yes | $x[n]+3$, $\lvert x[n]-x[n-1]\rvert$, $e^{x[n]+1}$, $x[n]x[n+1]$, clipping, median |
| convolution with any fixed $h$ | yes | $x*2^nu[-n]$, $x*u[n+1]$, $x*(-1)^nu[n]$ |
| LCCDE, constant coefficients, at rest | yes | $y[n]=y[n-5]+x[n]+10x[n-1]$ (HW2 #1a) |
| explicit $n$ outside $x$ | no | $\lvert n\rvert x[n]$, $\frac{x[n]}{\lvert n\rvert+1}$, $\cos^2(\frac{\pi}{2}n)\,x[n]$, $(\frac12)^{\lvert n\rvert}x[n]$, $\cos(\frac{\pi}{6}n)\,x[n]$ in an LCCDE (HW2 #1b), window (HW1 #6) |
| index map other than $n-k$ | no | $x[2n]$, $x[\lvert n\rvert]$, $x[\lvert n\rvert+n]$, $2x[\lvert n\rvert]+10$ |
| a sample at a fixed time | no | $x[n]x[0]$, $x[3]x[n]$, $x[n]/x[2]$, $\sin(x[n])+x[0]$ |

> [!trap]
> - **Shifting the input goes inside the index map.** For $y=x[2n]$, $T\{x[n-n_0]\}=x[2n-n_0]$, not $x[2(n-n_0)]$ (that one is the shifted output).
> - **Leave the outside $n$ alone** when shifting the input: for $y=n\,x[n]$, $T\{x[n-n_0]\}=n\,x[n-n_0]$ while $y[n-n_0]=(n-n_0)\,x[n-n_0]$.
> - **Check that the gain really varies on the integers**: $\cos(2\pi n)=1$ for every integer $n$, so $\cos(2\pi n)\,x[n]=x[n]$ is time-invariant; $\cos^2(\frac{\pi}{2}n)$ alternates $1,0,1,0,\dots$ and is not.
> - **TI and causality are unrelated**: "any causal system must be time-invariant" ([[0-midterm-1/past-exams/fall-2023|FA2023 #1a]]) and "a time-varying system cannot be causal" ([[0-midterm-1/past-exams/fall-2019|FA2019 #1f]]) are both False: $y=n\,x[n]$ is causal and time-varying.
> - **TI does not need linearity**: $x[n]+3$ and $e^{x[n]+1}$ are time-invariant and nonlinear.
> - A convolution is time-invariant **whatever $h$ is** (non-causal or unstable included): [[homework/hw2|HW2]] #2.

**Where it appears.** [[1-signals-and-systems/03-system-properties|Lecture 3]] §2.2 (Exercises 3–5); [[homework/hw1|HW1]] #5(c) (clipping: TI), #6(c) (window: time-varying); [[homework/hw2|HW2]] #1, #2. The Shift-invariant column of every property table (7/7 exams) and [[0-midterm-1/past-exams/fall-2025|FA2025 #4a]]. Drill: [[problems/classifying-system-properties]], [[0-midterm-1/system-property-bank]].

**Related.** [[concepts/linearity|linearity]] · [[concepts/causality|causality]] · [[concepts/lti-system|LTI system]] · [[concepts/convolution|convolution]] · [[concepts/discrete-time-signal|discrete-time signal]] (index maps)

### Sources for this page
Lecture 3 §2.2 (Eqs. 8–10, Exercises 3–5; note the notes' typo $x[\lvert n\rvert-n_0\rvert]$ for $x[\lvert n\rvert-n_0]$) and slides 7–9; HW1 #5–#6, HW2 #1–#2 with solutions; past-exam property tables (cross-checked in `verify/exams/property_bank.py`); the $x[2n]$ counterexample in `verify/concepts/verify_glossary_time.py`.
