**numerical example of the 0/1 Knapsack problem** using **both Backtracking** and **Dynamic Programming** – **without coding**. I’ll show it step-by-step and in a way you can **write in your exam**.

---

## 🎒 Example:

|Item|Weight|Value|
|---|---|---|
|1|2 kg|Rs. 12|
|2|1 kg|Rs. 10|
|3|3 kg|Rs. 20|
|4|2 kg|Rs. 15|

Knapsack capacity: **5 kg**

---

## 🧠 A. Backtracking Solution (Step-by-step)

We try **all combinations** of items, but **stop early** if weight exceeds 5 kg.

---

### 🔄 Try all possibilities:

We make **decision tree** like this: for each item, **Include (Yes)** or **Exclude (No)**.

We keep track of:

- **Total weight**
    
- **Total value**
    

---

### Try Combinations (Total 2⁴ = 16 options)

|Items Taken|Total Weight|Total Value|Valid?|
|---|---|---|---|
|None|0|0|✅|
|1|2|12|✅|
|2|1|10|✅|
|3|3|20|✅|
|4|2|15|✅|
|1+2|3|22|✅|
|1+3|5|32|✅ ✅ Best|
|1+4|4|27|✅|
|2+3|4|30|✅|
|2+4|3|25|✅|
|3+4|5|35|✅ ✅ BEST|
|1+2+3|6|42|❌|
|1+2+4|5|37|✅ ✅ 2nd best|
|1+3+4|7|47|❌|
|2+3+4|6|45|❌|
|1+2+3+4|8|57|❌|

---

### ✅ Best valid option:

- **Items: 3 + 4** (weights 3 + 2 = 5)
    
- **Value: Rs. 35**
    

---

## 📋 Final Backtracking Answer:

> Using backtracking, we try all possible combinations of items and reject those that exceed the weight limit. The best valid combination is taking **Item 3 and Item 4**, giving total weight **5 kg** and total value **Rs. 35**.

---

## 💾 B. Dynamic Programming (Table Method)

We create a table:

- **Rows** = items (0 to 4)
    
- **Columns** = capacity (0 to 5)
    

We fill the table `dp[i][w]` = **max value using first `i` items and capacity `w`**

---

### Step-by-step Table Filling:

#### Initialization:

- `dp[0][w] = 0` for all `w` (0 capacity, no items = 0 value)
    

---

### Fill DP table:

#### Row 1: Item 1 (weight 2, value 12)

|Capacity (w)|0|1|2|3|4|5|
|---|---|---|---|---|---|---|
|Value|0|0|12|12|12|12|

---

#### Row 2: Item 2 (weight 1, value 10)

|Capacity (w)|0|1|2|3|4|5|
|---|---|---|---|---|---|---|
|Value|0|10|12|22|22|22|

Explanation:

- For w = 1 → we can take item 2 only → value = 10
    
- For w = 3 → we can take item 1 + item 2 → value = 12 + 10 = 22
    

---

#### Row 3: Item 3 (weight 3, value 20)

|Capacity (w)|0|1|2|3|4|5|
|---|---|---|---|---|---|---|
|Value|0|10|12|22|22|30|

Explanation:

- For w = 5 → best is item 2 + item 3 = 10 + 20 = 30
    

---

#### Row 4: Item 4 (weight 2, value 15)

|Capacity (w)|0|1|2|3|4|5|
|---|---|---|---|---|---|---|
|Value|0|10|15|25|27|35|

---

## ✅ Final Dynamic Programming Answer:

- **Maximum value** = Rs. **35** at capacity = 5
    
- Achieved by selecting **Item 3 and Item 4**
    

---

## 📌 Final Summary

### 1. **Backtracking**:

> In backtracking, we try all combinations of items. We reject those where the total weight exceeds the knapsack capacity. For this problem, the best selection is **Item 3 and 4** (total weight 5 kg, total value Rs. 35).

### 2. **Dynamic Programming**:

> We build a table of values for smaller subproblems (items and capacities). Each cell represents the best value achievable with that item and capacity. The final answer is in the bottom-right cell. The best value is **Rs. 35**, achieved by selecting **Item 3 and 4**.