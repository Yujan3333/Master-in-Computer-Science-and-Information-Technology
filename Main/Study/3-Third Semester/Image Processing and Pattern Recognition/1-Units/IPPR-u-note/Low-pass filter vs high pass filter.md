#ippr #third-semester #exam-paper-answer #old-que 

---

# Question 1

**What is the difference between a Low-Pass Filter (LPF) and High-Pass Filter (HPF) in the spatial domain?**

## Low-Pass Filter (LPF)

A **Low-Pass Filter** is used for **image smoothing (blurring)**. It allows **low-frequency components** (slow intensity changes) to remain while suppressing **high-frequency components** (edges, fine details, noise).

### Purpose

* Reduce noise
* Remove small details
* Blur the image
* Smooth intensity variations

### Common Masks

**Mean Filter (3×3)**

$$[
\frac{1}{9}
\begin{bmatrix}
1&1&1\
1&1&1\
1&1&1
\end{bmatrix}
]$$

**Weighted Average Filter**

$$[
\frac{1}{16}
\begin{bmatrix}
1&2&1\
2&4&2\
1&2&1
\end{bmatrix}
]$$

### Effect

Before filtering

```
Sharp edges
Noise present
```

After LPF

```
Smooth image
Edges become blurred
Noise decreases
```

---

## High-Pass Filter (HPF)

A **High-Pass Filter** is used for **image sharpening**. It preserves **high-frequency components** (edges and details) while suppressing **low-frequency components**.

### Purpose

* Detect edges
* Sharpen image
* Enhance fine details
* Highlight sudden intensity changes

### Common Masks

**Laplacian Mask**

$$[
\begin{bmatrix}
0&-1&0\\
-1&4&-1\\
0&-1&0
\end{bmatrix}
]$$

or

$$[
\begin{bmatrix}
-1&-1&-1\\
-1&8&-1\\
-1&-1&-1
\end{bmatrix}
]$$

### Effect

Before filtering

```
Blurred image
```

After HPF

```
Edges become sharper
Details enhanced
Noise may also increase
```

---

# Difference between LPF and HPF

| Low-Pass Filter (LPF)                  | High-Pass Filter (HPF)                     |
| -------------------------------------- | ------------------------------------------ |
| Smooths the image                      | Sharpens the image                         |
| Removes noise                          | Enhances edges                             |
| Passes low frequencies                 | Passes high frequencies                    |
| Blocks high frequencies                | Blocks low frequencies                     |
| Produces blur                          | Produces edge enhancement                  |
| Used before segmentation               | Used after smoothing or for edge detection |
| Examples: Mean filter, Gaussian filter | Examples: Laplacian, High-boost, Sobel     |

---

# Simple Example

Suppose an image contains:

* Noise
* Smooth background
* Object edges

### Applying LPF

```
Original

████████
██▒▒▒███
██ Noise
████████
```

↓

```
After LPF

████████
████████
Smooth image
```

Noise is reduced but edges become blurred.

---

### Applying HPF

```
Original

████████
██▒▒▒███
████████
```

		↓

```
After HPF

Only edges become bright
Background suppressed
```

Edges become more visible.

---

# Advantages

### Low-Pass Filter

* Removes random noise
* Smooths images
* Easy to implement
* Good preprocessing step

### High-Pass Filter

* Enhances edges
* Improves details
* Useful for feature extraction
* Helps in object detection

---

# Disadvantages

### Low-Pass Filter

* Blurs edges
* Removes fine details

### High-Pass Filter

* Amplifies noise
* May create false edges

---

# Exam Answer (5 Marks)

**Low-Pass Filter (LPF):**
A low-pass filter smooths an image by allowing low-frequency components to pass while suppressing high-frequency components. It is mainly used for noise reduction and image smoothing. Examples include mean, weighted average, and Gaussian filters.

**High-Pass Filter (HPF):**
A high-pass filter sharpens an image by preserving high-frequency components such as edges while removing low-frequency components. It is mainly used for edge detection and image sharpening. Examples include Laplacian, Sobel, and high-boost filters.

### Differences

| LPF                    | HPF                         |
| ---------------------- | --------------------------- |
| Smoothing              | Sharpening                  |
| Removes noise          | Enhances edges              |
| Passes low frequencies | Passes high frequencies     |
| Blurs image            | Highlights details          |
| Mean/Gaussian filter   | Laplacian/High-boost filter |

> **Memory tip:**
> **LPF = Blur = Smooth = Remove Noise**
> **HPF = Sharp = Edge = Detail Enhancement**
