#advanced-cryptography #third-semester 

# Autokey Cipher

The **Autokey Cipher** is a **polyalphabetic substitution cipher** that is an improvement over the **Vigenère Cipher**.

Instead of repeating the key again and again, the **Autokey Cipher extends the key using the plaintext itself**.

---

# Simple Definition (Exam)

> **An Autokey Cipher is a polyalphabetic substitution cipher in which the initial secret key is followed by the plaintext itself to generate a longer key.**

---

# How It Works

### Step 1

Choose a secret key.

Example:

```text id="2v0p5z"
Key = KING
```

---

### Step 2

Write the plaintext.

```text id="c0cc70"
HELLOWORLD
```

---

### Step 3

Extend the key using the plaintext.

Original key:

```text id="jcz70l"
KING
```

Remaining plaintext:

```text id="g3e88m"
HELLOWORLD
```

Use the plaintext after the key:

```text id="f50z5i"
KEY:

KINGHELLOW
```

Notice:

```text id="mnbgku"
Plaintext : HELLOWORLD
Key       : KINGHELLOW
```

The key is now the **same length** as the plaintext.

---

# Encryption Formula

Convert letters:

```text id="xw62zk"
A = 0
B = 1
...
Z = 25
```

Then,

$$
C=(P+K)\bmod26
$$

where:

* **$P$** = Plaintext value
* **$K$** = Key value
* **$C$** = Ciphertext value

---

# Simple Example

### Plaintext

```text id="hvtjfs"
HELLO
```

### Secret Key

```text id="3pxifq"
KEY
```

Extend the key:

```text id="t5ixp0"
KEYHE
```

Now convert to numbers.

| Letter | H | E | L  | L  | O  |
| ------ | - | - | -- | -- | -- |
| Plain  | 7 | 4 | 11 | 11 | 14 |

| Key   | K  | E | Y  | H | E |
| ----- | -- | - | -- | - | - |
| Value | 10 | 4 | 24 | 7 | 4 |

Encrypt:

| Plain | Key | Calculation   | Cipher |
| ----- | --- | ------------- | ------ |
| 7     | 10  | $(7+10)=17$   | R      |
| 4     | 4   | $(4+4)=8$     | I      |
| 11    | 24  | $35\bmod26=9$ | J      |
| 11    | 7   | $(11+7)=18$   | S      |
| 14    | 4   | $(14+4)=18$   | S      |

### Ciphertext

```text id="y6mn5l"
RIJSS
```

---

# Decryption

Formula:

$$
P=(C-K)\bmod26
$$

The important point is:

After recovering each plaintext letter, **it is added to the key** for decrypting the next letters.

---

# Advantages

* More secure than the Vigenère Cipher.
* The key is not repeated.
* Reduces repeated patterns in the ciphertext.

---

# Disadvantages

* If part of the plaintext becomes known, the rest of the key can be discovered.
* Not secure against modern cryptanalysis.

---

# Difference Between Vigenère and Autokey

| Vigenère Cipher          | Autokey Cipher                        |
| ------------------------ | ------------------------------------- |
| Repeats the key.         | Uses the plaintext to extend the key. |
| Example: `KEYKEYKEY`     | Example: `KEYHELLOW`                  |
| Repeated patterns occur. | Fewer repeated patterns.              |
| Less secure.             | More secure than Vigenère.            |

---

# Easy Memory Trick

### Vigenère

```text id="2mwb08"
KEYKEYKEYKEY
```

(repeat the key)

---

### Autokey

```text id="nv2knh"
KEYHELLOW...
```

(key + plaintext)

---

# Exam Definition (2 Marks)

> **An Autokey Cipher is a polyalphabetic substitution cipher in which a short secret key is followed by the plaintext itself to generate a key that is the same length as the plaintext. Encryption is performed using the Vigenère method with this extended key.**

---

# One-Line Memory Trick ⭐

> **Vigenère repeats the key. Autokey grows the key using the plaintext.**

This is the easiest way to remember the difference in exams.
