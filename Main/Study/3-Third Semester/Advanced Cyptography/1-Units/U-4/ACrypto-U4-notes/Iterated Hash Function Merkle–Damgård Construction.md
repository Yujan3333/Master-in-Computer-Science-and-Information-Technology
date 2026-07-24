#advanced-cryptography #third-semester 

# Iterated Hash Functions (Merkle–Damgård Construction)

> **Exam Importance:** ⭐⭐⭐⭐⭐ (Very Important)

---

# Q. What is an Iterated Hash Function? Explain the Merkle–Damgård Construction with a neat diagram.

---

# Answer

## Introduction

Most modern cryptographic hash functions must process messages of **any length**. Since a compression function can only process **fixed-size inputs**, the message is divided into **fixed-size blocks** and processed one block at a time.

This repeated processing of message blocks is called an **Iterated Hash Function**.

The **Merkle–Damgård Construction** is the most widely used method for building iterated hash functions. It is used in **MD5**, **SHA-1**, and the **SHA-2 family**.

---

# What is an Iterated Hash Function?

An **Iterated Hash Function** is a hash function that computes the hash of a long message by dividing it into fixed-size blocks and repeatedly applying a **compression function** to each block until a final hash value is obtained.

Instead of hashing the entire message at once, the message is hashed **block by block**.

---

# Definition

> **An Iterated Hash Function is a cryptographic hash function that repeatedly applies a compression function to fixed-size message blocks, using the output of the previous computation (chaining value) as input to the next computation, until a final hash value is produced.**

---

# Why is an Iterated Hash Function Needed?

Suppose you want to hash a **5 GB** file.

A compression function cannot process the whole file at once.

Instead,

```text
5 GB File

↓

Divide into Blocks

↓

Block 1
Block 2
Block 3
...
Block n

↓

Process One by One

↓

Final Hash
```

Thus, an iterated hash function can efficiently process messages of **any length**.

---

# Merkle–Damgård Construction

The **Merkle–Damgård Construction** is a technique for building a secure hash function using a **compression function**.

It processes the message **iteratively**, where each round depends on the result of the previous round.

---

# Components of Merkle–Damgård Construction

## 1. Padding

The message is padded so that its length becomes an exact multiple of the block size.

### Why is padding needed?

* Ensures equal-sized blocks.
* Allows processing of the last incomplete block.
* Appends the message length to improve security.

---

## 2. Message Blocks

The padded message is divided into equal-sized blocks.

Example

```text
Original Message

↓

Padding

↓

M1 | M2 | M3 | M4
```

---

## 3. Initialization Vector (IV)

Before hashing begins, a predefined fixed value called the **Initialization Vector (IV)** is used.

It is denoted as

$$
H_0
$$

The IV acts as the starting point for hashing.

---

## 4. Compression Function

A **compression function** combines:

* Previous chaining value
* Current message block

to generate a new chaining value.

Mathematically,

$$
H_i = f(H_{i-1}, M_i)
$$

where

* $H_{i-1}$ = Previous chaining value
* $M_i$ = Current message block
* $H_i$ = New chaining value
* $f$ = Compression function

---

## 5. Chaining Value

The output of one compression function becomes the input to the next compression function.

Example

```text
H0

↓

Compression

↓

H1

↓

Compression

↓

H2

↓

Compression

↓

H3
```

This creates a **chain**, so every block influences the final hash.

---

## 6. Final Hash Value

After the last message block is processed,

the last chaining value becomes the **final hash**.

$$
\text{Final Hash} = H_n
$$

---

# Working of Merkle–Damgård Construction

### Step 1

Pad the message.

---

### Step 2

Divide the message into fixed-size blocks.

```text
M1 | M2 | M3 | ... | Mn
```

---

### Step 3

Initialize

$$
H_0 = IV
$$

---

### Step 4

Apply the compression function repeatedly.

First block

$$
H_1 = f(H_0, M_1)
$$

Second block

$$
H_2 = f(H_1, M_2)
$$

Third block

$$
H_3 = f(H_2, M_3)
$$

