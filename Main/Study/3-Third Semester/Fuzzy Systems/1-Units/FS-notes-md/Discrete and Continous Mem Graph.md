#fuzzy-system #third-semester 

In fuzzy sets, the **membership graph** shows how the **membership value** ($\mu(x)$) changes for each element.

---

# 1. Discrete Membership Graph

Used when the universe of discourse contains **countable or separate values**.

Examples:

* Grades: {A, B, C, D}
* Days of the week
* Integer ages
* Number of cars

The graph consists of **individual points or vertical bars**.

### Example

Fuzzy set:

$$
A=\frac{0.2}{1}+\frac{0.5}{2}+\frac{1.0}{3}+\frac{0.7}{4}
$$

Graph:

```text
μ(x)

1.0 |           ●
0.8 |
0.6 |                  ●
0.4 |      ●
0.2 | ●
0.0 +--------------------------
      1     2     3     4     x
```

or

```text
μ(x)

1.0 |       |
0.8 |       |       |
0.6 |       |       |       |
0.4 |   |   |       |       |
0.2 | | |   |       |       |
0.0 +--------------------------
     1   2   3   4
```

**Characteristics**

* Separate values only.
* No line joining the points.
* Used for discrete fuzzy sets.

---

# 2. Continuous Membership Graph

Used when the universe contains **continuous values**.

Examples:

* Temperature
* Height
* Weight
* Speed

The membership function is drawn as a **continuous curve**.

### Example (Triangular Membership Function)

```text
μ(x)

1.0 |          /\
    |         /  \
0.5 |        /    \
    |       /      \
0.0 +------+--------+---------
      20    30      40      x
```

Here,

* Temperature = 20 → membership = 0
* Temperature = 30 → membership = 1
* Temperature = 40 → membership = 0

---

# Comparison

| Discrete Membership Graph | Continuous Membership Graph  |
| ------------------------- | ---------------------------- |
| Countable values          | Infinite values              |
| Individual points or bars | Continuous curve             |
| No joining of points      | Points are connected         |
| Example: Grades, Integers | Example: Temperature, Height |

### Exam Tip (2 Marks)

* **Discrete graph:** Draw **separate points/bars** for each element.
* **Continuous graph:** Draw a **smooth curve** (triangular, trapezoidal, Gaussian, etc.) over a continuous range of values.
