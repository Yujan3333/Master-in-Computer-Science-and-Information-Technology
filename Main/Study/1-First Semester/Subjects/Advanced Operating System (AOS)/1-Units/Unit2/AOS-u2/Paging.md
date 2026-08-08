#first-semester #advanced-operating-system
The text explains that paging allows a **logical address space of a process to be non-contiguous** - meaning a program doesn't need to be stored in consecutive memory locations. 

Instead, the process gets physical memory "wherever it's available."

---
### Key Components

#### 1. **Frames (Physical Memory Blocks)**

- Physical memory is divided into **fixed-size blocks called frames**
- Frame size is typically a **power of 2** (512 bytes to 8KB)
- Example: If frame size is 4KB, physical memory is divided into 4KB chunks

#### 2. **Pages (Logical Memory Blocks)**

- Logical memory is divided into **same-size blocks called pages**
- *Page size = Frame size* (both are 4KB in our example)
- This ensures pages fit perfectly into frames

#### 3. [Page Table](Page%20Table.md)

- A data structure that **translates logical addresses to physical addresses**
- Maps which virtual page corresponds to which physical frame
- Essential for the Memory Management Unit (MMU) to work

---
### How Paging Works

#### **Program Loading Process:**

1. To run a program of **n pages**, find **n free frames** in physical memory
2. Load the program pages into these available frames
3. Set up a **page table** to track the mapping
4. Pages don't need to be loaded contiguously - they can go anywhere

#### **Address Translation:**

When CPU generates an address, it's divided into:

1. **Page Number (p)**: Used as index into page table
2. **Page Offset (d)**: Position within the page

**Formula:** Physical Address = Base Address of Frame + Page Offset

---
### Practical Example 

- **64KB program** can run in **32KB physical memory**
- **Page size**: 4KB
- **Virtual pages**: 64KB ÷ 4KB = 16 pages
- **Physical frames**: 32KB ÷ 4KB = 8 frames

Only 8 out of 16 pages can be in memory simultaneously. The rest stay on disk and are brought in "as needed" (demand paging).

---
### Advantages

- **No external fragmentation**: Pages fit exactly into frames
- **Flexible allocation**: Don't need contiguous memory
- **Larger programs**: Can run programs bigger than physical memory

### Disadvantages

- **Internal fragmentation**: Last page may be partially unused
- **Overhead**: Page table storage and lookup time