## 🔸 **Byte-level Striping**

### ✅ What it is:

- **Splits data into bytes** (8 bits each) and distributes each byte **across different disks**.
    

### 🧠 Example:

To store the word `HELLO` (which is 5 bytes), and we have 3 disks:

- Disk 1 → H
    
- Disk 2 → E
    
- Disk 3 → L
    
- Disk 1 → L
    
- Disk 2 → O
    

This allows **faster access than bit-level**, but still requires **cooperation between disks** for files.

### 📌 Used in:

- **RAID 3** (with one dedicated parity disk)