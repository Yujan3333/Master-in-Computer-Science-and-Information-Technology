
# **Q3. Support Vector Machine (SVM) Theory**

---

## **(a) Functional Margin**

For a training point $(x^{(i)},y^{(i)})$ with $y^{(i)}\in{-1,+1}$:

$$
\hat{\gamma}^{(i)} = y^{(i)}(w^T x^{(i)} + b)
$$

* If $\hat{\gamma}^{(i)} > 0$ → correctly classified
* Larger value → more confident prediction

For the whole dataset:

$$
\hat{\gamma}=\min_i \hat{\gamma}^{(i)}
$$

---

## **(b) Geometric Margin**

Distance of point from decision boundary:

$$
\gamma^{(i)}=\frac{y^{(i)}(w^T x^{(i)}+b)}{|w|}
$$

Relation:

$$
\gamma^{(i)}=\frac{\hat{\gamma}^{(i)}}{|w|}
$$

Overall geometric margin:

$$
\gamma=\min_i \gamma^{(i)}
$$

Important:

* Functional margin depends on scaling of $(w,b)$
* Geometric margin is scale-invariant

---

## **(c) SVM Optimization Problem**

Hard-margin primal:

$$
\min_{w,b};\frac{1}{2}|w|^2
$$

subject to

$$
y^{(i)}(w^T x^{(i)}+b)\ge1
$$

---

## **Lagrangian**

$$
\mathcal{L}(w,b,\alpha)
=
\frac12|w|^2

\sum_{i=1}^m
\alpha_i\Big(y^{(i)}(w^T x^{(i)}+b)-1\Big)
$$

with $\alpha_i\ge0$.

---

## **KKT Conditions**

1. **Primal feasibility**

$$
y^{(i)}(w^T x^{(i)}+b)\ge1
$$

2. **Dual feasibility**

$$
\alpha_i\ge0
$$

3. **Complementary slackness**

$$
\alpha_i\Big(y^{(i)}(w^T x^{(i)}+b)-1\Big)=0
$$

4. **Stationarity**

$$
w=\sum_i \alpha_i y^{(i)}x^{(i)},
\qquad
\sum_i \alpha_i y^{(i)}=0
$$

Interpretation:

* If $\alpha_i>0$ → point lies on margin → **support vector**
* If $\alpha_i=0$ → point correctly classified outside margin

---

## **Dual Optimization Problem**

$$
\max_{\alpha}
\left(
\sum_i\alpha_i
--------------

\frac12\sum_{i,j}\alpha_i\alpha_j y^{(i)}y^{(j)}(x^{(i)})^T x^{(j)}
\right)
$$

subject to

$$
\alpha_i\ge0,
\qquad
\sum_i\alpha_i y^{(i)}=0
$$

After solving:

$$
w=\sum_i\alpha_i y^{(i)}x^{(i)},
\qquad
b=y^{(j)}-w^T x^{(j)}
\quad\text{for any support vector } j
$$

---

## **Exam-Friendly Summary**

| Concept           | Formula                                      |
| ----------------- | -------------------------------------------- |
| Functional margin | $\hat{\gamma}^{(i)}=y^{(i)}(w^T x^{(i)}+b)$  |
| Geometric margin  | $\gamma^{(i)}=\dfrac{\hat{\gamma}^{(i)}}{w}$ |
| SVM objective     | $\min \frac12w^2$                            |
| Support vectors   | Points with $\alpha_i>0$                     |
| Decision boundary | Depends only on support vectors              |

---
