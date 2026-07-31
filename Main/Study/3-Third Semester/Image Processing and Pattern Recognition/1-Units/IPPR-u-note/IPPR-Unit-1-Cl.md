#ippr #third-semester 

# UNIT 1: Introduction

### Q1. Describe the fundamental steps in digital image processing with a block diagram. [Asked almost every year]
**Solution:**
```

Image Acquisition 
→ Enhancement 
→ Restoration 
→ Color Image Processing 
→ Wavelets/Compression 
→ Morphological Processing 
→ Segmentation 
→ Representation & Description 
→ Object Recognition

```
(all connected to a central "Knowledge Base")
- **Acquisition:** sensor converts scene into digital pixel array.
- **Enhancement:** subjective visual improvement (contrast/sharpness).
- **Restoration:** objective correction of known degradation using a math model.
- **Segmentation:** partition image into objects/regions.
- **Representation/Description:** convert segmented data into features (boundary/region descriptors).
- **Recognition:** label objects based on descriptors, using a knowledge base.

---

### Q2. An image of dimension 1024×768 has 256 gray levels. Calculate the number of bytes required to store the image. [Very common numeric]
**Solution:**
```
Bits required = M × N × k = 1024 × 768 × 8   (since 256 = 2^8, k=8 bits)
             = 6,291,456 bits
Bytes = 6,291,456 / 8 = 786,432 bytes ≈ 768 KB
```

### Q2b. If the same 1024×768 image used only 4 bits/pixel instead of 8, what changes?
**Solution:** Storage halves → 393,216 bytes (384 KB). But gray levels drop from 256 to 16 → smooth regions/gradients start showing **false contouring** (visible fake bands/edges) because there aren't enough intensity steps to represent gradual change.

---

### Q3. Explain sampling and quantization.
**Solution:**
- **Sampling** = digitizing the *spatial coordinates* (how many pixel positions represent the continuous scene). Coarser sampling → lower spatial resolution (blockiness).
- **Quantization** = digitizing the *amplitude/intensity values* into discrete gray levels. Fewer quantization levels → false contouring, loss of subtle tonal detail.
- Both together define an image as a matrix f(x,y) of finite size with finite gray levels.

---

### Q4. Explain basic relationships between pixels (neighbors, adjacency, distance measures). [Asked in 2075/2076 style]
**Solution:**
- **4-neighbors N4(p):** pixels directly above, below, left, right of p.
- **8-neighbors N8(p):** N4(p) + 4 diagonal neighbors.
- **Adjacency:** two pixels are adjacent if they are neighbors **and** satisfy some intensity similarity condition (belong to same set V, e.g. same gray-level range).
- **Path:** a sequence of distinct pixels where each consecutive pair is adjacent — connects one pixel to another.
- **Distance measures** between p(x,y) and q(s,t):
  - Euclidean: De = √[(x−s)² + (y−t)²]
  - City-block (D4): D4 = |x−s| + |y−t|
  - Chessboard (D8): D8 = max(|x−s|, |y−t|)

**Worked example:** p=(2,3), q=(5,7):
```
De = √[(5−2)² + (7−3)²] = √(9+16) = √25 = 5
D4 = |5−2| + |7−3| = 3 + 4 = 7
D8 = max(3,4) = 4
```

---

### Q5. What is image zooming/shrinking? (geometric transforms)
**Solution:** Zooming (enlarging) = increasing spatial resolution by inserting new pixels (via nearest-neighbor, bilinear, or bicubic interpolation) between existing ones. Shrinking = reducing resolution by row/column deletion or averaging, done carefully to avoid aliasing.

---
---
# UNIT 2: Image Enhancement and Filtering

### Q1. Perform histogram equalization on the given image data (L=8 gray levels). [Asked almost every year — master this]

**Example image**, 16 pixels, gray levels 0–7, with counts:

| Gray level (k) | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| $n_k (count)$  | 0   | 1   | 2   | 2   | 3   | 3   | 3   | 2   |

