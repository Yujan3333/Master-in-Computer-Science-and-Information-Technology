#fuzzy-system #third-semester 

# First, what does "Marginalization" mean?

The word **marginalization** simply means:

> **Ignore (remove) the variable you don't care about by adding its probabilities.**

That's why it is also called **Summing Out**.

---

# Example

Suppose we have two variables:

* Cavity (True/False)
* Weather (Sunny/Rainy)

Their joint probability distribution is

| Weather | Cavity | Joint Probability |
| ------- | ------ | ----------------: |
| Sunny   | True   |              0.30 |
| Sunny   | False  |              0.20 |
| Rainy   | True   |              0.10 |
| Rainy   | False  |              0.40 |

---

## Suppose the question asks

> **What is the probability of having a cavity?**

Notice something...

The question **doesn't mention weather.**

So we **don't care** whether it is Sunny or Rainy.

We only care about

> Cavity = True

---

## Step 1: Find all rows where Cavity=True

| Weather | Cavity | Probability |
| ------- | ------ | ----------: |
| Sunny   | True   |        0.30 |
| Rainy   | True   |        0.10 |

These are the only rows where the person has a cavity.

---

## Step 2: Add them

$$
P(\text{Cavity=True})
=====================

 0.30+0.10

0.40
$$

Done!

We **summed out Weather** because it wasn't asked.

---

# Why do we add?

Imagine 100 people.

| Weather | Cavity | People |
| ------- | ------ | -----: |
| Sunny   | Yes    |     30 |
| Sunny   | No     |     20 |
| Rainy   | Yes    |     10 |
| Rainy   | No     |     40 |

Now someone asks

> **How many people have a cavity?**

Would you answer

> 30

No!

Because there are also **10 people with a cavity when it's rainy**.

So

$$
30+10=40
$$

You ignored the weather because it wasn't important.

This is **marginalization**.

---

# Why is it called "Summing Out"?

Because you're literally **summing away** the unwanted variable.

You started with

```text
Weather + Cavity
```

After adding,

```text
Only Cavity remains
```

The Weather variable has disappeared.

---

# Understanding the Formula

Your notes give the formula 

$$
P(Y)=\sum P(Y,Z)
$$

Let's understand each part.

* $$Y$$ = the variable you **want**
* $$Z$$ = the variable you **don't care about**

So

$$
P(Y)
====

\sum P(Y,Z)
$$

means

> To find the probability of **Y**, add the joint probabilities for **all possible values of Z**.

---

## Apply it to the example

Suppose

* $$Y=\text{Cavity}$$
* $$Z=\text{Weather}$$

Then

$$
P(\text{Cavity})
================

\sum_{\text{Weather}}
P(\text{Cavity},\text{Weather})
$$

Expanding the summation gives

$$
P(\text{Cavity})
================

P(\text{Cavity},\text{Sunny})
+
P(\text{Cavity},\text{Rainy})
$$

Substitute the values:

$$
P(\text{Cavity})
================

 0.30+0.10

0.40
$$

---

# Visual Trick

Start with the full table.

| Weather | Cavity | Probability |
| ------- | ------ | ----------: |
| Sunny   | True   |  **0.30** ✅ |
| Sunny   | False  |        0.20 |
| Rainy   | True   |  **0.10** ✅ |
| Rainy   | False  |        0.40 |

Question:

> **Find $$P(\text{Cavity=True})$$**

Ignore Weather.

Only look for

```text
Cavity = True
```

Then add

```text
0.30
+
0.10
```

Result

$$
P(\text{Cavity=True})=0.40
$$

---

# One-line Exam Definition

**Marginalization (Summing Out):**
Marginalization is the process of obtaining the probability of one variable by **adding the joint probabilities over all possible values of the other (unwanted) variables**. 

## Memory Trick

Think of the question:

> **What do I want?**

* If the question asks for **Cavity**, **ignore everything else** and **add all rows where Cavity has the required value**.
* If the question asks for **Weather**, ignore Cavity and add all rows with the required weather.

**Marginalization = Ignore the unwanted variable by adding its probabilities.**
