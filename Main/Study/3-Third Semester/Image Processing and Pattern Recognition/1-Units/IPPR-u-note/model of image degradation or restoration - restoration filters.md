
#ippr #third-semester 
# 3. What is the Model of Image Degradation or Restoration Process? Explain Several Restoration Filters. **[4+6]**

This is one of the **most frequently asked theory questions** in Unit 3.

---

# Image Degradation Model

## Definition

The **image degradation model** describes how an original image becomes degraded due to factors such as:

* Blur
* Noise
* Motion
* Atmospheric turbulence
* Camera defocus

The purpose of **image restoration** is to recover the original image from the degraded image using mathematical models.

---

# Degradation Process

Let

* $$f(x,y)$$ = Original image
* $$h(x,y)$$ = Degradation function (blur)
* $$\eta(x,y)$$ = Noise
* $$g(x,y)$$ = Degraded image

The degradation model is

$$
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
$$

where

* $$*$$ denotes convolution.

---

# Frequency Domain Representation

Applying Fourier Transform,

$$
G(u,v)=H(u,v)F(u,v)+N(u,v)
$$

where

* $$F(u,v)$$ = Fourier transform of original image
* $$H(u,v)$$ = Degradation function
* $$N(u,v)$$ = Noise
* $$G(u,v)$$ = Degraded image

---

# Image Restoration Model

The restoration process estimates the original image.

If the restoration filter is

$$
R(u,v)
$$

then

$$
\hat{F}(u,v)=R(u,v)G(u,v)
$$

where

$$
\hat F(u,v)
$$

is the restored image.

---

# Block Diagram

```text
              Original Image
                 f(x,y)
                    │
                    ▼
          Degradation Function
              h(x,y)
                    │
            + Noise η(x,y)
                    │
                    ▼
            Degraded Image
               g(x,y)
                    │
                    ▼
         Restoration Filter
               R(u,v)
                    │
                    ▼
            Restored Image
             f̂(x,y)
```

---

# Restoration Filters

A **restoration filter** removes degradation or noise from an image to obtain an estimate of the original image.

The commonly used restoration filters are:

1. Arithmetic Mean Filter
2. Geometric Mean Filter
3. Harmonic Mean Filter
4. Contra-Harmonic Mean Filter
5. Median Filter
6. Adaptive Mean Filter
7. Adaptive Median Filter
8. Inverse Filter
9. Wiener Filter
10. Band Reject Filter

---

# 1. Arithmetic Mean Filter

## Definition

Each pixel is replaced by the average of its neighboring pixels.

Formula

$$
\hat f(x,y)=\frac1{mn}
\sum_{(s,t)\in S_{xy}}
g(s,t)
$$

where

* $$m \times n$$ = mask size

### Advantages

* Simple
* Removes Gaussian noise

### Disadvantages

* Blurs edges
* Reduces image sharpness

---

# 2. Geometric Mean Filter

Formula

$$
\hat f(x,y)
===========

\left(
\prod g(s,t)
\right)^{\frac1{mn}}
$$

### Advantages

* Preserves detail better than arithmetic mean.
* Removes Gaussian noise.

---

# 3. Harmonic Mean Filter

Formula

$$
\hat f(x,y)
===========

\frac{mn}
{\sum\frac1{g(s,t)}}
$$

### Advantages

* Effective for Gaussian noise.

### Disadvantage

* Not suitable for Salt-and-Pepper noise.

---

# 4. Contra-Harmonic Mean Filter

Formula

$$
\hat f(x,y)
===========

\frac{\sum g^{Q+1}}
{\sum g^Q}
$$

where

$$
Q
$$

is the order of the filter.

### Uses

* $$Q>0$$ removes pepper noise.
* $$Q<0$$ removes salt noise.

---

# 5. Median Filter

## Definition

Each pixel is replaced by the median value of neighboring pixels.

Example

Neighborhood

```text
20 21 22
18 255 24
19 20 23
```

Sorted values

```text
18 19 20 20 21 22 23 24 255
```

Median

$$
21
$$

So

```text
255 → 21
```

### Advantages

* Excellent for Salt-and-Pepper noise.
* Preserves edges.

---

# 6. Adaptive Mean Filter

## Definition

It adjusts the amount of smoothing based on the local variance.

Formula

$$
\hat f(x,y)
=

g(x,y)

\frac{\sigma_n^2}
{\sigma_L^2}
(g(x,y)-m_L)
$$

where

* $m_L$ = local mean
* $\sigma_L^2$ = local variance
* $\sigma_n^2$ = noise variance

### Advantages

* Preserves edges.
* Better than ordinary mean filter.

---

# 7. Adaptive Median Filter

## Definition

The window size changes automatically until the noisy pixel is removed.

### Advantages

* Removes high-density Salt-and-Pepper noise.
* Preserves edges.
* Better than fixed median filter.

---

# 8. Inverse Filter

The degraded image is restored using

$$
\hat F(u,v)
===========

\frac{G(u,v)}
{H(u,v)}
$$

### Advantages

* Simple.
* Removes blur when noise is absent.

### Disadvantages

* Very sensitive to noise.

---

# 9. Wiener Filter

Formula

$$
\hat F(u,v)
===========

\frac{H^*(u,v)}
{|H(u,v)|^2+\frac{S_n}{S_f}}
G(u,v)
$$

where

* $H^*$ = complex conjugate
* $S_n$ = noise power spectrum
* $S_f$ = image power spectrum

### Advantages

* Removes blur and noise simultaneously.
* Produces better restoration than the inverse filter.

---

# 10. Band Reject Filter

A Band Reject Filter removes frequencies lying within a specified band while allowing frequencies outside the band to pass.

### Uses

* Removes periodic noise.
* Used in image restoration.

---

# Difference Between Enhancement and Restoration

| Image Enhancement                     | Image Restoration              |
| ------------------------------------- | ------------------------------ |
| Improves appearance.                  | Recovers the original image.   |
| Subjective process.                   | Objective process.             |
| Does not require a degradation model. | Requires a degradation model.  |
| Used for visual improvement.          | Used to remove blur and noise. |

---

# Exam Answer (10 Marks)

1. Define the image degradation model.
2. Write the degradation equation:

$$
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
$$

3. Write the frequency-domain equation:

$$
G(u,v)=H(u,v)F(u,v)+N(u,v)
$$

4. Draw the degradation/restoration block diagram.
5. Explain restoration filters:

   * Arithmetic Mean
   * Median
   * Adaptive Mean
   * Adaptive Median
   * Inverse
   * Wiener
   * Band Reject

> **Exam Tip:** For a 10-mark question, always include the **block diagram**, **equations**, and **at least six restoration filters** with one or two lines explaining each. This is the format typically expected in TU examinations.
