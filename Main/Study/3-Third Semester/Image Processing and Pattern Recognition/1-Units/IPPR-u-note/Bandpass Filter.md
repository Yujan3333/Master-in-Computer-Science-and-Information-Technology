#ippr #third-semester 

# Bandpass Filter

## Definition

A **Bandpass Filter (BPF)** is a frequency domain filter that **passes (retains) a specified range of frequencies** while **attenuating or rejecting both low-frequency and high-frequency components**.

In other words, it allows only the frequencies within a selected band to pass through.

---

## Working Principle

A bandpass filter is obtained by combining:

* A **High-Pass Filter (HPF)** to remove low frequencies.
* A **Low-Pass Filter (LPF)** to remove high frequencies.

Only the frequencies between the two cutoff frequencies are preserved.

---

## Frequency Response

```text
Amplitude

1 ──────────      ──────────
            │      │
            │      │
0 ──────────┴──────┴────────────► Frequency
          D₀₁    D₀₂

Blocked   Pass   Blocked
```

where:

* $D_{01}$ = Lower cutoff frequency
* $D_{02}$ = Upper cutoff frequency

The filter passes frequencies satisfying:

$$
D_{01} < D(u,v) < D_{02}
$$

where:

* $D(u,v)$ = Distance from the center of the frequency spectrum

---

## Ideal Bandpass Filter

The transfer function is

$$
H(u,v)=
\begin{cases}
1, & D_{01}<D(u,v)<D_{02} \\
0, & \text{otherwise}
\end{cases}
$$

---

## Characteristics

* Passes only a selected range of frequencies.
* Removes both very low and very high frequencies.
* Enhances features corresponding to the selected frequency band.
* Implemented in the frequency domain.

---

## Advantages

* Removes unwanted low-frequency background.
* Eliminates high-frequency noise.
* Improves detection of features within a specific frequency range.
* Useful for image enhancement and texture analysis.

---

## Disadvantages

* Proper cutoff frequencies must be selected.
* Incorrect cutoff values may remove useful image information.
* Ideal bandpass filters may introduce ringing artifacts.

---

## Applications

* Texture analysis
* Medical image processing
* Remote sensing
* Fingerprint enhancement
* Image enhancement
* Feature extraction

---

## Difference from Other Frequency Filters

| Filter                    | Passes             | Removes                  |
| ------------------------- | ------------------ | ------------------------ |
| Low-Pass Filter (LPF)     | Low frequencies    | High frequencies         |
| High-Pass Filter (HPF)    | High frequencies   | Low frequencies          |
| **Bandpass Filter (BPF)** | Middle frequencies | Low and high frequencies |

---

## Memory Trick

* **LPF → Low frequencies pass.**
* **HPF → High frequencies pass.**
* **BPF → Only the middle band passes.**

Think of it as:

```text
Low      Middle      High

❌────────✅────────❌
```

Only the **middle frequency band** is allowed to pass.

---

# Exam Tip

**Definition (2 Marks):**

> A **Bandpass Filter** is a frequency domain filter that passes a specified range of frequencies while rejecting frequencies below the lower cutoff frequency and above the upper cutoff frequency.

**Important Formula (5 Marks):**

$$
H(u,v)=
\begin{cases}
1, & D_{01}<D(u,v)<D_{02} \\
0, & \text{otherwise}
\end{cases}
$$

Remember:

* **LPF = Smooths the image.**
* **HPF = Sharpens the image.**
* **Bandpass Filter = Preserves only the middle-frequency components.**

