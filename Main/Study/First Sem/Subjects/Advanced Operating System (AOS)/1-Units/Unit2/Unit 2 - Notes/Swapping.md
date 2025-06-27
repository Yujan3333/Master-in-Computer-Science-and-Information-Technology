### 🔁 **Swapping (Concept):**

- A **process** can be **temporarily moved out** of main memory to a **disk (backing store)** to **make space for other processes**.
    
- Later, it is **brought back in** to continue running.
    

---

### 💽 **Backing Store:**

- A **fast disk** (like an SSD or a dedicated swap partition).
    
- It should be **big enough** to hold **all memory images** of all processes.
    
- Must allow **direct access** (not sequential like tape).
    

---

### 🔄 **Roll Out, Roll In:**

- A special type of swapping used with **priority-based scheduling**.
    
- A **low-priority** process is **rolled out** (swapped out).
    
- A **high-priority** process is **rolled in** (loaded in memory to run).
    

---

### 🕒 **Swap Time:**

- The biggest time factor is **transfer time** (moving data to/from disk).
    
- More memory = more time to swap.
    

---

### 🖥️ **Where It’s Used:**

- Modified versions of swapping exist in:
    
    - **UNIX/Linux** (e.g., using `swap` space or `zram`)
        
    - **Windows** (using pagefile)
        

---
### Schematic View of Swapping
![](../../../../../../../../Images/First_Sem_Images/Swapping%20-%20schematic%20view.png)