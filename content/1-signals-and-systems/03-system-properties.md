---
title: "Lecture 3 — Discrete-time systems: linearity, time-invariance, causality, stability"
description: "What a discrete-time system is, and how to prove or disprove the four properties of every Midterm 1 property table: linearity, time-invariance, causality, BIBO stability."
tags: [lecture, midterm-1, systems]
lecture: 3
---

*Lecture 3 · Fri Aug 28, 2026 · notes + slides "Discrete-time systems" · prev: [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] · next: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]*

> [!abstract] In one breath
> - A system is any rule $T$ with $y[n] = T(x[n])$.
> - Four yes/no properties: linear, time-invariant, causal, BIBO stable.
> - Prove for *every* input; disprove with *one* counterexample.

## What was covered

1. **§1 Discrete-time systems** (eqs. 1–4; "not just filters") → [[concepts/lti-system|LTI system]] §1
2. **§2 The four properties** (overview; the property-table row) → [[concepts/lti-system|LTI system]] §2–3
3. **§2.1 Linearity** (eqs. 5–7, Exercises 1–2) → [[concepts/linearity|Linearity]]
4. **§2.2 Time-invariance** (eqs. 8–10, Exercises 3–5) → [[concepts/time-invariance|Time-invariance]]
5. **§2.3 Causality** (Exercise 6) → [[concepts/causality|Causality]]
6. **§2.4 Stability** (eq. 11, Exercise 7) → [[concepts/bibo-stability|BIBO stability]] §1

## Exercises from this lecture

- Exercises 1–2, slide 5 and slide 6 extra practice, linear? → [[concepts/linearity|Linearity]] §2
- Exercises 3–5, slide 8 ($y[n] = x[2n]$ on $\{\underset{\uparrow}{2}, 4, 6, 1, 3, 5\}$, $n_0 = 1$) and slide 9, time-invariant? → [[concepts/time-invariance|Time-invariance]] §2
- Exercise 6, slides 10–11, causal? → [[concepts/causality|Causality]] §2
- Exercise 7, slides 12–13, BIBO stable? → [[concepts/bibo-stability|BIBO stability]] §1

**Practice:** [[homework/hw1|HW1]] #5–#6 · [[homework/hw2|HW2]] #1–#2 · [[problems/classifying-system-properties|classifying system properties]] · [[exams/midterm-1/system-property-bank|system-property bank]] · [[demos/practice-drills|drills]]

## Related

[[1-signals-and-systems/index|Unit 1]] · prev: [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] · next: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 3 notes (§1, §2.1–2.4, Exercises 1–7) and annotated slides, Aug 28, 2026.
