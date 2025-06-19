**Belady's Anomaly** is a counter-intuitive phenomenon in page replacement algorithms where **increasing the number of page frames can actually increase the number of page faults**.

## What You'd Expect:
- More frames = More space for pages = Fewer page faults
- **Logical assumption:** More memory should always help performance

## What Actually Happens:
- Sometimes **more frames = MORE page faults**
- This violates our intuition about memory management

## **Classic Example - FIFO Algorithm:**

**Page Reference String:** 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

**With 3 Frames (FIFO):**

```
Reference: 1  2  3  4  1  2  5  1  2  3  4  5
Frame 1:   1  1  1  4  4  4  5  5  5  3  3  3
Frame 2:   -  2  2  2  1  1  1  1  1  1  4  4
Frame 3:   -  -  3  3  3  2  2  2  2  2  2  5

Faults:    F  F  F  F  F  F  F  -  -  F  F  F
Total Page Faults: 9
```

**With 4 Frames (FIFO):**

```
Reference: 1  2  3  4  1  2  5  1  2  3  4  5
Frame 1:   1  1  1  1  1  1  5  5  5  5  4  4
Frame 2:   -  2  2  2  2  2  2  1  1  1  1  1
Frame 3:   -  -  3  3  3  3  3  3  2  2  2  2
Frame 4:   -  -  -  4  4  4  4  4  4  3  3  5

Faults:    F  F  F  F  -  -  F  F  F  F  F  F
Total Page Faults: 10
```

**Result:** 4 frames gave **MORE** page faults than 3 frames!


## Why This Happens:
**Stack vs Non-Stack Algorithms:**

**Stack Algorithms (No Belady's Anomaly):**

- **LRU (Least Recently Used)**
- **Optimal Algorithm**
- Property: Pages in memory with n frames are **subset** of pages with n+1 frames

**Non-Stack Algorithms (Can Have Belady's Anomaly):**

- **FIFO (First In, First Out)**
- **Random**
- No inclusion property guaranteed

## FIFO's Problem:
- **Doesn't consider** page usage patterns
- **Oldest page** might still be frequently used
- **More frames** can change replacement patterns in unexpected ways

## Key Insights:
**1. More Memory ≠ Always Better Performance**
- Algorithm design matters more than just memory size
- Poor algorithms can waste additional memory

**2. Algorithm Choice is Critical**
- **LRU** and **Optimal** never show Belady's Anomaly
- **FIFO** is simple but can be counterproductive

**3. Real-World Impact**
- **Rare in practice** but theoretically important
- Shows why **algorithm analysis** is crucial

## Prevention:
- Use **stack-based algorithms** like LRU
- Avoid simple FIFO for critical systems
- Consider **working set** or **clock algorithms**