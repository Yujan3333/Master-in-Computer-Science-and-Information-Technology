
### 📘 **Page Fault Handling – Step-by-Step**

#### 🧩 When a process references a page not in memory:

---

### 🔹 Step 1: Page Fault Occurs

- The **CPU cannot find the page in memory** → a **page fault trap** is generated.
    
- **Control is transferred to the Operating System (OS)**.
    
- The **process is suspended** while the OS handles the page fault.
    

---

### 🔹 Step 2: Address Validation

- The OS checks whether the **referenced virtual address is valid**:
    
    - If the **address is invalid** (e.g., program bug), → **terminate the process**.
        
    - If the **address is valid**, continue with page loading.
        

---

### 🔹 Step 3: Bring Page into Memory

- OS **locates a free frame** in physical memory:
    
    - If no free frame → use a **replacement algorithm** (like LRU or FIFO).
        
- Map the **virtual address to the corresponding disk block**.
    
- **Read the page from disk** into the chosen frame.
    
- **Update page table** to show the page is now in memory.
    

---

### 🔹 Step 4: Restart the Process

- The **interrupted instruction** is restarted.
    
- The process continues **as if the page was always in memory**.
    
- The page fault is **completely transparent to the process**.
    

---

### ✅ Summary Line for Exam:

> On page fault, the OS validates the address, fetches the page from disk to memory, updates mappings, and resumes the process seamlessly.

