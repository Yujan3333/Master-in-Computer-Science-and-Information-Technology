
## 1️⃣ What is histogram equalization?

Histogram equalization is a technique in **image processing** to improve the contrast of an image. The idea is:

* Darker images or images with poor contrast often have **most pixels concentrated in a narrow range of gray levels**.
* Histogram equalization spreads the pixel values more evenly across the available gray levels, making details more visible.

So, we are **transforming original gray levels $r_k$ into new gray levels $s_k$** in a way that the new histogram is more "uniform".

---

## 2️⃣ Step 1: Compute Cumulative Distribution (CDF)

* $p_r(r_k)$ is the **probability of each gray level** (i.e., how many pixels have gray level $r_k$ divided by total pixels).
* The **CDF (cumulative distribution function)** adds up these probabilities progressively:

$$\text{CDF}(r_k) = \sum_{j=0}^{k} p_r(r_j)$$

* This gives us the fraction of pixels with intensity **less than or equal to $r_k$**.
* Example: For $r_2$, CDF = 0.19 + 0.25 + 0.21 = 0.65. That means **65% of pixels have gray level ≤ 2**.

---

## 3️⃣ Step 2: Compute Transformation $s_k$

The formula:

$$s_k = (L-1) \cdot \text{CDF}(r_k)$$

* $L$ = number of gray levels (here $L=8$, so $L-1=7$)
* Multiply the CDF by $L-1$ to scale it into the **new gray level range** $[0, L-1]$.
* Round $s_k$ to nearest integer because gray levels must be integers.
* This gives a **mapping from old gray level $r_k$ to new gray level $s_k$**.

Example:

* $r_0 = 0$, CDF = 0.19 → $s_0 = 7 * 0.19 = 1.33 ≈ 1$
* $r_1 = 1$, CDF = 0.44 → $s_1 = 7 * 0.44 = 3.08 ≈ 3$

This is why we get the mapping table:

$$0\to1, 1\to3, 2\to5, 3\to6, 4\to6, 5\to7, 6\to7, 7\to7$$

---

## 4️⃣ Step 3: Compute New Histogram $p_s(s_k)$

* Now we look at **how many original gray levels map to each new gray level**.
* For example, new level $6$ comes from $r_3$ and $r_4$, so its probability is $0.16 + 0.08 = 0.24$.
* This gives the **output histogram**, which is more spread out.

$$p_s(s_k) = {0, 0.19, 0, 0.25, 0, 0.21, 0.24, 0.11}$$

---

## ✅ In short:

1. Compute the **CDF** of the original histogram.
2. Scale it to the new gray levels to get **mapping $r_k \to s_k$**.
3. Calculate the **new histogram** after mapping.

The result is a **contrast-enhanced image** where pixel intensities are more evenly distributed.

---

