#ippr #third-semester 

# IPPR (C.Sc. 623) — Unit 2 (Spatial Domain Part)
## Exam-Oriented Notes: Image Enhancement & Filtering in the Spatial Domain

This covers everything in **Lecture 2 (Chapter 2)** and matches the spatial-domain questions from the old-question bank (2073–2081, Preboard/Midterm-83).

> **Note:** The frequency-domain half of Unit 2 (DFT/FFT, Butterworth, Gaussian, Haar, Hadamard filters) is **not** in this slide deck — it's covered in a separate lecture. Upload that file next and I'll build matching notes for it. Everything below is scoped to spatial-domain enhancement only.

---

## 1. Basic Gray-Level (Point) Transformations

**Definition:** Point processing transforms each pixel using `s = T(r)`, where `r` = input intensity, `s` = output intensity, independent of neighboring pixels.

### 1.1 Image Negative
`s = L − 1 − r` (for L gray levels, e.g., L=256 → s = 255−r)
- Use: enhances white/gray detail embedded in dark regions (e.g., mammograms).

### 1.2 Thresholding
```
s = L−1   if r > threshold
s = 0     if r ≤ threshold
```
- Produces a binary image; used for segmentation.

### 1.3 Log Transformation
`s = c · log(1 + r)`
- Expands dark pixel values, compresses bright ones.
- Used to compress large dynamic range (e.g., displaying Fourier spectra).
- Inverse-log does the opposite (expands bright values).

### 1.4 Power-Law (Gamma) Transformation
`s = c · r^γ`
- γ < 1: expands dark regions (brightens image) — used for **washed-out/overexposed** correction after inversion logic, or to reveal detail in dark images (MR spine example: γ=0.6→0.4→0.3, more detail revealed until image starts washing out).
- γ > 1: darkens image — used for images with **washed-out appearance** (aerial runway example: γ=3.0, 4.0 give good results; γ=5.0 loses shadow detail).
- **Gamma correction**: devices (CRT monitors, printers) respond to input via a power law (γ ≈ 1.8–2.5); we pre-correct images with the inverse power law so they display correctly.

**Exam Answer Template (typical marks: 2+1+3 style — "Explain intensity level slicing, negative and power law"):**
1. Define each with formula.
2. State the effect (brighten/darken/expand/compress).
3. Give one real use-case each.
4. Draw/describe the transformation curve shape.

---

## 2. Piecewise-Linear Transformations

### 2.1 Contrast Stretching
- Problem: low-contrast images (poor illumination/lens aperture/sensor).
- Solution: a piecewise-linear function that expands a narrow input range to the full output range [0, L−1].
- Typically defined by two corner points (r1,s1) and (r2,s2); extreme case (r1,s1)=(rmin,0), (r2,s2)=(rmax,L−1) → full contrast stretch; if r1=r2=mean → thresholding.

### 2.2 Gray-Level (Intensity-Level) Slicing
- Highlights a specific range of intensities.
- Two variants:
  - **Binary**: pixels in range of interest → white (L−1), all others → black (0).
  - **Preserve background**: pixels in range → brightened, others unchanged.
- Use: highlighting a feature (e.g., a mass in an X-ray) without losing background context.

### 2.3 Bit-Plane Slicing
- An 8-bit image = 8 binary bit-planes (plane 0 = LSB … plane 7 = MSB).
- Plane 7 obtained by thresholding: map [0,127]→0, [128,255]→255.
- **Uses:** convert grayscale→binary, reduce data (represent with fewer bits), analyze contribution of each bit to image appearance, image compression.
- Higher planes (MSB side) carry most visually significant information; lower planes carry fine detail/noise.
- Reconstructing with only top 2–3 planes (7,6,5) recovers most visual content.

**Worked Example Style (exactly the old-question format, L=8, i.e. 3-bit gray levels):**

Given pixel matrix:
```
0  7  3  1
3  6  4  6
2  4  2  2
1  2  5  3
```

**(a) Negative:** `s = L−1−r = 7−r`
```
7  0  4  6
4  1  3  1
5  3  5  5
6  5  2  4
```

