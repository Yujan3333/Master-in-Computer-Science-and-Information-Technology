
## **Encryption**

**1. Purpose**

* Protects data in an **insecure environment**.
* Involves transforming **plaintext** into **ciphertext** using an **encryption algorithm** and **key**.
* Original data is recovered using a **decryption key**.

**2. Data Encryption Standard (DES)**

* Developed by the **U.S. government**, widely adopted internationally.
* Provides **end-to-end encryption** between sender and receiver.
* Combines **substitution** and **permutation (transposition)** repeatedly for **16 cycles**.
* Operates on **64-bit blocks of plaintext**.

**3. Advanced Encryption Standard (AES)**

* Introduced by **NIST** after concerns about DES.
* Uses **128-bit blocks**, stronger and harder to break.

---

## **Public Key Encryption (Asymmetric Encryption)**

**1. Concept (Diffie-Hellman, 1976)**

* Uses **two separate keys**:

  * **Public key**: available to everyone
  * **Private key**: kept secret by the owner
* Based on **mathematical functions**, not simple bit operations.
* Key advantages: **confidentiality, key distribution, and authentication**.

**2. Components of a Public Key System**

| Component                 | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| **Plaintext**             | Original readable data/message.                         |
| **Encryption Algorithm**  | Transforms plaintext using a key.                       |
| **Public & Private Keys** | Pair of related keys; one encrypts, the other decrypts. |
| **Ciphertext**            | Scrambled output depending on plaintext and key.        |
| **Decryption Algorithm**  | Reverses encryption using the correct key.              |
| **Key Distribution**      | Public key is shared; private key is secret.            |

**3. Working Steps**

1. Each user generates a **key pair**.
2. **Public key** is shared; **private key** is kept secret.
3. Sender encrypts a message using the **receiver’s public key**.
4. Receiver decrypts the message using their **private key**.
5. Only the intended receiver can read the message.

---

## **RSA Algorithm (1978)**

* Named after **Rivest, Shamir, and Adleman**.
* Based on **number theory** and the difficulty of factoring large primes.
* Uses **modular arithmetic (mod n)** for encryption and decryption.

---

## **Digital Signatures**

**1. Purpose**

* Provides **authentication** and integrity in e-commerce applications.
* Associates a **unique mark** (signature) with a message.
* Ensures that the signature is **verifiable and unique for each use**.

**2. Mechanism**

* Digital signature = function of **message + timestamp**.
* Created using **public key cryptography**.
* Others can **verify the signature** using the sender’s public key.

---

### **Key Takeaways**

* **DES & AES**: Symmetric encryption (same key for encryption/decryption).
* **Public key cryptography**: Uses **key pairs**, enables secure communication without sharing private keys.
* **RSA**: Classic example of public key cryptography, relies on prime factorization.
* **Digital signatures**: Enable **authentication, non-repudiation, and integrity**.

---