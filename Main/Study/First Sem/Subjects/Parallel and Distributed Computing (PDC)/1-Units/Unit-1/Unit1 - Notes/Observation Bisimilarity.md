
## 📘 Observation Bisimilarity

Let

$$
A_1' = (A_1, S_1, \rightarrow_1, S_{01})
\quad \text{and} \quad
A_2' = (A_2, S_2, \rightarrow_2, S_{02})
$$

be two transition systems.

---

### ✅ Definition:

We say:

$$
A_1' \approx A_2' \quad \text{(observation bisimilar)}
$$

If there exists a relation:

$$
B \subseteq S_1 \times S_2
$$

such that:

---

### 🔁 Bisimulation Conditions:

1. $(S_{01}, S_{02}) \in B$
   *(Initial states are related)*

2. For all $(S_1, S_2) \in B$:

   * If $S_1 \xrightarrow{a} S_1'$,
     then $\exists S_2'$ such that
     $S_2 \xrightarrow{a} S_2'$ and
     $(S_1', S_2') \in B$

   * If $S_2 \xrightarrow{a} S_2'$,
     then $\exists S_1'$ such that
     $S_1 \xrightarrow{a} S_1'$ and
     $(S_1', S_2') \in B$

✅ This means:

> Both systems **can simulate each other’s observable steps** while keeping the states **related**.

---

## 📦 Example: Two-Place Buffer vs Two One-Place Buffers

Let’s understand what this means.

---

### 🟦 System 1: Two-Place Buffer

A single buffer with capacity 2.

Transitions (actions):

* `in`: insert item
* `out`: remove item

States:

```
B0 —in→ B1 —in→ B2  
B2 —out→ B1 —out→ B0
```

---

### 🟥 System 2: Two One-Place Buffers in Sequence

You connect two single-place buffers like this:

```
in → [Buffer1] → move → [Buffer2] → out
```

States:

* Each buffer can be empty or full
* System tracks contents of both buffers

States might look like:

* `(0,0)` — both empty
* `(1,0)` — first full, second empty
* `(0,1)` — first empty, second full
* `(1,1)` — both full

Transitions:

* `in`: add to first buffer if empty
* `move`: shift from buffer1 to buffer2
* `out`: remove from buffer2

---

### 🔁 Are They Observation Bisimilar?

Yes, **if we treat `move` as τ (invisible)**.

Both systems:

* Accept 2 inputs → `in in`
* Then `out out` removes them

From the **outside**, they behave **exactly the same**:

* Accept two items
* Deliver them in order

So they are **observation bisimilar**:

$$
\text{Two-place buffer} \approx \text{Two one-place buffers (with τ move)}
$$

---

## 📝 Summary for Exam

> Two transition systems are **observation bisimilar** if they simulate each other’s observable behavior step-by-step.
> A relation $B$ pairs their states such that **each observable action in one has a matching action in the other**, preserving the relation.
>
> A classic example:
> A **2-place buffer** and **two 1-place buffers in series** (with internal τ step) are **observation bisimilar** — they look the same from outside.

---
