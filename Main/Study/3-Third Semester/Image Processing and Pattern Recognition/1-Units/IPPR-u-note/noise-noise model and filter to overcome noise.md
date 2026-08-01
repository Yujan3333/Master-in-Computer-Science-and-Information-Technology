#ippr #third-semester 

# 5. What is Noise in the Context of Image? Classify Different Types of Noise Models with Examples. Explain Four Kinds of Filtering Mechanisms to Overcome the Noise. **[10 Marks]**

This is one of the **most important theory questions** in Unit 3.

---

# Noise

## Definition

**Noise** is the unwanted random variation in the intensity or brightness of pixels that degrades the quality of an image during acquisition, transmission, or processing.

Noise causes the image to appear distorted, making it difficult to extract useful information.

---

# Causes of Noise

* Camera sensor imperfections
* Low lighting conditions
* Electronic interference
* Transmission errors
* Dust or scratches
* Atmospheric disturbances

---

# Types of Noise Models

There are six commonly used noise models.

---

# 1. Gaussian Noise

## Definition

Gaussian noise is caused by random electronic fluctuations during image acquisition.

Its intensity values follow the **Gaussian (Normal) distribution**.

Probability Density Function (PDF)

$$
p(z)=\frac{1}{\sqrt{2\pi\sigma^2}}
e^{-\frac{(z-\mu)^2}{2\sigma^2}}
$$

where

* $$\mu$$ = mean
* $$\sigma$$ = standard deviation

### Characteristics

* Randomly distributed.
* Affects every pixel.
* Most common noise model.

### Example

Noise produced by digital camera sensors.

---

# 2. Salt-and-Pepper Noise (Impulse Noise)

## Definition

Salt-and-Pepper noise appears as randomly occurring **white (salt)** and **black (pepper)** pixels.

### Characteristics

* Pixels become either minimum intensity (0) or maximum intensity (255).
* Caused by transmission errors or faulty sensors.

### Example

```text
Original

50 52 54
55 56 58
60 61 63

Noisy

50 255 54
0   56 58
60 61 255
```

### Best Filter

Median Filter

Adaptive Median Filter

---

# 3. Uniform Noise

## Definition

The probability of every intensity value within a certain range is equal.

PDF

$$
p(z)=
\frac1{b-a}
\qquad
a\le z\le b
$$

### Characteristics

* All values occur with equal probability.
* Less common in practical imaging.

---

# 4. Rayleigh Noise

## Definition

Rayleigh noise occurs in radar and medical imaging systems.

PDF

$$
p(z)
====

\frac{z-a}{b}
e^{-\frac{(z-a)^2}{2b}}
\qquad
z\ge a
$$

### Applications

* Radar
* Ultrasound

---

# 5. Erlang (Gamma) Noise

Also called **Gamma Noise**.

PDF

$$
p(z)
====

\frac{a^bz^{b-1}e^{-az}}
{(b-1)!}
$$

### Applications

* Laser imaging
* Nuclear medicine

---

# 6. Exponential Noise

PDF

$$
p(z)=ae^{-az}
$$

### Applications

Communication systems.

---

# Classification of Noise Models

| Noise Model     | Characteristics          | Example                |
| --------------- | ------------------------ | ---------------------- |
| Gaussian        | Normal distribution      | Camera sensor noise    |
| Salt-and-Pepper | Black & white pixels     | Faulty transmission    |
| Uniform         | Equal probability        | Quantization noise     |
| Rayleigh        | Skewed distribution      | Radar images           |
| Erlang (Gamma)  | Gamma distribution       | Medical imaging        |
| Exponential     | Exponential distribution | Communication channels |

---

# Filtering Mechanisms for Noise Removal

Filtering removes or reduces noise from images.

The four commonly used filtering mechanisms are:

1. Arithmetic Mean Filter
2. Median Filter
3. Adaptive Mean Filter
4. Adaptive Median Filter

---

# 1. Arithmetic Mean Filter

## Definition

Each pixel is replaced by the average value of neighboring pixels.

Formula

$$
\hat f(x,y)
===========

\frac1{mn}
\sum g(s,t)
$$

### Advantages

* Simple implementation.
* Effective for Gaussian noise.

### Disadvantages

* Blurs edges.
* Reduces image sharpness.

---

# 2. Median Filter

## Definition

Each pixel is replaced by the median of the neighboring pixels.

Example

Window

```text
20 21 22
18 255 24
19 20 23
```

Sorted

```text
18 19 20 20 21 22 23 24 255
```

Median

$$
21
$$

New center pixel

```text
255 → 21
```

### Advantages

* Removes Salt-and-Pepper noise effectively.
* Preserves image edges.

### Disadvantages

* Less effective for Gaussian noise.

---

# 3. Adaptive Mean Filter

## Definition

The filter adjusts the amount of smoothing according to the local image variance.

Formula

$$
\hat f(x,y)
===========

 g(x,y)

\frac{\sigma_n^2}{\sigma_L^2}
(g(x,y)-m_L)
$$

where

* $$m_L$$ = Local mean
* $$\sigma_L^2$$ = Local variance
* $$\sigma_n^2$$ = Noise variance

### Advantages

* Better edge preservation.
* Reduces Gaussian noise.

---

# 4. Adaptive Median Filter

## Definition

Unlike the ordinary median filter, the window size changes automatically depending on the amount of noise.

Algorithm

1. Compute the median.
2. Check whether the median is noisy.
3. If noisy, increase the window size.
4. Replace the center pixel with the median.

### Advantages

* Removes high-density Salt-and-Pepper noise.
* Preserves edges better than the median filter.

---

# Which Filter Removes Which Noise?

| Noise Type      | Best Filter                    |
| --------------- | ------------------------------ |
| Gaussian        | Arithmetic Mean, Adaptive Mean |
| Salt-and-Pepper | Median, Adaptive Median        |
| Uniform         | Mean Filter                    |
| Rayleigh        | Adaptive Mean                  |
| Gamma           | Adaptive Mean                  |
| Exponential     | Adaptive Mean                  |

---

# Difference Between Median and Mean Filter

| Mean Filter             | Median Filter                    |
| ----------------------- | -------------------------------- |
| Uses average value      | Uses median value                |
| Blurs edges             | Preserves edges                  |
| Good for Gaussian noise | Good for Salt-and-Pepper noise   |
| Simple                  | More effective for impulse noise |

---

# Exam Answer (10 Marks)

1. Define image noise.
2. Mention the causes of noise.
3. Explain the six noise models:

   * Gaussian
   * Salt-and-Pepper
   * Uniform
   * Rayleigh
   * Erlang (Gamma)
   * Exponential
4. Explain four filtering mechanisms:

   * Arithmetic Mean Filter
   * Median Filter
   * Adaptive Mean Filter
   * Adaptive Median Filter
5. Draw a comparison table showing the best filter for each noise type.

> **Exam Tip:** For a 10-mark answer, include the **definition**, **classification table**, **PDF formulas (where applicable)**, and explain **at least four filters** with one or two advantages each. This structure typically earns full marks in TU examinations.
