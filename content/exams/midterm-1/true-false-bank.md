---
title: "True/False bank"
description: "All 43 non-DTFT True/False statements from the seven past ECE 310 Midterm 1 exams (FA2019–FA2025), grouped by topic, with the official answer and a one-line reason folded away so the page works as flashcards."
tags: [midterm-1, exam, problem-family]
family_frequency: "7 of 7 exams"
typical_points: "10–12"
lectures: [3, 4, 9, 10, 11]
---

*Problem family · on 7 of 7 past exams, always problem 1 · 10–12 pts on recent exams (SP2021: 15, FA2019: 20) · [[1-signals-and-systems/03-system-properties|Lecture 3]], [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · 43 statements, 27 of them False*

> [!abstract] How to use this page
> Every statement below is typed as it appeared on the exam, with its source linked. Say **True** or **False** out loud, *then* open the folded **Answer** callout: it holds the official answer and a one-line reason (usually a counterexample). The DTFT statements (SP2023 #1d, #1e) are left out, since the DTFT is not on the Fall 2026 Midterm 1. FA2019 #10(d), a True/False part inside a longer problem, is included.

> [!exam] How the problem looks
> Always problem 1: six statements × 2 pts on FA2023, FA2024, SP2025 and FA2025; five × 3 pts on SP2021; ten × 2 pts on FA2019; three (plus two DTFT) × 2 pts on SP2023. SP2025 and SP2023 print the rule **+2 correct, −1 wrong, 0 blank**. With that rule a pure coin flip is still worth $+0.5$ points on average, so never leave a statement blank. No justification is asked for.

## The counterexample kit

Most False statements are universal claims ("always", "never", "must", "cannot") and die to one counterexample. The same handful keep working:

> [!key] Six objects that refute most statements
> - $h[n] = u[n]$, the accumulator: **bounded but unstable** ($\sum\lvert h\rvert = \infty$; input $u[n]$ gives $(n+1)u[n]$).
> - $h[n] = \delta[n] - \delta[n-1]$, the first difference: **stable, and it undoes the accumulator**: $u[n] * (\delta[n]-\delta[n-1]) = \delta[n]$.
> - $h[n] = (\tfrac12)^{\lvert n\rvert}$: **two-sided and stable** ($\sum\lvert h\rvert = 3$).
> - $y[n] = n\,x[n]$: **causal, time-varying, unstable**, and its "impulse response" is $n\,\delta[n] = 0$.
> - $y[n] = x^2[n]$: **nonlinear with $h[n] = \delta[n]$**, the same $h$ as the identity system.
> - A zero on top of a pole: $H(z) = 1-2z^{-1}$ turns the unbounded input $2^n u[n]$ into $\delta[n]$. Pole–zero cancellation rescues inputs, sums and cascades.

## 1. Impulse response and LTI

What $h[n]$ tells you, and when. See [[concepts/impulse-response|impulse response]], [[concepts/lti-system|LTI system]], [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]].

**Q1** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(a)]] · For a discrete-time system with impulse response $h[n]$, the system output $y[n]$ to any input signal $x[n]$ is always determined using $h[n]$.

> [!success]- Answer
> **False.** Only an LTI system is determined by $h[n]$. Example: $y[n] = n\,x[n]$ has $h[n] = n\,\delta[n] = 0$, yet it answers $\delta[n-1]$ with $\delta[n-1]$.

**Q2** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(d)]] · For a discrete-time system with impulse response $h[n]$, the system output $y[n]$ to any input signal $x[n]$ is always given by $y[n] = x[n] * h[n]$.

> [!success]- Answer
> **False.** $y = x*h$ needs linearity *and* time-invariance. $y[n] = x^2[n]$ has $h[n] = \delta^2[n] = \delta[n]$, so $x*h = x$, but the output is $x^2$.

**Q3** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(b)]] · The input and output relationship of an arbitrary system is completely determined by the system's unit pulse response.

