
#ippr #third-semester 

# Line Detection

## Definition

**Line detection** is the process of identifying straight lines in an image by detecting pixels whose intensity values form a linear pattern in a particular direction.

It is a fundamental image segmentation technique used to extract line features from an image.

---

# Principle

Line detection is performed by **convolving the image with directional masks (kernels)**. Each mask is designed to detect lines in a specific direction.

If the convolution response is **large**, a line exists in that direction.

---

# Line Detection Masks

## Horizontal Line

$$
\begin{bmatrix}
-1 & -1 & -1 \\
2 & 2 & 2 \\
-1 & -1 & -1
\end{bmatrix}
$$

Detects **horizontal lines**.

---

## Vertical Line

$$
\begin{bmatrix}
-1 & 2 & -1 \\
-1 & 2 & -1 \\
-1 & 2 & -1
\end{bmatrix}
$$

Detects **vertical lines**.

---

## +45° Diagonal Line

$$
\begin{bmatrix}
-1 & -1 & 2 \\
-1 & 2 & -1 \\
2 & -1 & -1
\end{bmatrix}
$$

Detects **$+45^\circ$ diagonal lines**.

---

## -45° Diagonal Line

$$
\begin{bmatrix}
2 & -1 & -1 \\
-1 & 2 & -1 \\
-1 & -1 & 2
\end{bmatrix}
$$

Detects **$-45^\circ$ diagonal lines**.

---

# Algorithm

1. Read the input image.
2. Select the line detection mask according to the desired direction.
3. Perform convolution between the image and the mask.
4. Compute the response at every pixel.
5. Compare the response with a predefined threshold.
6. Pixels with responses greater than the threshold are marked as line pixels.
7. Display the detected lines.

---

# Example

Consider a horizontal line:

$$
\begin{bmatrix}
0 & 0 & 0 \\
255 & 255 & 255 \\
0 & 0 & 0
\end{bmatrix}
$$

Applying the horizontal mask

$$
\begin{bmatrix}
-1 & -1 & -1 \\
2 & 2 & 2 \\
-1 & -1 & -1
\end{bmatrix}
$$

produces a **high positive response**, confirming the presence of a horizontal line.

---

# Advantages

* Simple to implement.
* Detects lines in specific directions.
* Fast computation.
* Useful for feature extraction.

---

# Disadvantages

* Sensitive to noise.
* Separate masks are required for different directions.
* Not suitable for curved or irregular lines.

---

# Applications

* Road and lane detection
* OCR (Optical Character Recognition)
* Medical image analysis
* Fingerprint recognition
* Industrial inspection
* Document processing

---

# Exam Tips

### Remember the Four Masks

* Horizontal
* Vertical
* $+45^\circ$ diagonal
* $-45^\circ$ diagonal

### Key Idea

A line is detected when the **convolution response is maximum** for the corresponding directional mask.

### One-Line Definition

> **Line detection** is the process of detecting straight lines in an image by convolving the image with directional masks and identifying pixels with high responses.
