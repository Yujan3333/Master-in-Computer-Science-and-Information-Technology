# Question
![](../../../../../../../Images/Second_Sem_Images/Numerical%20of%20Bayes%20Theorem-que.png)

Predict class label of the tuple: X = (age = youth, income = medium, student = yes, credit_rating = fair) using Bayesian classification.

---
# 📌 Bayesian Classification - Answer

## Given

Tuple to be classified:

$X = (\text{age=youth},\ \text{income=medium},\ \text{student=yes},\ \text{credit=fair})$

Class attribute:
$C \in {\text{yes},\ \text{no}}$ where
*yes* = buys computer, *no* = does not buy computer

Total tuples: $14$

---

## Step 1️⃣ Compute prior probabilities

### Formula

$$
P(C_i) = \frac{\text{Number of tuples in class } C_i}{\text{Total number of tuples}}
$$

### Calculation

Number of **yes** = $9$
Number of **no** = $5$

$$
P(yes) = \frac{9}{14}
$$

$$
P(no) = \frac{5}{14}
$$

---

## Step 2️⃣ Compute likelihoods (conditional probabilities)

We assume **conditional independence** of attributes.

---

### 🔹 Attribute: age = youth

#### Formula

$$
P(\text{age=youth} \mid C_i) =
\frac{\text{Number of tuples with age=youth in } C_i}
{\text{Total tuples in } C_i}
$$

#### Calculation

* In class **yes**: youth = $2$
  $$
  P(\text{age=youth} \mid yes) = \frac{2}{9}
  $$

* In class **no**: youth = $3$
  $$
  P(\text{age=youth} \mid no) = \frac{3}{5}
  $$

---

### 🔹 Attribute: income = medium

#### Formula

$$
P(\text{income=medium} \mid C_i) =
\frac{\text{Number of tuples with income=medium in } C_i}
{\text{Total tuples in } C_i}
$$

#### Calculation

* In class **yes**: medium = $4$
  $$
  P(\text{income=medium} \mid yes) = \frac{4}{9}
  $$

* In class **no**: medium = $2$
  $$
  P(\text{income=medium} \mid no) = \frac{2}{5}
  $$

---

### 🔹 Attribute: student = yes

#### Formula

$$
P(\text{student=yes} \mid C_i) =
\frac{\text{Number of tuples with student=yes in } C_i}
{\text{Total tuples in } C_i}
$$

#### Calculation

* In class **yes**: student=yes = $6$
  $$
  P(\text{student=yes} \mid yes) = \frac{6}{9}
  $$

* In class **no**: student=yes = $1$
  $$
  P(\text{student=yes} \mid no) = \frac{1}{5}
  $$

---

### 🔹 Attribute: credit_rating = fair

#### Formula

$$
P(\text{credit=fair} \mid C_i) =
\frac{\text{Number of tuples with credit=fair in } C_i}
{\text{Total tuples in } C_i}
$$

#### Calculation

* In class **yes**: fair = $6$
  $$
  P(\text{credit=fair} \mid yes) = \frac{6}{9}
  $$

* In class **no**: fair = $2$
  $$
  P(\text{credit=fair} \mid no) = \frac{2}{5}
  $$

---

## Step 3️⃣ Apply Naive Bayes classifier

### Formula

$$
P(C_i \mid X) \propto P(C_i)
\prod P(x_k \mid C_i)
$$

---

### 🔹 For class = yes

#### Formula

$$
P(yes \mid X) \propto P(yes)
\cdot P(youth \mid yes)
\cdot P(medium \mid yes)
\cdot P(student=yes \mid yes)
\cdot P(fair \mid yes)
$$

#### Calculation

$$
P(yes \mid X) \propto
\frac{9}{14} \cdot
\frac{2}{9} \cdot
\frac{4}{9} \cdot
\frac{6}{9} \cdot
\frac{6}{9}
$$

$$
P(yes \mid X) \approx 0.028
$$

---

### 🔹 For class = no

#### Formula

$$
P(no \mid X) \propto P(no)
\cdot P(youth \mid no)
\cdot P(medium \mid no)
\cdot P(student=yes \mid no)
\cdot P(fair \mid no)
$$

#### Calculation

$$
P(no \mid X) \propto
\frac{5}{14} \cdot
\frac{3}{5} \cdot
\frac{2}{5} \cdot
\frac{1}{5} \cdot
\frac{2}{5}
$$

$$
P(no \mid X) \approx 0.007
$$

---

## Step 4️⃣ Final decision

### Formula

$$
\hat{C} = \arg\max_{C_i} P(C_i \mid X)
$$

### Comparison

$$
P(yes \mid X) > P(no \mid X)
$$

---

## ✅ Final Answer (write clearly in exam)

**The predicted class label for tuple $X$ is:**

$$
\boxed{\text{buys\_computer = yes}}
$$

---

## Examiner-friendly concluding line

Using Bayesian classification with conditional independence assumption, the tuple $X$ is classified as **yes**, since it has a higher posterior probability than class **no**.

---
---
