#ippr #third-semester 
# Explain the First Derivative Filter with an Example. Derive the Filter Mask for Elliptical Filter and Write the Algorithm for its Implementation. **[2+6+2 Marks]**

---

# (a) First Derivative Filter (2 Marks)

## Definition

A **First Derivative Filter** is a **spatial sharpening filter** used to detect **edges** by measuring the rate of change of image intensity.

* If the intensity changes slowly, the derivative is small.
* If the intensity changes suddenly (at an edge), the derivative is large.

Thus, the first derivative highlights image boundaries.

---

## Mathematical Expression

For a one-dimensional signal,

$$
\frac{df(x)}{dx}
$$

For a digital image, the first derivative is approximated by

$$
\frac{\partial f}{\partial x}\approx f(x+1,y)-f(x,y)
$$

and

$$
\frac{\partial f}{\partial y}\approx f(x,y+1)-f(x,y)
$$

---

## Example

Consider the pixel values

$$
[10,;10,;10,;80,;80,;80]
$$

The first differences are

$$
[0,;0,;70,;0,;0]
$$

The large value **70** indicates the location of the edge.

---

## Common First Derivative Masks

**Horizontal (Prewitt):**

$$
\begin{bmatrix}
-1&0&1\\
-1&0&1\\
-1&0&1
\end{bmatrix}
$$

**Vertical (Prewitt):**

$$
\begin{bmatrix}
-1&-1&-1\\
0&0&0\\
1&1&1
\end{bmatrix}
$$

These masks detect vertical and horizontal edges, respectively.

---

# (b) Derive the Filter Mask for Elliptical Filter (6 Marks)

## Definition

The **Elliptical Filter** is a weighted spatial smoothing filter in which the weights are distributed according to an **elliptical distance** from the center pixel.

Pixels closer to the center receive larger weights, while distant pixels receive smaller weights.

---

## Elliptical Distance

For a neighboring pixel,

$$
d=\sqrt{\frac{x^2}{a^2}+\frac{y^2}{b^2}}
$$

where

* $a$ = Major axis
* $b$ = Minor axis

---

## Weight Function

The weight assigned to each pixel is

$$
w(x,y)=\frac{1}{1+d}
$$

Substituting the elliptical distance,

$$
w(x,y)=
\frac{1}
{1+\sqrt{\frac{x^2}{a^2}+\frac{y^2}{b^2}}}
$$

---

## Filtered Output

The output pixel is

$$
g(x,y)=
\frac{\displaystyle\sum w(i,j)f(x+i,y+j)}
{\displaystyle\sum w(i,j)}
$$

where

* $f(x,y)$ = Input image
* $g(x,y)$ = Output image
* $w(i,j)$ = Elliptical weights

---

## Typical Elliptical Filter Mask

A commonly used normalized elliptical mask is

$$
\frac{1}{16}
\begin{bmatrix}
1&2&1\\
2&4&2\\
1&2&1
\end{bmatrix}
$$

The center pixel has the highest weight, and the surrounding weights decrease according to the elliptical distribution.

---

## Characteristics

* Smooths the image.
* Reduces noise.
* Preserves edges better than a simple averaging filter.
* Gives higher importance to the center pixel.

---

# (c) Algorithm for Elliptical Filter (2 Marks)

### Algorithm

1. Read the input image.

2. Select a neighborhood (usually $3\times3$).

3. Compute the elliptical distance for each neighboring pixel.

4. Calculate the weight using

   $$
   w=\frac{1}{1+\sqrt{\frac{x^2}{a^2}+\frac{y^2}{b^2}}}
   $$

5. Normalize the weights.

6. Multiply each neighboring pixel by its corresponding weight.

7. Sum the weighted values to obtain the output pixel.

8. Repeat for all pixels in the image.

9. Display the filtered image.

---

# Applications

* Noise reduction
* Medical image enhancement
* Satellite image processing
* Image smoothing before segmentation

---

# Exam Answer (2+6+2 Marks)

### (a) First Derivative Filter (2 Marks)

A **First Derivative Filter** is a sharpening filter used to detect edges by measuring the rate of change of pixel intensity. A large derivative indicates the presence of an edge.

$$
\frac{\partial f}{\partial x}\approx f(x+1,y)-f(x,y)
$$

Example:

$$
[10,;10,;10,;80,;80,;80]
\rightarrow
[0,;0,;70,;0,;0]
$$

showing an edge at the large intensity change.

---

### (b) Elliptical Filter (6 Marks)

The elliptical filter assigns weights based on the elliptical distance

$$
d=\sqrt{\frac{x^2}{a^2}+\frac{y^2}{b^2}}
$$

Weight function:

$$
w(x,y)=
\frac{1}
{1+\sqrt{\frac{x^2}{a^2}+\frac{y^2}{b^2}}}
$$

Filtered output:

$$
g(x,y)=
\frac{\displaystyle\sum w(i,j)f(x+i,y+j)}
{\displaystyle\sum w(i,j)}
$$

A commonly used mask is

$$
\frac{1}{16}
\begin{bmatrix}
1&2&1\\
2&4&2\\
1&2&1
\end{bmatrix}
$$

---

### (c) Algorithm (2 Marks)

1. Read the image.
2. Select a $3\times3$ neighborhood.
3. Compute elliptical weights.
4. Normalize the weights.
5. Multiply neighboring pixels by their weights.
6. Sum the weighted values to obtain the new pixel.
7. Repeat for all pixels.
