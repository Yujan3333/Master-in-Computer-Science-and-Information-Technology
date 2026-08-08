#fuzzy-system #third-semester 

## Properties of Fuzzy Sets – Normality (Normal Fuzzy Set)

A **normal fuzzy set** is a fuzzy set in which **at least one element has a membership value of 1**.

### Definition

A fuzzy set $A$ is **normal** if:

$$
\max_{x \in X} \mu_A(x) = 1
$$

or equivalently,

$$
\exists , x \in X \text{ such that } \mu_A(x)=1
$$

where:

* $\mu_A(x)$ = membership value of element $x$
* $X$ = universe of discourse

---

## Example (Normal Fuzzy Set)

Let

$$
A={(1,0.2),(2,0.5),(3,1.0),(4,0.7)}
$$

Membership values are:

| Element | Membership |
| ------- | ---------- |
| 1       | 0.2        |
| 2       | 0.5        |
| 3       | 1.0        |
| 4       | 0.7        |

Since the maximum membership value is **1**, the set is **normal**.

---

## Example (Not Normal / Subnormal)

$$
B={(1,0.3),(2,0.6),(3,0.8),(4,0.7)}
$$

Here,

$$
\max \mu_B(x)=0.8<1
$$

Therefore, **$B$ is not normal** (it is called a **subnormal fuzzy set**).

---

## Key Point (Exam)

* **Normal fuzzy set:** Maximum membership value is **1**.
* **Subnormal fuzzy set:** Maximum membership value is **less than 1**.

### One-line Definition (2 Marks)

> A fuzzy set is called **normal** if at least one element has a membership value equal to **1**, i.e.,
>
> $$
> \max_{x \in X}\mu_A(x)=1.
> $$