> [!success]- Answer
> **False.** "Arbitrary" is the trap: $y = x^2[n]$ and the identity $y = x[n]$ share $h[n] = \delta[n]$ but differ for $x = 2\delta[n]$ ($4\delta[n]$ vs $2\delta[n]$).

**Q4** · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(a)]] · If the system response $y[n]$ of a discrete-time system to any possible input signal $x[n]$ is fully described by its unit pulse response, then the system must be LTI.

> [!success]- Answer
> **True.** "Fully described by $h$ for every input" means $y = x*h$ for all $x$, and every convolution system is linear and time-invariant (HW2 #2). This is the converse of Q1–Q3.

## 2. Causality and sidedness

Causal means $y[n]$ uses no future input; for LTI systems that is $h[n] = 0$ for $n<0$. See [[concepts/causality|causality]], [[concepts/sided-sequences|sided sequences]].

**Q5** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(b)]] · The convolution of two causal signals always results in a causal signal. (A causal signal is defined as a signal that is zero for all negative time values.)

> [!success]- Answer
> **True.** $y[n] = \sum_k x[k]h[n-k]$ needs $k \ge 0$ (for $x$) and $k \le n$ (for $h$). For $n<0$ no $k$ qualifies, so $y[n] = 0$.

**Q6** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(a)]] · If the output, $y[n]$, of a system is related to its input, $x[n]$, by $y[n] = \sum_{\ell=-\infty}^{\infty} h[\ell]\,x[n-\ell]$, for some well-defined function $h[n]$, the system must be a causal system.

> [!success]- Answer
> **False.** The convolution sum makes the system LTI, not causal. It is causal only if $h[\ell] = 0$ for $\ell<0$; $h[n] = \delta[n+1]$ gives $y[n] = x[n+1]$.

**Q7** · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(c)]] · If a system has a right-sided unit pulse response, then it must be causal.

> [!success]- Answer
> **False.** Right-sided means $h[n] = 0$ for $n < N_0$ for *some* $N_0$, possibly negative. $h[n] = u[n+1]$ (the FA2023 #2 table system) is right-sided with $h[-1] = 1$, so it is not causal.

**Q8** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(d)]] · An LTI system with a left-sided impulse response can never be causal.

> [!success]- Answer
> **True** (official key). A left-sided $h$ keeps going to $n \to -\infty$, so $h[n] \ne 0$ for some $n<0$. Fine print: under the strict definition "$h[n] = 0$ for $n > N_0$", $\delta[n]$ counts as left-sided and *is* causal. The key means an $h$ that really extends to $-\infty$; answer True.

**Q9** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(a)]] · Any causal discrete-time system must also be time-invariant.

> [!success]- Answer
> **False.** The four properties are independent. $y[n] = n\,x[n]$ is causal (it only uses the present sample) and time-varying.

**Q10** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(f)]] · A time-varying system cannot be causal.

> [!success]- Answer
> **False.** Same example: $y[n] = n\,x[n]$ is time-varying and causal. So is the window $y[n] = x[n]$ for $0 \le n \le N-1$ (0 otherwise) from HW1 #6.

## 3. BIBO stability

For LTI systems: stable $\iff \sum_n \lvert h[n]\rvert < \infty$ $\iff$ the ROC contains $\lvert z\rvert = 1$. BIBO only talks about **bounded** inputs. See [[concepts/bibo-stability|BIBO stability]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]].

**Q11** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(a)]] · The impulse response of a given LTI system is known to be a bounded sequence. This system must be BIBO stable.

> [!success]- Answer
> **False.** Bounded is not absolutely summable. $h[n] = u[n]$ is bounded by 1, but $\sum\lvert h\rvert = \infty$: the bounded input $u[n]$ produces $(n+1)u[n]$.

**Q12** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(b)]] · The impulse response $h[n]$ of an unstable LTI system will always be an unbounded sequence.

