#ippr #third-semester 

# Fast Fourier Transform (FFT)

## Definition

The **Fast Fourier Transform (FFT)** is an efficient algorithm used to compute the **Discrete Fourier Transform (DFT)** and its inverse much faster.

**Important:** FFT is **not a different transform**. It is simply a **fast algorithm for computing the DFT**.

---

# Why Do We Need FFT?

The DFT requires a large number of computations.

For a signal of length $N$:

* **DFT complexity**

$$
O(N^2)
$$

* **FFT complexity**

$$
O(N\log_2N)
$$

Thus, FFT significantly reduces computation time, especially for large images.

---

# Basic Idea of FFT

Instead of computing every DFT term directly, FFT uses the **divide-and-conquer** approach.

It divides the input sequence into:

* Even-indexed elements
* Odd-indexed elements

Then it computes smaller DFTs and combines the results.

---

# FFT Procedure (Radix-2 FFT)

Suppose the input sequence is

$$
x(0),x(1),x(2),x(3),x(4),x(5),x(6),x(7)
$$

Split it into

Even-indexed elements:

$$
x(0),x(2),x(4),x(6)
$$

Odd-indexed elements:

$$
x(1),x(3),x(5),x(7)
$$

Compute the DFT of each half separately.

Combine the two smaller DFTs to obtain the complete DFT.

Repeat this process recursively until only single-element sequences remain.

---

# FFT Flow

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
Combine Results
       │
       ▼
Final DFT
```

---

# Butterfly Operation

The basic computation in FFT is called the **butterfly operation**.

```text
      a
       \
        \
         X------ Output 1
        /
       /
      b
        \
         ------ Output 2
```

Each butterfly combines two values using simple addition, subtraction, and multiplication by a **twiddle factor**.

---

# Twiddle Factor

The twiddle factor is

$$
W_N=e^{-j\frac{2\pi}{N}}
$$

or

$$
W_N^k=e^{-j\frac{2\pi k}{N}}
$$

It is used to combine the even and odd DFT results.

---

# Advantages of FFT

* Much faster than DFT.
* Reduces computation time significantly.
* Efficient for large images.
* Widely used in digital image and signal processing.

---

# Disadvantages

* Standard Radix-2 FFT works most efficiently when the number of samples is a power of 2:

$$
N=2^m
$$

* The algorithm is more complex than directly computing the DFT.

---

# Applications

* Image enhancement
* Frequency-domain filtering
* Image compression
* Medical image processing
* Audio and speech processing
* Radar and communication systems

---

# DFT vs FFT

| DFT                         | FFT                                   |
| --------------------------- | ------------------------------------- |
| Mathematical transform      | Algorithm to compute the DFT          |
| Direct computation          | Divide-and-conquer algorithm          |
| Complexity: $$O(N^2)$$      | Complexity: $$O(N\log_2N)$$           |
| Slower                      | Faster                                |
| More computations           | Fewer computations                    |
| Used for frequency analysis | Used for efficient frequency analysis |

---

# DFT Computation Example

Suppose

$$
N=1024
$$

DFT requires approximately

$$
1024^2=1,!048,!576
$$

operations.

FFT requires approximately

$$
1024\times\log_2(1024)
=1024\times10
=10,!240
$$

operations.

FFT performs dramatically fewer calculations.

---

# Memory Trick

Imagine searching for a word in a book.

### DFT

You read **every page one by one**.

```text
Page 1 → Page 2 → Page 3 → ... → Page 1000
```

### FFT

You repeatedly divide the book into halves until you find the word.

```text
1000 pages
      │
 ┌────┴────┐
500      500
 │          │
250      250
 │          │
...
```

The second approach is much faster.

---

# Exam Answer (5 Marks)

**Definition:**

The **Fast Fourier Transform (FFT)** is an efficient algorithm for computing the **Discrete Fourier Transform (DFT)** and its inverse. It uses the **divide-and-conquer** technique to reduce the number of computations.

**Working:**

1. Divide the input sequence into even- and odd-indexed samples.
2. Compute the DFT of each smaller sequence recursively.
3. Combine the results using butterfly operations and twiddle factors.
4. Continue until the complete DFT is obtained.

**Complexity:**

* DFT:

$$
O(N^2)
$$

* FFT:

$$
O(N\log_2N)
$$

**Advantages:**

* Faster computation.
* Reduced computational complexity.
* Suitable for large images and real-time applications.

> **Key point for exams:**
> **DFT** is the mathematical transform, while **FFT** is the efficient algorithm used to compute the same DFT result much faster.
