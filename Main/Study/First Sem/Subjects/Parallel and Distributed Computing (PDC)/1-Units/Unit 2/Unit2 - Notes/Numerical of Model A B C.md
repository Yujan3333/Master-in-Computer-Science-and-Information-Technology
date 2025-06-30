![](../../../../../../../../Images/First_Sem_Images/Numerical%20of%20Model%20A%20B%20C.png)

---
### Solution

Here Schedule Length for Model A and B is 4 beacuse
- P1 has 4 Tasks
- P2 has 2 Tasks
- P3 has 3 Tasks
- Max is 4 -> Schedule Length


![](../../../../../../../../Images/First_Sem_Images/Numerical%20of%20Model%20A%20B%20C-1.png)

#### For Model C

**Processor P1:**
- Task 1: time 0-1
- Task 4: time 1-2  
- Task 5: time 2-3
- Task 8: time 3-4
- **P1 finishes at time 4**

**Processor P2:**
- Task 2: time 0-1
- Task 9: time 1-2
- **P2 finishes at time 2**

**Processor P3:**
- Task 3: time 0-1
- Task 6: time 1-2
- Task 7: time 2-3
- **P3 finishes at time 3**

The **total cost (makespan)** is the maximum completion time across all processors.

**Total cost for Model C = max(4, 2, 3) = 4**