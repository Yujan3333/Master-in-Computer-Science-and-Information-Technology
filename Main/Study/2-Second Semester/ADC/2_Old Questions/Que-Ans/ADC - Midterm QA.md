
### **1. What are the differences between internal hashing and external hashing? What are the different techniques used for hashing? Explain any two.**

**Differences between internal and external hashing:**

| **Aspect**                | **Internal Hashing**                                      | **External Hashing**                                      |
|---------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| **Storage**               | Main memory (RAM)                                         | Secondary storage (disk)                                  |
| **Bucket size**           | Fixed (in memory)                                         | Disk block size                                           |
| **Overflow handling**     | Linked list (chaining) or open addressing                 | Overflow buckets (separate blocks)                        |
| **Used for**              | In-memory data structures (hash tables)                   | Database file organization                                |
| **Example**               | Symbol tables, compiler hash maps                         | Hash file organization in DBMS                            |

**Different hashing techniques:**
1. **Static Hashing**
2. **Dynamic Hashing** (Extendible, Linear)
3. **Consistent Hashing**

**Explanation of any two:**

**(a) Static Hashing:**  
- Uses a fixed hash function and fixed number of buckets.  
- If buckets become full, **overflow chaining** is used (linked list of overflow blocks).  
- Disadvantage: Performance degrades if data grows beyond initial allocation.

**(b) Extendible Hashing:**  
- Uses a directory (array of pointers) to map hash prefix to buckets.  
- Buckets split when they overflow, and directory doubles when needed.  
- Advantage: Minimal reorganization, good for dynamic databases.

---

### **2. What is indexing? What is its importance in searching? Explain primary indexing.**

**Indexing** is a database optimization technique that creates a **data structure** (index) to allow faster retrieval of records without scanning the entire table.

**Importance in searching:**
- Speeds up query performance (especially for SELECT, JOIN, WHERE).
- Reduces disk I/O.
- Supports efficient sorting and grouping operations.

**Primary indexing:**  
- Created on a **primary key** of an ordered data file.
- The data file is sorted on the primary key.
- The index file contains **key values** and **pointers** to the corresponding disk block.
- **Sparse indexing** is used — only one index entry per data block (first key of each block).
- Searching: Binary search on index, then linear search within the block.

---

### **3. Why query processing and optimization is necessary? Explain about different selection operations.**

**Why necessary:**
- Same query can be executed in multiple ways (different plans).
- Some plans are **much faster** than others.
- Goal: Choose the most efficient plan to minimize:
  - Execution time
  - Disk access
  - CPU usage
  - Memory usage
- Essential for large databases where naive execution can be extremely slow.

**Different selection operations in query processing:**

**(a) Linear search (file scan)**  
- Scan all records sequentially.
- Used when no index exists or selection condition is non-key.

**(b) Binary search**  
- Applicable if the file is **ordered** on the selection attribute.
- Efficient for equality searches.

**(c) Using primary index**  
- For equality on key attribute with primary index.
- Direct access via index.

**(d) Using secondary index**  
- Equality search on non-key attribute with secondary index.
- Returns pointers to all matching records.

**(e) Conjunctive selection (multiple conditions)**  
- Use one index for one condition, then check other conditions on retrieved records.
- Or use composite index if available.

**(f) Disjunctive selection**  
- If indexes exist on all disjuncts, use union of results from each.
- Otherwise, resort to linear scan.

---
