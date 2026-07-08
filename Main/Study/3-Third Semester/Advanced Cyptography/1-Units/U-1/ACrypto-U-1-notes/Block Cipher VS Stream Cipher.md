#advanced-cryptography #third-semester 


## Difference Between Block Cipher and Stream Cipher

| **Block Cipher**                                                                                                   | **Stream Cipher**                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Encrypts a **fixed-size block** of data at a time (e.g., 64 or 128 bits).                                          | Encrypts **one bit or one byte** at a time.                                                                         |
| Processes the entire block before encryption.                                                                      | Encrypts data continuously as it is received.                                                                       |
| Uses multiple encryption rounds and substitution/permutation operations.                                           | Uses a **keystream** and **XOR** operation.                                                                         |
| Generally slower than stream ciphers.                                                                              | Generally faster than block ciphers.                                                                                |
| Suitable for encrypting files, databases, and stored data.                                                         | Suitable for real-time communication such as voice and video.                                                       |
| An error in one ciphertext block may affect the entire block (and sometimes the next block depending on the mode). | A bit error usually affects only the corresponding bit (synchronous) or a few subsequent bits (self-synchronizing). |
| Requires padding if the final block is shorter than the block size (depending on the mode).                        | Does **not** require padding.                                                                                       |
| Examples: **AES**, **DES**, **3DES**                                                                               | Examples: **ChaCha20**, **RC4** (historical)                                                                        |

---

## Simple Comparison

| Feature            | Block Cipher          | Stream Cipher           |
| ------------------ | --------------------- | ----------------------- |
| Unit of encryption | Block                 | Bit/Byte                |
| Speed              | Slower                | Faster                  |
| Padding required   | Yes (usually)         | No                      |
| Best for           | Files and stored data | Real-time communication |
| Main operation     | Encryption rounds     | XOR with keystream      |

---

## Easy Diagram

### Block Cipher

```text
Plaintext
+--------+--------+--------+
| Block1 | Block2 | Block3 |
+--------+--------+--------+
     │        │        │
     ▼        ▼        ▼
 Encrypt  Encrypt  Encrypt
     │        │        │
     ▼        ▼        ▼
Cipher1  Cipher2  Cipher3
```

---

### Stream Cipher

```text
Plaintext : P1 P2 P3 P4 P5 ...
               │  │  │  │  │
Keystream : K1 K2 K3 K4 K5 ...
               │  │  │  │  │
             XOR XOR XOR XOR XOR
               │  │  │  │  │
Ciphertext: C1 C2 C3 C4 C5 ...
```

---

## Exam Definition (2 Marks)

### Block Cipher

> **A Block Cipher is a symmetric encryption algorithm that encrypts data in fixed-size blocks (such as 128 bits) using a secret key.**

### Stream Cipher

> **A Stream Cipher is a symmetric encryption algorithm that encrypts data one bit or one byte at a time by XORing the plaintext with a pseudorandom keystream.**

---

## Easy Memory Trick ⭐

```text
Block  = Whole Block at a Time 📦
Stream = One Bit (or Byte) at a Time 💧
```

Think of it like this:

* 📦 **Block Cipher** → Encrypts a **box** of data at once.
* 💧 **Stream Cipher** → Encrypts data like a **flowing stream**, one bit or byte at a time.
