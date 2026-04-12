# ⚙️ First: Install Required Libraries

```bash
pip install opencv-python numpy matplotlib scikit-image
```

---

# ✅ LAB 1: Image Fundamentals

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image (change path if needed)
img = cv2.imread('image.jpg')

# Convert BGR → RGB (OpenCV loads in BGR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# -------------------------------
# 1. IMAGE STATISTICS
# -------------------------------
print("Shape:", img.shape)
print("Datatype:", img.dtype)
print("Min pixel:", img.min())
print("Max pixel:", img.max())
print("Mean pixel:", img.mean())

# -------------------------------
# 2. DOWNSAMPLING
# -------------------------------
down2 = img_rgb[::2, ::2]   # every 2nd pixel
down4 = img_rgb[::4, ::4]   # every 4th pixel

# -------------------------------
# 3. QUANTIZATION
# -------------------------------
def quantize(image, levels):
    step = 256 // levels
    return (image // step) * step

q4 = quantize(img_rgb, 4)
q8 = quantize(img_rgb, 8)
q16 = quantize(img_rgb, 16)

# -------------------------------
# 4. RGB CHANNELS
# -------------------------------
r, g, b = img_rgb[:,:,0], img_rgb[:,:,1], img_rgb[:,:,2]

# Correlation between channels
print("R-G correlation:", np.corrcoef(r.flatten(), g.flatten())[0,1])
print("R-B correlation:", np.corrcoef(r.flatten(), b.flatten())[0,1])

# -------------------------------
# 5. TRANSFORMATIONS
# -------------------------------

# Rotation
h, w = img.shape[:2]
M = cv2.getRotationMatrix2D((w//2, h//2), 30, 1)
rotated = cv2.warpAffine(img_rgb, M, (w, h))

# Scaling
scaled = cv2.resize(img_rgb, None, fx=0.6, fy=0.6)

# Translation
M = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(img_rgb, M, (w, h))

# -------------------------------
# DISPLAY
# -------------------------------
plt.figure(figsize=(10,8))
plt.subplot(2,2,1); plt.imshow(img_rgb); plt.title("Original")
plt.subplot(2,2,2); plt.imshow(down2); plt.title("Downsample x2")
plt.subplot(2,2,3); plt.imshow(q4); plt.title("Quantized (4 levels)")
plt.subplot(2,2,4); plt.imshow(rotated); plt.title("Rotated")
plt.show()
```

---

# ✅ LAB 2: Histogram & Intensity

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------------------------------
# 1. GAMMA CORRECTION
# -------------------------------
gamma = 2.0
img_norm = gray / 255.0
gamma_img = np.power(img_norm, gamma)

# -------------------------------
# 2. HISTOGRAM EQUALIZATION
# -------------------------------
equalized = cv2.equalizeHist(gray)

# CLAHE (Adaptive)
clahe = cv2.createCLAHE(clipLimit=2.0)
clahe_img = clahe.apply(gray)

# -------------------------------
# 3. HISTOGRAM MATCHING
# -------------------------------
from skimage.exposure import match_histograms

ref = cv2.imread('reference.jpg')
ref_gray = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)

matched = match_histograms(gray, ref_gray)

# -------------------------------
# DISPLAY
# -------------------------------
plt.figure(figsize=(10,6))
plt.subplot(2,2,1); plt.imshow(gray, cmap='gray'); plt.title("Original")
plt.subplot(2,2,2); plt.imshow(equalized, cmap='gray'); plt.title("Equalized")
plt.subplot(2,2,3); plt.imshow(clahe_img, cmap='gray'); plt.title("CLAHE")
plt.subplot(2,2,4); plt.imshow(matched, cmap='gray'); plt.title("Matched")
plt.show()
```

---

# ✅ LAB 3: Filtering + PSNR

```python
import cv2
import numpy as np

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------------------------------
# ADD NOISE
# -------------------------------
noise = np.random.normal(0, 25, gray.shape)
noisy = gray + noise
noisy = np.clip(noisy, 0, 255).astype(np.uint8)

# -------------------------------
# FILTERS
# -------------------------------
avg = cv2.blur(noisy, (3,3))
gaussian = cv2.GaussianBlur(noisy, (5,5), 1)
median = cv2.medianBlur(noisy, 3)

# -------------------------------
# PSNR FUNCTION
# -------------------------------
def psnr(original, filtered):
    mse = np.mean((original - filtered) ** 2)
    return 10 * np.log10((255**2) / mse)

print("PSNR Avg:", psnr(gray, avg))
print("PSNR Gaussian:", psnr(gray, gaussian))
print("PSNR Median:", psnr(gray, median))

# -------------------------------
# SHARPENING
# -------------------------------
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
sharp = gray - laplacian
```

---

# ✅ LAB 4: FFT & Frequency Filtering

```python
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

# -------------------------------
# FFT
# -------------------------------
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

magnitude = np.log(np.abs(fshift) + 1)

# -------------------------------
# GAUSSIAN LOW PASS FILTER
# -------------------------------
rows, cols = img.shape
crow, ccol = rows//2, cols//2

mask = np.zeros((rows, cols))
D0 = 30  # cutoff

for i in range(rows):
    for j in range(cols):
        d = np.sqrt((i-crow)**2 + (j-ccol)**2)
        mask[i,j] = np.exp(-(d**2)/(2*(D0**2)))

# Apply filter
filtered = fshift * mask

# Inverse FFT
f_ishift = np.fft.ifftshift(filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# -------------------------------
# DISPLAY
# -------------------------------
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title("Original")
plt.subplot(1,2,2); plt.imshow(img_back, cmap='gray'); plt.title("Filtered")
plt.show()
```

---

# ✅ LAB 5: Advanced Filtering

```python
import numpy as np
import cv2

img = cv2.imread('image.jpg', 0)

# FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

# -------------------------------
# HIGH PASS FILTER
# -------------------------------
mask = np.ones((rows, cols))
D0 = 30

for i in range(rows):
    for j in range(cols):
        d = np.sqrt((i-crow)**2 + (j-ccol)**2)
        mask[i,j] = 1 - np.exp(-(d**2)/(2*(D0**2)))

# -------------------------------
# HIGH FREQUENCY EMPHASIS
# -------------------------------
a = 0.5
b = 1.5
Hfe = a + b * mask

filtered = fshift * Hfe

# Inverse FFT
img_back = np.fft.ifft2(np.fft.ifftshift(filtered))
img_back = np.abs(img_back)
```

---

# 🧠 FINAL SIMPLE UNDERSTANDING

* **Lab 1 → Learn image basics**
* **Lab 2 → Improve contrast**
* **Lab 3 → Remove noise + sharpen**
* **Lab 4 → Work in frequency**
* **Lab 5 → Advanced filtering**

---

# 🚀 What to Do Next

1. Run each lab one by one
2. Replace `'image.jpg'` with your own image
3. Take screenshots for report
4. Write simple observations like:

   * “Gaussian blur removes noise smoothly”
   * “Median filter is best for salt-and-pepper noise”

---
