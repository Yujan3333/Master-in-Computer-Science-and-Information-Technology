## Coprime (Relatively Prime)

**Coprime** (also called **relatively prime**) means:

> **Two numbers are coprime if their greatest common divisor (GCD or HCF) is 1.**

In simple words:

* They **do not share any common factor except 1**.

---

## Examples

### Example 1: 5 and 12

Factors of **5**:

```text
1, 5
```

Factors of **12**:

```text
1, 2, 3, 4, 6, 12
```

Common factor:

```text
1
```

Since the only common factor is **1**, **5 and 12 are coprime**.

---

### Example 2: 8 and 15

Factors of **8**:

```text
1, 2, 4, 8
```

Factors of **15**:

```text
1, 3, 5, 15
```

Common factor:

```text
1
```

✅ They are **coprime**.

---

### Example 3: 6 and 9

Factors of **6**:

```text
1, 2, 3, 6
```

Factors of **9**:

```text
1, 3, 9
```

Common factors:

```text
1, 3
```

Since they share **3**, they are **NOT coprime**.

---

## Easy Way to Check

Find the **GCD (Greatest Common Divisor)**.

* GCD = 1 → ✅ Coprime
* GCD > 1 → ❌ Not coprime

Examples:

| Numbers   | GCD | Coprime? |
| --------- | :-: | :------: |
| 7 and 20  |  1  |   ✅ Yes  |
| 9 and 28  |  1  |   ✅ Yes  |
| 12 and 18 |  6  |   ❌ No   |
| 15 and 25 |  5  |   ❌ No   |

---

## Why is Coprime Important in Cryptography?

In the **Affine Cipher**, the encryption formula is:

$$C=(aP+b)\bmod26$$

The value **$a$** **must be coprime with 26**.

Why?

Because during decryption, we need to find the **multiplicative inverse** of $a$ modulo 26. This inverse exists **only if $a$ and 26 are coprime**.

### Example

Is **5** allowed?

* $\gcd(5,26)=1$ ✅
* So **5 is allowed**.

Is **13** allowed?

* $\gcd(13,26)=13$ ❌
* So **13 is NOT allowed**.

---

## Valid Values of $a$ in the Affine Cipher

These are the numbers between 1 and 25 that are coprime with 26:

```text
1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
```

These are the **only valid choices** for $a$.

---

## Exam Definition (2 Marks)

> **Two integers are called coprime (or relatively prime) if their greatest common divisor (GCD) is 1, meaning they have no common factor other than 1.**

---

## Easy Memory Trick

* **Co** = together
* **Prime** = only share **1**

So think:

> **"Coprime = The only common factor is 1."**
