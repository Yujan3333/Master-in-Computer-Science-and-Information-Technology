#advanced-cryptography 

# Cryptanalysis of Permutation (Transposition) Cipher ⭐⭐⭐⭐⭐ (Exam-Focused)

This is another common **5-mark exam question**.

Unlike Caesar, Vigenère, or Hill ciphers, a **Permutation (Transposition) Cipher does NOT change the letters**.

It **only changes their positions**.

---

# What is a Permutation Cipher?

Example

Plaintext

```text
HELLO
```

After permutation

```text
LEHLO
```

Notice:

```text
Letters are the same.
Only positions changed.
```

---

# What is Cryptanalysis of Permutation Cipher?

**Cryptanalysis of a permutation cipher** is the process of finding the **correct order of letters** (or the permutation key) to recover the original plaintext.

> **Definition (2 Marks):**
>
> **Cryptanalysis of a permutation cipher is the process of recovering the original arrangement of letters or the permutation key without knowing the key.**

---

# Main Idea ⭐⭐⭐⭐⭐

Unlike substitution ciphers,

```text
HELLO

↓

KHOOR
```

Letters change.

But in permutation ciphers,

```text
HELLO

↓

LEHLO
```

Letters **never change**.

Only their **positions** change.

This makes cryptanalysis different.

---

# Methods of Cryptanalysis

There are **two common methods**.

---

# Method 1: Anagramming ⭐⭐⭐⭐⭐ (Most Important)

Since all original letters are present,

the attacker tries to **rearrange** the letters into meaningful words.

### Example

Ciphertext

```text
ETH
```

Possible arrangements

```text
THE ✅

ETH

TEH

HET
```

"The" is meaningful.

Therefore

```text
Plaintext = THE
```

---

Another example

Ciphertext

```text
LHEOL
```

Rearrange

```text
HELLO ✅
```

---

# Method 2: Frequency and Language Patterns ⭐⭐⭐⭐

Since letters are **not changed**,

English letter frequencies remain exactly the same.

The attacker looks for common English patterns.

Examples

```text
TH

HE

ER

ING

TION
```

Suppose ciphertext is

```text
HTE
```

Possible arrangements

```text
THE ✅

HET

ETH
```

"The" is the most likely plaintext.

---

# If the Block Size is Known ⭐⭐⭐⭐

Suppose encryption uses blocks of **4 letters**.

Ciphertext

```text
LLEHO WRODL
```

Break into blocks

```text
LLEH

OWRO

DL
```

The attacker tries different rearrangements.

```text
LLEH

↓

HELL
```

```text
OWRO

↓

OWOR

↓

WORO

↓

WORL
```

Eventually

```text
HELLO WORLD
```

is obtained.

---

# Brute Force Attack ⭐⭐⭐⭐

Suppose each block has **4 letters**.

Number of possible arrangements

```text
4! = 24
```

Try all 24 arrangements.

One will produce meaningful English.

---

If block size is **5**

```text
5!

=

120
```

possible arrangements.

---

# Why is Permutation Cipher Easier to Break?

Because

* Letters never change.
* Letter frequencies remain the same.
* Common English words are easy to recognize.
* Small block sizes have very few possible permutations.

---

# Example

Ciphertext

```text
ETM
```

Possible arrangements

```text
TEM

MET

EMT

MET ✅
```

Meaningful word

```text
MET
```

Therefore

```text
Plaintext = MET
```

---

# Diagram

```text
Ciphertext
      │
      ▼
Letters stay the same
      │
      ▼
Try different arrangements
      │
      ▼
Find meaningful English words
      │
      ▼
Recover permutation key
      │
      ▼
Decrypt message
```

---

# Why Frequency Analysis Alone Cannot Recover the Key

Suppose plaintext is

```text
HELLO
```

Ciphertext

```text
LEHLO
```

Letter frequencies

| Letter | Count |
| ------ | ----: |
| H      |     1 |
| E      |     1 |
| L      |     2 |
| O      |     1 |

Exactly the same.

Frequency analysis tells us **which letters exist**, but **not where they belong**.

Therefore,

the attacker must use

* anagramming,
* language patterns,
* or brute-force permutation testing.

---

# Permutation vs Substitution Cryptanalysis ⭐⭐⭐⭐⭐

| Permutation Cipher    | Substitution Cipher                     |
| --------------------- | --------------------------------------- |
| Letters unchanged     | Letters replaced                        |
| Positions change      | Characters change                       |
| Use anagramming       | Use frequency analysis                  |
| Frequencies unchanged | Frequencies change to different symbols |

---

# Exam Definition ⭐⭐⭐⭐⭐

> **Cryptanalysis of a permutation cipher is performed by rearranging the letters into meaningful plaintext using anagramming, language patterns, and brute-force testing of possible permutations.**

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define cryptanalysis of a permutation cipher.
2. Why is a permutation cipher vulnerable to anagramming?
3. Why does frequency analysis alone not recover the key?

---

### 5 Marks

1. Explain the cryptanalysis of a permutation cipher.
2. Explain how anagramming is used to break a permutation cipher.
3. Explain brute-force cryptanalysis of a permutation cipher.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
Permutation Cipher

Letters stay the same
↓

Only positions change

Cryptanalysis

1. Rearrange letters (Anagramming)
2. Use English language patterns
3. Try all permutations (Brute Force)
4. Recover the original order

Weakness:
• Same letters
• Same frequencies
• Small block size → Easy brute force
```

## Memory Trick ⭐⭐⭐⭐⭐

Think of a **jigsaw puzzle**.

Original word:

```text
HELLO
```

Someone mixes the pieces:

```text
LHEOL
```

Nothing is missing—**the letters are all still there**.

Your job is simply to **put the letters back in the correct order**.

That's exactly what **cryptanalysis of a permutation cipher** does.
