# **FP-Growth Algorithm (Simplified Explanation)**

### **What is FP-Growth?**

FP-Growth (**Frequent Pattern Growth**) is an algorithm used to **find frequent itemsets** from a transaction database **without generating candidate itemsets** (unlike Apriori).

---

## **Main Idea**

> Compress the database into an **FP-tree**, then **mine frequent patterns directly** from the tree.

## [FP-Growth Numerical Example](FP-Growth%20Numerical%20Example.md)

---

# **Step 1: FP-Tree Construction**

FP-tree is built using **two scans** of the database.

---

## **🔹 Pass 1: Find Frequent Items & Order**

### **1️⃣ Scan Database**

* Count support of each item.
* Remove **infrequent items** (below minimum support).

### **2️⃣ Sort Items**

* Sort remaining items in **descending order of support**.
* This order is **fixed globally**.

### **3️⃣ Sort Each Transaction**

* Reorder items in each transaction using the **global frequency order**.
* Purpose: **maximize shared prefixes** in the tree.

---

## **🔹 Pass 2: Build the FP-Tree**

### **1️⃣ Read Transactions One by One**

* Insert each transaction as a **path** in the tree.

### **2️⃣ Share Common Prefixes**

* If transactions start with same items → paths overlap.
* Increase count instead of creating new nodes.

### **3️⃣ Maintain Node Links**

* Nodes with the **same item name** are connected using pointers
  (used later for mining).

📌 Result: A **compact FP-tree** that stores frequency information.

---

# **Step 2: Mining Frequent Patterns from FP-Tree**

This step finds frequent itemsets from the FP-tree.

---

## **1️⃣ Start with Each Frequent 1-Item (Suffix Pattern)**

* Take items **one by one**, starting from **least frequent**.

---

## **2️⃣ Construct Conditional Pattern Base**

* Collect all **prefix paths** leading to that item.
* This is called the **conditional pattern base**.

📌 It shows **how that item appears with other items**.

---

## **3️⃣ Build Conditional FP-Tree**

* From the conditional pattern base, build a **smaller FP-tree**.

---

## **4️⃣ Pattern Growth**

* Combine (concatenate) the **suffix item** with frequent patterns
  found in its conditional FP-tree.

📌 This grows patterns like:

```
{b} → {a, b} → {a, c, b}
```

---

# **Why FP-Growth is Better than Apriori?**

✔ No candidate generation
✔ Only **2 DB scans**
✔ Faster for large datasets
✔ Efficient memory usage

---

# **One-Line Exam Answer**

> FP-Growth finds frequent itemsets by first compressing the transaction database into an FP-tree and then mining frequent patterns using conditional FP-trees without generating candidate itemsets.

---

## **Ultra-Short Exam Version (if asked in 3–4 lines)**

* FP-Growth builds an FP-tree using two scans of the database.
* Items are sorted by descending frequency and common prefixes are shared.
* Frequent patterns are mined using conditional pattern bases and conditional FP-trees.
* It avoids candidate generation and is faster than Apriori.

---
