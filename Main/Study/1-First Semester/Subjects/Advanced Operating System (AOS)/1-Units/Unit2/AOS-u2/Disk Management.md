#first-semester #advanced-operating-system
Disk is an I/O devices that is common to every computer.

**Disk Management** refers to how the operating system manages **secondary storage** (typically hard disks or SSDs) to store and retrieve data efficiently.

### 🔧 Main Responsibilities of Disk Management
|Task|Description|
|---|---|
|**Disk Scheduling**|Decides the order in which pending I/O requests are serviced|
|**Disk Formatting**|Prepares a disk for use (low-level and logical formatting)|
|**Partitioning**|Divides the disk into logical sections (partitions)|
|**Bad Block Recovery**|Detects and replaces bad sectors|
|**Free Space Management**|Tracks which blocks are free, allocated, or reserved|
|**File System Support**|Manages how files and directories are stored, accessed, and organized|

### 📊 1. Disk Scheduling Algorithms

These aim to **reduce seek time** (time to move disk arm):

|Algorithm|Description|Notes|
|---|---|---|
|**FCFS**|First Come First Serve|Simple, but inefficient|
|**SSTF**|Shortest Seek Time First|Picks request closest to current head position|
|**SCAN**|Elevator Algorithm|Moves in one direction, services all, then reverses|
|**LOOK**|Like SCAN but stops at last request before reversing||
|**C-SCAN**|Circular SCAN|Always scans in one direction; jumps back to beginning|
|**C-LOOK**|Like C-SCAN but stops at last request||

> **Goal:** Minimize **seek time** and **rotational latency**