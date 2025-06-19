- Not used in Practical system because know way of knowing all the page reference of future.
- But guarantees the lowest possible page fault rate.


![](../../../../../../../../Attachments/Optimal%20(OPR)%20%20Principle%20of%20Optimality-que.png)

### 📌 **Numerical Example**

Let’s say:

- We have **3 page frames** (can hold 3 pages in memory).
    
- The **reference string** (sequence of page requests) is:  
    `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`
    

---

#### 🧠 Step-by-step: Optimal Page Replacement

Let’s do the first few steps and show the logic using the “future instruction” count idea.

---

#### 🧮 Start with empty memory:

- Memory = `[]`
    
- Reference: `7` → page fault → Load page 7
    
- Memory = `[7]`
    

---

- Reference: `0` → page fault → Load page 0
    
- Memory = `[7, 0]`
    

---

- Reference: `1` → page fault → Load page 1
    
- Memory = `[7, 0, 1]` (memory full now)
    

---

- Reference: `2` → page fault  
    → Need to **replace** one page.
    

Now we apply **Optimal Replacement**:

- Look ahead to see **when 7, 0, and 1** will be used next:
    

|Page|Next Use (distance ahead in ref string)|
|---|---|
|7|❌ **Never used again**|
|0|In 1 step (next: 0)|
|1|❌ **Never used again**|

👉 Both 7 and 1 will **never be used again**, so either can be replaced.  
Let’s say we replace **page 7**.

- Load page 2
    
- Memory = `[2, 0, 1]`
- 