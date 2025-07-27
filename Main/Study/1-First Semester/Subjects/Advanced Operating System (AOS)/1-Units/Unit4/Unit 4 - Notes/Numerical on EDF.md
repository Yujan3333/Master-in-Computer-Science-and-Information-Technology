![](../../../../../../../../Images/First_Sem_Images/Numerical%20on%20EDF%20-%20Example%202%20again.png)
> [!question]+ Data
> p1 = 50 msec; t1 = 25 msec 
> p2 = 80 msec; t2 = 35 msec

   
## EDF Scheduling - Example 2 Numerical Solution

### Given Data

|Task|Period (P)|Execution Time (t)|Priority Rule|
|---|---|---|---|
|P₁|50 msec|25 msec|Dynamic (based on deadline)|
|P₂|80 msec|35 msec|Dynamic (based on deadline)|

**EDF Rule**: Earlier deadline = Higher priority

### Task Instance Analysis

#### Task Instances and Deadlines:

- **P₁ instances**: Deadlines at 50, 100, 150, 200, ...
- **P₂ instances**: Deadlines at 80, 160, 240, ...

### Step-by-Step EDF Scheduling

#### Time 0-25:

- **Ready tasks**: P₁ (deadline=50), P₂ (deadline=80)
- **Priority**: P₁ has earlier deadline (50 < 80)
- **Execute**: P₁ for 25 msec
- **Status**: P₁ completes first instance

#### Time 25-50:

- **Ready tasks**: P₂ (deadline=80)
- **Execute**: P₂ for 25 msec
- **Status**: P₂ has 10 msec remaining

#### Time 50-60:

- **Ready tasks**: P₁ (deadline=100), P₂ (deadline=80, remaining=10)
- **Priority**: P₂ has earlier deadline (80 < 100)
- **Execute**: P₂ for 10 msec
- **Status**: P₂ completes first instance

#### Time 60-80:

- **Ready tasks**: P₁ (deadline=100, remaining=25)
- **Execute**: P₁ for 20 msec
- **Status**: P₁ has 5 msec remaining

#### Time 80-85:

- **Ready tasks**: P₁ (deadline=100, remaining=5), P₂ (deadline=160)
- **Priority**: P₁ has earlier deadline (100 < 160)
- **Execute**: P₁ for 5 msec
- **Status**: P₁ completes second instance

#### Time 85-100:

- **Ready tasks**: P₂ (deadline=160, remaining=35)
- **Execute**: P₂ for 15 msec
- **Status**: P₂ has 20 msec remaining

#### Time 100-120:

- **Ready tasks**: P₁ (deadline=150), P₂ (deadline=160, remaining=20)
- **Priority**: P₁ has earlier deadline (150 < 160)
- **Execute**: P₁ for 20 msec
- **Status**: P₁ has 5 msec remaining

#### Time 120-125:

- **Ready tasks**: P₁ (deadline=150, remaining=5), P₂ (deadline=160, remaining=20)
- **Priority**: P₁ has earlier deadline (150 < 160)
- **Execute**: P₁ for 5 msec
- **Status**: P₁ completes third instance

#### Time 125-145:

- **Ready tasks**: P₂ (deadline=160, remaining=20)
- **Execute**: P₂ for 20 msec
- **Status**: P₂ completes second instance

#### Time 145-150:

- **Ready tasks**: None
- **Status**: System idle

### EDF Schedule (Gantt Chart)

```
Time:    0    25   50   60   80   85   100  120  125  145  150  160
Tasks:  |P₁25|P₂25|P₂10|P₁20|P₁5 |P₂15|P₁20|P₁5 |P₂20|idle|
        |    |    |    |    |    |    |    |    |    |    |
Jobs:   |P₁  |P₂  |P₂  |P₁  |P₁  |P₂  |P₁  |P₁  |P₂  |    |
```

### Deadline Analysis

|Task Instance|Start Times|Completion Time|Deadline|Status|
|---|---|---|---|---|
|P₁ (1st)|0|25|50|✓ Met|
|P₂ (1st)|25, 50|60|80|✓ Met|
|P₁ (2nd)|60, 80|85|100|✓ Met|
|P₂ (2nd)|85, 125|145|160|✓ Met|
|P₁ (3rd)|100, 120|125|150|✓ Met|

### Results Summary

- **Schedulability**: ✅ **SUCCESS** - All tasks meet their deadlines
- **Total CPU Utilization**: (25/50) + (35/80) = 0.5 + 0.4375 = **93.75%**
- **Algorithm**: EDF handles this 93.75% utilization successfully
- **Preemptions**: Multiple preemptions occur as deadlines change priority

### Key Observations

1. **Dynamic Priority**: Task priorities change based on approaching deadlines
2. **Optimal Scheduling**: EDF successfully schedules this task set that RMS couldn't handle
3. **Preemptive Nature**: Tasks are preempted when higher priority (earlier deadline) tasks become ready
4. **High Utilization**: 93.75% utilization is handled efficiently by EDF
5. **No Deadline Misses**: All task instances complete before their respective deadlines

**Conclusion**: EDF proves its superiority over RMS by successfully scheduling this high-utilization task set.
