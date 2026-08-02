#ippr #third-semester 

This is a common **Hadamard Transform** theory question. The key idea is that **sequency order is obtained by counting sign changes** in each row of the Hadamard matrix.

---

# How do you determine sequency in Hadamard transform from the natural order?

## Definition

**Sequency** is the **number of sign changes (+ ↔ −)** in a row of the Hadamard matrix.

* **Natural order:** Rows are arranged by recursive construction.
* **Sequency order:** Rows are rearranged in **increasing number of sign changes**.

Thus,

> **Sequency = Number of sign changes in a row.**

---

# Steps to Determine Sequency

1. Write the Hadamard matrix in **natural order**.
2. Count the number of sign changes in each row (ignore the wrap-around from last to first element).
3. Assign the sequency value equal to the number of sign changes.
4. Rearrange the rows from **lowest sequency to highest sequency**.

---

# Example (4 × 4 Hadamard Matrix)

Natural-order Hadamard matrix:

$$[
H_4=
\begin{bmatrix}
+&+&+&+\\
+&-&+&-\\
+&+&-&-\\
+&-&-&+
\end{bmatrix}
]$$

Now count the sign changes.

| Row | Pattern | Sign Changes | Sequency |
| --- | ------- | -----------: | -------: |
| 1   | + + + + |            0 |        0 |
| 2   | + − + − |            3 |        3 |
| 3   | + + − − |            1 |        1 |
| 4   | + − − + |            2 |        2 |

---

# Rearrange by Sequency

Arrange rows in the order:

```text
0 → 1 → 2 → 3
```

So the sequency-ordered matrix becomes

$$[
\begin{bmatrix}
+&+&+&+\\
+&+&-&-\\
+&-&-&+\\
+&-&+&-
\end{bmatrix}
]$$

---

# Another Small Example (8-Point Row)

Consider the row

```text
+ + − − + + − −
```

Count the changes:

```text
+ → +   (0)
+ → −   (1)
− → −   (1)
− → +   (2)
+ → +   (2)
+ → −   (3)
− → −   (3)
```

Total sign changes = **3**

Therefore,

**Sequency = 3**

---

# Exam Answer (5 Marks)

**Definition:** Sequency is the number of sign changes between consecutive elements in a row of the Hadamard matrix. The Hadamard matrix generated in natural order is converted to sequency order by counting the sign changes in each row and then rearranging the rows in ascending order of sign changes.

**Example:**

Natural-order matrix:

$$[
\begin{bmatrix}
+&+&+&+\\
+&-&+&-\\
+&+&-&-\\
+&-&-&+
\end{bmatrix}
]$$

| Row     | Sign Changes | Sequency |
| ------- | ------------ | -------- |
| + + + + | 0            | 0        |
| + − + − | 3            | 3        |
| + + − − | 1            | 1        |
| + − − + | 2            | 2        |

Rearranging the rows according to sequency (0,1,2,3) gives the **sequency-ordered Hadamard matrix**.

---

### Exam Tip

Many books mention **Gray code** because it provides an efficient way to generate the sequency ordering directly. However, if the exam asks **"How do you determine sequency from the natural order?"**, the expected method is simply:

1. Count the sign changes in each row.
2. Rearrange the rows in increasing order of sign changes.

This is the simplest and most commonly accepted answer in Digital Image Processing exams.
