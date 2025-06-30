
## ✅ **Terminology Recap**

* `f` = schedule function
* `v` = task
* `i` = processor Pi
* `start_time(v, i, f)` = earliest time task `v` can start on processor `i`
* `task(i, t, f)` = task assigned to processor `i` at time `t` in schedule `f`

---

## ✅ **Algorithm Overview (With Communication Considered)**

### 📌 Step 1: Priority Assignment

* Assign **priority = number of successors** (more successors = higher priority)

### 📌 Step 2: Scheduling in Priority Order

* Schedule **highest-priority unscheduled task** first

### 📌 Step 3: Find Best Processor

* For each processor `Pi`, compute when task `v` can start:

  * **If all predecessors of `v` are on the same processor → no delay**
  * **If at least one predecessor is on a different processor → +1 time unit delay**

### 📌 Step 4: Resolve Tie

* If multiple processors have **equal earliest start time**, choose the processor where the **last task has lowest priority**

---

## ✅ Example in Interval Form (1 communication unit delay)

Let’s say:

* Task `v` depends on `u`
* `u` is scheduled on `P1` at time `2`
* `v` is being considered for scheduling

### ➤ If `v` is also on **P1**:

* Then `v` can start at **time 3**

### ➤ If `v` is on **P2** (different processor):

* Then `v` must wait **1 extra unit** for communication
* So `v` starts at **time 4**

---

## ✅ Key Idea

This algorithm makes decisions **dynamically**, based on:

* **Current schedule**
* **Processor availability**
* **Communication cost (1 unit)**

---
