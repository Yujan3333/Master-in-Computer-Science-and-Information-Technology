
# ✅ 🔹 Problem Overview

We are given a **fuzzy similarity relation** $R_1$ for 5 bacteria strains:

$$
R_1=
\begin{bmatrix}
1 & 0.8 & 0 & 0.1 & 0.2\\
0.8 & 1 & 0.4 & 0 & 0.9\\
0 & 0.4 & 1 & 0 & 0\\
0.1 & 0 & 0 & 1 & 0.5\\
0.2 & 0.9 & 0 & 0.5 & 1
\end{bmatrix}
$$

---

# 🔹 Step 1: Check properties

### ✅ Reflexive

All diagonal elements = 1

### ✅ Symmetric

Matrix is symmetric

### ❌ Not Transitive

Example:

* $\mu(x_1,x_2)=0.8$
* $\mu(x_2,x_5)=0.9$

Expected:

$$
\mu(x_1,x_5)\ge\min(0.8,0.9)=0.8
$$

But:

$$
\mu(x_1,x_5)=0.2
$$

👉 So NOT transitive

---

# 🔹 Step 2: Goal

Convert this into a **fuzzy equivalence relation**, which must be:

* Reflexive ✅
* Symmetric ✅
* Transitive ❗

👉 We fix transitivity using **composition**

---

# 🔹 Step 3: Max–Min Composition

To compute:

$$
R_1^2 = R_1 \circ R_1
$$

Use:

$$
(R_1^2)(i,j)=\max_k\min(R_1(i,k),R_1(k,j))
$$

---

# 🔹 Step 4: Example Calculation (IMPORTANT)

## Compute $(x_1,x_5)$

### Row 1:

$$
[1,0.8,0,0.1,0.2]
$$

### Column 5:

$$
[0.2,0.9,0,0.5,1]
$$

---

### Compute for each $k$:

* $k=1 \rightarrow \min(1,0.2)=0.2$
* $k=2 \rightarrow \min(0.8,0.9)=0.8$
* $k=3 \rightarrow \min(0,0)=0$
* $k=4 \rightarrow \min(0.1,0.5)=0.1$
* $k=5 \rightarrow \min(0.2,1)=0.2$

---

### Take max:

$$
\max(0.2,0.8,0,0.1,0.2)=0.8
$$

---

### ✅ Result:

$$
(R_1^2)(x_1,x_5)=0.8
$$

---

# 🔹 Step 5: What does this mean?

Original:

$$
R_1(x_1,x_5)=0.2
$$

Updated:

$$
R_1^2(x_1,x_5)=0.8
$$

👉 It **replaces the old value**

---

# 🔹 Why did it increase?

Because of **indirect similarity**:

$$
x_1 \rightarrow x_2 = 0.8,\quad x_2 \rightarrow x_5 = 0.9
$$

So:

$$
\min(0.8,0.9)=0.8
$$

👉 Stronger path found → value updated

---

# 🔹 Step 6: Resulting Matrix $R_1^2$

$$
R_1^2=
\begin{bmatrix}
1 & 0.8 & 0.4 & 0.2 & 0.8\
0.8 & 1 & 0.4 & 0.5 & 0.9\
0.4 & 0.4 & 1 & 0 & 0.4\
0.2 & 0.5 & 0 & 1 & 0.5\
0.8 & 0.9 & 0.4 & 0.5 & 1
\end{bmatrix}
$$

---

# 🔹 Step 7: Still not transitive

Example:

* $x_1 \rightarrow x_2 = 0.8$
* $x_2 \rightarrow x_4 = 0.5$

Expected:

$$
x_1 \rightarrow x_4 \ge 0.5
$$

But:

$$
x_1 \rightarrow x_4 = 0.2
$$

👉 Still not transitive

---

# 🔹 Step 8: Repeat Composition

Compute again:

$$
R_1^3 = R_1^2 \circ R_1
$$

Repeat until matrix stops changing.

---

# 🔹 Final Result (Transitive Closure)

$$
R=
\begin{bmatrix}
1 & 0.8 & 0.4 & 0.5 & 0.8\\
0.8 & 1 & 0.4 & 0.5 & 0.9\\
0.4 & 0.4 & 1 & 0.4 & 0.4\\
0.5 & 0.5 & 0.4 & 1 & 0.5\\
0.8 & 0.9 & 0.4 & 0.5 & 1
\end{bmatrix}
$$

---

# 🔹 Step 9: Now it is transitive ✅

Example:

* $x_1 \rightarrow x_2 = 0.8$
* $x_2 \rightarrow x_4 = 0.5$

$$
\min(0.8,0.5)=0.5
$$

Now:

$$
x_1 \rightarrow x_4 = 0.5
$$

👉 Condition satisfied

---

# 🔹 Final Conclusion

After repeated composition:

👉 The relation becomes a **Fuzzy Equivalence Relation**

✔ Reflexive
✔ Symmetric
✔ Transitive

---

# 🔥 🔹 Key Intuition (MOST IMPORTANT)

* Initial matrix → only **direct similarity**
* Composition → adds **indirect similarity**
* Repeating → spreads similarity across network
* Final matrix → **complete similarity structure**

---

# 🔹 Exam Summary

👉 Use max–min composition:

$$
(R \circ R)(i,j)=\max_k\min(R(i,k),R(k,j))
$$

👉 Repeat until matrix stops changing
👉 Final matrix = **transitive closure (fuzzy equivalence relation)**
