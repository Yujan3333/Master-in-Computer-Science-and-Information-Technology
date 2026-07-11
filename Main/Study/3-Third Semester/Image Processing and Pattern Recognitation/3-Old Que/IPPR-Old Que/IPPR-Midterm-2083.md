#ippr #third-semester #old-que #exam-paper-answer 

# Q1. Describe the fundamental steps in Digital Image Processing with a block diagram. What is the difference between a low-pass filter and high-pass filter in the spatial domain?

## Fundamental Steps in Digital Image Processing

### Definition

Digital Image Processing (DIP) is the process of using a computer to improve image quality or extract useful information from digital images.

### Block Diagram

```text
Image Acquisition
        ↓
Image Enhancement
        ↓
Image Restoration
        ↓
Color Image Processing
        ↓
Compression
        ↓
Morphological Processing
        ↓
Segmentation
        ↓
Feature Extraction
        ↓
Recognition & Interpretation
```

### Explanation of Steps

### 1. Image Acquisition

* Captures the image using a camera or scanner.
* Converts it into digital form.

### 2. Image Enhancement

* Improves image quality.
* Example: Increase brightness and contrast.

### 3. Image Restoration

* Removes blur and noise using mathematical methods.

### 4. Color Image Processing

* Processes color images such as RGB images.

### 5. Image Compression

* Reduces image size for storage and transmission.

### 6. Morphological Processing

* Processes object shapes using operations like erosion and dilation.

### 7. Image Segmentation

* Divides the image into meaningful regions or objects.

### 8. Feature Extraction

* Extracts important features like shape, texture, and edges.

### 9. Recognition and Interpretation

* Identifies and classifies objects in the image.

---

## Difference Between Low-Pass Filter and High-Pass Filter

| Low-Pass Filter                       | High-Pass Filter                 |
| ------------------------------------- | -------------------------------- |
| Passes low-frequency components       | Passes high-frequency components |
| Removes noise                         | Enhances edges                   |
| Smooths or blurs the image            | Sharpens the image               |
| Also called smoothing filter          | Also called sharpening filter    |
| Example: Mean Filter, Gaussian Filter | Example: Laplacian, Sobel Filter |

---

# Q2. Differentiate between Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT). What is the purpose of using the Fourier Transform in image processing?

## Difference Between DFT and FFT

| Discrete Fourier Transform (DFT)                                  | Fast Fourier Transform (FFT)           |
| ----------------------------------------------------------------- | -------------------------------------- |
| Mathematical method to convert an image into the frequency domain | Fast algorithm used to compute the DFT |
| Slower computation                                                | Much faster computation                |
| High computational complexity                                     | Lower computational complexity         |
| Suitable for small datasets                                       | Suitable for large images              |
| Used for frequency analysis                                       | Used in real-time image processing     |

---

## Fourier Transform

### Definition

The **Fourier Transform (FT)** converts an image from the **spatial domain** into the **frequency domain**.

It separates the image into:

* **Low-frequency components** → Smooth regions
* **High-frequency components** → Edges and fine details

### Purpose of Fourier Transform in Image Processing

1. Converts the image into the frequency domain.
2. Removes noise using frequency filters.
3. Enhances image edges.
4. Performs frequency-domain filtering.
5. Compresses images.
6. Analyzes image frequency components.

### Block Diagram

```text
Input Image
      ↓
Fourier Transform
      ↓
Frequency Domain
      ↓
Filtering
      ↓
Inverse Fourier Transform
      ↓
Output Image
```

---

# Q3. What is Histogram Equalization in Image Enhancement? Illustrate with an example.

## Histogram Equalization

### Definition

**Histogram Equalization** is an image enhancement technique used to improve the **contrast** of an image by redistributing the gray-level values over the entire intensity range.

It spreads pixel values more uniformly, making hidden details easier to see.

---

## Why is Histogram Equalization Used?

* Improves image contrast.
* Enhances visibility of details.
* Makes dark images brighter.
* Produces a better gray-level distribution.

---

## Working Principle

1. Calculate the histogram of the image.
2. Compute the cumulative distribution function (CDF).
3. Map old gray levels to new gray levels.
4. Generate the enhanced image.

---

## Example

### Before Histogram Equalization

Suppose an image has pixel values concentrated between **100 and 130**.

```text
Gray Levels

0--------------------------------255

          ███████
       (100–130)
```

The image appears **dark with poor contrast**.

---

### After Histogram Equalization

The gray levels are spread across the full range.

```text
Gray Levels

0--------------------------------255

██████████████████████████████████
```

The image now has **better contrast**, and objects become more visible.

---

## Advantages

* Improves contrast automatically.
* Enhances hidden details.
* Easy to implement.
* Useful for medical and satellite images.

---

## Applications

* Medical imaging (X-ray, MRI)
* Satellite images
* Photography
* CCTV surveillance
* Fingerprint enhancement

---

## Exam Definition (2 Marks)

> **Histogram Equalization** is an image enhancement technique that improves image contrast by redistributing gray-level values over the entire intensity range.

---

## Important Exam Tips

* **Fundamental Steps in DIP**: Draw the complete block diagram and explain each step in 1–2 lines.
* **DFT vs FFT**: Remember that **DFT is the transform**, while **FFT is the efficient algorithm used to compute the DFT**.
* **Histogram Equalization**: Always mention that it **improves contrast by redistributing gray levels** and include a simple before/after histogram sketch for extra marks.
