In real-time systems, some tasks (like reading a sensor or controlling a motor) **must run repeatedly at fixed intervals**.

We define a **periodic task** with three main parameters:

| Parameter | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| `ti`      | **Execution time**: how long the task runs (in milliseconds) |
| `pi`      | **Period**: how often the task needs to run                  |
| `di`      | **Deadline**: when the task must finish (often `di = pi`)    |

---
### 🕒 Example:
Let’s say we have a task:

- `t₁ = 2 ms`: it needs 2 ms of CPU time
    
- `p₁ = 10 ms`: it must repeat every 10 ms
    
- `d₁ = 10 ms`: it must complete within the 10 ms window
    
This means **every 10 ms**, the CPU must give **2 ms** to this task.

```md
Time:     0     10     20     30     40
Task:   [==]   [==]   [==]   [==]   [==]
         t1     t1     t1     t1     t1
```
- The task runs for `2 ms` in every `10 ms` window.
- Must complete before time reaches `10`, `20`, `30`, etc.

---
### ✅ Schedulability Test
Process $i$ requires $t_i$ msec of processing time every ${p_i}$ msec.

#### Formula
$$\sum_{i=1}^{m} \frac{t_i}{p_i} \leq 1$$

- non-real-time process be `0`
- Priority of process `i` -> $\frac{1}{p_{i}}$

Priority is assigned based on the inverse of its period (its rate).  
   - Shorter periods = Higher priority  
   - Longer periods = Lower priority


The above equation should be true for the system **can schedule all tasks** without missing any deadlines.

**Highest Priority Process RUNS!**

---
### [Numerical on RMS](Numerical%20on%20RMS.md)