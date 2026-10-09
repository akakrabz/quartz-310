---
title: "Past Midterm 1 exams"
description: "All seven past ECE 310 Midterm 1 exams with typed problems and folded solutions: which exam to take first, the problem-family × exam map, the DTFT items that belong to Unit 3, and every answer-key erratum."
tags: [exam, midterm-1]
---

*Seven past Midterm 1 exams, newest first · every problem typed out with a folded solution, the traps that cost points, and the key's errors · every answer checked in Python*

> [!abstract] In one breath
> Midterm 1 is 2 hours, about 8 problems, 100 points, one handwritten two-sided sheet, no calculator, closed-form answers. Seven problem families appear on **every** past exam: True/False, the property table, finite convolution, finding $h$ from input–output data, inverse z / PFE / ROCs, LCCDE ↔ $H(z)$, and bounded/unbounded outputs by pole matching. Do **Fall 2025** and **Spring 2025** under exam conditions; use the rest as a problem bank by family.

## The seven exams

| exam | date | instructors | problems / points | notes |
|---|---|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|Fall 2025]] | Wed Oct 1, 2025, 7–9 pm | Do, Snyder | 8 / 100 | same instructor as this term; handwritten key (1 erratum) |
| [[exams/midterm-1/past-exams/spring-2025\|Spring 2025]] | Wed Feb 26, 2025, 7–9 pm | Liang, Snyder | 8 / 100 | T/F scored +2/−1/0; key's boxed #4(a) is wrong |
| [[exams/midterm-1/past-exams/fall-2024\|Fall 2024]] | Wed Oct 2, 2024, 7–9 pm | Do, Shomorony, Snyder | 8 / 100 | typed key |
| [[exams/midterm-1/past-exams/fall-2023\|Fall 2023]] | Wed Sep 27, 2023, 7–9 pm | Do, Snyder, Moustakides | 8 / 100 | typed key, no errors found |
| [[exams/midterm-1/past-exams/spring-2023\|Spring 2023]] | Wed Mar 1, 2023, 7–9 pm | Liang, Moon, Snyder | 9 / 100 | T/F +2/−1/0; #1(d–e), #8, #9 are DTFT (skip) |
| [[exams/midterm-1/past-exams/spring-2021\|Spring 2021]] | Thu Mar 11, 2021, 7:00–8:50 pm | Moon, Katselis, Shomorony | 7 / 100 | online exam; big property table (24 pts) |
| [[exams/midterm-1/past-exams/fall-2019\|Fall 2019]] | Thu Oct 3, 2019, 7:00–8:30 pm | Kamalabadi, Katselis, Liang | 10 / 100 | 90 min; 10 T/F items; #8, #9 are DTFT (skip) |

Older exams say **LSI** (linear shift-invariant) where the current course says **LTI** — same thing.

## How to use these exams

> [!tip] A plan for the last days before the exam
> 1. **Fall 2025, timed.** 2 hours, closed book, only your handwritten sheet, no calculator. Then grade yourself with the folded solutions and write down, per lost point, its [[problems/index|problem family]].
> 2. **Fix the weak families.** Read the family page (recipe + traps) for whatever cost you points; redo that problem cold.
> 3. **Spring 2025, timed** — same rules. It adds a parameter-for-stability problem and an "all possible outputs" problem that FA2025 lacks.
> 4. **Flashcards, 10 minutes each:** the [[exams/midterm-1/true-false-bank|T/F bank]] and the [[exams/midterm-1/system-property-bank|system-property bank]]. Say the *reason* out loud, not just the letter — the reasons repeat across years.
> 5. **Older exams as a bank, not as full runs:** pick problems from the families below where you are weakest. Skip the DTFT items (list below).
> 6. **Last hour:** no new problems. Re-read the [[exams/midterm-1/cheat-sheet|cheat sheet]], check your sheet has the z-transform pairs *with ROCs*, and eat something.

> [!trap] The pole-matching traps (worth 10 points almost every term)
> - **Read the pole digit by digit.** FA2025 #8(b): the system pole is $e^{j2/3}$ (angle $\tfrac23$ rad), the input is $\cos(\tfrac{2\pi}{3}n)u[n]$ (angle $\tfrac{2\pi}{3}$) — they do **not** match, so the output is bounded.
> - **A conjugate is a different pole.** SP2025 #6: only inputs containing $e^{+j\pi n/4}$ resonate with a pole at $e^{j\pi/4}$.
> - **Cancellation works both ways.** An input *zero* on an unstable system pole makes the output bounded (FA2025 #8(a) ii, v; FA2024 #7c); an input *pole* on a unit-circle system pole makes it unbounded.
> - **Check the question's wording:** "produces a bounded output" and "produces an unbounded output" flip every letter.
> - Recipe: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]].

> [!note] DTFT items — not on the Fall 2026 Midterm 1; use them with Unit 3
> Spring 2023 #1(d), #1(e), #8, #9 (12 points) and Fall 2019 #8, #9 (8 points) are DTFT problems: skip them when you practise for Midterm 1, and use them as self-tests after [[3-fourier-analysis/14-dtft-properties|Lecture 14]]. The four most recent exams (FA2025, SP2025, FA2024, FA2023) and Spring 2021 contain no DTFT at all.

