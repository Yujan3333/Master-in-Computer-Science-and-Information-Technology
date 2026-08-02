#ippr #third-semester #exam-paper-answer 

# Question

A $512 \times 512$ grayscale image is quantized using **8 bits**. Calculate the storage space required. How would this change if the same image is quantized using **4 bits**? Explain the impact on image quality. **[6+4=10]**

---

# Given

* Image size = $512 \times 512$ pixels
* Total number of pixels

$$
512 \times 512 = 262,144 \text{ pixels}
$$

---

# Case 1: 8-bit Quantization

Each pixel is represented using **8 bits**.

### Total storage in bits

$$
\text{Storage}
==============

512 \times 512 \times 8
$$

$$
=262,144 \times 8
$$

$$
=2,097,152 \text{ bits}
$$

### Convert to bytes

$$
\frac{2,097,152}{8}
===================

262,144 \text{ bytes}
$$

### Convert to KB

$$
\frac{262,144}{1024}
====================

256 \text{ KB}
$$

**Storage required = $\boxed{256\ \text{KB}}$**

---

# Case 2: 4-bit Quantization

Each pixel is represented using **4 bits**.

### Total storage in bits

$$
\text{Storage}
==============

512 \times 512 \times 4
$$

$$
=262,144 \times 4
$$

$$
=1,048,576 \text{ bits}
$$

### Convert to bytes

$$
\frac{1,048,576}{8}
===================

131,072 \text{ bytes}
$$

### Convert to KB

$$
\frac{131,072}{1024}
====================

128 \text{ KB}
$$

**Storage required = $\boxed{128\ \text{KB}}$**

---

# Comparison

| Quantization | Gray Levels | Storage    |
| ------------ | ----------- | ---------- |
| 8-bit        | $2^8 = 256$ | **256 KB** |
| 4-bit        | $2^4 = 16$  | **128 KB** |

Thus, reducing the quantization from **8 bits to 4 bits** cuts the storage requirement **by half**.

---

# Impact on Image Quality

### 8-bit Quantization

* Provides **256 gray levels**.
* Produces smooth intensity transitions.
* Preserves fine image details.
* Better visual quality.

### 4-bit Quantization

* Provides only **16 gray levels**.
* Reduces storage requirements.
* Causes loss of intensity information.
* Produces **false contouring (banding)** in smooth regions.
* Image appears less realistic with lower contrast.

---

# Conclusion

Using **4-bit quantization** reduces the storage space from **256 KB** to **128 KB**, saving **50%** of the memory. However, this reduction also decreases the number of gray levels from **256 to 16**, resulting in noticeable degradation of image quality due to loss of intensity resolution and the appearance of banding artifacts.

---

# Exam Tip

For an image of size $M \times N$ with $b$ bits per pixel,

$$
\boxed{\text{Storage (bits)} = M \times N \times b}
$$

and

$$
\boxed{\text{Gray Levels} = 2^b}
$$

Always calculate:

1. Total pixels
2. Storage in **bits**
3. Convert to **bytes**
4. Convert to **KB**
5. Mention the effect of changing the number of bits on **image quality**.
