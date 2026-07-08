#third-semester #advanced-cryptography #one-time-pad

key is given as **BAXYC**, the easiest exam method is to use the **letter-to-number method** ($A=0$, $B=1$, ..., $Z=25$).

> **Note:** Some textbooks explain Vernam/OTP using **binary XOR**, while others use **$A=0$ to $Z=25$** for simple examples. Check your course notes. For exam practice, the letter-number method is often used.

---

# Example (HELLO with Key BAXYC)

### Step 1: Convert letters to numbers

| Plaintext | H | E | L  | L  | O  |
| --------- | - | - | -- | -- | -- |
| Value     | 7 | 4 | 11 | 11 | 14 |

| Key   | B | A | X  | Y  | C |
| ----- | - | - | -- | -- | - |
| Value | 1 | 0 | 23 | 24 | 2 |

---

### Step 2: Encrypt

Formula:

$$
C=(P+K)\bmod26
$$

| Plain ($P$) | Key ($K$) | Calculation        | Cipher Value | Cipher Letter |
| ----------- | --------- | ------------------ | ------------ | ------------- |
| 7           | 1         | $(7+1)\bmod26=8$   | 8            | I             |
| 4           | 0         | $(4+0)\bmod26=4$   | 4            | E             |
| 11          | 23        | $(11+23)\bmod26=8$ | 8            | I             |
| 11          | 24        | $(11+24)\bmod26=9$ | 9            | J             |
| 14          | 2         | $(14+2)\bmod26=16$ | 16           | Q             |

### Ciphertext

```text id="6sifhq"
IEIJQ
```

---

# Decryption

Formula:

$$
P=(C-K)\bmod26
$$

| Cipher | Key | Calculation        | Plain Value | Plain Letter |
| ------ | --- | ------------------ | ----------- | ------------ |
| I (8)  | 1   | $(8-1)\bmod26=7$   | 7           | H            |
| E (4)  | 0   | $(4-0)\bmod26=4$   | 4           | E            |
| I (8)  | 23  | $(8-23)\bmod26=11$ | 11          | L            |
| J (9)  | 24  | $(9-24)\bmod26=11$ | 11          | L            |
| Q (16) | 2   | $(16-2)\bmod26=14$ | 14          | O            |

Recovered plaintext:

```text id="9sp1x2"
HELLO
```

---

# Is this Vernam Cipher or One-Time Pad?

The **encryption and decryption steps are identical**.

* **Vernam Cipher:** If you reuse the key **BAXYC** for another message, it is a Vernam Cipher.
* **One-Time Pad:** If **BAXYC** is a **truly random key**, has the **same length as HELLO**, is **used only once**, and is **never reused**, then it is a One-Time Pad.

---

## Exam Tip

If your professor teaches **binary XOR**, then you should solve it using ASCII/binary instead of the $A=0$ to $Z=25$ method. If your notes use the **$A=0$ to $Z=25$** approach like above, then this is the format you should write in the exam.
