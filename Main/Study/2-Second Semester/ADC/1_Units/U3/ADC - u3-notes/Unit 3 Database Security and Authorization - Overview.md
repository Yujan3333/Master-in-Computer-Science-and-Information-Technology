*(8 Hours – Very important for theory exams)*

---

## 1️⃣ Introduction to Database Security Issues

### 🔹 What is Database Security?

Database security means **protecting the database** from:

* Unauthorized access
* Misuse
* Data leakage
* Data corruption
* Data loss

👉 Goal: **Confidentiality, Integrity, Availability (CIA)**

---

### 🔹 Why Database Security is Needed?

Databases store **critical data**:

* Student records
* Bank details
* Medical data
* Company secrets

If security fails:

* Hackers can steal data
* Data can be modified or deleted
* Legal and financial loss

---

### 🔹 Types of Security Threats

| Threat              | Meaning                                |
| ------------------- | -------------------------------------- |
| Unauthorized access | User accesses data without permission  |
| Privilege abuse     | User misuses given rights              |
| Inference attack    | Guessing sensitive data using queries  |
| Malware             | Virus, Trojan, ransomware              |
| Insider threat      | Authorized user doing illegal activity |

---

### 🔹 Levels of Database Security

1. Physical level – protecting servers
2. Operating system level
3. DBMS level (our focus)
4. Network level
5. Application level

---

## 2️⃣ Discretionary Access Control (DAC)

### 🔹 Meaning

* Access control **decided by data owner**
* Owner can **GRANT** or **REVOKE** privileges

👉 Most common in **RDBMS**

---

### 🔹 Privileges

| Privilege  | Meaning         |
| ---------- | --------------- |
| SELECT     | Read data       |
| INSERT     | Add data        |
| UPDATE     | Modify data     |
| DELETE     | Remove data     |
| REFERENCES | Use foreign key |

---

### 🔹 GRANT Command

Used to **give permission**

```sql
GRANT SELECT, UPDATE
ON Student
TO user1;
```

👉 user1 can now **read and update** Student table

---

### 🔹 REVOKE Command

Used to **remove permission**

```sql
REVOKE UPDATE
ON Student
FROM user1;
```

---

### 🔹 WITH GRANT OPTION

Allows user to **pass privileges to others**

```sql
GRANT SELECT
ON Student
TO user1
WITH GRANT OPTION;
```

---

### 🔹 Problems of DAC

* Trojan horse attack
* Privileges spread uncontrollably
* No strict control

👉 Solution → **Mandatory Access Control**

---

## 3️⃣ Mandatory Access Control (MAC)

### 🔹 Meaning

* Access based on **security levels**
* Users **cannot change permissions**
* Used in **military & government systems**

---

### 🔹 Security Levels

Example:

* Top Secret
* Secret
* Confidential
* Unclassified

---

### 🔹 Rules (Very Important for Exam)

* **No Read Up**
  (Lower level cannot read higher data)
* **No Write Down**
  (Higher level cannot write to lower level)

👉 Prevents data leakage

---

### 🔹 Example

User clearance: **Secret**
Data classification: **Top Secret**

❌ User cannot read the data

---

## 4️⃣ Role-Based Access Control (RBAC)

### 🔹 Meaning

Permissions are assigned to **roles**, not users

---

### 🔹 Why RBAC?

Instead of:

* Giving permissions to 100 users

We:

* Create roles (Admin, Teacher, Student)
* Assign permissions to roles
* Assign users to roles

---

### 🔹 Example

| Role    | Privileges     |
| ------- | -------------- |
| Admin   | All            |
| Teacher | SELECT, UPDATE |
| Student | SELECT         |

---

### 🔹 Advantages

* Easy to manage
* Scalable
* Secure
* Used in real systems

---

### 🔹 RBAC vs DAC (Short Exam Point)

| DAC            | RBAC        |
| -------------- | ----------- |
| User-based     | Role-based  |
| Hard to manage | Easy        |
| Less secure    | More secure |

---

## 5️⃣ Statistical Database Security

### 🔹 Meaning

Protects **aggregate data** in statistical databases

Used when:

* Users query statistics, not individual records

---

### 🔹 Problem: Inference Attack

User can infer sensitive data by combining queries

---

### 🔹 Example

```sql
AVG(Salary) WHERE Dept='HR'
```

If only one employee → salary revealed ❌

---

### 🔹 Solutions

* Query size restriction
* Noise addition
* Data suppression

---

## 6️⃣ Introduction to Flow Control

### 🔹 Meaning

Controls **how information flows** between users and data

---

### 🔹 Goal

Prevent:

* High security data flowing to low security users

---

### 🔹 Example

Admin (high level)
↓
Public user (low level) ❌

---

### 🔹 Used with

* MAC
* Multilevel security systems

---

## 7️⃣ Encryption and Public Key Infrastructure (PKI)

### 🔹 Encryption

Converting plaintext → ciphertext

---

### 🔹 Types of Encryption

#### 1️⃣ Symmetric Key Encryption

* Same key for encrypt & decrypt
* Fast
* Key sharing problem

Example: AES

---

#### 2️⃣ Asymmetric Key Encryption

* Public key + Private key
* More secure
* Slower

Example: RSA

---

### 🔹 Public Key Infrastructure (PKI)

Framework for:

* Key management
* Digital certificates
* Authentication

---

### 🔹 Components of PKI

* Public Key
* Private Key
* Certificate Authority (CA)
* Digital Certificates

---

### 🔹 Uses

* Secure database communication
* Authentication
* Data confidentiality

---

## 📌 Exam-Oriented Summary (Very Important)

* DAC → GRANT / REVOKE
* MAC → Security levels, strict rules
* RBAC → Roles instead of users
* Statistical DB → Inference problem
* Flow Control → Prevent data leakage
* Encryption → Data protection

---

## ✅ How You Should Study This Unit

1. Learn **definitions**
2. Memorize **differences (DAC vs MAC vs RBAC)**
3. Practice **SQL GRANT/REVOKE**
4. Write **examples** in answers

---

