#ippr #third-semester 

# Unit 2: Image Enhancement and Filtering (Simple Exam Notes)

This unit is mainly divided into **three parts**:

1. Image Enhancement in Spatial Domain
2. Fourier Transform
3. Filtering in Frequency Domain

---

# Part A: Image Enhancement in Spatial Domain

## 1. Image Enhancement

### Definition

Image enhancement is the process of improving the appearance or quality of an image so that it becomes easier for humans or computers to analyze.

**Purpose**

* Improve image quality
* Increase contrast
* Remove noise
* Highlight important features

**Applications**

* Medical imaging
* Satellite images
* CCTV
* Photography

---

## 2. Spatial Domain and Frequency Domain

### Spatial Domain

In the spatial domain, we directly modify the pixel values of the image.

Mathematically,

$$[\space
g(x,y)=T[f(x,y)]
\space]$$

where:

* (f(x,y)) = input image
* (g(x,y)) = output image
* (T) = transformation

**Examples**

* Brightness adjustment
* Contrast enhancement
* Image smoothing

### Frequency Domain

Instead of changing pixels directly, the image is first converted into frequency components using the Fourier Transform.

High-frequency components:

* Edges
* Noise
* Fine details

Low-frequency components:

* Smooth areas
* Background

---

## Difference Between Spatial and Frequency Domain

| Spatial Domain          | Frequency Domain             |
| ----------------------- | ---------------------------- |
| Works on pixels         | Works on frequencies         |
| Faster                  | More mathematical            |
| Simple implementation   | Requires Fourier Transform   |
| Brightness and contrast | Noise removal and sharpening |

---

# 3. Gray Level Transformations

Gray-level transformations modify the intensity values of pixels.

## (a) Image Negative

Formula

$$[
s=L-1-r
]$$

where:

* (L) = number of gray levels
* (r) = original pixel
* (s) = new pixel

For an 8-bit image:

[
s=255-r
]

**Use**

* Medical images
* X-ray images

---

## (b) Log Transformation

Formula

$$[
s=c\log(1+r)
]$$

**Purpose**

* Expands dark pixels
* Compresses bright pixels

**Application**

* Satellite images

---

## (c) Power Law (Gamma Transformation)

Formula

$$[
s=cr^\gamma
]$$

where $(\gamma)$ (gamma) controls brightness.

* $(\gamma < 1$): image becomes brighter
* $(\gamma > 1)$: image becomes darker

---

## (d) Contrast Stretching

Increases the difference between dark and bright pixels.

**Purpose**

* Improve visibility
* Increase contrast

---

## (e) Thresholding

Converts a grayscale image into a binary image.

Rule:

```
Pixel > Threshold → White (1)

Pixel ≤ Threshold → Black (0)
```

---

# 4. Histogram

### Definition

A histogram is a graph showing the number of pixels at each gray level.

Horizontal axis:

* Gray level (0–255)

Vertical axis:

* Number of pixels

---

# 5. Histogram Equalization

### Definition

Histogram Equalization automatically improves image contrast by spreading pixel values over the full intensity range.

**Advantages**

* Better contrast
* More visible details
* Automatic method

---

# 6. Histogram Matching (Specification)

### Definition

Histogram Matching changes the histogram of one image to match a specified histogram.

Difference:

* Histogram Equalization → automatic distribution
* Histogram Matching → user-defined distribution

---

# 7. Histogram Processing

Histogram processing includes techniques such as:

* Histogram equalization
* Histogram matching
* Contrast stretching

**Purpose**

* Improve image quality
* Enhance contrast

---

# 8. Local Enhancement

Instead of enhancing the entire image, only a small neighborhood around each pixel is processed.

**Advantage**

* Better enhancement in local regions

**Example**

* Brightening a face while leaving the background unchanged

---

# 9. Image Subtraction

Subtracts one image from another.

Formula

$$[
g(x,y)=f_1(x,y)-f_2(x,y)
]$$

**Applications**

* Motion detection
* Medical image comparison
* Change detection

---

# 10. Image Averaging

Adds multiple images and divides by the number of images.

Formula

$$[
g(x,y)=\frac{1}{N}\sum_{i=1}^{N}f_i(x,y)
]$$

**Purpose**

* Reduce random noise
* Produce a cleaner image

---

# 11. Spatial Filtering

### Definition

Spatial filtering modifies a pixel based on its neighboring pixels using a small matrix called a **kernel** or **mask**.

---

# 12. Smoothing Filters

### Purpose

Reduce noise and blur the image.

Also called:

* Low-pass filters

Examples:

* Mean filter
* Gaussian filter
* Median filter

### Mean Filter

Replaces the center pixel with the average of neighboring pixels.

Advantages:

* Simple
* Removes small noise

Disadvantage:

* Blurs edges

---

### Median Filter

Replaces the center pixel with the median value of its neighbors.

Advantages:

* Removes salt-and-pepper noise
* Preserves edges better than the mean filter

