![](../../../../../../../../Images/First_Sem_Images/FIFO%20(First-In,%20First-Out).png)

### 📘 Reference String:

`7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`

### 📦 Number of Page Frames: 3

---

### ✅ FIFO (First-In, First-Out) Algorithm:

> Always remove the **oldest loaded page** (the one that came in first).

---

Tracking :

- Current **Page Frame content**
    
- Whether there’s a **Page Fault (✅)** or not (❌)


|Step|Page|Frame Content|Page Fault|
|---|---|---|---|
|1|7|[7]|✅|
|2|0|[7, 0]|✅|
|3|1|[7, 0, 1]|✅|
|4|2|[0, 1, 2] (7 removed)|✅|
|5|0|[0, 1, 2]|❌|
|6|3|[1, 2, 3] (0 removed)|✅|
|7|0|[2, 3, 0] (1 removed)|✅|
|8|4|[3, 0, 4] (2 removed)|✅|
|9|2|[0, 4, 2] (3 removed)|✅|
|10|3|[4, 2, 3] (0 removed)|✅|
|11|0|[2, 3, 0] (4 removed)|✅|
|12|3|[2, 3, 0]|❌|
|13|2|[2, 3, 0]|❌|
### 🔢 Page Fault Count: 10

✅ Page faults occur at:  
**7, 0, 1, 2, 3, 0 (again), 4, 2 (again), 3 (again), 0 (again)**  
Total: **10 page faults**

---
## Next Question
### 📘 Page Reference String:

`0, 1, 2, 3, 2, 1, 0, 3, 2, 3`

### 📦 Number of Page Frames: 4

---

### ✅ FIFO – Step-by-step Table

We’ll track:

- The **frames**
    
- Whether there is a **page fault**

| Step | Page | Frame Content | Page Fault |
| ---- | ---- | ------------- | ---------- |
| 1    | 0    | [0]           | ✅          |
| 2    | 1    | [0, 1]        | ✅          |
| 3    | 2    | [0, 1, 2]     | ✅          |
| 4    | 3    | [0, 1, 2, 3]  | ✅          |
| 5    | 2    | [0, 1, 2, 3]  | ❌          |
| 6    | 1    | [0, 1, 2, 3]  | ❌          |
| 7    | 0    | [0, 1, 2, 3]  | ❌          |
| 8    | 3    | [0, 1, 2, 3]  | ❌          |
| 9    | 2    | [0, 1, 2, 3]  | ❌          |
| 10   | 3    | [0, 1, 2, 3]  | ❌          |
