
![](../../../../../../Images/Third_Sem_Images/IPPR-Whole%20Lab%20what%20is%20being%20done.pdf)

---

# 🔵 LAB 1 – Basic Image Understanding

📄  (Pages 1–3)

### 💡 What this lab is about:

**Understanding what an image actually is in a computer**

---

### 1. Image Statistics

👉 You print:

* shape → size of image (height, width, color channels)
* min/max → darkest and brightest pixel
* mean → average brightness

📌 How to explain:

> “We first check basic properties of the image like size and brightness to understand the data.”

---

### 2. Downsampling (Reducing Size)

👉 You reduce resolution:

* x2 → smaller image
* x4 → even smaller

📌 Explanation:

> “We reduce image size by skipping pixels. This makes it faster but loses detail.”

---

### 3. Quantization (Reducing Gray Levels)

👉 Convert to grayscale and reduce levels:

* 4 levels → very rough
* 16 levels → better

📌 Explanation:

> “We reduce the number of shades in the image. Fewer levels = less detail.”

---

### 4. RGB Channels + Correlation

👉 Split image into:

* Red
* Green
* Blue

👉 Correlation shows similarity between channels

📌 Explanation:

> “Each image is made of 3 colors. We analyze them separately and check how similar they are.”

---

### 5. Geometric Transformations

👉 You apply:

* Rotation
* Scaling
* Translation (move image)

📌 Explanation:

> “We change the position and size of the image using transformations.”

---

# 🟢 LAB 2 – Improving Image Quality

📄  (Pages 4–6)

---

### 1. Contrast Stretching & Gamma

👉 Improves brightness and contrast

📌 Explanation:

> “We enhance the image so details become clearer.”

---

### 2. Histogram Equalization

👉 Makes brightness distribution better

* Global → whole image
* CLAHE → small regions (better)

📌 Explanation:

> “We redistribute brightness to improve visibility of features.”

---

### 3. Histogram Matching

👉 Match one image to another

📌 Explanation:

> “We make one image look like another by matching brightness patterns.”

---

### 4. Local Enhancement (Color)

👉 Improve only brightness channel (L)

📌 Explanation:

> “We enhance brightness without changing colors.”

---

# 🟡 LAB 3 – Filtering & Noise

📄  (Pages 7–10)

---

### 1. Smoothing (Blurring)

👉 Filters:

* Average
* Gaussian
* Median

📌 Explanation:

> “We remove noise by smoothing the image.”

---

### 2. Sharpening

👉 Methods:

* Laplacian
* Unsharp masking

📌 Explanation:

> “We enhance edges to make image sharper.”

---

### 3. Adding Noise

👉 Types:

* Gaussian noise
* Salt & pepper

📌 Explanation:

> “We artificially damage the image to test filters.”

---

### 4. Filtering + PSNR

👉 Remove noise and measure quality

📌 Explanation:

> “We clean noisy images and measure how close they are to the original.”

---

# 🔴 LAB 4 – Frequency Domain (Advanced Concept)

📄  (Pages 10–12)

---

### 💡 Key Idea:

👉 Image can be represented as frequencies (like sound)

---

### 1. FFT (Frequency Transform)

👉 Converts image to frequency domain

* Magnitude → strength
* Phase → structure

📌 Explanation:

> “We convert image into frequency form to analyze patterns.”

---

### 2. Frequency Filters

👉 Types:

* Low pass → blur
* High pass → edges

📌 Explanation:

> “Low frequencies = smooth areas, high frequencies = edges.”

---

### 3. Domain Comparison

👉 Compare:

* Frequency blur
* Normal blur

📌 Explanation:

> “Same result can be achieved in different ways.”

---

# 🟣 LAB 5 – Advanced Filtering

📄  (Pages 13–15)

---

### 1. Kernel Frequency Response

👉 Analyze filters:

* Box → blur
* Laplacian → edges
* Sobel → edges

📌 Explanation:

> “We study how filters behave in frequency space.”

---

### 2. Band-pass Filter

👉 Keeps mid frequencies

📌 Explanation:

> “We keep only certain details and remove others.”

---

### 3. High Frequency Emphasis

👉 Highlights edges

📌 Explanation:

> “We boost important details like edges and textures.”

---

# 🎯 FINAL SIMPLE SUMMARY (VERY IMPORTANT FOR YOU)

If someone asks: **“What did you do in this report?”**

👉 Say this:

> “This report focuses on digital image processing. We started by understanding images, then improved image quality, removed noise, applied filters, and finally analyzed images in the frequency domain to enhance features like edges and details.”

---
