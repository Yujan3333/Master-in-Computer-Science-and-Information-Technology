## 🔷 What is **LIFO (Last-In First-Out)**?

### 📌 Basic Idea:

- **LIFO** means:  
    The **most recently loaded page** (last in) is the **first one to be removed** (first out).
    

It’s like a **stack of books** — you remove the one you just placed on top.

---

## 🧠 In Paging (Page Replacement):

When a **new page needs to be loaded** and **there’s no free space**, the **most recently loaded page** is **removed first**, even if it's likely to be used again soon.

---

### 🔹 Simple Example:

Let’s say:

- Memory has **2 page frames**
    
- Page reference string is: `1, 2, 3, 1`
    

Apply **LIFO**:

|Step|Memory Contents|Page Fault?|Action|
|---|---|---|---|
|1. 1|1|Yes|Load 1|
|2. 2|1, 2|Yes|Load 2|
|3. 3|1, **3**|Yes|Remove last loaded (2), load 3|
|4. 1|1, 3|No|1 is already in memory|

→ **Total Page Faults** = 3

---

## 📉 Why LIFO is Rarely Used in Real Life?

Because it's **not intelligent** — it removes the **most recent page**, which is often the one you **just brought in for a reason**.

So:

- LIFO can cause **more page faults** than other strategies
    
- It’s mostly used as a **theoretical comparison** in online paging problems
    

---

## 🟩 Summary for Exam:

> ✅ **LIFO (Last-In First-Out)** is a **page replacement algorithm** that removes the **most recently loaded page** first.  
> 
> ✅ It is **simple but not efficient**, and not used in real systems.  
> 
> ✅ Included in syllabus to compare with other online strategies like **LRU**.  
> 
> ❌ Not optimal and often causes **more page faults**.