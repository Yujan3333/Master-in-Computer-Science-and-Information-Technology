#advanced-cryptography 

## Hill Cipher (Detailed Explanation)

The **Hill Cipher** is a classical **polygraphic substitution cipher** that uses **matrix multiplication** and modular arithmetic to encrypt blocks of letters.

It was invented by Lester S. Hill.

Unlike Caesar or Vigenère (one letter at a time), Hill cipher encrypts **multiple letters together**.

---

# Main Idea

Take letters in groups (usually 2 or 3), convert to numbers, multiply by a key matrix, then take mod 26.

- If exact group of letters **cannot be taken then** [Padding Rule](#Padding%20Rule)
This mixes letters strongly.

---

# Letter Values

```text id="ah5q1z"
A=0 B=1 C=2 ... Z=25
```

---

# 2×2 Hill Cipher Formula

- [Complete Example 2x2 Matrix Hill Cipher](Complete%20Example%202x2%20Matrix%20Hill%20Cipher.md)
- [Example 3x3 Matrix In Youtube](https://www.youtube.com/watch?v=qU1kcpuJXaw&list=PL9FuOtXibFjV77w2eyil4Xzp8eooqsPp8&index=16)

## Encryption

$C=KP\pmod{26}$

Where:

* $K$ = key matrix
* $P$ = plaintext column vector
* $C$ = ciphertext column vector

---

# Example Key Matrix

Use:

$K=\begin{bmatrix}3&3\\2&5\end{bmatrix}$

---

# Encrypt Example: HI

## Step 1: Convert Letters

* H = 7
* I = 8

Plaintext vector:

$P=\begin{bmatrix}7\\8\end{bmatrix}$

---

## Step 2: Multiply

$C=\begin{bmatrix}3&3\\2&5\end{bmatrix}\begin{bmatrix}7\\8\end{bmatrix}$

Compute:

First row:

$(3×7)+(3×8)=21+24=45$

Second row:

$(2×7)+(5×8)=14+40=54$

So:

$C=\begin{bmatrix}45\\54\end{bmatrix}\pmod{26}$

---

## Step 3: Apply mod 26

* $45\bmod26=19$
* $54\bmod26=2$

So:

$C=\begin{bmatrix}19\\2\end{bmatrix}$

19 = T
2 = C

Ciphertext = **TC**

---

# Decryption

Need inverse of key matrix:

$P=K^{-1}C\pmod{26}$

So decrypt by multiplying ciphertext vector with inverse matrix mod 26.

---

# Important Condition

Key matrix must be **invertible mod 26**.

That means determinant must have inverse modulo 26.

If not invertible, decryption impossible.

---

# Determinant Check (2×2)

For matrix:

$\begin{bmatrix}a&b\\c&d\end{bmatrix}$

Determinant:

$ad-bc$

Need:

$\gcd(ad-bc,26)=1$

---

# Why Hill Cipher Was Important

It provides **diffusion**:

Changing one plaintext letter changes multiple ciphertext letters.

Example:

`HI` and `HJ` produce very different outputs.

This matches Shannon’s diffusion principle.

---

# Advantages

* Encrypts blocks, not single letters
* Better letter mixing
* Hides single-letter frequencies more than monoalphabetic ciphers

---

# Weaknesses

* If attacker knows enough plaintext/ciphertext pairs, key matrix can be solved using linear algebra.
* Not secure today.

---

# Padding Rule

If plaintext length not multiple of block size, add filler letter like X.

Example:

`CAT` → `CATX`

---

# Exam Steps for Numericals

## Encryption

1. Choose key matrix
2. Convert letters to numbers
3. Split into blocks
4. Multiply $KP$
5. Take mod 26
6. Convert to letters

## Decryption

1. Find inverse of key matrix mod 26
2. Multiply $K^{-1}C$
3. mod 26
4. Convert back

---

# Exam Definition

**Hill Cipher:** A polygraphic substitution cipher that uses matrix multiplication modulo 26 to encrypt groups of plaintext letters.

---

# Memory Trick

**Hill = Linear Algebra Cipher**

letters → vectors → matrix multiply → ciphertext

---

# Likely Exam Questions

1. Define Hill cipher.
2. Encrypt plaintext using given 2×2 matrix.
3. Why must determinant be coprime with 26?
4. Explain diffusion in Hill cipher.
5. Compare Hill and Vigenère.

---

# Deep Understanding

Caesar changes one letter.
Vigenère changes letters with key shifts.
Hill mixes letters together mathematically.

That was a major leap toward modern block ciphers.
