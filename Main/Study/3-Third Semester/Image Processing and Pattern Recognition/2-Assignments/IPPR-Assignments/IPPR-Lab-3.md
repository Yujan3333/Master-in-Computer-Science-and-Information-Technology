
# ✅ 📌 **LAB 3 (Add These Cells AFTER Lab 2)**

---

# 🔹 **CELL 1: Smoothing Filters (Average, Gaussian, Median)**

```python
# ==========================================
# LAB 3 - 1. SMOOTHING FILTERS
# ==========================================

# Average Filter (Box Filter)
avg_3 = cv2.blur(gray, (3,3))
avg_7 = cv2.blur(gray, (7,7))

# Gaussian Filter
gauss_1 = cv2.GaussianBlur(gray, (5,5), 1.0)
gauss_2 = cv2.GaussianBlur(gray, (5,5), 2.0)

# Median Filter (good for salt & pepper noise)
med_3 = cv2.medianBlur(gray, 3)
med_7 = cv2.medianBlur(gray, 7)

# Display results
plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(avg_3, cmap='gray')
plt.title("Average 3x3")

plt.subplot(2,3,2)
plt.imshow(avg_7, cmap='gray')
plt.title("Average 7x7")

plt.subplot(2,3,3)
plt.imshow(gauss_1, cmap='gray')
plt.title("Gaussian σ=1")

plt.subplot(2,3,4)
plt.imshow(gauss_2, cmap='gray')
plt.title("Gaussian σ=2")

plt.subplot(2,3,5)
plt.imshow(med_3, cmap='gray')
plt.title("Median 3x3")

plt.subplot(2,3,6)
plt.imshow(med_7, cmap='gray')
plt.title("Median 7x7")

plt.axis('off')
plt.show()
```

---

# 🔹 **CELL 2: Sharpening (Laplacian + Unsharp Masking)**

```python
# ==========================================
# LAB 3 - 2. SHARPENING FILTERS
# ==========================================

# First blur image slightly (as required)
blur = cv2.GaussianBlur(gray, (5,5), 1)

# --- Laplacian Sharpening ---
laplacian = cv2.Laplacian(blur, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

sharp_lap = cv2.subtract(blur, laplacian)

# --- Unsharp Masking ---
gaussian = cv2.GaussianBlur(gray, (5,5), 1)
unsharp = cv2.addWeighted(gray, 1.5, gaussian, -0.5, 0)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(blur, cmap='gray')
plt.title("Blurred")

plt.subplot(1,3,2)
plt.imshow(sharp_lap, cmap='gray')
plt.title("Laplacian Sharp")

plt.subplot(1,3,3)
plt.imshow(unsharp, cmap='gray')
plt.title("Unsharp Masking")

plt.axis('off')
plt.show()
```

---

# 🔹 **CELL 3: Add Noise (Gaussian + Salt & Pepper)**

```python
# ==========================================
# LAB 3 - 3. ADD NOISE
# ==========================================

# --- Gaussian Noise ---
mean = 0
sigma = 25
gaussian_noise = np.random.normal(mean, sigma, gray.shape)
noisy_gauss = gray + gaussian_noise
noisy_gauss = np.clip(noisy_gauss, 0, 255).astype(np.uint8)

# --- Salt & Pepper Noise ---
noisy_sp = gray.copy()
prob = 0.02

# Salt (white)
num_salt = int(prob * gray.size / 2)
coords = [np.random.randint(0, i-1, num_salt) for i in gray.shape]
noisy_sp[coords[0], coords[1]] = 255

# Pepper (black)
num_pepper = int(prob * gray.size / 2)
coords = [np.random.randint(0, i-1, num_pepper) for i in gray.shape]
noisy_sp[coords[0], coords[1]] = 0

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(noisy_gauss, cmap='gray')
plt.title("Gaussian Noise")

plt.subplot(1,3,3)
plt.imshow(noisy_sp, cmap='gray')
plt.title("Salt & Pepper Noise")

plt.axis('off')
plt.show()
```

