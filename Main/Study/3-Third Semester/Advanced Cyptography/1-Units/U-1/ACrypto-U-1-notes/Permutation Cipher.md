## Permutation Cipher (Transposition Cipher) — Detailed Explanation

A **permutation cipher** (also called a **transposition cipher**) is a classical cipher where:

> The **letters of the plaintext are NOT changed**, only their **positions are rearranged (permuted)** according to a fixed rule/key.

So unlike substitution ciphers, the alphabet stays the same — only order changes.

![](../../../../../../../Images/Third_Sem_Images/Permutation%20Cipher.png)

---

# Core Idea

* Substitution → changes letters
* Permutation → changes positions

Example:

Plaintext: `HELLO`
After permutation: `LHOEL` (same letters, different order)

![](../../../../../../../Images/Third_Sem_Images/Permutation%20Cipher-ex.png)
- Here in inverse permutation the *1 is replaced by 3 so in 3 there is 1*
- [Further explanation of how inverse in Permutation Cipher works](Further%20explanation%20of%20how%20inverse%20in%20Permutation%20Cipher%20works.md)
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
- [Detailed understanding of ex of Columnar Transposition](Detailed%20understanding%20of%20ex%20of%20Columnar%20Transposition.md)


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

# [Types of Permutation Ciphers](Types%20of%20Permutation%20Ciphers.md)

##### 1. Rail Fence Cipher
##### 2. Columnar Transposition Cipher
##### 3. Double Transposition

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
