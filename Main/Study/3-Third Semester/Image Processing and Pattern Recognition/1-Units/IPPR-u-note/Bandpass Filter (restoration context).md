#ippr #third-semester 

# 9. Short Note: Bandpass Filter (Restoration Context) **[2.5 Marks]**

This is a **short-note** question. A concise answer with definition, transfer function, uses, advantages, and disadvantages is enough.

---

# Bandpass Filter

## Definition

A **Bandpass Filter (BPF)** is a frequency-domain filter that **passes (retains)** frequencies within a specified range and **rejects** both low-frequency and high-frequency components.

It is mainly used in **image restoration** to preserve useful image information lying in a particular frequency band while removing unwanted frequencies.

---

# Working Principle

A Bandpass Filter is obtained by combining a:

* **High Pass Filter (HPF)** → removes low-frequency components.
* **Low Pass Filter (LPF)** → removes high-frequency components.

Therefore, only the frequencies lying between the two cutoff frequencies are retained.

```text
Low Frequency      Middle Frequency        High Frequency
     |-----------------|-----------------------|
        Removed             Passed              Removed
```

---

# Transfer Function

The Bandpass Filter is given by

$$
H_{BP}(u,v)=H_{LP}(u,v)\times H_{HP}(u,v)
$$

where

* $$H_{LP}(u,v)$$ = Low Pass Filter transfer function.
* $$H_{HP}(u,v)$$ = High Pass Filter transfer function.

---

# Frequency Response

```text
Gain

1.0              ┌──────────┐
                 │          │
                 │          │
0.0 ─────────────┘          └────────────► Frequency
              D1            D2

D1 = Lower cutoff frequency
D2 = Upper cutoff frequency
```

Only frequencies between $$D_1$$ and $$D_2$$ pass through.

---

# Applications

* Image restoration.
* Texture analysis.
* Medical image processing.
* Remote sensing.
* Pattern recognition.

---

# Advantages

* Preserves important middle-frequency information.
* Removes low-frequency background variations.
* Reduces high-frequency noise.
* Improves feature extraction.

---

# Disadvantages

* Cutoff frequencies must be selected carefully.
* May remove useful image information if the passband is not chosen properly.
* Computationally more expensive than simple spatial filters.

---

# Difference Between LPF, HPF, and BPF

| Low Pass Filter                      | High Pass Filter                 | Bandpass Filter                              |
| ------------------------------------ | -------------------------------- | -------------------------------------------- |
| Passes low frequencies.              | Passes high frequencies.         | Passes only middle frequencies.              |
| Removes noise and smooths the image. | Enhances edges and fine details. | Preserves a selected frequency band.         |
| Used for smoothing.                  | Used for sharpening.             | Used for restoration and feature extraction. |

---

# Exam Answer (2.5 Marks)

A **Bandpass Filter (BPF)** is a frequency-domain filter that passes frequencies within a specified range while rejecting both low and high frequencies. It is formed by combining a Low Pass Filter and a High Pass Filter.

The transfer function is

$$
H_{BP}(u,v)=H_{LP}(u,v)\times H_{HP}(u,v)
$$

It is mainly used in image restoration, texture analysis, and medical imaging to preserve useful mid-frequency components while suppressing background variations and high-frequency noise.

**Advantages:** Preserves useful features, removes unwanted low and high frequencies.

**Disadvantages:** Requires proper selection of cutoff frequencies; otherwise, important image information may be lost.

---

## ⭐ Exam Tip

Don't confuse:

* **Band Reject Filter (BRF):** Rejects a specific band of frequencies and passes the rest. Used to remove periodic noise.
* **Bandpass Filter (BPF):** Passes only a specific band of frequencies and rejects both low and high frequencies. Used to retain useful frequency components.