**(b) Threshold** (assume threshold = 4, i.e., r≥4 → 7, r<4 → 0):
```
0  7  0  0
0  7  7  7
0  7  0  0
0  0  7  0
```

**(c) Clipping** (assume 2 ≤ r ≤ 5 → 7, otherwise → 0):
```
0  0  7  0
7  0  7  0
7  7  7  7
0  7  7  7
```

**(d) Bit-Plane Slicing** (each value → 3-bit binary: 0=000, 7=111, etc.):
```
000 111 011 001
011 110 100 110
010 100 010 010
001 010 101 011
```
Then separate into 3 planes: **Plane 0 (LSB)** = rightmost bit of each, **Plane 1 (center)**, **Plane 2/MSB** = leftmost bit of each.

> **Exam tip:** Practice this with different threshold/clipping ranges and different L (4-bit, 8-bit) — the method is identical, only the boundary numbers change.

---

## 3. Histogram Processing

### 3.1 Histogram — Definition
`h(rₖ) = nₖ` where `rₖ` = kth intensity level, `nₖ` = number of pixels with that intensity.
Normalized: `p(rₖ) = nₖ / (M×N)` (an estimate of probability of occurrence), with `Σ p(rₖ) = 1`.

**Uses:** image enhancement, image statistics, compression, segmentation; cheap to compute; standard tool in real-time systems.

### 3.2 Histogram Equalization

**Goal:** Spread out gray levels to be approximately uniformly distributed → increases contrast, especially for dark/washed-out images.

**Formula:**
$$ s_k = T(r_k) = (L-1)\sum_{j=0}^{k} \frac{n_j}{MN} = (L-1)\sum_{j=0}^{k} p_r(r_j) $$

**Step-by-step procedure (this is what to write in the exam):**
1. Compute histogram `nₖ` for each gray level `rₖ` present in the image.
2. Compute PDF: `p(rₖ) = nₖ / MN`.
3. Compute CDF (running sum): `cdf(rₖ) = Σ p(rⱼ)` for j=0..k.
4. New gray level: `sₖ = round[(L−1) × cdf(rₖ)]`.
5. Map every original pixel of value `rₖ` to new value `sₖ`.
6. (Optional) Re-draw the new histogram — it will be flatter/more spread than the original.

**Fully Worked Numerical Example** (typical exam style — L=8, 8×8 image = 64 pixels):

Suppose the histogram of an 8-level (L=8), 64-pixel image is:

| rₖ | nₖ | p(rₖ)=nₖ/64 |
|----|----|----|
| 0  | 8  | 0.125 |
| 1  | 6  | 0.094 |
| 2  | 10 | 0.156 |
| 3  | 14 | 0.219 |
| 4  | 12 | 0.188 |
| 5  | 8  | 0.125 |
| 6  | 4  | 0.063 |
| 7  | 2  | 0.031 |

**Step — cumulative sum and new level (L−1=7):**

| rₖ | p(rₖ) | CDF | sₖ = round(7×CDF) |
|----|-------|-----|--------------------|
| 0 | 0.125 | 0.125 | 1 |
| 1 | 0.094 | 0.219 | 2 |
| 2 | 0.156 | 0.375 | 3 |
| 3 | 0.219 | 0.594 | 4 |
| 4 | 0.188 | 0.781 | 5 |
| 5 | 0.125 | 0.906 | 6 |
| 6 | 0.063 | 0.969 | 7 |
| 7 | 0.031 | 1.000 | 7 |

**Mapping:** every pixel with old value 0→1, 1→2, 2→3, 3→4, 4→5, 5→6, 6→7, 7→7.
Then rebuild the new histogram by summing `nₖ` for old levels that map to the same new level (here 6 and 7 both map to 7, so new histogram at level 7 = n₆+n₇).

> **Exam tip:** This exact 8-value table format (rₖ, nₖ, p(rₖ), CDF, sₖ) is exactly how 2073, 2075, and Midterm-83 phrased the question. Memorize the table structure — you can fill in whatever histogram numbers are given.