**Solution steps:**
1. $p_k$ = $n_k$ / total(16) : 0, 0.0625, 0.125, 0.125, 0.1875, 0.1875, 0.1875, 0.125
2. Cumulative $CDF_k$: 0, 0.0625, 0.1875, 0.3125, 0.5, 0.6875, 0.875, 1.0
3. $s_k$ = round(7 × $CDF_k$):
```
s0 = round(0)      = 0
s1 = round(0.4375) = 0
s2 = round(1.3125) = 1
s3 = round(2.1875) = 2
s4 = round(3.5)    = 4
s5 = round(4.8125) = 5
s6 = round(6.125)  = 6
s7 = round(7)      = 7
```
**Mapping table:** old {0,1,2,3,4,5,6,7} → new {0,0,1,2,4,5,6,7}
4. Replace every pixel's old gray level with its new `s_k` value; redraw histogram (now more spread across 0–7 → better contrast).

### Q1b. Histogram matching / specification — extra step
Same as above, but instead of matching to uniform distribution: equalize the **reference image** the same way to get its mapping G(z), then for each `s_k` of the input, find the `z` where `G(z)` is closest → build input→reference mapping, apply to input image.

---

### Q2. Sketch a rectangular waveform f(t) = 3 for −2≤t≤2, 0 otherwise, and find its Fourier Transform. [Common Unit 2 question]
**Solution:**
```
F(ω) = ∫[-2 to 2] 3·e^(−jωt) dt
     = 3 · [e^(−jωt)/(−jω)] from −2 to 2
     = 3 · (2 sin(2ω)/ω)
     = 6 sin(2ω)/ω
```
This is a **sinc-shaped** function. At ω=0, F(0) = 12 (equals the area under the pulse = 3×4 = 12, a useful check).

---

### Q3. Explain basic gray-level (intensity) transformations.
**Solution:**
- **Negative:** s = (L−1) − r — reverses intensities (useful for enhancing detail in dark regions).
- **Log transform:** s = c·log(1+r) — expands dark pixel values, compresses bright ones (good for images with large dynamic range, e.g. Fourier spectra).
- **Power-law (Gamma):** s = c·r^γ — γ<1 brightens image (expands dark tones), γ>1 darkens it (expands bright tones); used for gamma correction on displays.

---

### Q4. Explain how to implement a Butterworth/Gaussian High-Pass filter in the frequency domain. [Asked almost every year]
**Solution steps:**
1. Compute `D(u,v)` = distance of each frequency-domain point from the center of the frequency rectangle.
2. Build the filter using its formula:
```
Butterworth HPF: H(u,v) = 1 / [1 + (D0/D(u,v))^(2n)]
Gaussian HPF:    H(u,v) = 1 − e^(−D²(u,v)/2D0²)
```
3. Multiply: G(u,v) = H(u,v) · F(u,v), where F(u,v) is the DFT of the input image.
4. Take inverse DFT of G(u,v) to get the sharpened spatial-domain image.
- D0 = cutoff frequency, n = filter order (Butterworth only — controls sharpness of transition).

(Low-pass versions use the inverted formulas: Butterworth LPF = 1/[1+(D/D0)^2n]; Gaussian LPF = e^(−D²/2D0²).)

---

### Q5. Differentiate between smoothing and sharpening spatial filters.
**Solution:**
- **Smoothing filters** (e.g., averaging/mean mask): blur the image, reduce noise, reduce edge sharpness — implemented by a mask of positive weights that averages neighboring pixels.
- **Sharpening filters** (e.g., Laplacian mask): highlight fine detail/edges — implemented using a **second derivative** mask (e.g., center weight positive/large, surrounding negative), added back to the original to enhance edges without removing the base image.

---

# UNIT 3: Image Restoration and Compression

### Q1. Construct Huffman code for the given gray levels, and calculate compression ratio & relative redundancy. [Asked almost EVERY year — highest priority numeric]

**Given (same style as your 2074 paper):**

| Gray level M | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| N_M (pixels) | 10  | 10  | 40  | 30  | 50  | 20  | 30  | 10  |

Total pixels = 200

**Step 1 — Probabilities:**
p0=0.05, p1=0.05, p2=0.20, p3=0.15, p4=0.25, p5=0.10, p6=0.15, p7=0.05

**Step 2 — Build Huffman tree (always merge two smallest probabilities):**
```
0.05(0)+0.05(1) = 0.10 [A]
0.05(7)+0.10(5) = 0.15 [B]
0.10[A]+0.15(3) = 0.25 [C]
0.15(6)+0.15[B] = 0.30 [D]
0.20(2)+0.25[C] = 0.45 [E]
0.25(4)+0.30[D] = 0.55 [F]
0.45[E]+0.55[F] = 1.00 (root)
```

