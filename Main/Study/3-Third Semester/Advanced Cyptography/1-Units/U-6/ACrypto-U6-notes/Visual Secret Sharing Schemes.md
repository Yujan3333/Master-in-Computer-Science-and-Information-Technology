#advanced-cryptography #third-semester

# Visual Secret Sharing Scheme (VSS)

## What is a Visual Secret Sharing Scheme?

A **Visual Secret Sharing Scheme (VSS)** is a secret-sharing technique in which a **secret image** is divided into several **image shares**. Individually, each share looks like random noise and reveals **no information** about the secret. When the required number of shares are **stacked together**, the original secret image becomes visible.

It was introduced by **Moni Naor** and **Adi Shamir** in **1994**.

---

# Main Idea

Instead of dividing a **text secret**, we divide an **image** into multiple image shares.

Each share appears as random black-and-white pixels.

* A single share reveals **nothing**.
* Only when enough shares are combined does the hidden image appear.

---

# Real-Life Analogy

Imagine a treasure map printed on two transparent sheets.

* Sheet 1 alone looks like random dots.
* Sheet 2 alone also looks random.

When you place one sheet on top of the other, the treasure map becomes visible.

This is exactly how a **Visual Secret Sharing Scheme** works.

---

# Why is it Needed?

Visual Secret Sharing is used to securely store or transmit secret images such as:

* Signatures
* Fingerprints
* Password images
* Medical images
* Military maps

Without all the required shares, no one can see the secret image.

---

# How Does It Work?

Suppose we have a secret image.

The image is divided into **multiple shares**.

Example:

```text
Secret Image

    😊

       │
       ▼

-------------------------
| Share 1 | Share 2 |
-------------------------
```

Each share looks like random black-and-white pixels.

```text
Share 1

█ ░ █ ░
░ █ ░ █

Share 2

░ █ ░ █
█ ░ █ ░
```

Looking at a single share gives **no clue** about the secret image.

---

# Reconstruction

When both shares are stacked together:

```text
Share 1

█ ░ █ ░
░ █ ░ █

+

Share 2

░ █ ░ █
█ ░ █ ░

=

Secret Image
```

The hidden image becomes visible to the human eye.

No complex calculations are required.

---

# (2,2) Visual Secret Sharing

The simplest VSS is the **(2,2) scheme**.

It means:

* Total shares = 2
* Required shares = 2

| Shares Available | Secret Visible? |
| ---------------- | --------------- |
| 1                | ❌ No            |
| 2                | ✅ Yes           |

---

# (2,n) Visual Secret Sharing

One secret image is divided into **n shares**.

Any **2 shares** are enough to reveal the secret image.

Example:

$$
(2,5)
$$

There are:

* 5 shares
* Any 2 shares can reconstruct the secret.

---

# Advantages

* Very easy to use.
* No decryption algorithm is required.
* Secret is revealed simply by stacking the shares.
* Individual shares reveal no information.
* High security for image-based secrets.

---

# Disadvantages

* Shares are usually larger than the original image.
* Image quality may decrease after reconstruction.
* Mainly suitable for images rather than text.
* Requires all required shares for reconstruction.

---

# Applications

* Digital signatures
* Biometric authentication (fingerprints, iris scans)
* Medical image protection
* Military confidential maps
* Secure document authentication
* Bank cheque and watermark security

---

# Difference Between Shamir's Threshold Scheme and Visual Secret Sharing

| Feature                | Shamir's Threshold Scheme         | Visual Secret Sharing  |
| ---------------------- | --------------------------------- | ---------------------- |
| Secret Type            | Text, password, cryptographic key | Image                  |
| Shares                 | Numerical shares                  | Image shares           |
| Reconstruction         | Lagrange Interpolation            | Stack the image shares |
| Computation Required   | Yes                               | No                     |
| Human Eye Can Recover? | No                                | Yes                    |

---

# Flow Diagram

```text
            Secret Image

                 │
                 ▼

        Divide into Shares

                 │

        ┌────────┴────────┐
        ▼                 ▼
     Share 1          Share 2

        │                 │
        └────────┬────────┘
                 ▼

      Stack the Shares

                 ▼

     Original Secret Image
```

---

# Exam Answer (5 Marks)

### Definition

A **Visual Secret Sharing Scheme (VSS)** is a cryptographic technique in which a **secret image** is divided into multiple **image shares**. Each share appears random and reveals no information individually. The original image is recovered by stacking the required number of shares together without performing mathematical decryption.

### Working

1. Divide the secret image into multiple image shares.
2. Distribute one share to each participant.
3. Each share appears as random noise.
4. Stack the required number of shares.
5. The original secret image becomes visible.

### Advantages

* No computation required for reconstruction.
* Individual shares reveal no information.
* Simple and secure for image-based secrets.
* Easy to implement.

---

# **Memory Trick**

Think of **Visual Secret Sharing** as **splitting a photo into transparent sheets**.

* **One sheet** → Looks like random dots ❌
* **All required sheets together** → Secret image appears ✅

This simple idea is the core concept of Visual Secret Sharing and is usually sufficient for MCA exam questions.
