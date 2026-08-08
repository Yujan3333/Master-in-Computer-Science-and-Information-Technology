#first-semester #advanced-operating-system
A **multilevel page table** is a memory management technique used to reduce the size of page tables when the virtual address space is large.

In a simple (single-level) page table, every process needs one big table that maps all virtual pages to physical frames. If the address space is large, this page table becomes very big and wastes memory.

To solve this problem, the page table is **divided into multiple smaller tables**. This is called **multilevel paging**.

---
### How it works

- The **virtual address** is divided into parts:
    
    1. **First part** selects the entry in the **first-level page table**.
        
    2. **Second part** selects the entry in a **second-level page table**.
        
    3. **Last part** gives the **offset** inside the actual memory page.
        
- This way, we only load the required parts of the page table into memory when needed.

### Further Explanation
#### How the translation works (step-by-step):

1. **PT1** is used to find the correct **second-level page table**.
    
    - This means **PT1 indexes into the top-level page table**, and each entry in this table points to a second-level page table (like a sub-folder).
        
2. **PT2** is then used to find the **exact frame number** in physical memory.
    
    - PT2 indexes into the **second-level page table**, and that entry contains the **physical frame number** (the start of the actual memory block).
        
3. The **Offset** is added to this physical frame to get the **exact physical address**.

---
![](../../../../../../../../Images/First_Sem_Images/Multi-Level%20Page%20Tables.png)