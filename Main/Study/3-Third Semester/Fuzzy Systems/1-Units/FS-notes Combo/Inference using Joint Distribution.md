#fuzzy-system #third-semester 

## Step 1: We have the Joint Probability Distribution

| Cavity | Toothache | Probability |
| ------ | --------- | ----------: |
| True   | True      |        0.30 |
| True   | False     |        0.20 |
| False  | True      |        0.10 |
| False  | False     |        0.40 |

Each row is one **atomic event**.



---

## Step 2: What does "Cavity OR Toothache" mean?

It means:

* Has a cavity ✅
  **OR**
* Has a toothache ✅
  **OR**
* Has both ✅

The **only case that does NOT satisfy "OR"** is:

* No cavity ❌
* No toothache ❌

Let's mark them.

| Cavity | Toothache | Probability | Include? |
| ------ | --------- | ----------: | :------: |
| True   | True      |        0.30 |     ✅    |
| True   | False     |        0.20 |     ✅    |
| False  | True      |        0.10 |     ✅    |
| False  | False     |        0.40 |     ❌    |

---

## Step 3: Add the probabilities

Since the first three rows satisfy **"Cavity OR Toothache"**, add them:

$$
0.30+0.20+0.10=0.60
$$

Therefore,

$$
P(\text{Cavity OR Toothache})=0.60
$$

---

## Why are we adding?

Because each row is a **different atomic event**.

The event "Cavity OR Toothache" consists of **three atomic events**:

1. (True, True)
2. (True, False)
3. (False, True)

So,

$$
P(\text{Cavity OR Toothache})
=============================

P(T,T)+P(T,F)+P(F,T)
$$

This is exactly what your notes mean by:

> **The probability of a proposition is equal to the sum of the probabilities of the atomic events in which it holds.** 

---

## Think of it like a classroom

Suppose there are four students.

| Student | Plays Football | Plays Cricket | Probability |
| ------- | -------------- | ------------- | ----------: |
| A       | Yes            | Yes           |        0.30 |
| B       | Yes            | No            |        0.20 |
| C       | No             | Yes           |        0.10 |
| D       | No             | No            |        0.40 |

Now ask:

> **What is the probability that a student plays Football OR Cricket?**

Who qualifies?

* A ✅
* B ✅
* C ✅
* D ❌

So,

$$
0.30+0.20+0.10=0.60
$$

---

## One-line idea to remember

**Inference using a joint distribution** means:

> **Find the rows (atomic events) that satisfy the condition, then add their probabilities.**

This is exactly how the notes compute probabilities such as (P(\text{Cavity or Toothache})) from the joint probability distribution. 
