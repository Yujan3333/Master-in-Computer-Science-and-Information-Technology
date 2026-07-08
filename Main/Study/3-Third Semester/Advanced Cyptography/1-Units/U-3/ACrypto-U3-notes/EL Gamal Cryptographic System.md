#advanced-cryptography #third-semester 

# ElGamal Cryptographic System (Easy & Exam-Focused)

The **ElGamal Cryptosystem** is an **asymmetric (public-key) encryption algorithm** introduced by Taher ElGamal in **1985**.

Unlike RSA, **ElGamal's security is based on the Discrete Logarithm Problem (DLP)** rather than integer factorization.

---

# What is ElGamal?

ElGamal is a public-key cryptosystem used for:

* Secure encryption
* Secure key exchange
* Digital signatures (ElGamal Signature)

It uses:

* Public Key → Encrypt
* Private Key → Decrypt

---

# Why ElGamal?

Imagine Alice wants to send a secret message to Bob.

Instead of sharing one secret key (as in symmetric encryption), Bob publishes a **public key**.

Anyone can encrypt a message using Bob's public key, but **only Bob can decrypt it** using his private key.

---

# Security Basis

ElGamal depends on the **Discrete Logarithm Problem (DLP)**.

Suppose

$$
y=g^x \bmod p
$$

Finding **$y$** is easy.

Finding **$x$** from **$g$**, **$y$**, and **$p$** is extremely difficult.

This difficulty makes ElGamal secure.

---

# ElGamal Algorithm

There are **3 phases**:

1. Key Generation
2. Encryption
3. Decryption

![](../../../../../../../Images/Third_Sem_Images/EL%20Gamal%20Cryptographic%20System.png)

---

# Phase 1: Key Generation

## Step 1

Choose a large prime number

```text
p
```

Example

```text
p = 23
```

---

## Step 2

Choose a generator

```text
g
```

Example

```text
g = 5
```

---

## Step 3

Choose Private Key

Bob chooses a secret number

```text
x
```

Example

```text
x = 6
```

Only Bob knows this.

---

## Step 4

Compute Public Key

Formula

$$
y=g^x \bmod p
$$

Example

$$
y=5^6 \bmod23
$$

$$
5^6=15625
$$

$$
15625\bmod23=8
$$

So

```text
Public Key = (p,g,y)

=(23,5,8)
```

Private key

```text
x=6
```

---

# Phase 2: Encryption

Suppose Alice wants to send

```text
M=10
```

---

## Step 1

Choose a random number

```text
k
```

Example

```text
k=3
```

This random value must be different for every message.

---

## Step 2

Compute

### First Ciphertext

Formula

$$
C_1=g^k\bmod p
$$

Example

$$
5^3\bmod23
$$

$$
125\bmod23=10
$$

So

```text
C1=10
```

---

### Second Ciphertext

Formula

$$
C_2=M\times y^k\bmod p
$$

Example

$$
10\times8^3\bmod23
$$

Since

$$
8^3=512
$$

$$
512\bmod23=6
$$

Then

$$
10\times6=60
$$

$$
60\bmod23=14
$$

So

```text
C2=14
```

Ciphertext is

```text
(C1,C2)

=(10,14)
```

---

# Phase 3: Decryption

Bob receives

```text
(10,14)
```

He uses private key

```text
x=6
```

Formula

$$
M=C_2\times(C_1^x)^{-1}\bmod p
$$

where

$$
(C_1^x)^{-1}
$$

means the **modular inverse**.

After calculation,

Bob gets

```text
M=10
```

Original message is recovered.

---

# Complete Flow

```text
Choose p,g

↓

Choose private key x

↓

Compute public key

y=g^x mod p

↓

Public Key=(p,g,y)

↓

Encrypt

Choose random k

↓

C1=g^k mod p

↓

C2=M×y^k mod p

↓

Ciphertext=(C1,C2)

↓

Decrypt

M=C2×(C1^x)^-1 mod p
```

---

# Why Random Number $k$ is Important

Every encryption uses a **new random value $k$**.

Even if the same message is encrypted twice,

```text
HELLO
```

the ciphertexts will be different.

Example

```text
HELLO

↓

Ciphertext 1
```

Next time

```text
HELLO

↓

Ciphertext 2
```

Different ciphertexts make ElGamal more secure.

---

# Advantages

* Very secure
* Based on the Discrete Logarithm Problem
* Same plaintext produces different ciphertexts because of random $k$
* Supports digital signatures
* Suitable for secure key exchange

---

# Disadvantages

* Slower than symmetric encryption
* Ciphertext is about **twice the size** of the plaintext
* Requires good random number generation
* Uses more computation than RSA for some operations

---

# ElGamal vs RSA

| Feature                      | ElGamal                            | RSA                                                                    |
| ---------------------------- | ---------------------------------- | ---------------------------------------------------------------------- |
| Security based on            | Discrete Logarithm Problem         | Integer Factorization Problem                                          |
| Keys                         | Public & Private                   | Public & Private                                                       |
| Same message encrypted twice | Different ciphertexts (random $k$) | Usually same ciphertext with textbook RSA (without randomized padding) |
| Ciphertext size              | Larger                             | Smaller                                                                |
| Digital Signature            | Yes                                | Yes                                                                    |

---

# Important Formulas ⭐⭐⭐⭐⭐

### Public Key

$$
y=g^x \bmod p
$$

### First Ciphertext

$$
C_1=g^k \bmod p
$$

### Second Ciphertext

$$
C_2=M\times y^k \bmod p
$$

### Decryption

$$
M=C_2\times(C_1^x)^{-1}\bmod p
$$

---

# Easy Memory Trick ⭐⭐⭐⭐⭐

Remember the order:

```text
Choose p, g

↓

Choose private key x

↓

Compute y = g^x mod p

↓

Public Key = (p, g, y)

↓

Choose random k

↓

C1 = g^k mod p

↓

C2 = M × y^k mod p

↓

Decrypt:
M = C2 × (C1^x)^-1 mod p
```

**Memory Trick:**

> **"p → g → x → y → k → C₁ → C₂ → M"**

---

# Exam Definition (2 Marks)

> **ElGamal Cryptosystem is an asymmetric (public-key) encryption algorithm developed by Taher ElGamal in 1985. It is based on the Discrete Logarithm Problem (DLP). It uses a public key for encryption and a private key for decryption. During encryption, a random number $k$ is chosen, producing a unique ciphertext even for the same plaintext, which enhances security.**

---

# Exam Answer (5 Marks)

**ElGamal Cryptosystem** is a public-key cryptographic algorithm proposed by Taher ElGamal in 1985. Its security is based on the **Discrete Logarithm Problem (DLP)**. In the **key generation** phase, a large prime number $p$, a generator $g$, and a private key $x$ are selected. The public key is computed as

$$
y=g^x \bmod p.
$$

During **encryption**, the sender chooses a random number $k$ and computes

$$
C_1=g^k \bmod p
$$

and

$$
C_2=M\times y^k \bmod p,
$$

where $M$ is the plaintext. During **decryption**, the receiver uses the private key to recover the original message using

$$
M=C_2\times(C_1^x)^{-1}\bmod p.
$$

ElGamal provides strong security because a fresh random value $k$ is used for every encryption, making identical plaintexts produce different ciphertexts.
