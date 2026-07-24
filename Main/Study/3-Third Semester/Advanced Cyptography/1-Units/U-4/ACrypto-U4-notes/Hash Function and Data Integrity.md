#advanced-cryptography #third-semester 

# Unit 4: Hash Functions and Data Integrity

# Introduction

A **cryptographic hash function** is a mathematical algorithm that converts an input message of **any length** into a **fixed-length output**, called a **hash value** or **message digest**. It is mainly used to ensure **data integrity**, i.e., to verify that data has not been altered during storage or transmission.

---

# 1. Hash Function

## Definition

A **hash function** is a one-way function that takes an input message of arbitrary length and produces a fixed-length hash value.

Mathematically,

$$
h = H(M)
$$

where:

* (M) = Original message
* (H) = Hash function
* (h) = Hash value (message digest)

---

## Characteristics (Properties)

A secure cryptographic hash function should have the following properties:

### 1. Deterministic

The same input always produces the same hash output.

### 2. Variable-Length Input

It accepts messages of any size.

### 3. Fixed-Length Output

The output size remains constant regardless of the input length.

### 4. Fast Computation

The hash value can be computed efficiently.

### 5. Preimage Resistance

Given a hash value, it should be computationally infeasible to determine the original message.

### 6. Second Preimage Resistance

Given one message, it should be infeasible to find another different message with the same hash.

### 7. Collision Resistance

It should be computationally infeasible to find any two different messages that produce the same hash value.

### 8. Avalanche Effect

A small change in the input causes a completely different hash output.

---

## Applications

* Password storage
* Digital signatures
* Message Authentication Codes (HMAC)
* File integrity verification
* Blockchain
* Software verification

---

# 2. Data Integrity

## Definition

**Data integrity** is the property that ensures data remains **accurate, complete, and unaltered** during storage or transmission.

Hash functions are commonly used to verify data integrity.

---

## How Hash Functions Ensure Data Integrity

### Step 1: Sender

The sender computes the hash of the original message.

```text
Message
   │
   ▼
Hash Function
   │
   ▼
Hash Value
```

The sender sends both the **message** and its **hash value**.

---

### Step 2: Receiver

The receiver computes the hash of the received message using the same hash algorithm.

```text
Received Message
        │
        ▼
 Hash Function
        │
        ▼
Computed Hash
```

---

### Step 3: Verification

The receiver compares the received hash with the computed hash.

* If both hashes are the same, the message has **not been modified**.
* If the hashes differ, the message has been **altered or corrupted**.

---

## Diagram

```text
              Sender

 Original Message
        │
        ▼
   Hash Function
        │
        ▼
     Hash Value
        │
        ├─────────────┐
        ▼             ▼
     Message       Hash Value
          (Sent Together)

==================================

             Receiver

Received Message
        │
        ▼
   Hash Function
        │
        ▼
 Computed Hash

Compare

Computed Hash = Received Hash

Yes → Integrity Verified

No → Message Altered
```

---

# Advantages

* Fast and efficient
* Detects data modification
* Fixed-size output
* One-way function
* Widely used in cryptography

---

# Limitations

* Does not provide confidentiality.
* Does not authenticate the sender by itself.
* Weak hash algorithms (e.g., SHA-1) are vulnerable to collision attacks.

---

# Difference: Hash Function vs Encryption

| Hash Function                        | Encryption                        |
| ------------------------------------ | --------------------------------- |
| One-way                              | Two-way                           |
| Used for integrity                   | Used for confidentiality          |
| No decryption                        | Can be decrypted using a key      |
| Original message cannot be recovered | Original message can be recovered |

---

# Key Points to Remember

* Accepts **variable-length input**.
* Produces **fixed-length output**.
* Used for **data integrity**, **not confidentiality**.
* A secure hash function should satisfy:

  * Deterministic
  * Fast computation
  * Fixed-length output
  * Preimage resistance
  * Second preimage resistance
  * Collision resistance
  * Avalanche effect

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define a cryptographic hash function.
2. What is a message digest?
3. Define data integrity.
4. What is the avalanche effect?
5. Define collision resistance.
6. What is preimage resistance?
7. What is second preimage resistance?
8. List any four properties of a secure hash function.
9. Give four applications of cryptographic hash functions.
10. Differentiate between hashing and encryption.

---

### Long Questions (8–10 Marks)

1. **Define a cryptographic hash function. Explain the properties of a secure hash function with suitable examples.**
2. **Explain how a cryptographic hash function ensures data integrity with a neat diagram.**
3. **What is data integrity? Describe the role of cryptographic hash functions in maintaining data integrity.**
4. **Differentiate between hashing and encryption. Discuss the applications of cryptographic hash functions.**
5. **Explain the working of a cryptographic hash function and discuss its advantages and limitations.**

> **Exam Tip:** This is one of the most important topics in Unit 4. In long-answer questions, always include the **definition, properties, data integrity process with a diagram, applications, and a comparison (e.g., hashing vs encryption)** to maximize your marks.
