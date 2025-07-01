
## 📘 Formal Definition of Labeled Transition System (LTS)

A labeled transition system is defined as:

$$
A' = (A, S, \rightarrow, S_0)
$$

### Where:

| Symbol     | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| **A**      | Alphabet: the set of **observable actions/events**      |
| **S**      | Set of **states**                                       |
| **→**      | Transition relation: $S \times (A \cup \{\tau\}) \to S$ |
| **$\tau$** | Unobservable (silent) action                            |
| **S₀**     | Initial (root) state                                    |

---

### 🔁 Transition Relation

* A transition $S \xrightarrow{a} S'$ means:
  From state $S$, the system **performs action $a$** and moves to state $S'$.

* If $a = \tau$, it's an **internal step** (unobservable).

---

## 📑 Conventions

* $a, b, c, \dots$: observable actions (from alphabet $A$)
* $u, v, \dots$: actions from $A \cup \{\tau\}$ (including silent actions)
* $w$: a **sequence of actions** (a word) from $(A \cup \{\tau\})^*$
* $ow$: a word from $A^*$ (only observable actions — **τs removed**)

---

## 🔄 Example: Multi-step Transition

You wrote:

> $S \xrightarrow{w} S'$ if there exists a sequence of transitions:
>
> $$
> $$

$S = S_1 \xrightarrow{u_1} S_2 \xrightarrow{u_2} S_3 \xrightarrow{u_3} \dots \xrightarrow{u_n} S_n = S']$

That means:

* The system can go from state $S$ to $S'$ by executing the sequence of actions $u_1, u_2, ..., u_n$, which together form the **word** $w = u_1 u_2 ... u_n$

---

## 📌 Summary (Exam-Ready):

> A **labeled transition system (LTS)** is a formal model of system behavior.
> It consists of **states**, **actions (observable + unobservable)**, and **transitions**.
> A transition $S \xrightarrow{a} S'$ means that **action $a$** causes a change from **state $S$** to **state $S'$**.
> A **path labeled by a word $w$** is a sequence of such transitions from one state to another.

---
