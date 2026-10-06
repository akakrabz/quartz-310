---
title: "Parameters for stability"
description: "Recipe for \"for what value(s) of α is the system BIBO stable?\": find the bad poles for the stated causality, then either cancel them with a zero that depends on α or put the α-dependent pole on the right side of the unit circle. Causal, anti-causal and two-sided cases, with three fresh practice problems."
tags: [problem-family, problem, midterm-1, stability, lccde, roc, z-transform]
family_frequency: "3 of 7 exams"
typical_points: "6–10"
lectures: [9, 11]
---

*Problem family · on 3 of 7 past midterms (SP2025, FA2024, FA2023; not FA2025) · typically 6–10 pts · uses [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · concepts: [[concepts/bibo-stability]], [[concepts/pole-zero-cancellation]], [[concepts/region-of-convergence]], [[concepts/lccde]]*

> [!abstract] In one breath
> The parameter almost always sits in the **numerator**, so it moves a **zero**, and a zero can make a system stable in only one way: by landing exactly on the bad pole and cancelling it. So: find the poles, decide which are bad for the stated causality (causal: $\lvert p\rvert\ge1$; left-sided: $\lvert p\rvert\le1$; two-sided: none, if the unit circle lies between them), and solve "numerator $=0$ at the bad pole" for the parameter. If the parameter is itself a pole, the condition is on its magnitude instead.

## What it looks like on the exam

An LCCDE with one unknown coefficient $\alpha$ (or $\beta$), real or complex, plus a sentence fixing the causality: "causal", "non-causal", "non-causal and two-sided". The question is "for what value(s) is it BIBO stable?", either open-ended or as a True/False list of candidate values. It appeared on FA2023, FA2024 and SP2025 (not on FA2025), worth 6–10 points.

| where | system | causality | answer |
|---|---|---|---|
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #7]] (6 pts) | $y[n]=-\tfrac32y[n-1]+y[n-2]+x[n]-\alpha^2x[n-2]$, $\alpha\in\mathbb{C}$ | causal | poles $-2,\ \tfrac12$; zeros $\pm\alpha$; stable iff $\alpha=\pm2$: $2$ T, $-2$ T, $j2$ F, $-j2$ F, $\tfrac{\sqrt2}{2}$ F, $\tfrac12$ F |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #8a]] | $y[n]+\alpha y[n-1]=x[n]+3x[n-1]$, $\alpha$ real | non-causal | $H=\dfrac{1+3z^{-1}}{1+\alpha z^{-1}}$, ROC $\lvert z\rvert<\lvert\alpha\rvert$: stable iff $\lvert\alpha\rvert>1$ (the key writes $\lvert a\rvert$) |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #8b]] | $y[n]-\tfrac52y[n-1]+y[n-2]=x[n]+\beta x[n-1]$ | causal | poles $2,\ \tfrac12$: $\beta=-2$ cancels the pole at 2 |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #8a]] | $y[n]-\tfrac23y[n-1]-\tfrac89y[n-2]=3x[n]+\alpha x[n-1]$ | causal | poles $\tfrac43,\ -\tfrac23$: $\alpha=-4$ cancels $\tfrac43$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #8b]] | same LCCDE | two-sided | ROC $\tfrac23<\lvert z\rvert<\tfrac43$ contains $\lvert z\rvert=1$: stable for **every** $\alpha$ |

Close relatives: the cancellation idea is the same as in [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]] (an input zero on a bad pole) and FA2019 #10d (a system zero cancelling the pole of $2^nu[n]$ in a cascade). The "non-causal LCCDE" of FA2024 #8a is explained on [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]].

## The recipe

