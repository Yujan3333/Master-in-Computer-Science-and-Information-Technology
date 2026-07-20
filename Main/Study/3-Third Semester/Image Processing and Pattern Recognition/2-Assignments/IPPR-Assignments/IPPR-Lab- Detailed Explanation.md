
# 🧠 1. What You Actually Need to Learn (Big Picture)

Think of the whole course in **3 layers**:

### 🔹 Layer 1: Image Basics (Assignment 1)

You learn:

* How images are stored (arrays)
* How to manipulate pixels
* Basic transformations

👉 This is your **foundation**

---

### 🔹 Layer 2: Image Enhancement (Assignments 2 & 3)

You learn:

* Improve brightness/contrast
* Remove noise
* Enhance edges

👉 This is **“make image better” part**

---

### 🔹 Layer 3: Frequency Domain (Assignments 4 & 5)

You learn:

* Work in frequency instead of pixels
* Advanced filtering & analysis

👉 This is **advanced + scoring area (30%)**

---

# 🛠️ 2. Tools You Need (VERY IMPORTANT)

You’ll mostly use:

* OpenCV (`cv2`)
* NumPy
* Matplotlib
* scikit-image

---

# 💻 3. Coding Mindset (Super Important)

Every task follows this pattern:

```
1. Load image
2. Apply operation
3. Display result
4. Compare (visual + metrics)
```

---

# 📘 4. Assignment-by-Assignment (Simple Explanation + Code Idea)

---

# ✅ Assignment 1: Image Fundamentals

## 🔹 What you need to understand

* Image = matrix (height × width × channels)
* Pixel values range:

  * 0–255 (uint8)
  * 0–1 (float)

---

## 🔹 Example Code Structure

### 📌 Load Image + Stats

```python
import cv2
import numpy as np

img = cv2.imread("image.jpg")

print("Shape:", img.shape)
print("Datatype:", img.dtype)
print("Min:", img.min())
print("Max:", img.max())
print("Mean:", img.mean())
```

---

## 🔹 Downsampling

```python
small = img[::2, ::2]   # factor 2
smaller = img[::4, ::4] # factor 4
```

---

## 🔹 Quantization (reduce gray levels)

```python
levels = 4
quantized = (img // (256//levels)) * (256//levels)
```

---

## 🔹 RGB Channels

```python
b, g, r = cv2.split(img)
```

---

## 🔹 Transformations

```python
# Rotation
M = cv2.getRotationMatrix2D((100,100), 30, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Scaling
scaled = cv2.resize(img, None, fx=0.6, fy=0.6)

# Translation
M = np.float32([[1,0,50],[0,1,30]])
translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
```

---

# ✅ Assignment 2: Histograms & Contrast

## 🔹 What you learn

* Histogram = pixel intensity distribution
* Improve contrast using math

---

## 🔹 Gamma Correction

```python
gamma = 2.0
img_float = img / 255.0
gamma_corrected = np.power(img_float, gamma)
```

---

## 🔹 Histogram Equalization

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)
```

---

## 🔹 CLAHE (Adaptive)

```python
clahe = cv2.createCLAHE(clipLimit=2.0)
result = clahe.apply(gray)
```

---

# ✅ Assignment 3: Filtering (Noise + Sharpening)

## 🔹 What you learn

* Remove noise
* Enhance edges

---

## 🔹 Smoothing Filters

```python
avg = cv2.blur(img, (3,3))
gaussian = cv2.GaussianBlur(img, (5,5), 1)
median = cv2.medianBlur(img, 3)
```

---

## 🔹 Sharpening

```python
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sharp = img - laplacian
```

---

## 🔹 PSNR (IMPORTANT)

$$PSNR=10\log_{10}\left(\frac{255^2}{MSE}\right)$$

```python
def psnr(original, filtered):
    mse = np.mean((original - filtered) ** 2)
    return 10 * np.log10((255**2) / mse)
```

---

# ✅ Assignment 4: Frequency Domain

## 🔹 What you learn

* Convert image → frequency
* Apply filters in frequency

---

## 🔹 FFT

```python
f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)

magnitude = np.log(np.abs(fshift))
```

---

## 🔹 Inverse FFT

```python
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
```

---

## 🔹 Gaussian Low Pass

```python
rows, cols = gray.shape
crow, ccol = rows//2 , cols//2

mask = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        d = np.sqrt((i-crow)**2 + (j-ccol)**2)
        mask[i,j] = np.exp(-(d**2)/(2*(30**2)))
```

---

# ✅ Assignment 5: Advanced Filtering

## 🔹 What you learn

* Frequency response of filters
* Edge enhancement

---

## 🔹 High Frequency Emphasis

$$H_{fe}=a+b\cdot H_{hp}$$

```python
a = 0.5
b = 1.5
Hfe = a + b * high_pass_filter
```

---

# 📊 5. What Your REPORT Should Say (IMPORTANT FOR 30%)

For every experiment, write:

### 🔹 1. What you did

* "Applied Gaussian filter with sigma=2"

### 🔹 2. What you observed

* "Image became smoother but edges blurred"

### 🔹 3. Why it happened

* "High-frequency components were removed"

### 🔹 4. Comparison

* "Median filter works better for salt-and-pepper noise"

---

# 🚀 6. How to Approach (Best Strategy)

### Step-by-step:

1. Do Assignment 1 properly → builds base
2. Reuse code for others
3. Always:

   * Show image
   * Show histogram
   * Print values (PSNR etc.)

---

# 💡 7. Pro Tips (Very Important for Marks)

* Use small images → faster
* Show **before vs after**
* Try multiple parameters:

  * sigma = 1,2,3
  * kernel = 3x3,7x7
* Comment your code clearly

---

# 🎯 Final Understanding

You are basically learning:

| Concept          | Meaning                |
| ---------------- | ---------------------- |
| Spatial domain   | Work on pixels         |
| Frequency domain | Work on patterns       |
| Filtering        | Remove noise / enhance |
| Histogram        | Understand brightness  |
| PSNR             | Measure quality        |

---

