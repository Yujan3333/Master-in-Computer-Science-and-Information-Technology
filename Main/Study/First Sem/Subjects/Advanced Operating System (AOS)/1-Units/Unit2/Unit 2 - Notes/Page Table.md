## Page Table Entry Layout (32-bit system)

![](../../../../../../../../Attachments/Page%20Table.png)

## Core Function

**Mathematical representation:**

```
page_frame = page_table(page_number)
```

The **virtual page number** serves as an **index** into the page table to find the corresponding **physical frame number**.

## Detailed Component Explanation

### 1. **Page Frame Number** (Primary Component)

- **Purpose**: Locate the physical frame where the page is stored
- **Size**: Most significant bits of the entry
- **Function**: Maps virtual page to physical frame

### 2. **Present/Absent Bit** (Validity Bit)

- **Present (1)**: Page is currently in physical memory
- **Absent (0)**: Page is not in memory (stored on disk)
- **Action on Absent**: Triggers a **page fault trap**
- **Page Fault**: OS must load the page from disk to memory

### 3. **Protection Bits**

- **Purpose**: Define access permissions for the page
- **Types**:
    - **Read-only**: Can only read data
    - **Read-write**: Can read and modify data
    - **Execute**: Can execute code from this page
- **Security**: Prevents unauthorized access to memory regions

### 4. **Modified Bit (Dirty Bit)**

- **Purpose**: Track if page has been changed since loading
- **Set when**: Any write operation occurs to the page
- **Importance**: Determines if page needs to be written back to disk
- **Optimization**: Clean pages can be discarded without writing to disk

### 5. **Referenced Bit**

- **Purpose**: Track page usage for replacement algorithms
- **Set when**: Page is accessed (read or write)
- **Usage**: Helps implement LRU, Clock, and other replacement policies
- **Reset**: Periodically cleared by OS to track recent usage

### 6. **Caching Disabled Bit**

- **Purpose**: Control CPU cache behavior for this page
- **When used**: Memory-mapped I/O, device registers
- **Function**: Ensures direct access to hardware without caching
- **Example**: Video memory, hardware control registers

## Page Table Operations

### Address Translation Process:

1. **Extract page number** from virtual address
2. **Use page number as index** into page table
3. **Check present/absent bit**:
    - If present: Get frame number and form physical address
    - If absent: Generate page fault
4. **Check protection bits** for access validity
5. **Set reference bit** (and modified bit if writing)

### Example Address Translation:

```
Virtual Address: 0x12345678
Page Size: 4KB (12 bits offset)

Page Number = 0x12345678 >> 12 = 0x12345
Offset = 0x12345678 & 0xFFF = 0x678

Page Table Entry = page_table[0x12345]
If present bit = 1 and frame = 0x789AB:
Physical Address = (0x789AB << 12) | 0x678 = 0x789AB678
```

## Page Fault Handling

When **present/absent bit = 0**:

1. **Page fault trap** is generated
2. **OS page fault handler** is invoked
3. OS finds a **free frame** (or evicts a page)
4. **Loads page from disk** into the frame
5. **Updates page table** with new frame number
6. **Sets present bit** to 1
7. **Restarts the instruction** that caused the fault

## Memory Management Benefits

- **Demand Paging**: Only load pages when needed
- **Memory Protection**: Prevent unauthorized access
- **Efficient Swapping**: Track which pages need disk writes
- **Smart Replacement**: Use reference bits for better algorithms
- **Hardware Integration**: Handle special memory regions properly

This structure enables efficient virtual memory management while providing security, performance optimization, and flexible memory allocation.

---
### [Page Table Challenges](Page%20Table%20Challenges.md)
