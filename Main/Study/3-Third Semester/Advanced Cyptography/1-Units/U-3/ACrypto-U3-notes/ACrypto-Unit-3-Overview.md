#advanced-cryptography #third-semester 

Below is an **exam-focused, easy-to-understand summary** of **Unit 3: Public Key Cryptography and Discrete Logarithms**. I've simplified each topic while keeping the important points for exams.

---

# Unit 3: Public Key Cryptography and Discrete Logarithms

## 1. Principles of Public-Key Cryptosystems

### What is Public-Key Cryptography?

Public-key cryptography (also called **asymmetric cryptography**) uses **two different keys**:

* **Public Key** → Shared with everyone.
* **Private Key** → Kept secret by the owner.

Unlike symmetric encryption, the encryption and decryption keys are different.

### Working

```text
Sender
   │
   │ Encrypt using Receiver's Public Key
   ▼
Ciphertext
   │
   ▼
Receiver
   │
Decrypt using Private Key
   ▼
Plaintext
```

### Features

* Uses two keys.
* Public key can be shared openly.
* Private key is secret.
* Solves the key distribution problem.
* Slower than symmetric encryption.

### Uses

* Encryption
* Digital signatures
* Key exchange

---

# 2. RSA Algorithm

RSA is the **most famous public-key cryptosystem**.

It was developed by:

* Ron Rivest
* Adi Shamir
* Leonard Adleman

(RSA comes from the first letters of their surnames.)

---

## RSA Steps

### Step 1

Choose two prime numbers

```text
p and q
```

Example

```text
p = 7
q = 11
```

---

### Step 2

Calculate

```text
n = p × q
```

Example

```text
n = 7 × 11 = 77
```

---

### Step 3

Calculate Euler's Totient

```text
φ(n) = (p−1)(q−1)
```

Example

```text
6 × 10 = 60
```

---

### Step 4

Choose public exponent

```text
e
```

such that

```text
gcd(e,φ)=1
```

---

### Step 5

Calculate private key

```text
d
```

where

```text
d × e ≡ 1 mod φ
```

---

### Encryption

```text
C = M^e mod n
```

---

### Decryption

```text
M = C^d mod n
```

---

### Remember

Public Key

```text
(e,n)
```

Private Key

```text
(d,n)
```

---

# 3. Security of RSA

RSA is secure because **factoring a large number into its prime factors is extremely difficult**.

---

## (a) Brute Force Attack

The attacker tries every possible private key.

Very difficult because the key is very large.

---

## (b) Mathematical Attack

The attacker tries to factor

```text
n = p × q
```

If they find p and q, they can calculate the private key.

This is the biggest theoretical attack on RSA.

---

## (c) Timing Attack

The attacker measures how long decryption takes.

Different execution times may reveal information about the private key.

Protection:

* Constant-time algorithms
* Random delays

---

## (d) Chosen Ciphertext Attack

The attacker submits specially chosen ciphertexts and studies the decrypted outputs.

Protection:

* Padding schemes (e.g., OAEP)
* Avoid decrypting arbitrary attacker-provided ciphertexts

---

# 4. Rabin Cryptosystem

Rabin Cryptosystem is another public-key algorithm.

### Main Idea

Encryption

```text
C = M² mod n
```

Security is based directly on the difficulty of **integer factorization**.

### Difference from RSA

RSA

```text
C=M^e
```

Rabin

```text
C=M²
```

---

# 5. Discrete Logarithm System

Many public-key systems are based on **modular arithmetic** instead of factorization.

Suppose

```text
2^x mod 13 = 8
```

Finding

```text
8
```

is easy.

Finding

```text
x
```

is difficult.

That difficult problem is called the **Discrete Logarithm Problem (DLP).**

---

# 6. Discrete Logarithm Problem (DLP)

## Definition

Given

```text
g

p

y
```

Find

```text
x
```

such that

```text
g^x mod p = y
```

This is easy to compute in the forward direction but hard to reverse.

