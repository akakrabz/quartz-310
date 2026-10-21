---
title: "True/False bank"
description: "All 43 non-DTFT True/False statements from the seven past ECE 310 Midterm 1 exams (FA2019–FA2025), grouped by topic, with the official answer and a one-line reason folded away as flashcards."
tags: [midterm-1, exam, problem-family]
family_frequency: "7 of 7 exams"
typical_points: "10–12"
lectures: [3, 4, 9, 10, 11]
---

*Problem family · 7 of 7 past exams, always problem 1 · 10–12 pts (SP2021: 15, FA2019: 20) · [[1-signals-and-systems/03-system-properties|L3]], [[1-signals-and-systems/04-impulse-response-and-convolution|L4]], [[2-z-transform/09-transfer-functions|L9]]–[[2-z-transform/11-bibo-stability-and-causality|L11]] · 43 statements, 27 False · DTFT items (SP2023 #1d–e) omitted; FA2019 #10(d) included.*

> [!exam] How the problem looks
> 6 × 2 pts (FA2023–FA2025), 5 × 3 (SP2021), 10 × 2 (FA2019), 3 (+2 DTFT) × 2 (SP2023). SP2023/SP2025 grade +2 / −1 / 0: a coin flip is worth $+0.5$, so never leave a blank. No justification asked.

## The counterexample kit

> [!key] Six objects that refute most statements
> - $h[n] = u[n]$: **bounded but unstable** (input $u[n]$ gives $(n+1)u[n]$).
> - $h[n] = \delta[n] - \delta[n-1]$: **stable, undoes the accumulator**: $u[n] * (\delta[n]-\delta[n-1]) = \delta[n]$.
> - $h[n] = (\tfrac12)^{\lvert n\rvert}$: **two-sided and stable** ($\sum\lvert h\rvert = 3$).
> - $y[n] = n\,x[n]$: **causal, time-varying, unstable**, "impulse response" $n\,\delta[n] = 0$.
> - $y[n] = x^2[n]$: **nonlinear with $h[n] = \delta[n]$**.
> - A zero on a pole: $H(z) = 1-2z^{-1}$ turns $2^n u[n]$ into $\delta[n]$.

## 1. Impulse response and LTI

[[concepts/impulse-response|impulse response]] · [[concepts/lti-system|LTI system]]

**Q1** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(a)]] · For a discrete-time system with impulse response $h[n]$, the system output $y[n]$ to any input signal $x[n]$ is always determined using $h[n]$.

> [!success]- Answer
> **False.** LTI only: $y[n] = n\,x[n]$ has $h = 0$, yet answers $\delta[n-1]$ with $\delta[n-1]$.

**Q2** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(d)]] · For a discrete-time system with impulse response $h[n]$, the system output $y[n]$ to any input signal $x[n]$ is always given by $y[n] = x[n] * h[n]$.

> [!success]- Answer
> **False.** $y[n] = x^2[n]$ has $h = \delta[n]$, so $x*h = x$, but the output is $x^2$.

**Q3** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(b)]] · The input and output relationship of an arbitrary system is completely determined by the system's unit pulse response.

> [!success]- Answer
> **False.** $y = x^2[n]$ and $y = x[n]$ share $h = \delta[n]$ but differ for $x = 2\delta[n]$ ($4\delta[n]$ vs $2\delta[n]$).

**Q4** · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(a)]] · If the system response $y[n]$ of a discrete-time system to any possible input signal $x[n]$ is fully described by its unit pulse response, then the system must be LTI.

> [!success]- Answer
> **True.** $y = x*h$ for all $x$ ⇒ LTI (HW2 #2); converse of Q1–Q3.

## 2. Causality and sidedness

[[concepts/causality|causality]] · [[concepts/sided-sequences|sided sequences]]

**Q5** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(b)]] · The convolution of two causal signals always results in a causal signal. (A causal signal is defined as a signal that is zero for all negative time values.)

> [!success]- Answer
> **True.** Needs $k \ge 0$ and $k \le n$; empty for $n<0$.

