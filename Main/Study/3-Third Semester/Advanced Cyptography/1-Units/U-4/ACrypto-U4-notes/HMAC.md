#advanced-cryptography #third-semester 


-[HMAC](https://www.youtube.com/watch?v=sxWxCtJ3og0)
# HMAC (Hash-based Message Authentication Code)

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Important – 5 to 10 Marks)

---

# Q. What is HMAC? Explain its working with a neat diagram.

---

# Answer

## Introduction

A **Hash-based Message Authentication Code (HMAC)** is a message authentication technique that combines a **cryptographic hash function** (such as SHA-256 or SHA-512) with a **secret key**.

HMAC is used to verify both the **authenticity** and **integrity** of a message. It is widely used in **SSL/TLS**, **IPsec**, **AWS APIs**, and many other security protocols.

---

# Definition

**HMAC (Hash-based Message Authentication Code)** is a cryptographic algorithm that uses a **secret key** and a **hash function** to generate a fixed-length authentication code.

It ensures:

* Authentication
* Integrity

It does **not** provide:

* ❌ Confidentiality
* ❌ Non-repudiation

---

# Components of HMAC

HMAC uses:

* Secret Key ($K$)
* Message ($M$)
* Hash Function ($H$)
* Inner Padding (**ipad**)
* Outer Padding (**opad**)

where

* **ipad** = Repeated byte **0x36**
* **opad** = Repeated byte **0x5C**

---

# HMAC Formula

The HMAC value is computed as

$$
\boxed{\text{HMAC}(K,M)=H\left((K\oplus opad);||;H((K\oplus ipad);||;M)\right)}
$$

where

* $H$ = Hash function
* $K$ = Secret key
* $M$ = Message
* $\oplus$ = XOR operation
* $||$ = Concatenation

---

# Working of HMAC

### Step 1

Prepare the secret key.

If the key is longer than the hash block size, it is first hashed.

If it is shorter, it is padded with zeros.

---

### Step 2

Generate the Inner Key

XOR the key with **ipad**.

$$
K_i = K \oplus ipad
$$

---

### Step 3

Compute the Inner Hash

Append the message to the inner key.

$$
\text{Inner Hash}=H(K_i||M)
$$

---

### Step 4

Generate the Outer Key

XOR the key with **opad**.

$$
K_o = K \oplus opad
$$

---

### Step 5

Compute the Final HMAC

Append the inner hash to the outer key.

$$
\text{HMAC}=H(K_o||\text{Inner Hash})
$$

This final value is sent along with the message.

---

# Working Diagram

```text id="5hjpqi"
                 Secret Key (K)
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
      K ⊕ ipad                  K ⊕ opad
          │                         │
          ▼                         │
      Append Message                │
          │                         │
          ▼                         │
      Hash Function                 │
          │                         │
     Inner Hash ────────────────────┘
                    │
                    ▼
             Hash Function
                    │
                    ▼
                 HMAC
```

---

# Verification

The receiver:

1. Receives the message and HMAC.
2. Uses the **same secret key**.
3. Computes a new HMAC.
4. Compares it with the received HMAC.

* Equal → Message is authentic and unchanged.
* Not Equal → Reject the message.

---

# Why Two Hash Operations?

HMAC uses **two hash operations**:

* **Inner Hash** protects the message.
* **Outer Hash** protects against attacks on the hash function and strengthens security.

This design makes HMAC much more secure than simply computing:

$$
H(K||M)
$$

---

# Security Services Provided

HMAC provides:

* ✅ Authentication
* ✅ Integrity

It does **not** provide:

* ❌ Confidentiality
* ❌ Non-repudiation

---

# Advantages

* Very secure.
* Resistant to collision attacks.
* Fast and efficient.
* Can use existing hash functions (SHA-256, SHA-512, SHA-3).
* Widely standardized and deployed.

---

# Limitations

* Requires a shared secret key.
* Does not encrypt the message.
* Does not provide non-repudiation because both parties know the same key.

---

# Applications

HMAC is widely used in:

* SSL/TLS
* IPsec
* HTTPS
* AWS API authentication
* OAuth
* Digital certificates
* Secure communication protocols

---

# HMAC vs MAC

| HMAC                           | MAC                                       |
| ------------------------------ | ----------------------------------------- |
| Based on a hash function       | Can be based on any algorithm             |
| Uses SHA-256, SHA-512, etc.    | May use block ciphers or hash functions   |
| Highly secure and standardized | General concept of message authentication |

---

# HMAC vs CBC-MAC

| HMAC                                  | CBC-MAC                               |
| ------------------------------------- | ------------------------------------- |
| Uses a hash function                  | Uses a block cipher                   |
| Suitable for variable-length messages | Best suited for fixed-length messages |
| Uses ipad and opad                    | Uses CBC chaining                     |
| Widely used on the Internet           | Common in block cipher-based systems  |

---

# Key Points to Remember

* **HMAC = Hash Function + Secret Key**
* Uses **two hash computations**.
* Uses **ipad (0x36)** and **opad (0x5C)**.
* Provides **Authentication** and **Integrity**.
* Does **not** provide **Confidentiality**.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define HMAC.
2. What are ipad and opad in HMAC?
3. What security services does HMAC provide?
4. Differentiate between HMAC and CBC-MAC.

### Long Questions (8–10 Marks)

1. **Explain the working of HMAC with a neat diagram.**
2. **Discuss the advantages and applications of HMAC.**
3. **Differentiate between HMAC and CBC-MAC.**

---

# Memory Trick

Remember the sequence:

```text id="q1w6m3"
Secret Key
     │
 ┌───┴───┐
 ▼       ▼
ipad    opad
 │        │
 ▼        │
Message   │
 │        │
 ▼        │
Hash      │
 │        │
 ▼────────┘
    Hash
      │
      ▼
    HMAC
```

The most important formula is:

$$
\boxed{\text{HMAC}(K,M)=H\left((K\oplus opad);||;H((K\oplus ipad);||;M)\right)}
$$

**Easy way to remember:**

1. XOR key with **ipad** → Hash with the **message**.
2. XOR key with **opad** → Hash with the **inner hash**.
3. The result is the **final HMAC**.
