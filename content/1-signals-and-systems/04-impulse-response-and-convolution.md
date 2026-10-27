---
title: "Lecture 4 — Impulse response and convolution"
description: "h[n] = T(δ[n]); signals as sums of shifted impulses; LTI ⇔ convolution ⇔ described by h; properties; table, matrix and sum methods; the three cases."
tags: [lecture, midterm-1, systems, convolution]
lecture: 4
---

*Lecture 4 · Mon Aug 31, 2026 · notes + slides "Convolution and impulse response" · prev: [[1-signals-and-systems/03-system-properties|Lecture 3]] · next: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]]*

> [!abstract] In one breath
> - $h[n] = T(\delta[n])$; every signal is $\sum_k x[k]\,\delta[n-k]$.
> - LTI ⇔ $y = x * h = \sum_k x[k]\,h[n-k]$ ⇔ $h$ describes the system.
> - Causal ⇔ $h[n] = 0$ for $n < 0$; stable ⇔ $\sum\lvert h[n]\rvert < \infty$.

## What was covered

1. **§1 Impulse response** (eqs. 1–4) → [[concepts/impulse-response|Impulse response]] §1
2. **§1.1 Signals as linear combination of impulses** (eqs. 5–6, slide 4) → [[concepts/kronecker-delta|Kronecker delta]] §2
3. **§1.2 System response for LTI systems** (eq. 7, Fig. 1) → [[concepts/lti-system|LTI system]] §4
4. **§2 Convolution** (eq. 8) → [[concepts/convolution|Convolution]] §1
5. **§2.1 Properties of convolution and impulse response** (eqs. 9–17) → [[concepts/convolution|Convolution]] §2 · [[concepts/causality|Causality]] · [[concepts/bibo-stability|BIBO stability]]
6. **§2.2 Computing the convolution** (Table 1, eqs. 18–22) → [[concepts/convolution|Convolution]] §3–4
7. **§2.3 Cases for computing convolution** (eqs. 23–24) → [[concepts/convolution|Convolution]] §5

## Exercises from this lecture

- Slide 4, eq. 5: $\cos(\frac{\pi}{4}n)$, $\sin(\frac{\pi}{4}n)$ over one period as deltas → [[concepts/kronecker-delta|Kronecker delta]] §2
- Lecture exercise, $\sum\lvert h\rvert < \infty$ ⇒ BIBO stable → [[concepts/convolution|Convolution]] §2
- Table 1, $\{\underset{\uparrow}{3}, 1, 0, 3, 1, 1\} * \{2, \underset{\uparrow}{-1}, 1\}$ (table, matrix); slide 10 → [[concepts/convolution|Convolution]] §3
- §2.2.3, $u[n] * (-\frac34)^n u[n]$; slide 12, $(\frac12)^n u[n] * (-\frac34)^n u[n]$ → [[concepts/convolution|Convolution]] §4
- Eqs. 23–24, $\{\underset{\uparrow}{1}, 0, 2, 0, -3\} * \sin^3(\frac{\pi}{4}n)u[n]$; slides 14–16 (a)–(c) → [[concepts/convolution|Convolution]] §5

**Practice:** [[homework/hw2|HW2]] #3–#5 · [[problems/finite-length-convolution|finite]] · [[problems/infinite-length-convolution|infinite]] · [[problems/finding-h-from-input-output-pairs|finding h]] · [[demos/convolution-explorer|explorer]]

## Related

[[1-signals-and-systems/index|Unit 1]] · prev: [[1-signals-and-systems/03-system-properties|Lecture 3]] · next: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 4 notes (§1–2.3, Fig. 1, Table 1), annotated slides, Aug 31, 2026.
