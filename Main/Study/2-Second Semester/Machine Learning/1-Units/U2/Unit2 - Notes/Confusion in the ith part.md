
## The expression

$$
y_i - a_0 - a_1 x_i
$$

represents the **error for the *i-th training example***.

---

## Why $x_i$ and not $x_1$?

### 1️⃣ Meaning of the subscript $i$

* $i$ is an **index** that runs over the dataset
* $i = 1, 2, 3, \dots, n$

So:

* $x_1$ → input of **1st data point**
* $x_2$ → input of **2nd data point**
* …
* $x_i$ → input of the **i-th data point**

---

## Dataset view

Suppose your data is:

| Index | $x$   | $y$   |
| ----- | ----- | ----- |
| 1     | $x_1$ | $y_1$ |
| 2     | $x_2$ | $y_2$ |
| 3     | $x_3$ | $y_3$ |
| $i$   | $x_i$ | $y_i$ |

When computing the cost function, we must compute **error for every data point**, not just the first one.

That’s why we write:

$$
\sum_{i=1}^n (y_i - \hat y_i)^2
$$

---

## Model prediction

The model is:

$$
\hat y_i = a_0 + a_1 x_i
$$

This means:

* For **each data point**, plug in its own $x_i$
* Compare prediction with its own $y_i$

Hence the error term:

$$
(y_i - a_0 - a_1 x_i)
$$

---

## What if we used $x_1$?

If we wrote:

$$
y_i - a_0 - a_1 x_1
$$

that would mean:

* Using the **same input $x_1$** for **all data points**
* Which makes no sense mathematically or logically

---

## Important clarification

This is **NOT** multivariable regression.

* $x_i$ ≠ $x_1, x_2$ as features
* Here:

  * Subscript = **data index**
  * Not feature number

---

## If there were multiple features

Then we would write:

$$
\hat y_i = a_0 + a_1 x_{i1} + a_2 x_{i2}
$$

* $x_{i1}$ → feature 1 of data point $i$
* $x_{i2}$ → feature 2 of data point $i$

---

## One-line exam-safe answer

> $x_i$ represents the input value of the i-th training example, and the cost function sums the error over all training samples.

