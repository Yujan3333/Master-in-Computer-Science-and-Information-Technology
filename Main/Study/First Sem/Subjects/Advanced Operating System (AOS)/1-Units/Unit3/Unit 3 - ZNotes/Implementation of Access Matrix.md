- [Access Control Matrix](Unit%203%20-%20ZNotes/Access%20Control%20Matrix.md)
- Global table
- Access Control List (ACL)
- Capability List for Domain
- [Lock-Key Mechanism](Unit%203%20-%20ZNotes/Lock-Key%20Mechanism.md)


---
## **Trade-offs in Access Control Mechanisms**

---

### 1. **Global Table**

- **Pros:** Simple and straightforward.
    
- **Cons:**
    
    - Very **large size**, even if sparse.
        
    - Difficult to manage and store efficiently.
        

---

### 2. **Access Control Lists (ACLs)**

- **Pros:** Matches well with **user needs**; easy to see who can access an object.
    
- **Cons:**
    
    - **Determining all access rights for a domain is difficult** (non-localized).
        
    - Each access request requires checking the object's ACL, which can be **slow when many objects and rights exist**.
        

---

### 3. **Capability Lists**

- **Pros:**
    
    - **Localizes access info** per process/domain.
        
    - Fast access check (possession of capability = access).
        
- **Cons:**
    
    - **Revoking capabilities** can be inefficient or complex.
        

---

### 4. **Lock-Key Mechanism**

- **Pros:**
    
    - Effective and **flexible**.
        
    - **Keys can be passed freely** between domains.
        
    - Supports **easy revocation** of access rights.
        
- **Cons:**
    
    - May require hardware support.
        
    - Complexity increases with system size.
        

---

### 📊 **Summary Table**

|Mechanism|Advantages|Disadvantages|
|---|---|---|
|**Global Table**|Simple concept|Very large, inefficient for big systems|
|**ACLs**|Matches user needs, object-focused|Access rights per domain hard to find, slow access checks|
|**Capabilities**|Localized info, fast checks|Revocation is difficult|
|**Lock-Key**|Flexible, keys transferable, easy revocation|Complexity, hardware dependence|