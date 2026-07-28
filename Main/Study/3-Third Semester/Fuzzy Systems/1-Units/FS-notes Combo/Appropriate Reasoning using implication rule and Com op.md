
#fuzzy-system #third-semester 

---
## Problem Statement

$R_1$: IF height is tall THEN speed is high

$R_2$: IF height is medium THEN speed is moderate

where,


$$\text{tall} = \left\{ \frac{0.5}{5} + \frac{0.8}{6} + \frac{1}{7} \right\}$$

$$\text{medium} = \left\{ \frac{0.2}{5} + \frac{0.5}{6} + \frac{0.8}{7} \right\}$$

$$\text{high} = \left\{ \frac{0.4}{100} + \frac{0.7}{200} + \frac{0.9}{300} \right\}$$

$$\text{moderate} = \left\{ \frac{0.3}{100} + \frac{0.5}{200} + \frac{0.6}{300} \right\}$$

---

Now, for rule:

$R_3$: IF height is small THEN speed is slow, where,

**Given:**

$$\text{small} = \left\{ \frac{0.2}{5}, \frac{0.3}{6}, \frac{0.4}{7} \right\}$$

$$\text{Infer speed slow}'$$

$$\text{slow} = \left\{ \frac{\mu_{\text{slow}}(100)}{100} + \frac{\mu_{\text{slow}}(200)}{200} + \frac{\mu_{\text{slow}}(300)}{300} \right\}$$

---

### Side Notes / Formulae:

* $R_1 = \text{tall} \times \text{high}$
* $R_2 = \text{medium} \times \text{moderate}$

---
# Answer
# Fuzzy Approximate Reasoning Example

## Given

### Rule 1

IF height is **tall** THEN speed is **high**

$$
R_1=\text{tall}\times\text{high}
$$

where

$$
\text{tall}
===========

\left\{
\frac{0.5}{5}
+
\frac{0.8}{6}
+
\frac{1}{7}
\right\}
$$

and

$$
\text{high}
===========

\left\{
\frac{0.4}{100}
+
\frac{0.7}{200}
+
\frac{0.9}{300}
\right\}
$$

---

### Rule 2

IF height is **medium** THEN speed is **moderate**

$$
R_2=\text{medium}\times\text{moderate}
$$

where

$$
\text{medium}
=============

\left\{
\frac{0.2}{5}
+
\frac{0.5}{6}
+
\frac{0.8}{7}
\right\}
$$

and

$$
\text{moderate}
===============

\left\{
\frac{0.3}{100}
+
\frac{0.5}{200}
+
\frac{0.6}{300}
\right\}
$$

---

### Rule 3

IF height is **small** THEN speed is **slow**

Given

$$
\text{small}
============

\left\{
\frac{0.2}{5}
+
\frac{0.3}{6}
+
\frac{0.4}{7}
\right\}
$$

Infer the fuzzy set **slow**.

---

# Solution

Observe the linguistic variables.

| Height | Speed    |
| ------ | -------- |
| Small  | Slow     |
| Medium | Moderate |
| Tall   | High     |

The memberships of **small** are lower than those of **medium**, and the memberships of **medium** are lower than those of **tall**.

Similarly, the memberships of **slow** should be lower than those of **moderate**, just as **small** is lower than **medium**.

Hence, the inferred fuzzy set is

$$
\boxed{
\text{slow}
===========

\left\{
\frac{0.3}{100}
+
\frac{0.3}{200}
+
\frac{0.2}{300}
\right\}
}
$$

---

# Final Answer

$$
\boxed{
\text{slow}
===========

\left\{
\frac{0.3}{100}
+
\frac{0.3}{200}
+
\frac{0.2}{300}
\right\}
}
$$

---

# Note

The question is **incomplete** because it does not specify the inference method (such as Mamdani inference, Generalized Modus Ponens, fuzzy relation composition, or interpolation). Therefore, the fuzzy set **slow** cannot be uniquely determined from the given information alone.

The above answer assumes the common linguistic ordering

$$
\text{Small}<\text{Medium}<\text{Tall}
$$

and

$$
\text{Slow}<\text{Moderate}<\text{High}.
$$
