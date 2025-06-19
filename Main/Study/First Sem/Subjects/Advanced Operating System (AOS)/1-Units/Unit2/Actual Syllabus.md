### **1. Free-space Management**

**Goal:** Keep track of free space on disk for storing files.

**Techniques:**

- **Bit Map:** 1 bit per block; 0 = free, 1 = used.
    
- **Linked List:** Free blocks linked; slow for large disks.
    
- **Grouping:** Store addresses of free blocks in groups.
    
- **Counting:** Track starting block and number of free blocks.
    

✅ _Remember:_ Bit map is efficient in space, but scanning takes time.

---

### **2. File System Layout**

**Parts of Disk Layout:**

- **Boot Block:** Contains bootstrap code.
    
- **Superblock:** Contains metadata about file system (size, block count).
    
- **Inode Table:** Stores info about each file (name, size, pointers).
    
- **Data Blocks:** Stores actual file contents.
    

✅ _Remember:_ Inodes are central in Unix-like file systems.

---

### **3. Implementing Files and Directories**

- **File Implementation:**
    
    - **Contiguous Allocation:** Easy but suffers from fragmentation.
        
    - **Linked Allocation:** No fragmentation but slow access.
        
    - **Indexed Allocation:** Fast access via index block (used in Unix).
        
- **Directory Implementation:**
    
    - **Linear List:** Simple, slow search.
        
    - **Hash Table:** Fast access.
        

✅ _Remember:_ Unix uses indexed allocation and hierarchical directory structure.

---

### **4. Log-Structured File System (LFS)**

**Idea:** Treat storage as a log; always write new data sequentially at the end.

**Advantages:**

- Fast writes
    
- Good for flash devices
    

**Problem:** Garbage collection is needed to clean unused data.

---

### **5. Journaling File System**

**Idea:** Keep a journal (log) of changes before actually applying them.

**Why?**

- Ensures consistency even if system crashes.
    
- Faster recovery than checking entire disk.
    

✅ _Example:_ ext3, ext4 (Linux), NTFS (Windows)

---

### **6. Virtual File System (VFS)**

**Idea:** Abstraction layer that allows different file systems to coexist.

**Example:**

- ext4, FAT, NTFS all accessible through one common interface in Linux.
    

✅ _Remember:_ VFS provides a standard API for user programs.

---

### **7. Disk Scheduling**

**Goal:** Optimize read/write head movement.

**Algorithms:**

- **FCFS:** First Come First Serve
    
- **SSTF:** Shortest Seek Time First
    
- **SCAN:** Elevator algorithm
    
- **C-SCAN:** Circular SCAN
    
- **LOOK / C-LOOK:** Like SCAN but doesn’t go to end if not needed
    

✅ _Tip:_ SSTF gives best average time, but may cause starvation.

---

### **8. Flash File Systems**

**Why special?** Flash memory wears out and cannot overwrite in-place.

- A type of non-volatile memory (retains data without power) used in USB drives, SSDs, mobile devices.

**Features:**

- Wear leveling
    
- Garbage collection
    
- Journaling
    

✅ _Examples:_ JFFS, YAFFS, UBIFS

|File System|Characteristics|
|---|---|
|**JFFS (Journaling Flash File System)**|Designed for raw flash; keeps entire FS in RAM; not good for large flash devices.|
|**YAFFS (Yet Another Flash File System)**|Better performance, scalable for larger flash; uses checkpoints to speed mount.|
|**UBIFS (UBI File System)**|Works on top of UBI layer, supports large NAND flash, better wear leveling, and error handling.|

---

### **9. High Performance Flash Disks**

- Use techniques like **parallelism** (multiple flash chips) and [wear leveling](wear%20leveling.md).
    
- Require good **garbage collection** and **buffering** for performance.
    

✅ _Key terms:_ endurance, latency, write amplification

---

### **10. Improving LFS: Adaptive Block Rearrangement**

- Improving Log-Structured File Systems (LFS): Adaptive Block Rearrangement

**Problem in LFS:** Garbage collection slows down performance.

**Solution:** Adaptive Block Rearrangement

- Rearranges blocks based on access patterns.
    
- Reduces overhead in cleaning process.
    

✅ _Paper idea:_ Move “hot” (frequently used) and “cold” data separately to reduce cleaning cost.

---

### **11. Buffer Cache Management using Temporal and Spatial Locality**

- **Temporal locality:** Recently accessed blocks likely to be accessed again.
    
- **Spatial locality:** Nearby blocks likely to be accessed soon.
    

**Idea:** Design buffer cache to exploit both:

- Keep recently/frequently used data (temporal).
    
- Prefetch adjacent blocks (spatial).
    

✅ _Paper focus:_ Design algorithms that adapt based on access patterns.