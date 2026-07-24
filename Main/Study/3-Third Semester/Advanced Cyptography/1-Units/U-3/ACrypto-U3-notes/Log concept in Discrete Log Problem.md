#third-semester #advanced-cryptography #discrete-log-problem

This is one of the most confusing topics in cryptography at first because **the logarithm here is NOT the normal logarithm (like (\log_{10}100=2))**. It is called the **Discrete Logarithm** because we work with **modular arithmetic**.

Let's build the idea from scratch.

---

# Step 1: Recall Normal Logarithm

You already know:

$$
2^3=8
$$

If someone asks

$$
\log_2 8=?
$$

you answer

$$
3
$$

because

> "What power of 2 gives 8?"

Answer:

$$
2^3=8
$$

So a logarithm simply asks:

> **What exponent was used?**

---

# Step 2: Discrete Logarithm

Now we add modular arithmetic.

Suppose

$$
2^n \equiv 9 \pmod{11}
$$

We write

$$
\log_2 9 \pmod{11}
$$

This means

> **Find the exponent (n) such that**

$$
2^n \equiv 9 \pmod{11}
$$

Notice it is **not**

$$
2^n=9
$$

Instead,

$$
2^n \bmod 11=9
$$

---

# Step 3: Solve by Trial

Since exponents are unknown, we simply compute powers of 2 modulo 11.

| n | $$2^n$$ | $$2^n \bmod 11$$ |
| - | ------- | ---------------- |
| 0 | 1       | 1                |
| 1 | 2       | 2                |
| 2 | 4       | 4                |
| 3 | 8       | 8                |
| 4 | 16      | 5                |
| 5 | 32      | 10               |
| 6 | 64      | 9 ✅              |

At

$$
n=6
$$

we get

$$
2^6=64
$$

and

$$
64\bmod11=9.
$$

Therefore,

$$
\boxed{\log_2 9\pmod{11}=6}
$$

---

# Why?

Because

$$
2^6\equiv9\pmod{11}
$$

Exactly like

$$
\log_2 64=6
$$

except now we work **modulo 11**.

---

# Another Example

Find

$$
\log_3 5\pmod7
$$

Meaning,

Find

$$
3^n\equiv5\pmod7.
$$

Make a table.

| n | $$3^n\bmod7$$ |
| - | ------------- |
| 0 | 1             |
| 1 | 3             |
| 2 | 2             |
| 3 | 6             |
| 4 | 4             |
| 5 | 5 ✅           |

Since

$$
3^5\equiv5\pmod7,
$$

the answer is

$$
\boxed{5}
$$

---

# General Method

Given

$$
\log_g X\pmod p
$$

you are really solving

$$
g^n\equiv X\pmod p.
$$

The unknown is **the exponent**.

For small numbers (like in exams):

1. Write powers of (g).
2. Reduce each modulo (p).
3. Stop when you get (X).
4. The exponent is the answer.

---

# Why Is It Called "Discrete"?

Normal logarithms work over continuous real numbers.

Example:

$$
\log_2 7.5
$$

can be computed using a calculator.

Discrete logarithms work only with integers modulo a prime.

Example:

$$
2^n\equiv9\pmod{11}
$$

There is **no simple formula** to find (n). For large primes, the best known algorithms are computationally difficult. This difficulty is known as the **Discrete Logarithm Problem (DLP)**.

---

# Why Is It Important?

Algorithms such as:

* ElGamal Encryption
* ElGamal Digital Signature
* Diffie–Hellman Key Exchange
* Elliptic Curve Cryptography (ECC)

all rely on the fact that:

* Computing

$$
g^x\bmod p
$$

is **easy**.

* Finding

$$
x
$$

from

$$
g^x\bmod p
$$

is **very hard**.

This "easy forward, hard backward" property is what provides security.

---

# Easy Trick for Exams ⭐

Whenever you see

$$
\log_g X\pmod p,
$$

**immediately rewrite it as**

$$
g^n\equiv X\pmod p.
$$

Then make a small table of powers.

For your example,

$$
\log_2 9\pmod{11}
$$

becomes

$$
2^n\equiv9\pmod{11}.
$$

| (n) | (2^n \bmod 11) |
| --- | -------------- |
| 0   | 1              |
| 1   | 2              |
| 2   | 4              |
| 3   | 8              |
| 4   | 5              |
| 5   | 10             |
| 6   | 9 ✅            |

Therefore,

$$
\boxed{\log_2 9\pmod{11}=6.}
$$

This table-based approach is the standard way to solve discrete logarithm questions with small numbers in university exams.
