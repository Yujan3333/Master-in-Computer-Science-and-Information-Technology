
### 🧠 Problem 1: **Huge Page Table Size**

- For a **32-bit system**:
    
    - Virtual address space = $2^{32} \text{ bytes} = 4 \text{ GB}$
        
    - Page size = $4 \text{ KB} = 2^{12}$ Bytes
        
    - Number of pages = $\frac{2^{32}}{2^{12}} = 2^{20} = 1 \text{ million pages}$
        

✅ So: 1 million page table entries per process!

---

#### ⚠️ What about a **64-bit system**?

- Virtual address space $= 2^{64}$ bytes (theoretical)
    
- Page size $= 4 \text{ KB} = 2^{12}$ Bytes
    
- Pages = $= \frac{2^{64}}{2^{12}} = 2^{52}$ pages
    ✅ That’s **over 4.5 _quadrillion_ entries**! (impossible to store directly)
    

---

### 🧠 Problem 2: **Mapping Efficiency**

- Page table lookup must be **very fast**.
    
- If each memory access requires **page table lookup**, and it’s slow → the **CPU becomes idle** waiting.
    

So we ask: **How to handle both size and speed?**

---

### ✅ Solutions to Handle Large Page Tables

#### 1. [Multi-Level Page Tables](Multi-Level%20Page%20Tables.md)

- Page table is split into **levels** (e.g., 2-level, 3-level, 4-level)
    
- Only the needed parts of the table are **loaded into memory**
    
- Greatly reduces memory use
    

> Like a folder inside a folder: You only open what you need.

---

#### 2. [Inverted Page Tables](Inverted%20Page%20Tables.md)

- One page table for the **whole system** (not per process)
    
- Entries are indexed by **physical frames**, not virtual pages
    
- Fewer entries, but needs **hashing/search** to map
    

---

#### 3. [TLB (Translation Lookaside Buffer](TLB%20(Translation%20Lookaside%20Buffer.md)

- **Small hardware cache** inside MMU
    
- Caches **recent virtual → physical** translations
    
- Fast lookup: avoids walking the page table every time
    

> Most translations come from TLB, not the full table.

---

### 📌 Summary:

|Challenge|Solution|
|---|---|
|Huge page tables|Multi-level page tables, Inverted page tables|
|Slow access|TLB (Translation Lookaside Buffer)|
|Memory waste|Only load parts of page table as needed|
