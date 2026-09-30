---
title: "Lecture 3 — Discrete-time systems: linearity, time-invariance, causality, stability"
description: "What a discrete-time system is, and how to prove or disprove the four properties in every Midterm 1 property table: linearity (superposition), time-invariance (the shift test), causality (no future inputs) and BIBO stability (bounded in, bounded out)."
tags: [lecture, midterm-1, systems]
lecture: 3
---

*Lecture 3 · Fri Aug 28, 2026 · notes + slides "Discrete-time systems" · prev: [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] · next: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]*

> [!abstract] In one breath
> A discrete-time system is any rule $T$ that turns an input sequence $x[n]$ into an output sequence $y[n] = T(x[n])$. Four yes/no properties classify it: **linear** (superposition holds), **time-invariant** (delaying the input only delays the output), **causal** (no future inputs are used) and **BIBO stable** (every bounded input gives a bounded output). To prove a property you must argue for *every* input; to disprove it, *one* concrete counterexample is enough. The four-column property table built on these definitions is on every past Midterm 1 (12 points), and the systems that pass the first two tests, the LTI systems, are the ones [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] describes completely by a single sequence $h[n]$.

## 1. What counts as a system

A **discrete-time system** is any computational process that maps a discrete-time input $x[n]$ to a discrete-time output $y[n]$. Writing the system (the *operator*) as $T$:

$$
x[n] \overset{T}{\longmapsto} y[n], \qquad y[n] = T(x[n]).
$$

Read the first as "$x[n]$ maps to $y[n]$ by $T$" and the second as "$y[n]$ is a function of $x[n]$ described by $T$". $T$ acts on the *whole sequence*: the output at one index may depend on any input samples, and on $n$ itself. Examples from the notes and slides:

- $y[n] = x[n] - x[n-1]$: the difference between the present and the previous sample, a detector of fast changes (figure below);
- $y[n] = \operatorname{median}\{x[n], x[n-1], x[n-2]\}$: a running median, which removes isolated spikes;
- $y[n] = \text{HalfCenterCrop}(x[n])$ or $\text{SnapchatFilter}(x[n])$: image operations are systems too.