**Q6** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(a)]] · If the output, $y[n]$, of a system is related to its input, $x[n]$, by $y[n] = \sum_{\ell=-\infty}^{\infty} h[\ell]\,x[n-\ell]$, for some well-defined function $h[n]$, the system must be a causal system.

> [!success]- Answer
> **False.** $h[n] = \delta[n+1]$ gives $y[n] = x[n+1]$.

**Q7** · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(c)]] · If a system has a right-sided unit pulse response, then it must be causal.

> [!success]- Answer
> **False.** $h[n] = u[n+1]$ is right-sided with $h[-1] = 1$.

**Q8** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(d)]] · An LTI system with a left-sided impulse response can never be causal.

> [!success]- Answer
> **True** (key). A left-sided $h$ extending to $-\infty$ has $h[n] \ne 0$ for some $n<0$ (under the strict definition $\delta[n]$ would qualify; answer True).

**Q9** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(a)]] · Any causal discrete-time system must also be time-invariant.

> [!success]- Answer
> **False.** $y[n] = n\,x[n]$: causal, time-varying.

**Q10** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(f)]] · A time-varying system cannot be causal.

> [!success]- Answer
> **False.** $y[n] = n\,x[n]$ (or the HW1 #6 window) is time-varying and causal.

## 3. BIBO stability

LTI: stable $\iff \sum_n \lvert h[n]\rvert < \infty$ $\iff$ ROC contains $\lvert z\rvert = 1$; bounded inputs only. [[concepts/bibo-stability|BIBO stability]]

**Q11** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(a)]] · The impulse response of a given LTI system is known to be a bounded sequence. This system must be BIBO stable.

> [!success]- Answer
> **False.** $h = u[n]$ is bounded; $u[n]$ in gives $(n+1)u[n]$.

**Q12** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(b)]] · The impulse response $h[n]$ of an unstable LTI system will always be an unbounded sequence.

> [!success]- Answer
> **False.** $h = u[n]$: unstable, bounded.

**Q13** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(c)]] · If an LSI system is BIBO unstable, its unit pulse response $h[n]$ must be unbounded.

> [!success]- Answer
> **False.** As Q12 (LSI = LTI).

**Q14** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(b)]] · If the unit pulse response, $h[n]$, of a system $S$ is absolutely summable, i.e., $\sum_{n=-\infty}^{\infty} \lvert h[n]\rvert < \infty$, then $S$ must be BIBO-stable regardless if $S$ is LSI or not.

> [!success]- Answer
> **False.** LTI-only test: $y[n] = n\,x[n]$ has $h = 0$, yet $x = u[n]$ gives $y = n\,u[n]$.

**Q15** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(f)]] · An LTI system with a two-sided impulse response is never BIBO stable.

> [!success]- Answer
> **False.** $h[n] = (\tfrac12)^{\lvert n\rvert}$, $\sum\lvert h\rvert = 1 + 2\cdot 1 = 3$ (see Q33).

**Q16** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(e)]] · An unbounded signal is passed as input to a BIBO stable LTI system. The resulting output is always an unbounded signal.

> [!success]- Answer
> **False.** Stable $h = \delta[n] - 2\delta[n-1]$ maps $2^n u[n]$ to $\delta[n]$.

**Q17** · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(b)]] · If a system is BIBO stable, any unbounded input will produce an unbounded output.

> [!success]- Answer
> **False.** $y[n] = x[n] - x[n-1]$ maps $n\,u[n]$ to $u[n-1]$.

**Q18** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(i)]] · If the response $y[n]$ of an LSI system to the input $x[n] = 3^n u[n]$ is unbounded, the system must be BIBO unstable.

> [!success]- Answer
> **False.** The identity $h = \delta[n]$ is stable and returns $3^n u[n]$.

**Q19** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(j)]] · The response $y[n]$ of a BIBO *unstable* LSI system to any non-zero input $x[n]$ is always unbounded.

