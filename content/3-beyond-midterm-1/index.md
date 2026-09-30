---
title: "Beyond Midterm 1 · Lectures 12–14"
description: "Outline of what comes after the Midterm 1 material — Lecture 12 (convolution as template matching, not tested), Lecture 13 (Fourier analysis and the DTFT), Lecture 14 (DTFT properties) and HW5 — with pointers to the Midterm 1 ideas each one builds on."
tags: [lecture]
---

*Lectures 12–14 · September 21–25, 2026 · outline · prev: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · **none of this is on Midterm 1***

> [!warning] Not on Midterm 1
> Midterm 1 covers Lectures 1–11 and HW1–HW4. Lecture 12 is not tested at all ("this lecture will not be tested on homeworks or exams"), and the DTFT of Lectures 13–14 and HW5 belongs to the next exam. If your exam is today, go to the [[0-midterm-1/index|survival guide]] and the [[0-midterm-1/cheat-sheet|cheat sheet]] instead.

These three lectures turn the corner from the time domain and the z-domain to the **frequency domain**. Each one leans on something you already know from Midterm 1, so the short sections below say what is new and where its foundations are on this site.

## Lecture 12 — Convolution as template matching (Mon Sep 21) · not tested

The convolution sum $y[n] = \sum_k x[k]\,h[n-k]$ is, for each $n$, an inner product between the input and a flipped, shifted copy of $h$. Choose $h$ to be a time-reversed **template** $t$, $h[n] = t[-n]$ — a *matched filter* — and $y[n] = \sum_k x[k]\,t[k-n]$ becomes large exactly where the input locally looks like the template, so the peaks of the output locate the pattern. The same sliding sum works in two dimensions, $y[m,n] = \sum_k\sum_l x[k,l]\,h[m-k,\,n-l]$, where a small kernel moves over an image to find a pattern (or to blur or detect edges). Builds on the flip-and-slide picture of [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] and [[concepts/convolution|convolution]]; try it in the [[demos/convolution-explorer|convolution explorer]].

## Lecture 13 — Fourier analysis (Wed Sep 23)

Periodic signals first: $x(t+T) = x(t)$ in continuous time, $x[n+N] = x[n]$ with an **integer** $N$ in discrete time — so a discrete-time sinusoid $\cos(\omega_0 n)$ is periodic only when $\omega_0/2\pi$ is rational, and $\omega_0$ and $\omega_0+2\pi$ give identical samples. The continuous-time Fourier series writes a periodic $x(t)$ as a sum of harmonics $e^{jk\Omega_0t}$; letting the period grow without bound turns the line spectrum into the continuous-time Fourier transform (conceptually). The discrete-time counterparts are the DTFS for $N$-periodic sequences (harmonics $e^{j2\pi kn/N}$ — the roots of unity again) and, for aperiodic sequences, the **DTFT**

$$
X_d(\omega) = \sum_{n=-\infty}^{\infty} x[n]\,e^{-j\omega n},
\qquad
x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi} X_d(\omega)\,e^{j\omega n}\,d\omega ,
$$

which is $2\pi$-periodic in $\omega$. It certainly exists (the sum converges for every $\omega$) when $x$ is absolutely summable; signals such as $e^{j\omega_0 n}$ or $\cos(\omega_0 n)$ that are not get transforms with impulses, $e^{j\omega_0 n} \leftrightarrow 2\pi\delta(\omega-\omega_0)$ on each period. Builds on complex exponentials and roots of unity ([[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]], [[concepts/complex-exponential|complex exponential]]), [[0-toolkit/02-geometric-series|geometric series]] (every DTFT of a finite or exponential sequence is one), and the eigenfunction property of LTI systems ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]).

## Lecture 14 — DTFT properties (Fri Sep 25)

The bridge from Midterm 1 is one line: **when the ROC of $X(z)$ contains the unit circle, $X_d(\omega) = X(z)\big|_{z = e^{j\omega}}$.** For an LTI system that is the frequency response $H_d(\omega) = H(e^{j\omega})$, and it exists as an ordinary function exactly when the system is BIBO stable — ROC contains $\lvert z\rvert = 1$ ⇔ stable ⇔ frequency response exists. The eigenfunction view then says $e^{j\omega_0n} \mapsto H_d(\omega_0)\,e^{j\omega_0n}$ and, for real $h$, $\cos(\omega_0n+\phi) \mapsto \lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\phi+\angle H_d(\omega_0)\big)$. The properties mirror the z-transform table evaluated on the unit circle: linearity; $x[n-n_0] \leftrightarrow e^{-j\omega n_0}X_d(\omega)$; $e^{j\omega_0n}x[n] \leftrightarrow X_d(\omega-\omega_0)$; convolution ↔ product; multiplication (windowing) ↔ periodic convolution divided by $2\pi$; for real $x$, $X_d(-\omega) = X_d^*(\omega)$ (magnitude even, phase odd); Parseval, $\sum_n\lvert x[n]\rvert^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$. Two past T/F statements test exactly this (DTFT questions, not on Midterm 1): SP2023 #1(d) "$X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$ **always**" is False — the ROC must contain the unit circle; SP2023 #1(e) "$\lvert X_d(\omega)\rvert$ is even for real $x$" is True. Builds on [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]], [[concepts/region-of-convergence|region of convergence]] and [[concepts/z-transform-properties|z-transform properties]].

## HW5 — the DTFT (due Sunday, October 4)

Two problems. (1) DTFTs from the definition: $\{\underset{\uparrow}{1},\ 0,\ 0,\ 0,\ -1\}$, $u[n]-u[n-4]$ (a finite geometric sum), $\cos(\tfrac{\pi}{3}n+\tfrac{\pi}{4})$ (via Euler and the impulse pair) and $\alpha^n e^{j\omega_0n}u[n]$ with $\lvert\alpha\rvert<1$ (a geometric series — or the z-transform pair $\frac{1}{1-\alpha e^{j\omega_0}z^{-1}}$ evaluated on the unit circle, since its ROC $\lvert z\rvert>\lvert\alpha\rvert$ contains it). (2) Reading a DTFT without computing it: $X_d(0) = \sum_n x[n]$, $X_d(\pi) = \sum_n(-1)^nx[n]$, $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega = 2\pi\,x[0]$, and Parseval for $\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$. The first two are the same $\sum y = \sum x\sum h$ checks the [[0-midterm-1/cheat-sheet|cheat sheet]] recommends for convolutions — $X(z)$ at $z = \pm1$.

## Related

[[0-midterm-1/index|Midterm 1 survival guide]] · [[2-z-transform/index|Unit 2 · The z-transform and LTI systems]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[concepts/bibo-stability|BIBO stability]] · [[supplements/course-summary|course summary]] (DTFT section) · [[supplements/transform-tables|transform tables]]

### Sources for this page

Course calendar (Lectures 12–14, Sep 21–25, 2026) and the lecture topics as announced; HW5 (Fall 2026); the ECE 310 course summary (DTFT definition, relation to the z-transform, properties, sinusoidal response); SP2023 Midterm 1 key, #1(d)–(e).