This one-way property provides security for algorithms like ElGamal and ECC.

---

# 7. ElGamal Cryptosystem

ElGamal is a **public-key encryption algorithm** based on the Discrete Logarithm Problem.

### Steps

* Generate keys.
* Encrypt using the receiver's public key.
* Decrypt using the private key.

### Features

* Public-key algorithm
* Uses modular arithmetic
* Based on DLP
* Produces different ciphertexts for the same plaintext because it uses a random value during encryption

---

# 8. ElGamal Digital Signature

Used to verify:

* Message authenticity
* Integrity
* Non-repudiation

### Process

Sender

```text
Message

↓

Hash

↓

Sign using Private Key

↓

Signature
```

Receiver

```text
Message

↓

Verify using Public Key

↓

Valid or Invalid
```

---

# 9. Basic Facts of Elliptic Curves

An **elliptic curve** is a special mathematical curve used in modern cryptography.

General equation:

```text
y² = x³ + ax + b
```

It is **not** an ellipse.

Points on the curve have special mathematical properties that form the basis of ECC.

---

# 10. Geometry of Elliptic Curves

Points on the curve can be **added together**.

This addition defines the cryptographic operations used in ECC.

---

# 11. Line Through Two Distinct Points

Take two different points

```text
P

Q
```

Draw a line through them.

The line intersects the curve at a third point.

Reflect that third point across the x-axis.

The reflected point is

```text
P + Q
```

---

# 12. Tangent Line

If

```text
P = Q
```

instead of drawing a line through two different points, draw the tangent at P.

The tangent intersects the curve again.

Reflect the intersection point across the x-axis.

This gives

```text
2P
```

(point doubling).

---

# 13. Addition of Points on Elliptic Curves

Rules:

Different points

```text
P + Q
```

Same point

```text
P + P = 2P
```

These operations replace ordinary multiplication in ECC.

---

# 14. Cryptosystems Defined over Elliptic Curves

Public-key systems can use elliptic curve mathematics instead of modular arithmetic.

Examples:

* ECC Encryption
* ECC Digital Signatures
* ECC Key Exchange

---

# 15. Discrete Logarithm Problem over Elliptic Curves (ECDLP)

Suppose

```text
Q = kP
```

Calculating Q from P and k is easy.

Finding k from P and Q is extremely difficult.

This is called the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

ECC security is based on this problem.

---

# 16. Elliptic Curve Cryptography (ECC)

ECC is a public-key cryptosystem based on elliptic curves.

### Advantages

* Very high security
* Small key sizes
* Fast operations
* Less memory usage
* Suitable for mobile devices and IoT

Example:

| RSA          | ECC                                    |
| ------------ | -------------------------------------- |
| 3072-bit key | 256-bit key                            |
| Larger keys  | Much smaller keys for similar security |

---

# 17. Digital Signatures using ECC

ECC can also create digital signatures (commonly using ECDSA).

Process:

```text
Message

↓

Hash

↓

Sign using ECC Private Key

↓

Signature

↓

Verify using ECC Public Key
```

Purpose:

* Authentication
* Integrity
* Non-repudiation

---

# ⭐ Most Important Exam Topics (Very Likely)

1. Principles of Public-Key Cryptography
2. RSA Algorithm (key generation, encryption, decryption)
3. Security of RSA (Brute Force, Mathematical, Timing, Chosen Ciphertext attacks)
4. Discrete Logarithm Problem (DLP)
5. ElGamal Cryptosystem
6. Elliptic Curve Cryptography (ECC)
7. Advantages of ECC over RSA
8. Digital Signatures using ECC

## 📌 Easy Memory Trick

Remember the unit in this order:

* **Public Key** → Two keys (Public + Private)
* **RSA** → Based on **factorization**
* **Rabin** → Based on **factorization**, uses (M^2)
* **DLP** → Hard to find the exponent
* **ElGamal** → Uses DLP
* **ECC** → Uses Elliptic Curves + ECDLP, gives strong security with **smaller keys**
