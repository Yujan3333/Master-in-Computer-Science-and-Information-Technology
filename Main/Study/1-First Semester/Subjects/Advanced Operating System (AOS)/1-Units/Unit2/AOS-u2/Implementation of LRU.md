#first-semester #advanced-operating-system
### 🕒 1. Counter Implementation

> Uses a **timestamp or clock** to track **when** each page was last used.

#### 📌 How it works:

- Every page table entry has an **associated counter**.
    
- On **every memory reference**, the **current clock time** is stored in the page’s counter.
    
- When a page needs to be replaced:
    
    - The system selects the page with the **smallest counter value** (i.e., **least recently used**).
        

#### ✅ Advantages:
- Conceptually simple
    
- Reflects **exact usage time**
    

#### ❌ Disadvantages:
- Requires a **global clock**
    
- **Updates the counter on every memory access**, which is costly
    

---

### 📚 2. Stack Implementation (Linked List Version)

> Uses a **stack (doubly linked list)** to maintain **recency order** of page accesses.

#### 📌 How it works:

- **Each time a page is referenced**, it is **moved to the top** of the stack.
    
- The **least recently used** page is at the **bottom**.
    
- When a page must be replaced, **remove from bottom**.
    

#### ⚙️ Internal Details:

- Implemented with a **doubly linked list**
    
- **6 pointers** are changed on each page reference (removal + re-insertion)
    

#### ✅ Advantages:

- No need to **search** during replacement – bottom is always LRU
    
- Always maintains **correct order**
    

#### ❌ Disadvantages:

- **High overhead** for maintaining the stack
    
- Costly in terms of **pointer manipulation** (especially in hardware)
    

---

## ✅ Summary Table

|**Feature**|**Counter Implementation**|**Stack Implementation**|
|---|---|---|
|Tracks time|Yes (via clock)|No|
|Recency maintained|Using counters|Using stack order|
|Update cost|High (each memory reference)|High (re-linking nodes)|
|Replacement complexity|Low (find smallest counter)|Low (remove bottom of stack)|
|Hardware friendliness|Poor (requires precise time tracking)|Poor (requires many pointer updates)|

---

### 🧠 Memory Tip for Exams:

> **"Counters tell when, stacks tell order."**  
> Use this to recall:

- Counter = **timestamps**
    
- Stack = **most recently used at top**