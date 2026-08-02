#ippr #third-semester 

# Explain the Laplacian Filter with an Example. Derive the Filter Mask for Hyperbolic Filter and Write the Algorithm for its Implementation. **[2+6+2]**

---

# 1. Laplacian Filter (2 Marks)

## Definition

The **Laplacian filter** is a **second-order derivative operator** used for image sharpening and edge detection. It detects regions where the image intensity changes rapidly.

The continuous Laplacian is defined as

$$
\nabla^2 f(x,y)=\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2}
$$

### Common Laplacian Masks

4-neighbour mask

$$
\begin{bmatrix}
0 & -1 & 0 \\
-1 & 4 & -1 \\
0 & -1 & 0
\end{bmatrix}
$$

8-neighbour mask

$$
\begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1
\end{bmatrix}
$$

### Example

Original image

$$
\begin{bmatrix}
10 & 10 & 10 \\
10 & 50 & 10 \\
10 & 10 & 10
\end{bmatrix}
$$

Applying the 4-neighbour Laplacian mask,

$$
(4\times50)-(10+10+10+10)=160
$$

The large positive value indicates the presence of an edge.

---

# 2. Hyperbolic Filter Mask (6 Marks)

## Definition

A **Hyperbolic filter** is a sharpening filter obtained by modifying the Laplacian operator so that the center pixel is emphasized while the neighboring pixels are subtracted. It enhances edges and fine details.

### Derivation

Using the discrete approximation of the Laplacian,

$$
\nabla^2f(x,y)
=

4f(x,y)
-\left[
f(x+1,y)
+
f(x-1,y)
+
f(x,y+1)
+
f(x,y-1)
\right]
$$

To sharpen the image,

$$
g(x,y)=f(x,y)-\nabla^2f(x,y)
$$

Substituting the Laplacian,

$$
g(x,y)
======

 5f(x,y)

\left[
f(x+1,y)
+
f(x-1,y)
+
f(x,y+1)
+
f(x,y-1)
\right]
$$

Hence, the corresponding **Hyperbolic filter mask** is

$$
\boxed{
\begin{bmatrix}
0 & -1 & 0 \\
-1 & 5 & -1 \\
0 & -1 & 0
\end{bmatrix}
}
$$

Another commonly used form is

$$
\boxed{
\begin{bmatrix}
-1 & -1 & -1 \\
-1 & 9 & -1 \\
-1 & -1 & -1
\end{bmatrix}
}
$$

Both masks enhance edges by increasing the weight of the center pixel while subtracting neighboring pixels.

---

# 3. Algorithm for Hyperbolic Filter (2 Marks)

**Algorithm**

1. Read the input image.
2. Select the hyperbolic filter mask.
3. Move the mask over the image using convolution.
4. Multiply corresponding pixels with the mask coefficients.
5. Sum the products to obtain the new pixel value.
6. Replace the center pixel with the computed value.
7. Repeat the process for all pixels.
8. Display the sharpened image.

---

# Advantages

* Enhances edges and fine details.
* Improves image sharpness.
* Simple to implement.

---

# Disadvantages

* Amplifies image noise.
* May produce oversharpening if applied repeatedly.

---

# Exam Tips

### Laplacian

* Second-order derivative.
* Used for edge detection and sharpening.
* Common masks: center value **4** or **8**.

### Hyperbolic Filter

* Derived from the Laplacian.
* Used for image sharpening.
* Common mask:

$$
\boxed{
\begin{bmatrix}
0 & -1 & 0 \\
-1 & 5 & -1 \\
0 & -1 & 0
\end{bmatrix}
}
$$

### One-Line Difference

* **Laplacian Filter:** Detects edges using the second derivative.
* **Hyperbolic Filter:** Sharpens the image by adding the Laplacian effect back to the original image.
