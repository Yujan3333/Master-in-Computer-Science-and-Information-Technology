#ippr #third-semester 

# Laplacian Filter

## Definition

The **Laplacian Filter** is a **second-order derivative filter** used for **image sharpening** and **edge detection**. It detects regions where the intensity changes rapidly in all directions.

Unlike first-derivative filters (Prewitt, Sobel), the Laplacian responds equally to edges in all directions (**isotropic**).

---

# Mathematical Expression

For a continuous image,

$$
\nabla^2 f(x,y)=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}
$$

where

* $\nabla^2$ = Laplacian operator
* $f(x,y)$ = Image intensity

---

# Discrete Laplacian

For digital images,

$$
\nabla^2f(x,y)
=

f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)-4f(x,y)
$$

---

# Laplacian Masks

Two commonly used masks are:

### 4-Neighbour Laplacian

$$
\begin{bmatrix}
0 & -1 & 0\\
-1 & 4 & -1\\
0 & -1 & 0
\end{bmatrix}
$$

---

### 8-Neighbour Laplacian

$$
\begin{bmatrix}
-1 & -1 & -1\\
-1 & 8 & -1\\
-1 & -1 & -1
\end{bmatrix}
$$

Both masks detect intensity changes (edges).

---

# Image Sharpening Using Laplacian

The sharpened image is obtained by adding or subtracting the Laplacian from the original image.

If the mask has a **positive center**,

$$
g(x,y)=f(x,y)-\nabla^2f(x,y)
$$

If the mask has a **negative center**,

$$
g(x,y)=f(x,y)+\nabla^2f(x,y)
$$

---

# Example

Consider the image

$$
\begin{bmatrix}
10&10&10\\
10&50&10\\
10&10&10
\end{bmatrix}
$$

Using the 4-neighbour mask,

$$
\nabla^2f
=========

10+10+10+10-4(50)
$$

$$
=40-200
$$

$$
=-160
$$

The large magnitude indicates a sharp intensity change, i.e., an edge.

---

# Advantages

* Simple and fast.
* Detects edges in all directions.
* Effective for image sharpening.
* Rotationally invariant (isotropic).

---

# Disadvantages

* Very sensitive to noise.
* Does not provide edge direction.
* Usually combined with smoothing filters to reduce noise.

---

# Applications

* Edge detection
* Image sharpening
* Medical image processing
* Satellite image enhancement
* Computer vision

---

# Difference Between First Derivative and Laplacian Filter

| First Derivative Filter                     | Laplacian Filter                             |
| ------------------------------------------- | -------------------------------------------- |
| Uses the **first derivative** of intensity. | Uses the **second derivative** of intensity. |
| Detects edge direction.                     | Does not indicate edge direction.            |
| Examples: Sobel, Prewitt.                   | Example: Laplacian operator.                 |
| Less sensitive to noise.                    | More sensitive to noise.                     |

---

# Exam Answer (5 Marks)

**Definition:**
The **Laplacian Filter** is a **second-order derivative filter** used for **edge detection** and **image sharpening**. It highlights regions of rapid intensity change and responds equally to edges in all directions.

The Laplacian operator is

$$
\nabla^2 f(x,y)=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}
$$

For digital images,

$$
\nabla^2f(x,y)
=

f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)-4f(x,y)
$$

Common masks:

**4-Neighbour**

$$
\begin{bmatrix}
0 & -1 & 0\\
-1 & 4 & -1\\
0 & -1 & 0
\end{bmatrix}
$$

**8-Neighbour**

$$
\begin{bmatrix}
-1 & -1 & -1\\
-1 & 8 & -1\\
-1 & -1 & -1
\end{bmatrix}
$$

The sharpened image is obtained using

$$
g(x,y)=f(x,y)-\nabla^2f(x,y)
$$

The Laplacian filter is widely used for **edge detection, image sharpening, and feature extraction**.
