#ippr #third-semester 
# Explain in detail the procedure for implementing Butterworth High Pass Filter (BHPF) in the Frequency Domain. (5 Marks)

## Definition

A **Butterworth High Pass Filter (BHPF)** is a frequency-domain filter that **suppresses low-frequency components** and **allows high-frequency components to pass**. Since high frequencies represent edges and fine details, the BHPF is mainly used for **image sharpening** and **edge enhancement**.

Unlike the Ideal High Pass Filter, the Butterworth filter has a **smooth transition** between the stopband and passband, reducing ringing artifacts.

---

# Transfer Function

The Butterworth High Pass Filter is defined as

$$
H(u,v)=\frac{1}{1+\left(\frac{D_0}{D(u,v)}\right)^{2n}}
$$

where

* $H(u,v)$ = Butterworth High Pass Filter
* $D(u,v)$ = Distance from the center of the frequency plane
* $D_0$ = Cutoff frequency
* $n$ = Order of the filter

The distance is

$$
D(u,v)=\sqrt{\left(u-\frac{M}{2}\right)^2+\left(v-\frac{N}{2}\right)^2}
$$

---

# Procedure for Implementation

### Step 1: Read the Input Image

Let the input image be

$$
f(x,y)
$$

of size

$$
M \times N.
$$

---

### Step 2: Zero Padding

Pad the image with zeros to size

$$
2M \times 2N
$$

to reduce wraparound (circular convolution) effects during filtering.

---

### Step 3: Center the Fourier Spectrum

Multiply the image by

$$
(-1)^{x+y}
$$

to shift the origin (DC component) to the center of the frequency spectrum.

$$
f_c(x,y)=f(x,y)(-1)^{x+y}
$$

---

### Step 4: Compute the 2D DFT

Transform the centered image into the frequency domain.

$$
F(u,v)=DFT{f_c(x,y)}
$$

---

### Step 5: Construct the Butterworth High Pass Filter

For every frequency coordinate $(u,v)$, compute

$$
H(u,v)=\frac{1}{1+\left(\frac{D_0}{D(u,v)}\right)^{2n}}
$$

---

### Step 6: Apply the Filter

Multiply the filter with the Fourier transform.

$$
G(u,v)=H(u,v)\times F(u,v)
$$

This suppresses low-frequency components while preserving high-frequency components.

---

### Step 7: Compute the Inverse DFT

Transform the filtered spectrum back into the spatial domain.

$$
g(x,y)=IDFT{G(u,v)}
$$

---

### Step 8: Undo the Centering

Multiply the result by

$$
(-1)^{x+y}
$$

to restore the original spatial arrangement.

---

### Step 9: Crop the Image

Remove the padded region and keep the original

$$
M \times N
$$

image.

The output image is sharpened with enhanced edges.

---

# Algorithm

```text
Input image f(x,y)
        │
        ▼
Zero pad to 2M × 2N
        │
        ▼
Multiply by (-1)^(x+y)
        │
        ▼
Compute 2D DFT
        │
        ▼
Generate Butterworth HPF H(u,v)
        │
        ▼
Multiply G(u,v)=H(u,v)F(u,v)
        │
        ▼
Compute Inverse DFT
        │
        ▼
Multiply by (-1)^(x+y)
        │
        ▼
Crop to M × N
        │
        ▼
Output sharpened image
```

---

# Advantages

* Smooth transition between passband and stopband.
* Produces less ringing than the Ideal High Pass Filter.
* Enhances edges and fine details.
* Cutoff frequency and filter order are adjustable.

---

# Applications

* Image sharpening
* Edge enhancement
* Medical image processing
* Satellite image processing
* Pattern recognition

---

# Exam Answer (5 Marks)

A **Butterworth High Pass Filter (BHPF)** is used to remove low-frequency components and preserve high-frequency components, thereby sharpening an image and enhancing edges. Its transfer function is

$$
H(u,v)=\frac{1}{1+\left(\frac{D_0}{D(u,v)}\right)^{2n}}
$$

**Procedure:**

1. Read the input image.

2. Pad the image with zeros to size $2M \times 2N$.

3. Multiply the image by $(-1)^{x+y}$ to center the Fourier spectrum.

4. Compute the 2D DFT.

5. Construct the Butterworth High Pass Filter.

6. Multiply the filter with the Fourier transform:

   $$
   G(u,v)=H(u,v),F(u,v)
   $$

7. Compute the inverse DFT.

8. Multiply again by $(-1)^{x+y}$ to restore the image.

9. Crop the padded image to its original size.

The resulting image has **enhanced edges and sharper details** because low-frequency components are attenuated while high-frequency components are preserved.

> **Exam Tip:** The implementation procedure is almost identical for all frequency-domain filters (Ideal, Butterworth, Gaussian). The only step that changes is the **transfer function $H(u,v)$** used in Step 5.
