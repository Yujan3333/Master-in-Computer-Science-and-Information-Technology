Perfect — I’ll give you **Lab 4 and Lab 5 separately**, both ready to paste into the **same notebook after Lab 3** ✅
(Structured, commented, and step-by-step like before)

---

# ✅ 📌 **LAB 4: Fourier Transform & Frequency Domain Filtering**

---

## 🔹 **CELL 1: 2D FFT + Magnitude & Phase**

```python id="lab4_cell1"
# ==========================================
# LAB 4 - 1. 2D FFT (Magnitude & Phase)
# ==========================================

# Compute FFT
f = np.fft.fft2(gray)

# Shift zero frequency to center
fshift = np.fft.fftshift(f)

# Magnitude spectrum (log scale for visibility)
magnitude = 20 * np.log(np.abs(fshift) + 1)

# Phase spectrum
phase = np.angle(fshift)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(magnitude, cmap='gray')
plt.title("Magnitude Spectrum")

plt.subplot(1,3,3)
plt.imshow(phase, cmap='gray')
plt.title("Phase Spectrum")

plt.axis('off')
plt.show()
```

---

## 🔹 **CELL 2: Frequency Filters (Ideal + Gaussian)**

```python id="lab4_cell2"
# ==========================================
# LAB 4 - 2. FREQUENCY FILTERS
# ==========================================

rows, cols = gray.shape
crow, ccol = rows//2 , cols//2

# Create distance matrix
x = np.arange(cols)
y = np.arange(rows)
X, Y = np.meshgrid(x, y)
D = np.sqrt((X - ccol)**2 + (Y - crow)**2)

# --- Ideal Low Pass Filter ---
D0 = 50
ideal_lpf = np.zeros((rows, cols))
ideal_lpf[D <= D0] = 1

# --- Gaussian Low Pass ---
gauss_lpf = np.exp(-(D**2) / (2*(D0**2)))

# --- Gaussian High Pass ---
gauss_hpf = 1 - gauss_lpf

# Apply filters
f_ideal = fshift * ideal_lpf
f_gauss = fshift * gauss_lpf
f_high = fshift * gauss_hpf

# Inverse FFT
img_ideal = np.abs(np.fft.ifft2(np.fft.ifftshift(f_ideal)))
img_gauss = np.abs(np.fft.ifft2(np.fft.ifftshift(f_gauss)))
img_high = np.abs(np.fft.ifft2(np.fft.ifftshift(f_high)))

# Display
plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(2,2,2)
plt.imshow(img_ideal, cmap='gray')
plt.title("Ideal LPF")

plt.subplot(2,2,3)
plt.imshow(img_gauss, cmap='gray')
plt.title("Gaussian LPF")

plt.subplot(2,2,4)
plt.imshow(img_high, cmap='gray')
plt.title("Gaussian HPF")

plt.axis('off')
plt.show()
```

---

## 🔹 **CELL 3: Domain Comparison (Frequency vs Spatial)**

```python id="lab4_cell3"
# ==========================================
# LAB 4 - 3. DOMAIN COMPARISON
# ==========================================

# Frequency domain Gaussian (already computed above)
freq_blur = img_gauss

# Spatial domain Gaussian blur
spatial_blur = cv2.GaussianBlur(gray, (5,5), 1)

# PSNR function (reuse from Lab 3)
def compute_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return 100
    return 10 * np.log10((255**2) / mse)

# Compare
psnr_val = compute_psnr(freq_blur.astype(np.uint8), spatial_blur)

print("PSNR between Frequency & Spatial Gaussian:", psnr_val)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(freq_blur, cmap='gray')
plt.title("Frequency Domain Blur")

plt.subplot(1,2,2)
plt.imshow(spatial_blur, cmap='gray')
plt.title("Spatial Domain Blur")

plt.axis('off')
plt.show()
```

---

# 🧠 KEY IDEA (LAB 4)

* FFT → converts image to frequency domain
* LPF → blur
* HPF → edges
* Spatial vs Frequency → should be similar

---
