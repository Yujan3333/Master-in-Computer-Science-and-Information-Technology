## What are *Discretionary Privileges*?

**Discretionary privileges** are permissions that control **what a user is allowed to do in a database**.
They are usually **granted by the DBA (Database Administrator)** or by the owner of the object.

---

## 1️⃣ Account-level privileges (What a user can do in general)

👉 **Meaning:**
At the **account level**, privileges are given **to a user account as a whole**, not to any specific table.

These privileges define **general capabilities of a user in the database system**, regardless of which table they access.

### Examples:

* CREATE TABLE
* CREATE VIEW
* CREATE PROCEDURE
* CREATE DATABASE
* CREATE USER

### Example explanation:

If user **U1** has the privilege:

```
CREATE TABLE
```

Then:

* U1 can create tables anywhere in the database
* This permission is **independent of existing relations**

📌 **Key idea:**
Account-level privileges = *What actions a user can perform in the DB system overall*

---

## 2️⃣ Relation-level (Table-level) privileges (What a user can do on a specific table)

👉 **Meaning:**
At the **relation (table) level**, privileges are given **for individual tables or views**.

The DBA controls **who can access which table and how**.

### Common table-level privileges:

* SELECT (read data)
* INSERT (add rows)
* UPDATE (modify rows)
* DELETE (remove rows)

### Example:

```
GRANT SELECT, INSERT ON Student TO U2;
```

This means:

* User **U2** can read and insert data **only in the Student table**
* U2 **cannot** update or delete
* U2 has **no access** to other tables unless granted separately

📌 **Key idea:**
Relation-level privileges = *What a user can do on a specific table or view*

---

## 🔑 Simple comparison (Very exam friendly)

| Level          | Controls                  | Example            |
| -------------- | ------------------------- | ------------------ |
| Account level  | General database actions  | CREATE TABLE       |
| Relation level | Access to specific tables | SELECT on Employee |

---

## 📝 One-line exam answer (You can memorize this)

> **Account-level privileges specify general actions a user can perform in the database system, while relation-level privileges control access rights (such as SELECT, INSERT, UPDATE) on individual tables or views.**