> [!success]- Answer
> **False.** Unstable only means $\sum\lvert h[n]\rvert = \infty$, which does not require $\lvert h\rvert \to \infty$. $h[n] = u[n]$ is unstable and bounded.

**Q13** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(c)]] · If an LSI system is BIBO unstable, its unit pulse response $h[n]$ must be unbounded.

> [!success]- Answer
> **False.** Same as Q12: the accumulator $h[n] = u[n]$ (LSI = LTI).

**Q14** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(b)]] · If the unit pulse response, $h[n]$, of a system $S$ is absolutely summable, i.e., $\sum_{n=-\infty}^{\infty} \lvert h[n]\rvert < \infty$, then $S$ must be BIBO-stable regardless if $S$ is LSI or not.

> [!success]- Answer
> **False.** The $\sum\lvert h\rvert$ test is a theorem about LTI systems only. $y[n] = n\,x[n]$ has $h[n] = n\,\delta[n] = 0$ (absolutely summable), yet $x = u[n]$ gives $y = n\,u[n]$.

**Q15** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(f)]] · An LTI system with a two-sided impulse response is never BIBO stable.

> [!success]- Answer
> **False.** $h[n] = (\tfrac12)^{\lvert n\rvert}$ is two-sided with $\sum\lvert h\rvert = 1 + 2\cdot 1 = 3$. Any stable $H(z)$ with poles both inside and outside the unit circle has a two-sided $h$ (see Q33).

**Q16** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(e)]] · An unbounded signal is passed as input to a BIBO stable LTI system. The resulting output is always an unbounded signal.

> [!success]- Answer
> **False.** BIBO promises nothing about unbounded inputs. The stable FIR $h = \delta[n] - 2\delta[n-1]$ maps $2^n u[n]$ to $\delta[n]$: its zero at $z = 2$ cancels the input's pole.

**Q17** · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(b)]] · If a system is BIBO stable, any unbounded input will produce an unbounded output.

> [!success]- Answer
> **False.** The first difference $y[n] = x[n] - x[n-1]$ is stable and maps the unbounded ramp $n\,u[n]$ to $u[n-1]$. (Or $y[n] = \sin(x[n])$, which is bounded for every input.)

**Q18** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(i)]] · If the response $y[n]$ of an LSI system to the input $x[n] = 3^n u[n]$ is unbounded, the system must be BIBO unstable.

> [!success]- Answer
> **False.** The input was already unbounded, so this proves nothing. The identity $h = \delta[n]$ is stable and returns $3^n u[n]$ unchanged.

**Q19** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(j)]] · The response $y[n]$ of a BIBO *unstable* LSI system to any non-zero input $x[n]$ is always unbounded.

> [!success]- Answer
> **False.** Unstable means *some* bounded input blows up, not every input. $h = u[n]$ with $x = \delta[n] - \delta[n-1]$ gives $y = \delta[n]$.

**Q20** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(d)]] · A causal LTI system with transfer function $H(z) = \dfrac{z^{-1}}{1-z^{-1}}$ produces an unbounded output for input $x[n] = u[n]$.

> [!success]- Answer
> **True.** $Y(z) = \dfrac{z^{-1}}{(1-z^{-1})^2}$, so $y[n] = n\,u[n]$. The input's pole at $z = 1$ lands on the system's pole on the unit circle and makes a double pole, which gives a ramp.

## 4. Parallel and series connections

Parallel: $h = h_1 + h_2$, $H = H_1 + H_2$. Series: $h = h_1 * h_2$, $H = H_1H_2$. See [[concepts/system-algebra|system algebra]], [[concepts/pole-zero-cancellation|pole–zero cancellation]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]].

**Q21** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(d)]] · The parallel connection of two BIBO stable LTI systems always results in another BIBO stable LTI system.

> [!success]- Answer
> **True.** $\sum\lvert h_1 + h_2\rvert \le \sum\lvert h_1\rvert + \sum\lvert h_2\rvert < \infty$ (triangle inequality).

