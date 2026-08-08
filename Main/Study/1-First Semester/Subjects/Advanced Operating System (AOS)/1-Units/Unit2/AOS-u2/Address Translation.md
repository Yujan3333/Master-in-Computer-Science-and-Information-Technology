#first-semester #advanced-operating-system
**Address Translation** using **base and limit registers**, 
which is a **simple memory protection and relocation mechanism**
in operating systems.

### 🔍Figure
![](../../../../../../../../Images/First_Sem_Images/Address%20Translation.png)
### 🔁 **What’s Happening? (Step-by-step)**

1. **The CPU generates a logical address** (e.g., `300`).
    
    - This is the address used inside the program.
        
    - It doesn't know where its code/data actually sits in RAM.
        
2. **The limit register checks if the address is valid:**
    
    - It stores the maximum allowed size (e.g., `Limit = 1000`).
        
    - If the logical address is **less than limit**, it is **safe**.
        
    - If **not**, a **trap or error** is raised: ❌ _addressing error_.
        
3. **The relocation (base) register** adds the base to the logical address:
    
    - Suppose `Base = 1500`.
        
    - Then **physical address = base + logical = 1500 + 300 = 1800**
        
4. **The final physical address (1800)** is used to access memory.
    

---

### 💡 Example Recap from Slide:

- **Logical address = 300**
    
- **Base = 1500**
    
- ✅ It is valid (within limit)
    
- 🧮 **Physical address = 1500 + 300 = 1800**
    

---

### 🔐 Protection Benefit:

- A process **cannot access memory outside its assigned range**.
    
- Prevents **one program from crashing or modifying another's memory**.