### 🎯 **Objective:**

We want users to **access restricted resources** (like databases or hardware) **safely**, **without giving them direct access**.

---

### 🧠 **How it's Done:**

> Instead of giving users direct access to a resource,  
> we give them access to a **trusted program** that has **permission** to access the resource.

This way:

- ✅ Users can **perform necessary actions**
    
- ❌ But they **cannot misuse** the resource
    

---

### 📌 **Example:**

#### 🚫 Not Allowed:

User doesn't have direct access to:

- **Database**
    
- **Printer**
    
- **Network configuration**
    

#### ✅ Allowed:

User runs a **program** like:

- A **report generator** that accesses the database
    
- A **print service** that accesses the printer
    
- A **network configuration utility** with restricted inputs
    

This **program runs with special privileges** (e.g. `SetUID` or `SetGID`)  
and **only exposes limited functionality** — like generating a report, printing, or applying basic settings.

---

### 🛡️ **Security Benefit:**

- Reduces the risk of **accidental or malicious damage**
    
- Follows the **Principle of Least Privilege**
    
- Allows **controlled, auditable** access to critical resources