**Step 3 — Assign codes (0=left, 1=right) tracing back from root:**

| Gray level | Code | Length |
| ---------- | ---- | ------ |
| 0          | 0100 | 4      |
| 1          | 0101 | 4      |
| 2          | 00   | 2      |
| 3          | 011  | 3      |
| 4          | 10   | 2      |
| 5          | 1111 | 4      |
| 6          | 110  | 3      |
| 7          | 1110 | 4      |

**Step 4 — Average code length:**
```
L = Σ(p_i × length_i)
 = 0.05(4)+0.05(4)+0.20(2)+0.15(3)+0.25(2)+0.10(4)+0.15(3)+0.05(4)
 = 0.20+0.20+0.40+0.45+0.50+0.40+0.45+0.20 = 2.80 bits/pixel
```

**Step 5 — Entropy:**
```
H = −Σ p·log2(p) ≈ 2.766 bits/symbol
```
(coding efficiency = H/L = 2.766/2.80 ≈ 98.8%, i.e., Huffman code is nearly optimal)

**Step 6 — Compression ratio (using 3-bit fixed code since 8 gray levels need ⌈log2 8⌉=3 bits):**
```
Compression ratio C = original bits/pixel ÷ Huffman avg length = 3 / 2.80 ≈ 1.07
Relative redundancy R = 1 − 1/C = 1 − (1/1.07) ≈ 0.067 → 6.7%
```

---

### Q2. What is image degradation and restoration? Explain noise models.
**Solution:**
- **Degradation model:** `g(x,y) = h(x,y) * f(x,y) + η(x,y)` — observed (degraded) image = degradation function convolved with original + additive noise.
- **Restoration** = estimating f(x,y) back from g(x,y), given knowledge/estimate of h and noise statistics.
- **Common noise models:**
  - Gaussian noise — sensor/electronic noise, bell-curve distribution.
  - Salt-and-pepper (impulse) noise — random black/white pixels, from transmission errors.
  - Rayleigh noise — often in range imaging.
  - Uniform noise — equal probability across a range.
  - Erlang/Gamma noise — from certain imaging sensors (e.g., laser).

---

### Q3. Explain adaptive mean/median filters in image restoration.
**Solution:** Unlike fixed filters, **adaptive filters change their behavior based on local image statistics** (local mean, variance) inside a moving window:
- **Adaptive mean filter:** adjusts the amount of smoothing based on the ratio of noise variance to local variance — smooths more in flat/noisy regions, less near edges (preserves detail).
- **Adaptive median filter:** increases the filter window size if the median found isn't a good representative (handles impulse/salt-and-pepper noise while preserving edges better than a fixed-size median filter, especially at high noise densities).

---

### Q4. Explain Wiener filtering and how it differs from inverse filtering.
**Solution:**
- **Inverse filtering:** simply divides G(u,v) by H(u,v) in frequency domain to recover F(u,v). Problem: amplifies noise badly, especially where H(u,v) is small.
- **Wiener filtering:** minimizes mean-square error between estimated and original image, incorporating both the degradation function **and** noise power spectrum — much more robust to noise than plain inverse filtering.

---

### Q5. Differentiate Lossy vs Lossless compression.
**Solution:**

|                   | Lossless                   | Lossy                            |
| ----------------- | -------------------------- | -------------------------------- |
| Reconstruction    | Exact, no data loss        | Approximate, some data discarded |
| Compression ratio | Lower                      | Higher                           |
| Examples          | Huffman coding, RLE, LZW   | JPEG, MPEG                       |
| Use case          | Text, medical/legal images | Photos, video, web images        |

---

# UNIT 4: Image Segmentation and Representation

### Q1. Explain point, line, and edge detection.
**Solution:** All done by convolving small masks with the image and thresholding the response:
- **Point detection:** Laplacian-like mask (center=8, all others=−1); flag pixel if |response| > threshold.
- **Line detection:** directional masks (horizontal, vertical, ±45°) that respond strongly to lines in that direction.
- **Edge detection:** gradient (first-derivative) operators — **Sobel**:
```
Gx = [-1 0 1;  -2 0 2;  -1 0 1]
Gy = [-1 -2 -1; 0 0 0;  1 2 1]
Gradient magnitude ≈ |Gx| + |Gy|  (or √(Gx²+Gy²))
```
Large gradient magnitude = likely edge pixel.

