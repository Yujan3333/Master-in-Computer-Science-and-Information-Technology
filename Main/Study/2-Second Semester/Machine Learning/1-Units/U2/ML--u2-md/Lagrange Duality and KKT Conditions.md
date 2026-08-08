For SVM, we start with a **constrained optimization problem** (primal).
Lagrange duality is the idea of converting this constrained problem into another problem (dual) that is often easier to solve.

Take the soft–margin SVM:

Primal problem:

$$
\min_{w,b,\xi};\frac{1}{2}|w|^2 + C\sum_{i=1}^n \xi_i
$$

subject to

$$
y_i(w\cdot x_i + b) \ge 1 - \xi_i,\quad \xi_i \ge 0
$$

Here:

* $w,b$ define the hyperplane
* $\xi_i$ are slack variables
* $C$ controls the penalty for misclassification

---

### Lagrange Duality Principle:

We introduce Lagrange multipliers:

* $\alpha_i \ge 0$ for constraints
  $y_i(w\cdot x_i + b) \ge 1 - \xi_i$
* $\mu_i \ge 0$ for constraints
  $\xi_i \ge 0$

Construct the Lagrangian:

$$
\begin{aligned}
L(w,b,\xi,\alpha,\mu)
= &\frac{1}{2}|w|^2 + C\sum_i \xi_i \
&- \sum_i \alpha_i\big[y_i(w\cdot x_i + b) - 1 + \xi_i\big] \
&- \sum_i \mu_i \xi_i
\end{aligned}
$$

Duality says:

* Minimize $L$ w.r.t. primal variables $(w,b,\xi)$
* Maximize $L$ w.r.t. dual variables $(\alpha,\mu)$

This gives the **dual problem**, which depends only on $\alpha_i$:

$$
\max_{\alpha};\sum_i \alpha_i

* \frac{1}{2}\sum_i\sum_j \alpha_i \alpha_j y_i y_j (x_i\cdot x_j)
  $$

subject to:

$$
0 \le \alpha_i \le C
$$

$$
\sum_i \alpha_i y_i = 0
$$

This is the optimization that SVM actually solves.

---

### KKT Conditions (Karush–Kuhn–Tucker):

They are the necessary conditions for optimality.
For SVM, they link the primal and dual solutions.

1. **Primal feasibility**

$$
y_i(w\cdot x_i + b) \ge 1 - \xi_i,\quad \xi_i \ge 0
$$

2. **Dual feasibility**

$$
\alpha_i \ge 0,\quad \mu_i \ge 0
$$

3. **Stationarity**

Partial derivatives of $L$ must vanish:

From $\frac{\partial L}{\partial w}=0$:

$$
w = \sum_i \alpha_i y_i x_i
$$

From $\frac{\partial L}{\partial b}=0$:

$$
\sum_i \alpha_i y_i = 0
$$

From $\frac{\partial L}{\partial \xi_i}=0$:

$$
\alpha_i + \mu_i = C
$$

So:

$$
0 \le \alpha_i \le C
$$

4. **Complementary slackness**

$$
\alpha_i,[y_i(w\cdot x_i + b) - 1 + \xi_i] = 0
$$

$$
\mu_i,\xi_i = 0
$$

This is the most important intuition:

* If $\alpha_i > 0$, then
  $y_i(w\cdot x_i + b) = 1 - \xi_i$
  → point lies on margin or inside margin
  → it is a **support vector**

* If $\alpha_i = 0$, the point does not affect the boundary.

---

So in simple words:

* **Lagrange duality**:
  Converts the constrained SVM problem into a dual problem using multipliers, making it solvable via $\alpha_i$ only.

* **KKT conditions**:
  They describe when a solution is optimal and explain:

  * why only some points become **support vectors**
  * how $w$ is built from training data
  * how margin conditions are satisfied

One-line summary:

> Lagrange duality gives us the dual SVM optimization, and KKT conditions explain which points shape the decision boundary and why they are called support vectors.