> [!recipe] Stability as a function of a parameter
> 1. **Transform** the LCCDE into $H(z)$ (signs as in [[problems/lccde-to-transfer-function-and-response|the LCCDE recipe]]). Note where the parameter lands: numerator (it moves a zero) or denominator (it moves a pole).
> 2. **Factor the parameter-free polynomial** (usually the denominator) into first-order factors: these poles are fixed.
> 3. **Mark the bad poles for the stated causality:**
>    - causal, ROC $\lvert z\rvert>\max\lvert p\rvert$: bad = every pole with $\lvert p\rvert\ge1$;
>    - anti-causal / left-sided, ROC $\lvert z\rvert<\min\lvert p\rvert$: bad = every pole with $\lvert p\rvert\le1$;
>    - two-sided, ROC between the poles: stable whenever the annulus contains $\lvert z\rvert=1$ (poles on both sides of the circle, none on it), **for every value of the parameter**.
> 4. **Parameter in the numerator:** each bad pole must be a zero. Substitute $z^{-1}=1/p_{\text{bad}}$ into the numerator, set it to $0$, solve. Two bad poles need two simultaneous conditions, usually impossible, and then the answer is "no value".
> 5. **Parameter in the denominator** (a pole at $-\alpha$, say): write the condition on $\lvert\alpha\rvert$ directly (causal: $\lvert\alpha\rvert<1$; left-sided: $\lvert\alpha\rvert>1$). Then ask whether some special value puts that pole **on a zero**, where it cancels (Practice 2).
> 6. **Complex parameter or $\alpha^2$:** solve for the zero *location* first, then for $\alpha$, keeping every root. Magnitude alone is not enough.
>
> **Check.** Put the value back and show the common factor, e.g. $3-4z^{-1} = 3(1-\tfrac43z^{-1})$. Then state the new $H(z)$ and its ROC, with the remaining poles on the correct side of $\lvert z\rvert=1$.

> [!trap] Where the points go
> - **Sign of the cancelling value.** FA2023 #8a: $3+\alpha z^{-1}$ must vanish at $z=\tfrac43$, i.e. $3+\tfrac34\alpha=0$, so $\alpha=-4$, not $+4$. Substitute $z^{-1}=\tfrac34$, not $z$.
> - **Cancelling the wrong pole.** SP2025 #7 with $\alpha=\tfrac12$ puts zeros at $\pm\tfrac12$ and cancels the *stable* pole $\tfrac12$; the pole at $-2$ is untouched: still unstable.
> - **$\alpha$ versus $\alpha^2$, real versus complex.** SP2025 #7: zeros at $\pm\alpha$ must include $-2$, so $\alpha=\pm2$. $\alpha=\pm j2$ has the right magnitude but gives zeros $\pm j2$: False.
> - **Left-sided flips the inequality.** FA2024 #8a: the ROC is *inside* the pole ($\lvert z\rvert<\lvert\alpha\rvert$), so stability needs the pole *outside* the unit circle, $\lvert\alpha\rvert>1$. (The key's "$\lvert a\rvert>1$" means $\lvert\alpha\rvert$.)
> - **Two-sided needs nothing.** FA2023 #8b: once the ROC is the annulus $\tfrac23<\lvert z\rvert<\tfrac43$, the system is stable for all $\alpha$. Cancelling something there only changes $h$. The other "two-sided" pattern is an empty ROC, not a second system.
> - **Poles on the unit circle are bad too.** A pole at $\lvert p\rvert=1$ (marginal stability) is unstable and must be cancelled as well.
> - **State the new ROC.** After $\beta=-2$ in FA2024 #8b, $H=\dfrac{1}{1-\frac12z^{-1}}$ with ROC $\lvert z\rvert>\tfrac12$. The old $\lvert z\rvert>2$ no longer applies.

## Practice problems

> [!question] Practice 1 — one LCCDE, three causality assumptions
> $$
> y[n] + \tfrac76\,y[n-1] - \tfrac12\,y[n-2] = 2x[n] + \alpha\,x[n-1],\qquad \alpha\in\mathbb{R}.
> $$
> For which $\alpha$ is the system BIBO stable if it is (a) causal, (b) anti-causal (left-sided), (c) non-causal and two-sided? In (a) and (b) give $h[n]$ for that $\alpha$.

