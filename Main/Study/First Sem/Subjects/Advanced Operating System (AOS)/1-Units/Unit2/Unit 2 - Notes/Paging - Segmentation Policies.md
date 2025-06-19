## 🔄 **1. Fetch Strategies**

**When should a page or segment be loaded into main memory from disk?**

### 📌 a) **Demand Fetch (Demand Paging)**

- A page/segment is **only loaded when it is actually needed** (i.e., accessed).
    
- **Advantage**: Saves memory and I/O if not all parts are needed.
    
- **Disadvantage**: First access causes a **page fault**, leading to delay.
    

### 📌 b) **Anticipatory Fetch (Pre-paging)**

- Pages or segments are **loaded in advance**, based on **prediction or patterns**.
    
- Example: loading the **next few pages** during program execution.
    
- **Advantage**: Can **reduce page faults** and improve performance.
    
- **Disadvantage**: Risk of **loading unnecessary pages**, wasting memory and I/O.
    

---

## 📍 **2. Placement Strategies**

**Where should a new page or segment be placed in memory?**

### 📌 a) **Paging – Trivial**

- Since **pages and frames are fixed in size**, any page can be placed in **any free frame**.
    
- No complex decision-making is needed.
    

### 📌 b) **Segmentation – Complex**

- Segments are **variable-sized**, so the system must find a **contiguous memory block** large enough.
    
- May use **first-fit**, **best-fit**, or **worst-fit** strategies.
    
- Can cause **external fragmentation** and complex allocation logic.
    

---

## 🔁 **3. Replacement Strategies**

**If memory is full, which page or segment should be removed to make space?**

Common **replacement algorithms** include:

|**Strategy**|**Idea**|
|---|---|
|**FIFO** (First-In, First-Out)|Replace the oldest loaded page/segment|
|**LRU** (Least Recently Used)|Replace the page/segment **not used recently**|
|**Optimal**|Replace the page that **won’t be used for the longest time** (used for comparison only)|
|**Clock** (Second-Chance)|Like FIFO but gives pages a "second chance" if recently used|

---

### ✅ Summary for Exam:

> **Fetch strategies** decide _when_ to bring data into memory (on-demand or in advance),  
> **placement strategies** decide _where_ to place it (easy for paging, complex for segmentation),  
> and **replacement strategies** decide _which_ existing page or segment to remove when memory is full.