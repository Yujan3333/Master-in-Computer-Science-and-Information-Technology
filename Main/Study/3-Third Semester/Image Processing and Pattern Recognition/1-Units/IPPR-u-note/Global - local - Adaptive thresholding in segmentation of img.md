#ippr #third-semester 
## 1. Explain Global, Local, and Adaptive Thresholding in Segmentation. **[5 Marks]**

### Image Segmentation

Image segmentation is the process of dividing an image into meaningful regions or objects by grouping pixels with similar characteristics.

Thresholding is one of the simplest segmentation techniques. It separates the foreground from the background based on pixel intensity.

---

# 1. Global Thresholding

### Definition

Global thresholding uses **one single threshold value (T)** for the entire image.

Every pixel is classified as:

* Foreground if intensity ≥ T
* Background if intensity < T

### Formula


$$g(x,y)=
\begin{cases}
1,&f(x,y)\ge T\\
0,&f(x,y)<T
\end{cases}$$

where

* (f(x,y)) = original image
* (g(x,y)) = segmented image
* (T) = global threshold

### Example

Suppose

[
$$T=120$$
]

Image intensities

| 100 | 140 | 180 |
| --- | --- | --- |
| 90  | 125 | 150 |
| 60  | 130 | 220 |

After thresholding

| 0 | 1 | 1 |
| - | - | - |
| 0 | 1 | 1 |
| 0 | 1 | 1 |

---

### Advantages

* Very simple
* Fast
* Low computation

### Disadvantages

* Does not work well when illumination is uneven.
* Sensitive to shadows.

---

# 2. Local Thresholding

### Definition

Instead of one threshold for the whole image, **each small neighborhood has its own threshold.**

The image is divided into small windows.

Each window computes its own threshold.

### Example

Window 1

$$[
T_1=80
]$$

Window 2

$$[
T_2=150
]$$

Thus different parts of image use different thresholds.

---

### Advantages

* Handles varying illumination better.
* Better than global thresholding.

### Disadvantages

* More computationally expensive.
* Window size selection affects result.

---

# 3. Adaptive Thresholding

### Definition

Adaptive thresholding computes the threshold **for every pixel** based on the surrounding neighborhood.

The threshold changes continuously throughout the image.

Common methods:

* Mean of neighborhood
* Gaussian weighted mean

---

### Formula

Mean method

$$[
T(x,y)=\text{Mean of neighboring pixels}
]$$

Then

$$[
g(x,y)=
\begin{cases}
1,&f(x,y)\ge T(x,y)\\
0,&f(x,y)<T(x,y)
\end{cases}
]$$

---

### Example

Suppose surrounding pixels have average intensity

$$[
T=105
]$$

Pixel value

$$[
110>105
]$$

Therefore

Foreground.

Another location

Neighborhood average

$$[
T=180
]$$

Pixel

$$[
170<180
]$$

Therefore

Background.

---

### Advantages

* Excellent under non-uniform lighting.
* Gives accurate segmentation.

### Disadvantages

* Highest computation cost.
* Slower than global thresholding.

---

# Comparison Table

| Feature             | Global    | Local          | Adaptive      |
| ------------------- | --------- | -------------- | ------------- |
| Threshold           | One value | One per region | One per pixel |
| Speed               | Fast      | Moderate       | Slow          |
| Uneven illumination | Poor      | Good           | Excellent     |
| Complexity          | Low       | Medium         | High          |

---

# Exam Answer (5 Marks)

**Global Thresholding:** Uses one threshold value for the entire image. Pixels above the threshold become foreground, while others become background. It is simple and fast but fails under uneven illumination.

**Local Thresholding:** Divides the image into small regions and computes a different threshold for each region. It performs better when lighting varies across the image.

**Adaptive Thresholding:** Calculates a threshold for every pixel based on its neighboring pixels (mean or Gaussian weighted average). It provides the best segmentation under varying illumination but requires more computation.

---

### **Exam Tip**

A common diagram to draw:

```
Image
   │
   ▼
Threshold Selection
   │
   ▼
Binary Image
```

Then mention:

* Global → One threshold
* Local → One threshold per region
* Adaptive → One threshold per pixel
