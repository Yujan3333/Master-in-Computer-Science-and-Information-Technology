### 1. Why are page sizes always a power of 2?

- **Easy address calculation:** When page size is a power of 2, splitting an address into page number and offset becomes simple. The offset is just the lower bits, and the page number is the higher bits of the address.
    
- **Hardware efficiency:** The CPU uses binary arithmetic, so powers of 2 allow fast bit masking and shifting instead of complicated arithmetic.
    
- **Simplifies memory management:** Aligning pages on power-of-2 boundaries makes memory allocation and protection easier.
    

**Summary:** Power-of-2 page sizes simplify address translation and hardware implementation.

---
### 2. Calculate how many bits are in a logical address

Given:

- Physical memory size = 2^{24} bytes (though this is physical, but we’ll focus on logical address size here)
    
- Logical address space pages = 256 pages
    
- Page size = 2^{10} bytes
    


**Step 1:** Number of pages = 256 = 2^8 pages  
This means the **page number** part of the logical address requires 8 bits.

**Step 2:** Page size = 2^{10} bytes  
This means the **offset** within a page requires 10 bits.

#### 📌Summary
**Total bits in logical address = bits for page number + bits for offset = 8 + 10 = 18 bits**

---

### 3. How does TLB increase performance in paging?

**TLB (Translation Lookaside Buffer)** is a special cache that stores recent page table entries (logical-to-physical address mappings).

- Normally, for each memory access, the CPU must:
    
    - Access the page table in memory to translate logical page number to physical frame.
        
    - Then access the actual physical memory.
        
- This two-step process increases memory access time.
    

---

**TLB improves performance by:**

- **Caching recent translations:** If the needed page table entry is in TLB (a TLB hit), the CPU can skip the page table memory access and directly get the physical frame number.
    
- **Reducing memory accesses:** TLB hit avoids the extra memory read for the page table, speeding up address translation.
    
- **Lowering average memory access time:** Because TLB hits are frequent due to locality, overall system memory access becomes much faster.