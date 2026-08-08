#fuzzy-system #third-semester 

## Composition of Fuzzy Relations

Composition combines **two fuzzy relations** to form a **new fuzzy relation**.

Suppose

* $R$ is a relation from $X$ to $Y$.
* $S$ is a relation from $Y$ to $Z$.

Their composition is denoted by

$$
R \circ S
$$

or sometimes

$$
S \circ R
$$

(depending on the textbook's notation). **Follow your textbook's convention.**

---

## Max-Min Composition (Most Common)

The membership function is

$$
\mu_{R\circ S}(x,z)
=

\max_{y}
\left[
\min\left(\mu_R(x,y),\mu_S(y,z)\right)
\right].
$$

### Steps

For each pair $(x,z)$:

1. Find all possible intermediate elements $y$.
2. Take the **minimum** of the two memberships.
3. Take the **maximum** of all those minimum values.

Hence the name **Max-Min Composition**.

---

## Example

Let

$$
R=
\begin{bmatrix}
0.7 & 0.5\\
0.2 & 1.0
\end{bmatrix},
\qquad
S=
\begin{bmatrix}
0.6 & 0.8\\
0.9 & 0.4
\end{bmatrix}
$$

Find

$$
T=R\circ S.
$$

### Element $(1,1)$

$$
\max\left(
\min(0.7,0.6),
\min(0.5,0.9)
\right)
$$

 $$

\max(0.6,0.5)
=0.6
$$

---

### Element $(1,2)$

$$
\max\left(
\min(0.7,0.8),
\min(0.5,0.4)
\right)
$$

 $$

\max(0.7,0.4)
=0.7
$$

---

### Element $(2,1)$

$$
\max\left(
\min(0.2,0.6),
\min(1.0,0.9)
\right)
$$

 $$

\max(0.2,0.9)
=0.9
$$

---

### Element $(2,2)$

$$
\max\left(
\min(0.2,0.8),
\min(1.0,0.4)
\right)
$$

 $$

\max(0.2,0.4)
=0.4
$$

---

Therefore,

$$
R\circ S=
\begin{bmatrix}
0.6 & 0.7\
0.9 & 0.4
\end{bmatrix}
$$

---

## Max-Product Composition

Instead of taking the minimum, multiply the memberships.

$$
\mu_{R\circ S}(x,z)
=

\max_y
\left[
\mu_R(x,y)\times\mu_S(y,z)
\right]
$$

### Example

For element $(1,1)$:

$$
\max(0.7\times0.6,;0.5\times0.9)
$$

$$

 \max(0.42,;0.45)
=
0.45
$$

---

## Comparison

| Composition     | Formula                     |
| --------------- | --------------------------- |
| **Max-Min**     | $$\max(\min(\mu_R,\mu_S))$$ |
| **Max-Product** | $$\max(\mu_R\times\mu_S)$$  |

---

## Exam Definition (5 Marks)

**Composition of fuzzy relations** combines two fuzzy relations into a new fuzzy relation using an intermediate variable.

The most common composition is the **Max-Min Composition**, defined as

$$
\mu_{R\circ S}(x,z)
===================

\max_{y}
\left[
\min\left(\mu_R(x,y),\mu_S(y,z)\right)
\right].
$$

Another commonly used composition is the **Max-Product Composition**, defined as

$$
\mu_{R\circ S}(x,z)
===================

\max_{y}
\left[
\mu_R(x,y)\times\mu_S(y,z)
\right].
$$

For exams, **Max-Min Composition** is the standard method unless your syllabus or textbook specifically asks for Max-Product.
