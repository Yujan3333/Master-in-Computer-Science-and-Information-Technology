#advanced-cryptography #third-semester #perfect-secrecy

# Step 0: What is the question asking?

The question asks whether the cryptosystem satisfies **perfect secrecy**.

We know that perfect secrecy means

$$
P(P=p\mid C=c)=P(P=p)
$$

This says:

> After seeing the ciphertext, my belief about the plaintext **should not change**.

So our job is:

1. Find the probability of each ciphertext.
2. Find the probability of the plaintext after seeing a ciphertext.
3. Compare it with the original probability.

If they are equal → Perfect secrecy.

If they are different → Not perfect secrecy.

---

# Step 1: Understand the Encryption Table

Given

| Key   | a | b |
| ----- | - | - |
| $K_1$ | 1 | 2 |
| $K_2$ | 2 | 3 |
| $K_3$ | 3 | 4 |

This tells us:

Using key $K_1$

$$
a\rightarrow1
$$

$$
b\rightarrow2
$$

Using key $K_2$

$$
a\rightarrow2
$$

$$
b\rightarrow3
$$

Using key $K_3$

$$
a\rightarrow3
$$

$$
b\rightarrow4
$$

This table tells us **which plaintext-key pair produces which ciphertext.**

---

# Step 2: Why compute ciphertext probabilities?

To calculate

$$
P(P=p\mid C=c)
$$

we must use Bayes' theorem.

Bayes' theorem is

$$
P(P=p\mid C=c)
==============

\frac{P(C=c\mid P=p),P(P=p)}
{P(C=c)}
$$

Notice the denominator.

We **cannot** calculate anything until we know

$$
P(C=c).
$$

That is why the **first step is finding the probability of every ciphertext.**

---

# Step 3: Find Probability of Ciphertext 1

Ask:

> Which combinations produce ciphertext 1?

Look at the table.

| Plaintext | Key      | Ciphertext |
| --------- | -------- | ---------- |
| a         | $K_1$    | 1 ✅        |
| b         | anything | never      |

Only one possibility.

So

$$
P(C=1)
======

P(a)\times P(K_1)
$$

Why multiply?

Because

* choosing plaintext
* choosing key

are **independent events**.

Independent events use multiplication.

Substitute values.

$$
P(C=1)
======

\frac14\times\frac12
$$

$$
=\frac18
$$

So ciphertext 1 appears with probability

$$
\boxed{\frac18}
$$

---

# Step 4: Find Probability of Ciphertext 2

Now ask

> Which combinations produce ciphertext 2?

From the table

| Plaintext | Key   |
| --------- | ----- |
| a         | $K_2$ |
| b         | $K_1$ |

There are **two ways** to obtain ciphertext 2.

First way

$$
P(a)P(K_2)
==========

 \frac14\times\frac14

\frac1{16}
$$

Second way

$$
P(b)P(K_1)
==========

 \frac34\times\frac12

\frac38
$$

Since **either event** can happen,

we **add** the probabilities.

$$
P(C=2)
======

\frac1{16}
+
\frac38
$$

Convert to a common denominator.

# $$

\frac1{16}
+
\frac6{16}
$$

# $$

\frac7{16}
$$

### Why add?

Remember:

* AND → Multiply
* OR → Add

Ciphertext 2 comes from

* this pair **OR**
* that pair.

So we add.

---

# Step 5: Ciphertext 3

Again ask

> Which pairs produce ciphertext 3?

From the table

| Plaintext | Key   |
| --------- | ----- |
| a         | $K_3$ |
| b         | $K_2$ |

First probability

$$
\frac14\times\frac14
====================

\frac1{16}
$$

Second

$$
\frac34\times\frac14
====================

\frac3{16}
$$

Add

$$
P(C=3)
======

\frac1{16}
+
\frac3{16}
==========

\frac14
$$

---

# Step 6: Ciphertext 4

Only one pair.

| Plaintext | Key   |
| --------- | ----- |
| b         | $K_3$ |

Therefore

$$
P(C=4)
=

 \frac34\times\frac14
=
\frac3{16}
$$

---

# Step 7: Now Why Bayes' Theorem?

Now we know all ciphertext probabilities.

The question asks

> After seeing ciphertext 1, what is the probability that the plaintext was "a"?

That is exactly

$$
P(a\mid C=1)
$$

This is **conditional probability**, so we use Bayes' theorem.

---

# Step 8: Apply Bayes

Bayes says

$$
P(a\mid C=1)
============

\frac{P(C=1\mid a)P(a)}
{P(C=1)}
$$

Let's understand each part.

---

## Numerator

First,

$$
P(C=1\mid a)
$$

means

> If we already know the plaintext is "a", what is the chance that ciphertext 1 is produced?

Look at the table.

If plaintext is

$$
a
$$

possible encryptions are

| Key   | Ciphertext |
| ----- | ---------- |
| $K_1$ | 1          |
| $K_2$ | 2          |
| $K_3$ | 3          |

Only

$$
K_1
$$

produces ciphertext 1.

Probability of choosing

$$
K_1
$$

is

$$
\frac12
$$

Therefore

$$
P(C=1\mid a)=\frac12
$$

---

Multiply by

$$
P(a)
====

\frac14
$$

Numerator becomes

$$
\frac12\times\frac14
====================

\frac18
$$

---

## Denominator

Earlier we already calculated

$$
P(C=1)=\frac18
$$

---

# Step 9: Divide

Now substitute everything.

$$
P(a\mid C=1)
============

 \frac{\frac18}{\frac18}

1
$$

Meaning

> If ciphertext 1 is observed, we are **100% certain** the plaintext was "a".

---

# Step 10: Compare

Originally,

before seeing ciphertext,

$$
P(a)=\frac14
$$

After seeing ciphertext,

$$
P(a\mid C=1)=1
$$

These are **not equal**.

Perfect secrecy requires

$$
P(a\mid C=1)=P(a).
$$

But

$$
1\ne\frac14.
$$

Therefore,

the ciphertext **revealed information** about the plaintext.

---

# Step 11: Final Conclusion

Since

$$
P(a\mid C=1)\ne P(a),
$$

the cryptosystem **does not satisfy perfect secrecy**.

---

# The Logic Behind the Whole Solution

```text
Question asks:
Does ciphertext reveal information?

        │
        ▼

Need conditional probability

        │
        ▼

Conditional probability requires Bayes' theorem

        │
        ▼

Bayes' theorem requires P(C)

        │
        ▼

Compute every ciphertext probability

        │
        ▼

Apply Bayes

        │
        ▼

Compare

P(Plaintext)

with

P(Plaintext | Ciphertext)

        │
        ▼

Equal?
 │
 ├── Yes → Perfect Secrecy
 │
 └── No → Not Perfect Secrecy
```

This is the reasoning expected in exams: first compute the ciphertext probabilities, then use Bayes' theorem to find the conditional probability, and finally compare it with the original plaintext probability to determine whether perfect secrecy holds.
