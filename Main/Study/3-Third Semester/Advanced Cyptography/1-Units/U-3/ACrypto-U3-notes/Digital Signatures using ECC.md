#advanced-cryptography #third-semester #elliptic-curve 


- [Digital Signatures using ECC- shorter](Digital%20Signatures%20using%20ECC-%20shorter.md)
# Digital Signatures using ECC (ECDSA)

**ECDSA (Elliptic Curve Digital Signature Algorithm)** is the most widely used digital signature algorithm based on **Elliptic Curve Cryptography (ECC)**.

It is used to **verify the authenticity, integrity, and non-repudiation** of a message.

---

# Purpose

Digital signatures provide:

* **Authentication** – Confirms the sender's identity.
* **Integrity** – Ensures the message has not been modified.
* **Non-repudiation** – The sender cannot deny sending the message.

---

# Key Generation

Choose:

* Elliptic curve $$E$$
* Base point $$G$$
* Private key $$d$$

Compute the public key:

$$
Q = dG
$$

* **Private Key:** $$d$$
* **Public Key:** $$Q$$

---

# Signature Generation

Suppose Alice wants to sign a message $$M$$.

### Step 1: Compute Message Hash

Calculate the hash of the message.

$$
e = H(M)
$$

where $$H$$ is a hash function (e.g., SHA-256).

---

### Step 2: Choose a Random Number

Select a random integer

$$
k
$$

where

$$
1 \le k \le n-1
$$

---

### Step 3: Compute Point

Calculate

$$
P = kG = (x_1, y_1)
$$

---

### Step 4: Compute

$$
r = x_1 \bmod n
$$

If

$$
r = 0
$$

choose another value of $$k$$.

---

### Step 5: Compute

$$
s = k^{-1}(e + dr)\bmod n
$$

If

$$
s = 0
$$

choose another value of $$k$$.

---

### Step 6: Signature

The digital signature is

$$
(r,s)
$$

---

# Signature Verification

The receiver receives

* Message $$M$$
* Signature $$ (r,s) $$

and knows the sender's public key $$Q$$.

---

### Step 1

Compute the message hash

$$
e = H(M)
$$

---

### Step 2

Compute

$$
w = s^{-1}\bmod n
$$

---

### Step 3

Compute

$$
u_1 = ew\bmod n
$$

$$
u_2 = rw\bmod n
$$

---

### Step 4

Compute

$$
X = u_1G + u_2Q
$$

Let

$$
X=(x_1,y_1)
$$

---

### Step 5

Accept the signature if

$$
r \equiv x_1 \pmod n
$$

Otherwise,

the signature is **invalid**.

---

# Block Diagram

```
Sender

Message
   │
Hash Function
   │
Message Digest
   │
Random Number k
   │
Private Key d
   │
ECDSA Signing
   │
Signature (r,s)
   │
---------------------> Receiver

Message + Signature
        │
Hash Function
        │
Public Key Q
        │
ECDSA Verification
        │
Valid / Invalid
```

---

# Advantages of ECC Digital Signature

* Smaller key size than RSA.
* Faster computation.
* Less memory required.
* Lower power consumption.
* High level of security.
* Suitable for mobile devices and IoT.

---

# Applications

* SSL/TLS certificates
* Bitcoin and other cryptocurrencies
* Secure email
* Digital certificates
* Smart cards
* Mobile banking
* Electronic documents

---

# Advantages over RSA Signatures

| ECC               | RSA              |
| ----------------- | ---------------- |
| Smaller key size  | Larger key size  |
| Faster            | Slower           |
| Less storage      | More storage     |
| Less bandwidth    | More bandwidth   |
| Higher efficiency | Lower efficiency |

---

# Exam-Oriented Summary

**ECDSA (Elliptic Curve Digital Signature Algorithm)** is a digital signature scheme based on elliptic curve cryptography. It uses a **private key** to generate a signature and a **public key** to verify it. The algorithm provides **authentication, integrity, and non-repudiation** while offering the same level of security as RSA with much smaller key sizes.

---

# Frequently Asked Exam Questions

### 2 Marks

* What is ECDSA?
* What are the objectives of digital signatures?
* What are the advantages of ECC over RSA?

### 5 Marks

* Explain the key generation process in ECDSA.
* Explain the signature generation steps.
* Explain the signature verification steps.

### 10 Marks

* Explain the Digital Signature Scheme using ECC with a neat block diagram.
* Compare ECC digital signatures with RSA digital signatures.

> **Exam Tip:** In most university cryptography courses, **Digital Signatures using ECC** is asked as a **theoretical algorithm**. You are usually expected to write the **key generation, signature generation, and verification steps**, rather than solve a full numerical example.