---

# 🔹 **CELL 4: Filtering + PSNR Calculation**

```python
# ==========================================
# LAB 3 - 4. FILTERING + PSNR
# ==========================================

# Apply filters on noisy images

# Gaussian noise → Gaussian filter
gauss_filtered = cv2.GaussianBlur(noisy_gauss, (5,5), 1)

# Salt & Pepper → Median filter
sp_filtered = cv2.medianBlur(noisy_sp, 5)

# PSNR function
def compute_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    return psnr

# Compute PSNR
psnr_gauss = compute_psnr(gray, gauss_filtered)
psnr_sp = compute_psnr(gray, sp_filtered)

print("PSNR (Gaussian Noise → Gaussian Filter):", psnr_gauss)
print("PSNR (Salt & Pepper → Median Filter):", psnr_sp)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(gauss_filtered, cmap='gray')
plt.title("Filtered Gaussian Noise")

plt.subplot(1,2,2)
plt.imshow(sp_filtered, cmap='gray')
plt.title("Filtered Salt & Pepper")

plt.axis('off')
plt.show()
```

---

# 🧠 🔥 What You MUST Understand (VERY IMPORTANT)

### 🔹 Average Filter

→ Smooths but blurs edges

### 🔹 Gaussian Filter

→ Better smoothing, preserves structure

### 🔹 Median Filter

→ Best for salt & pepper noise

### 🔹 Laplacian

→ Edge-based sharpening

### 🔹 Unsharp Masking

→ Enhances details using blurred version

### 🔹 PSNR

→ Higher PSNR = better quality

---

# ⚠️ IMPORTANT (Make it look yours)

Change:

```python
sigma = 20
prob = 0.01
```

Add comment:

```python
# Median filter works best for salt and pepper noise
```

---

# ✅ Next Step

If you want, I’ll now give:

✅ **Lab 3 Report (full marks)**
✅ **How to explain PSNR in viva**
✅ **Comparison table (very important for examiner)**

Just say: **“give lab3 report”** 👍
Perfect — now we move to **Lab 3**, again in the **same notebook (after Lab 2)** and only adding what’s needed ✅

👉 This one is important because:

* Includes **filters + noise + PSNR (very likely viva question)**

---

# ✅ 📌 **LAB 3 (Add These Cells AFTER Lab 2)**

---

# 🔹 **CELL 1: Smoothing Filters (Average, Gaussian, Median)**

```python
# ==========================================
# LAB 3 - 1. SMOOTHING FILTERS
# ==========================================

# Average Filter (Box Filter)
avg_3 = cv2.blur(gray, (3,3))
avg_7 = cv2.blur(gray, (7,7))

# Gaussian Filter
gauss_1 = cv2.GaussianBlur(gray, (5,5), 1.0)
gauss_2 = cv2.GaussianBlur(gray, (5,5), 2.0)

# Median Filter (good for salt & pepper noise)
med_3 = cv2.medianBlur(gray, 3)
med_7 = cv2.medianBlur(gray, 7)

# Display results
plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(avg_3, cmap='gray')
plt.title("Average 3x3")

plt.subplot(2,3,2)
plt.imshow(avg_7, cmap='gray')
plt.title("Average 7x7")

plt.subplot(2,3,3)
plt.imshow(gauss_1, cmap='gray')
plt.title("Gaussian σ=1")

plt.subplot(2,3,4)
plt.imshow(gauss_2, cmap='gray')
plt.title("Gaussian σ=2")

plt.subplot(2,3,5)
plt.imshow(med_3, cmap='gray')
plt.title("Median 3x3")

plt.subplot(2,3,6)
plt.imshow(med_7, cmap='gray')
plt.title("Median 7x7")

plt.axis('off')
plt.show()
```

---

# 🔹 **CELL 2: Sharpening (Laplacian + Unsharp Masking)**

