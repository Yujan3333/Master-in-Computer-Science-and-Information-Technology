
#advanced-cryptography #third-semester 
# 1. Cryptographic Key Infrastructure (PKI)

## Definition

**Public Key Infrastructure (PKI)** is a framework that manages **public keys**, **digital certificates**, and **Certificate Authorities (CA)** to enable secure communication and authentication.

PKI solves the problem:

> "How do I know that this public key really belongs to the claimed person?"

---

## Main Components

### 1. Certificate Authority (CA)

Trusted organization that issues digital certificates.

Example:

* Verifies Alice's identity.
* Signs Alice's public key.

---

### 2. Registration Authority (RA)

Verifies users before the CA issues a certificate.

Think of the RA as the identity checker.

---

### 3. Digital Certificate

Contains:

* User identity
* Public key
* Certificate validity
* CA's digital signature

---

### 4. Certificate Repository

Stores certificates for public access.

---

### 5. Certificate Revocation List (CRL)

Contains certificates that are no longer valid.

---

## Working of PKI

```text id="v1trcx"
User
 │
 │ Requests Certificate
 ▼
Registration Authority (RA)
 │
 │ Verifies Identity
 ▼
Certificate Authority (CA)
 │
 │ Issues Certificate
 ▼
Digital Certificate
 │
 ▼
Repository
```

---

## Advantages

* Authentication
* Confidentiality
* Integrity
* Non-repudiation
* Secure public key distribution

---

