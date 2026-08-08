#first-semester #advanced-operating-system

RBAC is a security model where **permissions (privileges)** are **assigned to roles**, and **users or programs are assigned to those roles**.

> Instead of giving permissions directly to each user or program,  
> you give them a **role**, and the role has the **required permissions**.

---

### 🧠 What are Privileges?

- **Privileges** refer to:
    
    - The **right to perform certain system calls** (like opening files, changing configurations).
        
    - The **right to use specific parameters** with those calls.
        

---

### 🧱 RBAC Structure:


`User → Role → Privileges`

**Example:**

- Role: "DatabaseAdmin"
    
    - Privileges: Read/write DB files, manage backup
        
- User: Yujan
    
    - Assigned to "DatabaseAdmin" role
        
    - Gains the above privileges indirectly
        

---

### 📌 Benefits of RBAC:

|Feature|Benefit|
|---|---|
|✅ **Supports Least Privilege**|Users only get access needed for their role|
|✅ **Reduces Risk of Abuse**|Safer than SUID/SGID, which give full user/group power|
|✅ **Easy Management**|Add/remove roles or users without changing many permissions|
|✅ **Auditable & Structured**|Easier to log and monitor role-based access|

---

### ❌ SUID/SGID vs RBAC

|Feature|SUID/SGID|RBAC|
|---|---|---|
|Privileges|Temporary **escalation** to another user/group|Assigned based on **defined roles**|
|Risk|High — grants full user/group power|Low — only specific actions allowed|
|Flexibility|Limited|Very flexible and policy-driven|

---

### ✅ Summary:

- RBAC assigns privileges **through roles**, not directly.
    
- Improves **security, manageability**, and supports the **principle of least privilege**.
    
- Safer alternative to using **SUID/SGID programs**, which can be abused more easily.