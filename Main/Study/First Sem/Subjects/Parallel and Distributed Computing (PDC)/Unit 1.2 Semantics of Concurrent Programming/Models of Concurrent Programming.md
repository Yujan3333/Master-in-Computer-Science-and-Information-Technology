
### 1. 🧱 "Level of Granularity"

This means: **At what scale** are we observing the system? Like zooming in and out.

Suppose two **bank tellers (agents)** are accessing the same **centralized database** at the same time to deposit `Rs.100`.

We observe this at different levels:

---

#### 1. 🔁 **Transaction Level**

- You look at it as **two complete transactions**:
    
    - Teller 1: Reads balance, adds Rs.100, writes new balance.
        
    - Teller 2: Same steps, possibly overlapping.
        

✅ At this level, the system must ensure **no conflict or data loss** (e.g., using database locking or atomic operations).

---

#### 2. ⚙️ **CPU Cycle Level**

- Now you zoom in **deeply** into how the CPU is executing the instructions:
    
    - Teller 1’s operation might be interrupted mid-way by Teller 2’s operation.
        
    - So even if both are doing the same thing, the CPU might mix their steps.
        

⚠️ If not synchronized properly, this can lead to **inconsistent database state** (e.g., both see old balance and both write same final value).

---

### 2. ⏰ **Sharing the Clock**

- Here the point is: Are these two processes using the **same system clock** or not?
    
    - Example: `p2` might depend on `p1`'s result before it starts (like Teller 2 waits for Teller 1).
        
    - So, the **timing/order of operations matters**.
        

📌 If they share the clock, their actions are **ordered**.  
📌 If not, they are **independent** and may cause **race conditions** unless managed.

---

### 3. 🧠 **Sharing the Memory**

- Both tellers are accessing **shared memory (database)**.
    
- If **both try to write at the same time**, it must be **mutually exclusive** (only one allowed at a time).
    

💡 This is where you use things like **locks** or **mutexes** to prevent problems.

---

### 4. 🔄 **Pattern of Interaction**

This describes **how the processes coordinate and talk to each other**.

There are two major types:

---

#### a)🕰️ **Synchronization**

- Ensures a proper **order** of events.
    
- Example: Teller 2 waits for Teller 1 to complete before proceeding.
    
- This avoids conflicts like both changing the balance at once.
    

---

#### 🔐 **Mutual Exclusion (Mutex)**

- Ensures that **only one teller** can update the balance **at a time**.
    
- Prevents **data corruption**.
    

✅ Example: Only one person can use the ATM at once — this is mutual exclusion.

---

#### 🚪 **Mutual Admission**

- Less common term; means **multiple processes may enter** a region **if safe**.
    
- It’s about **controlled concurrency**, not complete exclusion.
    

---

### b) 🗣️ **Communication Between Processes**

---

#### 📞 **Synchronous Communication**

- Both sender and receiver must be **active at the same time**.
    
- Like a **phone call** — you talk, and they listen **immediately**.
    
- Example: A client sends a request and waits for the server to respond.
    

---

#### 📧 **Asynchronous Communication**

- Sender and receiver do **not** have to be present at the same time.
    
- Like **email** — you send it now, the receiver reads it later.
    
- Example: A process puts data in a queue, another picks it up later.
    

---

### ✅ Summary

This topic is explaining how **concurrent processes interact** with:

| Concept          | Meaning                                              |
| ---------------- | ---------------------------------------------------- |
| Granularity      | Zoom level: transaction, CPU cycles, memory sharing  |
| Clock Sharing    | Do processes run in sync or not?                     |
| Memory Sharing   | Do they access same data? Use locks to avoid clash   |
| Synchronization  | Events must happen in a certain order                |
| Mutual Exclusion | Only one process at a time can do critical operation |
| Communication    | How they exchange info: sync (phone), async (email)  |

---

Let me know if you want **diagram examples** or code samples (like using threads or processes)!