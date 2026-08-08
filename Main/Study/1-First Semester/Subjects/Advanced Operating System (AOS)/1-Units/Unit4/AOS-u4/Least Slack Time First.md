#first-semester #advanced-operating-system

It's a **real-time scheduling algorithm** that selects the task with the **least slack time** (i.e., the one we can "least afford to delay").

### 🧮 **Slack Time Formula**:

$\text{Slack Time} = \text{Time until Deadline} - \text{Remaining Computation Time}$

### Example:
- Deadline in 20 ms
- 5 ms of computation left  
    ➝ Slack Time = 20 - 5 = **15 ms**

