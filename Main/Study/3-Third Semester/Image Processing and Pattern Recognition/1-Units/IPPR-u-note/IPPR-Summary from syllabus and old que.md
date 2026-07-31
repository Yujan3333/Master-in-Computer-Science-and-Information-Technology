#ippr #third-semester 
# IPPR (CSc.623)
Based on Preboard-83, Midterm-83, 2081, 2076, 2075, 2074, 2074-old, 2073

**How to use this:** Sections are ranked by how often they've been asked. Do the 🔴 (near-certain) topics cold — you should be able to write them without looking. Do 🟠 well. Skim 🟡 only if time allows.

---

## 0. The Big Picture (so nothing feels alien)

Digital Image Processing = taking a picture (a grid of pixel numbers), and mathematically manipulating that grid to make it look better (**enhancement**), fix damage (**restoration**), shrink its file size (**compression**), find objects in it (**segmentation**), or identify what those objects are (**pattern recognition**).

An image is just a **matrix of numbers**. A grayscale pixel is a number from 0 (black) to 255 (white) if using 8 bits. Almost every question in this course is really just "do something to this matrix" or "explain a step in the pipeline."

---

## 🔴 TOPIC 1: Fundamental Steps in Digital Image Processing (asked almost every single year)

**Answer skeleton (draw this as boxes in a line, memorize the order):**

```
Image Acquisition → Image Enhancement → Image Restoration → Color Image Processing
→ Wavelets/Compression → Morphological Processing → Segmentation
→ Representation & Description → Object Recognition
```
Plus a **Knowledge Base** box connected to all of them, and **Image Acquisition** feeds from "Problem Domain."

- **Acquisition:** capturing image via sensor (digitize into pixel matrix). Know "image acquisition using a single sensor" and "sensor strips" (line sensors that sweep — used in flatbed scanners; a strip of sensors moves across the scene).
- **Enhancement:** making image visually better (contrast, sharpening) — subjective.
- **Restoration:** removing known degradation (blur, noise) using a mathematical model — objective, opposite of enhancement in *method* though similar in *goal*.
- **Segmentation:** partitioning image into meaningful regions/objects.
- **Representation & Description:** converting segmented region into a form suitable for computer processing (boundary/region features).
- **Recognition:** assigning a label to an object based on its descriptors.

**Likely exact wording:** "Describe the fundamental steps in digital image processing with a block diagram."

---

## 🔴 TOPIC 2: Image Storage / Quantization Calculation (numeric — very likely, easy marks)

**Formula:**
```
Storage (bits) = M × N × k
```
where M×N = image dimensions, k = bits per pixel (bit depth).
Convert to Bytes: divide by 8. To KB: /1024, to MB: /1024².

**Worked example (matches your Preboard-83 Q2 style):**
512×512 image, 8 bits/pixel:
```
512 × 512 × 8 = 2,097,152 bits = 262,144 bytes = 256 KB
```
If quantized to 4 bits instead: half the storage (131,072 bytes = 128 KB), **but** image quality drops — fewer gray levels (16 instead of 256) causes **false contouring** (visible fake edges/banding in smooth gradient areas) because there aren't enough gray shades to represent smooth transitions.

**Also practice the reverse version (2074-old style):** "How many images of size 1200×800 with 256 gray levels can fit in 512 MB?"
```
1 image = 1200 × 800 × 8 bits = 9,600,000 bits = 1,200,000 bytes ≈ 1.144 MB
512 MB ÷ 1.144 MB ≈ 447 images
```

---

## 🔴 TOPIC 3: Huffman Coding + Compression Ratio (asked in nearly every paper — learn this cold)

**Steps:**
1. List symbols (gray levels) with their **probabilities** (freq ÷ total pixels).
2. Repeatedly combine the two **lowest-probability** nodes into a new node (sum their probabilities) until one node (prob = 1) remains — this builds a binary tree.
3. Assign 0/1 to branches going down from each merge; codeword = path from root to symbol.
4. **Average code length** L = Σ(probability × code length) for each symbol.
5. **Entropy** H = −Σ p·log₂(p) (theoretical minimum bits/symbol).
6. **Compression ratio** = (original bits/pixel) ÷ (average Huffman code length).
7. **Coding efficiency** = Entropy ÷ Average length (×100%).

**Do a full example by hand at least twice before your exam** using any of the tables in your old papers (e.g., 2081's Gray Level/pixel-count table, or 2076's data table) — the mechanics are identical every time, only numbers change.

**Also know conceptually:** Lossy vs Lossless compression — Lossless = no data lost, exact reconstruction (Huffman, RLE); used for text/medical images. Lossy = some data discarded for higher compression (JPEG); used for photos/video where minor loss is imperceptible.

