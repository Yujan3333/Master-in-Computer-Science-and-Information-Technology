### 📦 **3. Block-Level Striping**

- **What is it?**  
    Data is divided into **blocks (chunks)**, and each block is stored on a **different disk**.
    
- 🧱 **Example:**  
	Suppose we have 3 disks:
	```md
	File: A B C D E F
	Disk 1: A   D
	Disk 2: B   E
	Disk 3: C   F
	
	```



    
- ✅ **Used in RAID 0, 4, 5**  
    It improves **performance** because multiple disks work in **parallel**.
    
- 🔁 **Why it matters:**
    
    - **Block-level** striping is faster than byte-level (used in RAID 3).
        
    - It allows **independent access** to different parts of the data.