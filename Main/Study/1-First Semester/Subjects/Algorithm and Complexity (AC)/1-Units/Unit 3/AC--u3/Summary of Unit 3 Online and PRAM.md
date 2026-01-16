## 🔷 **Unit 3: Online Algorithms (Introduction + Examples)**

---

## ✅ **3.1 Online Algorithms – Introduction**

- An **Online Algorithm** is an algorithm that makes decisions **step-by-step** as input arrives **without knowing the future**.
    
- It **does not wait** to see the whole input — it must make decisions **immediately**.
    
- It is evaluated using **Competitive Analysis**:
    
    - Compare the **online algorithm's performance** with an **optimal offline algorithm** (which knows the entire input in advance).
        

---

### ✅ **Ski Rental Problem**

**Problem:**

- You can **rent skis** for Rs. 1 per day or **buy** them once for Rs. _b_ (say, Rs. 10).
    
- You don't know **how many days you'll ski**.
    

**Strategy:**

- Rent skis for _b_ days.
    
- If you still need them after _b_ days, buy.
    

**Competitive Ratio:**

- Online cost = _2b_, Offline optimal = _b_ → Competitive Ratio = **2**
    

✅ **This is a classic example** of balancing cost **without knowing the future**.

---

### ✅ **Load Balancing Problem**

**Problem:**

- Assign tasks to **m machines** (or servers).
    
- Goal: Keep the **load (total work)** on all machines as balanced as possible.
    

**Online version:**

- Each task arrives one by one.
    
- You must assign it **without knowing future tasks**.
    

**Greedy Algorithm:**

- Assign task to the machine with **least load so far**.
    

✅ Works well in practice, but not always optimal.

---

### ✅ **Paging and Caching Problem**

Used in memory management (like how OS manages RAM and cache).

---

### 📌 **Key Concepts:**

- **Cache Size = k**
    
- Sequence of **page requests**
    
- If page is in cache → **Hit**
    
- If not → **Miss** → bring from memory, may need to **evict** a page
    

---

### ✅ **1. LIFO (Last-In First-Out)**

- When cache is full, evict the **most recently added** page.
    

🟥 Not very efficient — can cause many unnecessary misses.

---

### ✅ **2. LFD (Longest Forward Distance)** / Optimal Page Replacement

- Evict the page that **will not be used for the longest time in future**.
    

✅ This is the **optimal offline algorithm** — but not usable online because it needs to know the future.

---

### ✅ **3. LRU (Least Recently Used)**

- Evict the page that **has not been used for the longest time in the past**.
    

✅ Commonly used online algorithm — works well in practice.

---

### 🟩 **Summary for Exam:**

|Topic|Description|
|---|---|
|**Online Algorithms**|Make decisions **without knowing the future**|
|**Ski Rental**|Rent daily until cost reaches buy price, then buy|
|**Load Balancing**|Assign each task to least-loaded machine|
|**LIFO**|Remove most recently added page (inefficient)|
|**LFD**|Remove page used **farthest in future** (offline optimal)|
|**LRU**|Remove **least recently used** page (online + practical)|

---
## 🔷 **3.2 PRAM Algorithms**

---

### ✅ **PRAM: Introduction**

**PRAM = Parallel Random Access Machine**

- A **theoretical model** for designing **parallel algorithms**.
    
- Multiple **processors** working **in parallel** and **sharing a common memory**.
    
- Time is divided into **synchronous steps**.
    

---

### ✅ **PRAM Computational Model**

- **Each processor can:**
    
    1. **Read** from shared memory
        
    2. **Write** to shared memory
        
    3. **Perform computation**
        
- All processors run in **lock-step (synchronous)**.
    

---

### ✅ **Types of PRAM Models (Based on Memory Access):**

|Model|Description|
|---|---|
|**EREW**|Exclusive Read Exclusive Write – No simultaneous read or write to the same memory|
|**CREW**|Concurrent Read Exclusive Write – Many can read same memory, but only one can write|
|**ERCW**|Exclusive Read Concurrent Write – Rare model|
|**CRCW**|Concurrent Read Concurrent Write – All processors can read and write at the same time|

---

## ✅ **Fundamental Techniques & Algorithms**

### 🔹 **1. Prefix Computation**

> Given array A[1..n], compute prefix sums:

$P[i] = A[1] + A[2] + \dots + A[i]$ 


**Example**:  
Input: [3,1,4,2]  
Output: [3,4,8,10]

- Can be solved using **log n time** with **n processors** in PRAM.


### 🔹 **2. List Ranking**

- Given a **linked list**, assign **rank (position)** to each node.
    
- Hard to parallelize because list is sequential.
    
- PRAM uses **pointer jumping** to skip nodes and compute ranks in **O(log n)** time with **n processors**.
    

---

## ✅ **Selection Problems**

### 🔹 **1. Maximal Selection (with n² processors)**

- Try all pairs $A[i],A[j]$ compare in parallel.
    
- Mark those not maximum.
    
- Remaining unmarked element is the **maximum**.
    

**Time:** O(1) with **$n^2$ processors**

### **2. Finding Maximum (with n processors)**

- **Pairwise compare** and eliminate smaller one.
    
- Repeat for survivors → like a tournament tree.
    

**Time:** O(log n) with **n processors**

## ✅ **Merging Algorithms**

---

### 🔹 **1. Logarithmic Time Merge (using binary search):**

- For every element in array A, find its correct position in array B (and vice versa) using **binary search**.
    
- Merge in **O(log n)** time with **n processors**
    

---

### 🔹 **2. Odd-Even Merge**

- Divide and conquer strategy.
    
- Merge odd and even indexed elements recursively.
    
- Used in **parallel sorting**.
    

---

## ✅ **Sorting Algorithms**

---

### 🔹 **1. Odd-Even Merge Sort**

- Based on divide-and-conquer.
    
- Sort odd and even parts separately.
    
- Use **odd-even merging**.
    
- Runs in **O(log² n)** time using **n processors**
    

---

### 🔹 **2. Preparata’s Sorting Algorithm**

- Another parallel sort algorithm.
    
- Based on **merging and splitting** in parallel steps.
    
- More complex, but better optimized.
    

---

### 🟩 **Summary Table for Exam:**

|Topic|Time|Processors|Notes|
|---|---|---|---|
|Prefix Sum|O(log n)|n|Use binary tree computation|
|List Ranking|O(log n)|n|Pointer jumping|
|Max Selection (n²)|O(1)|n²|All-pairs comparison|
|Max Selection (n)|O(log n)|n|Tournament style|
|Merge|O(log n)|n|Binary search merge|
|Odd-Even Merge Sort|O(log² n)|n|Efficient parallel sort|
|Preparata's Sort|O(log² n)|n|Optimized merge sort|