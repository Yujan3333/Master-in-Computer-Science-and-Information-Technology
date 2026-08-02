#ippr #third-semester 
# Laplacian Filter vs Sobel Filter vs Prewitt Filter

These are three of the most commonly used **edge detection filters** in Digital Image Processing. Their primary difference lies in **how they detect image edges**.

---

## Comparison

| Feature                  | **Laplacian Filter**            | **Sobel Filter**                      | **Prewitt Filter**                    |
| ------------------------ | ------------------------------- | ------------------------------------- | ------------------------------------- |
| Derivative Used          | Second-order derivative         | First-order derivative                | First-order derivative                |
| Edge Detection           | Detects edges in all directions | Detects horizontal and vertical edges | Detects horizontal and vertical edges |
| Edge Direction           | ❌ Not provided                  | ✅ Provided                            | ✅ Provided                            |
| Noise Sensitivity        | High                            | Low                                   | Moderate                              |
| Smoothing                | No                              | Yes (weighted smoothing)              | Very little smoothing                 |
| Accuracy                 | High but sensitive to noise     | More accurate than Prewitt            | Less accurate than Sobel              |
| Computational Complexity | Simple                          | Moderate                              | Simple                                |

---

# 1. Laplacian Filter

## Definition

The **Laplacian filter** is a **second-order derivative operator** that detects regions of rapid intensity change (edges). Since it computes the second derivative, it responds strongly to fine details and noise.

### Common Kernels

$$
\begin{bmatrix}
0 & -1 & 0 \\
-1 & 4 & -1 \\
0 & -1 & 0
\end{bmatrix}
$$

or

$$
\begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1
\end{bmatrix}
$$

### Characteristics

* Uses the **second-order derivative**.
* Detects edges in **all directions**.
* Does **not** provide edge orientation.
* Highly sensitive to noise.

### Advantages

* Simple to implement.
* Detects fine image details.
* Rotation invariant.

### Disadvantages

* Amplifies noise.
* Usually applied after image smoothing (e.g., Gaussian filtering).

---

# 2. Sobel Filter

## Definition

The **Sobel filter** is a **first-order gradient operator** that estimates image gradients in the horizontal and vertical directions. It also performs slight smoothing, making it more robust to noise.

### Horizontal Kernel ($G_x$)

$$
\begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}
$$

### Vertical Kernel ($G_y$)

$$
\begin{bmatrix}
-1 & -2 & -1 \\
0 & 0 & 0 \\
1 & 2 & 1
\end{bmatrix}
$$

### Gradient Magnitude

$$
G=\sqrt{G_x^2+G_y^2}
$$

Approximation:

$$
G \approx |G_x|+|G_y|
$$

### Characteristics

* Uses the **first-order derivative**.
* Detects horizontal and vertical edges.
* Performs weighted smoothing due to the coefficient **2**.

### Advantages

* Less sensitive to noise.
* Provides edge direction.
* Widely used.

### Disadvantages

* Slightly more computationally expensive than Prewitt.
* May miss extremely fine edges.

---

# 3. Prewitt Filter

## Definition

The **Prewitt filter** is another **first-order gradient operator** used for detecting horizontal and vertical edges. Unlike Sobel, it uses equal weights throughout the kernel.

### Horizontal Kernel ($G_x$)

$$
\begin{bmatrix}
-1 & 0 & 1 \\
-1 & 0 & 1 \\
-1 & 0 & 1
\end{bmatrix}
$$

### Vertical Kernel ($G_y$)

$$
\begin{bmatrix}
-1 & -1 & -1 \\
0 & 0 & 0 \\
1 & 1 & 1
\end{bmatrix}
$$

### Characteristics

* Uses the **first-order derivative**.
* Detects horizontal and vertical edges.
* Uses equal weights (no weighted smoothing).

### Advantages

* Easy to implement.
* Computationally efficient.

### Disadvantages

* More sensitive to noise than Sobel.
* Less accurate because it lacks weighted smoothing.

---

# Sobel vs Prewitt

| **Sobel**                | **Prewitt**                    |
| ------------------------ | ------------------------------ |
| Center weight is **2**   | All non-zero weights are **1** |
| Better noise suppression | Less noise suppression         |
| More accurate            | Less accurate                  |
| More commonly used       | Simpler implementation         |

---

# Laplacian vs Sobel

| **Laplacian**                   | **Sobel**                             |
| ------------------------------- | ------------------------------------- |
| Second-order derivative         | First-order derivative                |
| Detects edges in all directions | Detects horizontal and vertical edges |
| Does not provide edge direction | Provides edge direction               |
| Highly sensitive to noise       | Less sensitive to noise               |

---

# Memory Tricks

### Laplacian

* **L = Looks in all directions**
* **L = Second-order derivative**
* **L = Loves noise (highly sensitive)**

### Sobel

* **S = Smooth + Strong**
* Center weight = **2**
* Better noise suppression than Prewitt.

### Prewitt

* **P = Plain**
* All weights = **1**
* Simpler but less accurate.

---

# Exam Summary

Remember these three key differences:

### 1. Derivative Used

* **Laplacian:** Second-order derivative
* **Sobel:** First-order derivative
* **Prewitt:** First-order derivative

### 2. Noise Sensitivity

* **Laplacian:** High
* **Sobel:** Low
* **Prewitt:** Moderate

### 3. Kernel Characteristics

* **Laplacian:** Center surrounded by negative values (e.g., $4$ or $8$ at the center).
* **Sobel:** Center row/column has weight **2**, providing smoothing.
* **Prewitt:** All non-zero weights are **1**, making it simpler but more noise-sensitive.
