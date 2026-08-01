#ippr #third-semester 
# Discrete Fourier Transform (DFT)

## Definition

The **Discrete Fourier Transform (DFT)** is a mathematical technique used to convert a **discrete signal or digital image** from the **spatial domain** into the **frequency domain**.

It decomposes an image into its **frequency components**, showing how much of each frequency is present.

---

# Why is DFT Used?

In image processing, working in the frequency domain makes many operations easier.

DFT is used for:

* Image enhancement
* Noise removal
* Image smoothing (Low Pass Filters)
* Image sharpening (High Pass Filters)
* Edge detection
* Image restoration
* Image compression

---

# Basic Idea

Suppose an image consists of smooth areas and sharp edges.

* **Smooth areas** correspond to **low frequencies**.
* **Edges and fine details** correspond to **high frequencies**.

The DFT separates these components.

```text
Spatial Domain (Pixels)
        │
        ▼
      DFT
        │
        ▼
Frequency Domain
(Low + High Frequencies)
```

---

# 1D Discrete Fourier Transform

For a one-dimensional signal,

$$
F(u)=\sum_{x=0}^{N-1}f(x)e^{-j\frac{2\pi ux}{N}}
$$

where

* $f(x)$ = Input signal
* $F(u)$ = Frequency-domain representation
* $N$ = Number of samples
* $j=\sqrt{-1}$

---

# 2D Discrete Fourier Transform

For a digital image,

$$
F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f(x,y)e^{-j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

where

* $f(x,y)$ = Image in the spatial domain
* $F(u,v)$ = Frequency-domain representation
* $M,N$ = Image dimensions

---

# Inverse DFT (IDFT)

The inverse transform converts the frequency-domain image back into the spatial domain.

$$
f(x,y)=\frac{1}{MN}\sum_{u=0}^{M-1}\sum_{v=0}^{N-1}F(u,v)e^{j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

---

# DFT Process

```text
Image
(Pixel Values)
      │
      ▼
Compute DFT
      │
      ▼
Frequency Spectrum
      │
      ▼
Apply Filter
(LPF / HPF)
      │
      ▼
Inverse DFT
      │
      ▼
Processed Image
```

---

# Properties of DFT

1. **Linearity**

If

$$
g(x,y)=af(x,y)+bh(x,y)
$$

then

$$
G(u,v)=aF(u,v)+bH(u,v)
$$

---

2. **Periodicity**

Both the image and its DFT are periodic.

---

3. **Symmetry**

For real-valued images, the DFT has conjugate symmetry.

---

4. **Translation (Shifting)**

Shifting an image changes only the phase of its DFT, not the magnitude.

---

5. **Convolution Property**

Convolution in the spatial domain becomes multiplication in the frequency domain.

$$
f*g
\longleftrightarrow
F(u,v)G(u,v)
$$

This is why filtering is easier in the frequency domain.

---

# Advantages

* Efficient frequency analysis.
* Makes filtering easier.
* Used in image enhancement and restoration.
* Forms the basis of the Fast Fourier Transform (FFT).

---

# Disadvantages

* Computationally expensive with complexity

$$
O(N^2)
$$

for a 1D signal of length $N$ (or approximately $$O((MN)^2)$$ for a naïve 2D implementation).

* Produces complex-valued output.
* Slower than FFT.

---

# DFT vs FFT

| DFT                           | FFT                                           |
| ----------------------------- | --------------------------------------------- |
| Mathematical transform        | Fast algorithm to compute the DFT             |
| Computes frequency components | Computes the same DFT result more efficiently |
| Slower                        | Much faster                                   |
| Complexity: $$O(N^2)$$        | Complexity: $$O(N\log N)$$                    |

---

# Applications

* Image enhancement
* Frequency-domain filtering
* Image restoration
* Medical imaging
* Satellite image processing
* Image compression
* Pattern recognition

---

# Memory Trick

Imagine a song.

* The **song** is the image.
* The **individual musical notes** are the frequency components.

The **DFT separates the song into its individual notes**, just as it separates an image into its low- and high-frequency components.

---

# Exam Answer (5 Marks)

**Definition:**

The **Discrete Fourier Transform (DFT)** is a mathematical transform that converts a digital image or discrete signal from the **spatial domain** into the **frequency domain**, representing it as a sum of sinusoidal frequency components.

**1D DFT:**

$$
F(u)=\sum_{x=0}^{N-1}f(x)e^{-j\frac{2\pi ux}{N}}
$$

**2D DFT:**

$$
F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f(x,y)e^{-j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

**Applications:**

* Image enhancement
* Noise removal
* Frequency-domain filtering
* Image restoration
* Image compression

**Key Point:**
The DFT converts an image from the **spatial domain (pixel values)** to the **frequency domain (frequency components)**, allowing efficient analysis and filtering of low- and high-frequency information.
