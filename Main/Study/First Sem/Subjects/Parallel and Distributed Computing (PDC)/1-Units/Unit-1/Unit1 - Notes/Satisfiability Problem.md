
## 🔍 **Satisfiability Problem (SAT)**

### ✅ **Definition:**

The **Satisfiability Problem (SAT)** asks:

> **Is there an assignment of truth values (True or False) to the variables in a Boolean formula such that the entire formula evaluates to TRUE?**

If such an assignment exists, the formula is said to be **satisfiable**.

---

### 🔹 **CNF (Conjunctive Normal Form):**

* Boolean formula is often written in **CNF**: a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals.
* Example:

  $$
  S = (x_1 \lor x_2) \land (x_3 \lor x_4 \lor x_5)
  $$

---

### ✅ **SAT Problem Importance:**

* **First problem** proven to be **NP-complete** (Cook's Theorem)
* Fundamental to fields like:

  * Artificial Intelligence (logic reasoning)
  * Theorem proving
  * Software/hardware verification

---

### 🧠 **Examples from Your Question:**

#### ✅ Example 1:

$$
E = (x \lor y \lor z) \land (x \lor \lnot y \lor \lnot w) \land (\lnot z \lor w) \land (\lnot x)
$$

**Assignment**:
Let:

* $x = F$
* $y = T$
* $z = F$
* $w = F$

Now test each clause:

1. $(F \lor T \lor F) = T$ ✅
2. $(F \lor \lnot T \lor \lnot F) = (F \lor F \lor T) = T$ ✅
3. $(\lnot F \lor F) = (T \lor F) = T$ ✅
4. $(\lnot F) = T$ ✅

✅ All clauses are true → **Satisfiable**

---

#### ❌ Example 2:

$$
E = (x \lor y) \land (\lnot x) \land (\lnot y)
$$

Let’s analyze:

* Clause 1: $(x \lor y)$ requires **at least one to be true**
* Clause 2: $\lnot x$ → $x = F$
* Clause 3: $\lnot y$ → $y = F$

Then Clause 1 becomes:

$$
(x \lor y) = (F \lor F) = F ❌
$$

So the formula **cannot be satisfied**.
✅ **Not satisfiable**

---

### 📝 **Exam Answer Summary:**

> The **Satisfiability Problem (SAT)** asks whether a **Boolean formula** can be made **true** by assigning **true or false** values to its variables.
>
> The formula is typically given in **Conjunctive Normal Form (CNF)**, where each clause is a disjunction (OR) of literals, and the whole formula is a conjunction (AND) of such clauses.
>
> A formula is **satisfiable** if **there exists at least one assignment** that makes it true. SAT is the **first NP-complete problem**, and plays a key role in computer science, especially in logic and AI.

---

