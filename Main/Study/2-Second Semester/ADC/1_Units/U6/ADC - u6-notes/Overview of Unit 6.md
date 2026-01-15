## 1️⃣ Parallel Database (Simple idea)

**Parallel DBMS** = Database system that uses **multiple CPUs/processors** to run queries **at the same time** to make them faster.

👉 Goal: **High speed & high throughput**

### Types of Parallel Database Architecture

### 🔹 1. Shared Memory Architecture

* All processors **share the same main memory and disk**
* Fast communication
* Suitable for **small systems**
* ❌ Not scalable (memory becomes bottleneck)

### 🔹 2. Shared Disk Architecture

* Each processor has **its own memory**
* All processors **share the same disk**
* More scalable than shared memory
* ❌ Disk contention possible

### 🔹 3. Shared Nothing Architecture

* Each processor has **its own memory and disk**
* No sharing at all
* Most **scalable and fault tolerant**
* Used in **big data systems**

---

## 2️⃣ Distributed Database (DDB) – Simple idea

A **distributed database** is a database:

* Stored at **multiple computers (sites)**
* Connected by a **network**
* But appears to the user as **one single database**

👉 User doesn’t know **where data is stored** (this is called **transparency**)

---

## 3️⃣ Advantages of Distributed Databases

### 🔹 Transparency (Very important for exams)

1. **Distribution transparency**

   * User does not know data location

2. **Location transparency**

   * Query can be executed from any site

3. **Naming transparency**

   * Same name used to access data everywhere

4. **Replication transparency**

   * Multiple copies of data exist
   * User doesn’t worry which copy is used

5. **Fragmentation transparency**

   * Tables may be split (fragmented)
   * User still sees full table

---

### 🔹 Other Advantages

* ✅ **High reliability & availability**

  * If one site fails, others work
* ✅ **Better performance**

  * Data stored near where it is used
* ✅ **Easy expansion (scalability)**

---

## 4️⃣ Data Fragmentation (Breaking a table)

| Type         | Description                                 | Example                                    |
| ------------ | ------------------------------------------- | ------------------------------------------ |
| Horizontal   | Subset of rows based on a condition         | $\sigma_{DNO=5}(EMPLOYEE)$                 |
| Vertical     | Subset of columns, must include primary key | $\Pi_{SSN,Name}(EMPLOYEE)$                 |
| Mixed/Hybrid | Combination of horizontal and vertical      | $\Pi_{SSN,Name}(\sigma_{DNO=5}(EMPLOYEE))$ |


### 🔹 Horizontal Fragmentation

* Table is split by **rows**
* Uses **conditions**
* Example:

  * Employees where DNO = 5

👉 Reconstructed using **UNION**

---

### 🔹 Vertical Fragmentation

* Table is split by **columns**
* No conditions used
* **Primary key must be included** in every fragment

👉 Reconstructed using **JOIN (Outer Join)**

---

### 🔹 Mixed (Hybrid) Fragmentation

* Combination of **horizontal + vertical**
* Uses **SELECT + PROJECT**

---

## 5️⃣ Replication and Allocation

### 🔹 Data Replication

* Copy of data stored at multiple sites
* Types:

  * **Full replication** → whole DB copied everywhere
  * **Partial replication** → some data copied

### 🔹 Data Allocation

* Decides **which fragment goes to which site**

---

## 6️⃣ Types of Distributed Database Systems

### 🔹 Homogeneous DDBMS

* Same DBMS software everywhere
* Example: Oracle at all sites
* OS may differ (Linux, Windows, Unix)
![](../../../../../../../Images/Second_Sem_Images/Overview%20of%20Unit%206-homogeneous%20DDBMS.png)


### 🔹 Heterogeneous DDBMS

Different DBMS at different sites

1. **Federated DB**

   * Single global schema
   * Less local autonomy

2. **Multidatabase**

   * No global schema
   * Schema built dynamically

![](../../../../../../../Images/Second_Sem_Images/Overview%20of%20Unit%206-Heterogeneous%20DDBMS.png)


---

## 7️⃣ Query Processing in Distributed DB

### Main problem:

🚨 **Data transfer over network is expensive**

### Example idea:

* Employee table at Site 1
* Department table at Site 2
* Query submitted at Site 3

### Best strategy:

👉 **Send the smaller table to the bigger one**
👉 Perform join where data is large
👉 Send only **final result**

✔ This minimizes network cost

---

## 8️⃣ [Concurrency Control & Recovery](Concurrency%20Control%20&%20Recovery.md)

Distributed DB has extra problems:

### 🔹 Problems

* Multiple copies of data
* Site failure
* Network failure
* Distributed commit
* Distributed deadlock

---

### 🔹 Primary Site Technique

* One site acts as **coordinator**
* Manages locking & commit

✅ Simple to implement
❌ Single point of failure

![](../../../../../../../Images/Second_Sem_Images/Overview%20of%20Unit%206-primary%20site.png)

---

### 🔹 Primary Copy Technique

* Each data item has a **primary copy**
* Lock only primary copy

✅ Load distributed
❌ Complex directory management

---

### 🔹 Voting-Based Concurrency Control

* No primary site
* Majority vote required for lock
* Timeout → transaction aborted

---

## 9️⃣ Client–Server Database Architecture

### Simple idea:

* **Client** → sends request
* **Server** → processes request

### Responsibilities:

* Client:

  * Query parsing
  * Query decomposition
  * Result combination
* Server:

  * Data storage
  * Query execution
* Communication software:

  * Manages data transfer

---

### SQL Query Processing Flow

1. Client breaks query into sub-queries
2. Sub-queries sent to servers
3. Servers execute and return results
4. Client combines results

---

## 🔟 One-line Exam Summary

* **Parallel DB** → Multiple CPUs, faster execution
* **Distributed DB** → Multiple sites, single logical DB
* **Fragmentation** → Split data
* **Replication** → Copy data
* **Homogeneous** → Same DBMS
* **Heterogeneous** → Different DBMS
* **Primary site** → Central coordinator
* **Client-server** → Client requests, server responds

---