---

## 🔴 TOPIC 4: Histogram Equalization & Histogram Matching (asked constantly, both directions)

**Histogram equalization** — spreads out pixel intensities to use the *full* range 0–(L−1), improving contrast in washed-out images.

**Steps for an 8×8 image, gray levels 0–7 (L=8):**
1. Count frequency `n_k` of each gray level k.
2. `p_k = n_k / total pixels` (probability).
3. Cumulative distribution: `CDF_k = p_0 + p_1 + ... + p_k`
4. New gray level: `s_k = round((L−1) × CDF_k)`
5. Replace every old gray level with its new `s_k`, redraw the image/histogram.

**Histogram matching (specification)** — same as above, but instead of matching to a *uniform* histogram, you match to a **reference image's histogram**:
1. Equalize the input image (get s_k as above).
2. Equalize the reference image the same way (get G(z_k)).
3. For each s_k, find the z value where G(z) is closest to s_k → mapping table.
4. Apply mapping to input image.

Practice this exact steps on 2081's or 2075's 8×8 tables by hand — this is a guaranteed 10 marks in most years.

---

## 🔴 TOPIC 5: Fourier Transform / DFT / FFT (very frequent, both theory and small calculation)

- **Why we need it:** converts image from spatial domain (pixel intensities) to frequency domain (rate of intensity change) — lets us design filters based on "how fast things change" rather than pixel-by-pixel.
- **1D DFT formula:** F(u) = Σ f(x)·e^(−j2πux/N), x = 0 to N−1
- **2D DFT formula:** F(u,v) = ΣΣ f(x,y)·e^(−j2π(ux/M + vy/N))
- **FFT** = fast algorithm to compute DFT in O(N log N) instead of O(N²) — divide-and-conquer, splits sequence into even/odd indexed terms recursively.
- **DFT vs FFT:** DFT is the mathematical transform itself (direct computation is slow); FFT is just an efficient *algorithm* to compute the same DFT result faster. Same output, different computation cost.
- Low frequencies = smooth/slowly changing regions (backgrounds); high frequencies = edges, noise, fine detail.
- Be ready to **sketch a simple periodic waveform and compute its Fourier series/transform** (2075-style, e.g. a rectangular pulse f(t)=3 for −2≤t≤2, else 0) — this uses the standard Fourier transform integral of a rectangular pulse, giving a **sinc function**.

---

## 🔴 TOPIC 6: Frequency Domain Filtering (Smoothing & Sharpening) — pick 2-3 filters and know them cold

General filtering process in frequency domain:
```
1. Take DFT of image → F(u,v)
2. Multiply by filter H(u,v) → G(u,v) = H(u,v)·F(u,v)
3. Take Inverse DFT of G(u,v) → filtered image
```

**Smoothing (low-pass) filters** — pass low frequencies, block high (removes noise, blurs edges):
- **Ideal LPF:** H=1 inside radius D₀ from center, 0 outside — causes ringing artifacts.
- **Butterworth LPF:** H(u,v) = 1 / [1 + (D(u,v)/D₀)^(2n)] — smooth transition, n = filter order, no sharp cutoff → no ringing.
- **Gaussian LPF:** H(u,v) = e^(−D²(u,v)/2D₀²) — smoothest of all, no ringing at all.

**Sharpening (high-pass) filters** — opposite of above, pass high frequencies (edges), block low:
- **Butterworth HPF:** H(u,v) = 1 / [1 + (D₀/D(u,v))^(2n)]
- **Gaussian HPF:** H(u,v) = 1 − e^(−D²(u,v)/2D₀²)

**Answer template for "explain how to implement X filter":** (1) compute D(u,v) = distance of each frequency point from the center of the frequency rectangle, (2) plug into the filter's formula to build H(u,v), (3) multiply with F(u,v), (4) inverse transform.

Also know: **Bandpass/Bandreject filters** — pass/block only a *ring* of frequencies (used in restoration, e.g. removing periodic noise).

---

## 🟠 TOPIC 7: Image Restoration & Noise Models

- **Restoration vs Enhancement:** Enhancement is subjective (make it "look better" — no ground truth). Restoration is objective (undo a *known/estimated degradation process* using a mathematical model — has a ground truth target).
- **Degradation model:** g(x,y) = h(x,y)*f(x,y) + η(x,y) — degraded image = (original convolved with degradation function) + noise.
- **Noise models to name with examples:** Gaussian noise (electronic/sensor noise), Salt-and-pepper/impulse noise (dead pixels, transmission errors), Rayleigh, Uniform, Erlang/Gamma noise.
- **Restoration filters:** Mean filters (arithmetic, geometric), **Adaptive mean/median filters** (change behavior based on local statistics — median good for salt-and-pepper, adaptive versions change window size or weighting based on local noise variance), Inverse filtering, Wiener filtering (minimizes mean square error, accounts for noise + blur together — better than plain inverse filtering which amplifies noise).

