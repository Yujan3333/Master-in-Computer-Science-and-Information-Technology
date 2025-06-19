### ✅ **Pros of Increasing Page Size**

|**Pro**|**Explanation**|
|---|---|
|**1. Reduces page table size**|Fewer pages needed → fewer entries in page table → less memory overhead|
|**2. Increases TLB coverage**|Each TLB entry maps a larger chunk of memory → fewer TLB misses|
|**3. Improves I/O throughput**|Larger pages = fewer I/O operations during swapping or page-in/page-out|
|**4. Reduces page table lookup time**|Smaller page tables → faster access and less memory bandwidth usage|

---

### ❌ **Cons of Increasing Page Size**

|**Con**|**Explanation**|
|---|---|
|**1. Increases internal fragmentation**|More unused space within each page → wasted memory|
|**2. Increases page fault latency**|Larger pages take longer to load from disk during page faults|
|**3. Less flexibility in memory allocation**|Bigger blocks of memory harder to fit into free space → may cause inefficiency|
|**4. Wastes memory if only small part is used**|Small programs or data structures still get full-size pages|

---

### 📌 Summary Sentence for Exams:

> Increasing page size improves performance by reducing page table size, increasing TLB efficiency, and boosting I/O, but it also leads to more internal fragmentation and slower page fault handling.