**Q22** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(c)]] · Two BIBO stable LTI systems connected in parallel will always form a BIBO stable LTI system.

> [!success]- Answer
> **True.** Same as Q21.

**Q23** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(c)]] · Two BIBO stable systems connected in parallel always form a BIBO stable system.

> [!success]- Answer
> **True**, even without LTI: if $\lvert y_1\rvert \le B_1$ and $\lvert y_2\rvert \le B_2$ for a bounded input, then $\lvert y_1 + y_2\rvert \le B_1 + B_2$.

**Q24** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(f)]] · The parallel connection of two unstable LTI systems always forms another unstable LTI system.

> [!success]- Answer
> **False.** $h_1 = u[n]$ and $h_2 = \delta[n] - u[n]$ are both unstable, but $h_1 + h_2 = \delta[n]$.

**Q25** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(c)]] · Cascade of two BIBO *unstable* LTI systems cannot be stable.

> [!success]- Answer
> **False.** Pole–zero cancellation: the causal systems $H_1 = \dfrac{1-2z^{-1}}{1-3z^{-1}}$ and $H_2 = \dfrac{1-3z^{-1}}{1-2z^{-1}}$ are both unstable, but $H_1H_2 = 1$, i.e. $h = \delta[n]$.

**Q26** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(d)]] · Let $h[n] = h_1[n] * h_2[n]$ be the unit pulse response (UPR) of two serial subsystems with UPR $h_1[n]$ and $h_2[n]$. If $h_1$ or $h_2$ is BIBO *unstable*, $h$ must be BIBO *unstable*.

> [!success]- Answer
> **False.** $u[n] * (\delta[n] - \delta[n-1]) = \delta[n]$: the zero of the first difference at $z = 1$ cancels the accumulator's pole.

**Q27** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #10(d)]] · (Here $H(z) = \dfrac{1-2z^{-1}}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})}$ is causal.) If the previous system is serially connected to an unstable LSI system with impulse response $\tilde h[n] = 2^n u[n]$, then the overall system is BIBO unstable.

> [!success]- Answer
> **False.** $H(z)\cdot\dfrac{1}{1-2z^{-1}} = \dfrac{1}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})}$, ROC $\lvert z\rvert > \tfrac12$: the zero of $H$ at $z = 2$ cancels the pole, and what is left is stable.

**Q28** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(e)]] · Two LTI systems given by impulse responses $h_1[n]$ and $h_2[n]$ are connected in series in some order, i.e. $h_1[n]$ or $h_2[n]$ may come first. If we pass an input signal $x[n]$ to this system, we will receive the same output signal $y[n]$ for either ordering of $h_1[n]$ and $h_2[n]$.

> [!success]- Answer
> **True.** Convolution is commutative and associative: $(x*h_1)*h_2 = x*(h_1*h_2) = x*(h_2*h_1) = (x*h_2)*h_1$. (This fails for non-LTI blocks.)

## 5. z-transform, ROC and poles

The ROC never contains a pole; it is a ring bounded by poles; a stable system's ROC contains $\lvert z\rvert = 1$. Without a stated ROC, a rational $H(z)$ is several systems at once. See [[concepts/region-of-convergence|ROC]], [[concepts/poles-and-zeros|poles and zeros]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]].

**Q29** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(c)]] · The z-transform of $x[n] = e^{j\frac{\pi}{4}n}$ does not exist because the ROC is empty.

> [!success]- Answer
> **True.** $x$ is two-sided. The $n \ge 0$ half converges only for $\lvert z\rvert > 1$ and the $n<0$ half only for $\lvert z\rvert < 1$, so no $z$ satisfies both.

**Q30** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(b)]] · The ROC of a given z-transform cannot contain any poles or zeros.

