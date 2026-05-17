#RGIS #assignment 
# Histogram of Image Data

A histogram is a graphical representation of the distribution of pixel intensity values in an image. It shows how many pixels are present for each gray level or brightness value.

For a grayscale image:

* X-axis → Gray level/intensity value (0–255)
* Y-axis → Number of pixels having that intensity

## Information Contained in Histogram

An image histogram provides the following information:

1. **Brightness of Image**

   * Histogram shifted to left → Dark image
   * Histogram shifted to right → Bright image

2. **Contrast**

   * Narrow histogram → Low contrast
   * Wide spread histogram → High contrast

3. **Intensity Distribution**

   * Shows frequency of different gray levels

4. **Dynamic Range**

   * Indicates the range of pixel values used in the image

5. **Image Quality**

   * Helps identify overexposed or underexposed images

6. **Threshold Selection**

   * Useful in image segmentation and classification

---

## Example

Suppose an image has pixel values:

$$
[10,\ 10,\ 20,\ 20,\ 20,\ 50,\ 50,\ 80]
$$

Histogram:

| Gray Level | Frequency |
| ---------- | --------- |
| 10         | 2         |
| 20         | 3         |
| 50         | 2         |
| 80         | 1         |

This indicates that intensity value 20 occurs most frequently.

---

# Focal Cell in Neighborhood Operation

In image processing, a neighborhood operation processes a pixel based on the values of surrounding pixels.

The **focal cell** is the center pixel on which the operation is currently being performed.

The neighboring cells around it are used to compute a new value for the focal cell.

---

# Neighborhood Operation

A small moving window (kernel/filter), such as $3\times3$, slides over the image.

Example operations:

* Smoothing
* Edge detection
* Sharpening
* Mean filtering

---

# Example of Focal Cell

Consider a $3\times3$ neighborhood:

$$
\begin{matrix}
2 & 4 & 6 \\
3 & 5 & 7 \\
1 & 8 & 9
\end{matrix}
$$

Here, the center value **5** is the focal cell.

If a mean filter is applied:

Formula:

$$\text{New Value}=\frac{\sum \text{Neighborhood Pixels}}{9}$$

Calculation:

$$
\frac{2+4+6+3+5+7+1+8+9}{9}
=
\frac{45}{9}
=
5
$$

So the updated value of the focal cell becomes 5.

---

# Summary

* A histogram shows the frequency distribution of image pixel intensities.
* A focal cell is the center pixel being processed in a neighborhood operation.
* Neighboring pixels are used to modify or analyze the focal cell value.