> [!success]- Answer
> **False.** $h = u[n]$ with $x = \delta[n] - \delta[n-1]$ gives $y = \delta[n]$.

**Q20** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(d)]] · A causal LTI system with transfer function $H(z) = \dfrac{z^{-1}}{1-z^{-1}}$ produces an unbounded output for input $x[n] = u[n]$.

> [!success]- Answer
> **True.** $Y(z) = \dfrac{z^{-1}}{(1-z^{-1})^2}$, $y[n] = n\,u[n]$ (double pole on the unit circle).

## 4. Parallel and series connections

Parallel: $h = h_1 + h_2$. Series: $h = h_1 * h_2$, $H = H_1H_2$. [[concepts/system-algebra|system algebra]]

**Q21** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(d)]] · The parallel connection of two BIBO stable LTI systems always results in another BIBO stable LTI system.

> [!success]- Answer
> **True.** $\sum\lvert h_1 + h_2\rvert \le \sum\lvert h_1\rvert + \sum\lvert h_2\rvert < \infty$.

**Q22** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(c)]] · Two BIBO stable LTI systems connected in parallel will always form a BIBO stable LTI system.

> [!success]- Answer
> **True.** As Q21.

**Q23** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(c)]] · Two BIBO stable systems connected in parallel always form a BIBO stable system.

> [!success]- Answer
> **True**, even without LTI: $\lvert y_1 + y_2\rvert \le B_1 + B_2$.

**Q24** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(f)]] · The parallel connection of two unstable LTI systems always forms another unstable LTI system.

> [!success]- Answer
> **False.** $h_1 = u[n]$, $h_2 = \delta[n] - u[n]$: $h_1 + h_2 = \delta[n]$.

**Q25** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(c)]] · Cascade of two BIBO *unstable* LTI systems cannot be stable.

> [!success]- Answer
> **False.** Causal $H_1 = \dfrac{1-2z^{-1}}{1-3z^{-1}}$, $H_2 = \dfrac{1-3z^{-1}}{1-2z^{-1}}$: $H_1H_2 = 1$.

**Q26** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(d)]] · Let $h[n] = h_1[n] * h_2[n]$ be the unit pulse response (UPR) of two serial subsystems with UPR $h_1[n]$ and $h_2[n]$. If $h_1$ or $h_2$ is BIBO *unstable*, $h$ must be BIBO *unstable*.

> [!success]- Answer
> **False.** $u[n] * (\delta[n] - \delta[n-1]) = \delta[n]$.

**Q27** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #10(d)]] · (Here $H(z) = \dfrac{1-2z^{-1}}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})}$ is causal.) If the previous system is serially connected to an unstable LSI system with impulse response $\tilde h[n] = 2^n u[n]$, then the overall system is BIBO unstable.

> [!success]- Answer
> **False.** $H(z)\cdot\dfrac{1}{1-2z^{-1}} = \dfrac{1}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})}$, ROC $\lvert z\rvert > \tfrac12$: stable.

**Q28** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(e)]] · Two LTI systems given by impulse responses $h_1[n]$ and $h_2[n]$ are connected in series in some order, i.e. $h_1[n]$ or $h_2[n]$ may come first. If we pass an input signal $x[n]$ to this system, we will receive the same output signal $y[n]$ for either ordering of $h_1[n]$ and $h_2[n]$.

> [!success]- Answer
> **True.** $(x*h_1)*h_2 = x*(h_1*h_2) = x*(h_2*h_1) = (x*h_2)*h_1$.

## 5. z-transform, ROC and poles

[[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]]

**Q29** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(c)]] · The z-transform of $x[n] = e^{j\frac{\pi}{4}n}$ does not exist because the ROC is empty.

> [!success]- Answer
> **True.** $n \ge 0$ needs $\lvert z\rvert > 1$, $n<0$ needs $\lvert z\rvert < 1$.

**Q30** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(b)]] · The ROC of a given z-transform cannot contain any poles or zeros.

