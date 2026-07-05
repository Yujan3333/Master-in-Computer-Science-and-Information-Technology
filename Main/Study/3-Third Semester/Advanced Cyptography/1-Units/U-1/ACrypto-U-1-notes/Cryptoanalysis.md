#advanced-cryptography 

---

# Definition

**Cryptanalysis** is the process of **breaking encryption** by trying to recover the **plaintext or the secret key** **without knowing the key**.

### Simple Definition (2 Marks)

> **Cryptanalysis is the study and technique of breaking encrypted messages (ciphertext) to obtain the original plaintext or encryption key without knowing the secret key.**

---

# Easy Example

Suppose Alice sends:

```text
HELLO
```

Encrypted using Caesar Cipher (+3)

```text
KHOOR
```

Bob knows the key (+3), so he decrypts it.

But Eve (attacker) **does not know the key**.

She tries different keys:

```text
KHOOR
↓
Key 1 → JGNNQ
Key 2 → IFMMP
Key 3 → HELLO ✅
```

She successfully found the plaintext.

This process is called **Cryptanalysis**.

---

# Goal of Cryptanalysis

The attacker tries to:

* Recover the plaintext
* Find the secret key
* Break the encryption algorithm
* Read confidential information

---

# Cryptanalysis vs Cryptography ⭐⭐⭐⭐⭐

| Cryptography            | Cryptanalysis                         |
| ----------------------- | ------------------------------------- |
| Protects information    | Breaks protection                     |
| Encrypts data           | Decrypts without key                  |
| Used by sender/receiver | Used by attacker/security researchers |
| Goal is security        | Goal is finding weaknesses            |

### Easy Memory

**Cryptography = Locking the door 🔒**

**Cryptanalysis = Trying to open the locked door 🔓**

---

# Types of Cryptanalytic Attacks ⭐⭐⭐⭐⭐

## 1. Ciphertext-Only Attack (COA)

The attacker has **only the ciphertext**.

Example

```text
Ciphertext

KHOOR ZRUOG
```

No plaintext

No key

The attacker guesses the message.

**Hardest attack** because very little information is available.

---

## 2. Known Plaintext Attack (KPA)

The attacker knows

* Some plaintext
* Its corresponding ciphertext

Example

```text
Plaintext

HELLO

↓

Ciphertext

KHOOR
```

Using this information, the attacker tries to find the key.

---

## 3. Chosen Plaintext Attack (CPA)

The attacker can **choose any plaintext** and obtain its ciphertext.

Example

The attacker asks:

Encrypt

```text
AAAAA
```

Gets

```text
DDDDD
```

Then encrypts

```text
BBBBB
```

Gets

```text
EEEEE
```

Using many such pairs, the attacker discovers the key.

---

## 4. Chosen Ciphertext Attack (CCA)

The attacker chooses a ciphertext and asks for its decrypted plaintext.

Example

Ciphertext

```text
XYZABC
```

↓

System decrypts it

↓

Attacker analyzes the output to recover the key.

---

# Difficulty Order (Easy to Remember)

```text
Ciphertext Only
        ↓
Known Plaintext
        ↓
Chosen Plaintext
        ↓
Chosen Ciphertext
```

The attacker gets **more information** as you move down, making the attack generally more powerful.

---

# Brute Force Attack ⭐⭐⭐⭐⭐

The attacker tries **every possible key** until the correct one is found.

Example

Caesar Cipher has 26 possible keys.

Try

```text
Key 1

Key 2

Key 3

...

Key 26
```

Eventually, the correct plaintext is found.

---

Example

Ciphertext

```text
KHOOR
```

Try all shifts

```text
1 → JGNNQ

2 → IFMMP

3 → HELLO ✅
```

---

# Frequency Analysis ⭐⭐⭐⭐

Used mainly against substitution ciphers.

Idea:

Some letters appear more often.

Example (English)

```text
E → Most frequent

T

A

O

I
```

If a ciphertext contains many **X's**, the attacker may guess that **X = E**.

This helps recover the plaintext.

---

# Why Cryptanalysis is Important

* Tests the strength of encryption algorithms.
* Finds weaknesses before attackers do.
* Helps design stronger cryptographic systems.
* Improves computer and network security.

---

# Real-Life Applications

* Security testing
* Ethical hacking
* Government intelligence
* Cybersecurity research
* Digital forensics

---

# Exam Definitions ⭐⭐⭐⭐⭐

### Cryptanalysis

> The process of breaking encrypted messages to recover the plaintext or secret key without knowing the key.

### Brute Force Attack

> An attack that tries every possible key until the correct one is found.

### Frequency Analysis

> A method of breaking substitution ciphers by studying how often letters appear in the ciphertext.

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define cryptanalysis.
2. What is a brute force attack?
3. What is frequency analysis?
4. State the goal of cryptanalysis.

---

### 5 Marks

1. Explain cryptanalysis with an example.
2. Differentiate cryptography and cryptanalysis.
3. Explain different types of cryptanalytic attacks.
4. Explain brute force attack and frequency analysis with examples.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
Cryptanalysis
= Breaking encryption without the key.

Goal:
• Find plaintext
• Find secret key

Types:
1. Ciphertext Only Attack (COA)
2. Known Plaintext Attack (KPA)
3. Chosen Plaintext Attack (CPA)
4. Chosen Ciphertext Attack (CCA)

Common Techniques:
• Brute Force
• Frequency Analysis

Memory Trick:
Cryptography = Makes the lock 🔒
Cryptanalysis = Tries to break the lock 🔓
```

