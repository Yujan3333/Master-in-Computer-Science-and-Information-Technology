#ippr #third-semester 

# 13. Explain How Will You Use the Band Reject Filter in Image Restoration. **[6 Marks]**
---

# Band Reject Filter (BRF)

## Definition

A **Band Reject Filter (BRF)** is a **frequency-domain filter** that **rejects (removes)** a specific range (band) of frequencies while allowing both **low-frequency** and **high-frequency** components outside that band to pass.

It is mainly used to remove **periodic noise** from images.

---

# Why is it Used?

Some images are corrupted by periodic interference, such as:

* Electrical interference
* Scanner noise
* Mechanical vibration
* Power-line interference

These unwanted signals appear as **bright spots** in the Fourier spectrum. A Band Reject Filter removes these frequencies while preserving the remaining image information.

---

# Frequency Response

```text
Gain

1
│      ──────          ──────
│            │        │
│            │        │
│            └────────┘
0└────────────────────────────────► Frequency

      Low      Rejected      High
```

* Low frequencies → Passed
* Middle frequency band → Rejected
* High frequencies → Passed

---

# Transfer Function (Ideal Band Reject Filter)

The Ideal Band Reject Filter is

$$
H(u,v)=
\begin{cases}
0, & D_0-\dfrac{W}{2}\le D(u,v)\le D_0+\dfrac{W}{2} \
1, & \text{otherwise}
\end{cases}
$$

where

* $$D(u,v)$$ = Distance from the center of the frequency plane.
* $$D_0$$ = Center frequency of the rejected band.
* $$W$$ = Width of the rejected band.

---

# Butterworth Band Reject Filter

The transfer function is

$$
H(u,v)
======

\frac{1}
{1+
\left(
\dfrac{D(u,v),W}
{D(u,v)^2-D_0^2}
\right)^{2n}
}
$$

where

* $$D_0$$ = Cutoff frequency
* $$W$$ = Bandwidth
* $$n$$ = Order of the filter

The Butterworth filter has a **smooth transition**, reducing ringing artifacts.

---

# Gaussian Band Reject Filter

The transfer function is

$$
H(u,v)
======

1-
\exp
\left[
-\frac12
\left(
\frac{D(u,v)^2-D_0^2}
{D(u,v),W}
\right)^2
\right]
$$

It provides the smoothest transition and produces very little ringing.

---

# Algorithm for Image Restoration Using Band Reject Filter

1. Read the degraded image.

2. Compute the **2D Fourier Transform** of the image.

3. Shift the spectrum so that the origin is at the center.

4. Identify the frequency band corresponding to periodic noise.

5. Design a Band Reject Filter (Ideal, Butterworth, or Gaussian).

6. Multiply the Fourier spectrum by the filter:

   $$
   G(u,v)=H(u,v)\times F(u,v)
   $$

7. Apply the inverse Fourier Transform.

8. Take the real part of the result.

9. Display the restored image.

---

# Block Diagram

```text
Degraded Image
       │
       ▼
2D Fourier Transform
       │
       ▼
Shift Spectrum
       │
       ▼
Apply Band Reject Filter
       │
       ▼
Inverse Fourier Transform
       │
       ▼
Restored Image
```

---

# Advantages

* Removes periodic noise effectively.
* Preserves most image details.
* Can be implemented using Ideal, Butterworth, or Gaussian filters.

---

# Disadvantages

* Requires knowledge of the noise frequency.
* May remove useful image information if the rejected band is too wide.
* Frequency-domain implementation is computationally expensive.

---

# Applications

* Removing periodic electronic interference.
* Scanner image restoration.
* Satellite image processing.
* Medical image restoration.
* Industrial inspection systems.

---

# Difference Between Band Reject and Bandpass Filter

| Band Reject Filter                      | Bandpass Filter                                       |
| --------------------------------------- | ----------------------------------------------------- |
| Rejects a selected band of frequencies. | Passes only a selected band of frequencies.           |
| Used to remove periodic noise.          | Used to preserve useful middle-frequency information. |
| Low and high frequencies are retained.  | Low and high frequencies are removed.                 |
| Mainly used in image restoration.       | Used in restoration and feature extraction.           |

---

# Exam Answer (6 Marks)

A **Band Reject Filter (BRF)** is a frequency-domain filter that removes a specified range of frequencies while allowing lower and higher frequencies to pass. It is mainly used to eliminate **periodic noise** from images.

The basic implementation steps are:

1. Compute the 2D Fourier Transform of the degraded image.
2. Shift the spectrum to the center.
3. Identify the noisy frequency band.
4. Design a Band Reject Filter.
5. Multiply the spectrum by the filter.
6. Apply the inverse Fourier Transform to obtain the restored image.

The Ideal Band Reject Filter is defined as

$$
H(u,v)=
\begin{cases}
0, & D_0-\dfrac{W}{2}\le D(u,v)\le D_0+\dfrac{W}{2} \
1, & \text{otherwise}
\end{cases}
$$

Band Reject Filters are widely used to remove periodic interference in satellite, medical, and scanned images.

---
