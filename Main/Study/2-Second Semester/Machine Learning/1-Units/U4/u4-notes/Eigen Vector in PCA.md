![](../../../../../../../Images/Second_Sem_Images/Eigen%20Vector%20in%20PCA.png)

To solve this, we need to find the **eigenvector** corresponding to the eigenvalue $\lambda$.

---

### 1. Substitute $\lambda$ into the Matrix

We substitute $\lambda$ for the eigenvalue in the equation

$$
(A - \lambda I)\mathbf{x} = 0
$$

This simplifies to

$$
(A - \lambda I)
\begin{bmatrix}
x \
y
\end{bmatrix}
=============

\begin{bmatrix}
0 \
0
\end{bmatrix}
$$

---

### 2. Set up the System of Equations

From the matrix multiplication, we get two equations (which should be linearly dependent):

1.

$$
a_{11}x + a_{12}y = 0
$$

2.

$$
a_{21}x + a_{22}y = 0
$$

Using the first equation to find the ratio between $x$ and $y$:

$$
a_{11}x = -a_{12}y
$$

$$
\frac{x}{y} = -\frac{a_{12}}{a_{11}}
$$

---

### 3. Determine the Eigenvector

Since eigenvectors are defined by their **direction**, not by a unique length, we can choose a convenient value.

* If we let $y = 1$, then

$$
x = -\frac{a_{12}}{a_{11}}
$$

So the eigenvector $\mathbf{v}$ is:

$$
\mathbf{v} =
\begin{bmatrix}
-\dfrac{a_{12}}{a_{11}} \
1
\end{bmatrix}
$$

(or any scalar multiple of this vector)

---

### Normalized Eigenvector (Optional)

If you need the **unit eigenvector**, divide by its magnitude:

$$
|\mathbf{v}| = \sqrt{x^2 + y^2}
$$

$$
\hat{\mathbf{v}} = \frac{1}{\sqrt{x^2 + y^2}}
\begin{bmatrix}
x \
y
\end{bmatrix}
$$

---
