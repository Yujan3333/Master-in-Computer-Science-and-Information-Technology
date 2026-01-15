
## 1️⃣ Discretionary Access Control (DAC)

### 👉 What it means

Access to data is **decided by the owner of the object** (table, file, view).

The owner can **grant or revoke permissions** to other users.

### 👉 Key idea

**“Owner decides who gets access.”**

### 👉 Example

* User **U1** creates a table `Student`
* U1 grants:

  ```
  GRANT SELECT ON Student TO U2;
  ```
* U2 can now read the table

### 👉 Characteristics

* Flexible
* User-controlled
* Common in traditional DBMS

### 👉 Weakness

* Prone to information leakage
* No strict security enforcement

---

## 2️⃣ Mandatory Access Control (MAC)

### 👉 What it means

Access is **controlled by the system**, not by users.

Both:

* Users have **security clearances**
* Data has **security classifications**

Access is allowed **only if clearance ≥ classification**.

### 👉 Key idea

**“System decides based on security levels.”**

### 👉 Example

* User clearance: **Secret**
* Data classification: **Top Secret**
* ❌ Access denied

### 👉 Characteristics

* Very strict
* Used in military/government systems
* Users cannot override rules

### 👉 Strength

* Prevents data leakage
* High security

---

## 3️⃣ Role-Based Access Control (RBAC)

### 👉 What it means

Access is assigned based on **roles**, not individual users.

Users are assigned roles, and roles have permissions.

### 👉 Key idea

**“Roles decide access.”**

### 👉 Example

* Role: `Doctor`

  * SELECT Patient
  * UPDATE Prescription
* User Ram → assigned role `Doctor`

Ram automatically gets all doctor permissions.

### 👉 Characteristics

* Easy to manage
* Scales well for large organizations
* Common in enterprise systems

---

## 📊 Comparison Table (Best for exams)

| Feature                   | DAC          | MAC           | RBAC        |
| ------------------------- | ------------ | ------------- | ----------- |
| Access control decided by | Object owner | System        | Role        |
| User can grant access     | Yes          | No            | No          |
| Security levels used      | No           | Yes           | Optional    |
| Flexibility               | High         | Low           | Medium      |
| Security strength         | Low–Medium   | High          | Medium–High |
| Used in                   | General DBMS | Military/Govt | Enterprises |

- *user* Takes *AC* and goes to *SL* with full *Security Strength* to *use* it

---

## 📝 One-line definitions (Very exam friendly)

* **DAC:** Access is controlled by the data owner.
* **MAC:** Access is controlled by the system using security classifications.
* **RBAC:** Access is controlled based on user roles.

---

## ✍️ 5-marks exam answer (ready to write)

> Discretionary Access Control (DAC) allows data owners to grant or revoke access privileges to other users. Mandatory Access Control (MAC) enforces access decisions based on system-defined security classifications and user clearances, without user discretion. Role-Based Access Control (RBAC) assigns permissions to roles, and users acquire permissions by being assigned to appropriate roles. MAC provides the highest security, while RBAC improves manageability in large systems.

---
