#advanced-cryptography #third-semester 

# RC5 Cipher

**RC5** is a **symmetric-key block cipher** designed by Ron Rivest in **1994**. It is known for its **simplicity, speed, and flexibility** because users can choose different block sizes, key sizes, and the number of encryption rounds.

Unlike **RC4** (which is a **stream cipher**), **RC5 is a block cipher**.

---

# Key Features

* **Type:** Symmetric-key block cipher
* **Designer:** Ron Rivest
* **Year:** 1994
* **Cipher Type:** Block Cipher
* **Variable Block Size:** 32, 64, or 128 bits
* **Variable Key Size:** 0–2040 bits
* **Variable Number of Rounds:** 0–255 (typically **12 or 20 rounds**)

---

# Why is RC5 Flexible?

Most encryption algorithms have fixed parameters.

RC5 lets you choose:

* **Block size**
* **Key size**
* **Number of rounds**

For example:

```text
RC5-32/12/16
```

means:

* **32-bit block size**
* **12 rounds**
* **16-byte (128-bit) key**

---

# How RC5 Works

RC5 encrypts data in blocks.

For a **64-bit block**, the plaintext is divided into two equal halves:

```text
64-bit Plaintext

+---------+---------+
|    A    |    B    |
| 32 bits | 32 bits |
+---------+---------+
```

Each encryption round performs operations on these two halves.

---

# Operations Used in RC5

RC5 uses only **three simple operations**:

### 1. XOR (⊕)

Compares two bits.

Example:

```text
0 ⊕ 0 = 0
0 ⊕ 1 = 1
1 ⊕ 0 = 1
1 ⊕ 1 = 0
```

---

### 2. Addition Modulo 2ⁿ

For 8-bit numbers:

```text
250 + 10 = 260
```

Since 8 bits can store values only from 0 to 255:

```text
260 mod 256 = 4
```

Result:

```text
250 + 10 = 4
```

---

### 3. Circular Left Rotation

Bits rotate to the left.

Example:

```text
10110001
```

Rotate left by one bit:

```text
01100011
```

The leftmost bit wraps around to the end.

---

# RC5 Encryption Process

Suppose the plaintext is divided into:

```text
A

B
```

Each round performs approximately:

```text
A = ((A ⊕ B) <<< B) + RoundKey

B = ((B ⊕ A) <<< A) + RoundKey
```

where:

* `⊕` = XOR
* `<<<` = Circular left rotation
* `+` = Modular addition

These steps repeat for the chosen number of rounds (for example, **12 rounds**).

---

# RC5 Structure

```text
Plaintext
     |
Split into A and B
     |
Add Initial Round Keys
     |
Round 1
     |
Round 2
     |
...
     |
Round 12
     |
Ciphertext
```

---

# Example (Conceptual)

Suppose:

```text
Plaintext

HELLO123
```

The plaintext is converted into binary and split into two halves:

```text
A

B
```

Encryption rounds then repeatedly perform:

* XOR
* Rotation
* Modular addition

Finally:

```text
Ciphertext

9F72A1C8...
```

*(The actual ciphertext depends on the key and chosen parameters.)*

---

# RC5 vs RC4

| RC4                                      | RC5                                           |
| ---------------------------------------- | --------------------------------------------- |
| Stream cipher                            | Block cipher                                  |
| Encrypts one byte/bit at a time          | Encrypts fixed-size blocks                    |
| Uses a generated keystream               | Uses multiple encryption rounds               |
| Simple but has known security weaknesses | More secure than RC4 when properly configured |
| Very fast                                | Fast and flexible                             |

---

# Advantages

* Simple design.
* Fast encryption and decryption.
* Flexible block size, key size, and rounds.
* Easy to implement.
* Suitable for both hardware and software.

---

# Disadvantages

* Slower than RC4 because it encrypts blocks over multiple rounds.
* Older algorithm and less commonly used today.
* Modern algorithms like Advanced Encryption Standard are generally preferred.

---

# RC5 vs AES

| RC5                              | AES                                            |
| -------------------------------- | ---------------------------------------------- |
| Variable block size              | Fixed 128-bit block size                       |
| Variable key size                | 128, 192, or 256-bit keys                      |
| Uses XOR, addition, and rotation | Uses substitution, permutation, and key mixing |
| Flexible                         | Standardized worldwide                         |
| Less commonly used today         | Most widely used modern block cipher           |

---

# Exam Answer (5 Marks)

**RC5** is a **symmetric-key block cipher** designed by **Ron Rivest** in **1994**. It encrypts data in fixed-size blocks and is known for its **flexibility**, allowing users to choose the **block size**, **key size**, and **number of encryption rounds**. RC5 uses three simple operations: **XOR**, **modular addition**, and **circular left rotation**.

**Features:**

* Symmetric-key block cipher
* Variable block size (32, 64, or 128 bits)
* Variable key size (0–2040 bits)
* Variable number of rounds (typically 12 or 20)
* Fast and simple implementation

RC5 is used for secure data encryption, although modern applications generally prefer **AES** due to its stronger standardization and broader adoption.

---

## Easy Memory Trick ⭐

Think of these ciphers like this:

* **RC4** → **R**unning stream of bytes → **Stream Cipher**
* **RC5** → **5 rounds?** (Actually variable rounds) → **Block Cipher**
* **AES** → Modern standard **Block Cipher**

**Remember:**

```text
RC4 → Stream Cipher → Keystream

RC5 → Block Cipher → XOR + Rotation + Modular Addition

AES → Modern Block Cipher → Today's standard
```

This one-line comparison is often enough to answer multiple exam questions.
