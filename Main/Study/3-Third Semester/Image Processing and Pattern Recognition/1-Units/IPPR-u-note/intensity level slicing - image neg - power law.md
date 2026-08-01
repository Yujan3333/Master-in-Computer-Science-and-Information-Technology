#ippr #third-semester 

# Explain the intensity level slicing, the image negative and the power law transformation techniques for the purpose of image enhancement. **[2+1+3 Marks]**

---

# (a) Intensity Level Slicing (2 Marks)

## Definition

**Intensity Level Slicing** is an image enhancement technique that **highlights a specific range of gray levels** while suppressing or leaving other gray levels unchanged.

It is used to emphasize important objects whose intensities lie within a particular range.

---

## Types

### 1. Slicing without background

Pixels within the selected intensity range are assigned the maximum intensity, while all other pixels are set to zero.

$$
s=
\begin{cases}
L-1, & A\le r\le B\\
0, & \text{otherwise}
\end{cases}
$$

---

### 2. Slicing with background

Pixels within the selected range are highlighted, while all other pixels retain their original intensity.

$$
s=
\begin{cases}
L-1, & A\le r\le B\\
r, & \text{otherwise}
\end{cases}
$$

---

### Example

Suppose the gray levels of interest are between

$$
80 \le r \le 150.
$$

Only pixels in this range are highlighted to make the desired object more visible.

---

### Applications

* Medical image analysis
* Satellite image enhancement
* Defect detection
* Object highlighting

---

# (b) Image Negative (1 Mark)

## Definition

An **image negative transformation** reverses the gray levels of an image by converting bright pixels into dark pixels and dark pixels into bright pixels.

It is useful for enhancing **white or gray details embedded in dark regions**.

---

## Formula

$$
s=(L-1)-r
$$

where

* $r$ = Input gray level
* $s$ = Output gray level
* $L$ = Number of gray levels

For an 8-bit image,

$$
s=255-r
$$

---

### Example

If

$$
r=80,
$$

then

$$
s=255-80=175.
$$

---

### Applications

* X-ray image enhancement
* Medical imaging
* Photography
* Remote sensing

---

# (c) Power Law (Gamma) Transformation (3 Marks)

## Definition

The **Power Law Transformation**, also called **Gamma Transformation**, enhances an image by applying a power function to the pixel intensities.

It is mainly used to **correct brightness and improve contrast**.

---

## Formula

$$
s=c,r^\gamma
$$

where

* $r$ = Input gray level
* $s$ = Output gray level
* $c$ = Constant
* $\gamma$ = Gamma value

---

## Effect of Gamma

### 1. When

$$
\gamma<1
$$

* Image becomes brighter.
* Dark regions are enhanced.

---

### 2. When

$$
\gamma>1
$$

* Image becomes darker.
* Bright regions are compressed.

---

### 3. When

$$
\gamma=1
$$

The image remains unchanged.

---

### Example

If

$$
r=0.5,\quad c=1,\quad \gamma=2,
$$

then

$$
s=(0.5)^2=0.25.
$$

The output becomes darker.

---

### Applications

* Gamma correction of displays
* Medical imaging
* Satellite image enhancement
* Image preprocessing

---

# Difference Between the Three Techniques

| Intensity Level Slicing                     | Image Negative                    | Power Law Transformation                   |
| ------------------------------------------- | --------------------------------- | ------------------------------------------ |
| Highlights a selected range of gray levels. | Reverses gray levels.             | Adjusts brightness using gamma correction. |
| Enhances specific objects.                  | Enhances details in dark regions. | Controls brightness and contrast.          |
| Based on intensity range.                   | Based on intensity inversion.     | Based on exponential transformation.       |

---

# Exam Answer (2+1+3 Marks)

### (a) Intensity Level Slicing (2 Marks)

Intensity level slicing is an image enhancement technique that highlights a selected range of gray levels while suppressing or preserving the remaining gray levels. It is mainly used to emphasize objects of interest.

Formula (without background):

$$
s=
\begin{cases}
L-1, & A\le r\le B\\
0, & \text{otherwise}
\end{cases}
$$

Formula (with background):

$$
s=
\begin{cases}
L-1, & A\le r\le B\\
r, & \text{otherwise}
\end{cases}
$$

---

### (b) Image Negative (1 Mark)

Image negative transforms each gray level into its complement.

$$
s=(L-1)-r
$$

For an 8-bit image,

$$
s=255-r
$$

It is useful for enhancing white or gray details in dark regions.

---

### (c) Power Law Transformation (3 Marks)

Power law (gamma) transformation modifies image brightness according to

$$
s=c,r^\gamma
$$

* $\gamma<1$ → brighter image
* $\gamma>1$ → darker image
* $\gamma=1$ → no change

It is widely used for **gamma correction, brightness adjustment, and contrast enhancement**.
