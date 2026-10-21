---
title: "Marginal stability"
description: "Simple poles on the unit circle: h[n] bounded but not absolutely summable, so unstable; only inputs with a matching unit-circle pole (double pole, resonance) give unbounded outputs."
tags: [concept, stability, z-transform, roc]
aliases: ["marginally stable"]
---

> [!key] Definition (Lecture 11)
> ROC of $H(z)$ bounded by the unit circle without containing it; causal: no poles outside, at least one **simple** pole **on** $|z|=1$.
> - **Not BIBO stable:** $h$ bounded, $\sum_n |h[n]| = \infty$ ($h=u[n]$).
> - Unbounded output **only** for an input with a pole at the same unit-circle location: $Y$ gets a double pole,
> $$
> \frac{1}{(1-e^{j\omega}z^{-1})^2} \leftrightarrow (n+1)e^{j\omega n}u[n],\quad |z|>1 .
> $$

> [!example] Accumulator $H(z) = \frac{1}{1-z^{-1}}$
> $x=u[n]$: $y=(n+1)u[n]$, unbounded. $x=(-1)^nu[n]$ or $(\frac12)^nu[n]$: bounded. $x=\delta[n]-\delta[n-1]$: $y=\delta[n]$.

> [!recipe] Which bounded inputs give an unbounded output?
> 1. List the poles of $H$ on $|z|=1$.
> 2. Input poles: $e^{j\omega n}u[n]\to e^{j\omega}$; $\cos/\sin(\omega n)u[n]\to e^{\pm j\omega}$; $u[n]\to1$; $(-1)^nu[n]\to-1$; finite inputs none.
> 3. Cancel input zeros against system poles.
> 4. Unbounded iff an input pole lands **exactly** on a unit-circle pole of $H$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" width="760" height="330" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ahpm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="50.0" y1="165.0" x2="350.0" y2="165.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="200.0" y1="15.0" x2="200.0" y2="315.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="200.0" cy="165.0" r="120.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><text x="350.0" y="159.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="206.0" y="27.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><line x1="283.0" y1="158.0" x2="297.0" y2="172.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="283.0" y1="172.0" x2="297.0" y2="158.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="193.0" y1="38.0" x2="207.0" y2="52.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="193.0" y1="52.0" x2="207.0" y2="38.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="287.3" y1="83.8" x2="301.3" y2="97.8" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="287.3" y1="97.8" x2="301.3" y2="83.8" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><rect x="134.0" y="55.1" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><rect x="134.0" y="262.9" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="200.0" cy="45.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="2"/><path d="M242.0,165.0 A42,42 0 0,0 233.0,139.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><text x="250.0" y="154.0" text-anchor="start" fill="var(--hi)" style="font-size:12px;">2/3 rad</text><path d="M226.0,165.0 A26,26 0 0,0 187.0,142.5" fill="none" stroke="var(--accent2)" stroke-width="1.4"/><text x="170.0" y="135.0" text-anchor="end" fill="var(--accent2)" style="font-size:12px;">2π/3</text><text x="306.3" y="82.8" text-anchor="start" fill="var(--hi)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">j2/3</tspan></text><text x="218.0" y="33.0" text-anchor="start" fill="var(--hi)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">j</text><text x="290.0" y="187.0" text-anchor="middle" fill="var(--hi)" style="font-size:14px;">¾</text><text x="128.0" y="51.1" text-anchor="end" fill="var(--accent2)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">j2π/3</tspan></text><text x="128.0" y="290.9" text-anchor="end" fill="var(--accent2)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">−j2π/3</tspan></text><line x1="382.0" y1="54.0" x2="394.0" y2="66.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="382.0" y1="66.0" x2="394.0" y2="54.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="406.0" y="65.0" text-anchor="start" fill="currentColor" style="font-size:13px;">poles of H(z): ¾, j, e<tspan dy="-6" font-size="10">j2/3</tspan></text><circle cx="388.0" cy="94.0" r="10.0" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="406.0" y="99.0" text-anchor="start" fill="currentColor" style="font-size:13px;">j<tspan dy="-6" font-size="10">n</tspan><tspan dy="6">u[n], sin(πn/2)u[n] hit j</tspan></text><text x="406.0" y="117.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">→ double pole on |z| = 1 → unbounded</text><rect x="382.0" y="140.0" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="406.0" y="151.0" text-anchor="start" fill="currentColor" style="font-size:13px;">cos(2πn/3)u[n]: poles e<tspan dy="-6" font-size="10">±j2π/3</tspan></text><text x="406.0" y="169.0" text-anchor="start" fill="var(--accent2)" style="font-size:13px;">→ no match (120° ≠ 38.2°) → bounded</text><text x="406.0" y="205.0" text-anchor="start" fill="var(--muted)" style="font-size:13px;">δ[n] − ¾δ[n−1] cancels ¾ → bounded;</text><text x="406.0" y="223.0" text-anchor="start" fill="var(--muted)" style="font-size:13px;">(⅔)ⁿu[n] adds a pole inside → bounded</text></svg><figcaption><strong>FA2025 #8(b).</strong> The pole e<sup>j2/3</sup> sits at 2/3 rad ≈ 38.2°, not at the ±120° poles of cos(2πn/3)u[n], so that output stays bounded; jⁿu[n] and sin(πn/2)u[n] double the pole at j and grow like n.</figcaption></figure>

> [!trap]
> - Marginally stable = unstable on T/F.
> - $e^{j2/3}$ is not $e^{j2\pi/3}$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #8b]]).
> - A cosine resonates with a pole at **either** $e^{\pm j\omega_0}$; $e^{-j\pi n/4}u[n]$ alone does not match $e^{j\pi/4}$ ([[exams/midterm-1/past-exams/spring-2025|SP2025 #6]]).
> - A double pole **inside** the circle is harmless: $n(\frac23)^n u[n]$.

**Where it appears:** [[2-z-transform/11-bibo-stability-and-causality|L11]]; [[problems/unbounded-outputs-and-pole-matching]] (7/7 exams); [[homework/hw4|HW4]] #3(c)–(d); [[exams/midterm-1/true-false-bank|T/F bank]].

## Related
[[concepts/bibo-stability]] · [[concepts/region-of-convergence]] · [[concepts/poles-and-zeros]] · [[concepts/pole-zero-cancellation]] · [[concepts/complex-exponential]]

### Sources for this page
Lecture 11 notes §1.2–1.2.1, slides 14–18; FA2025 #8b, SP2025 #6, FA2023 #7, SP2021 #5 keys; HW4 #3 solutions.
