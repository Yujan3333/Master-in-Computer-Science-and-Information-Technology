### **P, NP, NP-Complete, and NP-Hard**

✅ With definitions, relations, and examples — perfect for **5 or 10 mark exam answers**.

---

## ✅ **Comparison Table**

|Class|Can be Solved in Poly Time?|Can be Verified in Poly Time?|Is in NP?|Is at least as hard as all NP problems?|Example|
|---|---|---|---|---|---|
|**P**|✅ Yes|✅ Yes|✅ Yes|❌ No|Merge Sort, Binary Search|
|**NP**|❓ Unknown (maybe not)|✅ Yes|✅ Yes|❌ No|Subset Sum, 3-SAT|
|**NP-Complete**|❓ Unknown|✅ Yes|✅ Yes|✅ Yes|3-SAT, Vertex Cover, Hamiltonian Cycle|
|**NP-Hard**|❌ Not necessarily|❌ Not necessarily|❌ Not necessarily|✅ Yes|TSP (optimization), Halting Problem|

---

## 📘 **Definitions with Examples**

### 1. **P (Polynomial Time)**

- Solvable in polynomial time.
    
- Both solving and verifying are efficient.  
    **Example**:
    
- Sorting, Matrix Multiplication
    

---

### 2. **NP (Nondeterministic Polynomial Time)**

- Solutions can be **verified in polynomial time**, but may be hard to solve.  
    **Example**:
    
- Subset Sum, Sudoku solution checking
    

---

### 3. **NP-Complete**

- A subset of NP.
    
- ✅ **In NP**, and
    
- ✅ **As hard as any problem in NP** (i.e., any NP problem can be reduced to it in polynomial time).
    
- If you solve any NP-Complete problem in poly time → you solve **all NP problems** in poly time → **P=NPP = NPP=NP**.  
    **Example**:
    
- 3-SAT, Hamiltonian Cycle, Vertex Cover
    

---

### 4. **NP-Hard**

- At least as hard as NP-Complete, **but not required to be in NP**.
    
- May be optimization problems or undecidable problems.
    
- May not even have verifiable solutions in polynomial time.  
    **Example**:
    
- TSP (optimization version), Halting Problem
    

---

## 🔄 **Relationship Diagram**

```md
         NP-Hard
        /       \
   NP-Complete   ← Not in NP
        |
        NP
        |
        P

```

- **P** ⊆ **NP**
    
- **NP-Complete** ⊆ **NP**
    
- **NP-Hard** ⊇ **NP-Complete**, but may include problems **not in NP**
    

---

## ✍️ Short Exam Answer Summary (Write-up Style)

> **P** problems are solvable and verifiable in polynomial time (e.g., Merge Sort).  
> **NP** problems are verifiable in polynomial time but not necessarily solvable efficiently (e.g., Subset Sum).  
> **NP-Complete** problems are both in NP and as hard as any NP problem. If one is solved in polynomial time, all NP problems can be solved (e.g., 3-SAT).  
> **NP-Hard** problems are at least as hard as NP-Complete, but may not be verifiable or even decidable (e.g., Halting Problem, TSP Optimization).x