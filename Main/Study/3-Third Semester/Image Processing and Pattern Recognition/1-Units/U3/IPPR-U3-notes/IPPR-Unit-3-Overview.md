#ippr #third-semester 

# Unit 3: Image Restoration and Compression (Simple Exam Notes)

This unit has **2 major topics**:

1. **Image Restoration**
2. **Image Compression**

---

# Part A: Image Restoration

## 1. Image Restoration

### Definition

Image restoration is the process of recovering the **original image** from a degraded (blurred or noisy) image using mathematical and statistical techniques.

### Purpose

* Remove blur
* Remove noise
* Recover the original image
* Improve image quality

### Applications

* Medical imaging
* Satellite imaging
* CCTV footage
* Old photograph restoration

---

## Image Enhancement vs Image Restoration

| Image Enhancement              | Image Restoration                        |
| ------------------------------ | ---------------------------------------- |
| Improves appearance            | Recovers the original image              |
| Subjective (depends on viewer) | Objective (based on mathematical models) |
| No degradation model required  | Uses degradation/noise models            |
| Example: Increase brightness   | Example: Remove blur and noise           |

**Memory Tip:**
**Enhancement = Make image look better**
**Restoration = Recover the original image**

---

# 2. Image Degradation and Restoration Model

### Image Degradation

Image degradation means the original image becomes distorted due to:

* Blur
* Noise
* Motion
* Poor lighting
* Camera vibration

### Restoration Process

```text
Original Image
       │
       ▼
Degradation (Blur + Noise)
       │
       ▼
Degraded Image
       │
       ▼
Restoration Filter
       │
       ▼
Restored Image
```

### Mathematical Model

$$[
g(x,y)=H[f(x,y)] + n(x,y)
]$$

where:

* (f(x,y)) = Original image
* (H) = Degradation function (blur)
* (n(x,y)) = Noise
* (g(x,y)) = Degraded image

---

# 3. Noise Models

### Definition

Noise is unwanted random information added to an image during image acquisition or transmission.

### Causes

* Poor camera sensor
* Low light
* Electronic interference
* Transmission errors

---

## Types of Noise

### (a) Gaussian Noise

* Most common noise
* Randomly distributed
* Follows a normal (Gaussian) distribution

**Applications**

* Camera sensor noise
* Electronic circuits

---

### (b) Salt-and-Pepper Noise

Also called **Impulse Noise**.

Contains:

* White pixels (Salt)
* Black pixels (Pepper)

**Cause**

* Transmission errors
* Faulty sensors

**Best Filter**

* Median Filter

---

### (c) Uniform Noise

Noise values are equally distributed over a range.

---

### (d) Rayleigh Noise

Common in radar and remote sensing images.

---

### (e) Exponential Noise

Occurs in some electronic systems.

---

### (f) Gamma (Erlang) Noise

Used in laser imaging and radar systems.

---

# 4. Estimation of Noise Parameters

### Definition

Noise estimation is the process of finding the characteristics of noise present in an image.

Common parameters:

* Mean
* Variance
* Standard deviation

### Why Estimate Noise?

* Choose the correct restoration filter.
* Improve restoration accuracy.

---

# 5. Restoration Filters

### Definition

Restoration filters reduce blur and noise to recover the original image.

Common filters:

* Inverse Filter
* Wiener Filter
* Band Reject Filter
* Band Pass Filter

---

# 6. Band Reject Filter (BRF)

### Definition

A Band Reject Filter removes frequencies within a specific frequency band while allowing lower and higher frequencies to pass.

### Purpose

* Remove periodic noise
* Remove interference

**Example**
Removing repetitive stripe patterns in scanned images.

---

# 7. Band Pass Filter (BPF)

### Definition

A Band Pass Filter allows only a selected range of frequencies to pass while blocking the rest.

### Purpose

* Extract specific image features
* Frequency analysis

---

## Difference Between Band Reject and Band Pass Filters

| Band Reject Filter              | Band Pass Filter              |
| ------------------------------- | ----------------------------- |
| Removes selected frequency band | Keeps selected frequency band |
| Removes periodic noise          | Extracts desired frequencies  |
| Blocks middle frequencies       | Passes middle frequencies     |

---

# 8. Inverse Filtering

### Definition

Inverse Filtering removes blur by applying the inverse of the degradation function.

### Formula (Concept)

$$[
F(u,v)=\frac{G(u,v)}{H(u,v)}
]$$

where:

* (F(u,v)) = Restored image
* (G(u,v)) = Degraded image
* (H(u,v)) = Degradation function

### Advantages

* Simple
* Removes blur if degradation is known

### Disadvantages

* Very sensitive to noise
* Performs poorly with noisy images

---

# 9. Wiener Filtering

### Definition

The Wiener Filter restores images by reducing both blur and noise.

It is one of the **most widely used restoration filters**.

### Advantages

* Removes blur
* Reduces noise
* Produces better-quality restored images

### Applications

* Medical images
* Satellite images
* Digital photography

---

