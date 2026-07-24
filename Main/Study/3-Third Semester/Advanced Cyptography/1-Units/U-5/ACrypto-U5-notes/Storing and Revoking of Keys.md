#advanced-cryptography #third-semester 

# 1. Storing Keys

## Definition

**Key storage** is the secure preservation of cryptographic keys to prevent unauthorized access.

---

## Methods of Storing Keys

### 1. Hardware Security Module (HSM)

Dedicated hardware device.

Most secure.

---

### 2. Smart Cards

Stores private keys securely.

---

### 3. Trusted Platform Module (TPM)

Built into many computers.

Protects encryption keys.

---

### 4. Encrypted Key Files

Keys stored in encrypted files protected by a password.

---

### 5. Cloud Key Management Service

Examples:

* AWS KMS
* Azure Key Vault
* Google Cloud KMS

---

## Good Practices

* Encrypt stored keys.
* Restrict access.
* Back up keys securely.
* Rotate keys periodically.

---

# 2. Revoking Keys

## Definition

**Key revocation** is the process of invalidating a cryptographic key or certificate before its normal expiration because it is no longer trusted.

---

## Reasons for Revocation

* Private key compromised.
* Device stolen.
* Employee leaves the organization.
* Certificate issued incorrectly.
* Key expiration.

---

## Revocation Methods

### Certificate Revocation List (CRL)

A list published by the CA containing revoked certificates.

---

### Online Certificate Status Protocol (OCSP)

Allows users to check the current status of a certificate online.

---

## Advantages

* Prevents misuse of compromised keys.
* Improves security.
* Maintains trust in PKI.

---

# Complete Relationship

```text id="9fbmvh"
Generate Key
      │
      ▼
Store Key Securely
      │
      ▼
Use Key
      │
      ▼
Rotate / Renew Key
      │
      ▼
Revoke Key (if compromised)
      │
      ▼
Destroy Key
```

---
