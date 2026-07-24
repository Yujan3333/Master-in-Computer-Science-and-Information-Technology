#advanced-cryptography #third-semester 


## Q. What is a Message Authentication Code (MAC)? Explain its working with a neat diagram.

---

# Answer

## Definition

A **Message Authentication Code (MAC)** is a cryptographic technique that uses a **shared secret key** and a **message** to generate a fixed-size authentication value called a **MAC tag**.

The receiver uses the **same secret key** to verify the MAC and determine whether the message is authentic and has not been modified.

---

# Objectives of MAC

A Message Authentication Code provides:

* **Authentication** – Verifies that the message comes from the legitimate sender.
* **Integrity** – Ensures that the message has not been modified during transmission.

It does **not** provide:

* ❌ Confidentiality
* ❌ Non-repudiation

---

# Working of MAC

### Step 1: Sender

The sender combines:

* Message ($M$)
* Secret Key ($K$)

and computes the MAC.

$$
\text{MAC} = f(K, M)
$$

The sender sends:

* Message ($M$)
* MAC

---

### Step 2: Receiver

The receiver receives:

* Message ($M$)
* MAC

Using the **same secret key ($K$)**, the receiver computes a new MAC.

$$
\text{MAC}' = f(K, M)
$$

---

### Step 3: Verification

The receiver compares the received MAC with the computed MAC.

* If both MACs are equal → The message is authentic and unchanged.
* If they differ → The message has been modified or is from an unauthorized sender.

---

# Diagram

```text
              Sender

 Message (M)
      │
Secret Key (K)
      │
      ▼
 MAC Algorithm
      │
      ▼
     MAC
      │
      ├───────────────┐
      ▼               ▼
  Message (M)       MAC
      (Sent Together)

====================================

             Receiver

Message (M)          Received MAC
      │                  │
Secret Key (K)           │
      │                  │
      ▼                  │
 MAC Algorithm           │
      │                  │
      ▼                  │
 Computed MAC            │
         └──────Compare──┘

Equal → Accept Message

Not Equal → Reject Message
```

---

# Characteristics of MAC

* Uses a **shared secret key**.
* Provides **authentication** and **integrity**.
* Detects message tampering.
* Produces a fixed-length MAC tag.
* Efficient and fast to compute.

---

# Advantages

* Verifies the sender's authenticity.
* Detects message modification.
* Fast and efficient.
* Simple to implement.

---

# Limitations

* Does not provide confidentiality.
* Does not provide non-repudiation because both sender and receiver share the same secret key.
* Requires secure key distribution.

---

# Applications

* Online banking
* Secure communication protocols
* API authentication
* SSL/TLS
* VPNs
* Network security protocols

---

# Difference Between MAC and Hash Function

| Hash Function               | MAC                                                |
| --------------------------- | -------------------------------------------------- |
| Does not use a secret key   | Uses a shared secret key                           |
| Provides integrity only     | Provides integrity and authentication              |
| Anyone can compute the hash | Only users with the secret key can compute the MAC |

---

# Key Points to Remember

* MAC = **Message + Secret Key**
* Uses the **same secret key** for generation and verification.
* Provides **Authentication + Integrity**.
* Does **not** provide **Confidentiality** or **Non-repudiation**.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define Message Authentication Code (MAC).
2. What security services does a MAC provide?
3. Why does a MAC require a secret key?
4. Differentiate between a MAC and a hash function.

### Memory Trick

Remember:

```text
MAC

↓

Message + Secret Key

↓

MAC Tag

↓

Authentication + Integrity
```

**Easy Formula:**

$$
\boxed{\text{MAC} = f(K, M)}
$$

where:

* $K$ = Secret key
* $M$ = Message
* MAC = Authentication code
