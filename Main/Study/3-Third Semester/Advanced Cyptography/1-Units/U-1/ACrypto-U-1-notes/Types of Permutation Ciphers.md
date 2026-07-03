#advanced-cryptography #permutation-cipher 

---

# 1. Rail Fence Cipher

### Idea

Imagine writing a message in a **zig-zag (railway track) pattern**, then reading it row by row.

### Example

Plaintext:

```text
HELLO
```

Using **2 rails**:

```
Rail 1: H   L   O
Rail 2:  E L
```

Visual representation:

```
H   L   O
 E L
```

Now read the first rail:

```
HLO
```

Then read the second rail:

```
EL
```

Ciphertext:

```
HLOEL
```

### Memory Trick

**Rail Fence = Zig-zag writing.**

---

# 2. Columnar Transposition Cipher

### Idea

Instead of zig-zag, you write the plaintext **row by row in a table**.

Then you read the columns according to a **key**.

### Example

Plaintext:

```
HELLO
```

Key:

```
3 1 2
```

Write in rows (3 columns):

| 3 | 1 | 2 |
| - | - | - |
| H | E | L |
| L | O | X |

(X is added because one letter is missing.)

Now read according to the key:

* Key 1 → Column 2 → **EO**
* Key 2 → Column 3 → **LX**
* Key 3 → Column 1 → **HL**

Ciphertext:

```
EOLXHL
```

### Memory Trick

**Columnar = Table + Key.**

---

# 3. Double Transposition Cipher

### Idea

Do **Columnar Transposition twice**.

Example:

Plaintext:

```
HELLOWORLD
```

### First Transposition

↓

```
LRO...
```

(Produces some ciphertext.)

Now take that ciphertext and **apply another columnar transposition with the same or a different key**.

↓

Final ciphertext becomes even more scrambled.

### Memory Trick

**Double Transposition = Table twice.**

---

# Easy Comparison

| Cipher                     | What You Do                                     | Memory Trick    |
| -------------------------- | ----------------------------------------------- | --------------- |
| **Rail Fence**             | Write in a zig-zag pattern and read row by row. | **Zig-zag**     |
| **Columnar Transposition** | Write in a table and read columns using a key.  | **Table + Key** |
| **Double Transposition**   | Apply columnar transposition **two times**.     | **Table twice** |

---

# Super Easy Way to Remember

Imagine you have the word:

```
HELLO
```

### Rail Fence

```
Write like stairs (zig-zag)

H   L   O
 E L
```

↓

Read across

```
HLOEL
```

---

### Columnar

```
Put it in a table

H E L
L O X
```

↓

Read columns according to the key.

---

### Double Transposition

```
Table
↓
Ciphertext
↓
Put the ciphertext into another table
↓
Read columns again
```

---

## Exam Tip ⭐

Most cryptography exams **do not ask you to perform Rail Fence or Double Transposition encryption in detail**. They usually ask:

* Define Rail Fence Cipher.
* Explain Columnar Transposition with an example. ✅ (Most important)
* What is Double Transposition?

So if you're short on time, **focus mainly on Columnar Transposition**, as it is the most commonly tested permutation cipher.
