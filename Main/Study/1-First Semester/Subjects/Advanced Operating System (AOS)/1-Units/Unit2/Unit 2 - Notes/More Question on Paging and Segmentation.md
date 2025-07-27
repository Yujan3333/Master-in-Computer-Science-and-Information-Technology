### 🔸 1. A smaller page size leads to smaller page tables

**❌ False**

- Smaller page size = **more pages** to cover the same memory space.
    
- More pages = **more entries** in the page table.
    
- Therefore, **smaller page size leads to **larger** page tables**.
    

> **Exam Point:** Smaller page size increases the number of pages, so the page table becomes **larger**, not smaller.

---
### 🔸 2. A smaller page size leads to more TLB misses

**✅ True**

- TLB (Translation Lookaside Buffer) stores **recent page table entries**.
    
- Smaller pages cover **less memory per entry**.
    
- So, the chance that the **needed address is already in the TLB** is **lower**.
    
- This leads to **more TLB misses**.
    

> **Exam Point:** Since each page maps a smaller portion of memory, more pages are needed, making it less likely the TLB contains the required page.

---

### 🔸 3. A smaller page size leads to fewer page faults

**❌ False** (This one needs correction)
- This is actually **not always true** — it **depends on the access pattern**.
    

#### 📌 Why it can be **False**:
- Smaller pages → more pages required.
    
- If a program accesses data **spread out** across memory, this can lead to **more page faults** because fewer addresses are in each page.
    

#### 📌 Why some might think it’s **True**:
- If the program only uses **small portions** of memory, smaller pages mean **less unused data is loaded**, and **fewer page faults** in some scenarios.
    

> **Correct Answer: ❌ False – smaller page size usually increases page faults** unless memory access is very localized.

### Summary of 1,2,3

|**Statement**|**True/False**|**Reason**|
|---|---|---|
|Smaller page size → smaller page tables|❌ False|More pages → more page table entries|
|Smaller page size → more TLB misses|✅ True|Less coverage per TLB entry|
|Smaller page size → fewer page faults|❌ False|More pages → more chance of missing needed page|

---
### 4. What is swapping? Can swapping permit an application  requiring 16M memory to run on a machine with 8M of  RAM?

|Question|Answer|
|---|---|
|What is swapping?|Moving whole processes between RAM and disk to manage memory|
|Can swapping run a 16MB app on 8MB RAM?|**No** — the whole process must fit into RAM to run|
This limitation cause the development of paging and virtual memory.

---

### 5. Consider the following segment table:
   ![](../../../../../../../../Images/First_Sem_Images/More%20Question%20on%20Paging%20and%20Segmentation-%20que5.png)

**Given Segment Table:**

- Segment 0: Base = 219, Size = 600
- Segment 1: Base = 2300, Size = 14
- Segment 2: Base = 90, Size = 100
- Segment 3: Base = 1327, Size = 580
- Segment 4: Base = 1952, Size = 96

**Address Translation Formula:** Physical Address = Segment Base + Offset (if offset < segment size)


**a) 0430**
- Segment number = 0, Offset = 430
- Check: 430 < 600 ✓ (valid) ✅
- Physical address = 219 + 430 = **649**

**b) 110**
- Segment number = 1, Offset = 10
- Check: 10 < 14 ✓ (valid) ✅
- Physical address = 2300 + 10 = **2310**

**c) 2500**
- Segment number = 2, Offset = 500
- Check: 500 < 100 ✗ (invalid - offset exceeds segment size) ❌
- Result: **Segmentation Fault**

**d) 3400**
- Segment number = 3, Offset = 400
- Check: 400 < 580 ✓ (valid) ✅
- Physical address = 1327 + 400 = **1727**

**e) 4112**
- Segment number = 4, Offset = 112
- Check: 112 < 96 ✗ (invalid - offset exceeds segment size) ❌
- Result: **Segmentation Fault**

#### Final Answers:
- a) 0430 → **649**
- b) 110 → **2310**
- c) 2500 → **Segmentation Fault**
- d) 3400 → **1727**
- e) 4112 → **Segmentation Fault**