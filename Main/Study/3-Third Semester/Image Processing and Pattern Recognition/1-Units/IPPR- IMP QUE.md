#ippr #third-semester #old-que 
# CSc.623 – Image Processing & Pattern Recognition
## Old Questions Sorted Unit-wise (Preboard-83, Midterm-83, 2081, 2076, 2075, 2074, 2074-old, 2073)

---

## UNIT 1: Introduction (Digital Image Fundamentals)

| Year | Question |
|---|---|
| Midterm-83 | Describe the fundamental steps in digital image processing with a block diagram. |
| Preboard-83 | Describe the fundamental steps in digital image processing with a block diagram. Explain the image acquisition process using a single sensor and sensor strips. [5+5=10] |
| Preboard-83 | A 512×512 grayscale image is quantized using 8 bits. Calculate the storage space required. How would this change if quantized using 4 bits? Explain the impact on image quality. [6+4=10] |
| 2081 | Define Digital image. Explain steps involved in digital image processing with diagram. [2+8] |
| 2076 | Considering an image, explain neighborhood, adjacency and path between pixels with examples. [5] |
| 2075 | Describe the relationship between the pixels with one another. [5] |
| 2074 (new) | How many images of size 1200×800 with 256 gray levels can be stored in a 512 MB storage space? [3] |
| 2074-old | What is a digital image? Draw only the block diagram of a typical digital image processing system. An image of dimension 1024×768 has 256 gray levels. Calculate number of bytes required to store the image. [1+2+3] |
| 2074-old | What is zooming? A 3×3 size image has following intensity information — [zooming calculation]. [6] |
| 2073 | Discuss the various steps in the digital image processing. An image of dimension 1024×768 has 256 gray levels. Calculate number of bytes required to store the image on a computer. [6] |

### 🎯 Important topics — Unit 1
1. **Fundamental steps of DIP + block diagram** — appears in nearly *every single paper*. Memorize the diagram and one line for each stage.
2. **Image storage/byte calculation** (rows × cols × bits/8, or "how many images fit in X MB") — appears almost every year, always an easy numerical if practiced.
3. Image acquisition (single sensor, sensor strip, sensor array) — asked at least once, worth knowing briefly.
4. Neighborhood, adjacency, connectivity, and paths between pixels — asked twice.
5. Image geometry transforms — zooming/shrinking (2074-old) — know nearest-neighbor and bilinear interpolation basics.
6. Sampling & Quantization — effect of reducing bits on image quality (Preboard-83).

---

## UNIT 2: Image Enhancement and Filtering (Spatial + Frequency Domain, Fourier)

| Year | Question |
|---|---|
| Midterm-83 | What is the difference between a low-pass filter and high-pass filter in the spatial domain? |
| Midterm-83 | Differentiate between Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT). What is the purpose of using the Fourier transform in image processing? |
| Midterm-83 | What is histogram equalization in image enhancement? Illustrate with example. |
| Preboard-83 | Describe how you implement the Gaussian High Pass Frequency domain filter for image smoothing in the frequency domain. |
| Preboard-83 | What is 2D Discrete Fourier Transform (DFT)? Explain. |
| Preboard-83 | What is the difference between spatial correlation and spatial convolution? |
| Preboard-83 | Describe the function of a high-boost filter. |
| 2081 | Consider two 8×8 images. Perform histogram matching for the image on the left using the reference image on the right, and plot the resulting histogram. [10] |
| 2081 | Explain in detail the procedure for implementing Butterworth High Pass filter in the Frequency domain. [5] |
| 2081 | What is boundary? Explain spatial weighted averaging filter with suitable example. [1+4] |
| 2076 | a) What do you understand by image processing? Draw the block diagram of image processing system and explain. b) Write expression for Discrete Fourier Transform for 1D and 2D signal. c) Explain importance of image enhancement in the Fourier Domain. |
| 2076 | Explain: i) Contrast stretching ii) Bit plane slicing |
| 2075 | Sketch the following periodic waveform in the time domain and calculate its Fourier transformation. f(t) = {3, −2≤t≤2; 0, otherwise} [10] |
| 2075 | Equalize the histogram of the given 8×8 image (gray levels 0–7). [10] |
| 2075 | Write short notes on (any two): a) Hough transform b) Bandpass Filter c) Smoothing vs Sharpening [2.5+2.5] |
| 2074 (new) | Explain the FFT algorithm for the one-dimensional case. [7] |
| 2074 (new) | Explain the Laplacian filter with an example. Derive the filter mask for hyperbolic filter and write the algorithm for its implementation. [2+6+2] |
| 2074 (new) | How do you determine sequency in Hadamard transform from the natural order? Explain with example. |
| 2074 (new) | Explain the Bit plane slicing technique for image enhancement. |
| 2074 (new) | Describe in brief how you implement Gaussian High Pass Frequency domain filter for image smoothing in the frequency domain. |
| 2074-old | Explain the intensity level slicing, the image negative and the power law transformation techniques for the purpose of image enhancement. [2+1+3] |
| 2074-old | What is a Fourier Transform and how can you apply it in digital image processing? Explain the different properties of the Fourier Transform. [1+1+4] |
| 2074-old | Derive the equation for hyperbolic filter and write the algorithm for its implementation. [3+3] |
| 2074-old | Short notes: Butterworth High Pass Frequency domain filter. [3] |
| 2073 | Explain the Haar transform and derive the Haar matrix for N = 4 case. [3+7] |
| 2073 | What do you mean by histogram and histogram equalization in image processing? Given a gray-level histogram of an image, compute the gray levels after histogram equalization. [1+2+7] |
| 2073 | Explain the first derivative filter with an example. Derive the filter mask for elliptical filter and write the algorithm for its implementation. [2+6+2] |
| 2073 | Describe in brief how you implement Butterworth Low Pass Frequency domain filter for image smoothing. |

