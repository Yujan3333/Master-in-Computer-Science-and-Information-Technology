#third-semester #advanced-cryptography 
# Example

### Plaintext

```text
ATTACKATDAWN
```

### Key

```text
3 1 4 2
```

---

# Step 1: Draw the table

Since the key has **4 numbers**, we need **4 columns**.

| Key | **3** | **1** | **4** | **2** |
| --- | ----- | ----- | ----- | ----- |
|     | A     | T     | T     | A     |
|     | C     | K     | A     | T     |
|     | D     | A     | W     | N     |

---

# Step 2: Find the Reading Order

We always read the columns according to **key values**:

### Key = 1

Where is **1**?

It is above **Column 2**.

Read Column 2:

```text
T
K
A
```

Result:

```text
TKA
```

---

### Key = 2

Where is **2**?

It is above **Column 4**.

Read Column 4:

```text
A
T
N
```

Result:

```text
ATN
```

---

### Key = 3

Where is **3**?

It is above **Column 1**.

Read Column 1:

```text
A
C
D
```

Result:

```text
ACD
```

---

### Key = 4

Where is **4**?

It is above **Column 3**.

Read Column 3:

```text
T
A
W
```

Result:

```text
TAW
```

---

# Step 3: Combine Everything

```text
TKA + ATN + ACD + TAW
```

Ciphertext:

```text
TKAATNACDTAW
```

---

# Final Encryption

```
Plaintext : ATTACKATDAWN

Key:
3 1 4 2

Table

3   1   4   2
--------------
A   T   T   A
C   K   A   T
D   A   W   N

Read Columns

Key 1 → Column 2 → TKA

Key 2 → Column 4 → ATN

Key 3 → Column 1 → ACD

Key 4 → Column 3 → TAW

Ciphertext = TKAATNACDTAW
```

---

# Decryption

Ciphertext:

```text
TKAATNACDTAW
```

Key:

```text
3 1 4 2
```

---

## Step 1

Count letters.

```
12 letters
```

There are **4 columns**.

So each column has

```
12 ÷ 4 = 3 letters
```

---

## Step 2

Remember the reading order during encryption:

```
Key 1 → Column 2
Key 2 → Column 4
Key 3 → Column 1
Key 4 → Column 3
```

Now split the ciphertext accordingly.

```
TKA | ATN | ACD | TAW
```

Assign them back to their columns.

| Key | Column   | Letters |
| --- | -------- | ------- |
| 1   | Column 2 | TKA     |
| 2   | Column 4 | ATN     |
| 3   | Column 1 | ACD     |
| 4   | Column 3 | TAW     |

Now the table becomes:

| 3 | 1 | 4 | 2 |
| - | - | - | - |
| A | T | T | A |
| C | K | A | T |
| D | A | W | N |

---

## Step 3

Read row by row.

```
A T T A
C K A T
D A W N
```

Plaintext:

```
ATTACKATDAWN
```

---

# Super Easy Memory Trick ⭐

### Encryption

```
Write row-wise
↓
Read column-wise
```

### Decryption

```
Fill column-wise
↓
Read row-wise
```

---

This is the **standard exam example** of a **Columnar Transposition (Permutation) Cipher**. It demonstrates both **encryption** and **decryption** clearly using the key **3 1 4 2**.
