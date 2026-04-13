# ⚙️ First: Install Required Libraries

```bash
pip install opencv-python numpy matplotlib scikit-image
```

---

# ✅ LAB 1: Image Fundamentals

```python
# ==========================================
   # LAB 1: IMAGE FUNDAMENTALS
   # ==========================================
   
   # Step 0: Upload image from local system (Google Colab)
   from google.colab import files
   uploaded = files.upload()
   
   # Import required libraries
   import cv2                  # OpenCV for image processing
   import numpy as np         # Numerical operations
   import matplotlib.pyplot as plt   # For displaying images
   
   # ==========================================
   # LOAD IMAGE
   # ==========================================
   
   # Load the uploaded image (takes first uploaded file)
   img = cv2.imread(list(uploaded.keys())[0])
   
   # OpenCV loads image in BGR format, so convert it to RGB
   img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   
   # Display the original image
   plt.imshow(img_rgb)
   plt.title("Original Image")
   plt.axis('off')   # Hide axis for better visualization
   plt.show()
   
   
   # ==========================================
   # 1. IMAGE STATISTICS
   # ==========================================
   
   # Display basic properties of the image
   print("---- IMAGE STATISTICS ----")
   
   # Shape gives (height, width, channels)
   print("Shape (H, W, C):", img.shape)
   
   # Data type usually uint8 (0–255 pixel values)
   print("Data Type:", img.dtype)
   
   # Minimum pixel value in the image
   print("Minimum Pixel Value:", img.min())
   
   # Maximum pixel value in the image
   print("Maximum Pixel Value:", img.max())
   
   # Mean pixel value (average brightness)
   print("Mean Pixel Value:", img.mean())
   
   # Show image again for reference
   plt.imshow(img_rgb)
   plt.title("Original Image (Reference)")
   plt.axis('off')
   plt.show()
   
   
   # ==========================================
   # 2. SAMPLING (DOWNSAMPLING)
   # ==========================================
   
   # Downsampling reduces image resolution by skipping pixels
   
   # Take every 2nd pixel → reduces size by factor of 2
   img_down2 = img_rgb[::2, ::2]
   
   # Take every 4th pixel → reduces size by factor of 4
   img_down4 = img_rgb[::4, ::4]
   
   # Display original and downsampled images
   plt.figure(figsize=(10,4))
   
   plt.subplot(1,3,1)
   plt.imshow(img_rgb)
   plt.title("Original Image")
   plt.axis('off')
   
   plt.subplot(1,3,2)
   plt.imshow(img_down2)
   plt.title("Downsampled (Factor 2)")
   plt.axis('off')
   
   plt.subplot(1,3,3)
   plt.imshow(img_down4)
   plt.title("Downsampled (Factor 4)")
   plt.axis('off')
   
   plt.show()
   
   
   # ==========================================
   # 3. QUANTIZATION (GRAY LEVEL REDUCTION)
   # ==========================================
   
   # Convert color image to grayscale
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
   # Function to reduce number of gray levels
   def quantize(image, levels):
       """
       image  : input grayscale image
       levels : number of gray levels required (e.g., 4, 8, 16)
       """
       step = 256 // levels   # size of each intensity interval
       return (image // step) * step   # map pixels to nearest level
   
   # Apply quantization with different levels
   q4 = quantize(gray, 4)
   q8 = quantize(gray, 8)
   q16 = quantize(gray, 16)
   
   # Display quantized images
   plt.figure(figsize=(10,4))
   
   plt.subplot(1,4,1)
   plt.imshow(gray, cmap='gray')
   plt.title("Original Gray")
   plt.axis('off')
   
   plt.subplot(1,4,2)
   plt.imshow(q4, cmap='gray')
   plt.title("4 Levels")
   plt.axis('off')
   
   plt.subplot(1,4,3)
   plt.imshow(q8, cmap='gray')
   plt.title("8 Levels")
   plt.axis('off')
   
   plt.subplot(1,4,4)
   plt.imshow(q16, cmap='gray')
   plt.title("16 Levels")
   plt.axis('off')
   
   plt.show()
   
   
   # ==========================================
   # 4. RGB CHANNEL EXTRACTION + CORRELATION
   # ==========================================
   
   # Extract individual color channels
   R = img_rgb[:, :, 0]   # Red channel
   G = img_rgb[:, :, 1]   # Green channel
   B = img_rgb[:, :, 2]   # Blue channel
   
   # Display each channel as grayscale image
   plt.figure(figsize=(10,4))
   
   plt.subplot(1,3,1)
   plt.imshow(R, cmap='gray')
   plt.title("Red Channel")
   plt.axis('off')
   
   plt.subplot(1,3,2)
   plt.imshow(G, cmap='gray')
   plt.title("Green Channel")
   plt.axis('off')
   
   plt.subplot(1,3,3)
   plt.imshow(B, cmap='gray')
   plt.title("Blue Channel")
   plt.axis('off')
   
   plt.show()
   
   # Flatten channels into 1D arrays for correlation computation
   R_flat = R.flatten()
   G_flat = G.flatten()
   B_flat = B.flatten()
   
   # Compute correlation between channels
   print("---- CHANNEL CORRELATION ----")
   print("R-G Correlation:", np.corrcoef(R_flat, G_flat)[0,1])
   print("R-B Correlation:", np.corrcoef(R_flat, B_flat)[0,1])
   print("G-B Correlation:", np.corrcoef(G_flat, B_flat)[0,1])
   
   
   # ==========================================
   # 5. GEOMETRIC TRANSFORMATIONS
   # ==========================================
   
   # Get image dimensions
   h, w = img.shape[:2]
   
   # -------- Rotation --------
   # Rotate image by 30 degrees around center
   center = (w//2, h//2)
   rot_matrix = cv2.getRotationMatrix2D(center, 30, 1)
   rotated = cv2.warpAffine(img_rgb, rot_matrix, (w, h))
   
   # -------- Scaling --------
   # Resize image to 60% of original size
   scaled = cv2.resize(img_rgb, None, fx=0.6, fy=0.6)
   
   # -------- Translation --------
   # Shift image by (50, 30) pixels
   trans_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
   translated = cv2.warpAffine(img_rgb, trans_matrix, (w, h))
   
   # Display transformed images
   plt.figure(figsize=(10,4))
   
   plt.subplot(1,4,1)
   plt.imshow(img_rgb)
   plt.title("Original")
   plt.axis('off')
   
   plt.subplot(1,4,2)
   plt.imshow(rotated)
   plt.title("Rotated 30°")
   plt.axis('off')
   
   plt.subplot(1,4,3)
   plt.imshow(scaled)
   plt.title("Scaled (0.6)")
   plt.axis('off')
   
   plt.subplot(1,4,4)
   plt.imshow(translated)
   plt.title("Translated (50,30)")
   plt.axis('off')
   
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
