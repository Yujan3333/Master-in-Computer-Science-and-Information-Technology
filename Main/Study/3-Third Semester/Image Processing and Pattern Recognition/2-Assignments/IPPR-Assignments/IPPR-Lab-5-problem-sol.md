```python
# ==========================================
# LAB 5
# ==========================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 0. IMAGE + FFT (IMPORTANT BASE)
# ===============================
# Make sure gray is already defined in previous labs

# FFT of image (DO NOT CHANGE THIS)
f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)

rows, cols = gray.shape
crow, ccol = rows//2, cols//2

# Distance matrix
x, y = np.meshgrid(np.arange(cols), np.arange(rows))
D = np.sqrt((x - ccol)**2 + (y - crow)**2)


# ===============================
# 1. KERNEL FREQUENCY RESPONSE
# ===============================

def kernel_fft(kernel, shape):
    padded = np.zeros(shape)
    kh, kw = kernel.shape
    padded[:kh, :kw] = kernel

    f = np.fft.fft2(padded)
    fshift_kernel = np.fft.fftshift(f)

    # Better visualization
    magnitude = np.log(np.abs(fshift_kernel) + 1)
    magnitude = magnitude / np.max(magnitude)

    return magnitude

# Kernels
box = np.ones((3,3)) / 9

laplacian = np.array([[0,-1,0],
                      [-1,4,-1],
                      [0,-1,0]])

sobel = np.array([[-1,0,1],
                  [-2,0,2],
                  [-1,0,1]])

# Compute FFT
box_f = kernel_fft(box, gray.shape)
lap_f = kernel_fft(laplacian, gray.shape)
sobel_f = kernel_fft(sobel, gray.shape)

# Display
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(box_f, cmap='gray')
plt.title("Box Filter Frequency")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(lap_f, cmap='gray')
plt.title("Laplacian Frequency")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(sobel_f, cmap='gray')
plt.title("Sobel Frequency")
plt.axis('off')

plt.show()


# ===============================
# 2. BAND-PASS FILTER
# ===============================

# Gaussian LPFs
low_small = np.exp(-(D**2)/(2*(10**2)))
low_large = np.exp(-(D**2)/(2*(50**2)))

# Band-pass
band_pass = low_large - low_small

# Apply filter (IMPORTANT: use image fshift)
f_band = fshift * band_pass

# Inverse FFT
band_img = np.abs(np.fft.ifft2(np.fft.ifftshift(f_band)))

# Normalize (FIX BLACK IMAGE)
band_img = cv2.normalize(band_img, None, 0, 255, cv2.NORM_MINMAX)

# Display
plt.imshow(band_img, cmap='gray')
plt.title("Band-Pass Filter Result")
plt.axis('off')
plt.show()


# ===============================
# 3. HIGH FREQUENCY EMPHASIS
# ===============================

# Gaussian LPF
gauss_lpf = np.exp(-(D**2)/(2*(30**2)))

# Parameters
k1 = 0.5
k2 = 1.5

# High Frequency Emphasis
hfe = k1 + k2 * (1 - gauss_lpf)

# Apply
f_hfe = fshift * hfe
img_hfe = np.abs(np.fft.ifft2(np.fft.ifftshift(f_hfe)))

# Normalize (FIX BLACK IMAGE)
img_hfe = cv2.normalize(img_hfe, None, 0, 255, cv2.NORM_MINMAX)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img_hfe, cmap='gray')
plt.title("High Frequency Emphasis")
plt.axis('off')

plt.show()
```