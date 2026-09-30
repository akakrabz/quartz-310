---
title: "Complex exponential"
description: "x[n] = B aⁿ with complex a = r e^{jω}: Euler's identities, polar form and the principal angle, growth vs. decay set by r, and how every exponential becomes a pole of the z-transform."
tags: [concept, signals, complex-numbers, midterm-1]
aliases: ["complex exponential", "Euler's formula", "Euler's identities", "complex sinusoid", "exponential signal", "polar form"]
---

> [!key] The signal and the identities (Lecture 2)
> **Exponential signal:** $x[n]=B\,a^n$ with $B,a\in\mathbb{C}$. Writing $a=r\,e^{j\omega}$,
> $$
> x[n]=B\,r^n\,e^{j\omega n}:\qquad \lvert x[n]\rvert=\lvert B\rvert\,r^n\ \ (\text{decays if } r<1,\ \text{constant if } r=1,\ \text{grows if } r>1),
> $$
> while the angle advances $\omega$ radians per sample.
> **Euler:** $e^{j\theta}=\cos\theta+j\sin\theta$, $\quad\cos\theta=\dfrac{e^{j\theta}+e^{-j\theta}}{2}$, $\quad\sin\theta=\dfrac{e^{j\theta}-e^{-j\theta}}{2j}$.
> **Polar form:** $a+jb=Re^{j\theta}$ with $R=\sqrt{a^2+b^2}$ and $\theta$ in the correct quadrant; products multiply magnitudes and add angles. **Principal angle:** $Re^{j\theta}=Re^{j(\theta+2\pi k)}$, so $e^{j7\pi/3}=e^{j\pi/3}$ and frequencies $\omega$, $\omega+2\pi$ give identical sequences.

**Why it matters for the z-transform.** $a^nu[n]\leftrightarrow\dfrac{1}{1-a\,z^{-1}}$, ROC $\lvert z\rvert>\lvert a\rvert$: each exponential becomes **a pole at $z=a$**; its radius $r$ is the growth or decay rate and its angle is the frequency. A real sinusoid is two exponentials, so $\cos(\omega_0n)u[n]$ has two poles $e^{\pm j\omega_0}$. Exponentials are also the [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]].

> [!recipe] Convert to exponentials first
> Before transforming or pole-matching a sinusoid, rewrite it with Euler. [[0-midterm-1/past-exams/fall-2025|FA2025 #5c]]:
> $$
> \cos^2\!\big(\tfrac{\pi}{4}n\big)=\tfrac12+\tfrac12\cos\big(\tfrac{\pi}{2}n\big)=\tfrac12+\tfrac14e^{j\pi n/2}+\tfrac14e^{-j\pi n/2},
> $$
> so $\cos^2(\frac{\pi}{4}n)\,u[n]$ has poles at $1,\ j,\ -j$ and ROC $\lvert z\rvert>1$. Other conversions to know: $j^n=e^{j\pi n/2}$, $(-1)^n=e^{j\pi n}=\cos(\pi n)$, and ([[homework/hw1|HW1]] #4) $z^4=1\Rightarrow z=e^{j\pi k/2}=1,j,-1,-j$ while $z^4=-1=e^{j\pi}\Rightarrow z=e^{j(\pi/4+k\pi/2)}$.

> [!trap]
> - **Read the exponent literally.** In [[0-midterm-1/past-exams/fall-2025|FA2025 #8b]] the pole $e^{j2/3}$ sits at $2/3$ rad $\approx38.2^\circ$, not at $2\pi/3=120^\circ$; that is why $\cos(\frac{2\pi}{3}n)u[n]$ gives a *bounded* output there (key: False).
> - **Only $r$ sets the size**: $\lvert e^{j\theta}\rvert=1$ for every real $\theta$, but $\lvert0.8+0.8j\rvert=0.8\sqrt2\approx1.13>1$, so the gain $(0.8+0.8j)^n$ grows and $y=(0.8+0.8j)^nx[n]$ is unstable ([[0-midterm-1/past-exams/spring-2021|SP2021 #3]]).
> - **Sine needs the $2j$**: $\sin\theta=(e^{j\theta}-e^{-j\theta})/(2j)$; dropping the $j$ flips signs and phases.
> - **A real cosine carries both frequencies**: $\cos(\frac{\pi}{4}n)u[n]$ blows up a system with a unit-circle pole at $e^{j\pi/4}$ (True), while $e^{-j\pi n/4}u[n]$ alone does not (False) ([[0-midterm-1/past-exams/spring-2025|SP2025 #6]]).
> - **Mind the quadrant**: $\angle(-1-j)=-\frac{3\pi}{4}$, although $\tan^{-1}(\frac{-1}{-1})=\frac{\pi}{4}$.
> - $e^{j\omega n}$ **for all $n$** has no z-transform: its ROC is empty ([[0-midterm-1/past-exams/spring-2025|SP2025 #1c]] T).

**Where it appears.** [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] (complex numbers, sinusoids, exponentials), [[2-z-transform/06-the-z-transform|Lecture 6]] §1 (eigenfunctions), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1 (unit-circle poles); [[homework/hw1|HW1]] #4, [[homework/hw4|HW4]] #3d (poles $e^{-j\pi/4}$, $e^{j3\pi/4}$); [[0-toolkit/01-complex-numbers]]. Exams: [[0-midterm-1/past-exams/fall-2025|FA2025 #5a, #5c, #8b]], [[0-midterm-1/past-exams/spring-2025|SP2025 #1c, #6]], [[0-midterm-1/past-exams/spring-2021|SP2021 #3, #5]]; families [[problems/z-transform-with-roc]] and [[problems/unbounded-outputs-and-pole-matching]].

**Related.** [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/discrete-time-signal|discrete-time signal]]

### Sources for this page
Lecture 2 §1.1–1.4 (Eqs. 1–20) and §2 (Eqs. 23–24); Lecture 6 §1; HW1 #4; FA2025 #5c and #8b, SP2025 #6 and #1c, SP2021 #3 (annotated "1.13 e^{jπ/4}"). Checked in `verify/concepts/verify_glossary_time.py`, `verify_signals.py`, `verify_stability.py`.
