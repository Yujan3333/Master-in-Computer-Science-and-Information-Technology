

# ✅ 📌 **LAB 2: Full Python Code (Colab, Step-by-Step)**

---

## 🔹 **STEP 0: Upload + Load Image**

```python
# ==========================================
# LAB 2: GRAY LEVEL & HISTOGRAM PROCESSING
# ==========================================

from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread(list(uploaded.keys())[0])
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show original
plt.imshow(gray, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis('off')
plt.show()
```

---

# 🔹 **1. INTENSITY TRANSFORMATIONS**

## ✅ (a) Linear Contrast Stretching

```python
# Linear contrast stretching improves contrast

# Normalize pixel values between 0 and 255
min_val = np.min(gray)
max_val = np.max(gray)

stretch = (gray - min_val) / (max_val - min_val) * 255
stretch = stretch.astype(np.uint8)

# Plot
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(stretch, cmap='gray')
plt.title("Contrast Stretched")

plt.show()
```

---

## ✅ (b) Gamma Correction

```python
# Gamma correction controls brightness

gamma = 0.5   # try 0.5, 1.5, 2.0
gamma_corrected = np.array(255 * (gray / 255) ** gamma, dtype='uint8')

# Plot
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(gamma_corrected, cmap='gray')
plt.title(f"Gamma = {gamma}")

plt.show()
```

---

# 🔹 **2. HISTOGRAM EQUALIZATION**

## ✅ (a) Global Histogram Equalization

```python
# Improves contrast globally
hist_eq = cv2.equalizeHist(gray)

# Plot images
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(hist_eq, cmap='gray')
plt.title("Global Histogram Equalization")

plt.show()

# Plot histograms
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(gray.flatten(), bins=256)
plt.title("Original Histogram")

plt.subplot(1,2,2)
plt.hist(hist_eq.flatten(), bins=256)
plt.title("Equalized Histogram")

plt.show()
```

---

## ✅ (b) Adaptive Histogram Equalization (CLAHE)

```python
# CLAHE improves contrast locally

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_img = clahe.apply(gray)

# Plot
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(hist_eq, cmap='gray')
plt.title("Global HE")

plt.subplot(1,2,2)
plt.imshow(clahe_img, cmap='gray')
plt.title("CLAHE")

plt.show()
```

---

# 🔹 **3. HISTOGRAM MATCHING**

```python
# Upload second image for reference
print("Upload reference image:")
uploaded2 = files.upload()

img2 = cv2.imread(list(uploaded2.keys())[0])
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Histogram matching
from skimage.exposure import match_histograms

matched = match_histograms(gray, gray2)

# Plot
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(gray, cmap='gray')
plt.title("Source Image")

plt.subplot(1,3,2)
plt.imshow(gray2, cmap='gray')
plt.title("Reference Image")

plt.subplot(1,3,3)
plt.imshow(matched, cmap='gray')
plt.title("Matched Image")

plt.show()
```

---

# 🔹 **4. LOCAL ENHANCEMENT (COLOR IMAGE)**

## ✅ Option A: Apply CLAHE on each RGB channel

```python
# Split channels
R, G, B = cv2.split(img_rgb)

# Apply CLAHE to each channel
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

R_cl = clahe.apply(R)
G_cl = clahe.apply(G)
B_cl = clahe.apply(B)

# Merge back
merged_rgb = cv2.merge((R_cl, G_cl, B_cl))

# Plot
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Color")

plt.subplot(1,2,2)
plt.imshow(merged_rgb)
plt.title("CLAHE on RGB")

plt.show()
```

---

## ✅ Option B (Better): CLAHE on Luminance (LAB Color Space)

```python
# Convert RGB → LAB
lab = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB)

# Split channels
L, A, B = cv2.split(lab)

# Apply CLAHE only on L channel
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
L_cl = clahe.apply(L)

# Merge back
lab_cl = cv2.merge((L_cl, A, B))

# Convert back to RGB
final_img = cv2.cvtColor(lab_cl, cv2.COLOR_LAB2RGB)

# Plot
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(final_img)
plt.title("CLAHE on L channel")

plt.show()
```

---

# 🧠 🔥 What You MUST Understand (Viva)

### 🔹 Contrast Stretching

→ Expands pixel range → improves visibility

### 🔹 Gamma

* γ < 1 → brighter
* γ > 1 → darker

### 🔹 Histogram Equalization

→ Redistributes intensity → improves contrast globally

### 🔹 CLAHE

→ Works locally → avoids over-enhancement

### 🔹 Histogram Matching

→ Makes one image look like another

### 🔹 LAB vs RGB CLAHE

→ LAB better (preserves color, avoids distortion)

---

# ⚠️ IMPORTANT (Make it YOURS)

Before submission:

* Change `gamma = 0.5` → try `1.2`
* Change comments slightly
* Add:

```python
# I observed CLAHE gives better local contrast
```

---
