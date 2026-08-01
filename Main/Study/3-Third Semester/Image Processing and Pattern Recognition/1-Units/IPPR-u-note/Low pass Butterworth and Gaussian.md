#ippr #third-semester 

Both **Butterworth Low Pass Filter (BLPF)** and **Gaussian Low Pass Filter (GLPF)** are used for **image smoothing (blurring)**. They remove **high-frequency components** (edges, fine details, and noise) while preserving **low-frequency components** (smooth regions).

The difference is **how gradually they remove the high frequencies**.

---

# Butterworth Low Pass Filter (BLPF)

## Definition

A **Butterworth Low Pass Filter** passes low frequencies and gradually attenuates high frequencies.

Its transfer function is

$$
H(u,v)=\frac{1}{1+\left(\frac{D(u,v)}{D_0}\right)^{2n}}
$$

where

* $D(u,v)$ = Distance from the center of the frequency plane
* $D_0$ = Cutoff frequency
* $n$ = Order of the filter

---

### Characteristics

* Passes low frequencies.
* Blocks high frequencies.
* Smooth transition.
* Transition sharpness depends on the filter order $n$.
* Higher $n$ makes it closer to an Ideal Low Pass Filter.
* May produce slight ringing.

---

### Shape

```text
H(u,v)

1.0 |─────────────\
    |              \
    |               \
0.5 |                \____
    |
0.0 +--------------------------
          D₀
```

---

# Gaussian Low Pass Filter (GLPF)

## Definition

A **Gaussian Low Pass Filter** also passes low frequencies and attenuates high frequencies, but its transition follows a Gaussian (bell-shaped) curve.

Transfer function

$$
H(u,v)=e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

---

### Characteristics

* Passes low frequencies.
* Removes high frequencies.
* Very smooth transition.
* No filter order.
* Produces almost no ringing.
* Gives smoother blur.

---

### Shape

```text
H(u,v)

1.0 |───────────\
    |            \
    |             \
0.5 |              \__
    |
0.0 +-------------------------
          D₀
```

The curve is smoother than Butterworth.

---

# Comparison

| Feature      | Butterworth LPF                                        | Gaussian LPF                       |
| ------------ | ------------------------------------------------------ | ---------------------------------- |
| Purpose      | Image smoothing                                        | Image smoothing                    |
| Passes       | Low frequencies                                        | Low frequencies                    |
| Removes      | High frequencies                                       | High frequencies                   |
| Formula      | $$H(u,v)=\frac{1}{1+\left(\frac{D}{D_0}\right)^{2n}}$$ | $$H(u,v)=e^{-\frac{D^2}{2D_0^2}}$$ |
| Filter order | Yes ($n$)                                              | No                                 |
| Transition   | Smooth and adjustable                                  | Very smooth                        |
| Ringing      | Slight ringing possible                                | Almost no ringing                  |
| Blur         | Stronger and adjustable                                | More natural                       |

---

# Easy Memory Trick

## Butterworth LPF

You have **two controls**:

* Cutoff frequency $D_0$
* Filter order $n$

You can make the blur stronger or weaker by changing $n$.

---

## Gaussian LPF

You have **one control**:

* Cutoff frequency $D_0$

The blur is always smooth.

---

# Relationship Between LPF and HPF

| Low Pass Filter                   | High Pass Filter           |
| --------------------------------- | -------------------------- |
| Passes low frequencies            | Passes high frequencies    |
| Removes noise and fine details    | Enhances edges and details |
| Produces a blurred/smoothed image | Produces a sharpened image |

---

# One Important Pattern to Remember

Notice the formulas:

### Butterworth LPF

$$
H(u,v)=\frac{1}{1+\left(\frac{D}{D_0}\right)^{2n}}
$$

### Butterworth HPF

$$
H(u,v)=\frac{1}{1+\left(\frac{D_0}{D}\right)^{2n}}
$$

The fraction is **reversed**.

---

### Gaussian LPF

$$
H(u,v)=e^{-\frac{D^2}{2D_0^2}}
$$

### Gaussian HPF

$$
H(u,v)=1-e^{-\frac{D^2}{2D_0^2}}
$$

The HPF is simply

$$
\boxed{\text{HPF} = 1 - \text{LPF}}
$$

This relationship is often useful in exams and makes the formulas easier to remember.
