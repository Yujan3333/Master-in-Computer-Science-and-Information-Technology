#ippr #third-semester 

---

# Derive the Equation for Hyperbolic Filter and Write the Algorithm for its Implementation. **[3+3 Marks]**

---

# (a) Derivation of Hyperbolic Filter Equation (3 Marks)

## Definition

A **Hyperbolic Filter** is a spatial smoothing filter in which the weight assigned to a neighboring pixel decreases **hyperbolically** as its distance from the center increases.

It smooths the image while preserving more details than a simple averaging filter.

---

## Distance from the Center

For a neighboring pixel located at $(x,y)$ with respect to the center,

$$
d=\sqrt{x^2+y^2}
$$

---

## Hyperbolic Weight Function

The weight is inversely proportional to the distance:

$$
w(x,y)=\frac{1}{1+d}
$$

Substituting $d$,

$$
w(x,y)=\frac{1}{1+\sqrt{x^2+y^2}}
$$

This is the **hyperbolic weighting function**.

---

## Filtered Pixel

The output pixel is obtained by the weighted average:

$$
g(x,y)=
\frac{\displaystyle\sum w(i,j)f(x+i,y+j)}
{\displaystyle\sum w(i,j)}
$$

where

* $f(x,y)$ = Input image
* $g(x,y)$ = Output image
* $w(i,j)$ = Hyperbolic weights

The denominator normalizes the weights so that the output intensity remains in the valid range.

---

# Typical $3\times3$ Hyperbolic Mask

Using the above equation, a commonly used normalized mask is approximately

$$
\begin{bmatrix}
0.41 & 0.50 & 0.41\
0.50 & 1.00 & 0.50\
0.41 & 0.50 & 0.41
\end{bmatrix}
$$

After normalization (divide each element by the sum of all weights), it is used for filtering.

> **Note:** Different textbooks may use slightly different normalized values, but they are all derived from the same hyperbolic weighting function.

---

# (b) Algorithm for Hyperbolic Filter (3 Marks)

### Algorithm

**Input:** Image $f(x,y)$

**Output:** Smoothed image $g(x,y)$

1. Read the input image.

2. Choose a neighborhood (usually $3\times3$).

3. Compute the distance of each neighboring pixel from the center.

4. Compute the weight for each neighbor using

   $$
   w=\frac{1}{1+\sqrt{x^2+y^2}}
   $$

5. Normalize the weights so that their sum equals 1.

6. Multiply each neighboring pixel by its corresponding weight.

7. Sum all weighted values to obtain the new pixel value.

8. Repeat for every pixel in the image.

9. Display the filtered image.

---

# Applications

* Image smoothing
* Noise reduction
* Medical image enhancement
* Satellite image processing

---

# Advantages

* Smooths the image effectively.
* Gives higher importance to the center pixel.
* Preserves edges better than a simple averaging filter.

---

# Disadvantages

* Some image blurring still occurs.
* More computations than a simple mean filter.

---

# Exam Answer (3+3 Marks)

### (a) Hyperbolic Filter Equation (3 Marks)

The hyperbolic filter is a spatial smoothing filter whose weights decrease hyperbolically with distance from the center.

Distance:

$$
d=\sqrt{x^2+y^2}
$$

Weight function:

$$
w(x,y)=\frac{1}{1+\sqrt{x^2+y^2}}
$$

Filtered output:

$$
g(x,y)=
\frac{\displaystyle\sum w(i,j)f(x+i,y+j)}
{\displaystyle\sum w(i,j)}
$$

---

### (b) Algorithm (3 Marks)

1. Read the input image.

2. Select a $3\times3$ neighborhood.

3. Compute the distance of each neighbor from the center.

4. Calculate weights using

   $$
   w=\frac{1}{1+\sqrt{x^2+y^2}}
   $$

5. Normalize the weights.

6. Multiply each pixel by its weight.

7. Sum the weighted values to obtain the output pixel.

8. Repeat for all pixels.

> **Exam Tip:** If asked to "derive the filter mask," first derive the weight equation, then calculate the weights for the $3\times3$ neighborhood and finally normalize them. This usually earns full marks.
