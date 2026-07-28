#fuzzy-system #third-semester #old-que #exam-paper-answer 

These are **5-mark questions**, so the answers should be **short, exam-oriented, and complete**. Below are concise answers you can write in the exam.

---

# Q1. Create fuzzy sets that are of type Convex, Non-Convex and Sub-normal. (5 Marks)

## 1. Convex Fuzzy Set

A fuzzy set is **convex** if, for any two elements, all elements between them have membership values **greater than or equal to the minimum** of the two endpoints.

Example:

$$
A={0.2/1+0.5/2+1/3+0.5/4+0.2/5}
$$

Membership graph:

```text
μ(x)

1.0          /\
            /  \
0.5        /    \
          /      \
0 -------------------------
   1  2  3  4  5
```

**Property:** Membership increases to a peak and then decreases without forming valleys.

---

## 2. Non-Convex Fuzzy Set

A fuzzy set is **non-convex** if there is a dip (valley) between two higher membership values.

Example:

$$
B={0.8/1+0.2/2+0.9/3+0.3/4+0.8/5}
$$

Graph:

```text
μ(x)

1.0   /\      /\
     /  \    /  \
0-----------------------
   1  2  3  4  5
```

**Property:** Contains one or more valleys.

---

## 3. Sub-normal Fuzzy Set

A fuzzy set is **sub-normal** if its maximum membership value is **less than 1**.

Example:

$$
C={0.2/1+0.5/2+0.8/3+0.5/4+0.3/5}
$$

Maximum membership

$$
\max(\mu)=0.8<1
$$

Therefore,

$$
C
$$

is a **sub-normal fuzzy set**.

---

# Q2. Explain Dilation and Concentration Operations on Fuzzy Sets. (5 Marks)

## 1. Dilation

Dilation makes a fuzzy set **less specific (more spread out)** by increasing lower membership values.

Formula:

$$
\mu_D(x)=\sqrt{\mu(x)}
$$

Example:

Suppose

$$
\mu(x)=0.25
$$

Then

$$
\mu_D(x)=\sqrt{0.25}=0.5
$$

Thus, the membership value increases.

**Application:** Used when we want to make the fuzzy set broader.

---

## 2. Concentration

Concentration makes a fuzzy set **more specific (narrower)** by decreasing lower membership values.

Formula:

$$
\mu_C(x)=\left(\mu(x)\right)^2
$$

Example:

Suppose

$$
\mu(x)=0.5
$$

Then

$$
\mu_C(x)=0.5^2=0.25
$$

Thus, the membership value decreases.

**Application:** Used to emphasize elements with high membership.

---

## Difference

| Dilation                  | Concentration             |
| ------------------------- | ------------------------- |
| Broadens the fuzzy set    | Narrows the fuzzy set     |
| Uses square root          | Uses square               |
| Increases low memberships | Decreases low memberships |

---

# Q3. Why is Defuzzification Needed? Which Method Will You Use? (5 Marks)

## (a) Why Defuzzification is Needed? (2 Marks)

The output of a fuzzy inference system is a **fuzzy set**, but real-world systems require a **single crisp value** to control devices such as motors, fans, and air conditioners.

Therefore, **defuzzification** converts a fuzzy output into a crisp numerical value.

---

## (b) Given Fuzzy Set

$$
A={0.1/2+0.4/4+0.7/5+0.77/6+0.78/7+0.78/8+0.78/9+0.55/10}
$$

The maximum membership value is

$$
0.78
$$

It occurs at

$$
7,;8,;9
$$

---

### Mean-Max Method

The Mean-Max (Mean of Maximum) method takes the average of all values having the maximum membership.

$$
\frac{7+8+9}{3}
$$

$$
=8
$$

---

### Max Function Method

The Max Function selects **one** of the values with the highest membership (e.g., 7, 8, or 9). Since there are multiple maxima, it does not produce a unique result.

---

### Final Answer

The **Mean-Max Method** is preferred because there are **three values (7, 8, and 9)** with the same maximum membership value. It gives a unique and representative crisp value.

Therefore,

$$
\boxed{8}
$$

---

# Q4. State and Prove Bayes' Theorem. What is Marginalization? (5 Marks)

## (a) Bayes' Theorem (2 Marks)

### Statement

Bayes' theorem gives the conditional probability of an event based on prior knowledge.

Formula:

$$
P(A|B)=\frac{P(B|A),P(A)}{P(B)}
$$

where:

* $P(A|B)$ = Posterior probability
* $P(B|A)$ = Likelihood
* $P(A)$ = Prior probability
* $P(B)$ = Evidence

### Proof

From conditional probability,

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

Also,

$$
P(B|A)=\frac{P(A\cap B)}{P(A)}
$$

Therefore,

$$
P(A\cap B)=P(B|A),P(A)
$$

Substituting into the first equation,

$$
P(A|B)=\frac{P(B|A),P(A)}{P(B)}
$$

Hence proved.

---

## (b) Marginalization (3 Marks)

### Definition

Marginalization is the process of obtaining the probability of one variable by summing over the probabilities of another variable.

Formula:

$$
P(X)=\sum_Y P(X,Y)
$$

### Example

Suppose

| X | Y | P(X,Y) |
| - | - | ------ |
| A | 1 | 0.20   |
| A | 2 | 0.30   |

Then,

$$
P(A)=0.20+0.30=0.50
$$

Thus, we obtain the marginal probability of **A**.

---

# Q5. Create Two Fuzzy Relations and Verify Whether $$R\circ S=S\circ R$$ Using Max-Product Composition. (5 Marks)

Let

$$
R=
\begin{bmatrix}
0.2 & 0.8\\
0.6 & 0.4
\end{bmatrix}
$$

$$
S=
\begin{bmatrix}
0.5 & 0.7\\
0.9 & 0.3
\end{bmatrix}
$$

---

## Compute $$R\circ S$$

Max-product composition:

$$
(R\circ S)_{ij}
===============

\max_k
\left(R_{ik}\times S_{kj}\right)
$$

### First element

$$
\max(0.2\times0.5,;0.8\times0.9)
$$

$$
=\max(0.10,;0.72)
$$

$$
=0.72
$$

Similarly,

$$
R\circ S=
\begin{bmatrix}
0.72 & 0.24\
0.36 & 0.42
\end{bmatrix}
$$

---

## Compute $$S\circ R$$

$$
S\circ R=
\begin{bmatrix}
0.42 & 0.40\\
0.18 & 0.72
\end{bmatrix}
$$

---

## Comparison

Since

$$
R\circ S
\neq
S\circ R
$$

the statement

$$
R\circ S=S\circ R
$$

is **false**.

### Conclusion

**Max-product composition is generally not commutative**, i.e.,

$$
\boxed{R\circ S\neq S\circ R}
$$

---

