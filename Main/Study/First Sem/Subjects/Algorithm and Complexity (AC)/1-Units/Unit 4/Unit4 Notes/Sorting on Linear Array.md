## 🔹 1. **Sorting on a Linear Array**

### 📌 Model:

- Processors are arranged **in a single line** (1D).
    
- Each processor holds one key (number to sort).
    
- Communication only with **left and right neighbors**.
    

---

### ✅ Algorithm: **Odd-Even Transposition Sort**

This is a parallel version of bubble sort.

**Steps:**

- Repeat **n** times (for n processors)
    
- Alternate between:
    
    - **Odd step**: Compare (P₁, P₂), (P₃, P₄), ...
        
    - **Even step**: Compare (P₂, P₃), (P₄, P₅), ...
        

Each pair:

- Swaps values **if they’re out of order**
    

---

### 🔁 Example:

Suppose values are: `5, 3, 1, 4`

|Step|Comparison Pairs|Result|
|---|---|---|
|1 (Odd)|(P1,P2), (P3,P4)|→ 3,5,1,4|
|2 (Even)|(P2,P3)|→ 3,1,5,4|
|3 (Odd)|(P1,P2), (P3,P4)|→ 1,3,4,5|
|...|Repeats until sorted|Final: 1,3,4,5|

---

### 🕒 Time Complexity:

- **O(n)** for **n processors**