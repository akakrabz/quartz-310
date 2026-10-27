---
title: "Time-invariance"
description: "Shift the input by n0 and the output shifts by n0: the two-sided shift test, Lecture 3's exercises, the rules that decide table rows at a glance, why x[2n], x[|n|], n·x[n] are time-varying."
tags: [concept, systems, midterm-1]
aliases: ["shift-invariance", "time-invariant", "shift-invariant", "time-varying", "shift-varying", "TI", "SI", "shift test"]
---

*Lecture 3 (Fri Aug 28) §2.2 · [[homework/hw1|HW1]] #5–#6 · [[homework/hw2|HW2]] #1–#2 · family: [[problems/classifying-system-properties|Classifying system properties]]*

> [!abstract] In one breath
> - Time-invariant ⇔ "system, then shift" equals "shift, then system" for every input and every $n_0$.
> - Left side: replace **every** $n$ by $n-n_0$. Right side: the shift goes only inside $x[\cdot]$; an $n$ outside stays $n$.
> - Explicit $n$ outside the brackets, index maps other than $n-k$, and fixed samples like $x[0]$ all break it.

## 1. Definition

> [!key] Time-invariance (shift-invariance) (Lecture 3, eqs. 8–10)
> $T$ is **time-invariant** if and only if, for every input and every integer $n_0$,
> $$
> \begin{gathered}
> y[n - n_0] = T(x[n - n_0]), \qquad \text{equivalently}\\
> T(x)[n-n_0] = T(x[n-n_0]), \qquad n \in \mathbb{Z}.
> \end{gathered}
> $$
> Left: system, then shift. Right: shift, then system. If the system acts on the index, $y[n] = x[f(n)]$, the test reads $x[f(n-n_0)] \overset{?}{=} x[f(n)-n_0]$ (eq. 10). "LSI" on older exams = LTI.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 196" width="640" height="196" role="img" aria-label="Time-invariance compares shift-then-system with system-then-shift" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="18.0" y="57.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="56.0" y1="52.0" x2="91.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="98.0,52.0 91.0,48.1 91.0,55.9" fill="currentColor"/><rect x="100.0" y="30.0" width="96.0" height="44.0" rx="6" fill="var(--accent)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="148.0" y="57.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">T</text><line x1="196.0" y1="52.0" x2="255.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,52.0 255.0,48.1 255.0,55.9" fill="currentColor"/><text x="229.0" y="42.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><rect x="264.0" y="30.0" width="96.0" height="44.0" rx="6" fill="var(--accent2)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="312.0" y="57.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">delay n₀</text><line x1="360.0" y1="52.0" x2="393.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="400.0,52.0 393.0,48.1 393.0,55.9" fill="currentColor"/><text x="406.0" y="57.0" text-anchor="start" fill="var(--accent)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">y[n − n₀]</text><text x="18.0" y="151.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="56.0" y1="146.0" x2="91.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="98.0,146.0 91.0,142.2 91.0,149.8" fill="currentColor"/><rect x="100.0" y="124.0" width="96.0" height="44.0" rx="6" fill="var(--accent2)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="148.0" y="151.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">delay n₀</text><line x1="196.0" y1="146.0" x2="255.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,146.0 255.0,142.2 255.0,149.8" fill="currentColor"/><text x="229.0" y="136.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n − n₀]</text><rect x="264.0" y="124.0" width="96.0" height="44.0" rx="6" fill="var(--accent)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="312.0" y="151.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">T</text><line x1="360.0" y1="146.0" x2="393.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="400.0,146.0 393.0,142.2 393.0,149.8" fill="currentColor"/><text x="406.0" y="151.0" text-anchor="start" fill="var(--accent2)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">T(x[n − n₀])</text><text x="18.0" y="20.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.85">system, then shift  (“left side”)</text><text x="18.0" y="114.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.85">shift, then system  (“right side”)</text><text x="548.0" y="92.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;" opacity="0.9">equal for every</text><text x="548.0" y="108.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;" opacity="0.9">x and every n₀?</text><text x="548.0" y="128.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">⇔ time-invariant</text><line x1="510.0" y1="60.0" x2="540.0" y2="78.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="540.0" y1="136.0" x2="520.0" y2="142.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/></svg><figcaption><strong>The shift test compares two orders.</strong> Top: run the system, then delay by n₀; bottom: delay the input, then run the system — time-invariant exactly when both agree for every input and shift.</figcaption></figure>

