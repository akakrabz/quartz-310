#!/usr/bin/env python3
"""Recomputes every number on the Lecture 24-27, HW10 and HW11 pages. Needs numpy.

    python3 -B tools/verify_l24_27.py        # prints each check, ends with ALL OK
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figs_l24_27 as figs  # noqa: E402

PI = math.pi
n_checks = 0


def ok(cond, what):
    global n_checks
    n_checks += 1
    print(("ok   " if cond else "FAIL ") + what)
    if not cond:
        sys.exit(1)


def close(a, b, tol=1e-9):
    return np.allclose(a, b, atol=tol, rtol=0)


def Wn(N, k):
    return np.exp(-2j * PI * k / N)


# ---------------------------------------------------------------- Lecture 25: cost and merging
def dft_sum(x):
    N = len(x)
    X = np.zeros(N, complex)
    ops = 0
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * Wn(N, k * n)
            ops += 1
    return X, ops


def fft_dit(x):
    """Radix-2 decimation in time, exactly the lecture's recursion; returns (X, multiply-adds)."""
    N = len(x)
    if N == 1:
        return np.array(x, complex), 0
    A, opa = fft_dit(x[0::2])
    B, opb = fft_dit(x[1::2])
    X = np.zeros(N, complex)
    ops = opa + opb
    for k in range(N // 2):
        t = Wn(N, k) * B[k]
        X[k] = A[k] + t
        X[k + N // 2] = A[k] - t
        ops += 2
    return X, ops


rng = np.random.default_rng(310)
for N in (2, 4, 8, 16, 64, 1024):
    x = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    X, ops = fft_dit(x)
    ok(close(X, np.fft.fft(x), 1e-8) and ops == N * int(math.log2(N)), f"DIT FFT = DFT for N = {N}, {ops} = N log2 N multiply-adds")
for N in (4, 16):
    x = rng.standard_normal(N)
    X, ops = dft_sum(x)
    ok(close(X, np.fft.fft(x)) and ops == N * N, f"DFT sum for N = {N}: {ops} = N^2 multiply-adds")
ok(16 ** 2 // (16 * 4) == 4, "N = 16: N^2 / (N log2 N) = 256 / 64 = 4")
ok(abs(1024 ** 2 / (1024 * 10) - 102.4) < 1e-9, "N = 1024: 2^20 / (10 * 2^10) = 102.4")
v = 1e5 * math.log2(1e5)
ok(abs(v / 1e5 - 16.61) < 0.01 and 6000 < 1e10 / v < 6050, f"N = 1e5: N log2 N = {v:.3g} (16.6e5), N^2 / (N log2 N) = {1e10 / v:.0f}")
ok(8 * 3 == 24 and 4 * 2 == 8, "N = 8: 3 stages of 8 multiply-adds = 24; N = 4: 2 stages of 4 = 8")

# twiddle factor facts
ok(close(Wn(16, 3 + 8), -Wn(16, 3)), "W_N^(k+N/2) = -W_N^k")
ok(close(Wn(16, 2 * 3 * 5), Wn(8, 3 * 5)), "W_N^(2kn) = W_(N/2)^(kn)")
ok(close(Wn(2, 0), 1) and close(Wn(4, 1), -1j) and close(Wn(8, 2), -1j) and close(Wn(16, 4), -1j), "W_2^0 = 1, W_4^1 = W_8^2 = W_16^4 = -j")
ok(close(Wn(16, 6), -math.sqrt(2) / 2 - 1j * math.sqrt(2) / 2), "W_16^6 = e^(-j3pi/4) = -sqrt2/2 - j sqrt2/2")
ok(close(-Wn(8, 3), np.exp(1j * PI / 4)) and close(-Wn(16, 7), np.exp(1j * PI / 8)), "-W_8^3 = e^(j pi/4), -W_16^7 = e^(j pi/8)")

# length-4 formulas (Example 1) and the numeric examples on the page
x = np.array([1.0, 2.0, 3.0, 4.0])
X = np.array([x[0] + x[2] + x[1] + x[3], (x[0] - x[2]) - 1j * (x[1] - x[3]),
              x[0] + x[2] - (x[1] + x[3]), (x[0] - x[2]) + 1j * (x[1] - x[3])])
ok(close(X, np.fft.fft(x)) and close(X, [10, -2 + 2j, -2, -2 - 2j]), "length-4 merging formulas; x = {1,2,3,4} -> X = {10, -2+2j, -2, -2-2j}")
x8 = np.array([1.0, 2, 3, 4, 4, 3, 2, 1])
c, d, e, f_ = x8[[0, 4]], x8[[2, 6]], x8[[1, 5]], x8[[3, 7]]
C, D, E, Fq = [np.array([s[0] + s[1], s[0] - s[1]]) for s in (c, d, e, f_)]
ok(close(C, [5, -3]) and close(D, [5, 1]) and close(E, [5, -1]) and close(Fq, [5, 3]), "N = 8 example, stage 1: C = {5,-3}, D = {5,1}, E = {5,-1}, F = {5,3}")
A = np.array([C[0] + D[0], C[1] - 1j * D[1], C[0] - D[0], C[1] + 1j * D[1]])
B = np.array([E[0] + Fq[0], E[1] - 1j * Fq[1], E[0] - Fq[0], E[1] + 1j * Fq[1]])
ok(close(A, [10, -3 - 1j, 0, -3 + 1j]) and close(B, [10, -1 - 3j, 0, -1 + 3j]), "stage 2: A = {10, -3-j, 0, -3+j}, B = {10, -1-3j, 0, -1+3j}")
X8 = np.concatenate([A + Wn(8, np.arange(4)) * B, A - Wn(8, np.arange(4)) * B])
ok(close(X8, np.fft.fft(x8)), "stage 3 = numpy FFT of {1,2,3,4,4,3,2,1}")
r2 = math.sqrt(2)
ok(close(X8, [20, -3 - 2 * r2 - 1j * (1 + r2) + 0j + (0), 0, -3 + 2 * r2 + 1j * (1 - r2), 0, -3 + 2 * r2 - 1j * (1 - r2), 0,
              -3 - 2 * r2 + 1j * (1 + r2)]), "X = {20, -(3+2r2) - j(1+r2), 0, -(3-2r2) + j(1-r2), 0, conj, 0, conj}")


# ---------------------------------------------------------------- butterflies as stage matrices (N = 16)
def stage(N, L):
    """Matrix of the DIT stage that merges length-L/2 DFTs into length-L DFTs (rows in diagram order)."""
    M = np.zeros((N, N), complex)
    for base in range(0, N, L):
        for k in range(L // 2):
            t, b = base + k, base + k + L // 2
            M[t, t], M[t, b], M[b, t], M[b, b] = 1, Wn(L, k), 1, -Wn(L, k)
    return M


def bitrev(N):
    bits = int(math.log2(N))
    return [int(format(i, f"0{bits}b")[::-1], 2) for i in range(N)]


for N in (8, 16, 32):
    x = rng.standard_normal(N)
    y = x[bitrev(N)].astype(complex)
    L = 2
    while L <= N:
        y = stage(N, L) @ y
        L *= 2
    ok(close(y, np.fft.fft(x), 1e-8), f"N = {N}: bit-reversed input through the butterfly stages = DFT")
ok(bitrev(8) == [0, 4, 2, 6, 1, 5, 3, 7], "input order of the length-8 diagram: x0 x4 x2 x6 x1 x5 x3 x7")
S8, S16 = stage(16, 8), stage(16, 16)
# Lecture 25, Example 3 (slide 14): entry [to, from]
ok(close(S8[15, 15], -Wn(8, 3)), "Example 3: a = -W_8^3  (left 15 -> middle 15)")
ok(close(S16[15, 15], -Wn(16, 7)), "Example 3: b = -W_16^7 (middle 15 -> right 15)")
ok(close(S8[2, 6], Wn(8, 2)), "Example 3: c = W_8^2  (left 6 -> middle 2)")
ok(close(S16[4, 4], 1), "Example 3: d = 1 (middle 4 -> right 4)")
ok(close(S16[4, 12], Wn(16, 4)), "Example 3: e = W_16^4 (middle 12 -> right 4)")
# HW10 #1 (official key: a = -1, b = W_16^6, c = W_8^2 = -j)
ok(close(S16[8, 8], -1), "HW10 #1: a = -W_16^0 = -1 (middle 8 -> right 8)")
ok(close(S16[6, 14], Wn(16, 6)), "HW10 #1: b = W_16^6 (middle 14 -> right 6)")
ok(close(S8[10, 14], -1j), "HW10 #1: c = W_8^2 = -j (left 14 -> middle 10)")
S32, S16of32 = stage(32, 32), stage(32, 16)
ok(close(S32[11, 11], 1) and close(S32[27, 27], -Wn(32, 11)) and close(S32[19, 19], -Wn(32, 3)) and close(S16of32[27, 27], -Wn(16, 3)),
   "FA2019 MT2 #10 as on its page: a = 1, c = -W_32^11, b = -W_32^3, d = -W_16^3")


# ---------------------------------------------------------------- Lecture 26 / HW10: convolution
def circ(x, h, N):
    xz, hz = np.pad(x, (0, N - len(x))), np.pad(h, (0, N - len(h)))
    return np.array([sum(xz[m] * hz[(n - m) % N] for m in range(N)) for n in range(N)])


x, h = np.array([3, 1, 0, -1]), np.array([5, 1, -1, 4])
ok(list(np.convolve(x, h)) == [15, 8, -2, 6, 3, 1, -4], "notes: {3,1,0,-1} * {5,1,-1,4} = {15,8,-2,6,3,1,-4}")
ok(list(circ(x, h, 4)) == [18, 9, -6, 6], "notes: 4-point circular = {18,9,-6,6}")
ok(list(circ(x, h, 7)) == list(np.convolve(x, h)), "notes: 7-point circular = linear")
x, h = np.array([1, 2, 3, 4]), np.array([-1, 1, -2, 2])
y = np.convolve(x, h)
ok(list(y) == [-1, -1, -3, -3, 2, -2, 8], "slides: {1,2,3,4} * {-1,1,-2,2} = {-1,-1,-3,-3,2,-2,8}")
ok(list(circ(x, h, 4)) == [1, -3, 5, -3] and [y[0] + y[4], y[1] + y[5], y[2] + y[6], y[3]] == [1, -3, 5, -3],
   "slides: 4-point circular = {1,-3,5,-3} = linear with the tail wrapped")
ok(list(circ(x, h, 7)) == list(y), "slides: 7-point circular = linear")
for M in (7, 8):
    r = np.fft.ifft(np.fft.fft(x, M) * np.fft.fft(h, M)).real
    ok(close(r[:7], y) and close(r[7:], 0), f"IFFT(FFT * FFT) with M = {M} = linear convolution")
ok(8 + 5 - 1 == 12 and 2 ** math.ceil(math.log2(12)) == 16, "N = 8, L = 5: pad to 12, or to 16 for a radix-2 FFT")
cost = lambda N: (N * N, 3 * (2 * N) * math.log2(2 * N) + 2 * N)
ok(cost(16)[0] < cost(16)[1] and cost(32)[0] < cost(32)[1] and cost(64)[0] > cost(64)[1] and cost(1024)[0] / cost(1024)[1] > 15,
   f"rough count N^2 vs 3M log2 M + M (M = 2N): N=16 {cost(16)}, 32 {cost(32)}, 64 {cost(64)}, 1024 ratio {cost(1024)[0] / cost(1024)[1]:.1f}")

# HW10 #2 and #3
x, h = np.array([1, 2, 3, 4, 5]), np.array([1, 1])
ok(list(np.convolve(x, h)) == [1, 3, 5, 7, 9, 5], "HW10 #2(a): x * h = {1,3,5,7,9,5}")
ok(list(circ(x, h, 5)) == [6, 3, 5, 7, 9], "HW10 #2(b): 5-point circular = {6,3,5,7,9}")
ok(list(circ(x, h, 6)) == [1, 3, 5, 7, 9, 5] and list(circ(x, h, 5)) != [1, 3, 5, 7, 9], "HW10 #2(c): N = 6 is the smallest")
ok(47 + 33 - 1 == 79 and (79 - 47, 79 - 33) == (32, 46), "HW10 #3(a): N = 79, zeros 32 and 46")
ok(2 ** 6 < 79 <= 2 ** 7 and (128 - 47, 128 - 33) == (81, 95), "HW10 #3(b): N = 128, zeros 81 and 95")
x, h = rng.standard_normal(47), rng.standard_normal(33)
y = np.convolve(x, h)
xf, hf = np.concatenate([np.zeros(32), x]), np.concatenate([np.zeros(46), h])
r = np.fft.ifft(np.fft.fft(xf) * np.fft.fft(hf)).real
ok(close(y, np.roll(r, 1), 1e-9) and close(y[0], r[78], 1e-9) and close(y[1:], r[:78], 1e-9),
   "HW10 #3(c): zeros in front -> result is y shifted by 78 = -1 (mod 79); y[n] = r[(n-1) mod 79]")

# ---------------------------------------------------------------- Lecture 27: ideal filters and specifications
wc = PI / 4
w = np.linspace(-PI, PI, 400001)
Hd = (np.abs(w) <= wc).astype(float)
for n in (0, 1, 3, 4, 7):
    num = np.trapezoid(Hd * np.exp(1j * w * n), w).real / (2 * PI)
    exact = wc / PI if n == 0 else math.sin(wc * n) / (PI * n)
    ok(abs(num - exact) < 2e-5, f"ideal low-pass h[{n}] = sin(wc n)/(pi n) = {exact:.4f}")
part = [sum(abs(math.sin(wc * n) / (PI * n)) for n in range(1, N + 1)) for N in (10 ** 2, 10 ** 4, 10 ** 6)]
ok(part[1] - part[0] > 0.85 and part[2] - part[1] > 0.85, f"sum |h[n]| keeps growing (by about 0.9 per factor of 100 in N): {part[0]:.2f}, {part[1]:.2f}, {part[2]:.2f}")
n = np.arange(-400, 401)
hl = np.where(n == 0, wc / PI, np.sin(wc * n) / (PI * np.where(n == 0, 1, n)))
dtft = lambda hh, om: np.sum(hh * np.exp(-1j * om * n)).real
hh = -hl.copy()
hh[n == 0] += 1
ok(abs(dtft(hh, 0.0)) < 0.01 and abs(dtft(hh, 3.0) - 1) < 0.01, "delta[n] - h_lpf[n] is high-pass: H(0) = 0, H(3) = 1")
hb = np.cos(PI / 2 * n) * hl
ok(abs(dtft(hb, PI / 2) - 0.5) < 0.01 and abs(dtft(hb, 0.0)) < 0.01 and abs(dtft(2 * hb, PI / 2) - 1) < 0.02,
   "cos(w0 n) h_lpf[n] is band-pass of height 1/2 at w0; 2cos(w0 n) h_lpf[n] has height 1")
ok(abs(20 * math.log10(0.1) + 20) < 1e-12 and abs(20 * math.log10(0.01) + 40) < 1e-12 and abs(10 ** (-23 / 20) - 0.0708) < 1e-4
   and abs(20 * math.log10(1e-5) + 100) < 1e-9, "-20 dB = 1/10, -40 dB = 1/100, -23 dB = 0.0708, -100 dB = 1e-5")
ok(abs(20 * math.log10(1.2) - 1.58) < 0.01 and abs(20 * math.log10(0.8) + 1.94) < 0.01, "gain 1.2 = +1.58 dB, gain 0.8 = -1.94 dB")
ok(close(2 * PI * 200 / 4000, PI / 10) and close(2 * PI * 300 / 4000, 3 * PI / 20) and close(3 * PI / 20 - PI / 10, PI / 20),
   "Example 1(a): ws = pi/10, wp = 3pi/20, transition bandwidth pi/20")
w0 = 2 * PI * 60 / 480
ok(close(w0, PI / 4) and close(w0 - PI / 12, PI / 6) and close(w0 + PI / 12, PI / 3) and close(PI / 6 * 480 / (2 * PI), 40)
   and close(PI / 3 * 480 / (2 * PI), 80), "Example 1(b): hum at pi/4; passband edges pi/6 (40 Hz) and pi/3 (80 Hz)")
sp = figs.lpf_specs(figs.truncated_lpf(**figs.SPEC_FILTER))
print(f"     filter-specs figure: dp = {sp['dp']:.4f}, As = {sp['As']:.4f} = {20 * math.log10(sp['As']):.2f} dB, "
      f"wp = {sp['wp'] / PI:.4f} pi, ws = {sp['ws'] / PI:.4f} pi, bandwidth {(sp['ws'] - sp['wp']) / PI:.4f} pi")
ok(abs(sp["dp"] - 0.088) < 0.002 and abs(20 * math.log10(sp["As"]) + 20.4) < 0.1 and abs(sp["wp"] / PI - 0.386) < 0.002
   and abs(sp["ws"] / PI - 0.488) < 0.002, "filter-specs figure values as quoted on the page")


# ---------------------------------------------------------------- Lecture 27: direct forms
def lccde(b, c, x):
    y = np.zeros(len(x))
    for n in range(len(x)):
        y[n] = sum(c[j] * x[n - j] for j in range(len(c)) if n - j >= 0) + sum(b[i - 1] * y[n - i] for i in range(1, len(b) + 1) if n - i >= 0)
    return y


def df2(b, c, x):
    D = max(len(b), len(c) - 1)
    v = np.zeros(D + 1)                      # v[0] = v[n], v[i] = v[n-i]
    y = np.zeros(len(x))
    for n in range(len(x)):
        v[1:] = v[:-1].copy()
        v[0] = x[n] + sum(b[i - 1] * v[i] for i in range(1, len(b) + 1))
        y[n] = sum(c[j] * v[j] for j in range(len(c)))
    return y


x = rng.standard_normal(60)
for b, c, name in (([0.5, -0.3, 0.1], [1.0, 2.0, -1.0, 0.5], "general K = 3, M = 4"), ([0, 1, -2], [3, -1, 2], "Example 2")):
    ya, yb_ = lccde(b, c, x[:25]), df2(b, c, x[:25])
    ok(np.allclose(ya, yb_, rtol=1e-9, atol=1e-6), f"direct form II computes the same output as the LCCDE ({name})")
ok((3 + 4, 3 + 3, 3 + 3) == (7, 6, 6) and max(3, 3) == 3, "K = 3, M = 4: 7 multiplies, 6 additions, DF-I 6 delays, DF-II 3 delays")
# Example 2: H(z) = (3 - z^-1 + 2 z^-2) / (1 - z^-2 + 2 z^-3): impulse response from both
imp = np.zeros(12)
imp[0] = 1
hI = lccde([0, 1, -2], [3, -1, 2], imp)
ok(list(hI[:6]) == [3, -1, 5, -7, 7, -17], f"Example 2 impulse response starts {[int(v) for v in hI[:6]]}")
ok(max(abs(np.roots([1, 0, -1, 2]))) > 1, f"Example 2 has a pole outside the unit circle (|p| max = {max(abs(np.roots([1, 0, -1, 2]))):.3f}): not stable")

# ---------------------------------------------------------------- remaining numbers quoted on the pages
ok(list(hI[:6]) == [3, -1, 5, -7, 7, -17] and abs(np.roots([1, 0, -1, 2])[0].real + 1.5214) < 1e-3, "Example 2: real pole at z = -1.52")
ya, yb_ = lccde([0.25, -0.125], [2, 0, -1], x[:25]), df2([0.25, -0.125], [2, 0, -1], x[:25])
ok(np.allclose(ya, yb_), "reading example: v = x + v1/4 - v2/8, y = 2v - v2  <=>  y = y1/4 - y2/8 + 2x - x2")
ok(100 + 30 - 1 == 129 and (129 - 100, 129 - 30) == (29, 99) and 2 ** 7 < 129 <= 2 ** 8 and (256 - 100, 256 - 30, 256 - 129) == (156, 226, 127),
   "practice: 100 and 30 samples -> 129: zeros 29 and 99; radix-2: 256: zeros 156 and 226, 127 trailing zeros")
ok(3 * 2048 * 11 + 2048 == 69632 and 3 * 32 * 5 + 32 == 512 and 3 * 64 * 6 + 64 == 1216 and 3 * 128 * 7 + 128 == 2816, "rough FFT-route counts 512, 1216, 2816, 69632")
ok(15 + 8 - 1 == 22 and (22 - 15, 22 - 8, 32 - 15, 32 - 8) == (7, 14, 17, 24), "FA2019 MT2 #11: 22 -> zeros 7 and 14; 32 -> 17 and 24")
# Lecture 24 numbers
ok(abs(4096 / 48000 - 0.0853) < 1e-4 and abs((4096 - 1365) / 48000 - 0.0569) < 1e-4 and round(4096 / 3) == 1365, "guitar: 4096/48000 = 0.085 s, overlap 0.057 s, S = L/3 = 1365")
ok(0.05 * 10000 == 500 and 2 * 10000 / 500 == 40 and 10000 / 500 == 20 and abs(293.66 - 261.63 - 32.03) < 1e-9 and 624 < 2 * 10000 / 32.03 < 625
   and abs(625 / 10000 - 0.0625) < 1e-12 and 0.5 / 0.0625 == 8, "piano: L = 500; full-lobe 40 Hz, half-lobe 20 Hz; C4-D4 32 Hz -> L > 624 (62.5 ms, 8 windows)")
ok(4 * 2000 / 64 == 125 and abs(4 * 2000 / 1024 - 7.8125) < 1e-9 and 64 / 2000 == 0.032 and 1024 / 2000 == 0.512, "spectrogram figure: Hamming lobe 125 Hz (L = 64) and 7.8 Hz (L = 1024)")
ok(abs(20 * math.log10(0.5) + 6.02) < 0.01, "-6 dB = 0.501")

print(f"\nALL OK ({n_checks} checks)")
