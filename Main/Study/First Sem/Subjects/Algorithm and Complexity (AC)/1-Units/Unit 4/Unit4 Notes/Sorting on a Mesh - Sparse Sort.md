## ✅ What is **Sparse Enumeration Sort**?

> A sorting method used **when number of keys is much less than the total processors** in the mesh.

- Say you have a **4×4 mesh** (16 processors), but only **4 keys to sort**.
    
- Goal: Sort those keys using the mesh in **parallel**.
    
- Result: Sorted keys should appear in the **first row** in sorted order.
    

---

## 📊 Example:

Input keys:  
**k₁ = 8**, **k₂ = 5**, **k₃ = 3**, **k₄ = 7**  
(Placed in first row: positions (1,1), (1,2), (1,3), (1,4))

We want:  
First row becomes → **3, 5, 7, 8**

---

## 🔄 Algorithm Steps:

### **Step i: Broadcast Each Key Down its Column**

- Each key (in row 1) is broadcast **down its own column**.
    
- So:
    
    - Column 1: All processors see key 8
        
    - Column 2: All processors see key 5
        
    - Column 3: All processors see key 3
        
    - Column 4: All processors see key 7  
        → (This allows all processors to **compare keys in parallel**)
        

📌 Done in **√p = 4 steps**

---

### **Step ii: Broadcast Along Rows**

- Each processor broadcasts its key **across the row**
    
- Now, each processor has all 4 keys — and can compare!
    

---

### **Step iii: Compute Rank (Prefix Computation)**

Each key compares itself with all others to **find its rank** (number of smaller keys):

- k₁ = 8 → 3 keys are smaller → rank = 4
    
- k₂ = 5 → 1 key smaller (3) → rank = 2
    
- k₃ = 3 → 0 smaller → rank = 1
    
- k₄ = 7 → 2 keys smaller (3, 5) → rank = 3
    

Now each key knows its **rank r**, i.e. its final position in sorted order.

---

### **Step iv: Send Rank to First Row**

- Each key sends its rank to processor in the first row
    
- i.e., key with rank = 1 goes to (1,1), rank = 2 to (1,2), etc.
    

---

### **Step v: Route Key to (1, r)**

- The key is moved (routed) to position (1, r)
    
- Final positions in Row 1:
    
    - (1,1) = 3
        
    - (1,2) = 5
        
    - (1,3) = 7
        
    - (1,4) = 8 ✅
        

---

## 🟩 Summary for Exam:

> **Sparse Enumeration Sort** is used when **number of keys ≪ mesh size**.  
> It uses a **2D mesh** to sort by broadcasting, computing **rank**, and **routing keys** to their final position.

### 📌 Time Complexity:

- Each step takes **O(√p)** time
    
- Total: **O(√p)** time for sorting p keys on a √p × √p mesh
    

---

### ✅ Final Sorted Output (Row 1):

`3, 5, 7, 8`