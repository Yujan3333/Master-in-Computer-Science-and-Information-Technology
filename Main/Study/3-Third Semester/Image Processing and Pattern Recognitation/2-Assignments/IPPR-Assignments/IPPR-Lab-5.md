
# ✅ 📌 **LAB 5: Filtering Correspondence & Edge Enhancement**

- [IPPR-Lab-5-problem-sol](IPPR-Lab-5-problem-sol.md)
---

## 🔹 **CELL 1: Kernel Frequency Response**

```python id="lab5_cell1"
# ==========================================
# LAB 5 - 1. KERNEL FREQUENCY RESPONSE
# ==========================================

# Define kernels
box = np.ones((3,3)) / 9

laplacian = np.array([[0, -1, 0],
                      [-1, 4, -1],
                      [0, -1, 0]])

sobel = np.array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]])

kernels = [box, laplacian, sobel]
titles = ["Box", "Laplacian", "Sobel"]

plt.figure(figsize=(12,4))

for i in range(3):
    # Pad kernel to image size
    padded = np.zeros_like(gray)
    k = kernels[i]
    padded[:k.shape[0], :k.shape[1]] = k

    # FFT
    f = np.fft.fft2(padded)
    fshift = np.fft.fftshift(f)
    magnitude = np.log(np.abs(fshift)+1)

    plt.subplot(1,3,i+1)
    plt.imshow(magnitude, cmap='gray')
    plt.title(titles[i])

plt.show()
```

---

## 🔹 **CELL 2: Band-Pass Filter**

```python id="lab5_cell2"
# ==========================================
# LAB 5 - 2. BAND-PASS FILTER
# ==========================================

# Two Gaussian LPFs
D0_low = 30
D0_high = 80

low = np.exp(-(D**2)/(2*(D0_high**2)))
high = np.exp(-(D**2)/(2*(D0_low**2))

# Band-pass = large LPF - small LPF
band_pass = low - high

# Apply
f_band = fshift * band_pass
img_band = np.abs(np.fft.ifft2(np.fft.ifftshift(f_band)))

# Display
plt.imshow(img_band, cmap='gray')
plt.title("Band Pass Result")
plt.axis('off')
plt.show()
```

---

## 🔹 **CELL 3: High-Frequency Emphasis**

```python id="lab5_cell3"
# ==========================================
# LAB 5 - 3. HIGH FREQUENCY EMPHASIS
# ==========================================

# Parameters
k1 = 0.5
k2 = 1.5

# High frequency emphasis filter
hfe = k1 + k2 * (1 - gauss_lpf)

# Apply
f_hfe = fshift * hfe
img_hfe = np.abs(np.fft.ifft2(np.fft.ifftshift(f_hfe)))

# Display
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(img_hfe, cmap='gray')
plt.title("High Frequency Emphasis")

plt.axis('off')
plt.show()
```

---

# 🧠 KEY IDEA (LAB 5)

* Kernel FFT → shows what frequencies it affects
* Band-pass → keeps mid frequencies
* High-frequency emphasis → enhances edges + keeps brightness

---

# 🔥 FINAL ADVICE (VERY IMPORTANT)

Before submission:

* Change cutoff values:

  ```python
  D0 = 40
  ```
* Change parameters:

  ```python
  k1 = 0.7
  ```
* Add 1–2 comments like:

  ```
  # I observed HPF enhances edges clearly
  ```

---
