<div align="center">

# 🔐 Number Theory Toolkit for Cryptography

**A single-file Python library of the core number theory algorithms and theorems used in cryptography.**

</div>

---

## 📋 Course Information

| | |
|---|---|
| **Assignment** | CT #1: Practicing Number Theory |
| **Name** | Sikder Moynul Hasan |
| **Student ID** | IT23017 |
| **Platform** | Python 3.8+ |

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Quick Start](#-quick-start)
- [Function Reference](#-function-reference)
  - [1. GCD, LCM and Extended Euclid](#1-gcd-lcm-and-extended-euclid)
  - [2. Modular Arithmetic](#2-modular-arithmetic)
  - [3. Chinese Remainder Theorem](#3-chinese-remainder-theorem)
  - [4. Primes and Factorization](#4-primes-and-factorization)
  - [5. Euler's Functions and Theorems](#5-eulers-functions-and-theorems)
  - [6. Group Structure](#6-group-structure)
  - [7. Quadratic Residues](#7-quadratic-residues)
  - [8. Discrete Logarithm](#8-discrete-logarithm)
  - [9. Cryptosystem Demos](#9-cryptosystem-demos)
- [Sample Output](#-sample-output)
- [Notes and Limitations](#-notes-and-limitations)

---

## 🔎 Overview

This project implements the fundamental number theory building blocks behind modern cryptography, from the Euclidean algorithm to RSA, Diffie-Hellman and ElGamal. It is written for **learning and experimentation** and uses **only the Python standard library**.

## ⚙️ Requirements

- Python **3.8+** (uses `math.isqrt` and `pow(g, -m, p)`)
- No third-party packages

## 🚀 Quick Start

Run the built-in demo and self-checks:

```bash
python number_theory.py
```

Use the functions in your own code:

```python
from number_theory import *

print(gcd(48, 18))                    # 6
print(modinv(3, 11))                  # 4
print(crt([2, 3, 2], [3, 5, 7]))      # (23, 105)
print(is_prime(2**61 - 1))            # True
print(factorize_fast(10403031209))    # {103: 1, 101: 1, 1000003: 1}

pub, priv, (p, q) = rsa_keygen(512)
c = rsa_encrypt(123456789, pub)
print(rsa_decrypt(c, priv))           # 123456789
```

---

## 📚 Function Reference

### 1. GCD, LCM and Extended Euclid

| Function | Description |
|---|---|
| `gcd(a, b)` | Euclidean algorithm |
| `lcm(a, b)` | Least common multiple |
| `egcd(a, b)` | Returns `(g, x, y)` with `a*x + b*y = g` (Bézout's identity); works for any order of `a, b` |
| `extended_gcd(a, b)` | Recursive version with built-in assertions (requires `a >= b >= 0`) |
| `diophantine(a, b, c)` | One solution `(x, y)` of `a*x + b*y = c` |

### 2. Modular Arithmetic

| Function | Description |
|---|---|
| `modinv(a, m)` / `modInverse(a, n)` | Modular inverse via extended Euclid |
| `divide(b, a, n)` | Modular division `b / a (mod n)` |
| `modpow(b, e, m)` / `FastModularExponentiation(b, e, m)` | Square-and-multiply (same result as the built-in `pow(b, e, m)`) |
| `solve_linear_congruence(a, b, m)` | All solutions of `a*x ≡ b (mod m)` |

### 3. Chinese Remainder Theorem

| Function | Description |
|---|---|
| `crt(remainders, moduli)` | General CRT for pairwise-coprime moduli; returns `(x, M)` |
| `ChineseRemainderTheorem(n1, r1, n2, r2)` | Two-congruence version (requires `gcd(n1, n2) = 1`) |

### 4. Primes and Factorization

| Function | Description |
|---|---|
| `sieve(n)` | Sieve of Eratosthenes: all primes ≤ `n` |
| `factorize(n)` | Trial-division factorization → `{prime: exponent}` |
| `pollard_rho(n)` | Finds a non-trivial factor (Pollard's rho) |
| `factorize_fast(n)` | Full factorization using Miller-Rabin + Pollard's rho |
| `fermat_test(n, k)` | Fermat primality test (fooled by Carmichael numbers such as 561) |
| `is_prime(n)` | Miller-Rabin (deterministic for n < 3.3·10²⁴, probabilistic beyond) |
| `gen_prime(bits)` | Random prime of the given bit length |

### 5. Euler's Functions and Theorems

| Function | Description |
|---|---|
| `phi(n)` | Euler's totient φ(n) |
| `carmichael(n)` | Carmichael function λ(n) |
| `fermat_little(a, p)` | Checks Fermat's little theorem: `a^(p-1) ≡ 1 (mod p)` |
| `euler_theorem(a, n)` | Checks Euler's theorem: `a^φ(n) ≡ 1 (mod n)` |
| `wilson(p)` | Checks Wilson's theorem: `(p-1)! ≡ -1 (mod p)` |

### 6. Group Structure

| Function | Description |
|---|---|
| `order(a, n)` | Multiplicative order of `a` modulo `n` |
| `primitive_root(p)` | Smallest primitive root (generator) of a prime `p` |

### 7. Quadratic Residues

| Function | Description |
|---|---|
| `legendre(a, p)` | Legendre symbol via Euler's criterion (`1`, `-1` or `0`) |
| `jacobi(a, n)` | Jacobi symbol (odd positive `n`) |
| `tonelli_shanks(n, p)` | Modular square root: solves `x² ≡ n (mod p)` |

### 8. Discrete Logarithm

| Function | Description |
|---|---|
| `bsgs(g, h, p)` | Baby-step Giant-step: solves `g^x ≡ h (mod p)` in O(√p) |

### 9. Cryptosystem Demos

| Function | Description |
|---|---|
| `rsa_keygen(bits)` | Returns `(public, private, (p, q))` with `e = 65537` and `d` computed from λ(n) |
| `rsa_encrypt(m, pub)` / `rsa_decrypt(c, priv)` | Textbook RSA |
| `rsa_decrypt_crt(c, d, p, q)` | Faster RSA decryption using the CRT |
| `diffie_hellman(p, g)` | Simulates a key exchange and returns both shared secrets (they match) |
| `elgamal_encrypt(m, p, g, y)` / `elgamal_decrypt(c1, c2, x, p)` | Textbook ElGamal |

---

## 🖥️ Sample Output

```text
gcd(48,18) = 6 | lcm = 144
modinv(3, 11) = 4
14x ≡ 30 (mod 100): [45, 95]
CRT x≡2(3), 3(5), 2(7): (23, 105)
Miller-Rabin(2**61-1): True
phi(36) = 12 | carmichael(36) = 6
primitive_root(23) = 5
sqrt(10) mod 13 = 7 (check: 10)
RSA decrypt ok: True | CRT decrypt ok: True
Diffie-Hellman shared secrets equal: True
ElGamal decrypt: 100
```

---

## ⚠️ Notes and Limitations

- `lcm` and `gcd` appear in two styles (`math.gcd`-based and hand-written). The later definition in the file overrides the earlier one with identical behavior.
- `extended_gcd` and `modInverse` follow a course-style implementation with assertions, while `egcd` and `modinv` are the more general versions. Prefer the latter in new code.
- `tonelli_shanks` and `legendre` require an odd prime modulus.
- `bsgs` needs `gcd(g, p) = 1`. Runtime and memory grow as √p, so it is only practical for small primes.
- RSA here is **textbook RSA**: always use OAEP/PSS padding in real applications.
