## 🔹 **Bit-level Striping**

### ✅ What it is:

- **Splits data into individual bits** and stores them **across multiple disks**.
    
- Each **bit** of a byte is written to a **different disk**.
    

### 🧠 Example:

Let’s say we want to write the byte `10110110` and we have 8 disks:

- Disk 1 → bit 1
    
- Disk 2 → bit 0
    
- Disk 3 → bit 1
    
- Disk 4 → bit 1
    
- Disk 5 → bit 0
    
- Disk 6 → bit 1
    
- Disk 7 → bit 1
    
- Disk 8 → bit 0
    

This is **very fine-grained** and **needs all disks to work together** for each operation.

### 📌 Used in:

- **RAID 2** (with Hamming code for error correction)
    

### ❌ Disadvantage:

- Complex and not practical
    
- Needs **synchronized access** to all disks for even a single byte