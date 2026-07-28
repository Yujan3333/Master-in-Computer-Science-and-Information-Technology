#fuzzy-system #third-semester 

![](../../../../../../Images/Third_Sem_Images/Anti%20Symmetric.png)

### Crisp Antisymmetric

A crisp relation is antisymmetric if

$$
(a,b)\in R \text{ and } (b,a)\in R
\Rightarrow
a=b
$$

This means that for **different elements**, you **cannot** have both directions present.

---

### Fuzzy Antisymmetric

In fuzzy relations, instead of "present" or "absent", we have membership values.

The definition becomes:

$$
\mu_R(x_i,x_j)>0
\Rightarrow
\mu_R(x_j,x_i)=0,
\qquad x_i\ne x_j
$$

This means:

> If the relation from $x_i$ to $x_j$ has **any positive membership**, then the reverse relation **must be exactly 0**.

For **different elements**, only **one direction** can have a positive membership.

---

## Example 1

Suppose

$$
R=
\begin{bmatrix}
0 & 0.7\
0 & 0
\end{bmatrix}
$$

This means

* $\mu(1,2)=0.7$
* $\mu(2,1)=0$

Since

$$
0.7>0
\quad\text{and}\quad
0=0,
$$

the relation **is antisymmetric**.

---

## Example 2 (Not Antisymmetric)

$$
R=
\begin{bmatrix}
0 & 0.7\
0.4 & 0
\end{bmatrix}
$$

Here,

* $\mu(1,2)=0.7$
* $\mu(2,1)=0.4$

Both are **greater than 0**.

This violates the rule because

$$
\mu(1,2)>0
$$

but

$$
\mu(2,1)\ne0.
$$

So the relation is **not antisymmetric**.

---

## Now let's check your matrix $R_4$

$$
R_4=
\begin{bmatrix}
0 & 0 & 0.7\
0.2 & 0 & 0\
0 & 0.1 & 0
\end{bmatrix}
$$

Look at each pair:

### Pair $(1,2)$ and $(2,1)$

$$
\mu(1,2)=0,\qquad
\mu(2,1)=0.2
$$

Only one direction is positive. ✅

---

### Pair $(1,3)$ and $(3,1)$

$$
\mu(1,3)=0.7,\qquad
\mu(3,1)=0
$$

Only one direction is positive. ✅

---

### Pair $(2,3)$ and $(3,2)$

$$
\mu(2,3)=0,\qquad
\mu(3,2)=0.1
$$

Only one direction is positive. ✅

So **$R_4$ is antisymmetric**.

---

## Now check $R_5$

$$
R_5=
\begin{bmatrix}
1 & 0 & 0\
0.6 & 0.5 & 0.7\
0.7 & 0 & 0.2
\end{bmatrix}
$$

### Pair $(1,2)$ and $(2,1)$

$$
0,\qquad0.6
$$

Only one is positive. ✅

---

### Pair $(2,3)$ and $(3,2)$

$$
0.7,\qquad0
$$

Only one is positive. ✅

---

### Pair $(1,3)$ and $(3,1)$

$$
0,\qquad0.7
$$

Only one is positive. ✅

So **$R_5$ is also antisymmetric**.

Notice that the diagonal entries like

$$
\mu(1,1)=1,\quad
\mu(2,2)=0.5,\quad
\mu(3,3)=0.2
$$

**do not matter**, because the condition is only for

$$
x_i\ne x_j.
$$

---

### Easy trick for exams

For every pair of different elements:

* Compare $(i,j)$ and $(j,i)$.
* If **both are positive**, ❌ **Not antisymmetric**.
* If **at most one is positive**, ✅ **Antisymmetric**.

That's all you need to check.
