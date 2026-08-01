#ippr #third-semester 

# What is Boundary? Explain Spatial Weighted Averaging Filter with Suitable Example. **[1+4 Marks]**

## (a) Boundary (1 Mark)

A **boundary** is the **border or edge of an image** where neighboring pixels required for filtering are unavailable.

When applying a filter (e.g., a $3 \times 3$ mask), pixels on the image boundary do not have enough surrounding neighbors. Therefore, special boundary handling methods are used.

### Common Boundary Handling Methods

* **Zero padding:** Add zeros around the image.
* **Replication:** Repeat the border pixels.
* **Reflection:** Mirror the image at the boundary.
* **Wrap-around:** Copy pixels from the opposite side.

---

## (b) Spatial Weighted Averaging Filter (4 Marks)

### Definition

A **spatial weighted averaging filter** is a **linear smoothing filter** that replaces the center pixel with the **weighted average** of its neighboring pixels.

Unlike the simple averaging filter, different neighbors are assigned different weights. Usually, the center pixel has the highest weight, giving it more influence on the output.

It is mainly used for:

* Noise reduction
* Image smoothing
* Blur while preserving more image detail than a simple averaging filter

---

## Formula

If the filter mask is

$$
W(i,j)
$$

then the output pixel is

$$
g(x,y)=\frac{\sum W(i,j),f(x+i,y+j)}{\sum W(i,j)}
$$

where

* $f(x,y)$ = Input image
* $W(i,j)$ = Weight mask
* $g(x,y)$ = Output image

---

## Common $3 \times 3$ Weighted Averaging Mask

$$
\frac{1}{16}
\begin{bmatrix}
1 & 2 & 1\\
2 & 4 & 2\\
1 & 2 & 1
\end{bmatrix}
$$

The weights sum to

$$
1+2+1+2+4+2+1+2+1=16
$$

Hence, divide by 16 to normalize the result.

---

## Example

Consider the following neighborhood:

$$
\begin{bmatrix}
10 & 20 & 30\\
20 & 40 & 20\\
30 & 20 & 10
\end{bmatrix}
$$

Apply the weighted averaging mask:

$$
\frac{1}{16}
\begin{bmatrix}
1 & 2 & 1\\
2 & 4 & 2\\
1 & 2 & 1
\end{bmatrix}
$$

Multiply corresponding elements:

$$
=(1\times10)+(2\times20)+(1\times30)
$$

$$
+(2\times20)+(4\times40)+(2\times20)
$$

$$
+(1\times30)+(2\times20)+(1\times10)
$$

$$
=10+40+30+40+160+40+30+40+10
$$

$$
=400
$$

Now divide by the sum of weights:

$$
g(x,y)=\frac{400}{16}=25
$$

Therefore, the filtered center pixel is

$$
\boxed{25}
$$

---

## Advantages

* Reduces random noise.
* Produces smoother images.
* Gives more importance to the center pixel.
* Preserves edges better than a simple averaging filter.

---

## Disadvantages

* Causes some image blurring.
* Fine details may be lost if applied repeatedly.

---

# Exam Answer (5 Marks)

**Boundary:**
A **boundary** is the edge of an image where neighboring pixels required for filtering are unavailable. Boundary handling methods such as **zero padding, replication, reflection, and wrap-around** are used to process these pixels.

**Spatial Weighted Averaging Filter:**
A spatial weighted averaging filter is a smoothing filter that computes the output pixel as the **weighted average** of neighboring pixels. Unlike a simple averaging filter, different weights are assigned to different pixels, with the center pixel usually receiving the highest weight.

The output is computed as

$$
g(x,y)=\frac{\sum W(i,j),f(x+i,y+j)}{\sum W(i,j)}
$$

A commonly used mask is

$$
\frac{1}{16}
\begin{bmatrix}
1 & 2 & 1\
2 & 4 & 2\
1 & 2 & 1
\end{bmatrix}
$$

This filter is used for **noise reduction and image smoothing** while preserving more image detail than a simple averaging filter.
