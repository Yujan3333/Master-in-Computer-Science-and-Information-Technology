#ippr #third-semester 

---

# Butterworth High Pass Filter vs Gaussian High Pass Filter

| Feature           | Butterworth HPF                             | Gaussian HPF                |
| ----------------- | ------------------------------------------- | --------------------------- |
| Transition        | Smooth but controllable                     | Very smooth                 |
| Ringing effect    | Small ringing may occur                     | Almost no ringing           |
| Control parameter | Cutoff frequency $D_0$ and filter order $n$ | Only cutoff frequency $D_0$ |
| Sharpness         | Becomes sharper as $n$ increases            | Always smooth               |
| Formula           | Depends on filter order                     | Exponential function        |
| Edge enhancement  | Stronger (especially for higher $n$)        | More natural and smoother   |

---

# 1. Butterworth High Pass Filter

Transfer function:

$$
H(u,v)=\frac{1}{1+\left(\frac{D_0}{D(u,v)}\right)^{2n}}
$$

where

* $D_0$ = cutoff frequency
* $D(u,v)$ = distance from the center
* $n$ = order of the filter

### Characteristics

* Smooth transition.
* Transition becomes steeper as $n$ increases.
* Higher $n$ makes it behave more like an Ideal High Pass Filter.
* May produce slight ringing.

---

### Shape

```text
1.0 |                    _______
    |                 __/
    |              __/
    |           __/
0.5 |__________/
    |
0.0 +-------------------------
           D₀
```

The curve becomes steeper when the filter order $n$ increases.

---

# 2. Gaussian High Pass Filter

Transfer function:

$$
H(u,v)=1-e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

### Characteristics

* Very smooth transition.
* No filter order.
* Almost no ringing artifacts.
* Produces smoother sharpening.

---

### Shape

```text
1.0 |                 ________
    |              __/
    |           _/
    |        _/
0.5 |_____/
    |
0.0 +--------------------------
          D₀
```

The curve is always smooth.

---

# Visual Comparison

```text
Butterworth

1.0 |                ______
    |            ___/
    |         __/
    |      __/
0.0 +------------------------


Gaussian

1.0 |             ________
    |          __/
    |       _/
    |    _/
0.0 +------------------------
```

Notice that:

* Butterworth has a **steeper** transition.
* Gaussian changes **more gradually**.

---

# Ringing Effect

Suppose an image contains a sharp edge.

Butterworth may produce

```text
████████░░░░████████
```

with small ripples near the edge.

Gaussian produces

```text
████████████████████
```

with much smoother edges and almost no ripples.

---

# Advantages

### Butterworth HPF

* Adjustable using filter order.
* Stronger sharpening.
* More flexible.

### Gaussian HPF

* No ringing.
* Smoothest frequency response.
* Better visual quality.

---

# Disadvantages

### Butterworth

* Slight ringing at higher orders.
* Requires choosing both cutoff frequency and filter order.

### Gaussian

* Less aggressive sharpening.
* Cannot adjust sharpness with a filter order.

---

# Which one is better?

* If you want **strong edge enhancement** and adjustable sharpness, use **Butterworth HPF**.
* If you want **smooth results with minimal ringing**, use **Gaussian HPF**.

---

# Easy Memory Trick

Think of driving over a speed bump.

### Butterworth

The road changes **fairly quickly**.

```text
______/‾‾‾‾
```

A quicker change means a steeper transition.

### Gaussian

The road rises **very gradually**.

```text
_____/~~~~
```

A gradual change means a smoother transition.

---

# Exam Answer (3–5 Marks)

| Butterworth High Pass Filter                                                   | Gaussian High Pass Filter                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| Transfer function: $$H(u,v)=\frac{1}{1+\left(\frac{D_0}{D(u,v)}\right)^{2n}}$$ | Transfer function: $$H(u,v)=1-e^{-\frac{D^2(u,v)}{2D_0^2}}$$ |
| Depends on cutoff frequency and filter order $n$.                              | Depends only on cutoff frequency.                            |
| Transition is smooth and controlled by $n$.                                    | Transition is always very smooth.                            |
| May introduce slight ringing artifacts.                                        | Produces almost no ringing artifacts.                        |
| Provides stronger edge enhancement.                                            | Produces smoother, more natural sharpening.                  |

**Key point to remember:** Both filters remove **low-frequency components** and preserve **high-frequency components** for image sharpening. The main difference is the **shape of the transition**—Butterworth is controlled by the filter order $n$, while Gaussian uses a smooth exponential response and minimizes ringing.
