#first-semester #advanced-operating-system

**EDF (Earliest Deadline First)** is a **dynamic priority** scheduling algorithm used in real-time systems.

- **Dynamic** means priorities **change over time**.
    
- The scheduler always runs the process **whose deadline is soonest**.

- The earlier the deadline, the higher the priority;
- The later the deadline, the lower the priority.

### Example
Assume 3 tasks arrive at time = 0:

|Process|Execution Time (`tᵢ`)|Deadline (`Dᵢ`)|
|---|---|---|
|P1|3 ms|9 ms|
|P2|2 ms|5 ms|
|P3|1 ms|7 ms|

#### EDF Order:
- P2 has the earliest deadline → *runs first.*
- Then P3.
- Then P1.

### Pros of EDF
- **Optimal**: If a set of tasks can be scheduled by _any_ algorithm, EDF will succeed.
    
- **Efficient** use of processor time.


### ⚠️ Cons
- Can be **complex** to implement in OS kernels.
    
- Needs **constant tracking** of deadlines.
    
- **Preemptions** can happen often (overhead).


---
### 💡 Key Concepts

- **No periodicity assumed** → Tasks can arrive **at any time**, not at fixed intervals.
    
- **No uniform processing time** → Tasks can have **different execution times**.
    
- **QoS (Quality of Service)** → Usually means **all tasks meet their deadlines**.


### ✅ Theorem (EDF is Optimal):

> **If _any_ scheduling policy** can schedule a set of real-time tasks such that **all deadlines are met**,  
> then **EDF can also do it.**

This means:

- **EDF is optimal** for uniprocessor scheduling of real-time tasks.
    
- If a feasible schedule exists, **EDF will find it**.

---
### [Numerical on EDF](Numerical%20on%20EDF.md)