#ippr #third-semester 

# Explain the FFT Algorithm for the One-Dimensional Case (7 Marks)

## Definition

The **Fast Fourier Transform (FFT)** is an efficient algorithm for computing the **Discrete Fourier Transform (DFT)**. It significantly reduces the computational complexity from

$$
O(N^2)
$$

to

$$
O(N\log_2N)
$$

by recursively dividing the DFT into smaller DFTs.

---

# Discrete Fourier Transform (DFT)

For an input sequence

$$
x(n), \quad n=0,1,\ldots,N-1
$$

the DFT is

$$
X(k)=\sum_{n=0}^{N-1}x(n)W_N^{nk},
\qquad
k=0,1,\ldots,N-1
$$

where

$$
W_N=e^{-j\frac{2\pi}{N}}
$$

is called the **twiddle factor**.

---

# Principle of FFT

The FFT uses the **Divide and Conquer** strategy.

The input sequence is divided into:

* Even-indexed samples
* Odd-indexed samples

Instead of computing one large DFT, FFT computes two smaller DFTs recursively and then combines their results.

---

# Derivation

The DFT is

$$
X(k)=\sum_{n=0}^{N-1}x(n)W_N^{nk}
$$

Separate the sequence into even and odd samples.

Even samples:

$$
x(0),x(2),x(4),\ldots
$$

Odd samples:

$$
x(1),x(3),x(5),\ldots
$$

Then,

$$
X(k)
====

\sum_{r=0}^{\frac{N}{2}-1}
x(2r)W_{\frac{N}{2}}^{rk}
+
W_N^k
\sum_{r=0}^{\frac{N}{2}-1}
x(2r+1)W_{\frac{N}{2}}^{rk}
$$

Let

$$
E(k)
====

\sum_{r=0}^{\frac{N}{2}-1}
x(2r)W_{\frac{N}{2}}^{rk}
$$

and

$$
O(k)
====

\sum_{r=0}^{\frac{N}{2}-1}
x(2r+1)W_{\frac{N}{2}}^{rk}
$$

Therefore,

$$
\boxed{
X(k)=E(k)+W_N^kO(k)
}
$$

and

$$
\boxed{
X\left(k+\frac{N}{2}\right)
===========================

E(k)-W_N^kO(k)
}
$$

These two equations form the basis of the **Radix-2 FFT algorithm**.

---

# FFT Algorithm (One-Dimensional)

1. Read the input sequence of length $N$, where $N=2^m$.
2. Divide the sequence into even-indexed and odd-indexed elements.
3. Compute the DFT of the even and odd sequences recursively.
4. Multiply the odd-sequence DFT by the twiddle factor $W_N^k$.
5. Combine the even and odd DFTs using

$$
X(k)=E(k)+W_N^kO(k)
$$

and

$$
X\left(k+\frac{N}{2}\right)
===========================

E(k)-W_N^kO(k)
$$

6. Repeat the process until the sequence length becomes 1.
7. The combined values give the final FFT.

---

# Flow of FFT

```text
Input Sequence

      │
      ▼
Split into Even and Odd Samples

      │
      ▼
Compute Smaller DFTs

      │
      ▼
Multiply by Twiddle Factors

      │
      ▼
Combine Results

      │
      ▼
Final FFT Output
```

---

# Example (8-Point FFT)

Input sequence

$$
[x_0,x_1,x_2,x_3,x_4,x_5,x_6,x_7]
$$

First split

```text
Even : x₀  x₂  x₄  x₆

Odd  : x₁  x₃  x₅  x₇
```

Then each group is divided again

```text
Even
 ├── x₀ x₄
 └── x₂ x₆

Odd
 ├── x₁ x₅
 └── x₃ x₇
```

This process continues until single elements remain.

The smaller DFTs are then combined to obtain the final FFT output.

---

# Advantages

* Much faster than the direct DFT.
* Reduces computations from $O(N^2)$ to $O(N\log_2N)$.
* Efficient for large data sets.
* Widely used in digital signal and image processing.

---

# Applications

* Image processing
* Signal processing
* Image filtering
* Image compression
* Audio and speech processing
* Medical imaging
* Radar and communication systems

---

# Exam Tips

### Key Points

* FFT is an efficient method to compute the DFT.
* Uses the **Divide and Conquer** approach.
* Splits the sequence into **even** and **odd** samples.
* Uses **Radix-2 decomposition**.
* Combines results using the twiddle factor.

### Important Formula

$$
\boxed{
X(k)=E(k)+W_N^kO(k)
}
$$

$$
\boxed{
X\left(k+\frac{N}{2}\right)
===========================

E(k)-W_N^kO(k)
}
$$

### Complexity

* **DFT:** $O(N^2)$
* **FFT:** $O(N\log_2N)$

### One-Line Definition

> **Fast Fourier Transform (FFT)** is an efficient algorithm for computing the Discrete Fourier Transform by recursively dividing the input sequence into even and odd parts and combining the results, reducing the computational complexity from $O(N^2)$ to $O(N\log_2N)$.

