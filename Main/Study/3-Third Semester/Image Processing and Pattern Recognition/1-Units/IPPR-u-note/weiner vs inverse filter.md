
#ippr #third-semester 

# Wiener Filtering vs Inverse Filtering

Both **Inverse Filtering** and **Wiener Filtering** are image restoration techniques used to recover a degraded image. The main difference is that **Inverse Filtering assumes no noise**, whereas **Wiener Filtering considers both blur and noise**.

---

## Comparison

| Feature                  | **Inverse Filtering**                            | **Wiener Filtering**                  |
| ------------------------ | ------------------------------------------------ | ------------------------------------- |
| Purpose                  | Removes blur only                                | Removes blur and reduces noise        |
| Noise Handling           | Assumes noise is absent or negligible            | Explicitly considers noise            |
| Principle                | Uses the inverse of the degradation function     | Minimizes the Mean Square Error (MSE) |
| Restoration Quality      | Poor when noise is present                       | Better even when noise is present     |
| Stability                | Can become unstable if $H(u,v)$ is close to zero | More stable and robust                |
| Computational Complexity | Simple                                           | More complex                          |
| Practical Use            | Suitable for ideal or noise-free images          | Suitable for real-world noisy images  |

---

# 1. Inverse Filtering

## Definition

**Inverse Filtering** restores an image by applying the inverse of the degradation function in the frequency domain. It assumes that the degradation function is known and that noise is absent or very small.

### Formula

If the degraded image is

$$
G(u,v)=H(u,v)F(u,v)
$$

then the restored image is

$$
\boxed{
F(u,v)=\frac{G(u,v)}{H(u,v)}
}
$$

where:

* $F(u,v)$ = Original image
* $G(u,v)$ = Degraded image
* $H(u,v)$ = Degradation (blur) function

### Advantages

* Simple to implement.
* Works well for blur-only degradation.

### Disadvantages

* Very sensitive to noise.
* Fails when $H(u,v)$ is zero or very close to zero.
* Noise gets greatly amplified.

---

# 2. Wiener Filtering

## Definition

**Wiener Filtering** restores an image by considering both the degradation function and the noise. It minimizes the **Mean Square Error (MSE)** between the restored image and the original image.

### Formula

$$
\boxed{
\hat{F}(u,v)
============

\frac{H^*(u,v)}
{|H(u,v)|^2+\dfrac{S_n(u,v)}{S_f(u,v)}}
,G(u,v)
}
$$

where:

* $H^*(u,v)$ = Complex conjugate of $H(u,v)$
* $S_n(u,v)$ = Noise power spectrum
* $S_f(u,v)$ = Original image power spectrum

If noise is negligible,

$$
\frac{S_n(u,v)}{S_f(u,v)} \approx 0
$$

then the Wiener filter approaches the inverse filter.

### Advantages

* Removes both blur and noise.
* Produces higher-quality restored images.
* More robust and stable.

### Disadvantages

* More computationally expensive.
* Requires estimation of noise and image statistics.

---

# Key Difference

Suppose an image is blurred and contains noise.

### Inverse Filtering

* Attempts to remove only the blur.
* Noise is amplified, leading to poor restoration.

### Wiener Filtering

* Removes blur while suppressing noise.
* Produces a cleaner and more accurate restored image.

---

# Memory Trick

### Inverse Filtering

* **Inverse = Blur only**
* **Ignores noise**
* **Simple but sensitive**

### Wiener Filtering

* **Wiener = Blur + Noise**
* **Minimizes error**
* **Best for practical image restoration**

---

# Exam Summary

### Inverse Filtering

* Removes blur using the inverse degradation function.
* Assumes little or no noise.
* Simple but unstable in noisy conditions.

### Wiener Filtering

* Restores images by considering both blur and noise.
* Minimizes the Mean Square Error (MSE).
* Produces better restoration for real-world images.

---

## One-Line Difference

* **Inverse Filtering:** Restores an image by **inverting the degradation function**, assuming noise is negligible.
* **Wiener Filtering:** Restores an image by **minimizing the Mean Square Error**, considering **both blur and noise**.
