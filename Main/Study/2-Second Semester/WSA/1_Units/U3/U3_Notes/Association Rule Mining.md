
## 🔹 What are Association Rules?

Association rules are used to **find relationships between items** in large datasets.

👉 In simple words:
**“If a customer buys X, they are likely to buy Y.”**

This technique is mainly used in **market basket analysis**.

---

## 🔹 Simple Example (Shopping Basket 🛒)

Transactions:

| Transaction | Items Bought        |
| ----------- | ------------------- |
| T1          | Bread, Milk         |
| T2          | Bread, Diaper, Beer |
| T3          | Milk, Diaper, Beer  |
| T4          | Bread, Milk, Diaper |

From this data, we may discover:

**Rule:**
If a customer buys **Diaper**, they also buy **Beer**

Written as:
Diaper → Beer

---

## 🔹 Key Terms (Very Important)

### 1️⃣ Support

Support shows **how often items appear together**.

$$
Support(X \rightarrow Y) = \frac{\text{Number of transactions containing } X \cup Y}{\text{Total transactions}}
$$

👉 Example:
If (Diaper, Beer) appear in **2 out of 4** transactions:

Support = 2 / 4 = 0.5

---

### 2️⃣ Confidence

Confidence shows **how often Y appears when X appears**.

$$
Confidence(X \rightarrow Y) = \frac{\text{Support}(X \cup Y)}{\text{Support}(X)}
$$

👉 Example:
If Diaper appears in 3 transactions and (Diaper, Beer) in 2:

Confidence = 2 / 3 ≈ 0.67

---

### 3️⃣ Lift

Lift shows **how strong the rule is**.

$$
Lift(X \rightarrow Y) = \frac{Confidence(X \rightarrow Y)}{Support(Y)}
$$

Interpretation:

* Lift > 1 → Positive association
* Lift = 1 → No association
* Lift < 1 → Negative association

---

## 🔹 How Association Rule Mining Works

1. Find **frequent itemsets** (items that appear together often)
2. Generate **rules** from these itemsets
3. Keep rules that satisfy:

   * Minimum Support
   * Minimum Confidence

---

## 🔹 Common Algorithms

* [Apriori Algorithm](Apriori%20Algorithm.md)
* [FP Growth](FP%20Growth.md)

(For exams: just naming is usually enough)

---

## 🔹 Applications

* Supermarket product placement
* Online recommendations (Amazon, Flipkart)
* Medical diagnosis
* Website click analysis

---

## 🔹 One-Line Exam Definition ✍️

> Association rule mining is a data mining technique used to discover interesting relationships and patterns among items in large datasets.

---
