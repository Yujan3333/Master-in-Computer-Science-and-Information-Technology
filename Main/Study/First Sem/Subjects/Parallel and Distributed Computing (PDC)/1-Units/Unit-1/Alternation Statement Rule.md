
## 🧠 **Alternation Statement Rule (Axiomatic Semantics)**

Alternation statements deal with conditional branching like `if-then` or `if-then-else`. The goal is to prove that, regardless of which branch is taken, the final **postcondition $Q$** holds.

---

### ✅ **1. IF–THEN Rule**

$$
\begin{align*}
\{P \land B\} &\; S \; \{Q\} \\
\{P \land \lnot B\} &\; \text{⊨} \; Q \\
\therefore \; \{P\} &\; \text{IF } B \text{ THEN } S \text{ END IF} \; \{Q\}
\end{align*}
$$

#### 🔹 Meaning:

* If **B is true**, statement `S` is executed and leads to `Q`.
* If **B is false**, `S` is skipped but `Q` must still hold.
* Thus, in **both cases**, `Q` must be satisfied.

---

### ✅ **2. IF–THEN–ELSE Rule**

$$
\begin{align*}
\{P \land B\} &\; S_1 \; \{Q\} \\
\{P \land \lnot B\} &\; S_2 \; \{Q\} \\
\therefore \; \{P\} &\; \text{IF } B \text{ THEN } S_1 \text{ ELSE } S_2 \text{ END IF} \; \{Q\}
\end{align*}
$$

#### 🔹 Meaning:

* If **B is true**, `S₁` executes and leads to `Q`.
* If **B is false**, `S₂` executes and also leads to `Q`.
* Thus, the entire `if-then-else` guarantees `Q` regardless of the condition.

---

### 📘 **Example:**

Let:

* $P \equiv x > 0$
* $B \equiv x > 5$
* $S_1 \equiv x := x - 1$
* $S_2 \equiv x := x + 1$
* $Q \equiv x \ne 0$

Check:

1. $\{x > 0 \land x > 5\} \; x := x - 1 \; \{x \ne 0\}$ ✅ true (since result ≥ 5)
2. $\{x > 0 \land x \le 5\} \; x := x + 1 \; \{x \ne 0\}$ ✅ true (since result ≥ 2)

Thus:

$$
\{x > 0\} \; \text{IF } x > 5 \text{ THEN } x := x - 1 \text{ ELSE } x := x + 1 \text{ END IF} \; \{x \ne 0\}
$$

✅ Holds!

---

### Loop



---
### Disjoint Parallel program


---
### Await Then Rule