## 2. The shift test

> [!recipe] The shift test (the hardest of the four)
> 1. **Left:** write $y[n]$, replace **every** $n$ by $n - n_0$, including coefficients ($n$, $\lvert n\rvert$, $\cos(\pi n/2)$).
> 2. **Right:** apply the system to $v[n] = x[n - n_0]$. The system acts on $n$ only; $n_0$ is a constant inside $v$. Wherever the rule reads $x[f(n)]$ it now reads $x[f(n) - n_0]$; an $n$ standing outside $x[\cdot]$ stays $n$.
> 3. **Compare** for all $n$, $n_0$ and $x$. Equal: time-invariant. Otherwise time-varying (one counterexample suffices).

> [!question] Notes Exercises 3–5: time-invariant?
> (E3) $y[n] = x[\lvert n\rvert]$ (E4) $y[n] = x[n] - x[n-1]$ (E5) $y[n] = n\,x[3n]$

> [!success]- Answers
> **E3, time-varying.** Left $x[\lvert n-n_0\rvert]$; right $v[\lvert n\rvert] = x[\lvert n\rvert - n_0]$. At $n = 0$, $n_0 = 1$: $x[1]$ vs $x[-1]$. (The notes print $x[\lvert n\rvert - n_0\rvert]$; the stray bar is a typo.)
> **E4, time-invariant.** Left $x[(n-n_0)] - x[(n-n_0)-1]$; right $x[n-n_0] - x[n-1-n_0]$: equal.
> **E5, time-varying.** Left $(n-n_0)\,x[3n-3n_0]$; right $n\,x[3n-n_0]$. Only the argument of $x$ picks up the shift on the right.

> [!question] Slide 8: $y[n] = x[2n]$ with $x[n] = \{\underset{\uparrow}{2}, 4, 6, 1, 3, 5\}$, $n_0 = 1$

> [!success]- Answer
> Abstractly left $x[2n-2n_0]$, right $x[2n-n_0]$. Concretely:
> $$
> \begin{aligned}
> y[n] = x[2n] &= \{\underset{\uparrow}{2},\ 6,\ 3\} &&\text{(keeps } x[0], x[2], x[4])\\
> y[n-1] &= \{\underset{\uparrow}{0},\ 2,\ 6,\ 3\}\\
> T(x[n-1]) = x[2n-1] &= \{\underset{\uparrow}{0},\ 4,\ 1,\ 5\} &&\text{(keeps } x[-1], x[1], x[3], x[5])
> \end{aligned}
> $$
> Different: **time-varying** (different samples survive the downsampling). Another counterexample: $\delta[n]\mapsto\delta[2n]=\delta[n]$, but $\delta[n-1]\mapsto\delta[2n-1]=0$ for every $n$.

