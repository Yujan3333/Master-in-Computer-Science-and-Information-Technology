#third-semester #advanced-cryptography #elliptic-curve 


# 1. Some Basic Facts of Elliptic Curves

## Definition

An **elliptic curve** is a set of points satisfying the equation

$$[
y^2=x^3+ax+b
]$$

where (a) and (b) are constants.

The curve must satisfy

$$[
4a^3+27b^2\neq0
]$$

Otherwise, the curve has singularities (cusps or self-intersections) and cannot be used in cryptography.

---

## Important Terms

### (a) Point on the curve

Any point ((x,y)) satisfying the equation.

Example

If

$$[
y^2=x^3-x+1
]$$

then every point satisfying this equation lies on the curve.

---

### (b) Point at Infinity ((O))

ECC introduces a special point called the **point at infinity**, denoted by (O).

It acts like **zero** in ordinary arithmetic.

Example:

$$[
P+O=P
]$$

So (O) is the **identity element**.

---

### (c) Inverse of a Point

If

$$[
P=(x,y)
]$$

then

$$[
-P=(x,-y)
]
$$
Graphically, it is the reflection across the x-axis.

Example

$$[
P=(3,5)
]$$

then

$$[
-P=(3,-5)
]$$

---

### (d) Group Property

The points on an elliptic curve form an **Abelian Group**, meaning:

* Closure
* Identity ((O))
* Inverse
* Associative
* Commutative

These properties allow point addition.

---

# 2. Geometry of Elliptic Curves

