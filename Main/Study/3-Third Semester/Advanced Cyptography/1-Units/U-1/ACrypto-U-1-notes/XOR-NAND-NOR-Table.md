#XOR-gate #NAND-gate #NOR-gate

# XOR ($\oplus$)

|  A  |  B  | $A\oplus B$ |
| :-: | :-: | :---------: |
|  0  |  0  |      0      |
|  0  |  1  |      1      |
|  1  |  0  |      1      |
|  1  |  1  |      0      |

**Rule:** Outputs **1** only when the inputs are **different**.

---

# AND ($\cdot$)

|  A  |  B  | $A\cdot B$ |
| :-: | :-: | :--------: |
|  0  |  0  |      0     |
|  0  |  1  |      0     |
|  1  |  0  |      0     |
|  1  |  1  |      1     |

**Rule:** Outputs **1** only when **both inputs are 1**.

---

# OR ($+$)

|  A  |  B  | $A+B$ |
| :-: | :-: | :---: |
|  0  |  0  |   0   |
|  0  |  1  |   1   |
|  1  |  0  |   1   |
|  1  |  1  |   1   |

**Rule:** Outputs **1** if **at least one input is 1**.

---

# NOT ($\overline{A}$)

|  A  | $\overline{A}$ |
| :-: | :------------: |
|  0  |        1       |
|  1  |        0       |

**Rule:** Flips the input bit.

---

# NAND ($\overline{A\cdot B}$)

|  A  |  B  | $\overline{A\cdot B}$ |
| :-: | :-: | :-------------------: |
|  0  |  0  |           1           |
|  0  |  1  |           1           |
|  1  |  0  |           1           |
|  1  |  1  |           0           |

**Rule:** Opposite of **AND**. Outputs **0** only when **both inputs are 1**.

---

# NOR ($\overline{A+B}$)

|  A  |  B  | $\overline{A+B}$ |
| :-: | :-: | :--------------: |
|  0  |  0  |         1        |
|  0  |  1  |         0        |
|  1  |  0  |         0        |
|  1  |  1  |         0        |

**Rule:** Opposite of **OR**. Outputs **1** only when **both inputs are 0**.


---
### XNOR
|  A  |  B  | $\overline{A\oplus B}$ |
| :-: | :-: | :--------------------: |
|  0  |  0  |            1           |
|  0  |  1  |            0           |
|  1  |  0  |            0           |
|  1  |  1  |            1           |
**Rule**: Outputs 1 only when the inputs are equal.

---

## Easy Memory Trick ⭐

| Gate     | When Output is **1**            |
| -------- | ------------------------------- |
| **XOR**  | Inputs are **Different**        |
| **AND**  | **Both** inputs are 1           |
| **OR**   | **At least one** input is 1     |
| **NOT**  | Flips the bit                   |
| **NAND** | **Everything except** both 1    |
| **NOR**  | **Only when both** inputs are 0 |
