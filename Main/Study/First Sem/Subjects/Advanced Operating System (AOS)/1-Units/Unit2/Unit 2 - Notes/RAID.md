## ✅ RAID Levels (0 to 5)

- [Block Level Striping](Block%20Level%20Striping.md)
- [Bit Level Striping](Bit%20Level%20Striping.md)
- [Byte Level Striping](Byte%20Level%20Striping.md)
- [Parity](Parity.md)
---

### 🔵 RAID 0 – Striping

- **How it works**: Splits (stripes) data **evenly across two or more disks**.
    
- ✅ **Advantage**:
    
    - High **read/write performance** (parallel access).
        
- ❌ **Disadvantage**:
    
    - **No redundancy** – if one disk fails, **all data is lost**.
        
- 📌 **Use Case**:
    
    - High-speed, **non-critical** applications (e.g., video editing).
        

---

### 🟢 RAID 1 – Mirroring

- **How it works**: Copies (mirrors) the **same data on two disks**.
    
- ✅ **Advantage**:
    
    - **High reliability** – one disk can fail without data loss.
        
- ❌ **Disadvantage**:
    
    - **Storage cost is 2x** (50% efficiency).
        
- 📌 **Use Case**:
    
    - **Critical systems** where data loss is not acceptable.
        

---

### 🟡 RAID 2 – Bit-level striping with Hamming code ECC

- **How it works**: Data is striped **at the bit level**, and error correction is done using [Hamming codes ](Unit%202%20-%20Notes/Hamming%20codes%20.md)on extra disks.
    
- ✅ **Advantage**:
    
    - Good **error detection and correction**.
        
- ❌ **Disadvantage**:
    
    - **Complex and expensive**; not used in practice.
        
- 📌 **Use Case**:
    
    - Mostly **theoretical/academic**; not used in commercial systems.
        

---

### 🟠 RAID 3 – Byte-level striping with dedicated parity

- **How it works**: Data is striped **at the byte level**, and **one disk stores parity** (error correction information).
    
- ✅ **Advantage**:
    
    - Better **fault tolerance** than RAID 0.
        
- ❌ **Disadvantage**:
    
    - Only **one request** at a time due to **byte-level striping**.
        
- 📌 **Use Case**:
    
    - Applications with large data transfers (e.g., video streaming).
        

---

### 🔴 RAID 4 – Block-level striping with dedicated parity

- **How it works**: Data is striped at the **block level**, and **one disk** stores all parity.
    
- ✅ **Advantage**:
    
    - Can handle **multiple reads simultaneously**.
        
- ❌ **Disadvantage**:
    
    - **Parity disk becomes a bottleneck** during write operations.
        
- 📌 **Use Case**:
    
    - Systems where reads are more common than writes.
        

---

### 🟣 RAID 5 – Block-level striping with distributed parity

- **How it works**: Data and parity are striped **across all disks** (no single parity disk).
    
- ✅ **Advantages**:
    
    - **High performance** (especially reads).
        
    - **Fault tolerant**: Can survive **1 disk failure**.
        
    - **Efficient storage**: Only one disk worth of space is used for parity.
        
- ❌ **Disadvantages**:
    
    - **Write performance** slightly slower due to parity calculation.
        
- 📌 **Use Case**:
    
    - Very popular in **servers and business environments** for a good balance of performance, fault tolerance, and cost.
        

---

### 🔚 **Summary Table**

|RAID|Data Protection|Speed|Storage Efficiency|Min. Disks|
|---|---|---|---|---|
|0|❌ None|🔼 High|100%|2|
|1|✅ Mirroring|🔼 High|50%|2|
|2|✅ ECC (bit-level)|❌ Complex|Low (unused)|≥3|
|3|✅ Parity|⚠️ Limited|Moderate|≥3|
|4|✅ Parity|⚠️ Bottleneck|Moderate|≥3|
|5|✅ Parity|✅ Balanced|Good (~75% with 4 disks)|≥3|