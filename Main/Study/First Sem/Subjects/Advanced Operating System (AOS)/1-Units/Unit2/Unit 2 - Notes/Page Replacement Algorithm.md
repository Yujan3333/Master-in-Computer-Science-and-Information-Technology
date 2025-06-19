## 📘 What is a Page Replacement Algorithm?
   
   > A **page replacement algorithm** is used by the operating system to **decide which memory page to remove** when a *page fault* occurs and **no free frame is available**.
   
   - It helps in managing **virtual memory** efficiently.
       
   - The goal is to **minimize page faults** and **maximize performance**.**

---
## 🔄 Common Page Replacement Algorithms

### 1️⃣ [Optimal (OPR) – Principle of Optimality](Optimal%20(OPR)%20–%20Principle%20of%20Optimality.md)

- Replace the page that will **not be used for the longest time** in the future.
    
- **Theoretical best**, but **not possible** in practice (requires future knowledge).
    
- Used for **benchmarking** other algorithms.
    

> 📌 _"Replace the page that will be used farthest in the future."_

---

### 2️⃣ Random Page Replacement

- Select a page **randomly** for replacement.
    
- Very simple, but **unpredictable**.
    
- May evict useful pages.
    

> 📌 _"Choose a page at random."_

---

### 3️⃣ [FIFO (First-In, First-Out)](FIFO%20(First-In,%20First-Out).md)

- Replace the page that has been in memory **the longest**.
    
- Easy to implement using a **queue**.
    
- **Doesn't consider how often or recently a page was used** → can perform poorly.
    

> 📌 _"Replace the oldest loaded page."_

---

### 4️⃣ [LRU (Least Recently Used)](LRU%20(Least%20Recently%20Used).md)

- Replace the page that was **least recently used**.
    
- Based on the idea that **recently used pages are likely to be used again**.
    
- More accurate but **requires tracking usage history**, which can be costly.
    

> 📌 _"Replace the page that hasn't been used for the longest time."_

---

### 5️⃣ LFU (Least Frequently Used)

- Replace the page with the **lowest access frequency**.
    
- Tracks how often each page is used.
    
- May keep old pages that were frequently used **long ago**.
    

> 📌 _"Replace the page used the least number of times."_

---

### 6️⃣ NUR (Not Used Recently)

- An **approximation of LRU**, using **reference and modify bits** set by hardware.
    
- Pages are classified into **classes** based on recent use.
    
- Lower overhead than exact LRU.
    

> 📌 _"Approximate LRU using reference bits."_

---

### 7️⃣ Working Set Model

- Keeps in memory the **set of pages** a process is **actively using** (its "working set").
    
- Pages outside the working set are candidates for replacement.
    
- Based on **locality of reference**.
    

> 📌 _"Keep pages that are actively being used by the process."_

---

## ✅ Summary Table

|Algorithm|Key Idea|Pros|Cons|
|---|---|---|---|
|**Optimal**|Replace page not used for longest time|Best performance|Not practical (needs future info)|
|**Random**|Replace a random page|Simple|Unpredictable|
|**FIFO**|Replace oldest loaded page|Simple|May evict useful pages|
|**LRU**|Replace least recently used page|Good performance|Hard to implement|
|**LFU**|Replace least frequently used page|Tracks usage|Can keep old pages|
|**NUR**|Approximation of LRU using reference bits|Efficient approximation|Less accurate than true LRU|
|**Working Set**|Keep active pages only|Low page faults|Needs tracking window|