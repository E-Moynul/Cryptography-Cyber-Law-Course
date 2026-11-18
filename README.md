# CT #1: Practicing Number Theory

**Name:** Sikder Moynul Hasan
<br>
**Student ID:** IT23017

# Number Theory Toolkit for Cryptography

A single-file Python library implementing the core number theory algorithms and theorems used in cryptography, written for learning and experimentation. It uses **only the Python standard library**.

## Requirements

- Python **3.8+** (uses `math.isqrt` and `pow(g, -m, p)`)
- No third-party packages

## Quick start

```bash
python number_theory.py        # runs the built-in demo / self-checks
```

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

## Contents

### 1. GCD, LCM and Extended Euclid
| Function | Description |
|---|---|
| `gcd(a, b)` | Euclidean algorithm |
| `lcm(a, b)` | Least common multiple |
| `egcd(a, b)` | Returns `(g, x, y)` with `a*x + b*y = g` (Bézout's identity), works for any order of `a, b` |
| `extended_gcd(a, b)` | Recursive version with built-in assertions (requires `a >= b >= 0`) |
| `diophantine(a, b, c)` | One solution `(x, y)` of `a*x + b*y = c` |

### 2. Modular arithmetic
| Function | Description |
|---|---|
| `modinv(a, m)` / `modInverse(a, n)` | Modular inverse via extended Euclid |
| `divide(b, a, n)` | Modular division `b / a (mod n)` |
| `modpow(b, e, m)` / `FastModularExponentiation(b, e, m)` | Square-and-multiply (same result as built-in `pow(b, e, m)`) |
| `solve_linear_congruence(a, b, m)` | All solutions of `a*x ≡ b (mod m)` |

### 3. Chinese Remainder Theorem
| Function | Description |
|---|---|
| `crt(remainders, moduli)` | General CRT for pairwise-coprime moduli; returns `(x, M)` |
| `ChineseRemainderTheorem(n1, r1, n2, r2)` | Two-congruence version (requires `gcd(n1, n2) = 1`) |

### 4. Primes and factorization
| Function | Description |
|---|---|
| `sieve(n)` | Sieve of Eratosthenes, all primes ≤ `n` |
| `factorize(n)` | Trial-division factorization → `{prime: exponent}` |
| `pollard_rho(n)` | Finds a non-trivial factor (Pollard's rho) |
| `factorize_fast(n)` | Full factorization using Miller-Rabin + Pollard's rho |
| `fermat_test(n, k)` | Fermat primality test (fooled by Carmichael numbers like 561) |
| `is_prime(n)` | Miller-Rabin (deterministic for n < 3.3·10²⁴, probabilistic beyond) |
| `gen_prime(bits)` | Random prime of the given bit length |

### 5. Euler's functions and theorems
| Function | Description |
|---|---|
| `phi(n)` | Euler's totient φ(n) |
| `carmichael(n)` | Carmichael function λ(n) |
| `fermat_little(a, p)` | Checks `a^(p-1) ≡ 1 (mod p)` |
| `euler_theorem(a, n)` | Checks `a^φ(n) ≡ 1 (mod n)` |
| `wilson(p)` | Checks `(p-1)! ≡ -1 (mod p)` |

### 6. Group structure
| Function | Description |
|---|---|
| `order(a, n)` | Multiplicative order of `a` modulo `n` |
| `primitive_root(p)` | Smallest primitive root (generator) of prime `p` |

### 7. Quadratic residues
| Function | Description |
|---|---|
| `legendre(a, p)` | Legendre symbol via Euler's criterion (`1`, `-1`, `0`) |
| `jacobi(a, n)` | Jacobi symbol (odd positive `n`) |
| `tonelli_shanks(n, p)` | Modular square root: `x² ≡ n (mod p)` |

### 8. Discrete logarithm
| Function | Description |
|---|---|
| `bsgs(g, h, p)` | Baby-step Giant-step: solves `g^x ≡ h (mod p)` in O(√p) |

### 9. Cryptosystem demos
| Function | Description |
|---|---|
| `rsa_keygen(bits)` | Returns `(public, private, (p, q))`, with e = 65537 and d computed from λ(n) |
| `rsa_encrypt(m, pub)` / `rsa_decrypt(c, priv)` | Textbook RSA |
| `rsa_decrypt_crt(c, d, p, q)` | Faster RSA decryption using CRT |
| `diffie_hellman(p, g)` | Simulates a key exchange, returns both shared secrets (they match) |
| `elgamal_encrypt(m, p, g, y)` / `elgamal_decrypt(c1, c2, x, p)` | Textbook ElGamal |

## Sample output

```
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

## Notes and limitations

- `lcm` and `gcd` appear in two styles (`math.gcd`-based and hand-written); the later definition in the file overrides the earlier one with identical behavior.
- `extended_gcd` and `modInverse` follow a course-style implementation with assertions, while `egcd` and `modinv` are the more general versions. Prefer the latter in new code.
- `tonelli_shanks` and `legendre` require an odd prime modulus.
- `bsgs` needs `gcd(g, p) = 1`; runtime and memory grow as √p, so it is only practical for small primes.
- RSA here is **textbook RSA**: always use OAEP/PSS padding in real applications.