![Image](https://images.openai.com/static-rsc-4/jhvsWiLX5lymd0J6P7lfEYG2r602C0NsOnaJ7kRS6yt2u97Ueh7GpPqiHURyEwBOT_pb0rlrBGsFW-jYTsz1xOa0Lkn0dqUBz-uexSbFS_8b62ZjOyucITsVDkN900gyqyOW4P-hmKmXofOUaNGCkfYZoQqUdqRcSYFS4aTIWDCPPwlzRqmLjD9AzyiambFk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/7vQ5J0OY0rgOwDnytHgKDahutvm37u9_AKg6-t0JStpczm6tkJfIndqayUIyYLTYy7XkYjd2uXUtdERWsfZnk_L2l0Ob1-XRmC2mezyxNPDADtTiY-VGw5lUCuB2BJ-ggVZ5wiGS576wLhxkknfpU_-RqfTaFrRehrGpS5UwrobY0LnGU_GDK2qYLtkXDPJJ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/HMw8lR__850X5jH9zU661t0J688kqbZLYs9FEahdRv5NrpEyLOs4uR2npEDoxfdDwB205znwFdKEI-rNFY0MHutrilcItywga-HktpbapuvlzyDWYqrB5s8uwiuOhZKUhWUlv37FxV8Q0Yhrs3VtHkDjW1L9m2y2Nu9okFRrSsoNqYHnsjRBlvOSmURRdtzh?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/l_R67udbMtxLLdn1JgvvSr0h4rx6OOBlXmxzT5SvlzzM6_hsyRAWS8Iu3fApmeHFSqRHNPL3aNmmR7q-elXrLJc5coSPHyXATzEfF-NL2NJLiPFgM9tydrV1N43Nb7IsQGNOPe0zdwG_Yw-fwmbSLRsN64Y4d2Z88XvPFHjPnagnT6KadT8T0gF8SrlCGYgi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/LVfpN4lY8aLVPoiwNETJlZAvGPYbaDyDcjiRKwOsBlJ9sn1mhJdfAoX-w_iK6xfv0Wo0cs8U2U7lavKOF9wVYw5dKy_rk3-AueixiOPVkQiJINf0fFxaWcLsyXcKBG1mD1NRQ56wQ9MMKgMfZyBaWP--Q_pzYbZFtqHU3Wbb6EXZ3DTE-tLPJAwKfiM8_dvm?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/NiyQiCzRGO-GM6LxUg3FMi3oACTfxO7wBTgczM0knehi1QqDWdbJVMkOM-xHRoLCP9frtEsyCaLsMgal8P8B4YbfGKBcbGO4UNxyXCqUhMnz8t0ArFQdDtxlq-WzhzYss2ntMkeOyvzNUx44aThTAF-7HU1oEGpaRmxV-9zGZF3rAZHoJw6RdDXg6IT8DpFi?purpose=fullsize)

Elliptic curve operations are based on geometry.

---

## Reflection Rule

If

$$[
P=(x,y)
]$$

then

$$[
-P=(x,-y)
]$$

Reflection occurs over the x-axis.

---

## Three-Point Rule

A straight line intersects an elliptic curve at **three points**.

If the line passes through

* (P)
* (Q)

it meets the curve again at a third point (R).

Reflect (R) across the x-axis to obtain

$$[
P+Q
]$$

This is the basis of point addition.

---

# 3. Line Through Two Distinct Points

Suppose

$$[
P=(x_1,y_1)
]$$

and

$$[
Q=(x_2,y_2)
]$$

where

$$[
P\neq Q
]$$

The slope of the line is

$$m=\frac{y_2-y_1}{x_2-x_1}$$

Using the slope,

$$[
x_3=m^2-x_1-x_2
]$$

$$[
y_3=m(x_1-x_3)-y_1
]$$

Then

$$[
P+Q=(x_3,y_3)
]$$

### Steps

1. Draw line through (P) and (Q).
2. Find third intersection point.
3. Reflect across x-axis.
4. Result is (P+Q).

---

# 4. A Tangent Line (Point Doubling)

When

$$[
P=Q
]$$

we cannot draw a line through two different points, so we use the tangent at (P).

The slope is

$$[
m=\frac{3x_1^2+a}{2y_1}
]$$

Then

$$[
x_3=m^2-2x_1
]
$$
$$[
y_3=m(x_1-x_3)-y_1
]$$

Thus,

$$[
2P=(x_3,y_3)
]$$

This operation is called **point doubling**.

---

# 5. Addition of Points on Elliptic Curves

There are four cases.

### Case 1: Identity

$$[
P+O=P
]$$

---

### Case 2: Inverse Points

If

$$[
Q=-P
]$$

then

$$[
P+Q=O
]$$

---

### Case 3: Different Points

If

$$[
P\neq Q
]$$

Use the line joining them.

---

### Case 4: Same Point

If

$$[
P=Q
]$$

Use the tangent line.

---

## Summary Table

| Situation   | Operation                     |
| ----------- | ----------------------------- |
| (P+O)       | (P)                           |
| $(P+(-P))$  | (O)                           |
| $(P\neq Q)$ | Draw line through both points |
| (P=Q)       | Draw tangent line             |

---

# 6. Cryptosystems Defined over Elliptic Curves

Instead of modular exponentiation (as in RSA or ElGamal), ECC uses **point multiplication**.

Instead of

[
$$g^k
]$$

ECC computes

$$[
Q=kP
]$$

where

* (P) = base point (public)
* (k) = private key
* (Q) = public key

Point multiplication means repeated point addition:

$$[
3P=P+P+P
]$$

$$[
5P=P+P+P+P+P
]$$

Efficient algorithms (such as double-and-add) are used instead of adding one point repeatedly.

---

## ECC Key Generation

Choose

* Elliptic curve
* Base point (P)
* Private key (d)

Compute


$$Q=dP
]$$

Public Key:

$$[
(E,P,Q)
]$$

Private Key:

$$[
d
]$$

---

## Why ECC is Secure

Given

$$[
Q=dP
]$$

it is easy to compute (Q) from (d), but extremely difficult to recover (d) from (P) and (Q). This hard problem is called the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

---

# Exam Questions

### Short Questions (2–5 marks)

* Define an elliptic curve.
* What is the point at infinity?
* What is the inverse of a point?
* State the equation of an elliptic curve.
* What condition makes an elliptic curve valid for cryptography?
* What is point doubling?
* What is point addition?
* What is point multiplication?

### Long Questions (8–10 marks)

* Explain the geometry of elliptic curves with diagrams.
* Explain addition of points on elliptic curves.
* Explain point doubling using the tangent method.
* Explain cryptosystems defined over elliptic curves.
* Explain how ECC differs from RSA and why it provides equivalent security with much smaller key sizes.

> **Exam tip:** In many university exams, you are **not** expected to perform lengthy numerical calculations for point addition. Most questions focus on explaining the geometric ideas, the addition rules, and how these operations are used to build ECC.