Continue until the last block

$$
H_n = f(H_{n-1}, M_n)
$$

---

### Step 5

The last chaining value becomes the final hash.

$$
\boxed{\text{Hash} = H_n}
$$

---

# Diagram

```text
                  Original Message
                         │
                         ▼
                     Padding
                         │
                         ▼
        +--------------------------------+
        |  M1 | M2 | M3 | ... | Mn       |
        +--------------------------------+
                         │

                   Initial Value
                     H0 = IV
                         │
                         ▼
               +----------------+
               | Compression f  |
               | (H0, M1)        |
               +----------------+
                         │
                        H1
                         │
                         ▼
               +----------------+
               | Compression f  |
               | (H1, M2)        |
               +----------------+
                         │
                        H2
                         │
                         ▼
                      ......
                         │
                         ▼
               +----------------+
               | Compression f  |
               | (Hn-1, Mn)      |
               +----------------+
                         │
                         ▼
                    Final Hash
```

---

# Why is Chaining Important?

Suppose each block were hashed independently.

```text
Hash(M1)

Hash(M2)

Hash(M3)
```

Changing **M1** would only change **Hash(M1)**.

The remaining hashes would remain unchanged.

In Merkle–Damgård,

```text
H0 → H1 → H2 → H3 → H4
```

Every hash depends on the previous one.

Therefore,

changing even **one bit** in **M1** changes **every subsequent chaining value**, resulting in a completely different final hash.

---

# Advantages

* Can hash messages of any length.
* Efficient for very large files.
* Simple and widely used.
* Forms the basis of SHA-1 and SHA-2.
* Provides strong data integrity.

---

# Limitations

* Vulnerable to **Length Extension Attacks** if used directly.
* Security depends on the underlying compression function.
* Does not completely eliminate collision attacks.

---

# Applications

Merkle–Damgård Construction is used in:

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512

**Note:** SHA-3 **does not** use the Merkle–Damgård construction. It uses the **Sponge Construction**.

---

# Merkle–Damgård vs Sponge Construction

| Merkle–Damgård                         | Sponge Construction                   |
| -------------------------------------- | ------------------------------------- |
| Used in SHA-1 and SHA-2                | Used in SHA-3                         |
| Uses a compression function            | Uses a sponge function                |
| Processes one block at a time          | Absorbs and squeezes data             |
| Vulnerable to length extension attacks | Resistant to length extension attacks |

---

# Key Points to Remember

* **Iterated Hash Function** processes data **block by block**.
* **Merkle–Damgård Construction** is the most common iterated hash design.
* **IV (Initialization Vector)** is the starting value.
* **Padding** ensures the message length is a multiple of the block size.
* **Compression Function** combines the previous hash and the current block.
* **Chaining Value** is the output of one round and the input to the next.
* The **last chaining value** is the **final hash**.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define an iterated hash function.
2. What is the Merkle–Damgård construction?
3. What is the purpose of padding in Merkle–Damgård construction?
4. What is the role of the Initialization Vector (IV)?
5. Define a compression function.
6. What is a chaining value?

### Long Questions (8–10 Marks)

1. **Explain the Merkle–Damgård construction with a neat diagram.**
2. **Describe the working of an iterated hash function.**
3. **Explain the components of the Merkle–Damgård construction.**
4. **Differentiate between the Merkle–Damgård construction and the Sponge construction.**

---

# Memory Trick

Remember the flow:

```text
Message
   │
   ▼
Padding
   │
   ▼
Divide into Blocks
   │
   ▼
IV (H0)
   │
   ▼
Compression Function
   │
   ▼
Chaining Value
   │
   ▼
Compression Function
   │
   ▼
...
   │
   ▼
Final Hash
```

And remember the most important formula:

$$
H_i = f(H_{i-1}, M_i)
$$

This means:

* Previous hash ($H_{i-1}$)
* * Current message block ($M_i$)
* ↓ Compression function
* = New hash ($H_i$)

This single equation summarizes the entire Merkle–Damgård construction.