> [!success]- Answer
> **False.** Zeros are allowed: $X(z) = 1 - z^{-1}$, ROC $z \ne 0$, contains $z = 1$.

**Q31** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(b)]] · Let $X_1(z)$, $X_2(z)$ be the rational z-transforms of $x_1[n]$, $x_2[n]$. Then the poles of $X_1(z)$ and $X_2(z)$ must be poles of the z-transform of $x[n] = x_1[n] + x_2[n]$.

> [!success]- Answer
> **False.** $x_1 = (\tfrac12)^n u[n]$, $x_2 = \delta[n] - (\tfrac12)^n u[n]$: $X = 1$ (key: "possible pole–zero cancellation").

**Q32** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(h)]] · Suppose that the step response $g[n]$ of an LSI system, i.e., the output of the system to the input $x[n] = u[n]$, has a z-transform with a pole at $z = 1/2$. Then, $H(z)$ has also pole at $z = 1/2$.

> [!success]- Answer
> **True.** $G(z) = H(z)\cdot\dfrac{1}{1-z^{-1}}$; the step factor is $-1$ at $z = \tfrac12$, so the pole comes from $H$.

**Q33** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(c)]] · A BIBO stable LTI system has a transfer function with two poles at $z = \frac14$ and $z = 3$. The impulse response of this system must be two-sided.

> [!success]- Answer
> **True.** Stability forces ROC $\tfrac14 < \lvert z\rvert < 3$: two-sided.

**Q34** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(e)]] · A BIBO stable LTI system has a transfer function given by $H(z) = \dfrac{1}{1-\sqrt{2}\,z^{-1}}$. This system must be anti-causal.

> [!success]- Answer
> **True.** Pole $\sqrt2 \approx 1.41$; ROC $\lvert z\rvert < \sqrt2$, $h[n] = -(\sqrt2)^n u[-n-1]$.

**Q35** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(f)]] · A BIBO stable LTI system with transfer function $H(z) = \dfrac{1}{1-3z^{-1}}$ must be non-causal.

> [!success]- Answer
> **True.** ROC $\lvert z\rvert < 3$, $h[n] = -3^n u[-n-1]$.

**Q36** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(f)]] · An LTI system with transfer function $H(z) = \dfrac{1}{1-0.5z^{-1}} + \dfrac{1}{1-2z^{-1}}$ must **not** be BIBO stable.

> [!success]- Answer
> **False.** ROC $\tfrac12 < \lvert z\rvert < 2$: $h[n] = (\tfrac12)^n u[n] - 2^n u[-n-1]$ is stable.

**Q37** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(a)]] · An LTI system with transfer function $H(z) = \dfrac{1-z^{-1}}{1-2z^{-1}}$ cannot be stable.

> [!success]- Answer
> **False.** ROC $\lvert z\rvert < 2$ is stable (left-sided); only "causal and stable" is impossible.

## 6. LCCDE, FIR and IIR

[[concepts/lccde|LCCDE]] · [[concepts/fir-and-iir|FIR and IIR]]

**Q38** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(d)]] · An LCCDE system can only have a finite number of poles.

> [!success]- Answer
> **True.** $H(z) = B(z)/A(z)$, finite-degree polynomials.

**Q39** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(e)]] · An LTI system given by $y[n] = y[n-3] + x[n]$ will have three distinct poles in its transfer function.

> [!success]- Answer
> **True.** $H(z) = \dfrac{1}{1-z^{-3}} = \dfrac{z^3}{z^3-1}$: poles $1, e^{\pm j2\pi/3}$, distinct.

**Q40** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(a)]] · An LSI system specified by the following difference equation: $y[n] - \tfrac12 y[n-1] = x[n]$ can be causal or anti-causal.

> [!success]- Answer
> **True.** $\lvert z\rvert > \tfrac12$: $(\tfrac12)^n u[n]$; $\lvert z\rvert < \tfrac12$: $-(\tfrac12)^n u[-n-1]$; both satisfy it.

**Q41** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(e)]] · An LSI system with a finite-length impulse response can be BIBO stable or unstable.