> [!success]- Answer
> **False.** No poles, yes, but zeros are allowed. $X(z) = 1 - z^{-1}$ (for $\delta[n]-\delta[n-1]$) has ROC $z \ne 0$, which contains its zero at $z = 1$.

**Q31** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(b)]] · Let $X_1(z)$, $X_2(z)$ be the rational z-transforms of $x_1[n]$, $x_2[n]$. Then the poles of $X_1(z)$ and $X_2(z)$ must be poles of the z-transform of $x[n] = x_1[n] + x_2[n]$.

> [!success]- Answer
> **False.** Poles can cancel in a sum. $x_1 = (\tfrac12)^n u[n]$ and $x_2 = \delta[n] - (\tfrac12)^n u[n]$ both have a pole at $\tfrac12$, but $x_1 + x_2 = \delta[n]$ has $X = 1$. (The key's margin note: "possible pole–zero cancellation".)

**Q32** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(h)]] · Suppose that the step response $g[n]$ of an LSI system, i.e., the output of the system to the input $x[n] = u[n]$, has a z-transform with a pole at $z = 1/2$. Then, $H(z)$ has also pole at $z = 1/2$.

> [!success]- Answer
> **True.** $G(z) = H(z)\cdot\dfrac{1}{1-z^{-1}}$. The step's factor is finite and nonzero at $z = \tfrac12$ (it equals $-1$ there), so it can neither create nor cancel a pole at $\tfrac12$. That pole must come from $H$.

**Q33** · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(c)]] · A BIBO stable LTI system has a transfer function with two poles at $z = \frac14$ and $z = 3$. The impulse response of this system must be two-sided.

> [!success]- Answer
> **True.** The possible ROCs are $\lvert z\rvert > 3$, $\lvert z\rvert < \tfrac14$ and $\tfrac14 < \lvert z\rvert < 3$. Stability forces the one that contains $\lvert z\rvert = 1$, which is the ring, so $h$ is two-sided.

**Q34** · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(e)]] · A BIBO stable LTI system has a transfer function given by $H(z) = \dfrac{1}{1-\sqrt{2}\,z^{-1}}$. This system must be anti-causal.

> [!success]- Answer
> **True.** The only pole is at $\sqrt2 \approx 1.41 > 1$. Stability forces the ROC $\lvert z\rvert < \sqrt2$, so $h[n] = -(\sqrt2)^n u[-n-1]$, which is left-sided (anti-causal).

**Q35** · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(f)]] · A BIBO stable LTI system with transfer function $H(z) = \dfrac{1}{1-3z^{-1}}$ must be non-causal.

> [!success]- Answer
> **True.** Pole at 3, so stability forces the ROC $\lvert z\rvert < 3$ and $h[n] = -3^n u[-n-1]$, which is not causal.

**Q36** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(f)]] · An LTI system with transfer function $H(z) = \dfrac{1}{1-0.5z^{-1}} + \dfrac{1}{1-2z^{-1}}$ must **not** be BIBO stable.

> [!success]- Answer
> **False.** No ROC is given. With $\tfrac12 < \lvert z\rvert < 2$ the ROC contains the unit circle, and $h[n] = (\tfrac12)^n u[n] - 2^n u[-n-1]$ is stable (two-sided). The other two ROCs ($\lvert z\rvert>2$, causal, and $\lvert z\rvert<\tfrac12$, anti-causal) both miss the unit circle and are unstable.

**Q37** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(a)]] · An LTI system with transfer function $H(z) = \dfrac{1-z^{-1}}{1-2z^{-1}}$ cannot be stable.

> [!success]- Answer
> **False.** The pole is at 2. The ROC $\lvert z\rvert < 2$ contains the unit circle, which gives a stable left-sided (non-causal) system. "Causal and stable" is what is impossible here.

## 6. LCCDE, FIR and IIR

See [[concepts/lccde|LCCDE]], [[concepts/fir-and-iir|FIR and IIR]], [[2-z-transform/09-transfer-functions|Lecture 9]].

