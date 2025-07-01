
## 📘 Process Algebra Operators

Let:

* $\text{act} = A \cup \{\tau\}$
  (the set of all **actions**, including the silent/unobservable action $\tau$)
* $\text{proc}$: the set of **process terms**, denoted by $P, Q, R$, etc.

---

### 🔹 1. **Prefixing**: $a.P$

$$
P \rightarrow a.P
$$

* Meaning: process first **performs action $a$**, then behaves like **process $P$**
* Example: `login → P` means: first do `login`, then behave like `P`

---

### 🔹 2. **Deadlock** (Stop): $\text{stop}_{A}$

$$
P \rightarrow \text{stop}_{A}
$$

* Meaning: process **cannot perform any action** (dead state)
* It **halts** or is **blocked forever**
* Used to model **termination** or **failure**

---

### 🔹 3. **Choice**: $P + Q$

$$
P \rightarrow P + Q
$$

* Meaning: the system **non-deterministically** behaves like **either $P$** or **$Q$**
* The **choice is external**, depending on which action is enabled
* Example: `read → P + write → Q` means: system can either read or write, then follow the corresponding path

---

### 🔹 4. **Parallel Composition**: $P \parallel Q$

$$
P \rightarrow P \parallel Q
$$

* Meaning: **P and Q run concurrently**
* Each can **perform actions independently**
* If they share actions, **synchronization** may happen (depends on semantic rules)

---

### 🔹 5. **Renaming**: $P[a \leftarrow b]$

$$
P \rightarrow P[a \leftarrow b]
$$

* Meaning: process behaves like $P$, but:

  * When it **executes $b$**, it’s **interpreted as action $a$** instead
* Example: if `P = b → stop`, then `P[a ← b] = a → stop`

---

### 🔹 6. **Restriction** (Hiding): $P \setminus \{b\}$

$$
P \rightarrow P \setminus \{b\}
$$

* Meaning: process behaves like $P$, **but cannot perform action $b$** — it's **hidden** or **blocked**
* Often used to **enforce synchronization or encapsulation**
* Example: hiding internal communication actions

---

## ✅ Summary Table (Exam-Ready)

| Operator    | Notation            | Meaning                                           |
| ----------- | ------------------- | ------------------------------------------------- |
| Prefix      | $a.P$               | Do action $a$, then behave like $P$               |
| Deadlock    | $\text{stop}_{A}$   | Process cannot perform any action (blocked)       |
| Choice      | $P + Q$             | Choose to behave like $P$ or $Q$                  |
| Parallelism | $P \parallel Q$     | Run $P$ and $Q$ concurrently                      |
| Renaming    | $P[a \leftarrow b]$ | Replace action $b$ in $P$ with $a$                |
| Restriction | $P \setminus \{b\}$ | Block/hide action $b$ from being performed by $P$ |

---
