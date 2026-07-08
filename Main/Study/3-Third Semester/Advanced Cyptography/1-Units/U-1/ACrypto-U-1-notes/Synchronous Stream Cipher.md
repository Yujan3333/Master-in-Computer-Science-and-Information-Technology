#third-semester #advanced-cryptography 

# Synchronous Stream Cipher

A **Synchronous Stream Cipher** is a type of **stream cipher** in which the **keystream is generated independently of the plaintext and ciphertext**.

Both the sender and receiver generate the **same keystream** using the **same secret key**, and encryption/decryption is done using the XOR operation.

![](../../../../../../../Images/Third_Sem_Images/Synchronous%20Stream%20Cipher.png)

---

# Simple Definition (Exam)

> **A Synchronous Stream Cipher is a stream cipher in which the keystream is generated independently of the plaintext and ciphertext. Both the sender and receiver must remain synchronized to generate the same keystream.**

---

# How It Works

1. Sender and receiver share the **same secret key**.
2. Both generate the **same keystream**.
3. Sender encrypts using XOR.
4. Receiver decrypts using the **same keystream**.

Encryption:

$$
C=P\oplus K
$$

Decryption:

$$
P=C\oplus K
$$

---

# Simple Diagram

```text id="2q9x6d"
             Secret Key
                 │
        ┌────────┴────────┐
        ▼                 ▼
 Keystream Generator  Keystream Generator
        │                 │
        ▼                 ▼
 Plaintext ──XOR──► Ciphertext ──XOR──► Plaintext
```

Notice:

* The **same key** is used at both ends.
* Both sides generate the **same keystream** independently.

---

# Example

### Plaintext

```text id="5n3g6x"
10110010
```

### Keystream

```text id="4kz9pj"
11001010
```

### Encryption

```text id="r7x4cm"
Plaintext : 10110010
Keystream : 11001010
--------------------
Ciphertext: 01111000
```

---

### Decryption

```text id="x9l2fw"
Ciphertext: 01111000
Keystream : 11001010
--------------------
Plaintext : 10110010
```

Original plaintext is recovered.

---

# Why is it called "Synchronous"?

Because:

* The sender and receiver must **stay synchronized**.
* They must generate **exactly the same keystream at the same time**.

If one side loses synchronization (for example, a bit is lost during transmission), the remaining data cannot be decrypted correctly until synchronization is restored.

---

# Advantages

* Very fast encryption and decryption.
* Suitable for real-time communication.
* Errors in one ciphertext bit affect only the corresponding plaintext bit.

---

# Disadvantages

* Sender and receiver **must remain synchronized**.
* If synchronization is lost, decryption fails.
* Reusing the same keystream with the same key is insecure.

---

# Applications

* Secure voice communication
* Video streaming
* Wireless communication
* VPNs

---

# Difference from Self-Synchronizing Stream Cipher

| Synchronous Stream Cipher                                                        | Self-Synchronizing Stream Cipher                          |
| -------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Keystream depends only on the secret key (and possibly an initialization value). | Keystream depends on previous ciphertext bits.            |
| Sender and receiver must stay synchronized.                                      | Automatically resynchronizes after a few ciphertext bits. |
| Loss of synchronization causes decryption errors until resynchronized.           | Can recover synchronization automatically.                |

---

# Exam Definition (2 Marks)

> **A Synchronous Stream Cipher is a stream cipher in which the keystream is generated independently of the plaintext and ciphertext. Encryption and decryption are performed using the XOR operation, and both the sender and receiver must remain synchronized to generate the same keystream.**

---

# Easy Memory Trick ⭐

Think of two identical clocks:

```text id="c1p8yr"
Sender Clock   ⏰ → Generates Keystream
Receiver Clock ⏰ → Generates the SAME Keystream
```

If **both clocks stay in sync**, encryption and decryption work correctly.

If **one clock becomes out of sync**, the receiver generates a different keystream, and the decrypted message becomes incorrect.

### One-line Memory Trick

> **Synchronous = Same key + Same keystream + Stay in Sync.**
