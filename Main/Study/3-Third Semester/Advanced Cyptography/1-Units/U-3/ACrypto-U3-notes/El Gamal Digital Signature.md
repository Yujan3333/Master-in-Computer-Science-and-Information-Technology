#advanced-cryptography #third-semester #el-gamal

- [El Gamal DS - Shorter](El%20Gamal%20DS%20-%20Shorter.md)
# ElGamal Digital Signature Scheme

The **ElGamal Digital Signature Scheme** is a public-key digital signature algorithm based on the **Discrete Logarithm Problem (DLP)**.

It is used to provide:

* **Authentication** – Verifies the sender's identity.
* **Integrity** – Ensures the message has not been modified.
* **Non-repudiation** – Prevents the sender from denying the signature.

---

# Algorithm

The ElGamal Digital Signature Scheme consists of three phases:

1. Key Generation
2. Signature Generation
3. Signature Verification

---

# 1. Key Generation

Choose:

* A large prime number

$$
p
$$

* A primitive root (generator)

$$
g
$$

* A private key

$$
x,\quad 1\le x\le p-2
$$

Compute the public key

$$
y=g^x \bmod p
$$

**Public Key**

$$
(p,;g,;y)
$$

**Private Key**

$$
x
$$

---

# 2. Signature Generation

Suppose Alice wants to sign message

$$
M
$$

### Step 1

Compute the message hash

$$
m=H(M)
$$

---

### Step 2

Choose a random integer

$$
k
$$

such that

$$
1<k<p-1
$$

and

$$
\gcd(k,p-1)=1
$$

This ensures that

$$
k^{-1}\pmod{p-1}
$$

exists.

---

### Step 3

Compute

$$
r=g^k \bmod p
$$

---

### Step 4

Compute

$$
s=k^{-1}(m-xr)\bmod (p-1)
$$

---

### Step 5

The digital signature is

$$
(r,s)
$$

---

# 3. Signature Verification

The receiver receives

* Message $$M$$
* Signature $$ (r,s) $$

and knows the sender's public key.

---

### Step 1

Compute the message hash

$$
m=H(M)
$$

---

### Step 2

Compute

$$
v_1=g^m \bmod p
$$

---

### Step 3

Compute

$$
v_2=y^r r^s \bmod p
$$

---

### Step 4

If

$$
v_1=v_2
$$

the signature is **valid**.

Otherwise,

the signature is **invalid**.

---

# Block Diagram

```text
             Sender

           Message M
               │
        Hash Function
               │
         Message Digest
               │
      Random Number k
               │
        Private Key x
               │
     ElGamal Signature
               │
        Signature (r,s)
               │
──────────────────────────────────► Receiver

      Message + Signature
               │
        Hash Function
               │
         Public Key y
               │
    ElGamal Verification
               │
       Valid / Invalid
```

---

# Advantages

* Based on the difficult Discrete Logarithm Problem.
* Provides authentication and integrity.
* Supports non-repudiation.
* Widely studied and secure when implemented correctly.

---

# Disadvantages

* Signature size is relatively large.
* Slower than some modern signature schemes.
* Requires a new random value $$k$$ for every signature.
* Reusing the same $$k$$ can reveal the private key.

---

# Applications

* Secure communications
* Digital certificates
* Electronic document signing
* Authentication systems

---

# Exam-Oriented Summary

The **ElGamal Digital Signature Scheme** is a public-key signature algorithm based on the **Discrete Logarithm Problem**. The signer uses a **private key** to generate a signature, while the receiver uses the **public key** to verify it. The scheme ensures **authentication, integrity, and non-repudiation**.

---

# Frequently Asked Exam Questions

### 2 Marks

* What is the ElGamal Digital Signature Scheme?
* What is the role of the random number $$k$$?
* Why must $$\gcd(k,p-1)=1$$?

### 5 Marks

* Explain the key generation process.
* Explain the signature generation process.
* Explain the signature verification process.

### 10 Marks

* Explain the ElGamal Digital Signature Scheme with a neat diagram.
* Explain the algorithm with the equations used in key generation, signing, and verification.

---

## Easy Memory Trick

### Key Generation

$$
y=g^x
$$

(Generate the public key.)

### Signature Generation

$$
r=g^k
$$

$$
s=k^{-1}(m-xr)
$$

(Sign using the private key.)

### Verification

$$
g^m=y^r r^s
$$

(Check if both sides are equal. If they are, the signature is valid.)