Speech recognition, photo editing, trading algorithms and de-noising filters all fit the definition. **Systems are not just filters**; filters are one important kind.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 215" width="640" height="215" role="img" aria-label="A system T maps an input sequence to an output sequence; here the first difference y[n] = x[n] - x[n-1]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="8.0" y1="172.0" x2="244.0" y2="172.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="246.0,172.0 239.0,168.2 239.0,175.8" fill="currentColor"/><text x="244.0" y="190.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">n</text><line x1="65.6" y1="80.0" x2="65.6" y2="180.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="28.0" y1="169.0" x2="28.0" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="28.0" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">−2</text><line x1="46.8" y1="169.0" x2="46.8" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="46.8" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">−1</text><line x1="65.6" y1="169.0" x2="65.6" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="65.6" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">0</text><line x1="84.4" y1="169.0" x2="84.4" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="84.4" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">1</text><line x1="103.2" y1="169.0" x2="103.2" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="103.2" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">2</text><line x1="122.0" y1="169.0" x2="122.0" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="122.0" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">3</text><line x1="140.8" y1="169.0" x2="140.8" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="140.8" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">4</text><line x1="159.6" y1="169.0" x2="159.6" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="159.6" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">5</text><line x1="178.4" y1="169.0" x2="178.4" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="178.4" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">6</text><line x1="197.2" y1="169.0" x2="197.2" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="197.2" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">7</text><line x1="216.0" y1="169.0" x2="216.0" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="216.0" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">8</text><text x="8.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">input  x[n] = u[n] + 2u[n−4]</text><circle cx="28.0" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="46.8" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="65.6" y1="172.0" x2="65.6" y2="146.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="65.6" cy="146.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="84.4" y1="172.0" x2="84.4" y2="146.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="84.4" cy="146.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="103.2" y1="172.0" x2="103.2" y2="146.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="103.2" cy="146.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="122.0" y1="172.0" x2="122.0" y2="146.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="122.0" cy="146.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="140.8" y1="172.0" x2="140.8" y2="94.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="140.8" cy="94.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="159.6" y1="172.0" x2="159.6" y2="94.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="159.6" cy="94.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="178.4" y1="172.0" x2="178.4" y2="94.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="178.4" cy="94.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="197.2" y1="172.0" x2="197.2" y2="94.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="197.2" cy="94.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="216.0" y1="172.0" x2="216.0" y2="94.0" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/><circle cx="216.0" cy="94.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="394.0" y1="172.0" x2="630.0" y2="172.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="632.0,172.0 625.0,168.2 625.0,175.8" fill="currentColor"/><text x="630.0" y="190.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">n</text><line x1="451.6" y1="106.0" x2="451.6" y2="180.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="414.0" y1="169.0" x2="414.0" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="414.0" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">−2</text><line x1="432.8" y1="169.0" x2="432.8" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="432.8" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">−1</text><line x1="451.6" y1="169.0" x2="451.6" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="451.6" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">0</text><line x1="470.4" y1="169.0" x2="470.4" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="470.4" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">1</text><line x1="489.2" y1="169.0" x2="489.2" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="489.2" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">2</text><line x1="508.0" y1="169.0" x2="508.0" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="508.0" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">3</text><line x1="526.8" y1="169.0" x2="526.8" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="526.8" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">4</text><line x1="545.6" y1="169.0" x2="545.6" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="545.6" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">5</text><line x1="564.4" y1="169.0" x2="564.4" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="564.4" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">6</text><line x1="583.2" y1="169.0" x2="583.2" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="583.2" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">7</text><line x1="602.0" y1="169.0" x2="602.0" y2="175.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="602.0" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">8</text><text x="394.0" y="26.0" text-anchor="start" fill="currentColor" style="font-size:13.5px;font-weight:600;">output  y[n] = δ[n] + 2δ[n−4]</text><circle cx="414.0" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="432.8" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="451.6" y1="172.0" x2="451.6" y2="146.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="451.6" cy="146.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="451.6" y="137.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">1</text><circle cx="470.4" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="489.2" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="508.0" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><line x1="526.8" y1="172.0" x2="526.8" y2="120.0" stroke="var(--accent2)" stroke-width="2.2" stroke-linecap="round"/><circle cx="526.8" cy="120.0" r="4.4" fill="var(--accent2)" stroke="none" stroke-width="1.4"/><text x="526.8" y="111.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">2</text><circle cx="545.6" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="564.4" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="583.2" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><circle cx="602.0" cy="172.0" r="2.6" fill="currentColor" stroke="none" stroke-width="1.4" opacity="0.55"/><rect x="268.0" y="70.0" width="104.0" height="58.0" rx="6" fill="var(--accent)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="320.0" y="97.0" text-anchor="middle" fill="currentColor" style="font-size:20px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">T</text><text x="320.0" y="114.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.85">x[n] − x[n−1]</text><line x1="236.0" y1="99.0" x2="259.0" y2="99.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="266.0,99.0 259.0,95.2 259.0,102.8" fill="currentColor"/><line x1="374.0" y1="99.0" x2="397.0" y2="99.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="404.0,99.0 397.0,95.2 397.0,102.8" fill="currentColor"/></svg><figcaption><strong>A system is a rule T that turns a whole input sequence into an output sequence.</strong> Here T is the first difference y[n] = x[n] − x[n−1] from the notes: wherever the input is flat the output is 0, and each jump of the input (by 1 at n = 0, by 2 at n = 4) shows up as a spike of that height. That is why this system is used to detect sudden changes.</figcaption></figure>

## 2. Linearity

> [!key] Linearity (superposition)
> $T$ is **linear** if and only if it satisfies both
> $$
> \begin{aligned}
> T(a\,x[n]) &= a\,T(x[n]) &&\text{(homogeneity)}\\
> T(x_1[n] + x_2[n]) &= T(x_1[n]) + T(x_2[n]) &&\text{(additivity)}
> \end{aligned}
> $$
> or, equivalently, the single condition **superposition**: $T(a\,x_1[n] + b\,x_2[n]) = a\,T(x_1[n]) + b\,T(x_2[n])$ for all inputs and all scalars $a, b$.

