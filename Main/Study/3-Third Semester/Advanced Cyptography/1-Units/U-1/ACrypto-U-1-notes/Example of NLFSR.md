#advanced-cryptography #example 


### LFSR Example (Linear)

Feedback uses **only XOR**.

Register:

```text
1 0 1 1
```

Feedback:

```text
New bit = Bit1 ⊕ Bit4
```

Calculation:

```text
1 ⊕ 1 = 0
```

After shifting:

```text
Before: 1 0 1 1
After : 0 1 0 1
```

---

### NLFSR Example (Non-Linear)

Register:

```text
1 0 1 1
```

Feedback:

```text
New bit = (Bit1 AND Bit2) ⊕ Bit4
```

Calculation:

```text
Bit1 AND Bit2 = 1 AND 0 = 0

0 ⊕ 1 = 1
```

New bit = **1**

After shifting:

```text
Before: 1 0 1 1
After : 1 1 0 1
```

---

### Key Difference

| LFSR          | NLFSR                       |
| ------------- | --------------------------- |
| `Bit1 ⊕ Bit4` | `(Bit1 AND Bit2) ⊕ Bit4`    |
| Uses only XOR | Uses AND + XOR (non-linear) |

### Easy way to remember

* **LFSR:** `XOR only`
* **NLFSR:** `XOR + other logic gates (AND, OR, NOT, etc.)`

The important point is that **NLFSR combines at least one non-linear operation (like AND, OR, NAND, NOR) with other logic to generate a less predictable keystream.**
