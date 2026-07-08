#advanced-cryptography #hill-cipher #example #third-semester 


### Key Matrix

$$
K=
\begin{bmatrix}
3 & 3\\
2 & 5
\end{bmatrix}
$$

Plaintext:

```text
HI
```

---

# Step 1: Convert letters to numbers

| Letter | Number |
| ------ | ------ |
| H      | 7      |
| I      | 8      |

So,

$$
P=
\begin{bmatrix}
7\\
8
\end{bmatrix}
$$

---

# Step 2: Encryption

Use:

$$
C=KP\pmod{26}
$$

Multiply:

$$
\begin{bmatrix}
3&3\\
2&5
\end{bmatrix}
\begin{bmatrix}
7\\
8
\end{bmatrix}
=============

\begin{bmatrix}
45\\
54
\end{bmatrix}
$$

Take mod 26:

$$
45\bmod26=19
$$

$$
54\bmod26=2
$$

So,

$$
C=
\begin{bmatrix}
19\\
2
\end{bmatrix}
$$

Convert back to letters:

| Number | Letter |
| ------ | ------ |
| 19     | T      |
| 2      | C      |

### Ciphertext

```text
TC
```

---

# Decryption

Now decrypt **TC**.

Ciphertext numbers:

| Letter | Number |
| ------ | ------ |
| T      | 19     |
| C      | 2      |

So,

$$
C=
\begin{bmatrix}
19\\
2
\end{bmatrix}
$$

---

## Step 1: Find the inverse of the key matrix

For this key,

$$
K^{-1}=
\begin{bmatrix}
15&17\\
20&9
\end{bmatrix}
$$

*(In exams, this inverse is usually given, or you may be asked to find it separately.)*

---

## Step 2: Multiply

$$
P=K^{-1}C\pmod{26}
$$

$$
\begin{bmatrix}
15&17\\
20&9
\end{bmatrix}
\begin{bmatrix}
19\\
2
\end{bmatrix}
$$

First row:

$$
15(19)+17(2)=285+34=319
$$

Second row:

$$
20(19)+9(2)=380+18=398
$$

So,

$$
\begin{bmatrix}
319\\
398
\end{bmatrix}
$$

---

## Step 3: Take mod 26

$$
319\bmod26=7
$$

$$
398\bmod26=8
$$

So,

$$
P=
\begin{bmatrix}
7\\
8
\end{bmatrix}
$$

Convert back:

| Number | Letter |
| ------ | ------ |
| 7      | H      |
| 8      | I      |

Recovered plaintext:

```text
HI
```

---

# Final Answer

### Encryption

```text
Plaintext : HI
Key       : [3 3]
            [2 5]

Ciphertext: TC
```

### Decryption

```text
Ciphertext : TC
Inverse Key: [15 17]
             [20  9]

Plaintext  : HI
```

---

# ⭐ Exam Memory Trick

Just memorize this one complete example:

* **Key Matrix**

$$
\begin{bmatrix}
3&3\\
2&5
\end{bmatrix}
$$

* **Plaintext:** `HI`
* **Ciphertext:** `TC`
* **Inverse Matrix:**

$$
\begin{bmatrix}
15&17\\
20&9
\end{bmatrix}
$$

This is a standard textbook example and is short enough to write in an exam.

> **Note:** If your exam asks you to **find the inverse matrix yourself**, you'll also need to know the steps for computing the inverse modulo 26 (determinant, multiplicative inverse of the determinant, adjugate matrix, and modulo reduction).
