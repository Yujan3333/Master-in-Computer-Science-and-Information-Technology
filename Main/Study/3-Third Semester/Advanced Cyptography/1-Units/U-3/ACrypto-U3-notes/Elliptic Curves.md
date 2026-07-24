#advanced-cryptography #third-semester 


![](../../../../../../../Images/Third_Sem_Images/Elliptic%20Curves.png)

![](../../../../../../../Images/Third_Sem_Images/Elliptic%20Curves-1.png)

ECC Keyexchange
![](../../../../../../../Images/Third_Sem_Images/Elliptic%20Curves-2.png)

ECC Encryption
![](../../../../../../../Images/Third_Sem_Images/Elliptic%20Curves-encrp.png)

ECC Decryption
![](../../../../../../../Images/Third_Sem_Images/Elliptic%20Curves-3.png)





---

# Elliptic Curves (ECC)

Elliptic Curve Cryptography (ECC) is a **public-key cryptographic system** based on the mathematics of **elliptic curves over finite fields**.

Instead of relying on the **Integer Factorization Problem (RSA)** or the **Discrete Logarithm Problem (ElGamal)**, ECC relies on the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

The main advantage of ECC is that it provides the **same security with much smaller key sizes**, making it faster and more efficient.

---

# Definition

An **elliptic curve** is a set of points satisfying the equation

$$
y^2=x^3+ax+b
$$

where

$$
4a^3+27b^2\ne0.
$$

The second condition ensures that the curve has **no cusps or self-intersections**.

---

## General Equation

$$
y^2=x^3+ax+b
$$

where

* (a,b) are constants.
* (x,y) are points on the curve.

The curve also includes a special point called the **Point at Infinity ((\mathcal O))**, which acts as the identity element.

---

# What Does the Curve Look Like?

A typical elliptic curve looks like this:

```
        y
        ↑
    •       •
      \     /
       \   /
--------\-/----------→ x
         /\
        /  \
    •        •
```

Notice:

* It is **not an ellipse**.
* It is a smooth cubic curve.
* It is symmetric about the x-axis.

---

# Why is ECC Secure?

Given two points

$$
P
$$

and

$$
Q=kP,
$$

it is easy to compute (Q) from (P).

However, given (P) and (Q), finding

$$
k
$$

is extremely difficult.

This difficult problem is called the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

---

# Operations on Elliptic Curves

ECC uses **points** instead of ordinary numbers.

The main operations are:

1. Point Addition
2. Point Doubling
3. Scalar Multiplication

---

# 1. Point Addition

Suppose

$$
P=(x_1,y_1)
$$

and

$$
Q=(x_2,y_2).
$$

Draw a straight line through (P) and (Q).

The line intersects the curve at a third point.

Reflect this third point across the x-axis.

The reflected point is

$$
R=P+Q.
$$

Diagram:

```
          Q

         •
        /
       /
      /
 P •
      \
       \
        •
        Third Point

Reflect ↓

      R=P+Q
```

---

# 2. Point Doubling

If

$$
P=Q,
$$

draw the tangent line at (P).

The tangent intersects the curve at another point.

Reflect it about the x-axis.

This gives

$$
2P.
$$

---

# 3. Scalar Multiplication

Repeated addition of a point.

Example

$$
3P=P+P+P
$$

$$
5P=P+P+P+P+P
$$

This operation is **easy**.

Finding

$$
P
$$

from

$$
Q=kP
$$

is **hard**.

---

# Key Generation in ECC

Choose

* Elliptic curve
* Base point

$$
G
$$

Choose private key

$$
d
$$

Compute public key

$$
Q=dG
$$

Thus

**Private key**

$$
d
$$

**Public key**

$$
Q
$$

---

# Encryption

Suppose

* Sender wants to send message (M).
* Receiver's public key is

$$
Q=dG.
$$

### Step 1

Choose a random number

$$
k.
$$

### Step 2

Compute

$$
C_1=kG
$$

### Step 3

Compute

$$
C_2=M+kQ
$$

Ciphertext is

$$
(C_1,C_2).
$$

---

# Decryption

Receiver knows

$$
d.
$$

Compute

$$
dC_1=d(kG)=kQ.
$$

Recover message

$$
M=C_2-dC_1.
$$

---

# Why Does It Work?

Because

$$
Q=dG.
$$

Therefore,

$$
dC_1
=

d(kG)

k(dG)

kQ
$$

Hence

$$
C_2-dC_1
=

(M+kQ)-kQ

M
$$

The added secret cancels out, revealing the original message.

---

# Advantages of ECC

* Smaller key sizes.
* Faster computations.
* Lower memory usage.
* Lower power consumption.
* Suitable for mobile devices and IoT.
* High security.

---

# Disadvantages

* More complex mathematics.
* Difficult implementation.
* Slower encryption than symmetric algorithms.
* Requires careful parameter selection.

---

# ECC vs RSA

| ECC                       | RSA                            |
| ------------------------- | ------------------------------ |
| Based on ECDLP            | Based on integer factorization |
| Smaller keys              | Larger keys                    |
| Faster with small keys    | Slower for same security       |
| Less memory               | More memory                    |
| Better for mobile devices | Better for traditional systems |

---

# Key Size Comparison

| Security Level | RSA        | ECC      |
| -------------- | ---------- | -------- |
| 80-bit         | 1024 bits  | 160 bits |
| 112-bit        | 2048 bits  | 224 bits |
| 128-bit        | 3072 bits  | 256 bits |
| 192-bit        | 7680 bits  | 384 bits |
| 256-bit        | 15360 bits | 521 bits |

ECC achieves the same level of security with much shorter keys.

---

# Applications

* HTTPS/TLS
* Bitcoin and other cryptocurrencies
* Digital signatures (ECDSA)
* Key exchange (ECDH)
* Smart cards
* Mobile phones
* IoT devices

---

# Exam Questions

### Q1. What is an Elliptic Curve?

**Answer:**
An elliptic curve is a set of points satisfying

$$
y^2=x^3+ax+b,
$$

where

$$
4a^3+27b^2\ne0.
$$

It forms the mathematical basis of Elliptic Curve Cryptography (ECC), which relies on the hardness of the Elliptic Curve Discrete Logarithm Problem.

---

### Q2. Why is ECC More Secure Than RSA?

**Answer:**

* ECC provides equivalent security with much smaller keys.
* It is based on the difficult Elliptic Curve Discrete Logarithm Problem.
* Smaller keys make ECC faster, require less storage, and consume less power than RSA.

---

## Exam Tip

For most university cryptography exams (including TU/MCA), **you are usually not expected to derive the point addition or point doubling formulas**. You should know:

* Definition of an elliptic curve.
* General equation.
* Concept of point addition, point doubling, and scalar multiplication.
* ECDLP (security basis).
* Key generation, encryption, and decryption (high-level steps).
* Advantages, disadvantages, and comparison with RSA.


