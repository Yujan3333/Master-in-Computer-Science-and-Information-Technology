#advanced-cryptography #third-semester 

# Digital Signature

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Important)

---

# Q. What is a Digital Signature? Explain its working with a neat diagram. Mention its advantages and applications.

---

# Answer

## Introduction

In electronic communication, it is important to verify the identity of the sender and ensure that the message has not been modified. A **digital signature** provides a way to authenticate the sender, verify the integrity of the message, and prevent the sender from denying that they sent the message.

Unlike a handwritten signature, a digital signature is created using **public-key cryptography**.

---

# Definition

A **Digital Signature** is a cryptographic technique that uses a **private key** to sign a message and a **public key** to verify the signature.

It provides:

* **Authentication** (verifies the sender)
* **Integrity** (detects message modification)
* **Non-repudiation** (the sender cannot deny sending the message)

> **Important:** A digital signature **does not provide confidentiality**. If confidentiality is required, the message must also be encrypted.

---

# Objectives of a Digital Signature

A digital signature provides the following security services:

1. **Authentication** – Confirms the identity of the sender.
2. **Integrity** – Ensures the message has not been altered.
3. **Non-repudiation** – Prevents the sender from denying that they signed the message.

It **does not** provide:

* ❌ Confidentiality

---

# Working of a Digital Signature

A digital signature has two phases:

## Phase 1: Signature Generation (Sender)

1. Alice writes the message (M).
2. Alice computes the hash of the message.

$$
h = H(M)
$$

3. Alice encrypts the hash using **her private key**.

$$
S = E_{\text{Private}}(h)
$$

This encrypted hash is the **digital signature**.

4. Alice sends:

* Message (M)
* Digital Signature (S)

---

## Phase 2: Signature Verification (Receiver)

1. Bob receives the message and signature.
2. Bob computes the hash of the received message.

$$
h_1 = H(M)
$$

3. Bob decrypts the received signature using **Alice's public key**.

$$
h_2 = D_{\text{Public}}(S)
$$

4. Bob compares:

* ($h_1$)
* ($h_2$)

If

$$
h_1 = h_2
$$

then:

* The message is authentic.
* The message has not been modified.
* The signature is valid.

Otherwise, the signature is invalid.

---

# Working Diagram

```text
                  Sender (Alice)

Message (M)
     │
     ▼
Hash Function
     │
     ▼
Hash Value
     │
Encrypt with Alice's Private Key
     │
     ▼
Digital Signature
     │
     ├─────────────────────────┐
     ▼                         ▼
Message (M)              Digital Signature
         (Sent Together)

==============================================

                 Receiver (Bob)

Message (M)                     Signature
     │                              │
     ▼                              ▼
Hash Function          Decrypt with Alice's Public Key
     │                              │
     ▼                              ▼
Computed Hash               Received Hash

        Compare

Computed Hash = Received Hash

Yes → Valid Signature

No → Invalid Signature
```

---

# Why is a Hash Used?

Instead of signing the entire message:

* Hashing is much faster.
* The hash is fixed in size.
* Any change in the message changes the hash (avalanche effect).

Therefore, digital signatures usually sign the **hash of the message**, not the whole message.

---

# Security Services Provided

| Security Service | Provided? |
| ---------------- | --------- |
| Authentication   | ✅ Yes     |
| Integrity        | ✅ Yes     |
| Non-repudiation  | ✅ Yes     |
| Confidentiality  | ❌ No      |

---

# Advantages

* Verifies the sender's identity.
* Detects message modification.
* Prevents forgery and impersonation.
* Provides non-repudiation.
* Legally accepted in many countries.
* Used in secure online transactions.

---

# Limitations

* Does not provide confidentiality.
* Requires a Public Key Infrastructure (PKI) or trusted public keys.
* If the private key is compromised, signatures can be forged.

---

# Applications

* Electronic documents
* Secure email
* Online banking
* E-commerce
* Software code signing
* Digital certificates
* Blockchain and cryptocurrencies

---

# Digital Signature vs Handwritten Signature

| Digital Signature                       | Handwritten Signature        |
| --------------------------------------- | ---------------------------- |
| Created using cryptographic algorithms  | Written by hand              |
| Difficult to forge                      | Can be forged                |
| Verifies identity and message integrity | Verifies identity only       |
| Can be verified electronically          | Requires manual verification |

---

# Digital Signature vs MAC

| Digital Signature                     | MAC                                     |
| ------------------------------------- | --------------------------------------- |
| Uses public/private key pair          | Uses a shared secret key                |
| Provides authentication               | Provides authentication                 |
| Provides integrity                    | Provides integrity                      |
| Provides non-repudiation              | Does **not** provide non-repudiation    |
| Anyone with the public key can verify | Only parties sharing the key can verify |

---

# Key Points to Remember

* A digital signature signs the **hash** of a message.
* **Private key** is used for signing.
* **Public key** is used for verification.
* It provides **authentication**, **integrity**, and **non-repudiation**.
* It does **not** provide confidentiality by itself.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define a digital signature.
2. What are the objectives of a digital signature?
3. Which key is used for signing and which key is used for verification?
4. Why is a hash function used in digital signatures?
5. Does a digital signature provide confidentiality? Explain.

---

### Long Questions (8–10 Marks)

1. **What is a digital signature? Explain its working with a neat diagram.**
2. **Discuss the security services provided by a digital signature.**
3. **Differentiate between a digital signature and a Message Authentication Code (MAC).**
4. **Explain the role of hash functions in digital signatures.**

---

# Memory Trick

Remember the phrase:

> **"Sign with Private, Verify with Public."**

* 🔑 **Private Key** → Creates the digital signature.
* 🌐 **Public Key** → Verifies the digital signature.

And remember the security services:

* ✅ Authentication
* ✅ Integrity
* ✅ Non-repudiation
* ❌ Confidentiality
