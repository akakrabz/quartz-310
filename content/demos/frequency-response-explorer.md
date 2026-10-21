---
title: "Demo — Frequency-response explorer"
description: "Type FIR taps or a difference equation, pick a preset, or drag poles and zeros; see |H_d(ω)|, principal or unwrapped phase, group delay, and the output for one cosine."
tags: [demo, dtft, frequency-response, group-delay]
---

*Demo · pairs with [[3-fourier-analysis/14-dtft-properties|Lecture 14]], [[3-fourier-analysis/15-frequency-response|Lecture 15]] and [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] · concepts: [[concepts/frequency-response]], [[concepts/magnitude-and-phase-response]], [[concepts/group-delay]], [[concepts/eigenfunctions-of-lti-systems]]*

<div class="ece-demo">
<iframe src="/static/demos/frequency-response/" title="Frequency-response explorer — interactive demo" loading="lazy" style="height:1600px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/frequency-response/).

**Input.** FIR: taps in **b**, **a** = `1`, first-tap index in **n₀** ($\{\underset{\uparrow}{3}, 2, 1\}$: b = `3, 2, 1`, n₀ = `0`). Recursive: Lecture 9 coefficients (the `b, a` of `lfilter`). Or type roots in **poles & zeros** mode (conjugates added). Plotted:

$$
H_d(\omega) = e^{-j\omega n_0}\,\frac{\sum_k b_k e^{-j\omega k}}{\sum_k a_k e^{-j\omega k}}
$$

## What to try

1. **Lecture 16, Exercise 1:** $h = \delta[n] - \delta[n-2]$, $H_d = 2j\,e^{-j\omega}\sin\omega$. Magnitude $2\lvert\sin\omega\rvert$; $\pi$ jump at $\omega=0$; group delay $1$. At ω₀ = π/2 the output is $2\cos(\tfrac{\pi}{2}n)$: phase delay $0$, group delay $1$.
2. **Exercise 2, $\{3, 2, 1\}$:** no jumps, but group delay falls from $\tfrac23$ at $0$ to about $-1.06$ near $2.2$. At ω₀ = π/3, $\lvert H_d\rvert = \sqrt{19}$.
3. **$\{1, 0, 1\}$, then n₀ = `-1`:** magnitude unchanged, phase collapses to $0$ or $\pm\pi$, group delay $1\to0$ (time-shift property).
4. **Pure delay $e^{-j2\omega}$:** phase wraps at $\pm\tfrac{\pi}{2}$; *unwrap* gives slope $-2$. At ω₀ = 3π/4 the principal phase reads $\tfrac{\pi}{2}$, yet the output is the input two samples later.
5. **3-point average:** zero at $\tfrac{2\pi}{3}$ blocks that cosine. Centred version at ω₀ = 5π/6: $H_d \approx -0.244$, an upside-down copy.
6. **Pole at $0.8$:** peak $5$ ($13.98$ dB) at $0$, $\tfrac59$ at $\pi$; move it to $0.95$: peak $20$.
7. **Notch:** zeros at $e^{\pm j\pi/3}$ block $\tfrac{\pi}{3}$; *sharp notch* adds poles at $0.9e^{\pm j\pi/3}$ for a nearly flat response elsewhere.
8. **Past exams:** SP2021 #3 ($6\lvert\sin 4\omega\rvert$, delay $3$), SP2023 #5 ($2\lvert\cos 3\omega\rvert$), FA2024 #3 ($1 + 2\cos 2\omega$: $3$, $-1$, $3$ at $0$, $\tfrac{\pi}{2}$, $\pi$).

> [!trap]
> - Real systems only; complex $h[n]$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4) is not handled.
> - *Unwrap* removes $2\pi$ wraps, not the $\pi$ jumps at unit-circle zeros.
> - A typed pole on or outside the circle: no causal stable system; curves show $H(z)$ on $\lvert z\rvert=1$.

> [!exam]
> Sketch $|H_d|$ and $\angle H_d$ of a short FIR, or push sinusoids through a system. Check your sketch here afterwards; axis labels earn the points.
> - [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2 #5]] · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2 #3]] (b = `1, 0, 0, 2, 0, 0, 1`) · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2 #3–4]] · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2 #2–3]]

## Related
[[concepts/frequency-response]] · [[concepts/magnitude-and-phase-response]] · [[concepts/group-delay]] · [[problems/magnitude-phase-and-group-delay]] · [[problems/lti-response-to-sinusoids]] · [[demos/practice-drills|Practice drills]] · [[demos/index|all demos]]

### Sources for this page
Lecture 14–16 notes and slides (Exercises 1–2, Examples 1–3); Lecture 3 slides, Lecture 5 notes (moving average); Midterm 2 keys SP2021, SP2023, FA2023, FA2024, SP2025.
