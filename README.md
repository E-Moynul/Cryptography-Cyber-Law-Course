# CT #1: Practicing Number Theory

**Name:** Sikder Moynul Hasan
**Student ID:** IT23017

## 📌 Overview
This repository contains the Python implementation of foundational Number Theory algorithms. The code covers the Extended Euclidean Algorithm, Diophantine equations, Modular Inverses, Fast Modular Exponentiation, and the Chinese Remainder Theorem.

---

## 🧮 1. Extended Euclid's Algorithm
The Extended Euclidean Algorithm finds the greatest common divisor (GCD) of two integers $a$ and $b$ along with the coefficients $x$ and $y$ (Bézout's identity) such that:
$$a \cdot x + b \cdot y = \gcd(a, b)$$

```python
def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    return d, y1, x1 - (a // b) * y1
```

🔄 2. Least Common Multiple (LCM)The relationship between GCD and LCM for two numbers $a$ and $b$ is given by:
$$ \text{LCM}(a, b) = \frac{|a \cdot b|}{\gcd(a, b)} $$⚖️ 3. Linear Diophantine EquationA Linear Diophantine equation takes the form:
$$ a \cdot x + b \cdot y = c $$
A solution exists if and only if $\gcd(a, b)$ divides $c$. We scale the outputs of the Extended Euclidean algorithm by $\frac{c}{\gcd(a, b)}$.➗ 4. Modular Division and InverseTo perform modular division $\frac{b}{a} \pmod n$, we first find the modular inverse of $a$ modulo $n$. The inverse $x$ satisfies:
$$ a \cdot x \equiv 1 \pmod n $$
Once the inverse is found, the division is computed as:
$$ x_{div} = (b \cdot a^{-1}) \pmod n $$⚡ 5. Fast Modular ExponentiationInstead of computing $b^e$ and then taking the modulo (which is computationally expensive), we use binary exponentiation to efficiently compute:
$$ b^e \pmod m $$
This runs in $O(\log e)$ time complexity.🇨🇳 6. Chinese Remainder TheoremGiven pairwise coprime moduli $n_1, n_2$ and remainders $r_1, r_2$, CRT finds a unique solution $x \pmod{n_1 \cdot n_2}$ to the system of congruences:
$$ x \equiv r_1 \pmod{n_1} $$
$$ x \equiv r_2 \pmod{n_2} $$
Using coefficients from the Extended GCD where $n_1 \cdot x + n_2 \cdot y = 1$, the solution is formed as:
$$ X = (r_2 \cdot n_1 \cdot x + r_1 \cdot n_2 \cdot y) \pmod{n_1 \cdot n_2} $$Practiced and implemented on Jupyter/Google Colab.
