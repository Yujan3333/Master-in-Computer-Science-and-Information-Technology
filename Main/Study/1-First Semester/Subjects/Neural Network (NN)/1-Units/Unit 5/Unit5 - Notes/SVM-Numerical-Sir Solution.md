

$$
\alpha s_1 \cdot s_1 + \beta s_2 \cdot s_1 + \lambda s_3 \cdot s_1 = -1  
$$

$$
\alpha s_1 \cdot s_2 + \beta s_2 \cdot s_2 + \lambda s_3 \cdot s_2 = +1  
$$

$$
\alpha s_1 \cdot s_3 + \beta s_2 \cdot s_3 + \lambda s_3 \cdot s_3 = +1  
$$

become the simplified system:

$$
2\alpha + 4\beta + 4\lambda = -1  
$$

$$
4\alpha + 11\beta + 9\lambda = 1  
$$

$$
4\alpha + 9\beta + 11\lambda = 1  
$$

---

### 🔧 Step 1: Augmented Vectors

We're working in **3D** now because the vectors are **augmented** by adding 1 at the end to incorporate the bias term $b$.

So:

* $s_1 = (1, 0, 1)$
* $s_2 = (3, 1, 1)$
* $s_3 = (3, -1, 1)$

---

### 📌 Step 2: Understand the Dot Products

Let’s compute the dot products between all combinations of these augmented vectors.

The dot product formula is:

$$
\textbf{u} \cdot \textbf{v} = u_1v_1 + u_2v_2 + u_3v_3
$$

---

### 🧮 Equation 1:

$$
\alpha s_1 \cdot s_1 + \beta s_2 \cdot s_1 + \lambda s_3 \cdot s_1 = -1
$$

* $s_1 \cdot s_1 = (1)^2 + (0)^2 + (1)^2 = 1 + 0 + 1 = 2$
* $s_2 \cdot s_1 = 3\cdot1 + 1\cdot0 + 1\cdot1 = 3 + 0 + 1 = 4$
* $s_3 \cdot s_1 = 3\cdot1 + (-1)\cdot0 + 1\cdot1 = 3 + 0 + 1 = 4$

So:

$$
2\alpha + 4\beta + 4\lambda = -1
$$

✅ Matches Equation 1.

---

### 🧮 Equation 2:

$$
\alpha s_1 \cdot s_2 + \beta s_2 \cdot s_2 + \lambda s_3 \cdot s_2 = 1
$$

* $s_1 \cdot s_2 = 1\cdot3 + 0\cdot1 + 1\cdot1 = 3 + 0 + 1 = 4$
* $s_2 \cdot s_2 = 3^2 + 1^2 + 1^2 = 9 + 1 + 1 = 11$
* $s_3 \cdot s_2 = 3\cdot3 + (-1)\cdot1 + 1\cdot1 = 9 -1 +1 = 9$

So:

$$
4\alpha + 11\beta + 9\lambda = 1
$$

✅ Matches Equation 2.

---

### 🧮 Equation 3:

$$
\alpha s_1 \cdot s_3 + \beta s_2 \cdot s_3 + \lambda s_3 \cdot s_3 = 1
$$

* $s_1 \cdot s_3 = 1\cdot3 + 0\cdot(-1) + 1\cdot1 = 3 + 0 + 1 = 4$
* $s_2 \cdot s_3 = 3\cdot3 + 1\cdot(-1) + 1\cdot1 = 9 -1 +1 = 9$
* $s_3 \cdot s_3 = 3^2 + (-1)^2 + 1^2 = 9 + 1 + 1 = 11$

So:

$$
4\alpha + 9\beta + 11\lambda = 1
$$

✅ Matches Equation 3.

---

### ✅ Final Summary

By plugging in the actual vector coordinates and computing all the dot products, we arrived at:

$$
\begin{align*}
2\alpha + 4\beta + 4\lambda &= -1 \\
4\alpha + 11\beta + 9\lambda &= 1 \\
4\alpha + 9\beta + 11\lambda &= 1
\end{align*}
$$

These equations are now ready to be solved (e.g., using substitution or matrix methods) to find $\alpha, \beta, \lambda$.

---


