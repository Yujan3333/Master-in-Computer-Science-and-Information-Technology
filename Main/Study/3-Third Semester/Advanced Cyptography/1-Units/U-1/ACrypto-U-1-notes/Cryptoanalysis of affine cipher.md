#advanced-cryptography #affine-cipher 


# Cryptanalysis of Affine Cipher (Detailed & Easy to Understand)

## 1. What is Cryptanalysis?

**Cryptanalysis** means **trying to break an encryption system** without knowing the secret key.

The goal is to find:

* The **secret key**, or
* The **original plaintext**.

---

## 2. Recall the Affine Cipher

The encryption formula is:

$$C=(aP+b)\bmod26$$

where:

* $P$ = Plaintext letter (A=0, B=1, ..., Z=25)
* $C$ = Ciphertext letter
* $a$ and $b$ are the secret keys
* $a$ must be coprime with 26

Example:

Suppose:

* $a=5$
* $b=8$

Then every plaintext letter is encrypted using the same formula.

---

# Why is the Affine Cipher Easy to Break?

There are **two main reasons**:

### 1. Very small number of keys

The key consists of:

* $a$
* $b$

But not every value of $a$ is allowed.

Valid values of $a$ are:

```text
1,3,5,7,9,11,15,17,19,21,23,25
```

There are only **12** choices.

For each $a$, there are **26** choices of $b$.

Therefore,

$$12\times26=312$$

Only **312 possible keys** exist.

Modern computers can try 312 keys almost instantly.

---

# Method 1: Brute Force Attack

Imagine someone intercepts this ciphertext:

```text
WTAAD
```

The attacker **doesn't know**:

* $a$
* $b$

Instead of solving the mathematics, they simply try every possible key.

For example:

Try

```text
a=1
b=0
```

Decrypt.

Result:

```text
WTAAD
```

Looks meaningless.

Next,

```text
a=1
b=1
```

Still meaningless.

Continue...

Eventually,

```text
a=5
b=8
```

Output becomes

```text
HELLO
```

Now the attacker knows:

* Plaintext = HELLO
* Key = $(5,8)$

Since there are only **312(12x26) possibilities**, brute force is very practical.

***Note***
- *a is coprime of 26 so only 12 values possible and b can 26 values*
- *a can be 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25*
- *b can 0 to 25*


---

# Method 2: Known-Plaintext Attack

Suppose the attacker somehow knows **part of the message**.

Example:

They know:

```text
Plaintext → Ciphertext

A → I
B → N
```

Convert letters into numbers:

```text
A = 0
B = 1

I = 8
N = 13
```

Using the Affine formula:

$$C=(aP+b)\bmod26$$

### First pair

$$8=(a\times0+b)\bmod26$$

Since anything multiplied by 0 is 0,

$$b=8$$

Now use the second pair.

$$13=(a\times1+8)\bmod26$$

So,

$$a=5$$

The attacker has recovered the complete key:

```text
a = 5
b = 8
```

Now every future message can be decrypted.

### Why only two letter pairs?

There are only **two unknowns**:

* $a$
* $b$

Two independent equations are enough to solve for them.

---

# Method 3: Frequency Analysis

This is the most interesting attack.

### Step 1

Suppose a very long ciphertext is intercepted.

```text
Q M L P Q X Q N Q ...
```

The attacker counts how often each letter appears.

Example:

```text
Q → 120 times
M → 60 times
L → 45 times
```

---

### Step 2

In English,

Some letters appear much more often than others.

Approximate frequency:

```text
E → Most common

T
A
O
I
N
```

If **Q** appears the most,

the attacker guesses:

```text
Q probably represents E
```

---

### Step 3

The attacker continues making guesses.

Example:

```text
Q → E

M → T

L → A
```

After enough guesses,

they calculate the values of $a$ and $b$.

Once the key is found,

the entire ciphertext becomes readable.

---

## Why does frequency analysis work?

Because the Affine cipher is a **monoalphabetic substitution cipher**.

That means:

Each plaintext letter **always** becomes the same ciphertext letter.

Example:

```text
E → Q
```

Every single E in the message becomes Q.

Example:

```text
HELLO

E becomes Q

TREE

E also becomes Q

SECRET

Both Es become Q
```

Since E is the most common English letter,

Q also becomes the most common ciphertext letter.

So the frequency pattern is preserved.

The letters change,

but **their frequencies do not**.

---

# Why Modern Ciphers Don't Have This Problem

Modern algorithms like the Advanced Encryption Standard produce ciphertext that looks random.

Example:

```text
Affine Cipher

HELLO
↓
RCLLA

Same letters always encrypt the same way.
```

But in AES,

the same plaintext can encrypt differently depending on the key and encryption mode, making frequency analysis ineffective.

---

# Summary Table

| Attack                     | How it Works                                                          | Why it Works                                                    |
| -------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Brute Force**            | Try all possible keys                                                 | Only **312** valid keys exist                                   |
| **Known-Plaintext Attack** | Use two known plaintext–ciphertext pairs to solve for $a$ and $b$     | Only two unknown keys need to be found                          |
| **Frequency Analysis**     | Compare ciphertext letter frequencies with English letter frequencies | Each plaintext letter always maps to the same ciphertext letter |

---

# Easy Way to Remember for Exams

**Affine cipher is weak because:**

* 🔹 **Small key space** → Only **312** keys → Easy brute-force attack.
* 🔹 **Two known plaintext–ciphertext pairs** are enough to calculate the key.
* 🔹 **Same plaintext letter always maps to the same ciphertext letter**, so **frequency analysis** can reveal the substitution.

These weaknesses make the Affine cipher unsuitable for modern secure communication.

