# 📌 Bayes’ Theorem

Bayes’ theorem is a **fundamental rule in probability** that allows you to **update the probability of an event** based on new evidence.

It is widely used in **machine learning, statistics, and decision making**.

---

## 1️⃣ Formula

### General formula:

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

Where:

* $P(A|B)$ → Posterior probability (probability of $A$ given $B$)
* $P(B|A)$ → Likelihood (probability of $B$ given $A$)
* $P(A)$ → Prior probability of $A$
* $P(B)$ → Total probability of $B$ (normalizing factor)

---

## 2️⃣ Total Probability (if needed)

If $B$ can happen under multiple mutually exclusive events $A_1, A_2, ..., A_n$:

Formula:
$$
P(B) = \sum_{i=1}^{n} P(B|A_i) \cdot P(A_i)
$$

This ensures **posterior probabilities sum to 1**.

---

## 3️⃣ How to use Bayes’ Theorem (Step by Step)

**Step 1:** Identify the prior $P(A)$
**Step 2:** Identify likelihood $P(B|A)$
**Step 3:** Compute total probability $P(B)$ if needed
**Step 4:** Apply the formula to get posterior $P(A|B)$

---

## 4️⃣ Example

**Problem:**

A test for a disease is **99% accurate**. Disease occurs in **1% of population**. What is the probability that a person has the disease if the test is positive?

---

### Step 1: Define events

* $D$: Person has disease
* $\bar{D}$: Person does not have disease
* $T$: Test is positive

Given:

* $P(D) = 0.01$
* $P(\bar{D}) = 0.99$
* $P(T|D) = 0.99$
* $P(T|\bar{D}) = 0.01$ (false positive rate)

---

### Step 2: Formula

$$
P(D|T) = \frac{P(T|D) \cdot P(D)}{P(T)}
$$

---

### Step 3: Compute $P(T)$ (total probability)

Formula:
$$
P(T) = P(T|D)\cdot P(D) + P(T|\bar{D}) \cdot P(\bar{D})
$$

Calculation:
$$
P(T) = 0.99 \cdot 0.01 + 0.01 \cdot 0.99
$$

$$
P(T) = 0.0099 + 0.0099 = 0.0198
$$

---

### Step 4: Compute posterior $P(D|T)$

Formula:
$$
P(D|T) = \frac{P(T|D) \cdot P(D)}{P(T)}
$$

Calculation:
$$
P(D|T) = \frac{0.99 \cdot 0.01}{0.0198} = \frac{0.0099}{0.0198} \approx 0.5
$$

---

### ✅ Step 5: Interpretation

Even though the test is **99% accurate**, the probability that a person actually has the disease **given a positive test is only 50%**.

> This happens because the disease is **rare**, so false positives dominate.

---

## 5️⃣ Key Points for Exams

1. **Always write formula first → then substitute numbers**
2. If multiple events contribute to $B$, **use total probability formula**
3. **Posterior probability** is what Bayes’ theorem computes
4. **Check units**: probabilities are between 0 and 1
5. Common ML application: **Naive Bayes classifier**

---