### 3.3 Histogram Matching / Specification

**Goal:** Instead of forcing a uniform histogram (equalization), transform the image so its histogram matches a **given/specified** histogram (equalization is the special case where the target is uniform).

**Procedure:**
1. Equalize the input image's histogram: get `sₖ = T(rₖ)` (same as above).
2. Equalize the **specified/target** histogram similarly: get `G(zq) = Σ p_z(zⱼ)` for the desired histogram.
3. For each `sₖ`, find `zq` such that `G(zq) ≈ sₖ` (find closest match — invert G).
4. Map original pixel `rₖ → sₖ → zq` (final output level).
5. Build a mapping table `rₖ → zq` and apply it to the whole image.

**Worked-example structure (as asked in 2081 — two 8×8 images):**
- Build histogram + equalization table for **image A** (input) → get `sₖ` values.
- Build histogram + equalization table for **image B** (reference) → get `G(zq)` values.
- For each `sₖ` from image A, scan the `G(zq)` table and pick the `zq` whose cumulative value is closest (≥) to `sₖ`.
- Produce final mapping `rₖ (image A) → zq (final gray level)`.
- Apply mapping to every pixel of image A; plot resulting histogram (it should resemble image B's histogram shape).

> This is a longer, higher-mark question (10 marks) — always draw the two histograms and the final mapped histogram if time permits.

---

## 4. Correlation vs. Convolution (Preboard-83 — direct question)

| | Correlation | Convolution |
|---|---|---|
| Kernel handling | Mask applied **as-is** | Mask is **rotated 180°** before applying |
| Formula | `g(x,y) = ΣΣ w(s,t)·f(x+s,y+t)` | `g(x,y) = ΣΣ w(s,t)·f(x−s,y−t)` |
| Symmetric masks | For symmetric kernels (e.g., averaging, Laplacian), result is **identical** to convolution | Same result for symmetric kernels |
| Use | Template/pattern matching | Standard filtering (spatial filtering theory is usually built on convolution) |

**One-line exam answer:** Correlation slides the filter mask directly over the image and sums products; convolution first flips the mask (rotate 180°) then does the same sliding-sum operation. For symmetric masks, the two operations give identical results.

---

## 5. Spatial Filtering — Smoothing (Low-Pass)

**Mechanism:** `R = w1z1 + w2z2 + ... + w9z9` — sum of products of mask coefficients and corresponding pixel values, mask slid over every pixel (with a boundary-handling rule: zero-pad / replicate / wrap-around at image edges).

### 5.1 Simple Averaging (Box) Filter
- All coefficients = 1/9 (for 3×3).
- Removes noise, blurs detail; larger mask = more smoothing but more blur (trade-off).
- Also called **low-pass filter**.

### 5.2 Weighted Averaging Filter (Preboard/2081-style question)
Example mask (weights sum to 16, center pixel weighted highest):
```
1/16  2/16  1/16
2/16  4/16  2/16
1/16  2/16  1/16
```
**Worked numeric example (3×3 averaging filter, general form asked in exams):**

Given neighborhood:
```
104 100 108
99  106  98
95   90  85
```
Simple averaging filter (all weights 1/9):
```
e = (1/9)(104+100+108+99+106+98+95+90+85)
  = (1/9)(885) = 98.33
```
For the weighted filter above, multiply each pixel by its corresponding weight (1/16, 2/16, 4/16, etc.) and sum — same procedure, different coefficients.

### 5.3 Median Filter (nonlinear, order-statistic)
- Replace pixel with **median** value of the neighborhood (sort values, pick the middle one).
- Better than averaging at removing **salt-and-pepper/impulse noise** while preserving edges.
- Max filter → brightest point in neighborhood; Min filter → dimmest point.

**Averaging vs Median — exam comparison:**
- Averaging blurs edges while removing noise (works best for Gaussian-type noise).
- Median preserves edge sharpness better and is superior for spike/impulse noise.

### 5.4 Directional Smoothing
- Uses directional kernels (x-direction, y-direction = transpose) to smooth while protecting edges from blurring in a specific direction.

---

## 6. Spatial Filtering — Sharpening (High-Pass)

### 6.1 First and Second Derivatives (1D concept)
- **1st derivative:** `∂f/∂x = f(x+1) − f(x)` — produces thick edges, responds to gray-level steps.
- **2nd derivative:** `∂²f/∂x² = f(x+1) + f(x−1) − 2f(x)` — stronger response to fine detail/thin lines/isolated points, produces a **double response** at edges.

**Comparison table (frequently asked as "explain first derivative filter"):**

| Property | 1st Derivative | 2nd Derivative |
|---|---|---|
| Edge thickness | Thicker edges | Finer/thinner edges |
| Response to noise/fine detail | Weaker | Stronger |
| Response to ramp/step edges | Nonzero along ramp | Double response (one positive, one negative spike) at step |
| Common filter | Gradient/Sobel | Laplacian |

### 6.2 The Laplacian Filter (very frequently asked — with derivation)

**Derivation:**
$$ \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} $$
where
$$ \frac{\partial^2 f}{\partial x^2} = f(x+1,y) + f(x-1,y) - 2f(x,y) $$
$$ \frac{\partial^2 f}{\partial y^2} = f(x,y+1) + f(x,y-1) - 2f(x,y) $$