> [!recipe] Proving or disproving linearity
> 1. **Guess** by inspection (§6 lists what to look for).
> 2. **Guess "linear"** → prove superposition for *arbitrary* $x_1, x_2, a, b$: name the combined input $v[n] = a\,x_1[n] + b\,x_2[n]$, write $T(v[n])$ from the formula, substitute, regroup into $a\,T(x_1[n]) + b\,T(x_2[n])$.
> 3. **Guess "nonlinear"** → break homogeneity or additivity with one concrete input. Fastest first test: a linear system maps the zero input to the zero output (homogeneity with $a = 0$). Next try $a = -1$ or $a = 2$.

**Notes Exercise 1: $y[n] = x[n] - x[n-1]$.** With $v[n] = a\,x_1[n] + b\,x_2[n]$:

$$
\begin{aligned}
T(v[n]) &= v[n] - v[n-1] = \big(a\,x_1[n] + b\,x_2[n]\big) - \big(a\,x_1[n-1] + b\,x_2[n-1]\big)\\
&= a\big(x_1[n] - x_1[n-1]\big) + b\big(x_2[n] - x_2[n-1]\big)\\
&= a\,T(x_1[n]) + b\,T(x_2[n]). \ \checkmark
\end{aligned}
$$

Linear. The slides' $y[n] = \tfrac12 x[n] + \tfrac12 x[n-1]$ is linear by the identical argument.

**Notes Exercise 2: $y[n] = (x[n])^p$, $p > 0$.** Homogeneity already fails: $T(a\,x[n]) = a^p (x[n])^p = a^p\,T(x[n]) \neq a\,T(x[n])$ for $p \neq 1$. Nonlinear.

**Slides: $y[n] = x[n] + 1$.** $T(a\,x[n]) = a\,x[n] + 1$, but $a\,T(x[n]) = a\,x[n] + a$. Nonlinear. Adding a constant makes a system *affine*, not linear; the zero-input test catches it at once ($x = 0$ gives $y = 1$).

