#ippr #third-semester #exam-paper-answer 

# Question 6

## What is the difference between Spatial Correlation and Spatial Convolution?

---

# Introduction

Both **spatial correlation** and **spatial convolution** are neighborhood operations used in **spatial-domain image processing**.

In both operations, a small matrix called a **kernel**, **mask**, or **filter** slides over the image and computes a new pixel value.

The **main difference** is that:

* **Correlation** uses the mask **as it is**.
* **Convolution** first **rotates the mask by $180^\circ$** before applying it.

---

# 1. Spatial Correlation

## Definition

**Spatial correlation** is an operation in which the filter mask is moved over the image **without changing its orientation**.

Each output pixel is obtained by multiplying the overlapping pixels with the corresponding mask coefficients and summing the results.

---

## Mathematical Formula

Let

* Image = $f(x,y)$
* Mask = $w(s,t)$

The correlation is

$$
g(x,y)=
\sum_{s=-a}^{a}
\sum_{t=-b}^{b}
w(s,t),
f(x+s,y+t)
$$

where

* $g(x,y)$ = Output image
* $w(s,t)$ = Filter mask
* $f(x+s,y+t)$ = Neighborhood pixels

---

## Correlation Process

Original mask

$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix}
$$

During correlation, the mask is used **exactly as it is**.

```text
Image
   │
   ▼
Mask (No Rotation)
   │
Multiply
   │
Sum
   │
Output
```

---

# 2. Spatial Convolution

## Definition

**Spatial convolution** is similar to correlation, except that **the mask is rotated by $180^\circ$** before it is applied to the image.

---

## Mathematical Formula

The convolution operation is

$$
g(x,y)=
\sum_{s=-a}^{a}
\sum_{t=-b}^{b}
w(s,t),
f(x-s,y-t)
$$

Notice the negative signs in the indices, which correspond to flipping the kernel.

---

## Mask Rotation

Original mask

$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix}
$$

Rotate by $180^\circ$

$$
\begin{bmatrix}
9 & 8 & 7\\
6 & 5 & 4\\
3 & 2 & 1
\end{bmatrix}
$$

This rotated mask is then applied to the image.

---

## Convolution Process

```text
Image
   │
   ▼
Rotate Mask by 180°
   │
Multiply
   │
Sum
   │
Output
```

---

# Why Rotate the Mask?

Convolution is defined mathematically with a flipped kernel. This property ensures important theoretical results, such as:

* Associativity
* Commutativity
* The **Convolution Theorem**, which states that convolution in the spatial domain corresponds to multiplication in the frequency domain.

Because of these properties, convolution is the standard operation used in image filtering.

---

# Example

Suppose the mask is

$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix}
$$

### Correlation

The same mask is applied:

$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix}
$$

---

### Convolution

First rotate the mask:

$$
\begin{bmatrix}
9 & 8 & 7\\
6 & 5 & 4\\
3 & 2 & 1
\end{bmatrix}
$$

Then perform the multiplication and summation.

---

# When Are the Results the Same?

If the mask is **symmetric**, correlation and convolution produce identical results.

Example:

$$
\begin{bmatrix}
1 & 2 & 1\\
2 & 4 & 2\\
1 & 2 & 1
\end{bmatrix}
$$

Rotating this mask by $180^\circ$ gives the same mask.

Therefore,

$$
\text{Correlation}=\text{Convolution}
$$

Examples include:

* Mean filter
* Gaussian filter
* Weighted averaging filter

---

# When Are the Results Different?

If the mask is **asymmetric**, correlation and convolution produce different outputs.

Example:

$$
\begin{bmatrix}
-1 & 0 & 1\\
-2 & 0 & 2\\
-1 & 0 & 1
\end{bmatrix}
$$

This is the **Sobel operator**. Rotating it changes the mask, so correlation and convolution give different results.

---

# Applications

## Correlation

* Template matching
* Pattern recognition
* Feature matching
* Image registration

---

## Convolution

* Image smoothing
* Image sharpening
* Edge detection
* Noise removal
* Frequency-domain filtering

---

# Advantages

### Correlation

* Simpler computation
* Useful for measuring similarity
* Widely used in template matching

### Convolution

* Mathematically well-defined
* Used by most image filters
* Satisfies important mathematical properties
* Standard operation in digital image processing

---

# Difference Between Correlation and Convolution

| Spatial Correlation                     | Spatial Convolution                            |
| --------------------------------------- | ---------------------------------------------- |
| Mask is **not rotated**                 | Mask is rotated by **$180^\circ$**             |
| Original kernel is used                 | Flipped kernel is used                         |
| Formula uses $f(x+s,y+t)$               | Formula uses $f(x-s,y-t)$                      |
| Mainly measures similarity              | Mainly performs filtering                      |
| Used for template matching              | Used for smoothing, sharpening, edge detection |
| Results differ for asymmetric masks     | Results differ for asymmetric masks            |
| Same as convolution for symmetric masks | Same as correlation for symmetric masks        |

---

# Memory Trick

**Correlation**

```text
No Rotation
↓
Use Mask Directly
```

**Convolution**

```text
Rotate 180°
↓
Then Apply
```

---

# Exam Answer (5 Marks)

**Spatial Correlation** is a neighborhood operation in which the filter mask is applied directly to the image without changing its orientation.

$$
g(x,y)=
\sum_{s=-a}^{a}
\sum_{t=-b}^{b}
w(s,t),f(x+s,y+t)
$$

**Spatial Convolution** is a neighborhood operation in which the filter mask is first rotated by **$180^\circ$** and then applied to the image.

$$
g(x,y)=
\sum_{s=-a}^{a}
\sum_{t=-b}^{b}
w(s,t),f(x-s,y-t)
$$

### Differences

| Correlation                                    | Convolution                                    |
| ---------------------------------------------- | ---------------------------------------------- |
| No mask rotation                               | Mask rotated by $180^\circ$                    |
| Used for similarity measurement                | Used for image filtering                       |
| Original kernel                                | Flipped kernel                                 |
| Template matching                              | Smoothing, sharpening, edge detection          |
| Same result as convolution for symmetric masks | Same result as correlation for symmetric masks |

> **Exam Tip:** The most frequently tested point is: **"Convolution = Correlation + 180° rotation of the kernel."** Always mention this in your answer.
