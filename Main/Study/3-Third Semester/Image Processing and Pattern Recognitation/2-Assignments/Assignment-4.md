![](../../../../../Images/Third_Sem_Images/Assignment-4-que.png)

### [What is actually happening](IPPR-Assignments/What%20is%20actually%20happening.md)
- [Complete Answer](IPPR-Assignments/Complete%20Answer.md)
---
### ✅ Given

* Number of gray levels: $L=8$
* Formula for histogram equalization:
  $$s_k=(L-1)\sum_{j=0}^{k}p_r(r_j)$$

---

### 🔹 Step 1: Compute Cumulative Distribution (CDF)

| $r_k$ | $p_r(r_k)$ | CDF  |
| ----- | ---------- | ---- |
| 0     | 0.19       | 0.19 |
| 1     | 0.25       | 0.44 |
| 2     | 0.21       | 0.65 |
| 3     | 0.16       | 0.81 |
| 4     | 0.08       | 0.89 |
| 5     | 0.06       | 0.95 |
| 6     | 0.03       | 0.98 |
| 7     | 0.02       | 1.00 |

---

### 🔹 Step 2: Compute Transformation $s_k$

Using:
$$s_k = 7 \times \text{CDF}$$

| $r_k$ | CDF  | $s_k = 7 \cdot \text{CDF}$ | Rounded $s_k$ |
| ----- | ---- | -------------------------- | ------------- |
| 0     | 0.19 | 1.33                       | **1**         |
| 1     | 0.44 | 3.08                       | **3**         |
| 2     | 0.65 | 4.55                       | **5**         |
| 3     | 0.81 | 5.67                       | **6**         |
| 4     | 0.89 | 6.23                       | **6**         |
| 5     | 0.95 | 6.65                       | **7**         |
| 6     | 0.98 | 6.86                       | **7**         |
| 7     | 1.00 | 7.00                       | **7**         |

---

### 🔹 Step 3: Compute $p_s(s_k)$

Group probabilities that map to same $s_k$:

| $s_k$ | From $r_k$      | $p_s(s_k)$                    |
| ----- | --------------- | ----------------------------- |
| 0     | —               | 0                             |
| 1     | $r_0$           | 0.19                          |
| 2     | —               | 0                             |
| 3     | $r_1$           | 0.25                          |
| 4     | —               | 0                             |
| 5     | $r_2$           | 0.21                          |
| 6     | $r_3, r_4$      | 0.16 + 0.08 = **0.24**        |
| 7     | $r_5, r_6, r_7$ | 0.06 + 0.03 + 0.02 = **0.11** |

---

### ✅ Final Answer

#### ✔ Transformation Function:

$$s_k = 7 \cdot \sum_{j=0}^{k} p_r(r_j)$$

#### ✔ Mapping:

$$0\to1,;1\to3,;2\to5,;3\to6,;4\to6,;5\to7,;6\to7,;7\to7$$

#### ✔ Output Histogram:

$$p_s(s_k) = {0,;0.19,;0,;0.25,;0,;0.21,;0.24,;0.11}$$

---

# Tag
#ippr #assignment #third-semester 