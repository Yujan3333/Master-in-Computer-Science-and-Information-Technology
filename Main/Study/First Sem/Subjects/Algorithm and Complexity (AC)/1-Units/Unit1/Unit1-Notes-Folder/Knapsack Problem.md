Imagine you are a thief breaking into a shop with a **knapsack (bag)** that can only hold a certain **maximum weight**.

There are **many items** in the shop.  
Each item has:

- A **weight** (how heavy it is)
    
- A **value** (how useful or expensive it is)
    

But… you **can’t take everything** because your bag has a **weight limit**.  
So you must choose **some items** in such a way that:

- The total **weight** of selected items is **less than or equal** to the capacity of the bag
    
- The total **value** of selected items is **as high as possible**
    

This is the **Knapsack Problem**.

---

### ❗**Why is it called "0/1"?**

Because:

- For each item, you can either **take it (1)** or **leave it (0)**.
    
- You **cannot take half** an item or break it.
    

---

### 🧠 **Main Idea**

You have to **decide which items to take** to:

- **Maximize value**
    
- **Not exceed the weight limit**
    

You can try **all combinations of items**, but that takes a long time if there are many items.  
That’s why we use **smart methods** like:

- **Backtracking** – Try all combinations but skip (prune) impossible ones early.
    
- **Dynamic Programming** – Use a table to remember the best value for smaller problems and build the solution step-by-step.



---
### [Numerical](Numerical.md)