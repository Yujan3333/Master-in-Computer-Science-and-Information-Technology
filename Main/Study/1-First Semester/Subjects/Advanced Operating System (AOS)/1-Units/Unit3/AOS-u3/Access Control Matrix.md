#first-semester #advanced-operating-system

## 🔐 **Access Control Matrix**

- The **Access Control Matrix** is a model that defines **who (domains)** can do **what (operations)** on **which (objects)**.
    
- It’s visualized as a table:
    
    - **Rows** = Domains (users/processes)
        
    - **Columns** = Objects (files, devices, etc.)
        
    - **Cells** = Allowed operations (read, write, execute, etc.)
        
![](../../../../../../../../Images/First_Sem_Images/Access%20Control%20Matrix.png)

---
## 1. Global Table

A **Global Table** is a **centralized data structure** that holds **all access rights** for **all domains and objects**.

`< Domain, Object, Rights >`

Example :

```md
< D1, FileA, Read >
< D2, Printer, Execute >
< D3, FileA, Read, Write >

```

### 🧠 **Why it Seems Simple:**

- Everything is in **one place**.
    
- Easy to **check access rights**: just search the table.


### ❌ **Disadvantages:**

|Problem|Description|
|---|---|
|**Too large**|The table becomes **very big** if there are many domains and objects.|
|**Memory inefficient**|The table is often **sparse** (most domains don’t use most objects), wasting space.|
|**Hard to manage**|If **many domains share the same access**, you still need a **separate entry** for each.|
|**No grouping support**|Can't define **groups of users** or **shared roles** efficiently.|
|**Slow search**|Searching for access rights in a huge table can be **time-consuming**.|


### 📌 **Why it’s not used in practice:**

Although simple, it doesn't scale well. That’s why **Access Control List (ACLs)** or **Capability Lists** are preferred in real systems.

---

## 📋 2. Access Control List (ACL)

### ✅ What it is:

- **Object-based** access control.
    
- Each **column** in the matrix = **ACL for that object**.
    

### 🔑 Key Ideas:

- ACL for an object lists **which domains** (users/processes) can **access it** and **what operations** are allowed.
    

### 📌 Example (for a file):

```md
ACL for File A:
  - Domain 1: Read, Write
  - Domain 2: Read
  - Domain 3: Read

```

### 🔐 Security Model:

- Object holds the list.
    
- System checks if the current domain is in the list when access is requested.
    

---

## 🧾 3. Capability List

### ✅ What it is:

- **Domain-based** access control.
    
- Each **row** in the matrix = **Capability list for a domain**.
    

### 🔑 Key Ideas:

- A **domain** has a list of **capabilities**, where each capability includes:
    
    - An **object name or address**
        
    - The **permitted operations**
        

### 📌 Example (for Domain 1):

```md 
Capability List for Domain 1:
  - File A: Read, Write
  - Printer: Execute
  - File B: Read

```


### 🔐 Important Notes:

- Capabilities act like **secure tokens or pointers**.
    
- They are **protected by the OS**.
    
- A process cannot forge or alter them.
    
- Possession of a capability **implies access** — no additional checks are needed.