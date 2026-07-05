#advanced-cryptography #cryptanalysis 

# Cryptanalysis of Shift Cipher (Caesar Cipher) ⭐⭐⭐⭐⭐

---

# What is a Shift Cipher?

A **Shift Cipher (Caesar Cipher)** encrypts a message by shifting each letter by a fixed number of positions.

Example (Key = 3)

```text
Plaintext : HELLO
```

Shift every letter by **3**

```text
H → K
E → H
L → O
L → O
O → R
```

Ciphertext

```text
KHOOR
```

---

# What is Cryptanalysis of Shift Cipher?

**Cryptanalysis of a Shift Cipher** means **finding the original plaintext or the key without knowing the secret key**.

Since there are only **26 possible keys (0–25)** in the English alphabet, an attacker can try every key until the correct message appears.

> **Definition:** Cryptanalysis of a shift cipher is the process of breaking the cipher by trying all possible shifts or by using letter frequency analysis to recover the plaintext.

---

# Method 1: Brute Force Attack ⭐⭐⭐⭐⭐ (Most Important)

Because there are only **26 possible shifts**, the attacker tries every key.

### Example

Ciphertext

```text
KHOOR
```

Try every key:

| Key   | Decrypted Text |
| ----- | -------------- |
| 0     | KHOOR          |
| 1     | JGNNQ          |
| 2     | IFMMP          |
| **3** | **HELLO ✅**    |
| 4     | GDKKN          |
| ...   | ...            |

At **Key = 3**, the attacker gets a meaningful word:

```text
HELLO
```

Therefore,

```text
Secret Key = 3
```

---

# Method 2: Frequency Analysis ⭐⭐⭐⭐

English letters have different frequencies.

Most common letters are:

```text
E > T > A > O > I > N
```

Suppose ciphertext is

```text
WKLV LV D WHVW
```

The attacker notices that one letter appears most often.

If that letter probably represents **E**, the attacker estimates the shift and decrypts the message.

This technique is called **frequency analysis**.

---

# Why Shift Cipher is Easy to Break

* Only **26 keys** exist.
* The key space is very small.
* Brute-force search is fast.
* Frequency analysis also works well.

Therefore, the shift cipher is **not secure**.

---

# Steps in Cryptanalysis of Shift Cipher ⭐⭐⭐⭐

1. Obtain the ciphertext.
2. Try all possible keys (0–25), **or** use frequency analysis.
3. Decrypt the ciphertext for each key.
4. Choose the result that forms a meaningful message.
5. The corresponding key is the secret key.

---

# Diagram

```text
Ciphertext
     │
     ▼
Try Keys 0–25
     │
     ▼
Meaningful Plaintext Found
     │
     ▼
Secret Key Recovered
```

---

# Example (Exam Style)

**Ciphertext:** `KHOOR`

Try different keys:

```text
Key = 1 → JGNNQ
Key = 2 → IFMMP
Key = 3 → HELLO ✅
```

**Answer:**

* Plaintext = **HELLO**
* Key = **3**

---

# Advantages (for the Attacker)

* Easy to break
* Small key space
* Requires very little computation

---

# Disadvantages (of the Shift Cipher)

* Very weak encryption
* Easily broken using brute force
* Vulnerable to frequency analysis

---

# Exam Definition (2 Marks)

> **Cryptanalysis of a shift cipher is the process of recovering the plaintext or secret key by trying all possible shifts (brute force) or by using frequency analysis.**

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

* Define cryptanalysis of a shift cipher.
* Why is the shift cipher easy to break?

### 5 Marks

* Explain the cryptanalysis of the shift cipher with a suitable example.
* Explain how brute force and frequency analysis are used to break a shift cipher.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
Shift Cipher
↓
Only 26 possible keys

Cryptanalysis Methods:
1. Brute Force → Try keys 0–25
2. Frequency Analysis → Use common letter frequencies

Example:
Ciphertext = KHOOR
Key = 3
Plaintext = HELLO

Reason it is weak:
• Small key space
• Easy to brute-force
• Vulnerable to frequency analysis
```

## Memory Trick

* **Shift Cipher = Lock with only 26 keys.**
* **Cryptanalysis = Try every key until the lock opens.** 🔑