---

# 13. Sharpening Filters

### Purpose

Increase edge sharpness and highlight fine details.

Also called:

* High-pass filters

Examples:

* Laplacian filter
* Sobel filter
* Prewitt filter

---

### Laplacian Filter

Uses the second derivative to detect edges.

Application:

* Edge enhancement

---

# Part B: Fourier Transform

## 14. Fourier Transform (FT)

### Definition

Fourier Transform converts an image from the spatial domain into the frequency domain.

It separates:

* Low frequencies (smooth regions)
* High frequencies (edges and noise)

---

## 15. Discrete Fourier Transform (DFT)

Since digital images are discrete, the **Discrete Fourier Transform (DFT)** is used.

**Purpose**

* Analyze image frequencies
* Perform frequency-domain filtering

---

## 16. Fast Fourier Transform (FFT)

### Definition

FFT is a fast algorithm for computing the DFT.

Advantages:

* Faster computation
* Less processing time
* Used in real-time image processing

---

## Difference: FT, DFT, FFT

| FT                     | DFT                          | FFT                           |
| ---------------------- | ---------------------------- | ----------------------------- |
| Continuous signals     | Discrete signals             | Fast algorithm for DFT        |
| Mathematical transform | Practical for digital images | Most efficient implementation |

---

## 17. Fourier Properties

Important properties:

### Linearity

Transform of a sum equals the sum of the transforms.

### Symmetry

Useful for real-valued images.

### Translation

Shifting an image changes only the phase, not the magnitude.

### Scaling

Changing image size changes its frequency representation.

---

## 18. Two-Dimensional Fourier Transform (2D FT)

Images are two-dimensional, so the **2D Fourier Transform** is used.

It converts:

* Rows
* Columns

into frequency components.

---

## 19. Inverse Fourier Transform (IFT)

Converts the frequency-domain image back into the spatial-domain image after processing.

---

# Part C: Filtering in Frequency Domain

## 20. Frequency Domain Filtering

### Steps

```
Input Image

↓

Fourier Transform

↓

Apply Frequency Filter

↓

Inverse Fourier Transform

↓

Output Image
```

---

## 21. Relationship Between Spatial and Frequency Filtering

Both methods aim to improve image quality.

* Spatial filtering works directly on pixel values.
* Frequency filtering works on frequency components.

According to the **Convolution Theorem**:

> Convolution in the spatial domain is equivalent to multiplication in the frequency domain.

---

# 22. Smoothing Frequency Filters

Purpose:

* Remove noise
* Blur the image

Also called:

* Low-pass filters

Types:

* Ideal Low-Pass Filter (ILPF)
* Butterworth Low-Pass Filter (BLPF)
* Gaussian Low-Pass Filter (GLPF)

---

## 23. Sharpening Frequency Filters

Purpose:

* Enhance edges
* Increase image sharpness

Also called:

* High-pass filters

Types:

* Ideal High-Pass Filter (IHPF)
* Butterworth High-Pass Filter (BHPF)
* Gaussian High-Pass Filter (GHPF)

---

# Low-Pass vs High-Pass Filters

| Low-Pass Filter        | High-Pass Filter        |
| ---------------------- | ----------------------- |
| Passes low frequencies | Passes high frequencies |
| Removes noise          | Enhances edges          |
| Smooths image          | Sharpens image          |
| Blurs details          | Highlights fine details |

---

# Spatial vs Frequency Filtering

| Spatial Filtering          | Frequency Filtering                  |
| -------------------------- | ------------------------------------ |
| Operates on pixels         | Operates on frequencies              |
| Uses kernels/masks         | Uses Fourier Transform               |
| Easier to implement        | More computationally intensive       |
| Good for local enhancement | Better for global frequency analysis |

---

# Exam Tips (Most Important Questions)

### 2 Marks

* Define image enhancement.
* Define histogram.
* What is histogram equalization?
* Define Fourier Transform.
* What is FFT?
* Define low-pass and high-pass filters.
* Define image subtraction and image averaging.

### 5 Marks

* Explain gray-level transformations.
* Explain histogram equalization and histogram matching.
* Explain smoothing and sharpening spatial filters.
* Explain Fourier Transform, DFT, and FFT.
* Explain frequency-domain filtering.

### 10 Marks

* Explain image enhancement in the spatial domain with suitable examples.
* Explain histogram processing techniques.
* Explain Fourier Transform and its properties.
* Explain filtering in the frequency domain with a neat block diagram.
* Differentiate spatial-domain and frequency-domain filtering.

### **Memory Trick**

* **Spatial Domain** → **Directly changes pixels** (brightness, contrast, filtering with masks).
* **Frequency Domain** → **Changes frequencies** using the **Fourier Transform** (low frequencies = smooth areas, high frequencies = edges/noise).
* **Low-Pass Filter** → Smooths the image, removes noise.
* **High-Pass Filter** → Sharpens the image, enhances edges.
