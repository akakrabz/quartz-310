---
title: "Right-, left- and two-sided sequences"
description: "Where a sequence is nonzero — right-sided, left-sided, two-sided, finite — fixes the shape of its ROC, and for an impulse response it fixes causality: causal, anti-causal or non-causal."
tags: [concept, signals, z-transform, roc]
aliases: ["right-sided", "left-sided", "two-sided", "anti-causal"]
---

> [!key] Definitions (Lectures 7 and 11)
> - **Right-sided**: $x[n] = 0$ for $n < n_0$ (for some integer $n_0$, positive or negative).
> - **Left-sided**: $x[n] = 0$ for $n > n_0$.
> - **Two-sided**: neither — nonzero for arbitrarily large positive **and** negative $n$.
> - **Finite-length**: both right- and left-sided.
>
> For an impulse response: **causal** means $h[n]=0$ for $n<0$ (right-sided with $n_0\ge0$); **anti-causal** means $h[n]=0$ for $n\ge0$ (uses only future inputs); anything else with $h[n]\neq0$ for some $n<0$ is **non-causal**.

**Why it shapes the ROC.** A right-sided tail $\sum_{n\ge n_0} x[n]z^{-n}$ converges for large $|z|$ (outside a circle); a left-sided tail $\sum_{n\le n_0} x[n]z^{-n}$ for small $|z|$ (inside a circle); a two-sided sequence needs both at once (an annulus). The start/end index decides the two special points: samples at $n<0$ contribute positive powers $z^{|n|}$, which blow up at $z=\infty$; samples at $n>0$ contribute $z^{-n}$, which blow up at $z=0$.

| sequence | example | ROC | as an impulse response |
|---|---|---|---|
| right-sided, $n_0 \ge 0$ | $\left(\frac12\right)^n u[n]$ | $\lvert z\rvert > \frac12$ (includes $\infty$) | causal |
| right-sided, $n_0 < 0$ | $\left(\frac12\right)^n u[n+2]$ | $\frac12 < \lvert z\rvert < \infty$ | non-causal |
| left-sided, $n_0 \le -1$ | $-2^n u[-n-1]$ | $\lvert z\rvert < 2$ (includes $0$) | anti-causal |
| left-sided, $n_0 > 0$ | $3^n u[-n+2]$ | $0 < \lvert z\rvert < 3$ | non-causal |
| two-sided | $\left(\frac12\right)^{\lvert n\rvert}$ | $\frac12 < \lvert z\rvert < 2$ | non-causal |
| finite, around $n=0$ | $\delta[n+1]+\delta[n]+\delta[n-1]$ | $0 < \lvert z\rvert < \infty$ | non-causal |

(The borderline $n_0 = 0$ for a left-sided sequence, e.g. $a^n u[-n]$, keeps $z=0$ in the ROC but is still non-causal because it uses the present **and** future inputs.)

> [!example] Two exam z-transforms where the endpoint matters
> - FA2025 #5a: $e^{j\pi n/3}u[n+4]$ is right-sided but starts at $n=-4$: $\ X(z) = \dfrac{e^{-j4\pi/3}z^{4}}{1-e^{j\pi/3}z^{-1}}$, ROC $1<|z|<\infty$ — **not** plain $|z|>1$.
> - SP2025 #5b: $3^n u[-n+2]$ is left-sided but ends at $n=2$: $\ X(z) = \dfrac{9z^{-2}}{1-\frac13 z} = \dfrac{-27z^{-3}}{1-3z^{-1}}$, ROC $0<|z|<3$.
> - Lecture 7's finite pair: $\delta[n]+\delta[n-1] \leftrightarrow 1+z^{-1}$ (ROC $|z|>0$, causal) versus $\delta[n+1]+\delta[n] \leftrightarrow z+1$ (ROC $|z|<\infty$, non-causal); their sum needs $0<|z|<\infty$.

