### ✅ What is **Data Concentration**?

> **Data concentration** means **collecting data** from many processors in a mesh network and **sending it to a single destination processor**, usually the top-left corner **(0,0)** or any fixed node.

It's the opposite of **broadcasting** — instead of **one-to-all**, it’s **many-to-one**.

---

### 🔹 **Why is Data Concentration Needed?**

- In many parallel algorithms, each processor performs local computation.
    
- At the end, we often need to **gather the final results in one place** for:
    
    - Output
        
    - Further computation
        
    - Decision making (e.g., min, max, sum)
        

---

## 🖧 **Example Setup: √p × √p Mesh**

Let’s assume a **4×4 mesh** (p = 16 processors):

```md
(0,0)  (0,1)  (0,2)  (0,3)  
(1,0)  (1,1)  (1,2)  (1,3)  
(2,0)  (2,1)  (2,2)  (2,3)  
(3,0)  (3,1)  (3,2)  (3,3)

```

Each processor holds **one value**. We want to **concentrate** all values to processor **(0,0)**.

---

## 🔁 **Two-Phase Data Concentration Algorithm**

### **🔹 Phase 1: Row-wise Gathering**

- In each row, all values are sent **leftward** to the **first column**.
    
- After this step, all values are stored in processors of **column 0**
    

So:

- (1,1), (1,2), (1,3) → send to (1,0)
    
- (2,1), (2,2), (2,3) → send to (2,0)
    
- (3,1), (3,2), (3,3) → send to (3,0)
    

Result: All data from each row is now at the first column (0th column)

---

### **🔹 Phase 2: Column-wise Gathering**

- Now all processors in column 0 **send their data upward** toward (0,0)
    
- (1,0) → (0,0), (2,0) → (1,0) → (0,0), etc.
    

After this step, **(0,0)** has all the values concentrated from all 16 processors.

---

### ✅ Total Time:

Each phase (row and column movement) takes **O(√p)** steps

> So, total time = **O(√p)**

---

## 🟩 Summary for Exams:

> **Data Concentration** is the process of **collecting data from all processors** in a mesh to a **single node** (usually (0,0)).  
> It is done in **two phases**:
> 
> 1. **Row-wise**: Move all data to the **first column**
>     
> 2. **Column-wise**: Move all data **upward** to the **top-left node**
>     
> 
> 🔸 Time complexity: **O(√p)**  
> 🔸 Used in: **final result collection**, min/max/sum aggregation, etc.