
# Image Sampling and Quantization

*(Based on Digital Image Processing)*

---

# 1. Basic Concept

To convert a **continuous image** into a **digital image**, two processes are required:

1. **Sampling** → digitization of spatial coordinates
2. **Quantization** → digitization of intensity values

---

# 2. Continuous Image

A continuous image is:

$$f(x,y)$$

* Continuous in **spatial coordinates (x, y)**
* Continuous in **intensity (amplitude)**

👉 To make it digital → both must be discretized

---

# 3. Image Sampling

## Definition

Sampling is the process of converting **continuous spatial coordinates** into **discrete coordinates**.

---

## Explanation

* Take samples at **equally spaced intervals**
* Converts image into a **grid of pixels**

---

## Result

* Produces discrete coordinates:
  $$x=0,1,2,\dots,M-1$$
  $$y=0,1,2,\dots,N-1$$

* Output → **M × N image (rows × columns)**

---

## Key Point

* Determines **spatial resolution**
* More samples → higher detail

---

# 4. Image Quantization

## Definition

Quantization is the process of converting **continuous intensity values** into **discrete levels**.

---

## Explanation

* Intensity values are divided into **finite levels**
* Each sample is assigned nearest level

---

## Result

* Intensity levels:
  $$0,1,2,\dots,L-1$$

* Number of levels:
  $$L=2^k$$

---

## Key Point

* Determines **gray-level resolution**
* More levels → better image quality

---

# 5. Combined Process

After sampling and quantization:

$$f(x,y)\rightarrow \text{digital image}$$

* Coordinates → discrete
* Intensity → discrete

👉 Final result = **digital image (matrix of pixels)**

---

# 6. Representation of Digital Image

A digital image is represented as:

$$f(x,y), \quad x,y \in \text{integers}$$

* Stored as **2D array (matrix)**
* Each element = **pixel value**

---

# 7. Important Concepts

## (a) Pixel

* Smallest element of image
* Also called **picture element (pel)**

---

## (b) Spatial Domain

* Plane defined by $(x,y)$ coordinates

---

## (c) Dynamic Range

* Ratio of maximum to minimum intensity

---

## (d) Image Quality Depends On:

* Number of samples (M, N)
* Number of intensity levels (L)
* Image content

---

# 8. Key Differences

| Sampling               | Quantization              |
| ---------------------- | ------------------------- |
| Spatial discretization | Intensity discretization  |
| Affects resolution     | Affects brightness levels |
| Produces pixels        | Assigns gray values       |

---

# 9. Key Exam Points

* Digital image = sampled + quantized image
* Sampling → spatial grid
* Quantization → intensity levels
* Image size = $M \times N$
* Intensity levels = $L=2^k$
* More sampling & quantization → better quality

---
