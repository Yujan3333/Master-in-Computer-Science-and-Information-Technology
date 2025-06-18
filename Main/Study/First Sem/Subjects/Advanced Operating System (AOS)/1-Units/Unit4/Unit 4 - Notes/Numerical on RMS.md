![](../../../../../../../../Attachments/Numerical%20on%20RMS%20Que1.png)

## Rate Monotonic Scheduling Basics

**Key Principle**: Priority is assigned based on the **inverse of the period** (rate)

- **Shorter periods = Higher priority**
- **Longer periods = Lower priority**

This is a **fixed-priority preemptive** scheduling algorithm.

### Example 1 (Schedulable Case)

**Given Tasks:**

- **P₁**: Period = 50 msec, Execution time = 20 msec
- **P₂**: Period = 100 msec, Execution time = 35 msec

**Priority Assignment:**

- P₁ has higher priority (shorter period: 50 < 100)

**Schedulability Analysis:**

- Total CPU utilization = (20/50) + (35/100) = 0.4 + 0.35 = **0.75 = 75%**.         *from formula*
- Since 75% < 100%, there's spare capacity (25 msec per 100 msec)

**Schedule Execution:**

- **0-20**: P₁ executes (1st instance)
- **20-50**: P₂ executes (partial, 30 msec)
- **50-70**: P₁ executes (2nd instance) - **preempts P₂**
- **70-75**: P₂ completes remaining 5 msec
- **75-100**: Idle time (spare capacity)

**Result**: ✅ **Both tasks meet all deadlines**

---
### Example 2  (Non-Schedulable Case)
![](../../../../../../../../Attachments/Numerical%20on%20RMS%20Num2.png)

> [!info]+ Even though there is CPU capacity $P_2$ is not completed HERE!


**Given Tasks:**

- **P₁**: Period = 50 msec, Execution time = 25 msec
- **P₂**: Period = 80 msec, Execution time = 35 msec

**Priority Assignment:**

- P₁ has higher priority (shorter period: 50 < 80)

**Schedulability Analysis:**

- Total CPU utilization = (25/50) + (35/80) = 0.5 + 0.4375 = **0.9375 = 94%**
- Even though 94% < 100%, **RMS cannot guarantee schedulability**

**Schedule Execution:**

- **0-25**: P₁ executes (1st instance)
- **25-50**: P₂ executes (25 msec)
- **50-75**: P₁ executes (2nd instance) - **preempts P₂**
- **75-80**: P₂ continues (5 msec)
- **80**: P₂'s deadline arrives, but P₂ still needs 5 more msec!

**Result**: ❌ **P₂ misses its deadline at time 80**