#first-semester #advanced-operating-system

## EDF (Earliest Deadline First) Scheduling Solution

![](../../../../../../../../Images/First_Sem_Images/EDF%20Numerical%20Fig.png)



|Job|Arrival Time (aᵢ)|Execution Time (Cᵢ)|Deadline (dᵢ)|
|---|---|---|---|
|J₁|0|1|2|
|J₂|0|2|5|
|J₃|2|2|4|
|J₄|3|2|10|
|J₅|6|2|9|

### EDF Scheduling Steps

**EDF Rule**: Always execute the job with the earliest deadline among all ready jobs.

#### Time-by-Time Analysis:

**Time 0**:

- Ready jobs: J₁ (deadline=2), J₂ (deadline=5)
- **Execute J₁** (earliest deadline = 2)

**Time 1**:

- J₁ completes
- Ready jobs: J₂ (deadline=5)
- **Execute J₂** (only available job)

**Time 2**:

- J₃ arrives
- Ready jobs: J₂ (deadline=5, remaining=1), J₃ (deadline=4)
- **Preempt J₂, Execute J₃** (deadline=4 < 5)

**Time 3**:

- J₄ arrives
- Ready jobs: J₂ (deadline=5, remaining=1), J₃ (deadline=4, remaining=1), J₄ (deadline=10)
- **Continue J₃** (deadline=4 is earliest)

**Time 4**:

- J₃ completes
- Ready jobs: J₂ (deadline=5, remaining=1), J₄ (deadline=10)
- **Execute J₂** (deadline=5 < 10)

**Time 5**:

- J₂ completes
- Ready jobs: J₄ (deadline=10)
- **Execute J₄**

**Time 6**:

- J₅ arrives
- Ready jobs: J₄ (deadline=10, remaining=1), J₅ (deadline=9)
- **Preempt J₄, Execute J₅** (deadline=9 < 10)

**Time 7**:

- **Continue J₅**

**Time 8**:

- J₅ completes
- Ready jobs: J₄ (deadline=10, remaining=1)
- **Execute J₄**

**Time 9**:

- J₄ completes
- All jobs completed

## EDF Schedule (Gantt Chart)

```
Time:  0   1   2   3   4   5   6   7   8   9
Jobs: |J₁ |J₂ |J₃ |J₃ |J₂ |J₄ |J₅ |J₅ |J₄ |
```

### Completion Analysis

|Job|Start Time|Completion Time|Deadline|Status|
|---|---|---|---|---|
|J₁|0|1|2|✓ Met|
|J₂|1, 4|5|5|✓ Met|
|J₃|2|4|4|✓ Met|
|J₄|5, 8|9|10|✓ Met|
|J₅|6|8|9|✓ Met|

### Results

- **All deadlines are met** ✓
- **Total completion time**: 9 time units
- **Schedule is feasible** under EDF
- **Preemptions occurred**: J₂ was preempted by J₃, J₄ was preempted by J₅

### Key Observations

1. EDF successfully scheduled all jobs within their deadlines
2. **Preemptions occurred**: J₂ was interrupted by J₃ (better deadline), J₄ was interrupted by J₅
3. Total system utilization: (1+2+2+2+2)/9 = 9/9 = 100%