---

### Q2. What is Hough Transform? How is it useful in line detection? [Asked almost every year]
**Solution:** The Hough Transform maps edge points from image space into a **parameter space** (e.g., ρ = x·cosθ + y·sinθ). Every edge point votes for all lines that could pass through it (a curve in parameter space). Points that lie on the *same* straight line in the image will produce curves that **all intersect at one point** in parameter space — that intersection's (ρ,θ) gives the line's equation. This lets you detect lines even with noise or small gaps in the edge, since it works by accumulating votes rather than requiring a perfectly continuous edge.

---

### Q3. Explain the region-growing technique for segmentation, and its problems.
**Solution:** Start with one or more **seed pixels**; iteratively add neighboring pixels to the region if they satisfy a similarity criterion (e.g., intensity within a threshold of the region's mean). Continue until no more pixels qualify.
**Problems:** choice of seed points affects the result; choice of similarity/stopping criterion is often ad-hoc; sensitive to noise (can leak into unrelated regions or stop too early).

---

### Q4. Explain Global, Local, and Adaptive thresholding.
**Solution:**
- **Global thresholding:** one single threshold T applied to the whole image — works only if illumination is uniform.
- **Local thresholding:** image divided into sub-regions, each region gets its own threshold based on local statistics — handles uneven illumination better.
- **Adaptive thresholding:** threshold value is computed as a function that varies smoothly across the image (e.g., based on local mean/variance in a sliding window) — most flexible for images with varying lighting/contrast.

---

### Q5. Define chain code. Explain with example.
**Solution:** Chain code represents a boundary as a sequence of direction numbers between consecutive boundary pixels. For **8-directional** chain code, directions 0–7 represent: 0=East, 1=NE, 2=North, 3=NW, 4=West, 5=SW, 6=South, 7=SE (numbered counter-clockwise from East). Starting at a defined pixel, trace the boundary (commonly clockwise) and record the direction to each next boundary pixel — e.g., a boundary going right, right, down, down, left would generate the code `0 0 6 6 4`.

---

# UNIT 5: Pattern Recognition

### Q1. Distinguish between pattern and pattern class. Explain PR strategies.
**Solution:**
- **Pattern:** a description/arrangement of measured features of an object (usually represented as a feature vector).
- **Pattern class:** a category/family of patterns sharing common properties (e.g., "the class of all letter A's").
- **Strategies:**
  - **Statistical (decision-theoretic):** classify using probability distributions/feature vectors and distance/probability measures.
  - **Structural (syntactic):** represent patterns via relationships between sub-patterns (like a grammar) — good for patterns with clear structural rules.
  - **Neural network-based:** learns decision boundaries from training data automatically.

---

### Q2. Explain the Minimum Distance Classifier with an example.
**Solution:** Assigns an unknown pattern to the class whose **mean (prototype) vector is closest** (usually Euclidean distance).

**Example:** Class 1 mean m1=(2,2); Class 2 mean m2=(6,6). Unknown pattern x=(4,3). Classify x.
```
D(x, m1) = √[(4−2)² + (3−2)²] = √(4+1) = √5 ≈ 2.24
D(x, m2) = √[(4−6)² + (3−6)²] = √(4+9) = √13 ≈ 3.61
```
Since D(x,m1) < D(x,m2), **x is classified as Class 1**.

---

### Q3. Explain sensitivity and specificity derived from a confusion matrix; describe use in pattern classification.
**Solution:**
```
Sensitivity (Recall) = TP / (TP + FN)   → how well the classifier catches actual positives
Specificity          = TN / (TN + FP)   → how well the classifier catches actual negatives
```
Used to evaluate a trained classifier's real-world reliability beyond simple accuracy — especially important when classes are imbalanced (e.g., rare disease detection), since a classifier could have high accuracy just by always predicting the majority class.

---

## Final Tip
In the exam: for numeric questions (Huffman, histogram equalization, storage calc), **show every step** — markers give partial credit heavily on method even if final arithmetic is slightly off. For theory questions, always structure your answer as: **definition → 1-2 line explanation → diagram/formula → example**, that structure alone captures most of the marks.