---

## 🟠 TOPIC 8: Image Segmentation Basics

- **Point/Line/Edge detection:** all done using small spatial masks (kernels) convolved with the image; a point/line/edge is detected where the response exceeds a threshold. Edge detection uses **gradient operators** (Sobel, Prewitt, Roberts) — first derivative masks that highlight intensity change.
- **Hough Transform:** used for detecting lines (or shapes) even with gaps/noise. Converts each edge point (x,y) into a **parameter space** (e.g., slope-intercept or ρ-θ space); points lying on the same line in image space produce curves that **intersect at one point** in parameter space — that intersection identifies the line's parameters.
- **Thresholding:** Global (single threshold for whole image), Local (different threshold per region), Adaptive (threshold varies based on local image statistics like local mean/variance — good for uneven illumination).
- **Region-growing:** start from seed pixels, grow region by adding neighboring pixels with similar properties. Problem: choosing good seed points and stopping criteria; sensitive to noise.

---

## 🟡 TOPIC 9: Representation & Small Concepts (quick wins, short-note questions)

- **Chain code:** represents a boundary as a sequence of directional numbers (0-7 for 8-connectivity, each number = direction to next boundary pixel, usually starting from a defined point, traversed clockwise).
- **Neighborhood/Adjacency/Path:** 4-neighbors (N4) = directly above/below/left/right; 8-neighbors (N8) = N4 + 4 diagonal; **Adjacency** = two pixels are adjacent if they're neighbors AND satisfy a similarity criterion (e.g., same intensity/set V); **Path** = sequence of pixels each adjacent to the next, connecting one pixel to another.
- **Bit-plane slicing:** decompose image into 8 binary planes (one per bit position); higher-order bit planes contain most visually significant info, useful for compression (can drop lower planes) and watermarking.
- **Contrast stretching:** stretches a narrow range of intensities to cover the full range, improving contrast — piecewise linear transformation.
- **Erosion & Dilation (morphology):** Dilation grows/thickens objects (adds pixels at boundaries); Erosion shrinks objects (removes boundary pixels). Both use a "structuring element" that slides over the image.
- **Spatial correlation vs convolution:** Correlation = slide the mask directly over the image and multiply-sum (no flipping). Convolution = flip the mask (rotate 180°) before sliding and multiplying-sum. For symmetric masks, results are identical.
- **High-boost filter:** = A×(original) − (blurred/lowpass version), where A>1; emphasizes/boosts the original image while adding sharpening — a generalization of unsharp masking.

---

## 🟡 TOPIC 10: Pattern Recognition (Unit 5 — usually 1 short question)

- **Pattern vs Pattern class:** A pattern is an arrangement/description of features of an object (e.g., a feature vector). A pattern class is a family/category of patterns sharing common properties (e.g., "all handwritten 7s").
- **Pattern recognition strategies:** statistical (decision-theoretic, uses probability/feature vectors), structural/syntactic (uses relationships between sub-patterns, e.g., grammar rules), neural network-based (learns patterns from training data).
- **Minimum Distance Classifier:** assigns unknown pattern to the class whose mean/prototype vector is *closest* (typically Euclidean distance) to the pattern's feature vector.
- **Confusion Matrix / Sensitivity & Specificity:** Sensitivity = TP/(TP+FN) — how well it catches actual positives. Specificity = TN/(TN+FP) — how well it catches actual negatives. Used to evaluate classifier performance in pattern recognition tasks.

---

## 📋 Exam Strategy for the Next 2 Days

**Day 1:** Master Topics 1–6 (🔴) completely — these appear in almost every paper and carry the most marks. Actually work through a Huffman coding example and a histogram equalization example by hand (don't just read the steps).

**Day 2:** Cover 🟠 topics (restoration, segmentation) with enough depth to write 5-mark answers, then skim 🟡 topics just enough to recognize and write a short paragraph if they show up.

**Section A pattern (10-mark questions, choose 2):** almost always includes: fundamental steps + block diagram, storage/quantization math, OR a full Huffman coding numerical.

**Section B pattern (5-mark questions, attempt all/5):** mix of: one filter (Butterworth/Gaussian), one restoration/noise topic, one segmentation/detection topic, one short-note style topic (chain code, morphology, correlation vs convolution, bit-plane slicing).

Good luck — you've got this; the paper *really does* recycle the same core ~10 topics every year.