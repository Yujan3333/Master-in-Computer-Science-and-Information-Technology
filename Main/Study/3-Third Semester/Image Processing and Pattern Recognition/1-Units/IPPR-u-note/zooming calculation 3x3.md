#ippr #third-semester 

# Q4. What is Zooming?

**Definition:**

**Zooming** is the process of enlarging a digital image by increasing its spatial resolution (number of pixels). New pixels are generated using techniques such as **replication (nearest neighbor)** or **interpolation**.

Given image:

$$
\begin{bmatrix}
1 & 7 & 6 \\
4 & 6 & 2 \\
1 & 5 & 3
\end{bmatrix}
$$

---

# Method 1: Zooming by Replication (2×)

In replication, **each pixel is copied** into a $$2 \times 2$$ block.

## Step 1: Original Image

$$
\begin{bmatrix}
1 & 7 & 6 \\
4 & 6 & 2 \\
1 & 5 & 3
\end{bmatrix}
$$

---

## Step 2: Replicate Each Pixel Horizontally

First row:

$$
1 ;; 7 ;; 6
$$

becomes

$$
1 ;; 1 ;; 7 ;; 7 ;; 6 ;; 6
$$

Second row:

$$
4 ;; 6 ;; 2
$$

becomes

$$
4 ;; 4 ;; 6 ;; 6 ;; 2 ;; 2
$$

Third row:

$$
1 ;; 5 ;; 3
$$

becomes

$$
1 ;; 1 ;; 5 ;; 5 ;; 3 ;; 3
$$

Intermediate image:

$$
\begin{bmatrix}
1 & 1 & 7 & 7 & 6 & 6 \\
4 & 4 & 6 & 6 & 2 & 2 \\
1 & 1 & 5 & 5 & 3 & 3
\end{bmatrix}
$$

---

## Step 3: Replicate Each Row Vertically

Copy every row once more.

Final zoomed image:

$$
\boxed{
\begin{bmatrix}
1 & 1 & 7 & 7 & 6 & 6 \\
1 & 1 & 7 & 7 & 6 & 6 \\
4 & 4 & 6 & 6 & 2 & 2 \\
4 & 4 & 6 & 6 & 2 & 2 \\
1 & 1 & 5 & 5 & 3 & 3 \\
1 & 1 & 5 & 5 & 3 & 3
\end{bmatrix}
}
$$

---

# Method 2: Zooming by Interpolation (Average Method)

Instead of copying pixels, we **calculate new pixel values** by averaging neighboring pixels.

---

## Step 1: Original Image

$$
\begin{bmatrix}
1 & 7 & 6 \\
4 & 6 & 2 \\
1 & 5 & 3
\end{bmatrix}
$$

---

## Step 2: Insert Empty Columns

$$
\begin{bmatrix}
1 & ? & 7 & ? & 6 \\
4 & ? & 6 & ? & 2 \\
1 & ? & 5 & ? & 3
\end{bmatrix}
$$

---

## Step 3: Compute Horizontal Averages

### Row 1

Between $$1$$ and $$7$$:

$$
\frac{1+7}{2}=4
$$

Between $$7$$ and $$6$$:

$$
\frac{7+6}{2}=6.5
$$

Row becomes

$$
1 ;; 4 ;; 7 ;; 6.5 ;; 6
$$

---

### Row 2

Between $$4$$ and $$6$$:

$$
\frac{4+6}{2}=5
$$

Between $$6$$ and $$2$$:

$$
\frac{6+2}{2}=4
$$

Row becomes

$$
4 ;; 5 ;; 6 ;; 4 ;; 2
$$

---

### Row 3

Between $$1$$ and $$5$$:

$$
\frac{1+5}{2}=3
$$

Between $$5$$ and $$3$$:

$$
\frac{5+3}{2}=4
$$

Row becomes

$$
1 ;; 3 ;; 5 ;; 4 ;; 3
$$

After horizontal interpolation:

$$
\begin{bmatrix}
1 & 4 & 7 & 6.5 & 6 \\
4 & 5 & 6 & 4 & 2 \\
1 & 3 & 5 & 4 & 3
\end{bmatrix}
$$

---

## Step 4: Insert Empty Rows

$$
\begin{bmatrix}
1 & 4 & 7 & 6.5 & 6 \\
? & ? & ? & ? & ? \\
4 & 5 & 6 & 4 & 2 \\
? & ? & ? & ? & ? \\
1 & 3 & 5 & 4 & 3
\end{bmatrix}
$$

---

## Step 5: Compute Vertical Averages

### Between Row 1 and Row 2

Column 1:

$$
\frac{1+4}{2}=2.5
$$

Column 2:

$$
\frac{4+5}{2}=4.5
$$

Column 3:

$$
\frac{7+6}{2}=6.5
$$

Column 4:

$$
\frac{6.5+4}{2}=5.25
$$

Column 5:

$$
\frac{6+2}{2}=4
$$

Inserted row:

$$
2.5 ;; 4.5 ;; 6.5 ;; 5.25 ;; 4
$$

---

### Between Row 2 and Row 3

Column 1:

$$
\frac{4+1}{2}=2.5
$$

Column 2:

$$
\frac{5+3}{2}=4
$$

Column 3:

$$
\frac{6+5}{2}=5.5
$$

Column 4:

$$
\frac{4+4}{2}=4
$$

Column 5:

$$
\frac{2+3}{2}=2.5
$$

Inserted row:

$$
2.5 ;; 4 ;; 5.5 ;; 4 ;; 2.5
$$

---

## Final Interpolated Image

$$
\boxed{
\begin{bmatrix}
1 & 4 & 7 & 6.5 & 6 \\
2.5 & 4.5 & 6.5 & 5.25 & 4 \\
4 & 5 & 6 & 4 & 2 \\
2.5 & 4 & 5.5 & 4 & 2.5 \\
1 & 3 & 5 & 4 & 3
\end{bmatrix}
}
$$

---

# Final Answers

### Replication

$$
\boxed{
\begin{bmatrix}
1 & 1 & 7 & 7 & 6 & 6 \\
1 & 1 & 7 & 7 & 6 & 6 \\
4 & 4 & 6 & 6 & 2 & 2 \\
4 & 4 & 6 & 6 & 2 & 2 \\
1 & 1 & 5 & 5 & 3 & 3 \\
1 & 1 & 5 & 5 & 3 & 3
\end{bmatrix}
}
$$

### Interpolation

$$
\boxed{
\begin{bmatrix}
1 & 4 & 7 & 6.5 & 6 \\
2.5 & 4.5 & 6.5 & 5.25 & 4 \\
4 & 5 & 6 & 4 & 2 \\
2.5 & 4 & 5.5 & 4 & 2.5 \\
1 & 3 & 5 & 4 & 3
\end{bmatrix}
}
$$