> [!question] Extra practice (slides): linear or nonlinear?
> (1) $y[n] = \lvert x[n]\rvert$ (2) $y[n] = n\,(x[n] - x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$ (annotated deck) or $\max\{0, x[n]\}$ (posted deck) (5) the running median

> [!success]- Answers (annotated slides)
> 1. Nonlinear: $T(a\,x) = \lvert a\rvert\,\lvert x[n]\rvert \neq a\,\lvert x[n]\rvert$ when $a < 0$.
> 2. **Linear**: the factor $n$ is the same for every input, so superposition goes through exactly as in Exercise 1.
> 3. Nonlinear: $e^{a\,x[n]} \neq a\,e^{x[n]}$.
> 4. Nonlinear: $T(a\,x) = a^2\,x[n]\,x[0]$. And $\max\{0, -x\} \neq -\max\{0, x\}$ ($a = -1$).
> 5. Nonlinear: windows $(1, 0, 0)$ and $(0, 1, 0)$ each have median $0$, but their sum $(1, 1, 0)$ has median $1$.

> [!trap] A factor of $n$ does not make a system nonlinear
> $y[n] = n\,x[n]$, $\cos(\pi n/2)\,x[n]$ and $(0.8+0.8j)^n\,x[n]$ are all **linear**: the multiplier is a fixed sequence, identical for every input. What such factors break is *time-invariance* (§3). Linearity is about what happens to the **values** of $x$: anything that bends the values ($\lvert x\rvert$, $x^2$, $e^{x}$, $\log x$, $\sin x$, clipping, max, median), multiplies input samples together ($x[n]\,x[n+1]$, $x[3]\,x[n]$), divides by an input sample, or adds a constant makes the system nonlinear.

## 3. Time-invariance

> [!key] Time-invariance (shift-invariance)
> $T$ is **time-invariant** if and only if, for every input and every integer shift $n_0$,
> $$
> y[n - n_0] = T(x[n - n_0]), \qquad n \in \mathbb{Z}.
> $$
> Shifting the input by $n_0$ samples shifts the output by the same $n_0$ samples and does nothing else. "Shift-invariant" (and "LSI" on older exams) means the same thing.

The notes warn that this intuitive definition is the hardest of the four to apply, because the two sides are built differently:

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 196" width="640" height="196" role="img" aria-label="Time-invariance compares shift-then-system with system-then-shift" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="18.0" y="57.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="56.0" y1="52.0" x2="91.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="98.0,52.0 91.0,48.1 91.0,55.9" fill="currentColor"/><rect x="100.0" y="30.0" width="96.0" height="44.0" rx="6" fill="var(--accent)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="148.0" y="57.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">T</text><line x1="196.0" y1="52.0" x2="255.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,52.0 255.0,48.1 255.0,55.9" fill="currentColor"/><text x="229.0" y="42.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><rect x="264.0" y="30.0" width="96.0" height="44.0" rx="6" fill="var(--accent2)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="312.0" y="57.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">delay n₀</text><line x1="360.0" y1="52.0" x2="393.0" y2="52.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="400.0,52.0 393.0,48.1 393.0,55.9" fill="currentColor"/><text x="406.0" y="57.0" text-anchor="start" fill="var(--accent)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">y[n − n₀]</text><text x="18.0" y="151.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><line x1="56.0" y1="146.0" x2="91.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="98.0,146.0 91.0,142.2 91.0,149.8" fill="currentColor"/><rect x="100.0" y="124.0" width="96.0" height="44.0" rx="6" fill="var(--accent2)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="148.0" y="151.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">delay n₀</text><line x1="196.0" y1="146.0" x2="255.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="262.0,146.0 255.0,142.2 255.0,149.8" fill="currentColor"/><text x="229.0" y="136.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n − n₀]</text><rect x="264.0" y="124.0" width="96.0" height="44.0" rx="6" fill="var(--accent)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.4"/><text x="312.0" y="151.2" text-anchor="middle" fill="currentColor" style="font-size:15px;font-weight:600;">T</text><line x1="360.0" y1="146.0" x2="393.0" y2="146.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><polygon points="400.0,146.0 393.0,142.2 393.0,149.8" fill="currentColor"/><text x="406.0" y="151.0" text-anchor="start" fill="var(--accent2)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">T(x[n − n₀])</text><text x="18.0" y="20.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.85">system, then shift  (“left side”)</text><text x="18.0" y="114.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;" opacity="0.85">shift, then system  (“right side”)</text><text x="548.0" y="92.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;" opacity="0.9">equal for every</text><text x="548.0" y="108.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;" opacity="0.9">x and every n₀?</text><text x="548.0" y="128.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">⇔ time-invariant</text><line x1="510.0" y1="60.0" x2="540.0" y2="78.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="540.0" y1="136.0" x2="520.0" y2="142.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/></svg><figcaption><strong>The time-invariance test compares two orders of doing things.</strong> Top: run the system, then delay the output by n₀. Bottom: delay the input by n₀, then run the system. The system is time-invariant exactly when both orders give the same sequence, for every input and every shift. Any dependence on absolute time (a coefficient like n, a fixed sample like x[0], an index like 2n or −n) breaks the tie.</figcaption></figure>

> [!recipe] The shift test, done right
> 1. **Left side (system, then shift).** Write $y[n]$ from the formula and replace **every** $n$ by $n - n_0$: inside the brackets of $x$ *and* in coefficients such as $n$, $\lvert n\rvert$, $\cos(\pi n/2)$.
> 2. **Right side (shift, then system).** Name the shifted input $v[n] = x[n - n_0]$ and apply the system *to $v$*. The system acts on its time variable $n$ only; $n_0$ is a constant that lives inside $v$. If $y[n] = x[f(n)]$, then $T(v)[n] = v[f(n)] = x[f(n) - n_0]$: the shift is subtracted from the *whole* argument, after $f$ has acted on $n$.
> 3. **Compare.** Equal for all $n$ and $n_0$ → time-invariant. Different → time-varying (confirm with a concrete $x$ and $n_0$ if you like).

**Notes Exercise 4: $y[n] = x[n] - x[n-1]$.** Left: $y[n-n_0] = x[(n-n_0)] - x[(n-n_0)-1]$. Right: $T(x[n-n_0]) = x[n-n_0] - x[n-1-n_0]$. Equal: **time-invariant**.

