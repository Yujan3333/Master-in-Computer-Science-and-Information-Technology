#fuzzy-system #third-semester 


# Fuzzy Relation Operations

Let

$$
R=
\begin{bmatrix}
0.2 & 0.8\\
0.5 & 1.0
\end{bmatrix},
\qquad
S=
\begin{bmatrix}
0.7 & 0.3\\
0.5 & 0.6
\end{bmatrix}
$$

---

# 1. Union

**Membership Function**

$$
\mu_{R\cup S}(x,y)=\max(\mu_R(x,y),\mu_S(x,y))
$$

**Example**

$$
R\cup S=
\begin{bmatrix}
\max(0.2,0.7) & \max(0.8,0.3)\\
\max(0.5,0.5) & \max(1.0,0.6)
\end{bmatrix}
=============

\begin{bmatrix}
0.7 & 0.8\\
0.5 & 1.0
\end{bmatrix}
$$

---

# 2. Intersection

**Membership Function**

$$
\mu_{R\cap S}(x,y)=\min(\mu_R(x,y),\mu_S(x,y))
$$

**Example**

$$
R\cap S=
\begin{bmatrix}
\min(0.2,0.7) & \min(0.8,0.3)\\
\min(0.5,0.5) & \min(1.0,0.6)
\end{bmatrix}
=============

\begin{bmatrix}
0.2 & 0.3\\
0.5 & 0.6
\end{bmatrix}
$$

---

# 3. Complement

**Membership Function**

$$
\mu_{R^c}(x,y)=1-\mu_R(x,y)
$$

**Example**

$$
R^c=
\begin{bmatrix}
1-0.2 & 1-0.8\\
1-0.5 & 1-1.0
\end{bmatrix}
=============

\begin{bmatrix}
0.8 & 0.2\\
0.5 & 0
\end{bmatrix}
$$

---

# 4. Subset (Containment)

A fuzzy relation $R$ is a subset of $S$ if

$$
\mu_R(x,y)\le\mu_S(x,y)
$$

for every ordered pair.

**Example**

$$
\begin{aligned}
0.2&\le0.7 \quad \checkmark\\
0.8&\le0.3 \quad \times
\end{aligned}
$$

Hence,

$$
R\nsubseteq S
$$

---

# 5. Identity Relation

$$
\mu_I(x,y)=
\begin{cases}
1,&x=y\\
0,&x\ne y
\end{cases}
$$

**Example**

$$
I=
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}
$$

---

# 6. Distributive Law

$$
R\cup(S\cap T)=(R\cup S)\cap(R\cup T)
$$

$$
R\cap(S\cup T)=(R\cap S)\cup(R\cap T)
$$

Let

$$
T=
\begin{bmatrix}
0.4 & 0.9\\
0.6 & 0.2
\end{bmatrix}
$$

**Example**

$$
S\cap T=
\begin{bmatrix}
0.4 & 0.3\\
0.5 & 0.2
\end{bmatrix}
$$

$$
R\cup(S\cap T)=
\begin{bmatrix}
0.4 & 0.8\\
0.5 & 1.0
\end{bmatrix}
$$

$$
R\cup S=
\begin{bmatrix}
0.7 & 0.8\\
0.5 & 1.0
\end{bmatrix}
$$

$$
R\cup T=
\begin{bmatrix}
0.4 & 0.9\\
0.6 & 1.0
\end{bmatrix}
$$

$$
(R\cup S)\cap(R\cup T)=
\begin{bmatrix}
0.4 & 0.8\\
0.5 & 1.0
\end{bmatrix}
$$

Hence,

$$
R\cup(S\cap T)=(R\cup S)\cap(R\cup T)
$$

---

# 7. Associative Law

$$
(R\cup S)\cup T=R\cup(S\cup T)
$$

$$
(R\cap S)\cap T=R\cap(S\cap T)
$$

**Example**

$$
(R\cup S)\cup T=
\begin{bmatrix}
0.7 & 0.9\\
0.6 & 1.0
\end{bmatrix}
$$

$$
R\cup(S\cup T)=
\begin{bmatrix}
0.7 & 0.9\\
0.6 & 1.0
\end{bmatrix}
$$

Hence,

$$
(R\cup S)\cup T=R\cup(S\cup T)
$$

---

# 8. Commutative Law

$$
R\cup S=S\cup R
$$

$$
R\cap S=S\cap R
$$

**Example**

$$
R\cup S=
\begin{bmatrix}
0.7 & 0.8\\
0.5 & 1.0
\end{bmatrix}
=============

S\cup R
$$

$$
R\cap S=
\begin{bmatrix}
0.2 & 0.3\\
0.5 & 0.6
\end{bmatrix}
=============

S\cap R
$$

---

# 9. De Morgan's Laws

$$
(R\cup S)^c=R^c\cap S^c
$$

$$
(R\cap S)^c=R^c\cup S^c
$$

**Example**

$$
(R\cup S)^c=
\begin{bmatrix}
0.3 & 0.2\\
0.5 & 0
\end{bmatrix}
$$

$$
R^c=
\begin{bmatrix}
0.8 & 0.2\\
0.5 & 0
\end{bmatrix},
\qquad
S^c=
\begin{bmatrix}
0.3 & 0.7\\
0.5 & 0.4
\end{bmatrix}
$$

$$
R^c\cap S^c=
\begin{bmatrix}
0.3 & 0.2\\
0.5 & 0
\end{bmatrix}
$$

Hence,

$$
(R\cup S)^c=R^c\cap S^c
$$

---

# 10. Excluded Middle

$$
R\cup R^c\ne U
$$

**Example**

$$
R=
\begin{bmatrix}
0.2 & 0.8\\
0.5 & 1.0
\end{bmatrix},
\qquad
R^c=
\begin{bmatrix}
0.8 & 0.2\\
0.5 & 0
\end{bmatrix}
$$

$$
R\cup R^c=
\begin{bmatrix}
0.8 & 0.8\\
0.5 & 1.0
\end{bmatrix}
$$

$$
U=
\begin{bmatrix}
1 & 1\\
1 & 1
\end{bmatrix}
$$

Hence,

$$
R\cup R^c\ne U
$$

---

# Quick Comparison

| Property         | Crisp Relation              | Fuzzy Relation                                             |
| ---------------- | --------------------------- | ---------------------------------------------------------- |
| Union            | $R\cup S$                   | Maximum of corresponding memberships                       |
| Intersection     | $R\cap S$                   | Minimum of corresponding memberships                       |
| Complement       | $A-R$                       | $1-\mu_R$                                                  |
| Subset           | Every pair of $R$ is in $S$ | Every corresponding membership of $R$ is $\le$ that of $S$ |
| Identity         | $(x,x)$ only                | 1 on the diagonal, 0 elsewhere                             |
| Distributive     | Holds                       | Holds                                                      |
| Associative      | Holds                       | Holds                                                      |
| Commutative      | Holds                       | Holds                                                      |
| De Morgan's Laws | Hold                        | Hold                                                       |
| Excluded Middle  | Holds                       | Does **not** generally hold                                |