**Q38** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(d)]] · An LCCDE system can only have a finite number of poles.

> [!success]- Answer
> **True.** A finite-order LCCDE gives $H(z) = B(z)/A(z)$, a ratio of finite-degree polynomials, so it has finitely many poles.

**Q39** · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(e)]] · An LTI system given by $y[n] = y[n-3] + x[n]$ will have three distinct poles in its transfer function.

> [!success]- Answer
> **True.** $H(z) = \dfrac{1}{1-z^{-3}} = \dfrac{z^3}{z^3-1}$, with poles at the cube roots of unity $1, e^{\pm j2\pi/3}$. They are distinct, and all three sit on the unit circle, so the causal system is not BIBO stable.

**Q40** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(a)]] · An LSI system specified by the following difference equation: $y[n] - \tfrac12 y[n-1] = x[n]$ can be causal or anti-causal.

> [!success]- Answer
> **True.** The LCCDE fixes $H(z) = \dfrac{1}{1-\frac12 z^{-1}}$ but not its ROC. $\lvert z\rvert > \tfrac12$ gives $(\tfrac12)^n u[n]$ and $\lvert z\rvert < \tfrac12$ gives $-(\tfrac12)^n u[-n-1]$, and both satisfy the equation. (Key: "we do not know if $y[n]$ or $y[n-1]$ represents the output", i.e. the recursion can run either way.)

**Q41** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(e)]] · An LSI system with a finite-length impulse response can be BIBO stable or unstable.

> [!success]- Answer
> **False.** For an FIR system, $\sum\lvert h\rvert$ is a finite sum of finite numbers, so it is always stable.

## 7. Miscellaneous tricks: $\sum x[n]\,\delta[f(n)]$

$\delta[f(n)] = 1$ exactly at the integers where $f(n) = 0$, so the sum picks out $x$ at those $n$. See [[concepts/kronecker-delta|Kronecker delta]].

**Q42** · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(e)]] · Suppose $\sum_{n=-\infty}^{\infty} x[n]\,\delta\!\left[4\cos(2n\pi + \tfrac{\pi}{2}) - 6\sin(n\pi)\right] = 4$. Then, $\sum_{n=-\infty}^{\infty} x[n] = 3$.

> [!success]- Answer
> **False.** For every integer $n$, $\cos(2\pi n + \tfrac\pi2) = 0$ and $\sin(\pi n) = 0$, so the delta equals 1 for **all** $n$. The given sum *is* $\sum x[n] = 4$, not 3.

**Q43** · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(g)]] · Let $\sum_{n=-\infty}^{\infty} x[n]\,\delta[2^n u[n] - 8] = 4$. Then, $x[3] = 2$.

> [!success]- Answer
> **False.** $2^n u[n] - 8$ is $-8$ for $n<0$ and $2^n - 8$ for $n \ge 0$, so it vanishes only at $n = 3$. The sum is $x[3] = 4$.

## 8. Patterns that recur

