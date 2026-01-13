Indexing in DBMS is a technique used to **speed up data retrieval** by reducing the number of disk I/O operations.
Instead of scanning the whole table, the database uses an index to directly locate the required records.

Think of it like the **index of a book**:

* Without index → you read every page
* With index → you jump to the exact page number

---

### Types of Indexing (Short & Exam-Friendly)
#### Single Level Indexing

#### 1. **Primary Index**

* Created on the **primary key**
* File is ordered on this key
* One index entry per data block
* Very fast for searching a single record

Example:

```sql
WHERE roll = 10
```

##### a. **Dense Index**

* One index entry for **every record**
* Faster search, more storage

---

##### b. **Sparse Index**

* One index entry for **some records only** (usually one per block)
* Less storage, slightly slower

---

#### 2. **Clustering Index**

* Created on a **non-key attribute**
* Records with same value are stored together
* Used when many records have the same value

Example:

```sql
WHERE department = 'CSE'
```

---

#### 3. **Secondary Index**

* Created on any attribute (key or non-key)
* File is **not ordered** on this field
* Each index entry points to record(s)

Example:

```sql
WHERE name = 'Ram'
```


---

### **Composite (Multilevel) Index**

* Index on **multiple attributes together**

Example:

```sql
(department, age)
```

---

#### 7. **Multilevel Index**

* Index on top of another index
* Used when index becomes large
* Reduces search time further

---

#### 8. **B+ Tree Index**

* Balanced tree structure
* Most common index type in DBMS
* Supports equality and range queries efficiently

---

#### 9. **Hash Index**

* Uses hash function
* Best for equality search
* Not good for range queries

Example:

```sql
WHERE roll = 20
```

---

### One-line Definition for Exam:

> **Indexing is a database technique that reduces disk I/O by providing fast access paths to records, improving the performance of SELECT and JOIN operations.**

---

### Quick Table for Revision

| Index Type | Key Idea                    |
| ---------- | --------------------------- |
| Primary    | On primary key, ordered     |
| Clustering | On non-key, grouped records |
| Secondary  | On any attribute            |
| Dense      | Entry for every record      |
| Sparse     | Entry for some records      |
| Composite  | On multiple attributes      |
| Multilevel | Index of index              |
| B+ Tree    | Balanced, most used         |
| Hash       | Fast equality search        |
