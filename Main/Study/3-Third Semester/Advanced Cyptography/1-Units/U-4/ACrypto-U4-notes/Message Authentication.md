#third-semester #advanced-cryptography 

# Q. What is Message Authentication? Explain its objectives and methods.

## Answer

# Introduction

When a message is transmitted over a network, an attacker may **modify**, **delete**, **insert**, or **impersonate** the sender. Therefore, the receiver must verify that the message is genuine and has not been altered. This process is called **message authentication**.

---

# Definition

**Message Authentication** is the process of verifying that:

1. The message **comes from the claimed sender (authentication/origin authentication)**.
2. The message **has not been modified during transmission (integrity)**.

It ensures that the received message is genuine and trustworthy.

> **Note:** Message authentication **does not provide confidentiality** unless encryption is also used.

---

# Objectives of Message Authentication

The main objectives are:

### 1. Data Integrity

Ensures that the message has not been altered during transmission.

Example:

```
Original:
Pay Rs. 1000

Modified:
Pay Rs. 9000
```

Message authentication detects such changes.

---

### 2. Source Authentication (Origin Authentication)

Ensures that the message was sent by the claimed sender.

Example:

Bob verifies that the message really came from Alice and not from an attacker.

---

### 3. Detect Message Modification

Detects if anyone has:

* Modified
* Deleted
* Inserted
* Reordered

any part of the message.

---

# How Message Authentication Works

### Step 1: Sender

The sender generates an authentication value (MAC or Digital Signature) from the message.

```text
Message
     │
     ▼
MAC / Digital Signature Algorithm
     │
     ▼
Authentication Code
```

The sender transmits:

* Message
* Authentication code

---

### Step 2: Receiver

The receiver generates a new authentication code from the received message.

```text
Received Message
       │
       ▼
Same MAC / Signature Algorithm
       │
       ▼
New Authentication Code
```

---

### Step 3: Verification

The receiver compares both authentication codes.

```
Authentication Codes Match

↓

Message is authentic.
```

If they differ,

```
Authentication Codes Do Not Match

↓

Message has been modified or is from an invalid sender.
```

---

# Diagram

```text
                 Sender

 Message
    │
    ▼
Generate MAC / Digital Signature
    │
    ▼
Authentication Code
    │
    ├──────────────┐
    ▼              ▼
 Message        Auth Code
      (Sent Together)

=================================

               Receiver

Received Message
        │
        ▼
Generate New MAC / Signature
        │
        ▼
New Auth Code

Compare

Equal → Authentic

Not Equal → Reject
```

---

# Methods of Message Authentication

### 1. Message Authentication Code (MAC)

* Uses a **shared secret key**.
* Provides:

  * Authentication
  * Integrity
* Does **not** provide non-repudiation because both parties know the same key.

---

### 2. Digital Signature

* Uses **public-key cryptography**.
* Provides:

  * Authentication
  * Integrity
  * Non-repudiation

---

# Security Services Provided

Message authentication provides:

* ✅ Authentication
* ✅ Data Integrity

It does **not** provide:

* ❌ Confidentiality (unless combined with encryption)

---

# Applications

* Online banking
* Secure email
* E-commerce transactions
* VPN communication
* SSL/TLS protocols
* API authentication

---

# Advantages

* Detects message tampering
* Verifies the sender's identity
* Prevents impersonation attacks
* Ensures trustworthy communication

---

# Limitations

* Does not hide the message contents.
* Requires secure key management (for MAC).
* If the secret key is compromised, authentication can be forged.

---

# Difference: Authentication vs Message Authentication

| Authentication                            | Message Authentication                                               |
| ----------------------------------------- | -------------------------------------------------------------------- |
| Verifies the identity of a user or device | Verifies the sender **and** the integrity of a message               |
| Example: Login with username/password     | Example: Verifying a received email using a MAC or digital signature |

---

# Difference: Message Authentication vs Confidentiality

| Message Authentication        | Confidentiality               |
| ----------------------------- | ----------------------------- |
| Verifies sender and integrity | Protects message secrecy      |
| Uses MAC or Digital Signature | Uses Encryption               |
| Detects modification          | Prevents unauthorized reading |

---

# Key Points to Remember

* **Message Authentication = Authentication + Integrity**
* It verifies **who sent the message** and **whether the message has been changed**.
* It **does not provide confidentiality**.
* It is commonly implemented using **MACs** and **Digital Signatures**.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define message authentication.
2. What are the objectives of message authentication?
3. Does message authentication provide confidentiality? Explain.
4. List two methods of message authentication.
5. Differentiate between authentication and message authentication.

### Long Questions (8–10 Marks)

1. **What is message authentication? Explain its objectives and working with a neat diagram.**
2. **Describe the methods used for message authentication.**
3. **Differentiate between message authentication and confidentiality.**
4. **Explain the role of MACs and digital signatures in message authentication.**

### Memory Trick

* **Confidentiality** → **Who can read it?** → Encryption 🔒
* **Authentication** → **Who are you?** → Password/OTP/Fingerprint 👤
* **Message Authentication** → **Who sent it, and was it changed?** → MAC/Digital Signature ✅