> [!question] Extra practice (slide 9): time-invariant?
> (1) $y[n] = x[\lvert n\rvert]$ (2) $y[n] = n\,(x[n]-x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers
> 1. Time-varying (E3).
> 2. Time-varying: $y[n-n_0] = (n-n_0)\big(x[n-n_0] - x[n-n_0-1]\big)$ but $T(x[n-n_0]) = n\big(x[n-n_0] - x[n-1-n_0]\big)$.
> 3. Time-invariant: $T(v)[n] = e^{v[n]} = e^{x[n-n_0]} = y[n-n_0]$. Any memoryless function of $x[n]$ alone is TI.
> 4. Time-varying: $y[n-n_0] = x[n-n_0]\,x[0]$ but $T(x[n-n_0]) = x[n-n_0]\,x[-n_0]$.

## 3. Reading time-invariance off a formula

| form of the system | TI? | examples from exams and homework |
|---|---|---|
| function of $x[n-k]$ values only, no explicit $n$ | yes | $x[n]+3$, $\lvert x[n]-x[n-1]\rvert$, $e^{x[n]+1}$, $x[n]x[n+1]$, clipping, median |
| convolution with any fixed $h$ | yes | $x*2^nu[-n]$, $x*u[n+1]$, $x*(-1)^nu[n]$ |
| LCCDE, constant coefficients, at rest | yes | $y[n]=y[n-5]+x[n]+10x[n-1]$ (HW2 #1a) |
| explicit $n$ outside $x$ | no | $\lvert n\rvert x[n]$, $\frac{x[n]}{\lvert n\rvert+1}$, $\cos^2(\frac{\pi}{2}n)\,x[n]$, $(\frac12)^{\lvert n\rvert}x[n]$, $\cos(\frac{\pi}{6}n)\,x[n]$ in an LCCDE (HW2 #1b), window (HW1 #6) |
| index map other than $n-k$ | no | $x[2n]$, $x[-n]$, $x[\lvert n\rvert]$, $x[\lvert n\rvert+n]$, $2x[\lvert n\rvert]+10$ |
| a sample at a fixed time | no | $x[n]x[0]$, $x[3]x[n]$, $x[n]/x[2]$, $\sin(x[n])+x[0]$ |

All four properties in one table: [[concepts/lti-system|LTI system]] §3.

> [!trap]
> - **Shifting the input goes inside the index map.** For $y=x[2n]$, $T\{x[n-n_0]\}=x[2n-n_0]$, not $x[2(n-n_0)]$ (that one is the shifted output); for $x[-n]$: left $x[-n+n_0]$, right $x[-n-n_0]$. Every index map other than $n-k$ is time-varying (and linear).
> - **Leave the outside $n$ alone** when shifting the input: for $y=n\,x[n]$, $T\{x[n-n_0]\}=n\,x[n-n_0]$ while $y[n-n_0]=(n-n_0)\,x[n-n_0]$.
> - **Check that the gain really varies on the integers**: $\cos(2\pi n)=1$ for every integer $n$, so $\cos(2\pi n)\,x[n]=x[n]$ is time-invariant; $\cos^2(\frac{\pi}{2}n)$ alternates $1,0,1,0,\dots$ and is not.
> - **TI and causality are unrelated**: "any causal system must be time-invariant" ([[exams/midterm-1/past-exams/fall-2023|FA2023 #1a]]) and "a time-varying system cannot be causal" ([[exams/midterm-1/past-exams/fall-2019|FA2019 #1f]]) are both False: $y=n\,x[n]$ is causal and time-varying.
> - **TI does not need linearity**: $x[n]+3$ and $e^{x[n]+1}$ are time-invariant and nonlinear.
> - A convolution is time-invariant **whatever $h$ is** (non-causal or unstable included): [[homework/hw2|HW2]] #2.

> [!exam] The Shift-invariant column of the property table, 7 of 7 exams
> Three systems × four yes/no boxes; plus T/F on independence from causality.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #2, #4a]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #2]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #2]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1a, #2]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #2]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #3]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1f, #2]] · [[exams/midterm-1/system-property-bank|system-property bank]]

**Where it appears:** [[1-signals-and-systems/03-system-properties|Lecture 3]] §2.2 (Exercises 3–5, slides 7–9); [[homework/hw1|HW1]] #5(c) (clipping: TI), #6(c) (window: time-varying); [[homework/hw2|HW2]] #1, #2; [[problems/classifying-system-properties|classifying system properties]], [[demos/practice-drills|practice drills]].

## Related
[[concepts/linearity|linearity]] · [[concepts/causality|causality]] · [[concepts/lti-system|LTI system]] · [[concepts/convolution|convolution]] · [[concepts/discrete-time-signal|discrete-time signal]] (index maps)

### Sources for this page
Lecture 3 §2.2 (eqs. 8–10, Exercises 3–5; note the notes' typo $x[\lvert n\rvert-n_0\rvert]$ for $x[\lvert n\rvert-n_0]$) and slides 7–9 with the annotated deck; HW1 #5–#6, HW2 #1–#2 with solutions; past-exam property tables.