**Notes Exercise 3: $y[n] = x[\lvert n\rvert]$.** Left: $y[n-n_0] = x[\lvert n-n_0\rvert]$. Right: $v[\lvert n\rvert] = x[\lvert n\rvert - n_0]$. Different (at $n = 0$, $n_0 = 1$: $x[1]$ versus $x[-1]$): **time-varying**. The notes print the right side as $x[\lvert n\rvert - n_0\rvert]$; the stray bar is a typo.

**Notes Exercise 5: $y[n] = n\,x[3n]$.** Left: $y[n-n_0] = (n-n_0)\,x[3(n-n_0)] = (n-n_0)\,x[3n-3n_0]$. Right: $T(x[n-n_0]) = n\,x[3n-n_0]$. Different: **time-varying**. On the right, only the argument of $x$ picks up the shift; the $n$ in front stays $n$.

**Slides: $y[n] = x[2n]$, with numbers.** Abstractly, left $= x[2n-2n_0]$ and right $= x[2n-n_0]$. The annotated slide makes it concrete with $x[n] = \{\underset{\uparrow}{2}, 4, 6, 1, 3, 5\}$ (so $x[0] = 2$) and $n_0 = 1$:

$$
\begin{aligned}
y[n] = x[2n] &= \{\underset{\uparrow}{2},\ 6,\ 3\} &&\text{(keeps } x[0], x[2], x[4])\\
y[n-1] &= \{\underset{\uparrow}{0},\ 2,\ 6,\ 3\}\\
T(x[n-1]) = x[2n-1] &= \{\underset{\uparrow}{0},\ 4,\ 1,\ 5\} &&\text{(keeps } x[-1], x[1], x[3], x[5])
\end{aligned}
$$

The two differ, so $x[2n]$ is **time-varying**: after the shift, *different* input samples survive the downsampling. One counterexample is a complete proof. The same check in NumPy:

```python
import numpy as np
x = np.array([2, 4, 6, 1, 3, 5])      # x[0..5]; zero elsewhere
T = lambda s: s[::2]                   # y[n] = x[2n] for n >= 0
x_shift = np.r_[0, x]                  # x[n-1]: one zero in front
print("y[n]          :", T(x))
print("y[n-1]        :", np.r_[0, T(x)])
print("T(x[n-1])     :", T(x_shift))
```

```text
y[n]          : [2 6 3]
y[n-1]        : [0 2 6 3]
T(x[n-1])     : [0 4 1 5]
```

