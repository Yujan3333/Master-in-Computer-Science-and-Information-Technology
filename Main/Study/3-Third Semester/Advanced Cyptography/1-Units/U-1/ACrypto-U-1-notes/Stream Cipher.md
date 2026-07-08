#third-semester #advanced-cryptography 

# Stream Cipher

A **Stream Cipher** is a type of **symmetric key encryption** in which **plaintext is encrypted one bit or one byte at a time**, instead of encrypting a whole block of data.

It is widely used for **real-time communication** because it is fast and efficient.

---

# Simple Definition (Exam)

> **A Stream Cipher is a symmetric encryption algorithm that encrypts plaintext one bit or one byte at a time by combining it with a pseudorandom keystream using the XOR operation.**

---

# How Stream Cipher Works

A stream cipher generates a **keystream** (a sequence of random-looking bits).

Each plaintext bit is XORed with the corresponding keystream bit.

Encryption:

$$
C=P\oplus K
$$

Decryption:

$$
P=C\oplus K
$$

where:

* **$P$** = Plaintext
* **$K$** = Keystream
* **$C$** = Ciphertext
* **$\oplus$** = XOR

---

# Simple Example

### Plaintext

```text id="2dxxof"
10110010
```

### Keystream

```text id="9cljtl"
11001010
```

### Encryption (XOR)

```text id="d8i4ny"
Plaintext : 10110010
Keystream : 11001010
--------------------
Ciphertext: 01111000
```

---

### Decryption

```text id="5yyqao"
Ciphertext: 01111000
Keystream : 11001010
--------------------
Plaintext : 10110010
```

The original plaintext is recovered because:

$$
(P\oplus K)\oplus K=P
$$

---

# Diagram

```text id="kz0ezq"
Plaintext
     │
     ▼
  XOR ◄──── Keystream Generator
     │
     ▼
Ciphertext
```

---

# Types of Stream Cipher

## 1. [Synchronous Stream Cipher](Synchronous%20Stream%20Cipher.md)

* The keystream is generated **independently** of the plaintext and ciphertext.
* Both sender and receiver must stay synchronized.

**Example:** RC4 (historically)

---

## 2. [Self-Synchronizing (Asynchronous) Stream Cipher](Self-Synchronizing%20(Asynchronous)%20Stream%20Cipher.md)

* The keystream depends on previous ciphertext bits.
* If synchronization is lost, it automatically recovers after a few characters.

---

# Advantages

* Very fast encryption and decryption.
* Suitable for real-time communication (voice, video, live streaming).
* Uses less memory.
* No need to wait for an entire block of data.

---

# Disadvantages

* Reusing the same keystream is insecure.
* Errors in key generation affect security.
* Some older stream ciphers (like RC4) have known weaknesses.

---

# Stream Cipher vs Block Cipher

| Stream Cipher                       | Block Cipher                                  |
| ----------------------------------- | --------------------------------------------- |
| Encrypts one bit or byte at a time. | Encrypts a fixed-size block (e.g., 128 bits). |
| Faster for continuous data.         | Better for files and stored data.             |
| Uses a keystream and XOR.           | Uses multiple encryption rounds.              |
| Example: RC4 (historical), ChaCha20 | Example: AES, DES                             |

---

# Applications

* Secure messaging
* Video streaming
* Voice over IP (VoIP)
* Wireless communication
* VPNs

---

# Exam Definition (2 Marks)

> **A Stream Cipher is a symmetric key encryption algorithm that encrypts data one bit or one byte at a time by XORing the plaintext with a pseudorandom keystream. The same keystream is used during decryption to recover the original plaintext.**

---

# Easy Memory Trick ⭐

Remember:

```text id="h0pwt8"
Stream = One Bit (or Byte) at a Time
Block = Whole Block at a Time
```

And remember the formula:

$$
\boxed{Ciphertext=Plaintext \oplus Keystream}
$$

This is the key concept of a **Stream Cipher** and is the most important point for exams.
