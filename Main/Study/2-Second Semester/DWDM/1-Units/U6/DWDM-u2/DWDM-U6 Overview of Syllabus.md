# **Unit VI: Mining Association Rules in Large Databases**

Association rule mining discovers **interesting relationships** between items in large databases.

---

## **1️⃣ Basics of Association Rules**

* **Association rule:** An implication of the form **$X \Rightarrow Y$**

  * $X$, $Y$ are itemsets
  * **Support:** Fraction of transactions containing $X \cup Y$
  * **Confidence:** Probability that a transaction containing $X$ also contains $Y$

**Example:**

* Rule: `{Bread} ⇒ {Butter}`
* Support = 5%, Confidence = 60% → 60% of transactions with bread also have butter

---

## **2️⃣ Single-Dimensional Boolean Association Rules**

* Only **one attribute** or **item presence/absence** considered
* Example: Market-basket transactions (items bought together)
* Steps:

  1. Find **frequent itemsets** (using **Apriori** or **FP-Growth**)
  2. Generate rules from frequent itemsets
* **Boolean:** Presence (1) or absence (0) of items

---

## **3️⃣ Multilevel Association Rules**

* Rules at **different levels of abstraction** (concept hierarchies)
* Example:

  * Level 1: `{Laptop} ⇒ {Mouse}`
  * Level 2: `{Electronics} ⇒ {Accessory}`
* Steps:

  1. Define **concept hierarchies** for items
  2. Mine rules **level by level**
* Benefits: Detects patterns at **both general and detailed levels**

---

## **4️⃣ Multidimensional Association Rules**

* Rules involve **multiple attributes** (not just items)
* Example:

  * `{Age=Young, Income=High} ⇒ {Buy=SportsCar}`
* Can be mined from **relational databases** or **data warehouses**
* More expressive, helps find **complex patterns across dimensions**

---

## **5️⃣ From Association to Correlation Analysis**

* Association rules **don’t always indicate true correlation**
* Correlation measures: Determine if $X$ and $Y$ are **positively or negatively related**
* **Example:** Bread and butter may appear together often (support), but are they really correlated?

---

## **6️⃣ Constraint-Based Association Mining**

* Adds **user-defined constraints** to focus mining
* Examples of constraints:

  1. **Item constraints:** Only consider certain items
  2. **Aggregate constraints:** Support must exceed 5%
  3. **Boolean constraints:** Must include/exclude some items
* **Benefits:** Reduces search space and improves efficiency

---

### **Quick Exam Tip**

You can summarize **types of association rule mining** as:

> **Single-dimensional → Multilevel → Multidimensional → Correlation → Constraint-based**

**Key formulas:**

* Support: $$support(X \Rightarrow Y) = \frac{count(X \cup Y)}{Total\ Transactions}$$
* Confidence: $$confidence(X \Rightarrow Y) = \frac{count(X \cup Y)}{count(X)}$$

---
