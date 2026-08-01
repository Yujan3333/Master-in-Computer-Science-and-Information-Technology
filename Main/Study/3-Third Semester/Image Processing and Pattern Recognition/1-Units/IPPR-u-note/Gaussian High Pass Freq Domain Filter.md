#ippr #third-semester #exam-paper-answer 

# Question 4

## Describe how you implement the Gaussian High Pass Frequency Domain Filter (GHPF) in the Frequency Domain.

> **Note:** The question says **Gaussian High Pass Filter for image smoothing**, but this is incorrect. A **Gaussian High Pass Filter (GHPF)** is used for **image sharpening and edge enhancement**, **not smoothing**. Image smoothing is done using a **Gaussian Low Pass Filter (GLPF)**.

---

# Gaussian High Pass Filter (GHPF)

A **Gaussian High Pass Filter (GHPF)** is a frequency-domain filter that **passes high-frequency components** while **attenuating low-frequency components**.

Since edges and fine details correspond to high frequencies, the GHPF is mainly used for:

* Image sharpening
* Edge enhancement
* Detail enhancement

---

# Transfer Function

The transfer function of the Gaussian High Pass Filter is

$$
H(u,v)=1-e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

where

* $D(u,v)$ = Distance from the center of the frequency rectangle
* $D_0$ = Cutoff frequency
* $H(u,v)$ = Filter transfer function

The distance is calculated as

$$
D(u,v)=\sqrt{\left(u-\frac{M}{2}\right)^2+\left(v-\frac{N}{2}\right)^2}
$$

where

* $M,N$ = Size of the image

---

# How the Filter Works

At the center of the frequency spectrum,

$$
D(u,v)=0
$$

Therefore,

$$
H(0,0)=1-e^0=0
$$

Hence, the **DC (low-frequency) component is completely removed**.

As the distance from the center increases,

$$
D(u,v)\uparrow
$$

then

$$
H(u,v)\rightarrow1
$$

Thus,

* Low frequencies are rejected.
* High frequencies are allowed to pass.

---

# Frequency Response

```
Gain

1.0 |                     _________
    |                 __/
    |              __/
    |           __/
0.0 |__________/
    +---------------------------->
          Low         High
         Frequency
```

* Center → blocked
* Outer frequencies → passed

---

# Steps for Implementing Gaussian High Pass Filter

The implementation of a Gaussian High Pass Filter in the frequency domain consists of the following steps.

---

## Step 1: Read the Image

Take the input image

$$
f(x,y)
$$

of size

$$
M\times N
$$

---

## Step 2: Zero Padding

Pad the image with zeros to size

$$
2M\times2N
$$

Padding avoids circular convolution and improves filtering accuracy.

---

## Step 3: Center the Fourier Transform

Multiply every pixel by

$$
(-1)^{x+y}
$$

to shift the origin of the Fourier spectrum to the center.

The centered image becomes

$$
f_c(x,y)=f(x,y)(-1)^{x+y}
$$

---

## Step 4: Compute the DFT

Apply the two-dimensional Fourier Transform

$$
F(u,v)=DFT\left\{f_c(x,y)\right\}
$$

Now the image is represented in the frequency domain.

---

## Step 5: Construct the Gaussian High Pass Filter

Calculate the distance from the center

$$
D(u,v)=\sqrt{\left(u-\frac{M}{2}\right)^2+\left(v-\frac{N}{2}\right)^2}
$$

Then compute

$$
H(u,v)=1-e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

where

* $D_0$ controls the cutoff frequency.

---

## Step 6: Apply the Filter

Multiply the image spectrum by the filter

$$
G(u,v)=H(u,v)\times F(u,v)
$$

This suppresses low frequencies while preserving high frequencies.

---

## Step 7: Compute the Inverse DFT

Transform the filtered spectrum back to the spatial domain

$$
g_c(x,y)=IDFT\left\{G(u,v)\right\}
$$

---

## Step 8: Undo the Centering

Multiply by

$$
(-1)^{x+y}
$$

again

$$
g(x,y)=g_c(x,y)(-1)^{x+y}
$$

---

## Step 9: Crop the Image

Remove the padding and retain only the original

$$
M\times N
$$

image.

The resulting image is the sharpened output.

---

# Flowchart

```
Input Image
      │
      ▼
Zero Padding
      │
      ▼
Multiply by (-1)^(x+y)
      │
      ▼
Compute DFT
      │
      ▼
Construct Gaussian HPF
      │
      ▼
Multiply H(u,v) × F(u,v)
      │
      ▼
Compute IDFT
      │
      ▼
Multiply by (-1)^(x+y)
      │
      ▼
Crop Image
      │
      ▼
Output Sharpened Image
```

---

# Effect of Cutoff Frequency $D_0$

### Small $D_0$

* Blocks more low frequencies.
* Strong sharpening.
* May amplify noise.

### Large $D_0$

* Removes fewer low frequencies.
* Mild sharpening.
* Less noise amplification.

---

# Advantages

* Smooth frequency response.
* No ringing artifacts.
* Produces natural-looking sharpening.
* Enhances edges effectively.
* Easy to implement in the frequency domain.

---

# Disadvantages

* Amplifies high-frequency noise.
* More computationally expensive than spatial filters.
* Requires DFT and IDFT computations.

---

# Applications

* Edge enhancement
* Medical image processing
* Satellite image analysis
* Fingerprint enhancement
* Industrial inspection
* Image sharpening before feature extraction

---

# Difference between Gaussian LPF and Gaussian HPF

| Gaussian LPF           | Gaussian HPF            |
| ---------------------- | ----------------------- |
| Used for smoothing     | Used for sharpening     |
| Passes low frequencies | Passes high frequencies |
| Removes noise          | Enhances edges          |
| Blurs the image        | Sharpens the image      |
| Reduces fine details   | Enhances fine details   |

---

# Exam Answer (5 Marks)

A **Gaussian High Pass Filter (GHPF)** is a frequency-domain filter used to enhance edges and sharpen an image by suppressing low-frequency components and preserving high-frequency components.

The transfer function is

$$
H(u,v)=1-e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

where

$$
D(u,v)=\sqrt{\left(u-\frac{M}{2}\right)^2+\left(v-\frac{N}{2}\right)^2}
$$

**Implementation Steps:**

1. Read the input image.
2. Pad the image with zeros.
3. Multiply by $(-1)^{x+y}$ to center the Fourier transform.
4. Compute the 2D DFT.
5. Construct the Gaussian High Pass Filter.
6. Multiply the filter with the image spectrum: $G(u,v)=H(u,v)F(u,v)$.
7. Compute the inverse DFT.
8. Multiply by $(-1)^{x+y}$ to restore the original orientation.
9. Crop the image to its original size.

The output is a **sharpened image** with enhanced edges and fine details.

> **Exam Tip:** The implementation procedure is almost identical for **Butterworth HPF**, **Gaussian HPF**, **Butterworth LPF**, and **Gaussian LPF**. The **only difference is the transfer function**. Memorize the common algorithm once and only change the filter equation.
