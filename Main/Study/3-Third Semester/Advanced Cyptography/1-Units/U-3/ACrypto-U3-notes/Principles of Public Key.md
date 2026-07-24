#advanced-cryptography #third-semester 

# 1. Principles of Public-Key Cryptosystems

## Concept of Public-Key Cryptography

Public-key cryptography (also called **asymmetric cryptography**) is a cryptographic system that uses **two different but mathematically related keys**:

* **Public Key** → Shared openly with everyone.
* **Private Key** → Kept secret by the owner.

One key is used for encryption, while the other is used for decryption.

Unlike symmetric cryptography, both communicating parties **do not need to share a secret key beforehand**.

---

## Public Key and Private Key

### Public Key

* Can be shared publicly.
* Used to encrypt messages.
* Used to verify digital signatures.
* Cannot practically be used to derive the private key.

### Private Key

* Kept secret by the owner.
* Used to decrypt encrypted messages.
* Used to create digital signatures.
* If compromised, system security is lost.

---

## Encryption and Decryption

### Encryption

Encryption converts plaintext into ciphertext using the recipient's **public key**.

**Process**

```
Plaintext
    │
Encrypt using Receiver's Public Key
    │
Ciphertext
```

### Decryption

Only the receiver can decrypt the ciphertext using their **private key**.

```
Ciphertext
    │
Decrypt using Receiver's Private Key
    │
Plaintext
```

### Example

Suppose Bob wants to receive secure messages.

* Bob publishes his public key.
* Alice encrypts the message using Bob's public key.
* Bob decrypts it using his private key.

```
Alice
   │
Encrypt with Bob's Public Key
   │
Ciphertext
   │
Bob
Decrypt with Bob's Private Key
   │
Original Message
```

---

# Digital Signature

A digital signature provides:

* Authentication
* Integrity
* Non-repudiation

### Working

Instead of encrypting with the public key:

1. Sender computes a hash of the message.
2. Sender encrypts the hash using **their private key**.
3. This encrypted hash becomes the digital signature.
4. Receiver decrypts the signature using the sender's public key.
5. Receiver computes the message hash.
6. If both hashes match, the signature is valid.

```
Message
   │
Hash Function
   │
Message Digest
   │
Encrypt with Sender's Private Key
   │
Digital Signature
```

Receiver:

```
Digital Signature
      │
Decrypt using Sender's Public Key
      │
Original Hash

Message
      │
Hash Function
      │
Computed Hash

Compare

If Equal → Valid Signature
Else → Invalid
```

---

# Advantages of Public-Key Cryptography

1. No need to share a secret key before communication.
2. Supports digital signatures.
3. Provides authentication.
4. Ensures non-repudiation.
5. Easier key distribution.
6. Suitable for secure communication over the Internet.

---

# Disadvantages

1. Slower than symmetric encryption.
2. Requires more computational power.
3. Uses larger key sizes.
4. More complex algorithms.
5. Not suitable for encrypting large amounts of data directly.
6. Depends on certificate management (PKI).

---

# Difference Between Symmetric and Asymmetric Cryptography

| Feature            | Symmetric Cryptography        | Asymmetric Cryptography                          |
| ------------------ | ----------------------------- | ------------------------------------------------ |
| Number of keys     | One shared key                | Two keys (public and private)                    |
| Encryption key     | Same as decryption key        | Different keys                                   |
| Speed              | Fast                          | Slow                                             |
| Key distribution   | Difficult                     | Easy                                             |
| Security           | Depends on secret key sharing | Public key can be shared safely                  |
| Digital signature  | Not supported                 | Supported                                        |
| Computational cost | Low                           | High                                             |
| Used for           | Bulk data encryption          | Key exchange, authentication, digital signatures |
| Examples           | AES, DES, Blowfish            | RSA, ElGamal, ECC                                |

---

# Exam Questions

## Q1. What is a Public-Key Cryptosystem? **(5 Marks)**

**Answer:**

A **public-key cryptosystem** is an asymmetric encryption system that uses two mathematically related keys:

* A **public key** for encryption or signature verification.
* A **private key** for decryption or signature generation.

The public key is openly distributed, while the private key remains secret. It provides confidentiality, authentication, integrity, and non-repudiation.

---

## Q2. Explain the Working Principle of Public-Key Cryptography. **(5 Marks)**

**Answer:**

The working principle is:

1. The receiver generates a public key and a private key.
2. The receiver publishes the public key.
3. The sender encrypts the plaintext using the receiver's public key.
4. The ciphertext is sent to the receiver.
5. The receiver decrypts the ciphertext using the private key to obtain the original plaintext.

For digital signatures:

1. The sender hashes the message.
2. The sender encrypts the hash using their private key to create a digital signature.
3. The receiver decrypts the signature using the sender's public key and compares the hash values.
4. If the hashes match, the signature is verified.

---

## Q3. Compare Symmetric and Asymmetric Cryptography. **(8 Marks)**

| Symmetric Cryptography              | Asymmetric Cryptography                          |
| ----------------------------------- | ------------------------------------------------ |
| Uses one shared secret key          | Uses public and private keys                     |
| Fast encryption/decryption          | Slower encryption/decryption                     |
| Difficult key distribution          | Easy key distribution                            |
| Suitable for large data encryption  | Suitable for key exchange and digital signatures |
| Does not provide digital signatures | Supports digital signatures                      |
| Lower computational cost            | Higher computational cost                        |
| Examples: AES, DES                  | Examples: RSA, ElGamal, ECC                      |

**Conclusion:**
In practice, **hybrid cryptography** is commonly used: asymmetric cryptography securely exchanges a symmetric session key, and symmetric cryptography encrypts the actual data because it is much faster.
