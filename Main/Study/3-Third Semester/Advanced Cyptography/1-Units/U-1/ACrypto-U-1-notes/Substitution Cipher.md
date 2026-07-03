#advanced-cryptography 
## Substitution Cipher (Detailed Explanation)

A **substitution cipher** is an encryption technique where each letter (or symbol) in the plaintext is **replaced by another letter/symbol** according to a fixed rule.

The positions of letters stay the same, only identities change.

![](../../../../../../../Images/Third_Sem_Images/Substitution%20Cipher.png)
- [Permutation in Substitution Cipher](Permutation%20in%20Substitution%20Cipher.md)

---

## Basic Idea

Plaintext:

`HELLO`

If rule is:

* A → D
* B → E
* C → F
* H → K
* E → H
* L → O
* O → R

Then:

`HELLO` → `KHOOR`

(Example of Caesar/Shift substitution)

---

# Main Principle

Instead of writing original letters, substitute with mapped letters.

```text id="zvfqfw"
Plaintext alphabet : ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher alphabet    : QWERTYUIOPASDFGHJKLZXCVBNM
```

So:

* A → Q
* B → W
* C → E
  etc.

---

# Types of Substitution Cipher

## 1. Monoalphabetic Substitution Cipher

- Each letter is always replaced by the same unique letter.

Uses **one fixed alphabet mapping** for entire message.

Example:

```text id="xw3h1x"
A→M
B→N
C→B
D→V
...
```

Message:

`BAD` → `NMV`

### Characteristics

* Same plaintext letter always becomes same ciphertext letter.
* Easy to implement.
* Vulnerable to frequency analysis.

---

## 2. Caesar Cipher (Shift Cipher)

A special monoalphabetic substitution.

Each letter shifted by fixed number.

Example shift +3:

* A→D
* B→E
* C→F

`HELLO` → `KHOOR`

---

## 3. Affine Cipher

Also substitution based, but uses formula:

$C=(aP+b)\bmod26$

Each letter replaced mathematically.

---

## 4. Polyalphabetic Substitution Cipher

- A plaintext letter may be replaced by different letters depending on its position or the key.

Uses multiple substitution alphabets.

Example: Vigenère Cipher

Same plaintext letter may encrypt differently depending on position/key.

Example:

`A` may become `D` in one place, `M` in another.

Harder to break than monoalphabetic.

---

# Encryption Process (Monoalphabetic)

Suppose key mapping:

```text id="t9gz3j"
ABCDEFGHIJKLMNOPQRSTUVWXYZ
QWERTYUIOPASDFGHJKLZXCVBNM
```

Encrypt `CAT`

* C → E
* A → Q
* T → Z

Ciphertext = `EQZ`

---

# Decryption Process

Use reverse mapping:

* E → C
* Q → A
* Z → T

Recovered plaintext = `CAT`

---

# Why It Was Used Historically

* Simple by hand
* No machines needed
* Useful before computers
* Military and diplomatic use in old times

---

# Weaknesses (Important)

## Frequency Analysis

In English:

* E most common
* T common
* A common
* TH, HE common pairs

If ciphertext letter `X` appears most often, maybe it means `E`.

Since same plaintext letter always maps same ciphertext letter, patterns remain.

This is why monoalphabetic substitution is weak.

---

# Example Attack

Ciphertext:

`QZZQF QZZQF`

Repeated pattern suggests repeated word.

Could be:

`HELLO HELLO`

Patterns help attacker.

---

# Advantages

* Easy to understand
* Simple manual encryption
* Better than plain text

---

# Disadvantages

* Weak against frequency analysis
* Pattern leaks
* Not secure today

---

# Exam Definition

**Substitution Cipher:** A classical encryption method in which each plaintext letter is replaced by another letter or symbol according to a substitution rule.

---

# Memory Trick

**Substitution = Replace letters**
**Permutation = Rearrange letters**

---

# Comparison with Permutation Cipher

| Feature          | Substitution | Permutation |
| ---------------- | ------------ | ----------- |
| Changes letters? | Yes          | No          |
| Changes order?   | No           | Yes         |
| Example          | A→D          | CAT→TCA     |

---

# Deep Understanding

Substitution hides **what letters are used**
Permutation hides **where letters are placed**

Modern ciphers combine both ideas.

---
