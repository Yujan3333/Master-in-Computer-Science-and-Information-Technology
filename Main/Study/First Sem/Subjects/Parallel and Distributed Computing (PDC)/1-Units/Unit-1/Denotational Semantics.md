
## 📐 **Denotational Semantics**

### ✅ **Definition:**

**Denotational semantics** assigns **mathematical meaning** to each construct (expression, statement, etc.) of a programming language.

> It maps every syntactic element to a **mathematical object** (like a number, function, or domain).

---

### 🧠 **Key Idea:**

* Instead of describing *how* a program executes (like operational semantics), denotational semantics describes *what it means* mathematically.
* This is done using **functions** that map inputs to outputs.

---

### 🧾 **Example: Expression `3 * 5 + 4`**

Let’s break it into a **syntax tree**:

```
      +
     / \
    *   4
   / \
  3   5
```

We define denotational meaning as:

* ⟦3⟧ = 3
* ⟦5⟧ = 5  
* ⟦3 * 5⟧ = ⟦3⟧ × ⟦5⟧ = 15
* ⟦3 * 5 + 4⟧ = ⟦3 * 5⟧ + ⟦4⟧ = 15 + 4 = 19

So:

$$
[[ 3 * 5 + 4 ]] = 19
$$

---

### 📝 **Exam-Style Summary:**

> In **denotational semantics**, each program construct is mapped to a **mathematical object** that represents its meaning.
> For example, the expression `3 * 5 + 4` is represented as a **syntax tree**, and its meaning is computed compositionally:
> $[[ 3 * 5 + 4 ]] = 19$.
> This approach emphasizes **mathematical clarity and abstraction** over step-by-step execution.

---

