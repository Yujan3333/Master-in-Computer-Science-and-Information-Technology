## Constraint-Based Association Mining

Constraint-based association mining is a **variant of association rule mining** where **additional constraints** are imposed to focus the search on **interesting or useful patterns only**.

Instead of generating **all possible rules**, we **guide the mining process** using constraints to reduce computational cost and improve relevance.

---

### **1️⃣ Types of Constraints**

1. **Item Constraints**

   * Limit rules to contain **specific items**.
   * Example: Only find rules that **include “Milk”**.

2. **Length Constraints**

   * Restrict the **number of items** in rules.
   * Example: Only consider rules with **2 or 3 items**.

3. **Aggregate Constraints**

   * Use **numerical attributes** like price, quantity, or profit.
   * Example: Rules where **total transaction amount > 100**.

4. **Boolean Constraints**

   * Combine conditions using AND, OR, NOT.
   * Example: **(Milk AND Bread) → NOT Butter**

5. **Interestingness Constraints**

   * Use measures like **lift, confidence, correlation** to filter rules.
   * Example: Only rules with **lift > 1.5**.

---

### **2️⃣ Why It’s Required**

* **Reduce search space:** Standard association mining can generate **too many rules**, most of which may be irrelevant.
* **Focus on domain-relevant rules:** Only rules that satisfy business or scientific constraints are generated.
* **Improve efficiency:** Less computation, faster mining.
* **Increase actionability:** Rules are more meaningful and usable.

---

### **3️⃣ Example**

Suppose transaction dataset:

| Transaction | Items               |
| ----------- | ------------------- |
| T1          | Milk, Bread, Butter |
| T2          | Milk, Bread         |
| T3          | Bread, Butter       |
| T4          | Milk, Butter        |

**Constraint:** Only rules containing **Milk**.

**Mining result:**

* Milk → Bread (support=2, confidence=66%) ✅
* Milk → Butter (support=2, confidence=66%) ✅

**Rules without Milk** are ignored due to the constraint.

---

✅ **Summary:**

Constraint-based association mining is about **filtering and focusing association rules** using conditions on items, length, aggregates, or interestingness measures.

---
