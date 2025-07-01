
## 🔄 **Sequence Rule**

### ✅ **Definition:**

The **Sequence Rule** lets you reason about the correctness of **two statements executed one after the other**.

If you know:

* Starting from a precondition $P$, after executing statement $S_1$, the postcondition $Q$ holds.
* Starting from $Q$, after executing statement $S_2$, the postcondition $R$ holds.

Then you can conclude:

* Starting from $P$, after executing the sequence $S_1; S_2$, the postcondition $R$ holds.

---

### ✅ **Formal Rule:**

$$
\frac{
\{P\} \; S_1 \; \{Q\} \quad \quad \{Q\} \; S_2 \; \{R\}
}{
\{P\} \; S_1; S_2 \; \{R\}
}
$$

---

### 🔹 **Explanation:**

* $S_1$ transforms the state from satisfying $P$ to satisfying $Q$.
* Then $S_2$ transforms the state from $Q$ to $R$.
* Therefore, running $S_1$ followed by $S_2$ transforms the state from $P$ to $R$.

---

### 📝 **Example:**

* Given:

  $$
  \{x > 1\} \quad x := x + 1 \quad \{x > 2\}
  $$

  and

  $$
  \{x > 2\} \quad x := x * 2 \quad \{x > 4\}
  $$

* By the sequence rule:

  $$
  \{x > 1\} \quad x := x + 1; \; x := x * 2 \quad \{x > 4\}
  $$

---



## 🧠 **Axiomatic Semantics – Sequence Rule Recap**
![](../../../../../../../../Images/First_Sem_Images/Sequence%20Statement%20Rule.png)
The sequence rule is:

$$
\{P\}\;S_1\;\{Q\},\;\{Q\}\;S_2\;\{R\}
\;\Rightarrow\;
\{P\}\;S_1;\;S_2\;\{R\}
$$

This allows us to reason **compositionally** about sequential statements.

---

## 🧩 **Given:**

### 1.

$$
\{x > 1\} \; x := x + 1 \; \{x > 2\}
$$

### 2.

$$
\{x > 0\} \; x := -x \; \{x < 0\}
$$

We also observe:

$$
x > 2 \Rightarrow x > 0
$$

So, even though Statement 2 starts from `x > 0`, we can connect it to Statement 1's postcondition `x > 2` **because** $x > 2 \Rightarrow x > 0$.

---

## ✅ **Conclusion Using Sequence Rule:**

By applying the sequence rule:

$$
\{x > 1\} \; x := x + 1;\; x := -x \; \{x < 0\}
$$

So, the correct postcondition is:

### 🎯 Final Answer:

$$
\{x > 1\} \; x := x + 1; x := -x \; \{x < 0\}
$$

---