> [!question] Extra practice (slides): time-invariant or time-varying?
> (1) $y[n] = x[\lvert n\rvert]$ (2) $y[n] = n\,(x[n]-x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers (annotated slides)
> 1. Time-varying: Exercise 3 above.
> 2. Time-varying: $y[n-n_0] = (n-n_0)\big(x[n-n_0] - x[n-n_0-1]\big)$ but $T(x[n-n_0]) = n\big(x[n-n_0] - x[n-1-n_0]\big)$. Replace *every* $n$ on the left.
> 3. Time-invariant: with $v[n] = x[n-n_0]$, $T(v)[n] = e^{v[n]} = e^{x[n-n_0]} = y[n-n_0]$. Any memoryless function of $x[n]$ alone is time-invariant.
> 4. Time-varying: $y[n-n_0] = x[n-n_0]\,x[0]$ but $T(x[n-n_0]) = x[n-n_0]\,x[-n_0]$. The sample at $n = 0$ is "locked in" before the shift; shifting the input changes *which* sample sits at $0$.

> [!trap] Time reversal is time-varying
> $y[n] = x[-n]$: left $y[n-n_0] = x[-(n-n_0)] = x[-n+n_0]$, right $T(x[n-n_0]) = x[-n-n_0]$. Delaying the input *advances* the reversed output. The same goes for every index map other than $n - k$: $x[2n]$, $x[\lvert n\rvert]$, $x[-n+3]$ and $x[\lvert n\rvert + n]$ are all time-varying (and all linear).

## 4. Causality

> [!key] Causality
> A system is **causal** if its output at every time $n$ depends only on **present or past** input (and output) samples: $y[n]$ never uses $x[m]$ with $m > n$.

> [!recipe] Causality check
> For each input term $x[g(n)]$, ask whether $g(n) \le n$ for **every** integer $n$, negative ones included. If so for all terms, the system is causal. If some $n$ gives $g(n) > n$, that $n$ is your counterexample. Coefficients ($n$, $n+1$, $\cos(\pi n/3)$) do not matter: they do not select input samples.

**Notes Exercise 6: $y[n] = x[n] + x[n-2] - x[n-4]$.** The indices $n$, $n-2$, $n-4$ are all $\le n$: **causal**. So is the slides' 3-point average $\tfrac13\big(x[n] + x[n-1] + x[n-2]\big)$.

**Slides: $y[n] = x[\lvert n\rvert]$.** At $n = -2$: $y[-2] = x[2]$, a future input. **Non-causal.** For $n \ge 0$ it looks harmless ($x[\lvert n\rvert] = x[n]$); the future dependence hides at negative $n$.

> [!question] Extra practice (slides): causal?
> (1) $y[n] = x[\lvert n\rvert - n]$ (2) $y[n] = (n+1)\,(x[n] - x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers (annotated slides)
> 1. Non-causal: $y[-1] = x[\lvert -1\rvert - (-1)] = x[2]$.
> 2. Causal: $y[n]$ uses $x[n]$ (present) and $x[n-1]$ (past); the factor $(n+1)$ does not change which samples are used.
> 3. Causal: only the present sample.
> 4. Non-causal: $y[-1] = x[-1]\,x[0]$ needs $x[0]$, which is in the future at time $-1$.

> [!trap] Check negative $n$ and positive $n$
> $x[2n]$ reads the past for $n < 0$ (because $2n < n$) but the future for $n > 0$ ($y[1] = x[2]$): non-causal. $n\,x[3n]$: $y[1] = x[3]$, non-causal. For a convolution system $y = x * h$ (Lecture 4), causal $\Leftrightarrow h[n] = 0$ for $n < 0$, so $x[n] * u[n+1]$ is **not** causal ($h[-1] = 1$).

## 5. BIBO stability

> [!key] BIBO stability
> $T$ is **bounded-input bounded-output (BIBO) stable** if for **every** input with $\lvert x[n]\rvert < \beta < \infty$ for all $n$, the output satisfies $\lvert y[n]\rvert < \alpha < \infty$ for all $n$. The bound $\alpha$ may depend on $\beta$, but not on $n$.

> [!recipe] Stability check
> - **To prove stable:** assume $\lvert x[n]\rvert < \beta$ and bound $\lvert y[n]\rvert$ by a constant, with the triangle inequality $\lvert a+b\rvert \le \lvert a\rvert + \lvert b\rvert$ and facts such as $\lvert\sin(\cdot)\rvert \le 1$.
> - **To prove unstable:** exhibit **one** bounded input whose output is unbounded: it grows without limit as $n \to \pm\infty$, or it is infinite at some $n$ (a $\log 0$, a division by $0$).

**Notes Exercise 7: $y[n] = x^{10}[n] + e^{x[n]}$.**

$$
\lvert y[n]\rvert \le \lvert x[n]\rvert^{10} + e^{\lvert x[n]\rvert} < \beta^{10} + e^{\beta} = \alpha < \infty .
$$

**Stable.**

**Slides.** $y[n] = \sin^2(x[n])$ satisfies $0 \le y[n] \le 1$ for any input: **stable**. $y[n] = \ln(\lvert x[n]\rvert)$: the bounded input $x[n] = 0$ (or $x[n] = \delta[n]$, which is $0$ for $n \ne 0$) gives $\ln 0 = -\infty$: **not stable**.

> [!question] Extra practice (slides): BIBO stable?
> (1) $y[n] = \dfrac{x[n]}{\lvert n\rvert + 1}$ (2) $y[n] = n\,(x[n]-x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers (annotated slides)
> 1. Stable: $\lvert y[n]\rvert < \beta/(\lvert n\rvert + 1) \le \beta$.
> 2. **Unstable**: $\lvert y[n]\rvert = \lvert n\rvert\,\lvert x[n]-x[n-1]\rvert$ can grow like $2\beta\lvert n\rvert$. Concretely, $x[n] = (-1)^n$ (bounded by 1) gives $\lvert y[n]\rvert = 2\lvert n\rvert \to \infty$.
> 3. Stable: $e^{x[n]} < e^{\beta}$.
> 4. Stable: $\lvert x[n]\,x[0]\rvert < \beta^2$.

> [!trap] An exponential of the input is harmless; an exponential of time is not
> $e^{x[n]}$ and $e^{x[n]+1}$ are **stable** (a bounded exponent gives a bounded result), but $2^n\,x[n]$ and $(0.8+0.8j)^n\,x[n]$ are **unstable**: the multiplier grows with $n$ ($\lvert 0.8+0.8j\rvert = 0.8\sqrt2 \approx 1.13 > 1$), so $x[n] = 1$ already gives an unbounded output. Also remember that stability speaks about *bounded* inputs only: a stable system fed an unbounded input may still return a bounded output. "BIBO stable ⇒ unbounded in gives unbounded out" is **False** ([[0-midterm-1/past-exams/spring-2023|SP2023 #1(b)]], [[0-midterm-1/past-exams/fall-2025|FA2025 #1(e)]]).

## 6. The property table: a row in 30 seconds

> [!recipe] Reading the four properties off a formula
> | property | it **fails** when you see… | it **holds** for… |
> |---|---|---|
> | linear | a function of the input's value ($\lvert x\rvert$, $x^2$, $e^{x}$, $\log x$, $\sin x$, clip, max, median); a product of input samples ($x[n]\,x[n+1]$, $x[3]\,x[n]$); division by an input sample; an added constant ($x[n]+3$) | sums of input samples times fixed coefficients, even coefficients that depend on $n$; pure index maps $x[f(n)]$ |
> | time-invariant | $n$ outside the brackets ($n\,x[n]$, $\cos(\pi n/2)\,x[n]$, a window); an index map other than $n-k$ ($x[2n]$, $x[-n]$, $x[\lvert n\rvert]$); a fixed sample ($x[0]$, $x[2]$) | constant-coefficient sums of $x[n-k]$; any function of $x[n]$ alone; convolution with a fixed $h$ |
> | causal | some $n$ (try negative ones!) whose input index exceeds $n$: $x[n+1]$, $x[\lvert n\rvert]$, $x[2n]$, $x[0]$; convolution with $h[n] \ne 0$ for some $n < 0$ | only $x[n-k]$ with $k \ge 0$ |
> | BIBO stable | a multiplier that grows ($n$, $\lvert n\rvert$, $\log(\lvert n\rvert+1)$, $2^n$); $\log x$ or $1/x$ (a bounded input may be $0$); convolution with an $h$ that is not absolutely summable | bounded multipliers times bounded functions of finitely many input samples; convolution with $\sum_n \lvert h[n]\rvert < \infty$ |

> [!question] Self-test: rows from past exam tables (Linear / Time-invariant / Causal / Stable?)
> - (a) $y[n] = \lvert n\rvert\,x[n]$ (FA2025)
> - (b) $y[n] = \lvert x[n]-x[n-1]\rvert$ (FA2025)
> - (c) $y[n] = 2x[\lvert n\rvert] + 10$ (SP2025)
> - (d) $y[n] = x[n]\,x[n+1]$ (FA2024)
> - (e) $y[n] = \sin(x[n]) + x[0]$ (FA2024)
> - (f) $y[n] = \log(\lvert n\rvert+1)\,x[n]$ (FA2023)
> - (g) $y[n] = x[n]/x[2]$ (SP2023)
> - (h) $y[n] = x[\lvert n\rvert + n]$ (FA2019)

> [!success]- Answers (official keys where the exam asked, re-checked numerically; FA2019 #2 had no stability column)
> | system | L | TI | C | S | the deciding observation |
> |---|---|---|---|---|---|
> | (a) $\lvert n\rvert\,x[n]$ | Y | N | Y | N | coefficient $\lvert n\rvert$: time-varying, and $x = 1$ gives $y = \lvert n\rvert$ |
> | (b) $\lvert x[n]-x[n-1]\rvert$ | N | Y | Y | Y | absolute value of a TI, causal, stable difference |
> | (c) $2x[\lvert n\rvert]+10$ | N | N | N | Y | the $+10$ kills linearity; $x[\lvert n\rvert]$ as in Exercise 3 |
> | (d) $x[n]\,x[n+1]$ | N | Y | N | Y | product of samples; $x[n+1]$ is the future |
> | (e) $\sin(x[n]) + x[0]$ | N | N | N | Y | the fixed sample $x[0]$ breaks TI and (at $n < 0$) causality; $\lvert y\rvert \le 1 + \beta$ |
> | (f) $\log(\lvert n\rvert+1)\,x[n]$ | Y | N | Y | N | the coefficient grows slowly, but without bound |
> | (g) $x[n]/x[2]$ | N | N | N | N | $T(a\,x) = T(x)$; $x[2]$ is fixed and in the future for $n < 2$; $x[2] = 0$ divides by zero |
> | (h) $x[\lvert n\rvert + n]$ | Y | N | N | Y | pure index map; $y[1] = x[2]$ |
>
> Every system from every exam table and homework, with proofs: [[0-midterm-1/system-property-bank|system-property bank]].

## 7. On the exam

> [!exam] Where Lecture 3 shows up
> - **The property table, on 7 of 7 past exams (12 points):** [[0-midterm-1/past-exams/fall-2025|FA2025 #2]], [[0-midterm-1/past-exams/spring-2025|SP2025 #2]], [[0-midterm-1/past-exams/fall-2024|FA2024 #2]], [[0-midterm-1/past-exams/fall-2023|FA2023 #2]], [[0-midterm-1/past-exams/spring-2023|SP2023 #2]], [[0-midterm-1/past-exams/spring-2021|SP2021 #3]], [[0-midterm-1/past-exams/fall-2019|FA2019 #2]]. Three systems × four yes/no boxes, graded on the boxes only. Rows such as $x[n] * u[n+1]$ use Lecture 4's rules (LTI; causal ⇔ $h[n] = 0$ for $n<0$; stable ⇔ $\sum\lvert h[n]\rvert < \infty$). Recipe page: [[problems/classifying-system-properties]].
> - **True/False (every exam).** "Any causal system must be time-invariant" ([[0-midterm-1/past-exams/fall-2023|FA2023 #1(a)]], False) and "a time-varying system cannot be causal" ([[0-midterm-1/past-exams/fall-2019|FA2019 #1(f)]], False): the four properties are independent, and $y[n] = n\,x[n]$ is causal *and* time-varying. "If the unit pulse response is absolutely summable, the system must be BIBO stable whether or not it is LSI" ([[0-midterm-1/past-exams/spring-2025|SP2025 #1(b)]], False): $y[n] = n\,x[n]$ answers $\delta[n]$ with $n\,\delta[n] = 0$, yet $x[n] = 1$ gives $y[n] = n$. More in the [[0-midterm-1/true-false-bank|T/F bank]].
> - **Proofs in words:** [[0-midterm-1/past-exams/fall-2025|FA2025 #4]] asks you to show the modified moving average $y[n] = \tfrac1L\sum_{k=0}^{L-1} x[n-Sk]$ is linear and time-invariant, which is §2 and §3 verbatim.
> - **Homework:** [[homework/hw1|HW1]] #5 (clipping: nonlinear, time-invariant) and #6 (windowing: linear, time-varying); [[homework/hw2|HW2]] #1 (two recursions and $(\tfrac12)^{\lvert n\rvert}x[n]$).

## Related

- [[concepts/linearity|Linearity]] · [[concepts/time-invariance|Time-invariance]] · [[concepts/causality|Causality]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/lti-system|LTI system]]
- Next: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] shows that an LTI system is completely described by its impulse response and turns causality and stability into tests on $h[n]$; [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] turns them into tests on poles and the ROC.
- Practice: [[problems/classifying-system-properties|classifying system properties]] · [[0-midterm-1/system-property-bank|system-property bank]] · [[0-midterm-1/practice-drills|practice drills]]

### Sources for this page
Snyder, ECE 310 Lecture 3 notes (definitions, Exercises 1–7) and slides "Discrete-time systems" (Aug 28, 2026), including the annotated in-class deck for the practice answers. The annotated deck's fourth extra-practice system is $x[n]\,x[0]$ where the posted deck has $\max\{0, x[n]\}$; both are covered above. HW1 #5–6, HW2 #1; the property tables and T/F items of the seven past Midterm 1 exams (FA2019–FA2025). Every verdict and number on this page is checked in `verify/lectures/l3_systems.py`.
