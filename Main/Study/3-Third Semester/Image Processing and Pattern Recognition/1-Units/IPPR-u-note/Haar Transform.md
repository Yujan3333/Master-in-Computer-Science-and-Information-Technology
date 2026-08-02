#ippr #third-semester 

# Explain the Haar Transform and derive the Haar Matrix for (N=4). **[3+7 Marks]**

---

# (a) Haar Transform (3 Marks)

## Definition

The **Haar Transform** is the **simplest orthogonal wavelet transform** used in digital image processing. It decomposes an image or signal into **average (low-frequency)** and **difference (high-frequency)** components.

It is mainly used for:

* Image compression
* Image enhancement
* Noise reduction
* Feature extraction
* Pattern recognition

The Haar transform is computationally simple because it uses only **addition and subtraction**.

---

## Working Principle

The Haar transform processes the input data in pairs.

For every pair of values:

* Compute the **average**.
* Compute the **difference**.

These averages and differences form the transformed signal.

For two values $a$ and $b$,

Average:

$$
\frac{a+b}{2}
$$

Difference:

$$
\frac{a-b}{2}
$$

Thus, the transform separates low-frequency (average) information from high-frequency (detail) information.

---

## Advantages

* Very simple to compute.
* Fast computation.
* Good for image compression.
* Orthogonal transform.
* Easy inverse transformation.

---

# (b) Derive the Haar Matrix for (N=4) (7 Marks)

The Haar matrix is constructed row by row.

---

## Step 1: First Row (Average)

The first row represents the average of all four elements.

$$
\left[\frac12,\frac12,\frac12,\frac12\right]
$$

---

## Step 2: Second Row

Split the signal into two halves.

Assign positive values to the first half and negative values to the second half.

$$
\left[\frac12,\frac12,-\frac12,-\frac12\right]
$$

---

## Step 3: Third Row

Split the first half again.

$$
\left[\frac{1}{\sqrt2},-\frac{1}{\sqrt2},0,0\right]
$$

---

## Step 4: Fourth Row

Split the second half.

$$
\left[0,0,\frac{1}{\sqrt2},-\frac{1}{\sqrt2}\right]
$$

---

## Haar Matrix for (N=4)

Combining all rows,

$$
H_4=
\begin{bmatrix}
\frac12 & \frac12 & \frac12 & \frac12\\
\frac12 & \frac12 & -\frac12 & -\frac12\\
\frac1{\sqrt2} & -\frac1{\sqrt2} & 0 & 0\\
0 & 0 & \frac1{\sqrt2} & -\frac1{\sqrt2}
\end{bmatrix}
$$

This is the required **Haar matrix of order 4**.

---

## Orthogonality Property

The Haar matrix is **orthogonal**, which means

$$
H_4H_4^T=I
$$

where

* $H_4^T$ = Transpose of Haar matrix
* $I$ = Identity matrix

Therefore,

$$
H_4^{-1}=H_4^T
$$

This makes reconstruction of the original image very easy.

---

## Haar Transform of a Vector

If

$$
X=
\begin{bmatrix}
x_1\\
x_2\\
x_3\\
x_4
\end{bmatrix},
$$

then the transformed vector is

$$
Y=H_4X.
$$

---

## Applications

* JPEG2000 image compression
* Image denoising
* Medical image processing
* Pattern recognition
* Feature extraction
* Signal processing

---

# Exam Answer (3+7 Marks)

### (a) Haar Transform (3 Marks)

The **Haar Transform** is the simplest orthogonal wavelet transform used to convert an image from the spatial domain into average and detail components. It computes averages and differences of neighboring pixels and is widely used in **image compression, enhancement, denoising, and feature extraction**.

For two values $a$ and $b$,

Average:

$$
\frac{a+b}{2}
$$

Difference:

$$
\frac{a-b}{2}
$$

---

### (b) Haar Matrix for (N=4) (7 Marks)

The Haar matrix is

$$
H_4=
\begin{bmatrix}
\frac12 & \frac12 & \frac12 & \frac12\\
\frac12 & \frac12 & -\frac12 & -\frac12\\
\frac1{\sqrt2} & -\frac1{\sqrt2} & 0 & 0\\
0 & 0 & \frac1{\sqrt2} & -\frac1{\sqrt2}
\end{bmatrix}
$$

It satisfies the orthogonality condition

$$
H_4H_4^T=I,
$$

hence

$$
H_4^{-1}=H_4^T.
$$

The Haar transform is widely used because it is **simple, fast, orthogonal, and efficient for image compression and image enhancement**.
