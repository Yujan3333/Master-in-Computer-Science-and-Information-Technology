#advanced-cryptography 

# Cryptanalysis of Vigenère Cipher ⭐⭐⭐⭐⭐ 


# What is the Vigenère Cipher?

The **Vigenère Cipher** is a **polyalphabetic substitution cipher**.

It encrypts plaintext using a **keyword**.

Example

```text
Plaintext : ATTACKATDAWN
Key       : LEMONLEMONLE
```

↓

Ciphertext

```text
LXFOPVEFRNHR
```

---

# What is Cryptanalysis of Vigenère Cipher?

**Cryptanalysis of the Vigenère Cipher** is the process of finding the **secret keyword** or the **original plaintext** without knowing the key.

> **Definition:** Cryptanalysis of the Vigenère cipher is the process of breaking the cipher by determining the keyword length and then recovering the key using statistical techniques such as the Kasiski examination and frequency analysis.

---

# Why is Vigenère Cipher Harder to Break?

Unlike the Shift Cipher:

**Shift Cipher**

```text
HELLO
```

↓

Every letter shifts by **the same amount**.

---

**Vigenère Cipher**

```text
HELLO
```

↓

Each letter may shift by a **different amount**, depending on the keyword.

Example

```text
Key = KEY

H + K

E + E

L + Y

L + K

O + E
```

Each letter uses a different shift.

---

# Methods of Cryptanalysis ⭐⭐⭐⭐⭐

There are **two main methods**.

---

# Method 1: Kasiski Examination ⭐⭐⭐⭐⭐ (Most Important)

### Idea

Repeated groups of letters in the ciphertext often occur because the **keyword repeats**.

- [Example of Kasiski](Example%20of%20Kasiski.md) 
### Steps

**Step 1**

Find repeated groups.

Example

```text
ABCDxxxxxxxxABCDxxxxxxxxABCD
```

Repeated

```text
ABCD
```

---

**Step 2**

Measure the distance between repetitions.

Example

```text
ABCD appears every 12 letters.
```

---

**Step 3**

Find the factors (common divisors).

Example

```text
12

Factors

1, 2, 3, 4, 6, 12
```

One of these is likely the **keyword length**.

---

### Why it Works

Since the keyword repeats, repeated plaintext encrypted with the same keyword positions often produces repeated ciphertext.

This helps estimate the keyword length.

---

# Method 2: Frequency Analysis ⭐⭐⭐⭐⭐

Once the keyword length is known:

Suppose

Keyword Length = **5**

Split the ciphertext into **5 groups**.

[Example Frequency Analysis - Vigenere Cipher](Example%20Frequency%20Analysis%20-%20Vigenere%20Cipher.md)

Ciphertext

```text
L X F O P V E F R N H R
```

```text
Position:

0  1  2  3  4  5  6  7  8  9 10 11

L  X  F  O  P  V  E  F  R  N  H  R
```

Groups

```text
Group 1

L
V
H

Group 2

X
E
R

Group 3

F
F

Group 4

O
R

Group 5

P
N
```

Each group was encrypted using the **same Caesar shift**.

Now perform **frequency analysis** on each group separately.

Find the shift for each group.

```
Combine all shifts.

↓

Recover the keyword.

↓

Decrypt the message.
```

---

# Diagram ⭐⭐⭐⭐

```text
Ciphertext
      │
      ▼
Find Repeated Patterns
      │
      ▼
Estimate Keyword Length
      │
      ▼
Split into Groups
      │
      ▼
Frequency Analysis
      │
      ▼
Recover Keyword
      │
      ▼
Decrypt Plaintext
```

---

# Example (Conceptual)

Ciphertext

```text
LXFOPVEFRNHR
```

Suppose

Kasiski Examination gives

```text
Keyword Length = 5
```

Split into 5 groups.

Analyze each group.

Determine shifts.

**Recovered key**

```text
LEMON
```

**Decrypt**

↓

```text
ATTACKATDAWN
```

---

# Why Frequency Analysis Works

Each column is encrypted with **one fixed Caesar shift**.

A Caesar cipher is vulnerable to frequency analysis.

So breaking each column individually reveals the keyword.

---

# Why Vigenère is Stronger than Shift Cipher

| Shift Cipher                | Vigenère Cipher                       |
| --------------------------- | ------------------------------------- |
| One key                     | Keyword                               |
| Same shift for every letter | Different shifts                      |
| Easy brute force            | Harder to brute force                 |
| Easy frequency analysis     | Requires Kasiski + frequency analysis |

---

# Advantages (of Vigenère Cipher)

* More secure than Caesar cipher.
* Uses multiple alphabets.
* Hides simple letter frequencies better.

---

# Weaknesses

* Keyword repeats.
* Kasiski examination can estimate keyword length.
* Frequency analysis can recover the keyword after its length is known.

---

# Exam Definition (2 Marks)

> **Cryptanalysis of the Vigenère cipher is the process of recovering the keyword or plaintext by first determining the keyword length (using Kasiski examination) and then applying frequency analysis to each group of ciphertext.**

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define cryptanalysis of the Vigenère cipher.
2. What is the Kasiski examination?
3. Why is the Vigenère cipher stronger than the Caesar cipher?

---

### 5 Marks

1. Explain the cryptanalysis of the Vigenère cipher.
2. Explain the Kasiski examination with steps.
3. Explain how frequency analysis is used to break the Vigenère cipher.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
Vigenère Cipher
↓
Uses a keyword
↓
Different shift for each letter

Cryptanalysis:

1. Kasiski Examination
   • Find repeated patterns
   • Estimate keyword length

2. Frequency Analysis
   • Split ciphertext into groups
   • Break each group like a Caesar cipher
   • Recover the keyword

Weakness:
Repeated keyword
```

## Super Easy Memory Trick

Imagine a **password lock**:

* **Shift Cipher** = A lock with **one number** (easy to guess).
* **Vigenère Cipher** = A lock with **multiple rotating numbers** (harder to guess).

To break the Vigenère lock:

1. **Figure out how many rotating wheels there are** → **Kasiski Examination**.
2. **Crack each wheel one by one** → **Frequency Analysis**.
3. **Combine them** → Recover the keyword and decrypt the message. 🔑
