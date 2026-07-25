#advanced-cryptography #third-semester 

# Q. Describe the Linear Feedback Shift Registers (LFSRs) in generating pseudorandom keystreams. Given an LFSR with a feedback polynomial $x^4 + x^3 + 1$ and an initial state $[1,0,1,1]$, generate the first 8 bits of the keystream. **(3+2)**

---

# Answer

## (a) Linear Feedback Shift Register (LFSR) (3 Marks)

A **Linear Feedback Shift Register (LFSR)** is a shift register used to generate **pseudorandom binary sequences (keystreams)** in stream ciphers.

It consists of:

* A series of flip-flops (registers).
* XOR gates for feedback.
* A feedback polynomial that determines which register bits are XORed.

At each clock pulse:

1. The **output bit** is taken from the last register.
2. The selected tap bits are XORed to produce the **feedback bit**.
3. All bits shift one position to the right.
4. The feedback bit enters the leftmost register.

### Advantages

* Simple and fast.
* Requires little hardware.
* Generates long pseudorandom sequences.
* Widely used in stream ciphers.

---

## (b) Generate the First 8 Keystream Bits (2 Marks)

### Given

Feedback polynomial:

$$
x^4+x^3+1
$$

This means the feedback is:

* Register 4
* Register 3

Initial state:

$$
[1,0,1,1]
$$

Assume:

* **Output = Rightmost bit**
* **Feedback = Register 4 XOR Register 3**

---

### Step-by-Step

| Clock   | Register State | Output | Feedback $(R_4 \oplus R_3)$ |
| ------- | -------------- | ------ | --------------------------- |
| Initial | 1 0 1 1        | **1**  | $1\oplus1=0$                |
| 1       | 0 1 0 1        | **1**  | $1\oplus0=1$                |
| 2       | 1 0 1 0        | **0**  | $0\oplus1=1$                |
| 3       | 1 1 0 1        | **1**  | $1\oplus0=1$                |
| 4       | 1 1 1 0        | **0**  | $0\oplus1=1$                |
| 5       | 1 1 1 1        | **1**  | $1\oplus1=0$                |
| 6       | 0 1 1 1        | **1**  | $1\oplus1=0$                |
| 7       | 0 0 1 1        | **1**  | $1\oplus1=0$                |

---

### First 8 Keystream Bits

Taking the output from the initial state and the next seven shifts:

$$
\boxed{11010111}
$$

---

# Final Answer

* **LFSR** is a shift register that generates pseudorandom keystreams using XOR feedback defined by a feedback polynomial.
* For the feedback polynomial $$x^4+x^3+1$$ and initial state $$[1,0,1,1]$$, the **first 8 keystream bits are**:

$$
\boxed{11010111}
$$

> **Exam Tip:** Some textbooks use a different convention for the shift direction or for which bit is treated as the output. If your instructor follows a different convention, the sequence may differ, but the method (feedback → shift → output) remains the same.
