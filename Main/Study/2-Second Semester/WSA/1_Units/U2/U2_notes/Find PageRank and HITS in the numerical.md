![](../../../../../../../Images/Second_Sem_Images/Find%20PageRank%20and%20HITS%20in%20the%20numerical-que2.png)
The graph in the image has **six nodes**: A, B, C, D, E, and F.


---
---

# **Step 0: Data Recap**

| Source | Destinations |
| ------ | ------------ |
| A      | B, E         |
| B      | A, C, E      |
| C      | B            |
| D      | C, E         |
| E      | B, C, D, F   |
| F      | B, E         |

* Pages: A, B, C, D, E, F → N = 6
* PageRank damping factor: **d = 0.85**
* Initial PageRank: **PR₀ = 1/N ≈ 0.1667**
* HITS: initial **hub = 1, authority = 1**

---

# **1️⃣ PageRank – 2 Iterations**

### **Step 1: Outbound Count (C(i))**

| Page | Outbound Links | C(i) |
| ---- | -------------- | ---- |
| A    | B, E           | 2    |
| B    | A, C, E        | 3    |
| C    | B              | 1    |
| D    | C, E           | 2    |
| E    | B, C, D, F     | 4    |
| F    | B, E           | 2    |

---

### **Step 2: Inbound Links**

| Page | Inbound Links |
| ---- | ------------- |
| A    | B             |
| B    | A, C, E, F    |
| C    | B, D, E       |
| D    | E             |
| E    | A, B, D, F    |
| F    | E             |

---

### **Step 3: Iteration 1 – PR formula**

$$[
PR(P) = \frac{1-d}{N} + d \sum_{i \in M(P)} \frac{PR(i)}{C(i)}
]$$

* ((1-d)/N = 0.025)

---

#### **PR₁(A)**

Inbound: B → C(B)=3

$$[
PR₁(A) = 0.025 + 0.85 * (0.1667/3) = 0.025 + 0.85*0.05556 ≈ 0.0723
]$$

#### **PR₁(B)**

Inbound: A, C, E, F → C(A)=2, C(C)=1, C(E)=4, C(F)=2

$$[
PR₁(B) = 0.025 + 0.85*(0.1667/2 + 0.1667/1 + 0.1667/4 + 0.1667/2)
]$$

Step: 0.08335 + 0.1667 + 0.041675 + 0.08335 = 0.3741
0.3741*0.85 ≈ 0.31798
Add 0.025 → **PR₁(B) ≈ 0.3430**

#### **PR₁(C)**

Inbound: B, D, E → 0.1667/3 + 0.1667/2 + 0.1667/4 = 0.05556 + 0.08335 + 0.041675 ≈ 0.1806
Multiply 0.85 → 0.1535
Add 0.025 → **PR₁(C) ≈ 0.1785**

#### **PR₁(D)**

Inbound: E → 0.1667/4 = 0.041675
Multiply 0.85 → 0.03544
Add 0.025 → **PR₁(D) ≈ 0.0604**

#### **PR₁(E)**

Inbound: A, B, D, F → 0.08335 + 0.05556 + 0.08335 + 0.08335 = 0.3056
Multiply 0.85 → 0.2598
Add 0.025 → **PR₁(E) ≈ 0.2848**

#### **PR₁(F)**

Inbound: E → 0.1667/4 = 0.041675
Multiply 0.85 → 0.03544
Add 0.025 → **PR₁(F) ≈ 0.0604**

---

### **Step 4: PageRank Iteration 1 Table**

| Page | PR₁    |
| ---- | ------ |
| A    | 0.0723 |
| B    | 0.3430 |
| C    | 0.1785 |
| D    | 0.0604 |
| E    | 0.2848 |
| F    | 0.0604 |

> Iteration 2: Use these PR₁ values to update PR₂ (optional for exams unless specified).

---

# **2️⃣ HITS – 2 Iterations**

### **Step 1: Correct inbound links**

| Page | Inbound Links |
| ---- | ------------- |
| A    | B             |
| B    | A, C, E, F    |
| C    | B, D, E       |
| D    | E             |
| E    | A, B, D, F    |
| F    | E             |

---

### **Step 2: Iteration 1 – Authority Scores**

* Authority = sum of hub scores of inbound pages (all hub =1 initially)

| Page | Authority₁ |
| ---- | ---------- |
| A    | 1          |
| B    | 1+1+1+1=4  |
| C    | 1+1+1=3    |
| D    | 1          |
| E    | 1+1+1+1=4  |
| F    | 1          |

---

### **Step 3: Iteration 1 – Hub Scores**

* Hub = sum of authority scores of outbound pages

| Page | Hub₁                  |
| ---- | --------------------- |
| A    | B(4)+E(4)=8           |
| B    | A(1)+C(3)+E(4)=8      |
| C    | B(4)=4                |
| D    | C(3)+E(4)=7           |
| E    | B(4)+C(3)+D(1)+F(1)=9 |
| F    | B(4)+E(4)=8           |

---

### **Step 4: Iteration 2 – Authority Scores**

* Authority = sum of **updated hub scores of inbound links**

| Page | Authority₂           |
| ---- | -------------------- |
| A    | B → Hub₁=8 → 8       |
| B    | A+B+E+F → 8+4+9+8=29 |
| C    | B+D+E → 8+7+9=24     |
| D    | E → 9                |
| E    | A+B+D+F → 8+8+7+8=31 |
| F    | E → 9                |

---

### **Step 5: Iteration 2 – Hub Scores**

* Hub = sum of updated authority of outbound links

| Page | Hub₂                     |
| ---- | ------------------------ |
| A    | B(29)+E(31)=60           |
| B    | A(8)+C(24)+E(31)=63      |
| C    | B(29)=29                 |
| D    | C(24)+E(31)=55           |
| E    | B(29)+C(24)+D(9)+F(9)=71 |
| F    | B(29)+E(31)=60           |

---

### **Step 6: Observations about mutual links (A↔B)**

* **Mutual links** slightly reinforce each other’s scores
* Authority of B → increased by A’s hub
* Authority of A → increased by B’s hub
* But the **overall structure** dominates (pages with many inbound links like E have higher authority)

---

### ✅ **Final HITS Iteration 2 (Unnormalized)**

| Page | Authority | Hub |
| ---- | --------- | --- |
| A    | 8         | 60  |
| B    | 29        | 63  |
| C    | 24        | 29  |
| D    | 9         | 55  |
| E    | 31        | 71  |
| F    | 9         | 60  |

---

### **Step 7: Summary – Key Points**

* **PageRank**: Rank flows through links; mutual links slightly boost each other
* **HITS**: Authority = inbound, Hub = outbound; mutual links reinforce both hub & authority
* E is strongest hub & authority due to many links

---
