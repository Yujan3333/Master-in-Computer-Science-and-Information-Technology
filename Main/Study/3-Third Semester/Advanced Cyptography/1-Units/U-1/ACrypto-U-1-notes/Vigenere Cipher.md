#advanced-cryptography 
## Vigenère Cipher (Detailed Explanation)

The **Vigenère Cipher** is a **polyalphabetic substitution cipher** that uses a **keyword** to encrypt plaintext.

Unlike Caesar cipher (same shift every letter), Vigenère uses **different shifts** based on the repeating key.

This makes it stronger than monoalphabetic ciphers.

![](../../../../../../../Images/Third_Sem_Images/Vigenere%20Cipher.png)

---

# Main Idea

Each letter of plaintext is shifted according to the corresponding key letter.

Example:

Plaintext: `HELLO`
Key: `KEYKE`

(Original key `KEY` repeated)

Each key letter gives a different shift.

---

# Letter Values

```text id="49r3zm"
A=0 B=1 C=2 ... Z=25
```

---

# Encryption Formula

$$C=(P+K)\bmod26$$

Where:

* $P$ = plaintext letter number
* $K$ = key letter number
* $C$ = ciphertext letter number

---

# Decryption Formula

$$P=(C-K)\bmod26$$

---

# Step-by-Step Example

## Encrypt HELLO using key KEY

Plaintext:

`H E L L O`

Numbers:

* H=7
* E=4
* L=11
* L=11
* O=14

Key:

`K E Y K E`

Numbers:

* K=10
* E=4
* Y=24
* K=10
* E=4

---

## Encrypt Each Letter

| Plain |  P | Key |  K | Calculation     | Cipher |
| ----- | -: | --- | -: | --------------- | ------ |
| H     |  7 | K   | 10 | $(7+10)=17$     | R      |
| E     |  4 | E   |  4 | $(4+4)=8$       | I      |
| L     | 11 | Y   | 24 | $(35)\bmod26=9$ | J      |
| L     | 11 | K   | 10 | $(21)$          | V      |
| O     | 14 | E   |  4 | $(18)$          | S      |

Ciphertext = **RIJVS**

---

# Decryption Example

Ciphertext: `RIJVS`
Key: `KEYKE`

| Cipher |  C | Key |  K | Calculation      | Plain |
| ------ | -: | --- | -: | ---------------- | ----- |
| R      | 17 | K   | 10 | $(17-10)=7$      | H     |
| I      |  8 | E   |  4 | $(8-4)=4$        | E     |
| J      |  9 | Y   | 24 | $9-24=-15+26=11$ | L     |
| V      | 21 | K   | 10 | 11               | L     |
| S      | 18 | E   |  4 | 14               | O     |

Recovered plaintext = **HELLO**

---

# Why It Is Stronger Than Caesar

## Caesar Cipher

Same shift every letter.

```text id="9j5r3v"
HELLO
+3 +3 +3 +3 +3
```

## Vigenère Cipher

Different shifts:

```text id="msy8fz"
HELLO
K E Y K E
10 4 24 10 4
```

So repeated plaintext letters may become different ciphertext letters.

Example:

Two `L`s in HELLO became:

* `J`
* `V`

This hides frequency patterns.

---

# Why Called Polyalphabetic

Because it uses many substitution alphabets, not just one.

Each key letter creates a different Caesar shift.

---

# Key Repetition Rule

If key shorter than message, repeat it.

Example:

Message: `ATTACKNOW`

Key: `DOG`

Repeated key:

```text id="w8nyw9"
DOGDOGDOG
```

---

# Weaknesses

Still breakable if key repeats.

Attack methods:

## 1. Kasiski Examination

Looks for repeated ciphertext patterns to guess key length.

## 2. Frequency Analysis by Columns

Once key length known, split letters into groups and solve like Caesar ciphers.

---

# Advantages

* Stronger than shift and affine
* Hides simple frequency better
* Easy by hand

---

# Disadvantages

* Repeating key creates weakness
* Not secure for modern use

---

# Exam Definition

**Vigenère Cipher:** A polyalphabetic substitution cipher in which plaintext letters are encrypted using repeated keyword shifts.

---

# Memory Trick

**Caesar = one shift**
**Vigenère = many shifts**

---

# Likely Exam Questions

1. Define Vigenère cipher.
2. Encrypt HELLO using KEY.
3. Decrypt RIJVS using KEY.
4. Why stronger than Caesar cipher?
5. Explain Kasiski attack.

---

# Deep Understanding

Caesar changes letters uniformly.
Vigenère changes letters contextually based on key position.
That was a huge historical improvement before modern cryptography.