> [!success]- Answer
> **False.** FIR ⇒ finite $\sum\lvert h\rvert$ ⇒ always stable.

## 7. Miscellaneous tricks: $\sum x[n]\,\delta[f(n)]$

$\delta[f(n)] = 1$ where $f(n) = 0$. [[concepts/kronecker-delta|Kronecker delta]]

**Q42** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(e)]] · Suppose $\sum_{n=-\infty}^{\infty} x[n]\,\delta\!\left[4\cos(2n\pi + \tfrac{\pi}{2}) - 6\sin(n\pi)\right] = 4$. Then, $\sum_{n=-\infty}^{\infty} x[n] = 3$.

> [!success]- Answer
> **False.** The argument is 0 for every integer $n$, so the sum is $\sum x[n] = 4$.

**Q43** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(g)]] · Let $\sum_{n=-\infty}^{\infty} x[n]\,\delta[2^n u[n] - 8] = 4$. Then, $x[3] = 2$.

> [!success]- Answer
> **False.** $2^n u[n] - 8 = 0$ only at $n = 3$: $x[3] = 4$.

## 8. Patterns that recur

> [!key] The ten patterns
> 1. Parallel of stable is stable (Q21–Q23).
> 2. "Must be unstable" after connection: False, by cancellation (Q24–Q27).
> 3. Unbounded in/out claims for stable or unstable systems: False (Q16–Q19).
> 4. "Bounded $h$ ⇒ stable" and "unstable ⇒ unbounded $h$": both False, $h = u[n]$ (Q11–Q13).
> 5. $h$ speaks only for LTI (Q1–Q3, Q14); converse True (Q4).
> 6. No ROC given ⇒ you choose it (Q36, Q37); stable + poles ⇒ sidedness (Q33–Q35).
> 7. Sidedness ≠ causality (Q5, Q7, Q8, Q15).
> 8. The four properties are independent (Q9, Q10).
> 9. Poles cancel in sums, products, input × system (Q16, Q25–Q27, Q31); a pole of $H\cdot\frac{1}{1-z^{-1}}$ away from $z = 1$ is a pole of $H$ (Q32); ROC may hold zeros (Q30).
> 10. $\sum x[n]\,\delta[f(n)]$: solve $f(n) = 0$ over integers (Q42, Q43).

> [!trap] Where points actually go
> - Universal claims answered by intuition (27 of 43 are False); BIBO read as "every input"; assuming causal without a stated ROC (Q36, Q37, Q40); reading "system" as LTI (Q2, Q3, Q14, Q23).

## 9. Answers by exam

| exam, problem | answers in order | on this page |
|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #1]] (12 pts) | F T T T F F | Q11, Q5, Q33, Q8, Q16, Q24 |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #1]] (12 pts) | F F T T T F | Q6, Q14, Q29, Q21, Q34, Q15 |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #1]] (12 pts) | F F T T T F | Q1, Q12, Q22, Q38, Q39, Q36 |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #1]] (12 pts) | F F T F T T | Q9, Q30, Q23, Q2, Q28, Q35 |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #1]] (10 pts) | T F F, then (d), (e) DTFT | Q4, Q17, Q7 |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #1]] (15 pts) | F F F T F | Q37, Q31, Q25, Q20, Q42 |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #1]] (20 pts) | T F F F F F F T F F | Q40, Q3, Q13, Q26, Q41, Q10, Q43, Q32, Q18, Q19 |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #10(d)]] | F | Q27 |

## Related

[[exams/midterm-1/system-property-bank|System-property bank]] · [[problems/classifying-system-properties|Classifying system properties]] · [[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]] · [[concepts/pole-zero-cancellation|Pole–zero cancellation]] · [[exams/midterm-1/past-exams/index|All past exams]]

### Sources for this page

Official keys of ECE 310 Midterm 1 #1, FA2019–FA2025, and FA2019 #10(d); Lectures 3, 4, 9–11; HW1 #6, HW2 #2.
