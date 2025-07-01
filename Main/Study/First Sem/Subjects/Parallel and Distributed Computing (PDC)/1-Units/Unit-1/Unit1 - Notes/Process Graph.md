
## 📘 Process Graph and Process Algebra

### 1. **Process Graph**

* A **process graph** is a **labeled transition system** where:

  * Each **node** represents a **state**.
  * Each **edge** represents a **transition** due to an **action**.
* One **state is selected as the root state** (initial state of the system).

#### ➤ Transition Notation:

* If the graph contains an edge:

  $$
  S \xrightarrow{a} S'
  $$

  * It means the system can evolve from **state S** to **state S′** by performing **action $a$**.

---

### 2. **Process Algebra**

* **Process algebra** is a **mathematical framework** to describe and reason about system behavior **using algebraic expressions**.
* It allows expressing **processes**, their **actions**, and how they **combine**, **interact**, or **evolve**.

---

### 3. **Types of Actions in Process Algebra**

#### a) **Observable Actions**

* Represent **visible events** that can be detected from outside the system.
* Example: sending a message, clicking a button, etc.

#### b) **Unobservable Actions (Silent Actions or τ-actions)**

* Represent **internal steps** or events **invisible to the external observer**.
* Denoted by the Greek letter **τ (tau)**.
* Example: internal computation or decision-making not visible to users.

---

## ✅ Summary for Exam:

> A **process graph** is a labeled transition system with a designated root state, modeling how processes move between states by performing actions.
> If the graph has a transition $S \xrightarrow{a} S'$, it means that performing **action a** in **state S** leads to **state S′**.
> To reason about system behavior mathematically, we use **process algebra**, which expresses such behavior using **algebraic terms**.
> Process algebra distinguishes between:
>
> * **Observable actions** (visible external behavior),
> * **Unobservable actions** (internal, silent steps).

---