> [!key] The ten patterns (with the statements that use them)
> 1. **Parallel of two stable systems is stable: always True** (Q21, Q22, Q23). This holds even for non-LTI systems.
> 2. **"Must be unstable" after a parallel or series connection: False.** Unstable parts can combine into a stable whole through cancellation: $u[n] + (\delta[n]-u[n])$, $u[n] * (\delta[n]-\delta[n-1])$, $H$ times $1/H$ (Q24, Q25, Q26, Q27).
> 3. **BIBO stable ⇒ unbounded in gives unbounded out: False** (Q16, Q17). The mirror images are False too: an unbounded output from an unbounded input proves nothing (Q18), and an unstable system does not blow up on every input (Q19).
> 4. **$h[n]$ bounded ⇒ stable: False. Unstable ⇒ $h$ unbounded: False.** The counterexample is always $h = u[n]$ (Q11, Q12, Q13).
> 5. **$h[n]$ only speaks for LTI systems.** "Any system", "arbitrary system", "regardless if LSI" + a claim that $h$ determines output or stability: False (Q1, Q2, Q3, Q14). The converse, "fully described by $h$ ⇒ LTI", is True (Q4).
> 6. **No ROC given ⇒ you choose the ROC.** "Cannot be stable" / "must not be stable" is False unless a pole sits *on* $\lvert z\rvert = 1$ (Q36, Q37). "Stable + these poles ⇒ this sidedness" is True: the ROC must contain the unit circle, and that decides the sidedness (Q33, Q34, Q35).
> 7. **Sidedness ≠ causality.** Right-sided can be non-causal (Q7), a left-sided $h$ that extends to $-\infty$ cannot be causal (Q8), and causal $*$ causal is causal (Q5). Two-sided can be stable (Q15).
> 8. **The four properties are independent.** Causal says nothing about time-invariance (Q9, Q10).
> 9. **Poles can cancel** in sums (Q31), products (Q25–Q27) and input × system (Q16). A pole of $G = H\cdot\frac{1}{1-z^{-1}}$ away from $z = 1$ must be a pole of $H$ (Q32). The ROC may contain zeros (Q30).
> 10. **$\sum x[n]\,\delta[f(n)]$: solve $f(n) = 0$ over the integers** (Q42, Q43). Trigonometric arguments at integer multiples of $\pi$ are usually identically zero.

> [!trap] Where points actually go
> - Answering a universal claim ("always", "never", "must", "cannot") from intuition. Look for one counterexample from the kit above first. 27 of these 43 statements are False.
> - Treating "stable" as "the output is bounded for every input". BIBO covers **bounded inputs only**.
> - Assuming a causal ROC when none was given (Q36, Q37, Q40).
> - Reading "system" as "LTI system". Check the wording: Q2, Q3, Q14 and Q23 say "system" and mean any system.

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

## Python: two False statements in four lines

Pattern 3 and pattern 2 in `scipy.signal.lfilter(b, a, x)` form (coefficients of $H(z)$ in powers of $z^{-1}$):

```python
import numpy as np
from scipy.signal import lfilter
n = np.arange(8)
# stable FIR h = δ[n] − 2δ[n−1] driven by the UNBOUNDED input 2^n u[n]
print(lfilter([1, -2], [1], 2.0**n))
# UNSTABLE accumulator h = u[n] (H = 1/(1 − z^-1)) driven by δ[n] − δ[n−1]
print(lfilter([1], [1, -1], [1.0, -1, 0, 0, 0, 0, 0, 0]))
```

```text
[1. 0. 0. 0. 0. 0. 0. 0.]
[1. 0. 0. 0. 0. 0. 0. 0.]
```

Both outputs are $\delta[n]$: a stable system with an unbounded input (Q16) and an unstable system with a bounded output (Q19, Q26).

## Related

[[exams/midterm-1/system-property-bank|System-property bank]] · [[problems/classifying-system-properties|Classifying system properties]] · [[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/causality|Causality]] · [[concepts/region-of-convergence|ROC]] · [[concepts/pole-zero-cancellation|Pole–zero cancellation]] · [[concepts/marginal-stability|Marginal stability]] · [[exams/midterm-1/past-exams/index|All past exams]]

### Sources for this page

- Official solutions of ECE 310 Midterm 1: FA2025 #1, SP2025 #1, FA2024 #1, FA2023 #1, SP2023 #1, SP2021 #1, FA2019 #1 and #10(d) (answers read off the keys; FA2019 and SP2021 are handwritten).
- Lecture 3 (system properties), Lecture 4 (impulse response, convolution), Lectures 9–11 (transfer functions, system algebra, BIBO stability and causality via the ROC); HW1 #6, HW2 #2.
- Every counterexample on this page is checked numerically in `verify/exams/tf_bank.py` (42 checks, all passing).
