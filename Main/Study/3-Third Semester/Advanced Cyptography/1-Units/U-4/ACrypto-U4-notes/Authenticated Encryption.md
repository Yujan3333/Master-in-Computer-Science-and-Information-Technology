#advanced-cryptography #third-semester 

# Authenticated Encryption (AE)

> **Exam Importance:** ⭐⭐⭐⭐ (5 Marks)

---

# Q. What is Authenticated Encryption? Explain its working with a neat diagram.

---

# Answer

## Introduction

In secure communication, **encryption alone is not sufficient**. While encryption provides **confidentiality**, it cannot detect whether the ciphertext has been modified. Similarly, a **MAC** provides **authentication** and **integrity**, but it does not hide the message.

**Authenticated Encryption (AE)** combines **encryption** and **message authentication** into a single mechanism, providing both **confidentiality** and **authentication**.

---

# Definition

**Authenticated Encryption (AE)** is a cryptographic technique that simultaneously provides:

* **Confidentiality** (by encrypting the message)
* **Authentication** (verifying the sender)
* **Integrity** (detecting message modification)

It combines an **encryption algorithm** with a **Message Authentication Code (MAC)**.

---

# Why is Authenticated Encryption Needed?

Using only encryption:

* ✔ Keeps the message secret.
* ❌ Cannot detect if the ciphertext has been modified.

Using only MAC:

* ✔ Detects message modification.
* ✔ Authenticates the sender.
* ❌ Does not hide the message.

Authenticated Encryption provides both.

---

# Working of Authenticated Encryption

Assume:

* $M$ = Message
* $K_E$ = Encryption key
* $K_M$ = MAC key

---

## Step 1: Encrypt the Message

The sender encrypts the plaintext.

$$
C = E_{K_E}(M)
$$

where:

* $M$ = Plaintext
* $C$ = Ciphertext

---

## Step 2: Generate the MAC

The sender computes a MAC on the ciphertext (or, in some schemes, on the plaintext).

$$
T = \text{MAC}(K_M, C)
$$

where:

* $T$ = Authentication tag

---

## Step 3: Send the Data

The sender sends:

* Ciphertext ($C$)
* Authentication Tag ($T$)

---

## Step 4: Verification

The receiver computes a new MAC on the received ciphertext using the same MAC key.

If

$$
T_{\text{received}} = T_{\text{computed}}
$$

the message is authentic and has not been modified.

Otherwise, the message is rejected.

---

## Step 5: Decryption

If the MAC verification is successful, the receiver decrypts the ciphertext.

$$
M = D_{K_E}(C)
$$

---

# Working Diagram

```text
              Sender

Plaintext (M)
      │
      ▼
Encryption
      │
      ▼
Ciphertext (C)
      │
      ├───────────────┐
      │               │
      ▼               ▼
   MAC Algorithm     Ciphertext
      │
      ▼
Authentication Tag (T)

Send → (Ciphertext, Tag)

====================================

             Receiver

Ciphertext + Tag
      │
      ▼
 MAC Verification
      │
      ▼
Tag Valid?

Yes ─────────► Decrypt ─────────► Plaintext

No ──────────► Reject Message
```

---

# Security Services Provided

Authenticated Encryption provides:

* ✅ Confidentiality
* ✅ Authentication
* ✅ Integrity

It does **not** provide:

* ❌ Non-repudiation (because both parties may share the same secret key)

---

# Advantages

* Provides confidentiality and authentication together.
* Detects message tampering.
* Protects against forgery attacks.
* More secure than using encryption alone.

---

# Limitations

* Requires secret key management.
* Slightly higher computational cost than encryption alone.
* Does not provide non-repudiation.

---

# Applications

Authenticated Encryption is widely used in:

* TLS/SSL
* VPNs (IPsec)
* Wireless security (WPA2/WPA3)
* Secure messaging applications
* Cloud storage security

---

# Encryption vs MAC vs Authenticated Encryption

| Feature         | Encryption | MAC | Authenticated Encryption |
| --------------- | ---------- | --- | ------------------------ |
| Confidentiality | ✅          | ❌   | ✅                        |
| Integrity       | ❌          | ✅   | ✅                        |
| Authentication  | ❌          | ✅   | ✅                        |
| Non-repudiation | ❌          | ❌   | ❌                        |

---

# Key Points to Remember

* **Encryption** hides the message.
* **MAC** verifies the message.
* **Authenticated Encryption** does both.
* Provides **Confidentiality + Authentication + Integrity**.
* Common implementations include **AES-GCM** and **ChaCha20-Poly1305**.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define Authenticated Encryption.
2. Why is Authenticated Encryption needed?
3. What security services are provided by Authenticated Encryption?
4. Differentiate between encryption and Authenticated Encryption.

### Long Questions (8–10 Marks)

1. **Explain the working of Authenticated Encryption with a neat diagram.**
2. **Discuss the advantages and applications of Authenticated Encryption.**
3. **Differentiate between Encryption, MAC, and Authenticated Encryption.**

---

# Memory Trick

Remember:

```text
Encryption
      │
      ▼
Ciphertext
      │
      ▼
MAC
      │
      ▼
Authentication Tag
```

**Easy Formula:**

$$
C = E_{K_E}(M)
$$

$$
T = \text{MAC}(K_M, C)
$$

The sender transmits:

$$
(C,;T)
$$

Think of it as:

* 🔒 **Encryption** → Keeps the message **secret**.
* 🛡️ **MAC** → Ensures the message is **authentic** and **unchanged**.
* ✅ **Authenticated Encryption** → Provides **Confidentiality + Integrity + Authentication** in one system.
