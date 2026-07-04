#advanced-cryptography 

# Block Cipher

A **Block Cipher** is a **symmetric encryption algorithm** that encrypts **a fixed-size block of data at a time**, rather than one bit or one byte at a time.

For example:

* **DES** encrypts **64-bit blocks**.
* **AES** encrypts **128-bit blocks**.

---

# Simple Definition (Exam)

> **A Block Cipher is a symmetric key encryption algorithm that encrypts plaintext in fixed-size blocks using the same secret key for both encryption and decryption.**

---

# How It Works

Suppose the block size is **8 bits** (real block ciphers use larger sizes, but this keeps the example simple).

### Plaintext

```text id="l5h6nd"
HELLO
```

Suppose we divide it into blocks:

```text id="uwjlwm"
Block 1 → HE
Block 2 → LL
Block 3 → OX
```

We add **X** because the last block has only one letter.

Each block is encrypted **separately**.

```text id="gmabg4"
HE  → Encrypted → AB

LL  → Encrypted → PQ

OX  → Encrypted → ZR
```

Final Ciphertext:

```text id="0ydu2k"
ABPQZR
```

---

# Diagram

```text id="msj63g"
Plaintext

HELLO

↓

Split into blocks

HE   LL   OX

↓

Encrypt each block

↓

Ciphertext

AB   PQ   ZR
```

---

# Block Cipher Formula

Encryption:

$$
C=E_K(P)
$$

where:

* **$P$** = Plaintext block
* **$K$** = Secret key
* **$E$** = Encryption algorithm
* **$C$** = Ciphertext block

Decryption:

$$
P=D_K(C)
$$

---

# Examples of Block Ciphers

| Algorithm | Block Size                         |
| --------- | ---------------------------------- |
| DES       | 64 bits                            |
| 3DES      | 64 bits                            |
| AES       | 128 bits                           |
| RC5       | Variable (commonly 64 or 128 bits) |
| Blowfish  | 64 bits                            |

---

# Characteristics

* Encrypts **fixed-size blocks**.
* Uses the **same secret key** for encryption and decryption.
* Usually performs **multiple rounds** of substitution and permutation.

---

# Advantages

* Strong security.
* Good for encrypting files and stored data.
* Widely used (AES is the current standard).

---

# Disadvantages

* Needs **padding** if the message length is not a multiple of the block size.
* Generally slower than stream ciphers for continuous real-time data.

---

# Block Cipher vs Stream Cipher

| Block Cipher                  | Stream Cipher                               |
| ----------------------------- | ------------------------------------------- |
| Encrypts a **block** of data. | Encrypts **one bit or one byte** at a time. |
| Example: AES, DES, RC5        | Example: RC4                                |
| Uses rounds.                  | Uses a keystream and XOR.                   |
| May require padding.          | No padding needed.                          |

---

# Real-Life Analogy

Imagine you're packing books.

### Block Cipher 📦

You pack books into **boxes of 10 books**.

If you have:

```text id="klmsiv"
25 books
```

You make:

```text id="h2j9dh"
Box 1 → 10 books
Box 2 → 10 books
Box 3 → 5 books + fillers
```

Each **box** is locked separately.

---

### Stream Cipher 🚰

Instead of boxes, imagine water flowing through a pipe.

You encrypt **one drop at a time** continuously.

---

# Memory Trick ⭐

Think:

```text id="7qzjki"
Block Cipher = Box 📦
Stream Cipher = Flowing Water 🚰
```

* **Block Cipher** → Processes data in **fixed-size blocks**.
* **Stream Cipher** → Processes data **continuously, bit by bit or byte by byte**.

---

# Exam Definition (2 Marks)

> **A Block Cipher is a symmetric encryption algorithm that encrypts plaintext in fixed-size blocks using a secret key. If the final block is shorter than the required block size, padding is added before encryption.**

---

# Quick Comparison (Most Important for Exams)

| Feature            | Block Cipher      | Stream Cipher |
| ------------------ | ----------------- | ------------- |
| Unit of encryption | Fixed-size block  | Bit/byte      |
| Padding required   | ✅ Yes (if needed) | ❌ No          |
| Uses keystream     | ❌ No              | ✅ Yes         |
| Encryption style   | Block by block    | Continuous    |
| Examples           | AES, DES, RC5     | RC4           |

### One-line Memory Trick

> **Block Cipher = Encrypts data in blocks. Stream Cipher = Encrypts data as a continuous stream using a keystream.**