## Problem families × exams

Every problem of every exam, sorted into the [[problems/index|exam problem families]] (a cell is the problem number on that exam):

| family | [[exams/midterm-1/past-exams/fall-2025\|FA25]] | [[exams/midterm-1/past-exams/spring-2025\|SP25]] | [[exams/midterm-1/past-exams/fall-2024\|FA24]] | [[exams/midterm-1/past-exams/fall-2023\|FA23]] | [[exams/midterm-1/past-exams/spring-2023\|SP23]] | [[exams/midterm-1/past-exams/spring-2021\|SP21]] | [[exams/midterm-1/past-exams/fall-2019\|FA19]] | count |
|---|---|---|---|---|---|---|---|---|
| [[exams/midterm-1/true-false-bank\|True/False]] | #1 | #1 | #1 | #1 | #1 | #1 | #1 | 7/7 |
| [[problems/classifying-system-properties\|System-property table]] ([[exams/midterm-1/system-property-bank\|bank]]) | #2 | #2 | #2 | #2 | #2 | #3 | #2 | 7/7 |
| [[problems/finite-length-convolution\|Finite-length convolution]] | #3a | #4a | #4a | #3a | #3a | #2 | #4 | 7/7 |
| [[problems/infinite-length-convolution\|Infinite / mixed convolution]] | #3b | #4b | #4b | #3b | #3b, #3c | — | — | 5/7 |
| [[problems/finding-h-from-input-output-pairs\|Finding h (or H) from input–output data]] | #4 | #3 | #3, #6 | #4 | #4, #6 | #7 | #3 | 7/7 |
| [[problems/z-transform-with-roc\|z-transform with ROC]] | #5 | #5 | #5 | #5 | — | #4 | #5 | 6/7 |
| [[problems/all-possible-rocs\|Inverse z / PFE / all possible ROCs]] | #7 | #8 | #7 | #6 | #6 | #5, #7 | #6, #7 | 7/7 |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z) ↔ response]] | #6 | #8 | #6 | #6, #7 | #5, #6 | #6 | #10 | 7/7 |
| [[problems/unbounded-outputs-and-pole-matching\|Unbounded outputs, pole matching, cancellation]] | #8 | #6 | #7 | #7 | #7 | #5 | #10 | 7/7 |
| [[problems/parameters-for-stability\|Parameters for stability]] | — | #7 | #8 | #8 | — | — | — | 3/7 |
| [[problems/two-sided-systems-as-recursions\|Two-sided systems as recursions]] | #7b | — | #8a | — | — | — | — | 2/7 |

Recent Fall exams (Snyder) spend roughly: T/F 12 points · property table 12 · convolution 8–10 · a short LTI problem 5–10 · z-transforms 9–15 · LCCDE / transfer function 15–20 · PFE / ROC / stability 15–20 · pole matching or a stability parameter 10.

## Answer-key errata at a glance

The official keys are mostly right; where they are not, the exam page gives the correct answer in a warning box. Full list with the lecture-note typos: [[0-toolkit/05-errata|errata]].

- **Fall 2025** #5(a): stray $n$ in the handwritten denominator — correct $X(z) = \dfrac{e^{-j4\pi/3}z^4}{1 - e^{j\pi/3}z^{-1}}$, $1 < \lvert z\rvert < \infty$. (#1(d) is not an erratum: "left-sided" means an infinite-length sequence extending to $-\infty$, so True is right.)
- **Spring 2025** #4(a): the boxed $\{2,-5,\underset{\uparrow}{6},0,-5,10,-4,3\}$ is wrong; correct $\{2,-5,\underset{\uparrow}{5},0,-5,12,-4,3\}$ (the key's own matrix column).
- **Fall 2024** #8(a): "$\lvert a\rvert > 1$" means $\lvert\alpha\rvert > 1$. #4(b): the boxed line is labelled $x[n]$ but is $y[n]$.
- **Fall 2023**: none found.
- **Spring 2023** #6(c): the difference equation repeats $y[n-1]$; correct $y[n] = \tfrac34 y[n-1] - \tfrac18 y[n-2] + x[n] - 2x[n-1]$.
- **Spring 2021** #6: correct $h[0] = -1$, $h[3] = -1$ (the key has $1$ and $3$).
- **Fall 2019** #5(b): $e^{-91}$ should be $e^{-81}$, and the result is $X(z)$ (ROC $z \ne 0$), not $X_d(\omega)$.

## Related

- [[exams/midterm-1/index|Midterm 1 review guide]] · [[exams/midterm-1/cheat-sheet|cheat sheet]] · [[demos/practice-drills|practice drills]]
- [[problems/index|Problem families]] · [[homework/index|homework]] · [[exams/midterm-2/past-exams/index|past Midterm 2 exams]] · [[exams/index|all exams]]

### Sources for this page

- The seven past Midterm 1 exams with their solution keys (`old-exams/`: Fall 2025, Spring 2025, Fall 2024, Fall 2023, Spring 2023, Spring 2021, Fall 2019), headers read for dates, instructors and point values.
- The problem-family classification shared across this site; the answer checks behind every exam page (numpy/scipy verification scripts, one per exam).
