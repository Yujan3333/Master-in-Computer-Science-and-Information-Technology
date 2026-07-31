#ippr 
## What is Contrast?

**Contrast** is the **difference in intensity (brightness)** between the darkest and the brightest parts of an image.

* **High contrast** → Large difference between dark and bright regions.
* **Low contrast** → Small difference between dark and bright regions.

---

### Example

#### High Contrast

$$
\text{Intensity values: } 0,;20,;240,;255
$$

The image has very dark blacks and very bright whites.

```text
Black ███░░░░░░ White
```

The objects are easy to distinguish.

---

#### Low Contrast

$$
\text{Intensity values: } 110,;120,;130,;140
$$

All pixels have similar brightness.

```text
Gray ▓▓▓▓▓▓▓▓▓ Gray
```

The image looks dull and details are difficult to see.

---

## Simple Definition (Exam)

> **Contrast** is the difference in brightness (gray-level intensity) between the darkest and brightest regions of an image. It determines how clearly objects can be distinguished from the background.

---

## Example Using Pixel Values

### High Contrast

$$
\begin{bmatrix}
0 & 0 & 255 \
0 & 255 & 255 \
255 & 255 & 0
\end{bmatrix}
$$

The image contains both black and white pixels, so the contrast is **high**.

---

### Low Contrast

$$
\begin{bmatrix}
120 & 125 & 122 \
124 & 126 & 121 \
123 & 124 & 125
\end{bmatrix}
$$

All pixel values are close together, so the contrast is **low**.

---

## Why is Contrast Important?

Good contrast helps to:

* Distinguish objects from the background.
* Reveal hidden details.
* Improve image quality.
* Make image analysis easier.

---

## Contrast Enhancement

If an image has low contrast, we can improve it using techniques such as:

* **Contrast stretching**
* **Histogram equalization**
* **Gamma correction**

These methods spread the gray-level values over a wider range, making the image clearer.

---

## One-Line Memory Tip

* **Brightness** = How light or dark the **whole image** is.
* **Contrast** = How **different** the bright and dark parts of the image are.
