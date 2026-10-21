---
title: "Past Midterm 1 exams"
description: "Seven past ECE 310 Midterm 1 exams with folded solutions: which to take first, the family × exam map, DTFT items belonging to Unit 3, and answer-key errata."
tags: [exam, midterm-1]
---

*Seven past Midterm 1 exams, newest first · folded solutions · [[exams/midterm-1/index|review guide]]*

> [!abstract] In one breath
> - 2 hours, ~8 problems, 100 points, one handwritten two-sided sheet, no calculator.
> - On every exam: T/F, property table, finite convolution, finding $h$, inverse z / ROCs, LCCDE ↔ $H(z)$, pole matching.
> - Take FA2025 and SP2025 timed; use the rest as a bank by family.

## The seven exams

| exam | date | instructors | probs / pts | notes |
|---|---|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|Fall 2025]] | Oct 1, 2025 | Do, Snyder | 8 / 100 | handwritten key (1 erratum) |
| [[exams/midterm-1/past-exams/spring-2025\|Spring 2025]] | Feb 26, 2025 | Liang, Snyder | 8 / 100 | T/F +2/−1/0; key's #4(a) wrong |
| [[exams/midterm-1/past-exams/fall-2024\|Fall 2024]] | Oct 2, 2024 | Do, Shomorony, Snyder | 8 / 100 | typed key |
| [[exams/midterm-1/past-exams/fall-2023\|Fall 2023]] | Sep 27, 2023 | Do, Snyder, Moustakides | 8 / 100 | no key errors |
| [[exams/midterm-1/past-exams/spring-2023\|Spring 2023]] | Mar 1, 2023 | Liang, Moon, Snyder | 9 / 100 | T/F +2/−1/0; DTFT items |
| [[exams/midterm-1/past-exams/spring-2021\|Spring 2021]] | Mar 11, 2021 | Moon, Katselis, Shomorony | 7 / 100 | online; 24-pt property table |
| [[exams/midterm-1/past-exams/fall-2019\|Fall 2019]] | Oct 3, 2019 | Kamalabadi, Katselis, Liang | 10 / 100 | 90 min; DTFT items |

LSI (older exams) = LTI.

> [!tip] Plan
> 1. FA2025 timed; grade; tag each lost point with its [[problems/index|family]].
> 2. Repair: family recipe and traps, redo cold.
> 3. SP2025 timed (adds a stability parameter and "all possible outputs").
> 4. [[exams/midterm-1/true-false-bank|T/F bank]] and [[exams/midterm-1/system-property-bank|property bank]]: say the reason.
> 5. Older exams by family.

> [!trap] Pole matching (10 points most terms)
> - FA2025 #8(b): pole $e^{j2/3}$ vs input angle $\tfrac{2\pi}{3}$: no match, bounded.
> - SP2025 #6: only $e^{+j\pi n/4}$ resonates with a pole at $e^{j\pi/4}$.
> - Input zero on an unstable pole ⇒ bounded (FA2025 #8(a) ii, v; FA2024 #7c); input pole on a unit-circle pole ⇒ unbounded.
> - "Bounded" vs "unbounded" in the question flips every answer.
> - Recipe: [[problems/unbounded-outputs-and-pole-matching|pole matching]].

> [!note] DTFT items (Unit 3, not Midterm 1)
> SP2023 #1(d), #1(e), #8, #9 and FA2019 #8, #9: self-tests after [[3-fourier-analysis/14-dtft-properties|Lecture 14]].

## Problem families × exams

| family | [[exams/midterm-1/past-exams/fall-2025\|FA25]] | [[exams/midterm-1/past-exams/spring-2025\|SP25]] | [[exams/midterm-1/past-exams/fall-2024\|FA24]] | [[exams/midterm-1/past-exams/fall-2023\|FA23]] | [[exams/midterm-1/past-exams/spring-2023\|SP23]] | [[exams/midterm-1/past-exams/spring-2021\|SP21]] | [[exams/midterm-1/past-exams/fall-2019\|FA19]] | count |
|---|---|---|---|---|---|---|---|---|
| [[exams/midterm-1/true-false-bank\|True/False]] | #1 | #1 | #1 | #1 | #1 | #1 | #1 | 7/7 |
| [[problems/classifying-system-properties\|Property table]] | #2 | #2 | #2 | #2 | #2 | #3 | #2 | 7/7 |
| [[problems/finite-length-convolution\|Finite convolution]] | #3a | #4a | #4a | #3a | #3a | #2 | #4 | 7/7 |
| [[problems/infinite-length-convolution\|Infinite convolution]] | #3b | #4b | #4b | #3b | #3b, #3c | — | — | 5/7 |
| [[problems/finding-h-from-input-output-pairs\|Finding h]] | #4 | #3 | #3, #6 | #4 | #4, #6 | #7 | #3 | 7/7 |
| [[problems/z-transform-with-roc\|z-transform with ROC]] | #5 | #5 | #5 | #5 | — | #4 | #5 | 6/7 |
| [[problems/all-possible-rocs\|Inverse z / all ROCs]] | #7 | #8 | #7 | #6 | #6 | #5, #7 | #6, #7 | 7/7 |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z)]] | #6 | #8 | #6 | #6, #7 | #5, #6 | #6 | #10 | 7/7 |
| [[problems/unbounded-outputs-and-pole-matching\|Pole matching]] | #8 | #6 | #7 | #7 | #7 | #5 | #10 | 7/7 |
| [[problems/parameters-for-stability\|Parameters for stability]] | — | #7 | #8 | #8 | — | — | — | 3/7 |
| [[problems/two-sided-systems-as-recursions\|Two-sided recursions]] | #7b | — | #8a | — | — | — | — | 2/7 |

## Answer-key errata

Full list: [[0-toolkit/05-errata|errata]].
- **FA2025** #5(a): $X(z) = \dfrac{e^{-j4\pi/3}z^4}{1 - e^{j\pi/3}z^{-1}}$, $1 < \lvert z\rvert < \infty$ (stray $n$ in key). #1(d) True is right.
- **SP2025** #4(a): $\{2,-5,\underset{\uparrow}{5},0,-5,12,-4,3\}$, not the boxed $\{2,-5,\underset{\uparrow}{6},0,-5,10,-4,3\}$.
- **FA2024** #8(a): "$\lvert a\rvert > 1$" means $\lvert\alpha\rvert > 1$. #4(b): boxed line is $y[n]$.
- **SP2023** #6(c): $y[n] = \tfrac34 y[n-1] - \tfrac18 y[n-2] + x[n] - 2x[n-1]$.
- **SP2021** #6: $h[0] = -1$, $h[3] = -1$ (key: $1$, $3$).
- **FA2019** #5(b): $e^{-81}$, not $e^{-91}$; result is $X(z)$ (ROC $z \ne 0$).

## Related
[[exams/midterm-1/index|review guide]] · [[exams/midterm-1/cheat-sheet|cheat sheet]] · [[demos/practice-drills|drills]] · [[homework/index|homework]] · [[exams/midterm-2/past-exams/index|past Midterm 2 exams]] · [[exams/index|all exams]]

### Sources for this page
The seven past Midterm 1 exams with keys (FA2019–FA2025): headers for dates, instructors, points.
