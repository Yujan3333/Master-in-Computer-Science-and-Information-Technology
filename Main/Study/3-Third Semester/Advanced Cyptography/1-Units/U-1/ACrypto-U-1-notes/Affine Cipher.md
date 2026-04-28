## Affine Cipher (Detailed Explanation)

The **Affine Cipher** is a **monoalphabetic substitution cipher** where each plaintext letter is converted into ciphertext using a mathematical formula.

It is stronger than simple Caesar cipher because it uses **multiplication + addition**.

---

# Core Formula

## Encryption

C=(aP+b)\bmod 26

## Decryption

P=a^{-1}(C-b)\bmod 26

Where:

* $P$ = plaintext letter number
* $C$ = ciphertext letter number
* $a,b$ = keys
* $a^{-1}$ = modular inverse of $a$ modulo 26

Alphabet numbering:

```text id="p8f41v"
A=0 B=1 C=2 ... Z=25
```

---

# Why Called Affine?

Because it uses a linear transformation:

multiply by $a$, then add $b$.

---

# Important Condition on Key $a$

$a$ must be **coprime with 26**, otherwise decryption fails.

Valid values:

```text id="2ry01s"
1,3,5,7,9,11,15,17,19,21,23,25
```

Because these have modular inverses mod 26.

---

# Example Encryption

Use keys:

* $a=5$
* $b=8$

Encrypt plaintext: `H`

`H = 7`

Apply formula:

C=(5\cdot7+8)\bmod26

$35+8=43$

$43\bmod26=17$

17 = `R`

So:

`H → R`

---

# Encrypt Full Word: HELLO

Letters:

* H=7
* E=4
* L=11
* L=11
* O=14

Apply formula $C=(5P+8)\bmod26$

| Plain |  P | Calculation         |  C | Cipher |
| ----- | -: | ------------------- | -: | ------ |
| H     |  7 | $(5×7+8)=43\bmod26$ | 17 | R      |
| E     |  4 | $(5×4+8)=28\bmod26$ |  2 | C      |
| L     | 11 | $(55+8)=63\bmod26$  | 11 | L      |
| L     | 11 | same                | 11 | L      |
| O     | 14 | $(70+8)=78\bmod26$  |  0 | A      |

Ciphertext = **RCLLA**

---

# Decryption Example

Ciphertext letter: `R`

`R=17`

Need inverse of $5$ mod 26.

Find number such that:

$5x\equiv1\pmod{26}$

$x=21$ because:

$5×21=105 \equiv1 \pmod{26}$

So inverse of 5 is 21.

Now decrypt:

P=21(17-8)\bmod26

$=21×9=189$

$189\bmod26=7$

7 = `H`

Recovered correctly.

---

# Why Stronger than Caesar Cipher

Caesar only adds shift:

C=P+k

Affine uses multiply + shift:

C=aP+b

So letter relationships are more scrambled.

---

# Still Weak Because

It is still monoalphabetic:

* Same plaintext letter always same ciphertext letter
* Frequency analysis still works
* Brute force possible (limited keys)

Total keys:

* 12 possible $a$
* 26 possible $b$

Total = **312 keys only**

Very weak by modern standards.

---

# Steps to Solve Exam Numericals

## Encryption

1. Convert letters to numbers
2. Apply $C=(aP+b)\bmod26$
3. Convert back to letters

## Decryption

1. Convert ciphertext letters to numbers
2. Find inverse of $a$ mod 26
3. Apply $P=a^{-1}(C-b)\bmod26$
4. Convert back to letters

---

# Exam Definition

**Affine Cipher:** A substitution cipher where each plaintext letter is mapped to ciphertext using the function $C=(aP+b)\bmod26$, where $a$ and $b$ are keys.

---

# Memory Trick

**Affine = Arithmetic Cipher**

* multiply
* add
* mod 26

---
