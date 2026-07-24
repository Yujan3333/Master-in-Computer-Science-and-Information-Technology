#advanced-cryptography #third-semester 

# Rabin Cryptosystem

The **Rabin Cryptosystem** is an **asymmetric (public-key) cryptographic algorithm** proposed by **Michael O. Rabin (1979)**.

It is based on the difficulty of **integer factorization**, the same hard problem used by RSA. The security of the Rabin cryptosystem is **provably equivalent** to the difficulty of factoring a large composite number.

A unique feature of Rabin is that **encryption is very simple**, but **decryption produces four possible plaintexts**, requiring additional information to identify the correct one.

---

# Algorithm

The Rabin cryptosystem consists of three phases:

1. Key Generation
2. Encryption
3. Decryption

---

# 1. Key Generation

## Step 1: Choose two large prime numbers

Choose two distinct large primes

$$
p \equiv 3 \pmod 4
$$

$$
q \equiv 3 \pmod 4
$$

This condition simplifies square root computation during decryption.

---

## Step 2: Compute modulus

$$
n=pq
$$

---

## Step 3: Publish keys

**Public Key**

$$
(n)
$$

**Private Key**

$$
(p,q)
$$

---

# 2. Encryption

Suppose the plaintext message is

$$
M<n
$$

The sender computes

$$
C=M^2 \bmod n
$$

where

* (M) = plaintext
* (C) = ciphertext

Only **one modular squaring** is required, making encryption very fast.

---

## Encryption Steps

```text
Plaintext M
      │
      ▼
Square modulo n
C = M² mod n
      │
      ▼
Ciphertext
```

---

# Example of Encryption

Choose

$$
p=7,\qquad q=11
$$

Compute

$$
n=7\times11=77
$$

Public key

$$
(77)
$$

Private key

$$
(7,11)
$$

Suppose

$$
M=20
$$

Encryption

$$
C=20^2\bmod77
$$

$$
=400\bmod77
$$

Since

$$
400=77\times5+15
$$

Therefore

$$
C=15
$$

Ciphertext sent is

$$
15
$$

---

# 3. Decryption

The receiver knows

$$
p,q
$$

and must recover

$$
M
$$

from

$$
C=M^2\bmod n
$$

Unlike RSA, Rabin decryption gives **four square roots**, meaning **four candidate plaintexts**.

---

## Step 1: Compute square roots modulo p

Compute

$$
m_p=C^{\frac{p+1}{4}}\bmod p
$$

The two roots are

$$
m_p
$$

and

$$
p-m_p
$$

---

## Step 2: Compute square roots modulo q

Compute

$$
m_q=C^{\frac{q+1}{4}}\bmod q
$$

The two roots are

$$
m_q
$$

and

$$
q-m_q
$$

---

## Step 3: Apply Chinese Remainder Theorem (CRT)

Combine the roots modulo (p) and modulo (q).

Possible combinations:

1.

$$
(+m_p,+m_q)
$$

2.

$$
(+m_p,-m_q)
$$

3.

$$
(-m_p,+m_q)
$$

4.

$$
(-m_p,-m_q)
$$

These produce **four different plaintexts**.

The receiver selects the correct one using redundancy, padding, or message formatting.

---

# Complete Numerical Example

Given

$$
p=7,\qquad q=11
$$

Then

$$
n=77
$$

Ciphertext

$$
C=15
$$

---

## Step 1: Find roots modulo 7

Compute

$$
m_p=15^{\frac{7+1}{4}}\bmod7
$$

Since

$$
\frac{7+1}{4}=2
$$

$$
15^2\bmod7
$$

Because

$$
15\equiv1\pmod7
$$

$$
1^2=1
$$

Thus

$$
m_p=1
$$

Other root

$$
7-1=6
$$

Roots modulo 7 are

$$
1,;6
$$

---

## Step 2: Find roots modulo 11

Compute

$$
m_q=15^{\frac{11+1}{4}}\bmod11
$$

Since

$$
\frac{11+1}{4}=3
$$

First,

$$
15\equiv4\pmod{11}
$$

Then

$$
4^3=64
$$

$$
64\bmod11=9
$$

Thus

$$
m_q=9
$$

Other root

$$
11-9=2
$$

Roots modulo 11

$$
9,;2
$$

---

## Step 3: Combine Using CRT

Possible pairs:

$$
(1,9)
$$

$$
(1,2)
$$

$$
(6,9)
$$

$$
(6,2)
$$

Using CRT:

### Pair (1,9)

Solution:

$$
x=64
$$

---

### Pair (1,2)

Solution:

$$
x=57
$$

---

### Pair (6,9)

Solution:

$$
x=20
$$

---

### Pair (6,2)

Solution:

$$
x=13
$$

---

Hence the four possible plaintexts are

$$
13,;20,;57,;64
$$

Since the original message was

$$
20
$$

the receiver chooses **20** as the valid plaintext.

---

# Why Four Plaintexts?

Squaring is **not one-to-one** modulo a composite number.

Each ciphertext corresponds to **four square roots**, so decryption always yields four candidates.

---

# Advantages

* Very fast encryption (only one modular squaring).
* Security is directly related to the integer factorization problem.
* Simpler encryption than RSA.

---

# Disadvantages

* Decryption returns **four possible plaintexts**.
* Requires redundancy or padding to identify the correct message.
* Less widely used than RSA due to ambiguity in decryption.

---

# Flow Diagram

```text
                Key Generation
           Choose p and q (≡3 mod 4)
                    │
                    ▼
                n = p × q
                    │
     Public Key = n     Private Key = (p,q)

------------------------------------------------

Sender

Plaintext M
      │
      ▼
C = M² mod n
      │
      ▼
Ciphertext

------------------------------------------------

Receiver

Ciphertext C
      │
      ▼
Find square roots mod p and mod q
      │
      ▼
Apply Chinese Remainder Theorem (CRT)
      │
      ▼
Four candidate plaintexts
      │
      ▼
Choose the correct plaintext using redundancy/padding
```

## Exam Tip

For a **10-mark question**, write:

1. Definition.
2. Key Generation.
3. Encryption algorithm with formula.
4. Decryption algorithm (roots modulo (p) and (q), then CRT).
5. Numerical example.
6. Advantages and disadvantages.
7. Flow diagram.

This covers all the points typically expected in university cryptography exams.
