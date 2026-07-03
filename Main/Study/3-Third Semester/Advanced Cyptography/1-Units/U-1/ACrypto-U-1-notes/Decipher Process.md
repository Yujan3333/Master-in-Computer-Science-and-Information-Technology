#advanced-cryptography 
## Playfair Cipher Decryption

**Decryption** is the process of converting the **ciphertext** back into the **original plaintext** using the **same 5 × 5 key matrix** that was used for encryption. The receiver must know the secret key to decrypt the message correctly.

### Decryption Rules

Suppose the ciphertext is divided into pairs of letters (digraphs). For each pair, apply the following rules:

### 1. Same Row Rule

If both letters are in the **same row** of the key matrix:

* Replace each letter with the letter **immediately to its left**.
* If the letter is at the beginning of the row, wrap around to the **last letter** of the same row.

**Example:**

```
Row: T  A  N  G  O

Cipher Pair: A N
Plain Pair : T A
```

---

### 2. Same Column Rule

If both letters are in the **same column**:

* Replace each letter with the letter **immediately above** it.
* If the letter is at the top of the column, wrap around to the **bottom**.

**Example:**

```
Column:
T
D
F
M
U

Cipher Pair: D F
Plain Pair : T D
```

---

### 3. Rectangle Rule

If the two letters form the **corners of a rectangle**:

* Replace each letter with the letter in the **same row** but in the **other letter's column**.

**Example:**

```
T  A  N  G  O
D  W  B  C  E
F  H  I  K  L
M  P  Q  R  S
U  V  X  Y  Z
```

Cipher Pair: **A F**

* A → row 1, column 2
* F → row 3, column 1

After swapping columns:

* A becomes **T**
* F becomes **H**

Plain Pair = **TH**

---

## Example Decryption

### Key Matrix

| T | A | N | G | O |
| - | - | - | - | - |
| D | W | B | C | E |
| F | H | I | K | L |
| M | P | Q | R | S |
| U | V | X | Y | Z |

### Ciphertext

```
AFDBOPLQEGQFGO
```

Split into pairs:

```
AF DB OP LQ EG QF GO
```

Decrypt each pair:

| Cipher Pair | Plain Pair |
| ----------- | ---------- |
| AF          | TH         |
| DB          | EW         |
| OP          | AS         |
| LQ          | IS         |
| EG          | CO         |
| QF          | MI         |
| GO          | NG         |

Combine the pairs:

```
TH EW AS IS CO MI NG
```

Remove the spaces:

```
THEWASISCOMING
```

Final plaintext:

**THE WAS IS COMING**

### Summary

* **Same Row:** Move **left**.
* **Same Column:** Move **up**.
* **Rectangle:** Swap the columns of the two letters.
* Use the **same key matrix** that was used for encryption.

These are the exact reverse operations of Playfair encryption.