Adding:
$$ \nabla^2 f = [f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)] - 4f(x,y) $$

**Mask:**
```
0   1   0
1  -4   1
0   1   0
```

**Enhancement (final sharpened image):**
`g(x,y) = f(x,y) − ∇²f(x,y)` (subtract because the mask's center coefficient is negative in this convention)

**Simplified single-step mask** (combining original + Laplacian sharpening in one filter):
```
0  -1   0
-1   5  -1
0  -1   0
```
(Derivation: `g = f − ∇²f = 5f(x,y) − f(x+1,y) − f(x−1,y) − f(x,y+1) − f(x,y−1)`.)

**Variants of the Laplacian mask (8-connected/diagonal versions):**
```
1   1   1              -1  -1  -1
1  -8   1              -1   9  -1
1   1   1              -1  -1  -1
```

**Isotropic property:** The Laplacian is *isotropic* — rotating the image then filtering gives the same result as filtering then rotating (i.e., it's rotation-invariant, direction-independent response to edges).

**Exam Answer Template ("Explain Laplacian filter with an example" — 2+6+2 style marks):**
1. State purpose: sharpening/edge detection via 2nd derivative (2 marks).
2. Derive ∂²f/∂x² and ∂²f/∂y², combine to get ∇²f, show the mask (6 marks).
3. Give a small worked numeric example: take a 3×3 pixel block, apply the mask, compute output value; show the final enhanced image = original − Laplacian (2 marks).

### 6.3 High-Boost / High-Frequency-Emphasis Filter
```
High-pass = Original − Low-pass
High-boost = A(Original) − Low-pass, where A ≥ 1
           = (A−1)(Original) + High-pass
```
- If A=1 → pure high-pass (edge-only, dark background).
- If A>1 → part of the original is preserved/added back, giving an edge-enhanced image that still looks like the original (not just edges on black).
- Center mask coefficient becomes `w = 9A − 1` for a 3×3 all-negative-outer mask.
- **Use:** emphasize high-frequency detail (edges) *without* losing low-frequency (overall brightness/contrast) content — unlike plain high-pass which zeroes out the average gray level.

### 6.4 Unsharp Masking
1. Blur the image → `f_b(x,y)`.
2. Compute mask: `m(x,y) = f(x,y) − f_b(x,y)` (this is the "unsharp mask" — the high-frequency residual).
3. Final: `g(x,y) = f(x,y) + k·m(x,y)`.
   - k=1 → standard unsharp masking.
   - k>1 → high-boost filtering (extra emphasis on edges).
   - k<1 → de-emphasizes the mask's contribution.

### 6.5 Sobel Operator (edge detection)
```
Gx:                    Gy:
-1  -2  -1             -1   0   1
 0   0   0             -2   0   2
 1   2   1             -1   0   1
```
- Apply both masks, combine: `|∇f| ≈ |Gx| + |Gy|` (simplified magnitude).
- Used for edge detection (e.g., detecting defects on a contact lens image in the textbook example).
- Based on the gradient vector `∇f = [Gx, Gy]ᵀ`, magnitude `|∇f| = √(Gx²+Gy²)`, approximated as `|Gx|+|Gy|` for computational efficiency.

### 6.6 Combining Enhancement Techniques
Real enhancement rarely uses one filter alone. Classic textbook example (bone-scan image):
1. Laplacian filter → highlights fine detail/edges.
2. Sharpened image = Original − Laplacian result.
3. Sobel filter → highlights prominent edges (used as a mask).
4. Smooth the Sobel result with a 5×5 averaging filter (to make it a usable mask, not noisy edges).
5. Multiply smoothed-Sobel mask with the Laplacian-sharpened image → a mask that sharpens *only* around strong edges.
6. Add this masked result to the original image.
7. Apply a power-law (gamma) transform to the final result for overall contrast adjustment.

> Good conceptual answer for "how is enhancement achieved in practice" — shows you understand these aren't standalone tools but a pipeline.

---

## 7. Boundary / Edge Effects in Filtering
When the mask overhangs the image border, options are:
1. **Omit** missing pixels (only works for some filters, adds complexity).
2. **Zero-pad** the image (pad with black/white).
3. **Replicate** border pixels outward.
4. **Wrap-around** (treat the image as periodic) — can cause artifacts.

---

## 8. Quick-Reference: Mapping Old Questions → This Chapter's Topics

| Old Question (paraphrased) | Topic in these notes |
|---|---|
| "What is the difference between low-pass and high-pass filter?" (Midterm-83) | §5 vs §6 intro |
| "What is histogram equalization? Illustrate with example" (Midterm-83) | §3.2 |
| "Difference between spatial correlation and convolution" (Preboard-83) | §4 |
| "Function of high-boost filter" (Preboard-83) | §6.3 |
| "Histogram matching for two 8×8 images" (2081) | §3.3 |
| "Boundary + weighted averaging filter example" (2081) | §7, §5.2 |
| "Contrast stretching, bit-plane slicing" (2076) | §2.1, §2.3 |
| "Equalize histogram of given 8×8 image" (2075) | §3.2 |
| "Short note: Smoothing vs Sharpening" (2075) | §5 vs §6 |
| "Laplacian filter with example; derive hyperbolic filter mask" (2074-new) | §6.2 (Laplacian part — hyperbolic filter is frequency-domain, separate topic) |
| "Bit plane slicing technique" (2074-new) | §2.3 |
| "Intensity level slicing, negative, power law" (2074-old) | §1.1, §1.4, §2.2 |
| "First derivative filter with example; derive elliptical filter mask" (2073) | §6.1 (first-derivative part — elliptical filter is frequency-domain) |
| "Histogram + histogram equalization numerical" (2073) | §3.2 |

---

## 9. High-Yield Practice Checklist (do these by hand, untimed, at least once each)

- [ ] Negative, threshold, clip, bit-plane slice a given 4×4 or 8×8 matrix (any L).
- [ ] Full histogram equalization table (rₖ, nₖ, p(rₖ), CDF, sₖ) for an 8-level image.
- [ ] Histogram matching between two small images (equalize both, map via closest CDF).
- [ ] Apply a 3×3 averaging filter and a weighted-averaging filter to a given neighborhood.
- [ ] Apply the Laplacian mask (0,1,0/1,-4,1/0,1,0) and the combined mask (0,-1,0/-1,5,-1/0,-1,0) to a given neighborhood.
- [ ] Apply Sobel Gx and Gy to a 3×3 block and compute |Gx|+|Gy|.
- [ ] Explain (in words, 3–5 lines each): correlation vs convolution; smoothing vs sharpening; median vs averaging filter; high-pass vs high-boost.