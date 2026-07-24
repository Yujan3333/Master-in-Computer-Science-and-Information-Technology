#advanced-cryptography #third-semester 

# CBC-MAC (Cipher Block Chaining Message Authentication Code)

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Important – 5 Marks)

---

# Q. What is CBC-MAC? Explain its working with a neat diagram.

---

# Answer

## Definition

**CBC-MAC (Cipher Block Chaining Message Authentication Code)** is a **Message Authentication Code (MAC)** algorithm based on the **Cipher Block Chaining (CBC)** mode of a block cipher (such as AES or DES).

It uses a **shared secret key** to generate a fixed-length MAC that verifies the **authenticity** and **integrity** of a message.

---

# Principle

CBC-MAC works similarly to CBC encryption, but:

* The message is **not encrypted for confidentiality**.
* Only the **last ciphertext block** is used as the MAC.

Thus, the final ciphertext block becomes the **authentication tag (MAC)**.

---

# Working of CBC-MAC

Assume:

* $M = M_1, M_2, \ldots, M_n$ (message blocks)
* $K$ = Shared secret key
* $E_K$ = Block cipher encryption using key $K$

---

## Step 1: Divide the Message

Divide the message into fixed-size blocks.

```text id="j3r3ho"
M1 | M2 | M3 | ... | Mn
```

---

## Step 2: Initialize

Set the Initialization Vector (IV) to **all zeros**.

$$
C_0 = 0
$$

---

## Step 3: Process Each Block

For the first block,

$$
C_1 = E_K(M_1 \oplus C_0)
$$

For the second block,

$$
C_2 = E_K(M_2 \oplus C_1)
$$

Continue until the last block,

$$
C_n = E_K(M_n \oplus C_{n-1})
$$

---

## Step 4: Generate MAC

The **last ciphertext block** is the MAC.

$$
\boxed{\text{MAC} = C_n}
$$

The sender transmits:

* Message
* MAC

---

## Step 5: Verification

The receiver repeats the same CBC-MAC computation using the **same secret key**.

* If the computed MAC matches the received MAC, the message is authentic.
* Otherwise, the message is rejected.

---

# Working Diagram

```text id="0gk0jx"
          IV = 0
             │
             ▼
 M1 ──⊕────► Encrypt(K) ───► C1
             ▲
             │

 M2 ──⊕────► Encrypt(K) ───► C2
             ▲
             │

 M3 ──⊕────► Encrypt(K) ───► C3
             ▲
             │

            ...

 Mn ──⊕────► Encrypt(K) ───► Cn

                    │
                    ▼
               MAC = Cn
```

---

# Why is the Last Ciphertext Used?

Each ciphertext block depends on:

* The current message block.
* The previous ciphertext block.

Therefore, the final ciphertext block depends on **all previous message blocks**.

If any block changes, the final MAC also changes.

---

# Security Services Provided

CBC-MAC provides:

* ✅ Message Authentication
* ✅ Data Integrity

It does **not** provide:

* ❌ Confidentiality
* ❌ Non-repudiation

---

# Advantages

* Simple and efficient.
* Uses existing block ciphers (AES/DES).
* Detects message modification.
* Suitable for fixed-length messages.

---

# Limitations

* Does **not** provide confidentiality.
* Secure mainly for **fixed-length messages**.
* Not suitable for variable-length messages without additional modifications.
* Requires a shared secret key.

---

# Applications

CBC-MAC is used in:

* Secure communication protocols.
* Banking systems.
* Wireless security protocols.
* Embedded systems.
* Authentication in block cipher-based systems.

---

# CBC-MAC vs HMAC

| CBC-MAC                           | HMAC                                        |
| --------------------------------- | ------------------------------------------- |
| Based on a block cipher (AES/DES) | Based on a hash function (SHA-256, SHA-512) |
| Uses CBC mode                     | Uses nested hashing                         |
| Best for fixed-length messages    | Works for messages of any length            |
| Authentication and integrity      | Authentication and integrity                |

---

# Key Points to Remember

* CBC-MAC is based on the **CBC mode** of a block cipher.
* Uses a **shared secret key**.
* The **IV is fixed to zero**.
* The **last ciphertext block** is the MAC.
* Provides **authentication** and **integrity** only.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define CBC-MAC.
2. Why is the IV set to zero in CBC-MAC?
3. Which block is used as the MAC in CBC-MAC?
4. What security services are provided by CBC-MAC?

### Long Questions (8–10 Marks)

1. **Explain the working of CBC-MAC with a neat diagram.**
2. **Discuss the advantages and limitations of CBC-MAC.**
3. **Differentiate between CBC-MAC and HMAC.**

---

# Memory Trick

Remember the flow:

```text id="pxs2l8"
IV = 0
   │
   ▼
M1 ⊕ IV
   │
Encrypt
   │
C1
   │
M2 ⊕ C1
   │
Encrypt
   │
C2
   │
...
   │
Cn
   │
▼
MAC
```

The most important formulas are:

$$
C_0 = 0
$$

$$
C_i = E_K(M_i \oplus C_{i-1})
$$

$$
\boxed{\text{MAC} = C_n}
$$

These three equations summarize the complete working of **CBC-MAC**.
