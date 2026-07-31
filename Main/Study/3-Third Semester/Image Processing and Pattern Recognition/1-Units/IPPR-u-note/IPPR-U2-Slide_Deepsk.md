#ippr #third-semester 
# Image Processing Lecture 2: Image Enhancement and Filtering in Spatial Domain

## 1. Types of Image Operations

### Point Operations
- Output value at a coordinate depends **only** on input value at same coordinate
- **Complexity**: Constant per pixel (O(1))
- Examples: Brightening, contrast stretching, thresholding, negative images

### Local Operations
- Output depends on input values in a **neighborhood** of that coordinate
- **Complexity**: P² (where P is neighborhood size)
- Examples: Smoothing, sharpening, edge detection

### Global Operations
- Output depends on **all** values in the input image
- **Complexity**: N² (where N is image size)
- Examples: Histogram equalization, Fourier transforms

---

## 2. Point Processing Transformations

### General Form
**s = T(r)**
- s = processed pixel value
- r = original pixel value
- T = grey level transformation function

### Types of Transformations

#### a) Image Negative
```
s = L - 1 - r
```
- Where L = number of intensity levels (e.g., 256 for 8-bit)
- **Use**: Enhances white/grey detail in dark regions

#### b) Thresholding
```
s = { 1, if r > threshold
    { 0,   if r ≤ threshold
```
- Creates binary image
- **Use**: Segmentation, isolating objects from background

#### c) Contrast Stretching
- Expands range of intensity levels to span full device range
- Piecewise linear transformation
- Low-contrast images → improved contrast

#### d) Intensity/Gray Level Slicing
- Highlights specific range of intensities
- Two approaches:
  1. Set range to white, all others to black (binary)
  2. Brighten range, leave others unchanged

---

## 3. Logarithmic Transformations

### Log Transformation
```
s = c * log(1 + r)
```
- Expands dark pixel values, compresses bright values
- **Use**: Images with large dynamic range (e.g., Fourier spectra)

### Power Law (Gamma) Transformation
```
s = c * r^γ
```
- **γ < 1**: Expands dark values, compresses bright (brightens image)
- **γ > 1**: Compresses dark, expands bright (darkens image)
- **Use**: Gamma correction for display devices

### Gamma Correction
- CRT displays have power-law response (γ ≈ 1.8-2.5)
- Pre-process images with s = r^(1/γ) to display correctly
- Important for web images viewed on different monitors

---

## 4. Bit Plane Slicing

### Concept
- Each pixel represented by bits (e.g., 8-bit = 8 planes)
- Plane 0 = LSB (Least Significant Bit)
- Plane 7 = MSB (Most Significant Bit)

### Key Points
- Higher-order bits contain most visual information
- Lower-order bits contain subtle details
- **Uses**:
  1. Convert grayscale to binary image
  2. Reduce image size
  3. Enhance image by focusing on specific bits

---

## 5. Histogram Processing

### Definition
```
h(r_k) = n_k
```
- r_k = kth intensity value
- n_k = number of pixels with intensity r_k

### Normalized Histogram
```
p(r_k) = n_k / MN
```
- MN = total pixels
- Sum of p(r_k) = 1 (probability distribution)

### Histogram Equalization

**Continuous Form:**
```
s = T(r) = (L-1) ∫₀ʳ p_r(w) dw
```

**Discrete Form:**
```
s_k = T(r_k) = ((L-1)/MN) * Σⱼ₌₀ᵏ n_j
```

**Properties:**
- Spreads histogram uniformly
- Increases contrast
- Works best for low-contrast images
- May increase visual graininess

**Example Calculation:**

| r_k | n_k  | p_r(r_k) | T(r_k) | s_k |
| --- | ---- | -------- | ------ | --- |
| r₀  | 790  | 0.19     | 1.33   | 1   |
| r₁  | 1023 | 0.25     | 3.08   | 3   |
| r₂  | 850  | 0.21     | 4.55   | 5   |
| r₃  | 656  | 0.16     | 5.67   | 6   |
| r₄  | 329  | 0.08     | 6.23   | 6   |
| r₅  | 245  | 0.06     | 6.65   | 7   |
| r₆  | 122  | 0.03     | 6.86   | 7   |
| r₇  | 81   | 0.02     | 7.00   | 7   |

### Histogram Specification/Matching
- Transform image to match a specified histogram
- **Process:**
  1. Equalize input image: s = T(r)
  2. Compute G(z) from specified histogram
  3. Map s to z: z = G⁻¹(s)

---

## 6. Spatial Filtering

### General Form
```
g(x,y) = Σ(s=-a to a) Σ(t=-b to b) w(s,t) f(x+s, y+t)
```

### Filter Types

#### a) Linear Filters (Convolution)
- Multiply mask coefficients with pixel values
- Sum products for output

#### b) Nonlinear Filters
- Based on pixel order, not coefficients
- Examples: Median, Max, Min filters

---

## 7. Smoothing (Low-Pass) Filters

