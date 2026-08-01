#ippr #third-semester 
# 11. Explain How Will You Use the Adaptive Mean Filter in Image Restoration. **[6 Marks]**

---

# Adaptive Mean Filter

## Definition

An **Adaptive Mean Filter** is a spatial-domain restoration filter that **reduces noise while preserving image details and edges**. Unlike the ordinary mean filter, it **adapts its smoothing based on the local image statistics** (local mean and local variance).

It is particularly effective for **Gaussian noise** and other additive noise.

---

# Principle

The filter assumes that:

* If the local variance is **small**, the region is nearly uniform, so more smoothing is applied.
* If the local variance is **large**, the region contains edges or fine details, so less smoothing is applied to preserve them.

Thus, the amount of smoothing changes from one neighborhood to another.

---

# Mathematical Formula

The restored pixel value is

$$
\hat{f}(x,y)
============

 g(x,y)

\frac{\sigma_n^2}{\sigma_L^2}
\left(g(x,y)-m_L\right)
$$

where

* $$\hat{f}(x,y)$$ = Restored pixel
* $$g(x,y)$$ = Noisy pixel
* $$m_L$$ = Local mean of the neighborhood
* $$\sigma_L^2$$ = Local variance
* $$\sigma_n^2$$ = Noise variance

---

# Interpretation of the Formula

### Case 1: Uniform Region

If

$$
\sigma_L^2 \approx \sigma_n^2
$$

the region mainly contains noise.

The filter performs **strong smoothing**.

---

### Case 2: Edge Region

If

$$
\sigma_L^2 \gg \sigma_n^2
$$

the region contains edges or important details.

The correction term becomes small, so the filter changes the pixel only slightly.

Thus, **edges are preserved**.

---

# Algorithm

1. Select a neighborhood (e.g., $$3\times3$$ or $$5\times5$$ window).

2. Compute the **local mean** $$m_L$$.

3. Compute the **local variance** $$\sigma_L^2$$.

4. Estimate or use the known **noise variance** $$\sigma_n^2$$.

5. Apply

   $$
   \hat{f}(x,y)
   ============

g(x,y)

   \frac{\sigma_n^2}{\sigma_L^2}
   \left(g(x,y)-m_L\right)
   $$

6. Repeat for every pixel.

7. The resulting image is the restored image.

---

# Flow Diagram

```text
Noisy Image
      │
      ▼
Select Local Window
      │
      ▼
Compute Local Mean
      │
      ▼
Compute Local Variance
      │
      ▼
Estimate Noise Variance
      │
      ▼
Apply Adaptive Mean Formula
      │
      ▼
Restored Image
```

---

# Advantages

* Reduces Gaussian noise effectively.
* Preserves edges better than the ordinary mean filter.
* Performs different amounts of smoothing in different regions.
* Produces better image quality than a simple averaging filter.

---

# Disadvantages

* Requires an estimate of the noise variance.
* More computationally expensive than the arithmetic mean filter.
* Less effective for Salt-and-Pepper noise.

---

# Applications

* Medical image restoration
* Satellite image processing
* Remote sensing
* Camera image enhancement
* Scientific imaging

---

# Difference Between Mean Filter and Adaptive Mean Filter

| Mean Filter                                  | Adaptive Mean Filter                                      |
| -------------------------------------------- | --------------------------------------------------------- |
| Uses a simple average of neighboring pixels. | Uses local mean and local variance.                       |
| Applies the same smoothing everywhere.       | Applies variable smoothing depending on the image region. |
| Blurs edges significantly.                   | Preserves edges much better.                              |
| Simple and fast.                             | More complex and computationally expensive.               |
| Suitable for low Gaussian noise.             | Better for images with varying Gaussian noise.            |

---

# Exam Answer (6 Marks)

An **Adaptive Mean Filter** is a restoration filter that removes **Gaussian noise** by using the **local mean** and **local variance** of the image. Unlike the ordinary mean filter, it adapts the amount of smoothing according to the local image characteristics, thereby preserving edges while reducing noise.

The restored pixel is computed using

$$
\hat{f}(x,y)
============

g(x,y)

\frac{\sigma_n^2}{\sigma_L^2}
\left(g(x,y)-m_L\right)
$$

where $$g(x,y)$$ is the noisy pixel, $$m_L$$ is the local mean, $$\sigma_L^2$$ is the local variance, and $$\sigma_n^2$$ is the noise variance.

**Algorithm:**

1. Select a local window.
2. Compute the local mean.
3. Compute the local variance.
4. Estimate the noise variance.
5. Apply the adaptive mean filter formula.
6. Repeat for all pixels to obtain the restored image.

**Advantages:** Preserves edges, reduces Gaussian noise effectively, and provides adaptive smoothing.

**Disadvantages:** Requires noise variance estimation and has higher computational complexity.

---

## ⭐ Exam Tip

A common comparison is:

* **Arithmetic Mean Filter:** Same averaging for every pixel → more blurring.
* **Adaptive Mean Filter:** Adjusts smoothing using local variance → better edge preservation.

