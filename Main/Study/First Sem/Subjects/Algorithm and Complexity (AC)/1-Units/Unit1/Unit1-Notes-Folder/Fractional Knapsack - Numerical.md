Absolutely, Yujan! Let’s now talk about the **Fractional Knapsack Problem** and compare it with the **0/1 Knapsack**, focusing on:

- What it is
    
- How it's solved
    
- What algorithm is used
    
- Its time complexity
    

---

## 🥧 **Fractional Knapsack Problem** – Explained Simply

---

### 📌 **What is it?**

You are given:

- `n` items, each with:
    
    - **Weight** $w_i$
        
    - **Value** $v_i$
        
- A **knapsack with capacity W**
    

But this time, **you can take fractions of items**, not just the whole thing.

---

### 🎯 **Goal**

Maximize total **value** in the knapsack without exceeding the weight limit.

---

### 🧠 **Key Difference from 0/1 Knapsack**

|Feature|0/1 Knapsack|Fractional Knapsack|
|---|---|---|
|Items|Either **take whole** or **not**|Can **take part** (e.g., half an item)|
|Method used|Dynamic Programming / Backtracking|**Greedy algorithm**|
|Time Complexity|O(nW)O(nW) or O(2n)O(2^n)|O(nlog⁡n)O(n \log n)|
|Optimal Greedy Solution?|❌ No (needs DP)|✅ Yes, greedy gives optimal|

---

## ✅ **How to Solve Fractional Knapsack** (Greedy)

---

### ⚖️ Step-by-Step:

1. **Calculate value-to-weight ratio** for each item:
    
    $\text{ratio}_i = \frac{w_i}{v_i}$
    
2. **Sort items** in **descending order** of this ratio.
    
3. Take as much as possible from the item with the **highest ratio**, then move to the next one.
    
4. If the item can't be taken fully, take the **fraction** that fits.
    

---

### 🧮 Example

|Item|Weight (kg)|Value (Rs.)|Ratio (value/weight)|
|---|---|---|---|
|1|10|60|6.0|
|2|20|100|5.0|
|3|30|120|4.0|

Knapsack Capacity: **50 kg**

---

### 🪜 Steps:

- Take all of Item 1 → 10 kg, Rs. 60
    
- Take all of Item 2 → 20 kg, Rs. 100
    
- Left space = 20 kg
    
- Take **20/30 = 2/3** of Item 3 → Rs. $\frac{2}{3} \times 120$ = 80
    

---

### ✅ Total value = Rs. 60 + 100 + 80 = **Rs. 240**

---

### ⏱️ **Time Complexity**

- Sort items by ratio → O(nlog⁡n)
    
- Loop through items →$O(n)$
    

→ Total: $\boxed{O(n \log n)}$

---

## 📓 **How to Write in Exam**

> The **Fractional Knapsack Problem** allows taking **fractions of items** to fill the knapsack. We aim to **maximize total value** without exceeding the weight capacity. It is solved using a **Greedy Algorithm**, where items are sorted by their value-to-weight ratio and added in that order. The item with the **highest ratio is picked first** until the bag is full. Its time complexity is **$O(n \log n)$, and unlike the 0/1 Knapsack, **greedy gives the optimal solution**.

---