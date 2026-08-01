#ippr #third-semester #exam-paper-answer 

# Question 3

## What is Histogram Equalization in Image Enhancement? Illustrate with an Example.

---

# Histogram

A **histogram** is a graphical representation of the distribution of pixel intensity (gray) levels in an image.

* **X-axis:** Gray levels (0–255 for an 8-bit image)
* **Y-axis:** Number of pixels corresponding to each gray level

A histogram helps determine whether an image is:

* Dark
* Bright
* Low contrast
* High contrast

---

# Histogram Equalization

**Histogram Equalization** is an image enhancement technique used to **improve the contrast** of an image by redistributing the gray levels so that they occupy the full available intensity range.

Instead of having most pixels concentrated in a small range of gray levels, histogram equalization spreads them over the entire range.

### Definition (Exam)

> **Histogram Equalization** is a technique that enhances the contrast of an image by transforming the intensity values using the cumulative distribution function (CDF), producing an approximately uniform histogram.

---

# Why Histogram Equalization is Needed

Suppose an image uses only gray levels from **40 to 90**.

Although the image can use values from **0 to 255**, most pixels are confined to a small range, resulting in **low contrast**.

Histogram equalization stretches these values across the entire range, making the image clearer and improving visibility.

---

# Mathematical Formula

Let

* $L$ = Number of gray levels
* $r_k$ = Original gray level
* $p(r_k)$ = Probability of occurrence of gray level $r_k$

The transformation function is

$$
s_k=(L-1)\sum_{j=0}^{k}p(r_j)
$$

where

* $s_k$ = New gray level after equalization
* $\sum p(r_j)$ = Cumulative Distribution Function (CDF)

---

# Steps of Histogram Equalization

1. Calculate the histogram.
2. Compute the probability of each gray level.

$$
p(r_k)=\frac{n_k}{N}
$$

where

* $n_k$ = Number of pixels having gray level $k$
* $N$ = Total number of pixels

3. Compute the cumulative distribution function (CDF).

$$
CDF(k)=\sum_{j=0}^{k}p(r_j)
$$

4. Calculate the new gray levels.

$$
s_k=(L-1)\times CDF(k)
$$

5. Round the values to the nearest integer.
6. Replace each old gray level with the corresponding new gray level.
7. Obtain the enhanced image.

---

# Example

Suppose a **3-bit image** has **8 gray levels (0–7)** and contains **8 pixels**.

### Original Histogram

| Gray Level | Number of Pixels |
| ---------- | ---------------: |
| 0          |                1 |
| 1          |                1 |
| 2          |                2 |
| 3          |                1 |
| 4          |                1 |
| 5          |                1 |
| 6          |                1 |
| 7          |                0 |

Total pixels

$$
N=8
$$

Number of gray levels

$$
L=8
$$

---

## Step 1: Calculate Probability

Using

$$
p(r_k)=\frac{n_k}{N}
$$

| Gray Level | Pixels | Probability |
| ---------- | -----: | ----------: |
| 0          |      1 |       0.125 |
| 1          |      1 |       0.125 |
| 2          |      2 |       0.250 |
| 3          |      1 |       0.125 |
| 4          |      1 |       0.125 |
| 5          |      1 |       0.125 |
| 6          |      1 |       0.125 |
| 7          |      0 |           0 |

---

## Step 2: Calculate CDF

| Gray Level | Probability |   CDF |
| ---------- | ----------: | ----: |
| 0          |       0.125 | 0.125 |
| 1          |       0.125 | 0.250 |
| 2          |       0.250 | 0.500 |
| 3          |       0.125 | 0.625 |
| 4          |       0.125 | 0.750 |
| 5          |       0.125 | 0.875 |
| 6          |       0.125 | 1.000 |
| 7          |           0 | 1.000 |

---

## Step 3: Calculate New Gray Levels

Using

$$
s_k=(L-1)\times CDF
$$

Since

$$
L-1=7
$$

The new gray levels become

| Old Gray Level |   CDF | $7\times CDF$ | New Gray Level |
| -------------: | ----: | ------------: | -------------: |
|              0 | 0.125 |         0.875 |              1 |
|              1 | 0.250 |         1.750 |              2 |
|              2 | 0.500 |         3.500 |              4 |
|              3 | 0.625 |         4.375 |              4 |
|              4 | 0.750 |         5.250 |              5 |
|              5 | 0.875 |         6.125 |              6 |
|              6 | 1.000 |         7.000 |              7 |
|              7 | 1.000 |         7.000 |              7 |

Thus the mapping is

| Original | Equalized |
| -------- | --------- |
| 0 → 1    |           |
| 1 → 2    |           |
| 2 → 4    |           |
| 3 → 4    |           |
| 4 → 5    |           |
| 5 → 6    |           |
| 6 → 7    |           |
| 7 → 7    |           |

Every pixel in the original image is replaced according to this mapping.

---

# Histogram Before and After

### Before Equalization

* Gray levels concentrated in a small range.
* Low contrast.
* Image appears dull.

```
Frequency

        ███
      ██████
████████████
-------------------
0 1 2 3 4 5 6 7
```

---

### After Equalization

* Gray levels spread over the entire range.
* Contrast improves.
* Image details become clearer.

```
Frequency

█ █ █ █ █ █ █
-------------------
0 1 2 3 4 5 6 7
```

---

# Advantages

* Improves image contrast.
* Reveals hidden details.
* Enhances dark and bright regions.
* Simple and automatic technique.
* Widely used in medical and satellite imaging.

---

# Disadvantages

* May amplify noise.
* Can produce an unnatural appearance.
* Does not preserve the original brightness.
* Less effective when the image already has good contrast.

---

# Applications

* Medical image enhancement
* Satellite image processing
* Remote sensing
* X-ray and MRI analysis
* Fingerprint recognition
* Document image enhancement

---

# Histogram Equalization vs Histogram Matching

| Histogram Equalization                      | Histogram Matching                                              |
| ------------------------------------------- | --------------------------------------------------------------- |
| Produces an approximately uniform histogram | Produces a histogram similar to a specified reference histogram |
| No reference image is required              | Requires a reference image                                      |
| Automatic enhancement                       | Controlled enhancement                                          |

---

# Exam Answer (5 Marks)

**Histogram Equalization** is an image enhancement technique used to improve image contrast by redistributing pixel intensity values over the available gray-level range. It uses the **Cumulative Distribution Function (CDF)** to transform the original gray levels into new gray levels, resulting in an approximately uniform histogram and better visual quality.

The transformation is given by

$$
s_k=(L-1)\sum_{j=0}^{k}p(r_j)
$$

**Steps:**

1. Compute the histogram.
2. Calculate the probability of each gray level.
3. Compute the CDF.
4. Calculate new gray levels using the transformation function.
5. Replace the old gray levels with the new ones.

**Advantages:** Improves contrast, enhances image details, and is widely used in medical imaging, satellite imaging, and image enhancement.

> **Exam Tip:** Histogram equalization numericals (especially for an **8×8 image with gray levels 0–7**) are among the **most frequently asked questions**. Practice the complete procedure:
>
> **Histogram → Probability → CDF → New Gray Levels → Equalized Histogram.**
