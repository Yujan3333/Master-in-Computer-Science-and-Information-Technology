#advanced-cryptography 
## Unit 1: Shannon Theory and Classical Cryptography (Summary)

### 1. Cryptosystems

A **cryptosystem** is a method used to secure information using:

* **Plaintext** = original message
* **Ciphertext** = encrypted message
* **Encryption algorithm** = converts plaintext to ciphertext
* **Decryption algorithm** = converts ciphertext back to plaintext
* **Key** = secret value used in encryption/decryption

Goal: **Confidentiality, Integrity, Authentication**

---

### 2. Shannon Theory

Introduced by Claude Shannon, considered the father of modern cryptography.

Main ideas:

* **Confusion**: Hide relationship between key and ciphertext

* **Diffusion**: Spread influence of plaintext across ciphertext
	* A small change in the original message should affect many parts of the encrypted message, not just one letter/bit.

* **Redundancy removal**: Makes cryptanalysis harder

These principles are used in modern ciphers.

---

### 3. Evaluation of Cryptosystems

#### a) Computational Security

* System is secure because breaking it requires too much **time/computing power**.
* Practical security.

#### b) Provable Security

* Security is mathematically proven based on hard problems.

#### c) Unconditional Security

* Cannot be broken even with unlimited computing power.
* Example: **[One-Time Pad](One-Time%20Pad.md)**

---

### 4. Entropy

Entropy measures **uncertainty/randomness** in data.

* Higher entropy = more unpredictable = stronger security
* Lower entropy = easier to guess

Used in passwords, keys, randomness.

---

## 5. Classical Cryptosystems

- [Substitution Cipher](Substitution%20Cipher.md)

### a) Shift Cipher (Caesar Cipher)

* Each letter shifted by fixed number positions.
* Example: A → D (shift +3)


### b) Affine Cipher
- [Affine Cipher](Affine%20Cipher.md)
Uses formula:

$$C=(aP+b)\bmod26$$

More secure than shift cipher.

### c) Vigenère Cipher
- [Vigenere Cipher](Vigenere%20Cipher.md)

* Uses repeating keyword for multiple shifts.
* Polyalphabetic cipher.

### d) Hill Cipher
- [Hill Cipher](Hill%20Cipher.md)

* Uses matrix multiplication and modular arithmetic.
* Encrypts blocks of letters.

### e) Permutation Cipher
- [Permutation Cipher](Permutation%20Cipher.md)

* Rearranges positions of letters without changing letters.

---

## 6. Cryptanalysis (Breaking Classical Ciphers)

### Shift Cipher

* Try all 25 possible shifts (brute force)

### Affine Cipher

* Try possible values of $a$ and $b$

### Vigenère Cipher

* Frequency analysis, Kasiski test

### Hill Cipher

* Use known plaintext and matrix inverse

### Permutation Cipher

* Try possible rearrangements, frequency clues

---

## Short Exam Summary

Unit 1 covers:

* Basics of cryptosystems
* Shannon’s security principles
* Security types: computational, provable, unconditional
* Entropy concept
* Classical ciphers: Shift, Affine, Vigenère, Hill, Permutation
* Methods to attack these ciphers
