import math

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
    ans = (r2 * n1 * x + r1 * n2 * y) % (n1 * n2)
    return (ans + (n1 * n2)) % (n1 * n2)