### Averaging Filter (Box Filter)
```
R = (1/9) * Σ(all 9 pixels)
```
**Pros:** Removes noise, reduces detail
**Cons:** Blurs edges, loses fine detail

### Weighted Averaging Filter
- Center pixel gets higher weight
- Example 3×3 mask:
```
1/16  2/16  1/16
2/16  4/16  2/16
1/16  2/16  1/16
```

### Median Filter
- Replaces pixel with median of neighborhood
- **Excellent for:** Salt-and-pepper noise
- **Advantage:** Preserves edges better than averaging

---

## 8. Sharpening (High-Pass) Filters

### Properties
- Positive center coefficients
- Negative outer coefficients
- Sum of coefficients = 0 (zero response in constant areas)

### Laplacian Filter

**Continuous:**
```
∇²f = ∂²f/∂x² + ∂²f/∂y²
```

**Discrete (3×3 mask):**
```
0  1  0
1 -4  1
0  1  0
```

**Sharpened Image:**
```
g(x,y) = f(x,y) - ∇²f(x,y)
```

**Alternative mask:**
```
1  1  1
1 -8  1
1  1  1
```

### Combined Laplacian Mask
```
0 -1  0
-1  5 -1
0 -1  0
```
(Does sharpening in one step)

---

## 9. Unsharp Masking & High-Boost Filtering

### Process
1. Create blurred image: f_b(x,y)
2. Generate mask: m(x,y) = f(x,y) - f_b(x,y)
3. Add back: g(x,y) = f(x,y) + k*m(x,y)

### High-Boost Filter
```
g(x,y) = (k+1)f(x,y) - k*f_b(x,y)
```
- **k > 1**: Emphasizes edges more
- **k = 1**: Standard unsharp masking
- **k < 1**: De-emphasizes mask

### Implementation
- Center coefficient: w = 9A - 1 (where A ≥ 1)
- For 3×3 mask: A is amplification factor

---

## 10. Derivative Filters (Edge Detection)

### 1st Derivative (Gradient)
```
∇f = [Gx, Gy]ᵀ = [∂f/∂x, ∂f/∂y]ᵀ
```

**Magnitude:**
```
|∇f| = √(Gx² + Gy²)
```

**Approximations:**
- Simple: |z₅ - z₈| + |z₅ - z₆|
- Cross: |z₅ - z₉| + |z₆ - z₈|

### Roberts Operators
```
[1  0]    [0  1]
[0 -1]    [-1 0]
```

### Prewitt Operators
```
[-1 -1 -1]    [-1 0 1]
[ 0  0  0]    [-1 0 1]
[ 1  1  1]    [-1 0 1]
```

### Sobel Operators (Most Common)
```
[-1 -2 -1]    [-1 0 1]
[ 0  0  0]    [-2 0 2]
[ 1  2  1]    [-1 0 1]
```

### 1st vs 2nd Derivatives
- **1st Order:** Thicker edges, stronger step response
- **2nd Order:** Stronger fine detail response, double response at steps

---

## 11. Magnification/Zooming

### Replication Method
- Simply copy neighboring pixels
- Simple but produces blocky images

### Interpolation Method
- Estimate unknown values from known data
- Smoother results

**Example (2×2 → 4×4):**
```
Original:   1  2
            3  4

Step 1 (Row):   1  1.5  2
                3  3.5  4

Step 2 (Column): 1  1.5  2  1
                 2  2.5  3  1.5
                 3  3.5  4  2
                 1.5 1.75 2  1
```

---

## 12. Edge Effects in Filtering

### Problems at Image Boundaries
- Missing pixels for neighborhood operations

### Solutions
1. **Omit missing pixels**: Only works for some filters
2. **Zero padding**: Add black/white border
3. **Border replication**: Copy edge pixels
4. **Wrap around**: Circular border (can cause artifacts)

---

## 13. Correlation vs Convolution

### Correlation
- Filter applied directly: output = sum(w * f)

### Convolution
- Filter is **rotated 180°** before application
- For symmetric filters: correlation = convolution

---

## Key Formulas to Remember

1. **Negative**: s = L - 1 - r
2. **Log**: s = c * log(1 + r)
3. **Power Law**: s = c * r^γ
4. **Histogram Equalization**: s_k = ((L-1)/MN) * Σⱼ₌₀ᵏ n_j
5. **Laplacian**: ∇²f = ∂²f/∂x² + ∂²f/∂y²
6. **Unsharp Mask**: g = f + k(f - f_b)
7. **Sobel Gradient**: |∇f| = √(Gx² + Gy²)
8. **Averaging Filter**: R = (1/9)Σ pixels

---

## Exam Tips

1. **Always specify the domain** (spatial vs frequency)
2. **Know the difference** between point, local, and global operations
3. **Memorize the mask patterns** for Sobel, Laplacian, averaging filters
4. **Understand histogram equalization** calculations and mapping
5. **Know when to use** median vs averaging vs sharpening filters
6. **Remember gamma correction** for display devices
7. **Be able to calculate** zooming by replication and interpolation
8. **Understand edge effects** and their solutions