**Two-sided impulse responses split.** Lecture 11 writes $h[n] = h_r[n] + h_l[n]$ with $h_r$ the $n\ge0$ part and $h_l$ the $n<0$ part; the ROC is (at least) the intersection $|p_{\max}(h_r)| < |z| < |p_{\min}(h_l)|$, and the system is stable iff that annulus contains $|z|=1$. The anti-causal part can still be computed — as a recursion that runs **backwards** in $n$ (FA2025 #7b, FA2024 #8a; [[problems/two-sided-systems-as-recursions]]).

> [!trap]
> - **Right-sided does not mean causal.** $\delta[n+1]$ is right-sided and non-causal: SP2023 T/F (c) ("right-sided ⇒ causal") is False.
> - **Left-sided vs causal.** FA2025 T/F (d) says "an LTI system with a left-sided impulse response can never be causal" and the key marks it True — reading "left-sided" as extending to $n\to-\infty$. Strictly, $\delta[n]$ is both left-sided and causal ([[0-toolkit/05-errata|errata]]). On the exam, answer as the key does, and say why if there is room.
> - **Two-sided can be stable**: $\left(\frac12\right)^{|n|}$ has $\sum|h| = 3$ (SP2025 T/F (f), "never stable": False). A stable system with poles $\frac14$ and $3$ **must** be two-sided (FA2025 T/F (c), True).
> - **Anti-causal is a kind of non-causal**: a stable $\frac{1}{1-3z^{-1}}$ must be non-causal (FA2023 T/F (f), True); a stable $\frac{1}{1-\sqrt2 z^{-1}}$ must be anti-causal (SP2025 T/F (e), True): its ROC $|z|<\sqrt2$ gives $h[n] = -(\sqrt2)^n u[-n-1]$.
> - $u[-n]$ includes $n=0$, $u[-n-1]$ does not; $u[n+k]$ starts at $n=-k$.

**Where it appears.**
- Lectures: [[2-z-transform/07-z-transform-properties|L7]] §1 (ROC shapes), [[2-z-transform/11-bibo-stability-and-causality|L11]] §1.1 (definitions, Fig. 1, $h = h_l + h_r$, Table 1); [[1-signals-and-systems/03-system-properties|L3]] and [[1-signals-and-systems/04-impulse-response-and-convolution|L4]] ([[concepts/causality|causality]]).
- Problem families: [[problems/z-transform-with-roc]], [[problems/all-possible-rocs]], [[problems/two-sided-systems-as-recursions]].
- Homework: [[homework/hw3|HW3]] #1 (c)–(d), #3(c); [[homework/hw4|HW4]] #1.
- Past exams: [[0-midterm-1/past-exams/fall-2025|FA2025]] #5a, #7, T/F (c), (d); [[0-midterm-1/past-exams/spring-2025|SP2025]] #5b, T/F (e), (f); [[0-midterm-1/past-exams/fall-2024|FA2024 #8a]]; [[0-midterm-1/past-exams/fall-2023|FA2023 T/F (f)]]; [[0-midterm-1/past-exams/spring-2023|SP2023 T/F (c)]].

Related: [[concepts/region-of-convergence]] · [[concepts/causality]] · [[concepts/bibo-stability]] · [[concepts/inverse-z-transform]] · [[concepts/z-transform-pairs]] · [[concepts/discrete-time-signal]]

### Sources for this page
Lecture 7 notes §1 (ROC shapes, the $\delta[n]+\delta[n\pm1]$ examples); Lecture 11 notes §1.1 (right/left-sided definitions, causal/anti-causal/non-causal, Fig. 1, Eqs. 15–18, Table 1); exam keys FA2025 #5a/#7, SP2025 #5b, and the T/F items cited; brief errata (FA2025 T/F (d)). Verification: `verify/concepts/verify_zdomain_extra.py` (every table row summed at a point inside its ROC), `verify_pairs.py` (FA2025 #5a, SP2025 #5b), `verify/exams/tf_bank.py`.
