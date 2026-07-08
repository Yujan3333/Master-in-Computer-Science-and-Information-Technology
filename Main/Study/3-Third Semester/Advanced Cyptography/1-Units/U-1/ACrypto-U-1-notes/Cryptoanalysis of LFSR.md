#advanced-cryptography #third-semester 

# Cryptanalysis of LFSR (Linear Feedback Shift Register) ⭐⭐⭐⭐⭐ (Exam-Focused)

---

# What is an LFSR?

An **LFSR (Linear Feedback Shift Register)** is used to generate a **keystream** in a stream cipher.

Example

```text
Initial State

1 0 1 1
```

↓

Generates keystream

```text
101101001101...
```

The keystream is XORed with the plaintext.

```text
Plaintext
     ⊕
Keystream
     =
Ciphertext
```

---

# What is Cryptanalysis of LFSR?

**Cryptanalysis of an LFSR** is the process of finding the **initial state (seed)** or the **feedback polynomial** so that the attacker can generate the same keystream and decrypt the ciphertext.

### Definition (2 Marks)

> **Cryptanalysis of an LFSR is the process of recovering the initial state or feedback function of the LFSR to reproduce the keystream and decrypt the ciphertext.**

---

# Why Attack an LFSR?

Suppose

```text
Plaintext
⊕
Keystream
=
Ciphertext
```

If the attacker finds the **keystream**, then

```text
Ciphertext
⊕
Keystream
=
Plaintext
```

So the attacker's goal is to generate the same keystream.

---

# Main Weakness of LFSR ⭐⭐⭐⭐⭐

An LFSR is called **Linear** because every new bit is calculated using **linear XOR operations**.

Example

```text
New Bit = Bit1 ⊕ Bit4
```

Because it is linear,

mathematical equations can be formed.

These equations can be solved to find the unknown state.

---

# Methods of Cryptanalysis ⭐⭐⭐⭐⭐

## 1. Known Plaintext Attack (Most Common)

Suppose the attacker knows

```text
Plaintext

HELLO
```

and

```text
Ciphertext
```

Since

```text
Ciphertext = Plaintext ⊕ Keystream
```

the attacker computes

```text
Keystream = Plaintext ⊕ Ciphertext
```

Now the attacker has part of the keystream.

Using enough keystream bits,

the attacker finds

* Initial State
* Feedback Polynomial

---

## Example

Suppose

```text
Plaintext

101101
```

Ciphertext

```text
111001
```

Compute

```text
101101
⊕

111001
--------
010100
```

Recovered keystream

```text
010100
```

Now use these bits to determine the LFSR.

---

# 2. Berlekamp–Massey Algorithm ⭐⭐⭐⭐⭐ (Most Important)

This is the **standard attack** on an LFSR.

### Purpose

Given enough keystream bits,

it finds

* Feedback polynomial
* Length of the LFSR

---

### How it Works (Concept)

Suppose the attacker observes

```text
101101011001...
```

The algorithm analyzes this sequence.

Eventually it finds

```text
LFSR Length = 5

Feedback

New Bit = Bit5 ⊕ Bit2
```

Now the attacker builds the same LFSR.

Generates the same keystream.

Decrypts every message.

---

# Diagram

```text
Ciphertext
       +
Known Plaintext
        │
        ▼
Recover Keystream
        │
        ▼
Berlekamp–Massey Algorithm
        │
        ▼
Recover LFSR
        │
        ▼
Generate Same Keystream
        │
        ▼
Decrypt Future Messages
```

---

# Why is LFSR Vulnerable?

Because

* XOR is linear.
* Future bits depend on previous bits.
* Enough output bits reveal the entire LFSR.

---

# How Many Bits Are Needed?

Suppose

LFSR length

```text
n
```

Usually about

```text
2n
```

output bits are enough for the Berlekamp–Massey algorithm to recover the LFSR.

Example

```text
LFSR = 8 bits

↓

Need about

16 keystream bits
```

to reconstruct the LFSR.

---

# How to Make LFSR More Secure?

Instead of one LFSR,

use

* Multiple LFSRs
* Nonlinear Feedback Shift Register (NLFSR)
* Nonlinear combining functions
* Irregular clocking

Example

```text
LFSR 1

+

LFSR 2

+

LFSR 3

↓

Nonlinear Function

↓

Keystream
```

This makes cryptanalysis much harder.

---

# LFSR vs NLFSR

| LFSR                          | NLFSR                                    |
| ----------------------------- | ---------------------------------------- |
| Linear feedback               | Nonlinear feedback                       |
| Easier to attack              | Harder to attack                         |
| Berlekamp–Massey works        | Berlekamp–Massey does not directly apply |
| Used in simple stream ciphers | Used in stronger stream ciphers          |

---

# Exam Definition ⭐⭐⭐⭐⭐

> **Cryptanalysis of an LFSR involves recovering the initial state and feedback polynomial from the keystream. The most common technique is the Berlekamp–Massey algorithm, which reconstructs the LFSR from a sufficient number of output bits.**

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define cryptanalysis of an LFSR.
2. What is the weakness of an LFSR?
3. What is the Berlekamp–Massey algorithm?

### 5 Marks

1. Explain the cryptanalysis of an LFSR.
2. Explain how a known plaintext attack is used against an LFSR.
3. Explain the Berlekamp–Massey algorithm.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
LFSR

↓

Generates Keystream

↓

Weakness:
Linear XOR operations

↓

Attack:
Recover keystream

↓

Use Berlekamp–Massey Algorithm

↓

Recover
• Initial State
• Feedback Polynomial

↓

Generate same keystream

↓

Decrypt messages
```

# Super Easy Memory Trick ⭐⭐⭐⭐⭐

Think of an LFSR like a **recipe** for making cookies.

* **Initial state** = the starting ingredients.
* **Feedback polynomial** = the recipe.

If someone discovers **both**, they can bake **exactly the same cookies**.

Similarly:

* **Initial state (seed)** + **feedback polynomial** = **same keystream**.
* Once an attacker recreates the same keystream, they can decrypt the encrypted messages.
