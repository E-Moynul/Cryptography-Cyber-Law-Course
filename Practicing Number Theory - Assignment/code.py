
import math
import random
from functools import reduce

# 1. Extended Euclid's Algorithm
def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        d1, x1, y1 = extended_gcd(b, a % b)
        d = d1
        x = y1
        y = x1 - (a // b) * y1
    
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

# 2. LCM
def lcm(a, b):
    return (a * b) // math.gcd(a, b)

# 3. Diophantine Equations
def diophantine(a, b, c):
    if a >= b:
        gcd, x_temp, y_temp = extended_gcd(a, b)
        x = x_temp * (c // gcd)
        y = y_temp * (c // gcd)
    else:
        gcd, y_temp, x_temp = extended_gcd(b, a)
        x = x_temp * (c // gcd)
        y = y_temp * (c // gcd)
        
    assert c % gcd == 0
    assert a * x + b * y == c
    return (x, y)

# 4. Modular Inverse and Division
def modInverse(a, n):
    if n >= a:
        d, y, x = extended_gcd(n, a)
    else:
        d, x, y = extended_gcd(a, n)
    return (x % n + n) % n

def divide(b, a, n):
    assert n > 1 and a > 0
    aInv = modInverse(a, n)
    assert (a * aInv) % n == 1
    return (aInv * b) % n

# 5. Fast Modular Exponentiation
def FastModularExponentiation(b, e, m):
    res = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            res = (res * b) % m
        b = (b * b) % m
        e = e // 2
    return res

# 6. Chinese Remainder Theorem
def ChineseRemainderTheorem(n1, r1, n2, r2):
    if n1 >= n2:
        (d, x, y) = extended_gcd(n1, n2)
    else:
        (d, y, x) = extended_gcd(n2, n1)
        
    assert d == 1













# ---------------------------------------------------------------
# 1. GCD, LCM, Extended Euclidean (Bezout's identity)
# ---------------------------------------------------------------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def egcd(a, b):
    """returns (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


# ---------------------------------------------------------------
# 2. Modular inverse, Modular exponentiation
# ---------------------------------------------------------------
def modinv(a, m):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        raise ValueError("gcd(a, m) != 1")
    return x % m


def modpow(base, exp, mod):
    """Square-and-multiply (built-in pow(base, exp, mod) )"""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result


# ---------------------------------------------------------------
# 3. Linear congruence: a*x ≡ b (mod m)
# ---------------------------------------------------------------
def solve_linear_congruence(a, b, m):
    g = gcd(a, m)
    if b % g != 0:
        return []
    a1, b1, m1 = a // g, b // g, m // g
    x0 = (modinv(a1, m1) * b1) % m1
    return [x0 + i * m1 for i in range(g)]


# ---------------------------------------------------------------
# 4. Chinese Remainder Theorem
# ---------------------------------------------------------------
def crt(remainders, moduli):
    """x ≡ r_i (mod m_i), m_i pairwise coprime. returns (x, M)"""
    M = reduce(lambda a, b: a * b, moduli)
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        x += r * Mi * modinv(Mi, m)
    return x % M, M


# ---------------------------------------------------------------
# 5. Prime generation: Sieve, Trial division
# ---------------------------------------------------------------
def sieve(n):
    """Sieve of Eratosthenes"""
    is_p = [True] * (n + 1)
    is_p[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return [i for i, v in enumerate(is_p) if v]


def factorize(n):
    """Trial division factorization -> {prime: exponent}"""
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


# ---------------------------------------------------------------
# 6. Primality tests: Fermat, Miller-Rabin
# ---------------------------------------------------------------
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def fermat_test(n, k=10):
    if n < 4:
        return n in (2, 3)
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def is_prime(n, k=20):
    """Miller-Rabin primality test"""
    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = SMALL_PRIMES if n < 3317044064679887385961981 else \
        [random.randrange(2, n - 1) for _ in range(k)]
    for a in bases:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def gen_prime(bits):

    while True:
        n = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(n):
            return n


# ---------------------------------------------------------------
# 7. Pollard's rho factorization
# ---------------------------------------------------------------
def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n
    while True:
        x = random.randrange(2, n)
        y, c, d = x, random.randrange(1, n), 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n:
            return d


def factorize_fast(n):
    if n == 1:
        return {}
    if is_prime(n):
        return {n: 1}
    d = pollard_rho(n)
    f = factorize_fast(d)
    for p, e in factorize_fast(n // d).items():
        f[p] = f.get(p, 0) + e
    return f


# ---------------------------------------------------------------
# 8. Euler's totient, Carmichael lambda
# ---------------------------------------------------------------
def phi(n):
    result = n
    for p in factorize_fast(n):
        result -= result // p
    return result


def carmichael(n):
    """Carmichael function λ(n)"""
    f = factorize_fast(n)
    vals = []
    for p, e in f.items():
        if p == 2 and e >= 3:
            vals.append(2 ** (e - 2))
        else:
            vals.append((p - 1) * p ** (e - 1))
    return reduce(lcm, vals, 1)


# ---------------------------------------------------------------
# 9. Theorem verifiers
# ---------------------------------------------------------------
def fermat_little(a, p):
    """a^(p-1) ≡ 1 (mod p), p prime, gcd(a,p)=1"""
    return pow(a, p - 1, p) == 1


def euler_theorem(a, n):
    """a^φ(n) ≡ 1 (mod n), gcd(a,n)=1"""
    return pow(a, phi(n), n) == 1


def wilson(p):
    """(p-1)! ≡ -1 (mod p) <=> p prime"""
    return math.factorial(p - 1) % p == p - 1


# ---------------------------------------------------------------
# 10. Order, Primitive root
# ---------------------------------------------------------------
def order(a, n):
    """multiplicative order of a mod n"""
    if gcd(a, n) != 1:
        raise ValueError("gcd(a, n) must be 1")
    ph = phi(n)
    o = ph
    for p in factorize_fast(ph):
        while o % p == 0 and pow(a, o // p, n) == 1:
            o //= p
    return o


def primitive_root(p):
  
    if p == 2:
        return 1
    factors = list(factorize_fast(p - 1))
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g


# ---------------------------------------------------------------
# 11. Quadratic residues: Legendre, Jacobi, Euler criterion, Tonelli-Shanks
# ---------------------------------------------------------------
def legendre(a, p):
    """Euler's criterion: a^((p-1)/2) mod p -> 1, -1, 0"""
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


def jacobi(a, n):
    """Jacobi symbol (n odd, positive)"""
    assert n > 0 and n % 2 == 1
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def tonelli_shanks(n, p):
 
    if legendre(n, p) != 1:
        raise ValueError("n quadratic residue নয়")
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while legendre(z, p) != -1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = pow(t2, 2, p)
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r


# ---------------------------------------------------------------
# 12. Discrete logarithm: Baby-step Giant-step
# ---------------------------------------------------------------
def bsgs(g, h, p):
    """"""
    m = math.isqrt(p - 1) + 1
    table = {pow(g, j, p): j for j in range(m)}
    factor = pow(g, -m, p)
    gamma = h
    for i in range(m):
        if gamma in table:
            return i * m + table[gamma]
        gamma = gamma * factor % p
    return None


# ---------------------------------------------------------------
# 13. Applications: RSA
# ---------------------------------------------------------------
def rsa_keygen(bits=512):
    p, q = gen_prime(bits // 2), gen_prime(bits // 2)
    while p == q:
        q = gen_prime(bits // 2)
    n, lam = p * q, lcm(p - 1, q - 1)
    e = 65537
    d = modinv(e, lam)
    return (n, e), (n, d), (p, q)


def rsa_encrypt(m, pub):
    return pow(m, pub[1], pub[0])


def rsa_decrypt(c, priv):
    return pow(c, priv[1], priv[0])


def rsa_decrypt_crt(c, d, p, q):

    mp = pow(c, d % (p - 1), p)
    mq = pow(c, d % (q - 1), q)
    return crt([mp, mq], [p, q])[0]


def diffie_hellman(p, g):
    a, b = random.randrange(2, p - 1), random.randrange(2, p - 1)
    A, B = pow(g, a, p), pow(g, b, p)
    return pow(B, a, p), pow(A, b, p)  


def elgamal_encrypt(m, p, g, y):
    k = random.randrange(2, p - 1)
    return pow(g, k, p), (m * pow(y, k, p)) % p


def elgamal_decrypt(c1, c2, x, p):
    return (c2 * modinv(pow(c1, x, p), p)) % p


# ---------------------------------------------------------------
# DEMO / TESTS
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("gcd(48,18) =", gcd(48, 18), "| lcm =", lcm(48, 18))
    g, x, y = egcd(240, 46)
    print(f"egcd(240,46): {g} = 240*{x} + 46*{y}")
    print("modinv(3, 11) =", modinv(3, 11))
    print("modpow(7, 128, 13) =", modpow(7, 128, 13), "== pow:", pow(7, 128, 13))
    print("14x ≡ 30 (mod 100):", solve_linear_congruence(14, 30, 100))
    print("CRT x≡2(3), 3(5), 2(7):", crt([2, 3, 2], [3, 5, 7]))
    print("Primes <= 50:", sieve(50))
    print("factorize(360):", factorize(360))
    print("Miller-Rabin(2**61-1):", is_prime(2 ** 61 - 1))
    print("Fermat fools Carmichael 561?", fermat_test(561, 20),
          "| Miller-Rabin:", is_prime(561))
    n = 10403 * 1000003
    print(f"pollard factorize({n}):", factorize_fast(n))
    print("phi(36) =", phi(36), "| carmichael(36) =", carmichael(36))
    print("Fermat little (a=5,p=17):", fermat_little(5, 17))
    print("Euler theorem (a=7,n=40):", euler_theorem(7, 40))
    print("Wilson(7):", wilson(7), "| Wilson(9):", wilson(9))
    print("order(2, 11) =", order(2, 11))
    print("primitive_root(23) =", primitive_root(23))
    print("Legendre(2, 7) =", legendre(2, 7), "| Jacobi(5, 21) =", jacobi(5, 21))
    r = tonelli_shanks(10, 13)
    print(f"sqrt(10) mod 13 = {r} (check: {r * r % 13})")
    print("BSGS 3^x ≡ 13 (mod 17): x =", bsgs(3, 13, 17))

    pub, priv, (p, q) = rsa_keygen(512)
    msg = 123456789
    c = rsa_encrypt(msg, pub)
    print("RSA decrypt ok:", rsa_decrypt(c, priv) == msg,
          "| CRT decrypt ok:", rsa_decrypt_crt(c, priv[1], p, q) == msg)

    P = gen_prime(64)
    G = primitive_root(P) if P < 10 ** 6 else 2
    s1, s2 = diffie_hellman(P, G)
    print("Diffie-Hellman shared secrets equal:", s1 == s2)

    P = 467
    G = primitive_root(P)
    xk = 127
    yk = pow(G, xk, P)
    c1, c2 = elgamal_encrypt(100, P, G, yk)
    print("ElGamal decrypt:", elgamal_decrypt(c1, c2, xk, P))
    ans = (r2 * n1 * x + r1 * n2 * y) % (n1 * n2)
    return (ans + (n1 * n2)) % (n1 * n2)
