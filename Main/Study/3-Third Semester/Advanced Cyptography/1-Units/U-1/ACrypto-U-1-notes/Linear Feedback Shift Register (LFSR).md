#advanced-cryptography #synchronous-stream-cipher

## LFSR (Linear Feedback Shift Register) – Easy Explanation

### Definition (Exam)

**Linear Feedback Shift Register (LFSR)** is a circuit used to generate a **long sequence of binary bits (0s and 1s)** for cryptography and communication systems.

It consists of:

* A series of **flip-flops (registers)** that store bits.
* A **feedback function** made using **XOR (⊕)** gates.
* At each clock pulse, all bits **shift one position**, and a new bit is generated using XOR.


![](../../../../../../../Images/Third_Sem_Images/Linear%20Feedback%20Shift%20Register%20(LFSR).png)

---

## Simple Idea

Think of an LFSR as a row of boxes.

```
+---+---+---+---+
| 1 | 0 | 1 | 1 |
+---+---+---+---+
```

Every clock cycle:

1. All bits move **one step to the right (or left, depending on design)**.
2. The last bit comes out as the **output**.
3. A **new bit** is calculated by XORing selected bits and inserted into the empty position.

---

## Example

Suppose we have a **4-bit LFSR**.

Initial state:

```
1 0 1 1
```

Choose feedback taps at positions 1 and 4.

New bit:

```
1 ⊕ 1 = 0
```

Shift:

```
Before:
1 0 1 1

After:
0 1 0 1
```

Repeat the same process to generate a long binary sequence.

---

## Why is it called "Linear"?

Because the feedback is calculated using only the **XOR (exclusive OR)** operation, which is a **linear operation** over binary numbers.

---

## Applications of LFSR

* Stream ciphers
* Pseudo-random number generation
* Data scrambling
* Error detection and correction (CRC)
* Digital communication systems

---

## Advantages

* Very fast
* Simple hardware implementation
* Generates long pseudo-random sequences
* Uses very little memory

---

## Disadvantages

* Not truly random
* The sequence eventually repeats (periodic).
* A single LFSR is **not secure enough** for modern cryptography because attackers can predict the sequence if they know enough output bits.

---

## Exam Definition (2 Marks)

> **A Linear Feedback Shift Register (LFSR) is a shift register that generates a pseudo-random sequence of binary bits by shifting stored bits and computing the new input bit using the XOR of selected register bits (feedback taps). It is widely used in stream ciphers, communication systems, and pseudo-random number generation.**

### Easy Memory Trick

**LFSR = Shift + XOR + Repeat**

* **Shift** → Move all bits one position.
* **XOR** → Compute the new bit from selected positions.
* **Repeat** → Produce a long pseudo-random binary sequence.