> [!success]- Solution
> $$
> \begin{gathered}
> H(z) = \frac{2+\alpha z^{-1}}{1+\frac76z^{-1}-\frac12z^{-2}} = \frac{2+\alpha z^{-1}}{(1+\frac32z^{-1})(1-\frac13z^{-1})},\\
> \text{poles } -\tfrac32,\ \tfrac13;\ \text{zero at } z=-\tfrac{\alpha}{2}.
> \end{gathered}
> $$
> **(a) Causal**, ROC $\lvert z\rvert>\tfrac32$: the bad pole is $-\tfrac32$. Zero there: $-\tfrac{\alpha}{2}=-\tfrac32$, so $\boxed{\alpha=3}$. Check: $2+3z^{-1} = 2(1+\tfrac32z^{-1})$ ✓, leaving $H=\dfrac{2}{1-\frac13z^{-1}}$, ROC $\lvert z\rvert>\tfrac13$, $h[n]=2(\tfrac13)^nu[n]$.
>
> **(b) Anti-causal**, ROC $\lvert z\rvert<\tfrac13$: now the *small* pole $\tfrac13$ is bad (a left-sided $(\tfrac13)^n u[-n-1]$ blows up as $n\to-\infty$). Zero there: $-\tfrac{\alpha}{2}=\tfrac13$, so $\boxed{\alpha=-\tfrac23}$. Check: $2-\tfrac23z^{-1} = 2(1-\tfrac13z^{-1})$ ✓, leaving $H=\dfrac{2}{1+\frac32z^{-1}}$, ROC $\lvert z\rvert<\tfrac32$ (contains the unit circle), $h[n] = -2\left(-\tfrac32\right)^nu[-n-1]$.
>
> **(c) Two-sided**, ROC $\tfrac13<\lvert z\rvert<\tfrac32$: contains $\lvert z\rvert=1$, so the system is stable for **every** real $\alpha$.
>
> The same equation needs a different answer in each case. The causality sentence is part of the problem.

> [!question] Practice 2 — the parameter is a pole
> $y[n] = a\,y[n-1] + x[n] - 2x[n-1]$ is causal and $a$ is real. For which $a$ is it BIBO stable? What are $h[n]$ for $a=2$ and for $a=1$?

