
#advanced-cryptography #third-semester 

# DAA (Data Authentication Algorithm)

> **Exam Importance:** ⭐⭐⭐⭐ (5 Marks)

---

# Q. What is DAA (Data Authentication Algorithm)? Explain its working with a neat diagram.

---

# Answer

## Introduction

The **Data Authentication Algorithm (DAA)** is a **Message Authentication Code (MAC)** algorithm based on the **Data Encryption Standard (DES)** block cipher. It is used to verify the **authenticity** and **integrity** of a message.

DAA processes the message using the **Cipher Block Chaining (CBC)** mode of DES and uses the **last ciphertext block** as the MAC.

It was standardized by **ANSI X9.9** for authentication in banking applications.

---

# Definition

**DAA (Data Authentication Algorithm)** is a MAC algorithm that uses the **DES block cipher in CBC mode** to generate a fixed-length authentication code. The final ciphertext block is used as the **MAC**.

---

# Working of DAA

Assume:

* $M = M_1, M_2, \ldots, M_n$ = Message blocks
* $K$ = Secret DES key
* $E_K$ = DES encryption using key $K$

---

## Step 1: Divide the Message

The message is divided into **64-bit blocks**, since DES operates on 64-bit blocks.

```text
M1 | M2 | M3 | ... | Mn
```

---

## Step 2: Initialize IV

The Initialization Vector (IV) is set to **all zeros**.

$$
C_0 = 0
$$

---

## Step 3: Process the First Block

The first message block is XORed with the IV and encrypted.

$$
C_1 = E_K(M_1 \oplus C_0)
$$

---

## Step 4: Process Remaining Blocks

Each subsequent message block is XORed with the previous ciphertext block and then encrypted.

$$
C_i = E_K(M_i \oplus C_{i-1})
$$

This process continues until all message blocks have been processed.

---

## Step 5: Generate the MAC

After processing the final block, the **last ciphertext block** is taken as the MAC.

$$
\boxed{\text{MAC} = C_n}
$$

The sender sends:

* Message
* MAC

---

## Step 6: Verification

The receiver performs the same DAA computation using the **same secret key**.

* If the computed MAC matches the received MAC, the message is accepted.
* Otherwise, it is rejected.

---

# Working Diagram

```text
             IV = 0
                │
                ▼
M1 ──⊕────► DES Encrypt(K) ───► C1
                ▲
                │

M2 ──⊕────► DES Encrypt(K) ───► C2
                ▲
                │

M3 ──⊕────► DES Encrypt(K) ───► C3
                ▲
                │

              ...

Mn ──⊕────► DES Encrypt(K) ───► Cn
                                     │
                                     ▼
                              MAC = Cn
```

---

# Security Services Provided

DAA provides:

* ✅ Authentication
* ✅ Integrity

It does **not** provide:

* ❌ Confidentiality
* ❌ Non-repudiation

---

# Advantages

* Simple and efficient.
* Uses the well-known DES algorithm.
* Detects message modification.
* Suitable for banking and financial systems.

---

# Limitations

* Based on **DES**, which is now considered insecure due to its **56-bit key**.
* Does not provide confidentiality.
* Requires both parties to share the same secret key.
* Largely replaced by **HMAC** and **CMAC** in modern systems.

---

# Applications

DAA was used in:

* Banking systems
* Financial transaction authentication
* Electronic funds transfer (EFT)
* Payment card systems

---

# DAA vs HMAC

| DAA                       | HMAC                           |
| ------------------------- | ------------------------------ |
| Based on DES block cipher | Based on a hash function       |
| Uses CBC mode             | Uses nested hashing            |
| Uses 64-bit DES blocks    | Can use SHA-256, SHA-512, etc. |
| Older algorithm           | Modern and more secure         |

---

# Key Points to Remember

* DAA is a **MAC algorithm based on DES**.
* Uses **CBC mode** of DES.
* **IV is initialized to zero**.
* The **last ciphertext block** is the MAC.
* Provides **authentication** and **integrity**, but **not confidentiality**.
* Has been largely replaced by more secure algorithms such as **HMAC** and **CMAC**.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define DAA.
2. Which block cipher is used in DAA?
3. What is the output of the DAA algorithm?
4. What security services does DAA provide?

### Long Questions (8–10 Marks)

1. **Explain the working of DAA with a neat diagram.**
2. **Discuss the advantages and limitations of DAA.**
3. **Differentiate between DAA and HMAC.**

---

# Memory Trick

Remember the flow:

```text
Message Blocks
      │
      ▼
XOR with Previous Ciphertext
      │
      ▼
DES Encryption
      │
      ▼
Ciphertext Block
      │
      ▼
Last Ciphertext = MAC
```

The important formulas are:

$$
C_0 = 0
$$

$$
C_i = E_K(M_i \oplus C_{i-1})
$$

$$
\boxed{\text{MAC} = C_n}
$$

**Easy way to remember:** DAA works almost exactly like **CBC-MAC**, except it specifically uses the **DES block cipher** to generate the authentication code.
