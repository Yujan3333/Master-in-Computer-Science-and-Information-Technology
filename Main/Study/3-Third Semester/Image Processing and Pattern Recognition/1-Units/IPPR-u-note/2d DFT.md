#ippr #third-semester #exam-paper-answer 

# Question 5

## What is 2D Discrete Fourier Transform (2D DFT)? Explain.

---

# Introduction

The **Two-Dimensional Discrete Fourier Transform (2D DFT)** is a mathematical transformation that converts a **2D digital image** from the **spatial domain** into the **frequency domain**.

Instead of representing an image by its pixel intensities, the 2D DFT represents it as a combination of **sinusoidal frequency components**.

The frequency-domain representation tells us **how rapidly the intensity changes** across the image.

---

# Why Do We Need 2D DFT?

In the spatial domain, it is difficult to perform operations such as:

* Noise removal
* Image smoothing
* Image sharpening
* Frequency analysis

The 2D DFT transforms the image into the frequency domain, where these operations become easier.

---

# Mathematical Expression

Let

$$
f(x,y)
$$

be an image of size

$$
M \times N
$$

The **2D Discrete Fourier Transform** is defined as

$$
F(u,v)=
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
f(x,y)
e^{-j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

where

* $f(x,y)$ = Image in the spatial domain
* $F(u,v)$ = Frequency-domain representation
* $M,N$ = Image dimensions
* $u,v$ = Frequency coordinates
* $j=\sqrt{-1}$

---

# Inverse 2D DFT

The original image is recovered using the inverse transform.

$$
f(x,y)=
\frac{1}{MN}
\sum_{u=0}^{M-1}
\sum_{v=0}^{N-1}
F(u,v)
e^{j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

---

# Meaning of the Variables

| Symbol   | Meaning                    |
| -------- | -------------------------- |
| $f(x,y)$ | Input image                |
| $F(u,v)$ | Frequency spectrum         |
| $x,y$    | Spatial coordinates        |
| $u,v$    | Frequency coordinates      |
| $M,N$    | Number of rows and columns |
| $j$      | Imaginary unit             |

---

# Frequency Components

The Fourier transform decomposes an image into two types of frequency components.

### Low Frequencies

Represent

* Smooth regions
* Slowly changing intensities
* Overall brightness

They are located **near the center** of the frequency spectrum (after centering).

---

### High Frequencies

Represent

* Edges
* Fine details
* Noise
* Sudden intensity changes

They are located **towards the corners** of the frequency spectrum (after centering, they appear away from the center).

---

# Frequency Spectrum

```text
+---------------------------+
| High | High | High | High |
|-------+------+------|------|
| High | Low  | Low  | High |
|-------+------+------|------|
| High | Low  | Low  | High |
|-------+------+------|------|
| High | High | High | High |
+---------------------------+
```

After multiplying the image by

$$
(-1)^{x+y}
$$

before computing the DFT, the **zero-frequency (DC) component** is shifted to the center of the spectrum, making it easier to analyze and apply frequency-domain filters.

---

# Properties of 2D DFT

### 1. Linearity

The Fourier transform of the sum of two images equals the sum of their Fourier transforms.

$$
DFT{af+bg}
==========

aF+bG
$$

---

### 2. Periodicity

Both the image and its Fourier transform are periodic with periods

$$
M
\quad\text{and}\quad
N.
$$

---

### 3. Symmetry

For a real-valued image,

$$
F(-u,-v)=F^*(u,v)
$$

where

$$
F^*
$$

is the complex conjugate.

---

### 4. Translation Property

Shifting an image in the spatial domain changes only the phase of its Fourier transform; the magnitude remains unchanged.

---

### 5. Convolution Property

Convolution in the spatial domain becomes multiplication in the frequency domain.

$$
f(x,y)*g(x,y)
\Longleftrightarrow
F(u,v),G(u,v)
$$

This property makes frequency-domain filtering efficient.

---

# Advantages

* Simplifies frequency-domain filtering.
* Separates low- and high-frequency components.
* Useful for image enhancement and restoration.
* Enables efficient processing using FFT.
* Supports frequency analysis.

---

# Disadvantages

* Computationally expensive if computed directly.
* Produces complex-valued output.
* Does not indicate the exact spatial location of frequency components.

---

# Applications

* Image smoothing
* Image sharpening
* Noise removal
* Edge detection
* Image restoration
* Image compression
* Medical image processing
* Satellite image analysis

---

# Difference Between 1D DFT and 2D DFT

| 1D DFT                                | 2D DFT                                 |
| ------------------------------------- | -------------------------------------- |
| Used for one-dimensional signals      | Used for two-dimensional images        |
| One summation                         | Two summations                         |
| Frequency represented by one variable | Frequency represented by two variables |
| Used in audio and signal processing   | Used in image processing               |

---

# Exam Answer (5 Marks)

The **Two-Dimensional Discrete Fourier Transform (2D DFT)** converts a digital image from the **spatial domain** into the **frequency domain**, where the image is represented by its frequency components. It is widely used for image enhancement, filtering, restoration, and compression.

The forward transform is

$$
F(u,v)=
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
f(x,y)
e^{-j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

The inverse transform is

$$
f(x,y)=
\frac{1}{MN}
\sum_{u=0}^{M-1}
\sum_{v=0}^{N-1}
F(u,v)
e^{j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

**Applications:**

* Image smoothing
* Image sharpening
* Noise removal
* Edge detection
* Image restoration
* Image compression

> **Exam Tip:** You should **memorize both the forward and inverse 2D DFT equations**. Questions often ask for the definition, formulas, and applications together (e.g., "What is 2D DFT? Explain with equations and uses.").
