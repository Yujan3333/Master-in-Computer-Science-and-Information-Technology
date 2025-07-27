### 🧮 **2. Parity**

- **What is it?**  
    **Parity** is a simple method to **check for errors** in data.
    
- **How it works:**  
    Add a **parity bit** that makes the total number of 1s in a group of bits **even (even parity)** or **odd (odd parity)**.
    
- ✅ **In RAID:**  
    Parity is used to **rebuild lost data** when a disk fails.
    
    For example:
    ```md
	Disk 1:  1011
	Disk 2:  1100
	Parity: 0111  (XOR of Disk1 and Disk2)
	
	```
    
    If Disk 1 is lost, RAID uses Disk 2 and Parity to **rebuild** Disk 1 using XOR.