# Unit 1: File Organizations & Indexes (Simple Explanation)

---

## 1️⃣ Storage of Databases (Basic Idea)

A database must be **stored physically** on storage devices.

### 🔹 Storage Hierarchy

1. **Primary Storage (RAM)**

   * Very fast
   * Volatile (data lost if power off)
   * Expensive
   * Used for **currently needed data**

2. **Secondary Storage (Disk)**

   * Non-volatile
   * Slower than RAM
   * Cheap and large
   * Used to store **main database**
   * Example: Hard disk, SSD

3. **Tertiary Storage**

   * Very slow
   * Used for **backup / archive**
   * Example: Magnetic tape

👉 DBMS mainly uses **secondary storage**

---

## 2️⃣ Why Not Store Everything in RAM?

* Too expensive 💰
* RAM is volatile ❌
* Database must persist after shutdown

👉 So:

* RAM → active data
* Disk → database
* Tape → backup

---

## 3️⃣ Disk Storage Devices (Very Important)

* Data stored on **magnetic disks**
* Disk consists of:

  * **Tracks** (circular)
  * **Sectors / Blocks**

### 🔹 Block

* Smallest unit transferred between disk & memory
* Typical size: **512 bytes – 4096 bytes**

### 🔹 Disk Access Time

Time needed because of:

* **Seek time** → moving head
* **Rotational delay** → waiting for block

👉 Disk access is **slow**, so DBMS minimizes disk I/O

---

## 4️⃣ Buffering of Blocks

**Buffer** = space in RAM to temporarily store disk blocks

### 🔹 Double Buffering

* While CPU processes one buffer,
* Disk loads next block into another buffer

👉 Improves performance by **parallelism**

---

## 5️⃣ Records and Files

### 🔹 Record

* Collection of fields (name, age, salary)
* Can be:

  * Fixed length
  * Variable length

### 🔹 File

* Collection of records
* Stored on disk blocks
* Has a **file header** (metadata)

### 🔹 Blocking Factor (bfr)

Number of records per block

$bfr = \lfloor B / R \rfloor$

Unused space:
$B - (bfr × R)$

---

## 6️⃣ Spanned vs Unspanned Records

### 🔹 Unspanned

* Record **cannot cross block boundary**
* Simple & fast
* Used when record size < block size

### 🔹 Spanned

* Record **can span multiple blocks**
* Used when record is large

---

## 7️⃣ File Block Allocation Methods

1. **Contiguous Allocation**

   * Blocks stored consecutively
   * Fast access
   * Difficult to grow

2. **Linked Allocation**

   * Each block points to next
   * Easy growth
   * Slow access

3. **Indexed Allocation**

   * Index contains block addresses
   * Fast random access

---

## 8️⃣ Operations on Files (Exam Favorite)

* OPEN
* FIND
* FINDNEXT
* READ
* INSERT
* DELETE
* MODIFY
* CLOSE
* REORGANIZE

---

## 9️⃣ Files of Unordered Records (Heap File)

### 🔹 Characteristics

* Records stored in **no order**
* Insert at end → **fast insertion**
* Search → **linear search (slow)**

### 🔹 Best for:

* Frequent inserts
* Rare searches

---

## 🔟 Files of Ordered Records (Sorted File)

### 🔹 Characteristics

* Records stored in **sorted order**
* Binary search possible → **fast search**
* Insert is **slow**

### 🔹 Overflow File

* New records inserted into overflow file
* Periodically merged with main file

---

## 1️⃣1️⃣ Hashing Techniques

### 🔹 Basic Idea

Hash function maps key → block address

Example:
$h(K) = K \bmod M$

### 🔹 Hash File

* Very fast search for **equality conditions**
* Collisions may occur

---

## 1️⃣2️⃣ Collision Resolution Techniques

1. **Open Addressing**

   * Search next free slot

2. **Chaining**

   * Overflow records linked together

3. **Multiple Hashing**

   * Use second hash function

---

## 1️⃣3️⃣ External Hashing (Disk Hashing)

* Uses **buckets** (one or more disk blocks)
* Each key mapped to a bucket
* Overflow handled using overflow file

---

## 1️⃣4️⃣ Dynamic Hashing Techniques

Used when file grows/shrinks

### 🔹 Extendible Hashing

* Uses directory
* Directory size = $2^d$
* No overflow file

### 🔹 Dynamic Hashing

* Uses tree-structured directory

### 🔹 Linear Hashing

* No directory
* Buckets split gradually

---

## 1️⃣5️⃣ RAID Technology (Very Important)

**RAID = Redundant Array of Independent Disks**

### 🔹 Goals

* Faster access 🚀
* Fault tolerance 🛡️

### 🔹 Data Striping

* Data split across multiple disks

### 🔹 RAID Levels (Short)

| Level  | Description                                  |
| ------ | -------------------------------------------- |
| RAID 0 | Striping only (high performance, no safety)  |
| RAID 1 | Mirroring (data safety, redundancy)          |
| RAID 2 | Bit-level striping with Hamming code parity  |
| RAID 3 | Byte-level striping with single parity disk  |
| RAID 4 | Block-level striping with single parity disk |
| RAID 5 | Block-level striping with distributed parity |
| RAID 6 | Block-level striping with double parity      |


---

## 1️⃣6️⃣ Storage Area Networks (SAN)

* High-speed network connecting servers & storage
* Storage devices shared among many servers
* Flexible and scalable

### 🔹 Advantages
* Long distance (up to 10 km)
* Easy expansion
* High performance

---

## 1️⃣7️⃣ Indexing (Very Important for Exams)

### 🔹 What is Index?

* Data structure with:

  * **Search key**
  * **Pointer to data block**

👉 Makes search **faster**

---

## 1️⃣8️⃣ Types of Indexing

### 🔹 Dense Index

* One index entry per record
* Fast search
* More space

### 🔹 Sparse Index

* One index entry per block
* Less space
* Slower than dense

---

## 1️⃣9️⃣ Single-Level Index Types

### 🔹 Primary Index

* On ordered file
* On primary key
* Sparse index

### 🔹 Clustering Index

* On ordered **non-key** field
* Groups same values together

### 🔹 Secondary Index

* On non-ordering field
* Dense index
* Multiple allowed

---

## 2️⃣0️⃣ Multi-Level Index

* Index on index
* Reduces search cost
* Acts like a **tree**
* Problem: insert & delete expensive

---

## 🧠 Final Exam Summary (Must Remember)

* Disk I/O is expensive → minimize it
* Heap file → fast insert, slow search
* Sorted file → slow insert, fast search
* Hashing → fastest equality search
* RAID → performance + reliability
* Index → faster SELECT queries
* Dense = faster, Sparse = smaller

---
