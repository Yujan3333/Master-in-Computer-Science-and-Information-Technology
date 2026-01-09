
# **PageRank Problem**
![](../../../../../../../Images/Second_Sem_Images/PageRank%20Algorithm-que.png)


We have **4 pages:** A, B, C, D

**Links:**

* B → A, C
* C → A
* D → A, B, C

No self-links. Multiple links to the same page → count as 1.

**Damping factor:** (d = 0.85)
**Initial PR:** All pages equal → (PR_0 = 1/4 = 0.25)

---

## **Step 1: PageRank Formula**

The PageRank of a page (P):

$$
PR(P) = \frac{1-d}{N} + d \sum_{i \in M(P)} \frac{PR(i)}{C(i)}
$$

Where:

* (N = 4) (total pages)
* (M(P)) = set of pages linking to P
* (C(i)) = number of outbound links from page i

---

## **Step 2: Identify inbound links and outbound counts**

| Page | Inbound links | Outbound count (C(i)) of each linking page |
| ---- | ------------- | ------------------------------------------ |
| A    | B, C, D       | B → 2, C → 1, D → 3                        |
| B    | D             | D → 3                                      |
| C    | B, D          | B → 2, D → 3                               |
| D    | none          | —                                          |

---

## **Step 3: Apply initial PR (0.25) – First iteration**

### **PR(A)**

$$
PR(A) = \frac{1-d}{N} + d \left( \frac{PR(B)}{C(B)} + \frac{PR(C)}{C(C)} + \frac{PR(D)}{C(D)} \right)
$$

Substitute values:

* $( \frac{1-d}{N} = \frac{1-0.85}{4} = 0.0375 )$
* $(PR(B)/C(B) = 0.25 / 2 = 0.125)$
* (PR(C)/C(C) = 0.25 / 1 = 0.25)
* $(PR(D)/C(D) = 0.25 / 3 \approx 0.0833)$

$$
PR(A) = 0.0375 + 0.85 (0.125 + 0.25 + 0.0833)
$$

First, sum inside parentheses:

$$
0.125 + 0.25 + 0.0833 = 0.4583
$$

Multiply by 0.85:

$$
0.85 \times 0.4583 \approx 0.3896
$$

Add 0.0375:

$$
PR(A) \approx 0.0375 + 0.3896 = 0.4271
$$

✅ **PR(A) ≈ 0.427**

---

### **PR(B)**

Inbound links: D only

$$
PR(B) = 0.0375 + 0.85 \left( \frac{PR(D)}{C(D)} \right)
$$

$$
PR(B) = 0.0375 + 0.85 (0.25 / 3) = 0.0375 + 0.85(0.0833)
$$

$$
PR(B) = 0.0375 + 0.0708 = 0.1083
$$

✅ **PR(B) ≈ 0.108**

---

### **PR(C)**

Inbound links: B, D

$$
PR(C) = 0.0375 + 0.85 \left( \frac{PR(B)}{C(B)} + \frac{PR(D)}{C(D)} \right)
$$

$$
PR(C) = 0.0375 + 0.85 \left(0.25/2 + 0.25/3\right)
$$

$$
0.25/2 = 0.125, \quad 0.25/3 \approx 0.0833
$$

Sum = 0.125 + 0.0833 = 0.2083

Multiply by 0.85:

$$
0.2083 \times 0.85 \approx 0.1771
$$

Add 0.0375:

$$
PR(C) \approx 0.0375 + 0.1771 = 0.2146
$$

✅ **PR(C) ≈ 0.215**

---

### **PR(D)**

Inbound links: none

$$
PR(D) = 0.0375 + 0.85 (0) = 0.0375
$$

✅ **PR(D) ≈ 0.038**

---

## **Step 4: First Iteration Results**

| Page | PR (iteration 1) |
| ---- | ---------------- |
| A    | 0.427            |
| B    | 0.108            |
| C    | 0.215            |
| D    | 0.038            |

> We would normally repeat **iterations 2, 3… until PR converges**, but for exams, **usually 1 iteration is enough** to show understanding.

---

### **Step 5: Key Points to Write in Exam**

* Mention **damping factor** and **initial PR = 1/N**
* Identify **inbound links and outbound counts**
* Show **formula with values**
* Solve **step by step for each page**
* Optional: mention **iterations are repeated until convergence**

---

