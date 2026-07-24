#advanced-cryptography #third-semester 

# Polynomial Arithmetic & Galois Field (Short Complete Notes)

Think of this as the **math behind AES and many cryptographic algorithms**.

---

# 1. What is a Polynomial?

A **polynomial** is an algebraic expression made of variables and coefficients.

Example:

$$
P(x)=x^3+2x^2+5x+1
$$

Here,

* Variable = $x$
* Coefficients = 1, 2, 5, 1
* Highest power = 3

---

# 2. Degree of a Polynomial

The **degree** is the highest exponent of the variable.

Examples

| Polynomial    | Degree |
| ------------- | ------ |
| $$x+1$$       | 1      |
| $$x^2+x+1$$   | 2      |
| $$x^5+x^2+1$$ | 5      |

---

# 3. Polynomial Arithmetic

Just like integers, polynomials can be:

* Added
* Subtracted
* Multiplied
* Divided

---

# 4. Polynomial Addition

Normal Mathematics

$$
(x^2+x+1)+(x^2+2)=2x^2+x+3
$$

---

## In Cryptography (GF(2))

Coefficients are only:

$$
0,;1
$$

Addition is **XOR**.

Rules:

```text
0+0=0

0+1=1

1+0=1

1+1=0
```

Notice

$$
1+1=0
$$

This is the biggest difference from normal arithmetic.

---

### Example

$$
(x^2+x+1)+(x^2+1)
$$

Combine like terms.

$$
x^2+x^2+x+1+1
$$

Using XOR

$$
x^2+x^2=0
$$

$$
1+1=0
$$

Answer

$$
x
$$

---

# 5. Polynomial Subtraction

In **GF(2)**,

Subtraction is exactly the same as addition.

Because

$$
1-1=0
$$

which is equivalent to XOR.

So

$$
A-B=A+B
$$

---

# 6. Polynomial Multiplication

Multiply just like algebra.

Example

$$
(x+1)(x+1)
$$

Expand

$$
x^2+x+x+1
$$

Since

$$
x+x=0
$$

Answer

$$
x^2+1
$$

---

# 7. Polynomial Division

Exactly like long division in school.

Example

Divide

$$
x^3+x+1
$$

by

$$
x+1
$$

You repeatedly divide the highest powers until the remainder degree is smaller than the divisor.

In cryptography, **only the remainder is usually important**.

---

# 8. Modulo Polynomial

Just like

$$
17 \bmod 5=2
$$

we also do

$$
P(x)\bmod Q(x)
$$

The answer is the **remainder** after polynomial division.

AES constantly performs polynomial modulo operations.

---

# 9. Irreducible Polynomial

An **irreducible polynomial** cannot be factored into smaller polynomials over the same field.

It is similar to a **prime number**.

Example

Prime number

$$
13
$$

cannot be divided.

Similarly,

$$
x^8+x^4+x^3+x+1
$$

is an irreducible polynomial used in AES.

---

# 10. What is a Galois Field?

A **Galois Field (GF)** is a **finite set of numbers** where arithmetic is performed.

Notation

$$
GF(p^n)
$$

where

* $p$ = Prime
* $n$ = Positive integer

---

# Example

$$
GF(2)
$$

Contains only

$$
{0,1}
$$

Operations are modulo 2.

---

# 11. GF(2)

Only two values exist.

```text
0

1
```

Addition

```text
0+0=0

0+1=1

1+1=0
```

Multiplication

```text
0×1=0

1×1=1
```

---

# 12. GF(2⁸)

AES works in

$$
GF(2^8)
$$

Meaning

There are

$$
2^8=256
$$

possible values.

Every byte (8 bits) represents one field element.

---

# 13. Why Does AES Use Polynomials?

AES treats every byte as a polynomial.

Example

Byte

```text
10110011
```

represents

$$
x^7+x^5+x^4+x+1
$$

AES performs

* XOR
* Polynomial multiplication
* Polynomial modulo

instead of normal arithmetic.

---

# 14. Why Use Galois Fields?

They make cryptographic operations:

* Fast
* Efficient
* Reversible
* Mathematically secure

---

# Relationship Between All Concepts

```text
Numbers
    │
    ▼
Integers
    │
    ▼
Modulo Arithmetic
    │
    ▼
Finite Field (GF)
    │
    ▼
Polynomial Arithmetic
    │
    ▼
GF(2)
    │
    ▼
GF(2⁸)
    │
    ▼
AES
```

---

# Difference Between Normal Math and GF(2)

| Normal Math        | GF(2)                     |
| ------------------ | ------------------------- |
| Digits 0–9         | Only 0 and 1              |
| $1+1=2$            | $1+1=0$                   |
| Normal addition    | XOR                       |
| Normal subtraction | XOR                       |
| Multiplication     | Polynomial multiplication |
| Division           | Polynomial division       |

---

# Memory Tricks

### Polynomial

```text
x³+x+1
```

Highest power = Degree

---

### GF

```text
GF(2)

↓

0,1 only
```

---

### Addition

```text
1+1=0
```

Think **XOR**.

---

### Irreducible Polynomial

Think:

```text
Prime Number

↓

Prime Polynomial
```

---

### AES

Remember:

```text
Byte

↓

Polynomial

↓

GF(2⁸)

↓

Modulo Polynomial

↓

AES Encryption
```

---

# One-Line Summary

* **Polynomial** → Algebraic expression like $x^3+x+1$.
* **Polynomial Arithmetic** → Addition, subtraction, multiplication, and division of polynomials.
* **GF(2)** → Arithmetic with only 0 and 1, where addition is XOR.
* **Irreducible Polynomial** → A polynomial that cannot be factored, like a prime number.
* **GF(2^8)** → A finite field with 256 elements, used by AES.
* **AES** → Represents bytes as polynomials and performs arithmetic in $GF(2^8)$ using an irreducible polynomial.
