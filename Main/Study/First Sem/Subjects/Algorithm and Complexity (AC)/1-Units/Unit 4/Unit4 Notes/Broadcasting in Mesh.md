## 📘 **Broadcasting in Mesh (√p × √p Processors)**

### ✅ **What is Broadcasting?**

> Broadcasting is the process of **sending a copy of a message** from one processor to **all other processors** in a network.

It is a **basic communication operation** used in many parallel algorithms.

---

## 🧩 **Why Broadcasting is Important?**

- Needed when one processor has important data (e.g., input, pivot value, global constant).
    
- Used in: **prefix sums, parallel sorting, matrix operations**, etc.
    

---

## 🖧 **Mesh Network Setup**

- You have a **2D mesh** with √p × √p processors. (For example, 16 processors → 4×4 mesh)
    
- Each processor is labeled by a coordinate (i, j) → row _i_, column _j_
    

---

## 🔄 **Broadcasting Algorithm (2 Phases)**

Let’s say a processor at position (i, j) wants to broadcast a message **M** to all others:

---

### **🔹 Phase 1: Row-wise Broadcast**

- From processor (i, j), message **M is sent to all processors in row _i_**
    
- This is done by **moving right and left** along the row.
    

> ⏱ **Takes at most (√p - 1) steps** (since there are √p processors in a row)

---

### **🔹 Phase 2: Column-wise Broadcast**

- Now that every processor in row _i_ has the message,
    
- Each of them sends message **down and up** to processors in their own column.
    

> ⏱ Again, takes **at most (√p - 1) steps** in each column.

---

### ✅ **Total Time Steps:**

- Row broadcast: ≤ √p − 1
    
- Column broadcast: ≤ √p − 1
    
- **Total = 2(√p − 1)**
    

⏱ So, **Broadcasting takes O(√p) time** on a √p × √p mesh

---

## 🔁 **Example** (for 4×4 mesh):

Let’s say processor at (0, 0) has message M

1. **Phase 1**: Send M to (0,1), (0,2), (0,3)
    
2. **Phase 2**: Each processor in row 0 sends M **down** their column:
    
    - (0,0) sends to (1,0), (2,0), (3,0)
        
    - (0,1) sends to (1,1), (2,1), (3,1)
        
    - And so on...
        

➡ Now **every processor has the message M**

---

## 🟩 Summary for Exam:

> In a √p × √p mesh:
> 
> - Broadcasting from processor (i, j) is done in **2 phases**
>     
>     - **Row-wise** first
>         
>     - **Then column-wise**
>         
> - Total time = **2(√p − 1)** steps
>     
> - Time complexity: **O(√p)**
>