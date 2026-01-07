# **Apriori Algorithm**

### **What is Apriori?**

Apriori is an algorithm used to **find frequent itemsets** in a transaction database and is the foundation for **association rule mining**.

---

## **Main Idea (Apriori Property)**

> **All non-empty subsets of a frequent itemset must also be frequent.**

📌 If an itemset is **infrequent**, all its **supersets are also infrequent**.

This helps in **pruning** (removing unnecessary candidates).

### [Apriori - Numerical Example](Apriori%20-%20Numerical%20Example.md)
---

# **Steps of Apriori Algorithm**

---

## **1️⃣ Generate Frequent 1-Itemsets**

* Scan the transaction database.
* Count support of each item.
* Remove items whose support < minimum support.
* Remaining items are **frequent 1-itemsets (L1)**.

---

## **2️⃣ Generate Candidate (k+1)-Itemsets**

* Use frequent k-itemsets (**Lk**) to generate candidate (k+1)-itemsets (**Ck+1**).
* This is done by **joining** itemsets with common items.

📌 Example:

```
{A, B} and {A, C} → {A, B, C}
```

---

## **3️⃣ Prune Infrequent Candidates**

* Remove candidates whose **any subset is not frequent**.
* Based on the Apriori property.

---

## **4️⃣ Scan Database to Find Frequent Itemsets**

* Scan the database again.
* Count support of candidates.
* Keep only those ≥ minimum support.
* These form **Lk+1**.

---

## **5️⃣ Repeat the Process**

* Increase k step by step.
* Stop when:

  * No new frequent itemsets are generated, or
  * Candidate set becomes empty.

---

# **Termination Condition**

The algorithm stops when **no frequent or candidate itemsets can be generated**.

---

# **Advantages**

✔ Simple and easy to understand
✔ Strong theoretical foundation
✔ Effective for small datasets

---

# **Limitations**

❌ Multiple database scans
❌ Large number of candidate itemsets
❌ Slow for large datasets

---

# **One-Line Exam Answer**

> Apriori is a frequent itemset generation algorithm that repeatedly generates candidate itemsets and prunes infrequent ones using the Apriori property until no more frequent itemsets can be found.

---

## **Ultra-Short Exam Version**

* Apriori generates frequent itemsets level-wise.
* Uses the Apriori property to prune infrequent itemsets.
* Repeatedly scans the database.
* Stops when no new frequent itemsets are produced.

---
