#fuzzy-system #third-semester 
A **fuzzy graph** is a graph in which **vertices and/or edges have membership values between 0 and 1**, instead of just being present (1) or absent (0).

---

## Definition

A fuzzy graph is defined as

$$
G=(V,\sigma,\mu)
$$

where:

* $V$ = set of vertices
* $\sigma:V\rightarrow[0,1]$ = membership function of vertices
* $\mu:V\times V\rightarrow[0,1]$ = membership function of edges

The edge membership must satisfy

$$
\mu(u,v)\le\min(\sigma(u),\sigma(v))
$$

This means an edge **cannot have a stronger membership than either of its end vertices**.

---

## Example

Let

$$
V={A,B,C}
$$

Vertex memberships:

| Vertex | Membership |
| ------ | ---------: |
| A      |        0.8 |
| B      |        1.0 |
| C      |        0.6 |

Edge memberships:

| Edge  | Membership |
| ----- | ---------: |
| (A,B) |        0.7 |
| (A,C) |        0.5 |
| (B,C) |        0.4 |

Check the condition:

For edge $(A,B)$,

$$
\mu(A,B)=0.7
$$

and

$$
\min(\sigma(A),\sigma(B))
=

 \min(0.8,1.0)

0.8
$$

Since

$$
0.7\le0.8
$$

the condition is satisfied.

Similarly,

$$
\mu(A,C)=0.5\le\min(0.8,0.6)=0.6
$$

and

$$
\mu(B,C)=0.4\le\min(1.0,0.6)=0.6
$$

---

## Visual Representation

```
        A (0.8)
       /       \
    0.7         0.5
     /           \
 B (1.0)---0.4---C (0.6)
```

* Numbers in **parentheses** are **vertex memberships**.
* Numbers on the **edges** are **edge memberships**.

---

## Crisp Graph vs Fuzzy Graph

| Crisp Graph                              | Fuzzy Graph                                      |
| ---------------------------------------- | ------------------------------------------------ |
| Vertex membership is always 1            | Vertex membership can be between 0 and 1         |
| Edge is either present (1) or absent (0) | Edge membership can be any value between 0 and 1 |
| Edge exists or does not exist            | Edge can exist with varying strength             |

---

### Exam Definition (2–3 marks)

 A **fuzzy graph** is a graph in which the vertices and edges are associated with membership values in the interval $[0,1]$. It is represented as

 $$
 G=(V,\sigma,\mu)
 $$

 where $\sigma$ is the vertex membership function and $\mu$ is the edge membership function satisfying

 $$
 \mu(u,v)\le\min(\sigma(u),\sigma(v)).
 $$

This is the standard definition commonly expected in fuzzy systems exams.