### 🎯 Important topics — Unit 2 (the biggest, most-tested unit)
1. **Histogram processing** — equalization (numerical, near-guaranteed) and histogram matching/specification (2081's worked 8×8 example is a great template).
2. **Frequency-domain filters** — Butterworth (LPF & HPF), Gaussian (LPF & HPF): derivation/transfer function + step-by-step implementation procedure. Extremely frequent — appears in almost every paper in some form.
3. **DFT/FFT** — definitions, 1D/2D expressions, properties, and the FFT algorithm (1D) derivation.
4. **Spatial filtering** — smoothing vs sharpening, correlation vs convolution, high-boost filter, weighted averaging filter, Laplacian filter, first-derivative filter, hyperbolic/elliptical filter mask derivations.
5. **Basic gray-level transformations** — negative, log, power-law (gamma), contrast/intensity-level slicing, bit-plane slicing.
6. **Transforms** — Haar transform (matrix derivation for N=4) and Hadamard transform (sequency ordering) — less frequent but heavy-mark (10) when they appear.
7. Fourier transform of a simple waveform (2075's rectangular pulse f(t) question) — know how to derive FT of a basic signal by hand.
8. Short-note staples: bandpass filter, smoothing vs sharpening comparison.

---

## UNIT 3: Image Restoration and Compression

| Year | Question |
|---|---|
| Preboard-83 | Given a 6-symbol image segment with probabilities: 0.5, 0.3, 0.16, 0.1, 0.1, 0.06 — compute the Huffman code and average length. Also calculate the compression ratio. [5+5=10] |
| Preboard-83 | What is image compression? Differentiate between Lossy and Lossless Compression with examples. |
| 2081 | What is the model of image degradation or restoration process? Explain several restoration filters. [4+6] |
| 2081 | Construct Huffman code for each gray level given and find the compression ratio and coding efficiency. [5] |
| 2076 | What is noise in the context of image? Classify different types of noise models with examples. Explain four kinds of filtering mechanism to overcome the noise. |
| 2076 | Calculate the entropy and the Huffman code for the given image data in the table. |
| 2076 | What do you understand by image restoration? Explain how it is different from image enhancement. |
| 2075 | Define image degradation and restoration. Explain the noise models with its effecting nature in degrading the image. [4+6] |
| 2075 | Short note: Bandpass Filter (restoration context) [2.5] |
| 2074 (new) | Given the frequency table from a histogram of a 16×16, 8-level image, construct Huffman code for each gray level. Calculate the compression ratio and the relative data redundancy assuming a 3-bit code is used instead of the Huffman code. [7+3] |
| 2074 (new) | Explain how will you use the adaptive mean filters in image restoration? |
| 2074-old | Given a frequency table from a 16×16, 8-level image histogram — Construct Huffman code for each gray level. [6] |
| 2074-old | Explain how will you use the adaptive median filters in image restoration? [6] |
| 2073 | Explain how will you use the band reject filters in image restoration. |

### 🎯 Important topics — Unit 3
1. **Huffman coding numerical** (build code, average length, entropy, compression ratio, coding efficiency, relative data redundancy) — the **single most repeated question type across the entire course**. Appears in 6 of 8 papers. Master this cold.
2. **Noise models** — Gaussian, Rayleigh, Erlang/Gamma, exponential, uniform, salt-and-pepper — classification + how each arises.
3. **Restoration filters** — mean filters (arithmetic, geometric, harmonic), order-statistic filters (median, adaptive median, adaptive mean), band-reject, band-pass, inverse filtering, Wiener filtering.
4. **Image restoration vs enhancement** — conceptual difference, frequently asked as a direct question.
5. Degradation/restoration model (the H(u,v), noise N(u,v) system diagram).
6. Lossy vs lossless compression with examples.

---

## UNIT 4: Image Segmentation and Representation

| Year | Question |
|---|---|
| 2081 | Explain Global, local, and Adaptive thresholding in segmentation. [5] |
| 2081 | What is boundary? Explain spatial weighted averaging filter with suitable example. [1+4] |
| 2081 | What is Hough transform? How is it useful in line detection? Explain with example. [1+4] |
| 2076 | Explain how a point and edges can be detected in an image? |
| 2075 | Define image segmentation. Explain the significance of image subtraction and image averaging. [1+4] |
| 2075 | Define chain code. Find the 8-directional chain code for the given image in clockwise direction. Assume the starting position is the third pixel from the top starting position. [1+4] |
| 2075 | Short note: Hough Transform [2.5] |
| 2074 (new) | Explain how Hough transform is useful in line detection? |
| 2074-old | Explain the region growing technique for image segmentation. What are the problems associated with it? [4+2] |
| 2074-old | Short note: Global Thresholding Technique [3] |
| 2073 | Explain the region growing technique for image segmentation. |
| Preboard-83 | Define erosion and dilation in morphological image processing, and also explain the concept of pattern recognition. |

### 🎯 Important topics — Unit 4
1. **Hough transform for line detection** — appears in almost every year, always with "explain with example" — know the parametrization (ρ, θ) and the accumulator-array procedure.
2. **Thresholding** — global, local (adaptive) thresholding; Otsu's method is worth knowing even if not named directly.
3. **Region growing** — algorithm + problems (seed selection, over/under-growing) — repeated twice with identical phrasing.
4. **Point, line, and edge detection** — masks (point detection mask, line detection masks in 4 directions), gradient/edge operators (Sobel, Prewitt, Roberts).
5. **Chain codes** — 8-directional chain code from a grid image — practice reading a grid and writing the code sequence clockwise.
6. **Boundary/boundary descriptors** — asked briefly, know definition and a simple descriptor or two.
7. Morphological operations — erosion & dilation (asked once but conceptually easy marks).
8. Image subtraction & image averaging significance (technically Unit 2 topic but tested alongside segmentation in 2075).

---

## UNIT 5: Pattern Recognition

| Year | Question |
|---|---|
| Preboard-83 | ...also explain the concept of pattern recognition (paired with erosion/dilation question). |
| 2076 | Explain sensitivity and specificity that is derived from confusion matrix and describe its use for pattern classification. |
| 2075 | Distinguish between pattern and pattern class. Explain the strategy for pattern recognition. [2+3] |
| 2074-old | What are the components of a pattern recognition system? Explain with relevant diagrams. [6] |
| 2073 | What is a Neural Network? Explain Minimum Distance Classifier. |

### 🎯 Important topics — Unit 5
1. **Components of a pattern recognition system** (sensing → segmentation → feature extraction → classification → post-processing) with block diagram.
2. **Pattern vs pattern class**, and general PR strategies (statistical, structural, neural).
3. **Minimum distance classifier** and basics of neural network-based classification.
4. **Confusion matrix** — sensitivity, specificity, accuracy, precision — and their role in evaluating a classifier. This is a fairly "new" style question (2076) so watch for it recurring.
5. Structural pattern recognition methods — worth a brief read even though not directly asked yet, since the syllabus lists it explicitly.

---

## Overall Cross-Unit Frequency Ranking (Most → Least likely to reappear)

1. Huffman coding / compression numericals — Unit 3
2. Fundamental steps of DIP + block diagram — Unit 1
3. Frequency-domain filters (Butterworth/Gaussian LPF & HPF) — Unit 2
4. Histogram equalization / matching numericals — Unit 2
5. Restoration filters + noise models — Unit 3
6. Hough transform (line detection) — Unit 4
7. Region growing + thresholding — Unit 4
8. Image storage/byte calculation — Unit 1
9. DFT/FFT theory — Unit 2
10. Pattern recognition system components / classifiers — Unit 5
11. Spatial filters (Laplacian, first derivative, high-boost, correlation vs convolution) — Unit 2
12. Chain codes, boundary descriptors — Unit 4
13. Haar/Hadamard transform derivations — Unit 2 (low frequency but high marks when asked)
14. Neighborhood/adjacency/pixel relationships — Unit 1