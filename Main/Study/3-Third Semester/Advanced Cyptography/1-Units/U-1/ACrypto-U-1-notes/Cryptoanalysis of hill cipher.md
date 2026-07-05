#advanced-cryptography 

# Cryptanalysis of Hill Cipher⭐⭐⭐⭐⭐

The **Hill Cipher** is much stronger than the **Shift** and **Vigenère** ciphers because it uses **matrix multiplication** instead of simple letter shifting.

---

# What is Cryptanalysis of Hill Cipher?

**Cryptanalysis of the Hill Cipher** is the process of finding the **key matrix** or the **plaintext** without knowing the secret key.

> **Definition (2 Marks):**
>
> **Cryptanalysis of the Hill Cipher is the process of recovering the secret key matrix or plaintext by using known plaintext-ciphertext pairs and matrix operations.**

---

# Why is Hill Cipher Hard to Break?

Unlike Caesar or Vigenère:

* Caesar uses **1 key (shift)**.
* Vigenère uses a **keyword**.
* Hill Cipher uses a **matrix**.

Example

```text
Key Matrix

| 3 3 |
| 2 5 |
```

Encryption

```text
Plaintext Vector
      ×
Key Matrix
      =
Ciphertext
```

So an attacker must find the **entire matrix**, not just one number.

---

# Main Method of Cryptanalysis ⭐⭐⭐⭐⭐

The most common attack is the **Known Plaintext Attack**.

### What does the attacker know?

* Some plaintext
* The corresponding ciphertext

Example

```text
Plaintext  : HELP

Ciphertext : HIAT
```

The attacker knows both.

---

# Step 1: Convert Letters into Numbers

Example

```text
A = 0
B = 1
C = 2
...
Z = 25
```

Suppose

```text
HE

↓

H = 7
E = 4
```

Vector

```text
|7|
|4|
```

---

# Step 2: Write Plaintext Matrix (P)

Suppose two plaintext blocks are

```text
HE

LP
```

Convert to numbers.

```text
H = 7
E = 4
L =11
P =15
```

Plaintext matrix

```text
P =

| 7 11 |
| 4 15 |
```

---

# Step 3: Write Ciphertext Matrix (C)

Suppose ciphertext is

```text
HI

AT
```

Convert

```text
H =7
I =8
A =0
T =19
```

Cipher matrix

```text
C =

| 7 0 |
| 8 19 |
```

---

# Step 4: Find the Key Matrix

Hill Cipher formula

```text
C = K × P
```

To find the key

Multiply both sides by the inverse of **P**

```text
K = C × P⁻¹  (mod 26)
```

where

* **K** = Key Matrix
* **C** = Ciphertext Matrix
* **P⁻¹** = Inverse of Plaintext Matrix (mod 26)

After performing the matrix calculations, the attacker recovers the key matrix.

---

# Diagram ⭐⭐⭐⭐

```text
Known Plaintext
        +
Known Ciphertext
          │
          ▼
Create Matrices
          │
          ▼
Find Inverse of Plaintext Matrix
          │
          ▼
K = C × P⁻¹ (mod 26)
          │
          ▼
Recover Key Matrix
          │
          ▼
Decrypt Future Messages
```

---

# Why Does This Work?

The Hill Cipher always satisfies

```text
Ciphertext = Key × Plaintext
```

If the attacker knows both **Plaintext** and **Ciphertext**, the only unknown is the **Key Matrix**.

Using matrix algebra, the key can be recovered.

---

# Weakness of Hill Cipher

The Hill Cipher is vulnerable to a **Known Plaintext Attack**.

If enough plaintext-ciphertext pairs are known, the attacker can compute the key matrix.

---

# Conditions Required

To recover the key matrix:

* The attacker must know enough plaintext-ciphertext pairs.
* The plaintext matrix must be **invertible modulo 26**.
* If the matrix has no inverse, the attack cannot proceed with that matrix.

---

# Example (Concept Only)

Suppose

```text
Plaintext

HELP
```

↓

Ciphertext

```text
HIAT
```

Attacker

1. Converts letters into numbers.
2. Forms plaintext and ciphertext matrices.
3. Computes the inverse of the plaintext matrix.
4. Uses

```text
K = C × P⁻¹ (mod 26)
```

5. Finds the secret key matrix.
6. Uses that key to decrypt future messages.

---

# Hill vs Vigenère Cryptanalysis

| Hill Cipher            | Vigenère Cipher                   |
| ---------------------- | --------------------------------- |
| Matrix-based           | Keyword-based                     |
| Uses matrix inverse    | Uses Kasiski + Frequency Analysis |
| Known Plaintext Attack | Frequency Analysis                |
| Harder to break        | Easier than Hill                  |

---

# Exam Definition ⭐⭐⭐⭐⭐

> **Cryptanalysis of the Hill Cipher is performed using a known plaintext attack, where known plaintext and ciphertext pairs are converted into matrices. The key matrix is recovered using the formula K = C × P⁻¹ (mod 26).**

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define cryptanalysis of the Hill Cipher.
2. Which attack is commonly used against the Hill Cipher?
3. Why must the plaintext matrix be invertible?

### 5 Marks

1. Explain the cryptanalysis of the Hill Cipher.
2. Explain the known plaintext attack on the Hill Cipher.
3. Explain how the key matrix is recovered using matrix operations.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
Hill Cipher Cryptanalysis

Attack Used:
Known Plaintext Attack

Steps:
1. Obtain plaintext and ciphertext pairs.
2. Convert letters to numbers.
3. Form plaintext matrix (P).
4. Form ciphertext matrix (C).
5. Compute P⁻¹ (mod 26).
6. Find key:
   K = C × P⁻¹ (mod 26).
7. Use the key to decrypt future messages.

Weakness:
If enough plaintext-ciphertext pairs are known, the key matrix can be recovered.
```

## Easy Memory Trick ⭐⭐⭐⭐⭐

Think of the Hill Cipher like solving a math equation.

You know:

```text
Ciphertext = Key × Plaintext
```

You want to find the **Key**.

Just like algebra:

```text
2x = 10
```

You solve for **x**.

Similarly:

```text
K × P = C
```

Move **P** to the other side using its **inverse**:

```text
K = C × P⁻¹
```

That's the main idea behind the cryptanalysis of the Hill Cipher and is usually what examiners expect in a 5-mark answer.
