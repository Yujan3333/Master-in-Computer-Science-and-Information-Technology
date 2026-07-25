#advanced-cryptography #third-semester 

# PKI Trust Model (Public Key Infrastructure Trust Model) **[5 Marks]**

## Definition

A **PKI Trust Model** is the framework that establishes **trust** among users by using **Certificate Authorities (CAs)** to issue, verify, and manage digital certificates. It ensures that a public key truly belongs to the claimed owner.

---

## Need for PKI Trust Model

Without a trust model, anyone could claim to own a public key. The PKI Trust Model prevents impersonation by having a trusted third party verify identities before issuing certificates.

---

## Components of PKI Trust Model

1. **Certificate Authority (CA):**

   * A trusted third party that issues and digitally signs certificates.
   * Verifies the identity of users before issuing certificates.

2. **Registration Authority (RA):**

   * Verifies the identity of users on behalf of the CA.
   * Sends verified requests to the CA.

3. **Digital Certificate:**

   * Contains the user's identity, public key, validity period, serial number, and the CA's digital signature.

4. **End User (Subscriber):**

   * The person or organization that owns the certificate and uses it for secure communication.

5. **Relying Party:**

   * The entity that verifies and trusts the certificate before communicating.

---

## Working of the PKI Trust Model

1. The user generates a public-private key pair.
2. The user requests a digital certificate from the RA/CA.
3. The RA verifies the user's identity.
4. The CA issues and digitally signs the certificate.
5. The certificate is sent to the user.
6. Others verify the CA's signature before trusting the user's public key.

---

## Diagram

```text
                Root CA
                   │
          Signs certificates
                   │
          Intermediate CA
                   │
          Issues certificates
                   │
        ┌──────────┴──────────┐
        │                     │
     User A                User B
        │                     │
        └──── Secure Communication ────┘
```

---

## Advantages

* Establishes trust between communicating parties.
* Prevents impersonation and man-in-the-middle attacks.
* Supports authentication, confidentiality, integrity, and non-repudiation.
* Enables secure communication over the Internet.

---

## Disadvantages

* Costly to deploy and maintain.
* Certificate management can be complex.
* If a CA is compromised, trust in issued certificates is affected.

---

## Applications

* HTTPS/SSL/TLS
* Secure Email (S/MIME)
* VPNs
* Digital Signatures
* Online Banking
* E-commerce

---

## Exam Conclusion

The **PKI Trust Model** is a trust framework in which **Certificate Authorities (CAs)** issue and verify digital certificates, allowing users to trust public keys and communicate securely over insecure networks. It forms the foundation of secure Internet communication.
