#advanced-cryptography #one-time-pad 


## Plaintext

```text
HELLO
```

## Key

```text
BAXYC
```

---

# Step 1: Convert to ASCII

| Letter | ASCII Decimal | Binary (8-bit) |
| ------ | ------------- | -------------- |
| H      | 72            | 01001000       |
| E      | 69            | 01000101       |
| L      | 76            | 01001100       |
| L      | 76            | 01001100       |
| O      | 79            | 01001111       |

### Key

| Letter | ASCII Decimal | Binary (8-bit) |
| ------ | ------------- | -------------- |
| B      | 66            | 01000010       |
| A      | 65            | 01000001       |
| X      | 88            | 01011000       |
| Y      | 89            | 01011001       |
| C      | 67            | 01000011       |

---

# Step 2: XOR Each Character

Remember the XOR rules:

| A | B | A ⊕ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

---

### Character 1

```
H = 01001000
B = 01000010
---------------- XOR
    00001010
```

Decimal = **10**

---

### Character 2

```
E = 01000101
A = 01000001
---------------- XOR
    00000100
```

Decimal = **4**

---

### Character 3

```
L = 01001100
X = 01011000
---------------- XOR
    00010100
```

Decimal = **20**

---

### Character 4

```
L = 01001100
Y = 01011001
---------------- XOR
    00010101
```

Decimal = **21**

---

### Character 5

```
O = 01001111
C = 01000011
---------------- XOR
    00001100
```

Decimal = **12**

---

# Ciphertext (Binary)

```
00001010
00000100
00010100
00010101
00001100
```

These bytes are the ciphertext. They may not correspond to printable letters, and that's perfectly normal when using XOR.

---

# Decryption

The best thing about XOR is:

$$[
P \oplus K = C
]
$$
and

$$[
C \oplus K = P
]$$

For example, take the first byte:

```
Cipher = 00001010
Key    = 01000010
---------------- XOR
Plain  = 01001000
```

```
01001000 = H
```

You repeat the same process for the remaining bytes to recover **HELLO**.

---

# Exam Trick ⭐

Most university exams **do not require you to convert letters to 8-bit ASCII by hand** unless the question specifically says:

* "Use ASCII"
* "Use binary"
* "Use XOR"

Usually, the question provides binary values such as:

```
Plaintext : 10101100
Key       : 11001010
```

Then you simply XOR them:

```
10101100
11001010
---------
01100110
```

So **check your past exam papers or lecture notes**. If they always use **binary**, practice XOR like this. If they use **A=0 to Z=25**, then use the modular arithmetic method instead.