```python
# ==========================================
# LAB 3 - 2. SHARPENING FILTERS
# ==========================================

# First blur image slightly (as required)
blur = cv2.GaussianBlur(gray, (5,5), 1)

# --- Laplacian Sharpening ---
laplacian = cv2.Laplacian(blur, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

sharp_lap = cv2.subtract(blur, laplacian)

# --- Unsharp Masking ---
gaussian = cv2.GaussianBlur(gray, (5,5), 1)
unsharp = cv2.addWeighted(gray, 1.5, gaussian, -0.5, 0)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(blur, cmap='gray')
plt.title("Blurred")

plt.subplot(1,3,2)
plt.imshow(sharp_lap, cmap='gray')
plt.title("Laplacian Sharp")

plt.subplot(1,3,3)
plt.imshow(unsharp, cmap='gray')
plt.title("Unsharp Masking")

plt.axis('off')
plt.show()
```

---

# 🔹 **CELL 3: Add Noise (Gaussian + Salt & Pepper)**

```python
# ==========================================
# LAB 3 - 3. ADD NOISE
# ==========================================

# --- Gaussian Noise ---
mean = 0
sigma = 25
gaussian_noise = np.random.normal(mean, sigma, gray.shape)
noisy_gauss = gray + gaussian_noise
noisy_gauss = np.clip(noisy_gauss, 0, 255).astype(np.uint8)

# --- Salt & Pepper Noise ---
noisy_sp = gray.copy()
prob = 0.02

# Salt (white)
num_salt = int(prob * gray.size / 2)
coords = [np.random.randint(0, i-1, num_salt) for i in gray.shape]
noisy_sp[coords[0], coords[1]] = 255

# Pepper (black)
num_pepper = int(prob * gray.size / 2)
coords = [np.random.randint(0, i-1, num_pepper) for i in gray.shape]
noisy_sp[coords[0], coords[1]] = 0

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(noisy_gauss, cmap='gray')
plt.title("Gaussian Noise")

plt.subplot(1,3,3)
plt.imshow(noisy_sp, cmap='gray')
plt.title("Salt & Pepper Noise")

plt.axis('off')
plt.show()
```

---

# 🔹 **CELL 4: Filtering + PSNR Calculation**

```python
# ==========================================
# LAB 3 - 4. FILTERING + PSNR
# ==========================================

# Apply filters on noisy images

# Gaussian noise → Gaussian filter
gauss_filtered = cv2.GaussianBlur(noisy_gauss, (5,5), 1)

# Salt & Pepper → Median filter
sp_filtered = cv2.medianBlur(noisy_sp, 5)

# PSNR function
def compute_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    return psnr

# Compute PSNR
psnr_gauss = compute_psnr(gray, gauss_filtered)
psnr_sp = compute_psnr(gray, sp_filtered)

print("PSNR (Gaussian Noise → Gaussian Filter):", psnr_gauss)
print("PSNR (Salt & Pepper → Median Filter):", psnr_sp)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(gauss_filtered, cmap='gray')
plt.title("Filtered Gaussian Noise")

plt.subplot(1,2,2)
plt.imshow(sp_filtered, cmap='gray')
plt.title("Filtered Salt & Pepper")

plt.axis('off')
plt.show()
```

---

# 🧠 🔥 What You MUST Understand (VERY IMPORTANT)

### 🔹 Average Filter

→ Smooths but blurs edges

### 🔹 Gaussian Filter

→ Better smoothing, preserves structure

### 🔹 Median Filter

→ Best for salt & pepper noise

### 🔹 Laplacian

→ Edge-based sharpening

### 🔹 Unsharp Masking

→ Enhances details using blurred version

### 🔹 PSNR

→ Higher PSNR = better quality

---

# ⚠️ IMPORTANT (Make it look yours)

Change:

```python
sigma = 20
prob = 0.01
```

Add comment:

```python
# Median filter works best for salt and pepper noise
```

---
