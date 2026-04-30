The **difference between characteristic function and membership function** is mainly in **classical sets vs fuzzy sets**.

## 1. Characteristic Function (Crisp Set)

A **characteristic function** tells whether an element **belongs or does not belong** to a set.

It gives only two values:

* **1** → element belongs to the set
* **0** → element does not belong to the set

### Definition

For a set $A$:

$$
\chi_A(x)=
\begin{cases}
1,& x\in A\
0,& x\notin A
\end{cases}
$$

### Example

Let $A={2,4,6,8}$

Then:

* $\chi_A(4)=1$
* $\chi_A(5)=0$

So membership is exact.

---

## 2. Membership Function (Fuzzy Set)

A **membership function** is used in **fuzzy sets** where belonging is gradual.

It gives values between **0 and 1**:

* **0** → no membership
* **1** → full membership
* **Between 0 and 1** → partial membership

### Definition

For fuzzy set $A$:

$$
\mu_A(x)\in[0,1]
$$

### Example

Fuzzy set = “Tall people”

* Person with height 150 cm → $\mu=0.2$
* Person with height 170 cm → $\mu=0.6$
* Person with height 190 cm → $\mu=1$

This means tallness is gradual, not strict.

---

## Key Differences

| Basis      | Characteristic Function | Membership Function |
| ---------- | ----------------------- | ------------------- |
| Used in    | Classical Set           | Fuzzy Set           |
| Values     | 0 or 1                  | 0 to 1              |
| Membership | Exact                   | Partial             |
| Logic      | Boolean                 | Fuzzy Logic         |
| Example    | Even numbers            | Tall people         |

---

## Important Relation

A characteristic function is a **special case** of membership function where only values **0 and 1** are allowed.

---

## 5-Mark Exam Answer

Characteristic function is used in classical set theory and gives only two values: 1 if the element belongs to the set, and 0 if it does not belong. Membership function is used in fuzzy set theory and gives any value between 0 and 1 to represent partial membership. Characteristic function represents exact membership, while membership function represents gradual membership. Thus, characteristic function is binary whereas membership function is continuous.
