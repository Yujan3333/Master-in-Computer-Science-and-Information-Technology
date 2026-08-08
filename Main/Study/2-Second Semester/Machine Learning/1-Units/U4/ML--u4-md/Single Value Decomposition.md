Single Value Decomposition (SVD) is a way to break any matrix into three very simple and meaningful parts.
For any matrix $A$, SVD says:

$$
A = U \Sigma V^T
$$

where:

* $U$ → left singular vectors (orthogonal matrix)
* $\Sigma$ → singular values (diagonal matrix)
* $V^T$ → right singular vectors (orthogonal matrix)

Think of it like this:

> A complicated transformation = rotation → scaling → rotation

---

### Intuition

Suppose $A$ takes a point and moves it in space.
SVD says:

1. First rotate the space using $V^T$
2. Then stretch or shrink along perpendicular directions using $\Sigma$
3. Then rotate again using $U$

So every matrix is just:
**rotation → scaling → rotation**

---

### Simple geometric picture

Imagine a unit circle:

* After applying $V^T$: still a circle, just rotated
* After applying $\Sigma$: becomes an ellipse (scaled along axes)
* After applying $U$: ellipse is rotated again

The lengths of the ellipse axes are the **singular values**.

---

### What are singular values?

They are the diagonal entries of $\Sigma$:

$$
\Sigma =
\begin{bmatrix}
\sigma_1 & 0 & 0 \
0 & \sigma_2 & 0 \
0 & 0 & \sigma_3
\end{bmatrix}
$$

with:

$$
\sigma_1 \ge \sigma_2 \ge \sigma_3 \ge 0
$$

They tell:

* How strongly the matrix stretches space
* Importance of each direction

Large $\sigma$ → important direction
Small $\sigma$ → less important direction

---

### Why is SVD so powerful?

Because it works for **any matrix**:

* Square / non-square
* Singular / non-singular
* Real-world noisy data

Applications:

| Area                   | Use                               |
| ---------------------- | --------------------------------- |
| Data compression       | Keep only largest singular values |
| Noise removal          | Drop small singular values        |
| PCA                    | SVD computes principal components |
| Image processing       | Image compression                 |
| Recommendation systems | Matrix factorization              |

---

### Small numeric example

Let

$$
A =
\begin{bmatrix}
3 & 0 \
0 & 1
\end{bmatrix}
$$

This is already diagonal, so:

$$
U = I, \quad \Sigma =
\begin{bmatrix}
3 & 0 \
0 & 1
\end{bmatrix}, \quad V^T = I
$$

So:

$$
A = U \Sigma V^T
$$

Here:

* No rotation
* Only scaling by 3 in $x$ direction and 1 in $y$ direction

---

### Slightly more interesting example

Let

$$
A =
\begin{bmatrix}
0 & 1 \
1 & 0
\end{bmatrix}
$$

This swaps coordinates. Its SVD is:

$$
U =
\begin{bmatrix}
1 & 0 \
0 & 1
\end{bmatrix},
\quad
\Sigma =
\begin{bmatrix}
1 & 0 \
0 & 1
\end{bmatrix},
\quad
V^T =
\begin{bmatrix}
0 & 1 \
1 & 0
\end{bmatrix}
$$

So it is:

* Pure rotation/reflection
* No scaling (all singular values = 1)

---

### Exam one-line definition

> “SVD factorizes any matrix $A$ as $A=U\Sigma V^T$, where $U$ and $V$ are orthogonal and $\Sigma$ contains singular values that represent the scaling effect of $A$.”

---
