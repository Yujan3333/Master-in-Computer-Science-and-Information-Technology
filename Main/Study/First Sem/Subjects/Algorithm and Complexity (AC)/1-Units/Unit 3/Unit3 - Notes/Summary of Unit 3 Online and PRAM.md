## 🔷 **Unit 3: Online Algorithms (Introduction + Examples)**

---

### ✅ **3.1 Online Algorithms – Introduction**

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

### ✅ **2. LFD (Longest Forward Distance)**

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
