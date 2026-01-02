
# 📌 Bayes Rule in Classification

Let:

* $D$ be a **database**
* $C_1, C_2, ..., C_m$ be **$m$ classes**
* $X = (x_1, x_2, ..., x_n)$ be a **tuple (feature vector)**

We want to **predict which class $X$ belongs to**.

---

## 1️⃣ Posterior probability

Formula (Bayes’ Theorem):

$$
P(C_i|X) = \frac{P(X|C_i) \cdot P(C_i)}{P(X)}
$$

Where:

* $P(C_i|X)$ → Posterior probability of class $C_i$ given tuple $X$
* $P(X|C_i)$ → Likelihood of tuple $X$ given class $C_i$
* $P(C_i)$ → Prior probability of class $C_i$
* $P(X)$ → Evidence / total probability of $X$

---

## 2️⃣ Decision rule

**Goal:** assign $X$ to class with **highest posterior probability**.

Formula:
$$
\hat{C} = \arg\max_{C_i} P(C_i|X)
$$

---

## 3️⃣ Simplification

Since $P(X)$ is **constant for all classes**, we only need to **maximize numerator**:

Formula:
$$
\hat{C} = \arg\max_{C_i} P(X|C_i) \cdot P(C_i)
$$

> ✅ This is the standard **Naive Bayes decision rule**.

---

## 4️⃣ Naive assumption

If features are [conditionally independent given the class](conditionally%20independent%20given%20the%20class.md)

Formula:
$$
P(X|C_i) = \prod_{k=1}^{n} P(x_k | C_i)
$$

Then the classification formula becomes:

$$
\hat{C} = \arg\max_{C_i} P(C_i) \cdot \prod_{k=1}^{n} P(x_k | C_i)
$$

> This is **what we call the Naive Bayes classifier**.

---

## 5️⃣ Exam-style summary

**Given:** tuple $X$

**Step 1:** Compute prior $P(C_i)$ for each class

**Step 2:** Compute likelihood $P(x_k | C_i)$ for all features

**Step 3:** Multiply: $P(C_i) \cdot \prod P(x_k | C_i)$

**Step 4:** Choose class with maximum value

Formula:
$$
\hat{C} = \arg\max_{C_i} P(C_i) \cdot \prod_{k=1}^{n} P(x_k | C_i)
$$

---
---
---

# 📌 Naive Bayes Classification Example 

**Given database:**

| Student | Passed Exam | Study Hours |
| ------- | ----------- | ----------- |
| 1       | Yes         | High        |
| 2       | Yes         | High        |
| 3       | No          | Low         |
| 4       | No          | Low         |
| 5       | Yes         | Low         |

**Task:** Classify a new student $X = ($Passed Exam=?, Study Hours=High$)$

Classes: $C_1 = Yes$, $C_2 = No$

---

## Step 1️⃣ Compute prior probabilities

**Formula:**
$$
P(C_i) = \frac{\text{Number of tuples in class } C_i}{\text{Total number of tuples}}
$$

**Calculation:**

* $P(Yes) = \frac{3}{5} = 0.6$
* $P(No) = \frac{2}{5} = 0.4$

---

## Step 2️⃣ Compute likelihoods

**Formula:**
$$
P(\text{Study Hours High} \mid C_i) = \frac{\text{Number of tuples with Study Hours High in class } C_i}{\text{Total number of tuples in class } C_i}
$$

**Calculation:**

* $P(High \mid Yes) = \frac{2}{3} \approx 0.667$
* $P(High \mid No) = \frac{0}{2} = 0$

> ✅ Optional: Use **Laplace smoothing** if zero probabilities are not allowed.

---

## Step 3️⃣ Apply Naive Bayes formula

**Formula:**
$$
P(C_i \mid X) \propto P(C_i) \cdot \prod_{k=1}^{n} P(x_k \mid C_i)
$$

**Calculation:**

* For $C_1 = Yes$:
  $$
  P(Yes \mid X) = P(Yes) \cdot P(High \mid Yes)
  $$
  $$
  P(Yes \mid X) = 0.6 \cdot 0.667 \approx 0.4
  $$

* For $C_2 = No$:
  $$
  P(No \mid X) = P(No) \cdot P(High \mid No)
  $$
  $$
  P(No \mid X) = 0.4 \cdot 0 = 0
  $$

---

## Step 4️⃣ Make decision

**Formula:**
$$
\hat{C} = \arg\max_{C_i} P(C_i \mid X)
$$

**Calculation:**
$$
\hat{C} = Yes \quad (\text{because } 0.4 > 0)
$$

---

## ✅ Step 5️⃣ Interpretation

The classifier **predicts that the student will pass the exam**, because the posterior probability $P(Yes \mid X)$ is higher than $P(No \mid X)$.

---

### 💡 Exam Tips for Speed

1. Write **formula once** → saves time
2. Compute **priors and likelihoods in a small table** → fast
3. Multiply likelihoods × prior → compare
4. Box the **final class prediction** → clear for examiner

---

