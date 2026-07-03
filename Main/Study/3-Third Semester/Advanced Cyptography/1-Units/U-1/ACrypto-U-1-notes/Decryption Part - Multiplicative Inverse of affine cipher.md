#affine-cipher #advanced-cryptography 

# Multiplicative Inverse

1  ↔ 1
3  ↔ 9
5  ↔ 21
7  ↔ 15
11 ↔ 19
17 ↔ 23
25 ↔ 25

| (a) | Multiplicative Inverse (a^{-1}) | Check                    |
| --: | ------------------------------: | ------------------------ |
|   1 |                               1 | 1 × 1 = 1 mod 26         |
|   3 |                               9 | 3 × 9 = 27 ≡ 1 mod 26    |
|   5 |                              21 | 5 × 21 = 105 ≡ 1 mod 26  |
|   7 |                              15 | 7 × 15 = 105 ≡ 1 mod 26  |
|   9 |                               3 | 9 × 3 = 27 ≡ 1 mod 26    |
|  11 |                              19 | 11 × 19 = 209 ≡ 1 mod 26 |
|  15 |                               7 | 15 × 7 = 105 ≡ 1 mod 26  |
|  17 |                              23 | 17 × 23 = 391 ≡ 1 mod 26 |
|  19 |                              11 | 19 × 11 = 209 ≡ 1 mod 26 |
|  21 |                               5 | 21 × 5 = 105 ≡ 1 mod 26  |
|  23 |                              17 | 23 × 17 = 391 ≡ 1 mod 26 |
|  25 |                              25 | 25 × 25 = 625 ≡ 1 mod 26 |


## First, think about normal math

Suppose:

$$5x=20$$

How do you find $x$?

You divide by 5.

$$x=\frac{20}{5}=4$$

Easy, right?

---

## But in modular arithmetic...

Suppose we have:

$$5x\equiv20\pmod{26}$$

**You cannot divide by 5 in modulo arithmetic.**

Instead, you need a number that **"acts like dividing by 5."**

That number is called the **multiplicative inverse**.

---

## What is the Multiplicative Inverse?

It is a number that, when multiplied by 5, gives **1 modulo 26**.

In other words, we want:

$$5\times?\equiv1\pmod{26}$$

Let's try numbers:

| Number | $5\times\text{Number}$ |  Mod 26 |
| :----: | :--------------------: | :-----: |
|    1   |            5           |    5    |
|    2   |           10           |    10   |
|    3   |           15           |    15   |
|    4   |           20           |    20   |
|    5   |           25           |    25   |
|   ...  |           ...          |   ...   |
| **21** |         **105**        | **1** ✅ |

Why?

$$105=26\times4+1$$

So,

$$105\bmod26=1$$

Therefore,

$$5^{-1}=21\pmod{26}$$

---

## Why is this Useful?

Suppose you have:

$$5P\equiv9\pmod{26}$$

Normally, you'd divide by 5.

Instead, multiply **both sides by 21** (the inverse of 5):

$$21\times5P\equiv21\times9\pmod{26}$$

Since

$$21\times5\equiv1\pmod{26},$$

this becomes:

$$P\equiv189\pmod{26}$$

Now reduce modulo 26:

$$189\bmod26=7$$

So,

$$P=7$$

Notice how multiplying by the inverse **cancels out** the 5, just like dividing by 5 does in normal arithmetic.

---

## Think of it Like This

### Normal Arithmetic

```text
×5  →  ÷5
```

Example:

```text
4 × 5 = 20

20 ÷ 5 = 4
```

---

### Modular Arithmetic

```text
×5  →  ×21
```

Because **21 is the multiplicative inverse of 5 modulo 26**.

---

## Memory Trick

**Normal math:**

> Multiply → Divide

**Modular math:**

> Multiply → Multiply by the inverse

---

## One Important Rule

A number has a multiplicative inverse modulo 26 **only if it is coprime with 26**.

For example:

* 5 → ✅ Has an inverse (21)
* 7 → ✅ Has an inverse (15)
* 13 → ❌ No inverse, because $\gcd(13,26)=13$

That's why in the **Affine Cipher**, the key $a$ **must be coprime with 26**.

---

## Exam Definition (2 Marks)

> **A multiplicative inverse of a number $a$ modulo 26 is another number $a^{-1}$ such that $$a\times a^{-1}\equiv1\pmod{26}$$ It is used in Affine Cipher decryption because division is not possible in modular arithmetic.**

---

## Easy Memory Trick

> **Normal Arithmetic:** Multiply → Divide

> **Modular Arithmetic:** Multiply → Multiply by the Inverse

Remember:

> **The multiplicative inverse replaces division in modular arithmetic.**
