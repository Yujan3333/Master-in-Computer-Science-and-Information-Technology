#third-semester #advanced-cryptography 
# UNIT 2: Block and Stream Ciphers (Summary)

## 1. Block Cipher Principles

A **block cipher** encrypts data in **fixed-size blocks** (e.g., 64-bit, 128-bit).

### Core Idea

* Input plaintext is divided into blocks
* Each block is encrypted using the same key
* Output = ciphertext blocks

### Important Concepts

* **Confusion** → hides relationship between key and ciphertext
* **Diffusion** → spreads plaintext influence across ciphertext
* Achieved using multiple rounds of substitution + permutation

---

## 2. Data Encryption Standard (DES)

Data Encryption Standard

### Overview

* Block size: 64-bit
* Key size: 56-bit (effective)
* Structure: Feistel network
* 16 rounds of encryption

### Steps

1. Initial permutation
2. Split into left and right halves
3. 16 rounds of:

   * Expansion
   * Substitution (S-boxes)
   * Permutation
   * XOR with key
4. Final permutation

---

## 3. Strength of DES

### Weakness

* Small key size (56-bit → brute-forceable today)

### Attacks

#### 1. Linear Cryptanalysis

* Uses **linear approximations** between plaintext, ciphertext, and key
* Finds statistical biases

#### 2. Differential Cryptanalysis

* Studies how **differences in plaintext affect ciphertext differences**
* Tracks patterns through encryption rounds

---

## 4. AES (Advanced Encryption Standard)

Advanced Encryption Standard

### Overview

* Block size: 128-bit
* Key sizes: 128 / 192 / 256-bit
* Based on substitution-permutation network (SPN)

### Rounds

* 10, 12, or 14 rounds depending on key size

### Operations per round

* SubBytes (substitution)
* ShiftRows (row shifting)
* MixColumns (diffusion)
* AddRoundKey (XOR)

### Strength

* Very secure
* Resistant to known attacks
* Widely used today (internet, banking, VPNs)

---

## 5. IDEA (International Data Encryption Algorithm)

International Data Encryption Algorithm

### Features

* 64-bit block size
* 128-bit key
* Uses:

  * XOR
  * Addition mod $2^{16}$
  * Multiplication mod $2^{16}+1$

### Strength

* Strong design (mix of algebraic operations)
* Resistant to classical attacks

---

## 6. Blowfish

Blowfish

### Features

* 64-bit block size
* Variable key length (32–448 bits)
* Feistel structure
* Fast and flexible

### Strength

* No practical attacks found
* Still secure, but replaced in many systems by AES

---

# STREAM CIPHERS

## Basic Idea

Unlike block ciphers:

> Stream ciphers encrypt **one bit/byte at a time**

They generate a **keystream** and XOR it with plaintext.

---

## 7. Synchronous Stream Ciphers

* Keystream depends only on key (not plaintext/ciphertext)
* Sender and receiver must stay synchronized

---

## 8. LFSR (Linear Feedback Shift Register)

Linear Feedback Shift Register

### Idea

* Uses shift register + XOR feedback
* Generates pseudo-random bit stream

### Weakness

* Linear → predictable → breakable with enough output

---

## 9. NLFSR (Non-Linear Feedback Shift Register)

### Idea

* Like LFSR but uses **non-linear functions**
* Stronger randomness

### Advantage

* Harder to predict than LFSR

---

## 10. Self-Synchronous Stream Cipher

* Keystream depends on previous ciphertext bits
* Automatically resynchronizes after errors

---

## 11. RC4

RC4

### Features

* Byte-based stream cipher
* Simple and fast
* Used in SSL/TLS (older versions)

### Weakness

* Biased outputs
* Key reuse is dangerous
* Now considered insecure

---

## 12. RC5

RC5

### Features

* Variable block size
* Variable rounds
* Variable key size
* Uses:

  * XOR
  * rotation
  * modular addition

### Strength

* Simple but flexible design
* Good performance

---

# BLOCK vs STREAM CIPHER (VERY IMPORTANT)

| Feature      | Block Cipher        | Stream Cipher      |
| ------------ | ------------------- | ------------------ |
| Data type    | Fixed blocks        | Bit/byte stream    |
| Speed        | Slower              | Faster             |
| Error effect | Affects whole block | Affects single bit |
| Examples     | AES, DES            | RC4, LFSR          |

---

# BIG PICTURE (How to Remember)

* DES → old standard (weak now)
* AES → modern secure standard
* IDEA/Blowfish → strong classical designs
* Stream ciphers → fast, real-time encryption
* LFSR → linear generator (weak alone)
* RC4 → broken but historically important

---

# Exam Memory Trick

**Block ciphers = “chunk encryption”**
**Stream ciphers = “flow encryption”**

---