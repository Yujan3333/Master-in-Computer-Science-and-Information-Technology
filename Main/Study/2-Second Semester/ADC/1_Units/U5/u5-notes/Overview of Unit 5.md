# 📘 UNIT 5: Object-Relational and Extended Relational Databases

---

## 1️⃣ Introduction

### 🔹 Background

Object-database systems developed in **two directions**:

### 1️⃣ Object-Oriented DBMS (OODBMS)

* Alternative to relational DB
* Designed for **complex objects**
* Strongly tied to **OOP languages**
* DBMS features added to programming languages

👉 Example use: CAD, multimedia, engineering apps

---

### 2️⃣ Object-Relational DBMS (ORDBMS)

* **Extension of relational DB**
* Adds **object-oriented features** to RDBMS
* Acts as a **bridge between RDBMS and OODBMS**

👉 Example: **PostgreSQL**

---

### 🔹 Why ORDBMS was needed?

* RDBMS cannot handle complex data well
* OODBMS too different from SQL world
* ORDBMS keeps **tables + SQL**, adds **objects**

---

## 2️⃣ RDBMS vs ORDBMS (VERY IMPORTANT FOR EXAM)

| RDBMS                     | ORDBMS                    |
| ------------------------- | ------------------------- |
| Based on relational model | Relational + Object model |
| Uses tables only          | Tables + objects          |
| Simple data types         | Complex data types        |
| No extensibility          | User-defined types        |
| Mature & stable           | Still evolving            |
| Poor OOP support          | Strong OOP support        |
| SQL                       | Extended SQL / OQL        |
| Traditional applications  | Complex applications      |

👉 Examples:

* RDBMS: MySQL, SQL Server
* ORDBMS: PostgreSQL

---

## 3️⃣ Database Design for an ORDBMS

### 🔹 Key Idea

Design database using:

* Tables (like RDBMS)
* User Defined Types (UDTs)
* Methods
* Inheritance

👉 Supports **complex real-world data**

---

## 4️⃣ Nested Relations and Collections

---

### 🔹 Meaning

A **nested collection** is:

* A collection **inside another collection or object**

---

### 🔹 Why needed?

To represent **one-to-many relationships naturally**

---

### 🔹 Example: Book & Authors

One book → many authors

Instead of multiple tables:

```
Book
 ├── title
 └── authors [Author1, Author2]
```

---

### 🔹 Advantage

✔ Natural modeling
✔ Less joins
✔ Better object representation

---

## 5️⃣ New Challenges in ORDBMS

Adding object features creates **new problems**:

1. Storage & access methods
2. Query processing
3. Query optimization

---

## 6️⃣ Storage and Access Methods

---

### 🔹 Why storage is difficult?

ORDBMS stores:

* Large objects
* User-defined types
* Nested structures

---

### 🔹 Storing Large ADTs

Problems:

* ADTs may be larger than disk page
* Need special storage (like BLOBs)
* Pointers from tuples to objects

---

### 🔹 Structured Objects

* Can grow in size over time
* Need flexible disk layout

👉 Example: movie stars list increasing over time

---

### 🔹 Arrays Storage Issue

* Subarrays may not be contiguous
* High I/O cost

👉 Solution:

* Break arrays into **chunks**
* Store efficiently

---

## 7️⃣ Indexing New Types

---

### 🔹 Problem

Traditional indexes support:

* Equality
* Range conditions

❌ Not enough for ADTs

---

### 🔹 ORDBMS Requirement

* Index methods & operators
* Index structured objects

👉 Example: spatial index for images

---

## 8️⃣ Query Processing in ORDBMS

---

### 🔹 Why different?

* ADTs and methods involved
* Costly operations

---

### 🔹 Important Concepts

#### 1️⃣ User-Defined Aggregates

* Users define their own aggregate functions

👉 SQL aggregates not suitable for images/audio

---

#### 2️⃣ Method Security

* ADT methods may contain bugs or malicious code
* DBMS must restrict harmful methods

---

#### 3️⃣ Method Caching

* Store method results
* Avoid repeated computation

👉 Improves performance

---

#### 4️⃣ Pointer Swizzling (Important Term)

* Replace OIDs with memory pointers
* Faster access to in-memory objects

---

## 9️⃣ Query Optimization

---

### 🔹 Why optimizer needs update?

* New indexes
* New operators
* Expensive methods

---

### 🔹 Registering Indexes

Optimizer must know:

1. Which conditions index supports
2. Cost of fetching tuples

---

### 🔹 Expensive Selection Optimization (Exam Favorite)

* Some conditions are costly
* Cheap conditions checked first

👉 Example:

```
frameno < 100 AND is_herbert(image)
```

✔ Check `frameno < 100` first

---

## 🔟 SQL3 (SQL:1999)

---

### 🔹 What is SQL3?

* SQL standard released in **1999**
* Adds object-oriented features

---

### 🔹 Key Features

* Object-relational extensions
* Recursive queries
* Triggers & stored procedures
* XML support
* User-defined types & functions

---

## 1️⃣1️⃣ Implementation Issues for Extended Types

When adding new types, DBMS must handle:

* Storage format
* Indexing
* Query optimization
* Transactions
* Concurrency control

---

## 1️⃣2️⃣ System Comparison (IMPORTANT)

---

### 🔹 Definitions

* **RDBMS**: Pure relational system
* **ORDBMS**: RDBMS + object extensions
* **OODBMS**: Programming language + persistence

---

### 🔹 RDBMS vs ORDBMS

| RDBMS             | ORDBMS               |
| ----------------- | -------------------- |
| Simple            | Feature rich         |
| Easy optimization | Complex optimization |
| Less versatile    | More versatile       |

---

### 🔹 OODBMS vs ORDBMS – Similarities

✔ ADTs
✔ Object identity
✔ Inheritance
✔ Queries
✔ Concurrency & recovery

---

### 🔹 OODBMS vs ORDBMS – Differences (VERY IMPORTANT)

| OODBMS                        | ORDBMS                      |
| ----------------------------- | --------------------------- |
| DB features added to language | Object features added to DB |
| OQL                           | Extended SQL                |
| Weak query optimization       | Strong query optimization   |
| Language-centric              | Database-centric            |

---

## 🔚 Final Exam-Oriented Summary

⭐ ORDBMS extends RDBMS with object features
⭐ Supports complex & nested data
⭐ Uses extended SQL (SQL3)
⭐ Bridges gap between RDBMS and OODBMS
⭐ Better for modern applications

---

## 📝 How to Write Answers in Exam

* Start with **definition**
* Add **comparison table**
* Give **simple example**
* Use keywords:
  *ADT, ORDBMS, Nested Collections, SQL3*

---

