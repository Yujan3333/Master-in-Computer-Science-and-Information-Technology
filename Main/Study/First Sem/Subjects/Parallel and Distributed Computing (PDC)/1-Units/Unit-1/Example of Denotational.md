
## 📐 **Denotational Semantics — Non-negative Integer Language**

### ✅ **Grammar Definition:**

We define a simple language for **non-negative integers**:

```
Number → Digit | Number Digit  
Digit  → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

---

### 🧠 **Semantic Functions:**

We use **semantic brackets ⟦ ⟧** to assign meanings (denotations) to syntactic constructs:

#### 🔹 **For Digit:**

$$
\text{digit}⟦0⟧ = 0,\; \text{digit}⟦1⟧ = 1,\; \dots,\; \text{digit}⟦9⟧ = 9
$$

#### 🔹 **For Number:**

If $N \rightarrow N_1\; D$, then:

$$
\text{value}⟦N_1 D⟧ = \text{plus}(\text{times}(10, \text{value}⟦N_1⟧), \text{digit}⟦D⟧)
$$

If $N \rightarrow D$, then:

$$
\text{value}⟦D⟧ = \text{digit}⟦D⟧
$$

---

### 🧾 **Worked Example: value⟦65⟧**

Let’s evaluate `65`, which is parsed as:

$$
\text{Number} \rightarrow \text{Number}\; \text{Digit} \rightarrow 6\; 5
$$

Now apply the semantic rule:

$$
\text{value}⟦65⟧ = \text{plus}(\text{times}(10,\; \text{value}⟦6⟧),\; \text{digit}⟦5⟧)
$$

Step-by-step:

* $\text{value}⟦6⟧ = \text{digit}⟦6⟧ = 6$
* $\text{digit}⟦5⟧ = 5$
* $\text{times}(10, 6) = 60$
* $\text{plus}(60, 5) = 65$

✅ Final result:

$$
\text{value}⟦65⟧ = 65
$$

---

### 📝 **Exam-Style Summary:**

> In **denotational semantics**, each syntactic construct is mapped to a **mathematical object**.
> For example, in a simple number language:
>
> * `Number → Digit | Number Digit`
> * We define semantic functions such as:
>
>   $$
>   \text{value}⟦ND⟧ = \text{plus}(\text{times}(10,\; \text{value}⟦N⟧),\; \text{digit}⟦D⟧)
>   $$
>
> Using this, `value⟦65⟧ = 65` is computed recursively.

---
