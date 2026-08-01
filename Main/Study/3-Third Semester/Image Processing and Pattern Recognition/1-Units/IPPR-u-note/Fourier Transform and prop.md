#ippr #third-semester 

# What is a Fourier Transform and how can you apply it in Digital Image Processing? Explain the different properties of the Fourier Transform. **[1+1+4 Marks]**

---

# (a) What is Fourier Transform? (1 Mark)

## Definition

The **Fourier Transform (FT)** is a mathematical technique that converts an image or signal from the **spatial (time) domain** into the **frequency domain**.

It decomposes an image into its **frequency components**, showing how much of each frequency is present.

* **Low frequencies** represent smooth regions.
* **High frequencies** represent edges and fine details.

---

# (b) Application of Fourier Transform in Digital Image Processing (1 Mark)

The Fourier Transform is applied in image processing by first converting the image into the **frequency domain**, performing the required processing, and then converting it back to the **spatial domain** using the **Inverse Fourier Transform (IFT/IDFT)**.

### Steps

```text
Input Image
      │
      ▼
Fourier Transform (FT/DFT)
      │
      ▼
Frequency Domain
      │
Apply Filter
(LPF / HPF)
      │
      ▼
Inverse Fourier Transform
      │
      ▼
Enhanced Image
```

### Applications

* Noise removal
* Image smoothing
* Image sharpening
* Image restoration
* Image compression

---

# (c) Properties of Fourier Transform (4 Marks)

## 1. Linearity

The Fourier Transform of a linear combination of signals equals the same linear combination of their Fourier Transforms.

If

$$
g(x,y)=af(x,y)+bh(x,y)
$$

then

$$
G(u,v)=aF(u,v)+bH(u,v)
$$

where $a$ and $b$ are constants.

---

## 2. Translation (Shifting) Property

Shifting an image in the spatial domain changes only the **phase** of its Fourier Transform; the **magnitude** remains unchanged.

This property is useful in image registration and alignment.

---

## 3. Convolution Property

Convolution in the spatial domain becomes multiplication in the frequency domain.

If

$$
g(x,y)=f(x,y)*h(x,y)
$$

then

$$
G(u,v)=F(u,v)\times H(u,v)
$$

Similarly,

multiplication in the spatial domain corresponds to convolution in the frequency domain.

This property makes frequency-domain filtering computationally efficient.

---

## 4. Periodicity

The Fourier Transform of a discrete image is **periodic** in both spatial and frequency domains.

This periodicity is considered when designing frequency-domain filters.

---

## 5. Symmetry

For a **real-valued image**, the Fourier Transform exhibits **complex conjugate symmetry**.

This means one half of the spectrum is the mirror image (complex conjugate) of the other half, reducing redundant information.

---

## 6. Rotation Property

If an image is rotated in the spatial domain, its Fourier Transform rotates by the **same angle** in the frequency domain.

---

# Advantages of Fourier Transform

* Separates low- and high-frequency information.
* Makes filtering easier.
* Efficient for image enhancement and restoration.
* Useful for compression and feature analysis.

---

# Exam Answer (1+1+4 Marks)

### (a) Fourier Transform (1 Mark)

The **Fourier Transform (FT)** is a mathematical transform that converts an image or signal from the **spatial domain** to the **frequency domain**, representing it as a combination of sinusoidal frequency components.

---

### (b) Application in Digital Image Processing (1 Mark)

In digital image processing, the image is transformed into the frequency domain using the Fourier Transform, processed with filters such as **Low Pass Filters (LPF)** or **High Pass Filters (HPF)**, and then converted back to the spatial domain using the **Inverse Fourier Transform**. It is used for **noise removal, smoothing, sharpening, restoration, and compression**.

---

### (c) Properties of Fourier Transform (4 Marks)

1. **Linearity:** The transform of a linear combination equals the same linear combination of the transforms.

2. **Translation (Shifting):** Shifting an image changes the phase but not the magnitude of its Fourier Transform.

3. **Convolution:** Convolution in the spatial domain becomes multiplication in the frequency domain.

$$
g(x,y)=f(x,y)*h(x,y)
$$

$$
G(u,v)=F(u,v)\times H(u,v)
$$

4. **Periodicity:** The Fourier Transform of a discrete image is periodic.

5. **Symmetry:** For real-valued images, the Fourier Transform has complex conjugate symmetry.

6. **Rotation:** Rotating an image causes its Fourier Transform to rotate by the same angle.

> **Exam Tip:** For a **4-mark properties question**, writing **Linearity, Translation, Convolution, and Periodicity** with one or two lines of explanation each is usually sufficient. If asked for more detail, you can additionally mention **Symmetry** and **Rotation**.