## Inverse Filter vs Wiener Filter

| Inverse Filter                      | Wiener Filter                            |
| ----------------------------------- | ---------------------------------------- |
| Removes blur only                   | Removes blur and noise                   |
| Sensitive to noise                  | Handles noise effectively                |
| Requires exact degradation function | Uses statistical information about noise |
| Less accurate in noisy conditions   | More accurate in practice                |

---

# Part B: Image Compression

## 10. Image Compression

### Definition

Image compression reduces the size of an image so it requires less storage space and can be transmitted faster.

### Objectives

* Save storage
* Reduce transmission time
* Reduce bandwidth usage

---

# 11. Image Compression Model

### Compression Process

```text
Original Image
      │
      ▼
Encoder (Compression)
      │
Compressed Data
      │
      ▼
Decoder (Decompression)
      │
      ▼
Reconstructed Image
```

---

# 12. Types of Compression

## (a) Lossless Compression

### Definition

No information is lost during compression.

After decompression:

* Original image is recovered exactly.

### Examples

* PNG
* GIF
* TIFF (lossless)

### Applications

* Medical images
* Legal documents
* Technical drawings

---

## (b) Lossy Compression

### Definition

Some image information is permanently removed to achieve higher compression.

### Examples

* JPEG
* WebP (lossy mode)

### Applications

* Digital photography
* Social media
* Websites

---

## Lossless vs Lossy Compression

| Lossless         | Lossy                    |
| ---------------- | ------------------------ |
| No data loss     | Some data loss           |
| Exact recovery   | Approximate recovery     |
| Larger file size | Smaller file size        |
| Higher quality   | Slight quality reduction |

---

# 13. Compression Standards

Common image compression standards:

### JPEG (Joint Photographic Experts Group)

* Lossy compression
* Most common for photographs

### PNG (Portable Network Graphics)

* Lossless compression
* Supports transparency

### GIF (Graphics Interchange Format)

* Lossless
* Supports simple animations

### TIFF (Tagged Image File Format)

* High-quality image storage
* Used in printing and medical imaging

---

# 14. Coding Techniques

Coding techniques represent image data efficiently.

### (a) Run-Length Encoding (RLE)

Stores repeated values as:

* Value
* Number of repetitions

Example:

```text
AAAAABBBBCC

↓

5A 4B 2C
```

Best for:

* Binary images
* Simple graphics

---

### (b) Huffman Coding

Assigns:

* Short codes to frequently occurring symbols
* Long codes to rare symbols

Advantages:

* Lossless
* Efficient

---

### (c) Arithmetic Coding

Represents the entire message as a single fractional number.

Provides:

* Better compression than Huffman in many cases

---

### (d) LZW (Lempel–Ziv–Welch)

Uses a dictionary of repeated patterns.

Applications:

* GIF
* TIFF

---

# Most Important Differences

## Enhancement vs Restoration

| Enhancement          | Restoration             |
| -------------------- | ----------------------- |
| Improves appearance  | Recovers original image |
| Subjective           | Mathematical/objective  |
| No degradation model | Uses degradation model  |

---

## Inverse Filter vs Wiener Filter

| Inverse         | Wiener                 |
| --------------- | ---------------------- |
| Removes blur    | Removes blur and noise |
| Noise sensitive | Noise resistant        |
| Simple          | More effective         |

---

## Lossless vs Lossy Compression

| Lossless             | Lossy                      |
| -------------------- | -------------------------- |
| No data loss         | Some data loss             |
| Exact reconstruction | Approximate reconstruction |
| Larger file size     | Smaller file size          |

---

## Band Reject vs Band Pass Filter

| Band Reject                     | Band Pass                      |
| ------------------------------- | ------------------------------ |
| Removes selected frequency band | Passes selected frequency band |
| Removes periodic noise          | Extracts desired frequencies   |

---

# Exam Tips (Most Important Questions)

### 2 Marks

* Define image restoration.
* What is image degradation?
* Define Gaussian noise.
* Define Wiener filter.
* Define image compression.
* What is lossless compression?
* What is lossy compression?

### 5 Marks

* Explain the image degradation and restoration model.
* Explain different types of noise models.
* Compare Inverse Filtering and Wiener Filtering.
* Explain image compression models.
* Explain coding techniques (RLE, Huffman, Arithmetic, LZW).

### 10 Marks

* Explain image restoration with a neat block diagram.
* Explain various restoration filters.
* Explain image compression, its types, standards, and coding techniques.
* Compare image enhancement and image restoration.
* Explain different noise models with suitable examples.

### **Memory Tricks**

* **Restoration** = Recover the original image.
* **Gaussian Noise** = Normal/random electronic noise.
* **Salt-and-Pepper Noise** = Black and white dots (best removed by a Median Filter).
* **Inverse Filter** = Removes blur but is sensitive to noise.
* **Wiener Filter** = Removes both blur and noise.
* **Lossless Compression** = No information lost (PNG, GIF, TIFF).
* **Lossy Compression** = Smaller files with some quality loss (JPEG).
