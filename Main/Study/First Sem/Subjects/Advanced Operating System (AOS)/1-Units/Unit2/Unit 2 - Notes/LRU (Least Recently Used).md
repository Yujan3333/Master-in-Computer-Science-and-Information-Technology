![](../../../../../../../../Images/First_Sem_Images/LRU%20(Least%20Recently%20Used).png)

- [Implementation of LRU](Implementation%20of%20LRU.md)
---
## Question
Calculate no of Page fault

For 3 frame and the page reference in order of

– 0	1	2	3	2	1	0	3	2	3

### 📘 **Page Reference String:**

`0, 1, 2, 3, 2, 1, 0, 3, 2, 3`

### 📦 **Number of Page Frames:** 3

---

### ✅ LRU (Least Recently Used) Algorithm:

- When a page needs to be replaced, LRU chooses the **page that hasn’t been used for the longest time**.
    
- We keep track of **recent usage history**.
    

---

### 🧮 Step-by-step Table

|Step|Page|Frame Content|Page Fault|Replaced Page|
|---|---|---|---|---|
|1|0|[0]|✅|-|
|2|1|[0, 1]|✅|-|
|3|2|[0, 1, 2]|✅|-|
|4|3|[1, 2, 3]|✅|0 (Least Used)|
|5|2|[1, 2, 3]|❌|-|
|6|1|[1, 2, 3]|❌|-|
|7|0|[2, 3, 0]|✅|1 (Least Used)|
|8|3|[2, 3, 0]|❌|-|
|9|2|[2, 3, 0]|❌|-|
|10|3|[2, 3, 0]|❌|-|

---

### ✅ **Total Page Faults = 5**

They occurred at:

- `0, 1, 2, 3, 0`  
    (steps 1, 2, 3, 4, and 7)
    

---

### Final Answer:

> **Number of Page Faults using LRU = 5**