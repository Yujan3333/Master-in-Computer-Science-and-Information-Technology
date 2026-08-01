#ippr #third-semester 
# 4. Explain How a Point and Edges Can Be Detected in an Image. **[5 Marks]** *(Asked in 2076)*

Point detection and edge detection are fundamental techniques in digital image processing used to identify important features in an image.

---

# (a) Point Detection

## Definition

**Point detection** is the process of identifying isolated pixels whose intensity is significantly different from their neighboring pixels.

For example, a bright pixel surrounded by dark pixels (or vice versa) is detected as an isolated point.

---

## Principle

A mask (kernel) is moved over the image.

If the response of the mask is greater than a predefined threshold, the center pixel is detected as a point.

---

## Point Detection Mask

$$
\boxed{
\begin{bmatrix}
-1 & -1 & -1\\
-1 & 8 & -1\\
-1 & -1 & -1
\end{bmatrix}
}
$$

* Center pixel has a large positive weight.
* Neighboring pixels have negative weights.
* A large response indicates an isolated point.

---

## Formula

$$
R=\sum_{i=-1}^{1}\sum_{j=-1}^{1} w(i,j),f(x+i,y+j)
$$

where

* $R$ = mask response
* $w(i,j)$ = mask values
* $f(x,y)$ = image pixel values

If

$$
|R|>T
$$

then the center pixel is detected as a point.

---

## Example

Image

```text
20   20   20
20  200   20
20   20   20
```

Applying the point detection mask,

$$
R=(8\times200)-8\times20
$$

$$
=1600-160
$$

$$
=1440
$$

Since $R>T$, the center pixel is detected as an isolated point.

---

# (b) Edge Detection

## Definition

**Edge detection** identifies pixels where there is a sudden change in intensity.

Edges represent the boundaries of objects.

---

## Principle

Edges occur where the **first derivative (gradient)** or **second derivative** of intensity is large.

The image is convolved with an edge detection operator.

---

## Common Edge Detection Operators

### 1. Roberts Operator

$$
G_x=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\qquad
G_y=
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}
$$

* Uses a $2\times2$ mask.
* Detects diagonal edges.
* Sensitive to noise.

---

### 2. Prewitt Operator

Horizontal mask

$$
G_x=
\begin{bmatrix}
-1&0&1\\
-1&0&1\\
-1&0&1
\end{bmatrix}
$$

Vertical mask

$$
G_y=
\begin{bmatrix}
-1&-1&-1\\
0&0&0\\
1&1&1
\end{bmatrix}
$$

* Detects horizontal and vertical edges.
* Simple to implement.

---

### 3. Sobel Operator (Most Common)

Horizontal mask

$$
G_x=
\begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix}
$$

Vertical mask

$$
G_y=
\begin{bmatrix}
-1&-2&-1\\
0&0&0\\
1&2&1
\end{bmatrix}
$$

* Gives higher weight to center pixels.
* Better noise resistance than Prewitt.

---

## Gradient Magnitude

The edge strength is calculated as

$$
G=\sqrt{G_x^2+G_y^2}
$$

or approximately

$$
G=|G_x|+|G_y|
$$

If the gradient magnitude exceeds a threshold, the pixel is classified as an edge.

---

## Example

Original image

```text
10   10   10
10   10   10
200 200 200
```

There is a sudden intensity change from **10** to **200**, so the boundary between the two regions is detected as an edge.

---

# Difference Between Point Detection and Edge Detection

| Point Detection                  | Edge Detection                                               |
| -------------------------------- | ------------------------------------------------------------ |
| Detects isolated pixels.         | Detects object boundaries.                                   |
| Uses a point detection mask.     | Uses gradient operators such as Sobel, Prewitt, and Roberts. |
| Finds single bright/dark points. | Finds continuous edges.                                      |

---

# Applications

### Point Detection

* Detecting stars in astronomical images.
* Detecting defects in industrial inspection.
* Finding isolated bright spots.

### Edge Detection

* Object recognition.
* Image segmentation.
* Medical image analysis.
* Face detection.
* Computer vision.

---

# **Exam Answer (5 Marks)**

**Point Detection:**
Point detection identifies isolated pixels whose intensity differs significantly from neighboring pixels. It commonly uses the mask

$$
\begin{bmatrix}
-1&-1&-1\\
-1&8&-1\\
-1&-1&-1
\end{bmatrix}
$$

If the mask response satisfies $|R|>T$, the center pixel is detected as a point.

**Edge Detection:**
Edge detection identifies object boundaries by detecting sudden intensity changes. It is commonly performed using **Roberts, Prewitt, and Sobel operators**. The Sobel operator is widely used because it provides better noise resistance.

The edge magnitude is computed as

$$
G=\sqrt{G_x^2+G_y^2}
$$

or

$$
G=|G_x|+|G_y|.
$$

Pixels with gradient magnitude above a threshold are considered edges.

---

## ⭐ Exam Tip

Remember these three important masks.

### Point Detection

$$
\boxed{
\begin{bmatrix}
-1&-1&-1\\
-1&8&-1\\
-1&-1&-1
\end{bmatrix}
}
$$

### Sobel Horizontal

$$
\boxed{
\begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix}
}
$$

### Sobel Vertical

$$
\boxed{
\begin{bmatrix}
-1&-2&-1\\
0&0&0\\
1&2&1
\end{bmatrix}
}
$$

I will use your preferred LaTeX style from now on:

* Inline math with `$...$`
* Display math with `$$...$$`
* Never `\[...\]` or `\(...\)` unless you specifically ask for it.
