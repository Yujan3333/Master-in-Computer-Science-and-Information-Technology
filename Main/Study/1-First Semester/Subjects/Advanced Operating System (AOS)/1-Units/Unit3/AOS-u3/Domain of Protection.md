#first-semester #advanced-operating-system

A **domain = what a user/process can access + what it can do to it** (like read, write, execute).

## 🧠 **Protection: Objects, Processes, and Domains**

---

### 💻 **1. Computer System = Objects + Processes**

- A **computer system** consists of:
    
    - **Objects**: Resources to be **protected or accessed**
        
    - **Processes**: **Active entities** that request access to objects
        

---

### 📦 **2. Objects**

- Objects include **both hardware and software components**:
    
    - 🖥️ **Hardware**: CPU, Memory, Disk, I/O devices
        
    - 📁 **Software**: Files, Programs, Databases
        

Each object has a defined set of **valid operations**, such as:

- Read, Write, Execute, Open, Close, etc.
    

---

### 🔐 **3. Domains**

- A **domain** is a set of **access rights**.
    
- It defines:
    
    > **Which objects a process can access, and what operations it can perform on them.**
    

Example:
```yaml
Domain D1:
  - File A: Read, Write
  - Printer: Use
  - Memory Segment X: Read

```

---

### 🔄 **4. Access Matrix Model**

- A useful way to visualize this relationship:
    
    - **Rows** → Domains (D1, D2, ...)
        
    - **Columns** → Objects (File1, Printer, CPU, ...)
        
    - **Cells** → Permissions (Read, Write, Execute, etc.)
        

---

### 📌 **Summary**

|Term|Description|
|---|---|
|**Object**|Hardware or software resource (e.g., file, memory, printer)|
|**Process**|Active entity that performs actions and needs access to objects|
|**Domain**|Set of access rights – defines what a process in that domain can do with objects|

---

### ✅ **Why this matters:**

- This model provides a **foundation for protection and security** in OS design.
    
- Helps enforce **access control**, **principle of least privilege**, and **isolation** between users/processes.