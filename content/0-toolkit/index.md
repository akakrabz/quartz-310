---
title: "Toolkit"
description: "The mathematics ECE 310 assumes — complex numbers, geometric series, index bookkeeping for sketching signals, factoring and long division — plus the list of errata in the course materials."
tags: [toolkit]
---

Reference pages, not lectures. Come here when a lecture says "recall…", when a PFE refuses to come out, or when you need to know whether the answer key or you made the sign error. Each page is short, has small worked examples checked in Python, and links to the lectures and exam problems that use it.

- [[0-toolkit/01-complex-numbers|Complex numbers]] — rectangular ↔ polar, the quadrant rule, $e^{j\theta}$ on the unit circle, roots of $z^N = a$ (HW1 #4), turning conjugate PFE terms into $\cos$/$\sin$, and $\cos^2$ (FA2025 #5c).
- [[0-toolkit/02-geometric-series|Geometric series]] — finite, infinite, shifted, left-sided and two-sided sums and $\sum k\,a^k$; how each convergence condition *is* a z-transform ROC.
- [[0-toolkit/03-sketching-and-transforming-signals|Sketching and transforming signals]] — the $n=0$ arrow, shift / reversal / downsampling, "substitute, don't guess" for $x[-n+3]$ and $x[2n+1]$ (HW1 #2), even and odd parts, $\delta$- and $u$-forms (HW1 #3).
- [[0-toolkit/04-factoring-and-long-division|Factoring and long division]] — $1+az^{-1}+bz^{-2} = (1-p_1z^{-1})(1-p_2z^{-1})$, poles and zeros at $0$ and $\infty$, the cover-up rule, and Lecture 10's long division for improper $H(z)$, with `residuez`.
- [[0-toolkit/05-errata|Errata in the course materials]] — every slip found in the past exam keys, lecture notes, homework solutions and the official transform table, with the correction and why; check your cheat sheet against it.

> [!tip] Where these show up on Midterm 1
> Complex numbers and geometric series are inside every [[problems/z-transform-with-roc|z-transform]] and [[problems/unbounded-outputs-and-pole-matching|pole-matching]] problem; index bookkeeping decides every [[problems/finite-length-convolution|convolution]] and [[problems/classifying-system-properties|system-property]] answer; factoring and long division are the first half of every [[problems/lccde-to-transfer-function-and-response|LCCDE]] and [[problems/all-possible-rocs|PFE/ROC]] problem. The reference sheets the course itself provides are collected under [[supplements/index|Supplements]].

### Sources for this page

Summaries of the five toolkit pages; see each page's own sources.
