#advanced-cryptography #third-semester 

# NLFSR (Non-Linear Feedback Shift Register) – Easy Explanation

## Definition (Exam)

**NLFSR (Non-Linear Feedback Shift Register)** is a type of shift register that generates a **pseudo-random keystream**, but unlike an LFSR, the new bit is produced using a **non-linear feedback function** (such as AND, OR, XOR, etc.).

- [XOR-NAND-NOR-Table](../../../../../4-General-Note/General-Notes/XOR-NAND-NOR-Table.md)

It is more secure than an LFSR because its output is much harder to predict.

---

## Simple Idea

Think of it just like an LFSR:

* It stores bits in registers.
* Bits shift one position at every clock pulse.
* A new bit is inserted.

**Difference:**

* **LFSR:** Uses only **XOR** (linear feedback).
* **NLFSR:** Uses a **combination of logic operations** (XOR, AND, OR, NOT, etc.), making the feedback non-linear.

---

## [Example of NLFSR](Example%20of%20NLFSR.md)

Suppose the register contains:

```text
1 0 1 1
```

An example non-linear feedback function could be:

```text
New bit = (Bit1 AND Bit2) XOR Bit4
```

The register shifts, and the new bit is inserted. Repeating this process generates a **keystream**.

---

## Why is it called "Non-Linear"?

Because the feedback function is **not limited to XOR**. It uses non-linear logic operations like **AND, OR, and NOT**, making the generated sequence much harder to analyze or predict.

---

## Applications

* Stream ciphers
* Secure keystream generation
* Modern cryptographic systems

---

## Advantages

* More secure than an LFSR.
* Output is much harder to predict.
* Better resistance against cryptographic attacks.

---

## Disadvantages

* More complex to design and implement.
* Slightly slower than an LFSR.

---

## LFSR vs NLFSR

| LFSR                       | NLFSR                                    |
| -------------------------- | ---------------------------------------- |
| Linear feedback (XOR only) | Non-linear feedback (AND, OR, XOR, etc.) |
| Simple design              | More complex design                      |
| Faster                     | Slightly slower                          |
| Easier to predict          | Harder to predict                        |
| Less secure                | More secure                              |

---

## Exam Definition (2 Marks)

> **A Non-Linear Feedback Shift Register (NLFSR) is a shift register that generates a pseudo-random keystream by shifting stored bits and producing the new input bit using a non-linear feedback function. It provides better security than an LFSR because its output is more difficult to predict.**

### Easy Memory Trick

* **LFSR = Linear (XOR only)**
* **NLFSR = Non-Linear (AND, OR, XOR, etc.)**

**Both generate a keystream, but NLFSR produces a much more secure keystream because its feedback is non-linear.**