> [!success]- Solution
> $H(z) = \dfrac{1-2z^{-1}}{1-az^{-1}}$: a zero at 2 and a pole at $a$.
> - If $a\neq2$ the pole survives, the causal ROC is $\lvert z\rvert>\lvert a\rvert$, and stability needs $\lvert a\rvert<1$. (For $a=0$ the system is the FIR filter $1-2z^{-1}$, also stable.)
> - If $a=2$ the pole lands on the zero: $H(z)=1$, $h[n]=\delta[n]$, stable.
>
> Answer: $\boxed{\lvert a\rvert<1\ \text{ or }\ a=2}$. For $a=1$: $H = \dfrac{1-2z^{-1}}{1-z^{-1}} = 1-\dfrac{z^{-1}}{1-z^{-1}}$, so $h[n]=\delta[n]-u[n-1]$. It is bounded but not absolutely summable: marginally stable, so **not** BIBO stable. Most students write only "$\lvert a\rvert<1$"; the exam logic (FA2024 #8b, FA2023 #8a) is exactly the one that makes $a=2$ count.

> [!question] Practice 3 — complex $\alpha$, true or false
> A causal system satisfies $y[n] = -\tfrac{11}{4}y[n-1] + \tfrac34y[n-2] + x[n] + \alpha^2x[n-2]$ with $\alpha\in\mathbb{C}$. Mark each value True if it makes the system BIBO stable: (a) $3$ (b) $-3$ (c) $3j$ (d) $-3j$ (e) $\tfrac{j}{4}$ (f) $\tfrac14$.

> [!success]- Solution
> $1+\tfrac{11}{4}z^{-1}-\tfrac34z^{-2} = (1+3z^{-1})(1-\tfrac14z^{-1})$: poles $-3$ (bad) and $\tfrac14$. Zeros: $1+\alpha^2z^{-2}=0 \iff z^2=-\alpha^2 \iff z=\pm j\alpha$. We need $-3$ among $\pm j\alpha$, i.e. $\alpha^2=-9$, $\alpha=\pm3j$.
>
> | $\alpha$ | $\alpha^2$ | zeros $\pm j\alpha$ | stable? |
> |---|---|---|---|
> | $3$ | $9$ | $\pm3j$ | **F** (right magnitude, wrong angle) |
> | $-3$ | $9$ | $\pm3j$ | **F** |
> | $3j$ | $-9$ | $\pm3$ | **T**: $1-9z^{-2}=(1-3z^{-1})(1+3z^{-1})$ cancels $-3$ |
> | $-3j$ | $-9$ | $\pm3$ | **T** |
> | $\frac{j}{4}$ | $-\frac{1}{16}$ | $\pm\frac14$ | **F**: cancels the harmless pole $\frac14$ |
> | $\frac14$ | $\frac{1}{16}$ | $\pm\frac{j}{4}$ | **F** |
>
> For (c) and (d): $H = \dfrac{1-3z^{-1}}{1-\frac14z^{-1}}$, ROC $\lvert z\rvert>\tfrac14$.

The same bookkeeping with `np.roots`, for three of the candidates:

```python
import numpy as np

poles = np.roots([1, 11/4, -3/4])            # Practice 3 denominator, z^2 + (11/4)z - 3/4
print("poles:", poles)
for alpha in [3, 3j, 0.25j]:
    zeros = np.roots([1, 0, alpha**2]) + 0  # numerator z^2 + alpha^2 (+0 drops -0.)
    left = [p for p in poles if not np.isclose(zeros, p).any()]     # poles that survive
    verdict = "stable" if all(abs(p) < 1 for p in left) else "unstable"
    print(f"alpha = {alpha}: zeros {np.round(zeros, 3)}, surviving poles {np.round(left, 3)}, {verdict}")
```

```text
poles: [-3.    0.25]
alpha = 3: zeros [0.+3.j 0.-3.j], surviving poles [-3.    0.25], unstable
alpha = 3j: zeros [ 3.+0.j -3.+0.j], surviving poles [0.25], stable
alpha = 0.25j: zeros [ 0.25+0.j -0.25+0.j], surviving poles [-3.], unstable
```

> [!note] Exact cancellation is an idealisation
> The course (and every exam key) treats a cancelled pole as gone, and so does this page. In a real implementation the recursion still contains the unstable mode, and any tiny mismatch or roundoff excites it. That is a reason to be careful in practice; on the exam, "cancel it" is the intended answer.

## Where to go next

- Concepts: [[concepts/bibo-stability|BIBO stability]], [[concepts/pole-zero-cancellation|pole–zero cancellation]], [[concepts/region-of-convergence|ROC]], [[concepts/causality|causality]], [[concepts/marginal-stability|marginal stability]].
- Lectures: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] (ROC shape ↔ causality ↔ stability table), [[2-z-transform/09-transfer-functions|Lecture 9]] (LCCDE → $H(z)$).
- Related families: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]], [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]] (what "non-causal LCCDE" means), [[problems/all-possible-rocs|all possible ROCs]].
- Try it: [[demos/pole-zero-and-roc-explorer|pole–zero and ROC explorer]] (drag the zero onto the pole and watch the ROC change), [[demos/difference-equation-simulator|difference-equation simulator]], [[demos/practice-drills|practice drills]].

### Sources for this page

Lecture 9 notes (LCCDE → transfer function), Lecture 11 notes (§1.1 ROC shapes, Table 1); past midterms SP2025 #7, FA2024 #8, FA2023 #8. Practice problems are new; every claim is checked in `verify/problems/params_practice.py` (exact rational recursions for the causal cases, closed forms checked against $H(z)$ for the left-sided and two-sided cases).
