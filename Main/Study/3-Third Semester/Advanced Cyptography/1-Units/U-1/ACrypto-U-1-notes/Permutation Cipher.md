## Permutation Cipher (Transposition Cipher) — Detailed Explanation

A **permutation cipher** (also called a **transposition cipher**) is a classical cipher where:

> The **letters of the plaintext are NOT changed**, only their **positions are rearranged (permuted)** according to a fixed rule/key.

So unlike substitution ciphers, the alphabet stays the same — only order changes.

---

# Core Idea

* Substitution → changes letters
* Permutation → changes positions

Example:

Plaintext: `HELLO`
After permutation: `LHOEL` (same letters, different order)

---

# Basic Principle

We define a **key-based rearrangement rule**.

Example key:

```text id="p7k2q1"
Key: 3 1 4 2
```

This means: rearrange positions of blocks according to this order.

---

# Simple Example (Columnar Transposition)

Let’s encrypt:

Plaintext: `ATTACKATDAWN`

---

## Step 1: Write in rows

Assume key length = 4

```text id="v3k9p2"
A T T A
C K A T
D A W N
```

---

## Step 2: Assign key order

Key: `3 1 4 2`

So columns are read in order: **1 → 2 → 3 → 4**

---

## Step 3: Read column-wise

Column 1 → K A A
Column 2 → T T A
Column 3 → A C D
Column 4 → A T N

Ciphertext:

**KAA TTA ACD ATN → KAATTAACDATN**

---

# Key Idea in One Line

> We shuffle positions of characters using a permutation pattern.

---

# Mathematical View

Permutation cipher applies a function:

$C=P(\pi(i))$

Where:

* $P$ = plaintext positions
* $\pi(i)$ = permutation function
* $C$ = ciphertext arrangement

---

# Important Characteristics

## 1. Letters remain unchanged

* No replacement
* Only rearrangement

Example:
`HELLO` → still uses H, E, L, L, O

---

## 2. Frequency preserved

Since letters are not changed:

* E still appears same number of times
* So frequency analysis still partially works

---

# Types of Permutation Ciphers

## 1. Rail Fence Cipher

Writes text in zig-zag pattern:

Example (2 rails):

```
H   L   O
 E L L
```

Ciphertext: `HLOELL`

---

## 2. Columnar Transposition Cipher

Most common exam type (like example above)

---

## 3. Double Transposition

Apply permutation twice (more secure than single pass)

---

# Why It Is Used

* Simple encryption method
* Good at hiding **patterns in word structure**
* Used historically in military communication

---

# Weaknesses

## 1. Letter frequencies unchanged

So attacker can still guess structure.

## 2. Pattern clues remain

Example:

Repeated words may still show structure.

## 3. Vulnerable to anagram attacks

Attackers try rearranging letters to form meaningful text.

---

# Comparison with Substitution Cipher

| Feature              | Substitution    | Permutation |
| -------------------- | --------------- | ----------- |
| Changes letters?     | Yes             | No          |
| Changes positions?   | No              | Yes         |
| Preserves frequency? | No              | Yes         |
| Security level       | Slightly better | Weak alone  |

---

# Why It Matters (Shannon Theory Connection)

Permutation provides:

* **Diffusion** → spreads plaintext structure across ciphertext

But alone, it is not enough. Modern cryptography combines:

* substitution + permutation (together = strong diffusion + confusion)

---

# Exam Definition

**Permutation Cipher:** A transposition cipher in which the positions of plaintext characters are rearranged according to a fixed permutation rule without changing the characters themselves.

---

# Memory Trick

**Permutation = “Position change, not letter change”**

---

# Likely Exam Questions

1. Define permutation cipher.
2. Explain columnar transposition with example.
3. Difference between substitution and permutation cipher.
4. Why permutation cipher alone is weak?
5. Explain diffusion in permutation cipher.

---
