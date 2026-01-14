
### **Section A**  

#### **1. What is hashing technique? What are the differences between internal hashing and external hashing? Explain.**  

**Hashing technique** is a method for directly accessing data on storage media by using a hash function that maps a search key directly to the address (or bucket) where the record is stored. It is used to speed up data retrieval without performing a full table scan.  

**Differences between internal hashing and external hashing:**  

| Aspect | Internal Hashing | External Hashing |
|--------|-------------------|-------------------|
| **Storage** | Main memory (RAM) | Secondary storage (disk) |
| **Bucket Size** | Fixed bucket size in memory | Buckets correspond to disk blocks |
| **Overflow Handling** | Limited, can use chaining or open addressing | Uses overflow buckets to handle collisions |
| **Scope** | Used for in-memory data structures (hash tables) | Used in database systems for disk-based files |
| **Example** | Symbol tables in compilers, hash maps | Hash file organization in DBMS |

- **Internal hashing** assumes all data fits in memory; collisions are handled via separate chaining (linked lists) or open addressing (probing).  
- **External hashing** must consider disk I/O; static hashing suffers from overflow problems, whereas dynamic hashing (extendible, linear) allows buckets to grow/shrink without full reorganization.  

---

#### **2. What are the differences between Mandatory Access Control and Role-Based Access Control. Explain Role based access control in the context of Multilevel Security.**  

**Differences:**  

| MAC (Mandatory Access Control) | RBAC (Role-Based Access Control) |
|--------------------------------|----------------------------------|
| Access determined by system based on security labels (Top Secret, Secret, etc.) | Access based on roles assigned to users |
| Centralized, rigid policy enforcement | Flexible, based on organizational roles |
| Labels assigned to subjects and objects | Permissions assigned to roles, users assigned roles |
| Used in military, high-security systems | Common in commercial, enterprise systems |
| Difficult to change policies | Easier to manage user permissions via roles |

**RBAC in Multilevel Security (MLS) context:**  
Multilevel Security requires data to be classified at different sensitivity levels (e.g., Confidential, Secret). In RBAC for MLS:  
- Roles are created with permissions to access certain security levels.  
- A user can be assigned multiple roles, but **role activation** may depend on clearance level.  
- **Constraints** can enforce separation of duties across security levels.  
- RBAC can be integrated with MAC by assigning security labels to roles or using role hierarchies that respect clearance levels.  

---

#### **3. What are the types of fragmentation? Explain horizontal fragmentation with its representation.**  

**Types of fragmentation in distributed databases:**  
1. **Horizontal fragmentation** – Partitioning of a table by rows based on a condition (e.g., location = ‘Kathamandu’).  
2. **Vertical fragmentation** – Partitioning by columns (attributes), each fragment containing a subset of columns but all rows.  
3. **Mixed (Hybrid) fragmentation** – Combination of horizontal and vertical.  

**Horizontal fragmentation:**  
A relation \( R \) is divided into subsets of tuples such that each fragment contains rows satisfying a certain predicate.  

**Example:**  
Relation: *Employee(EmpID, Name, Dept, Location)*  

Predicate: \( \text{Location} = 'KTM' \)  
Fragment 1: All employees in KTM.  
Predicate: \( \text{Location} = 'PKR' \)  
Fragment 2: All employees in PKR.  

**Representation:**  
\[
\sigma_{\text{Location}='KTM'}(Employee) \quad \text{and} \quad \sigma_{\text{Location}='PKR'}(Employee)
\]  
The union of all fragments reconstructs the original relation.  

---

### **Section B**  

#### **4. Discuss about the challenges in implementing an ORDBMS.**  

1. **Complexity in query processing** – Supporting extended data types (objects, collections) requires new indexing, join methods, and optimization strategies.  
2. **Schema evolution** – Changing class hierarchies, methods, or attributes while maintaining data integrity and backward compatibility.  
3. **Performance** – Object-relational mapping can cause impedance mismatch; navigation via references may be slower than relational joins.  
4. **Storage management** – Storing large objects (BLOBs, CLOBs) and structured ADTs efficiently.  
5. **Transaction management** – Long-duration transactions due to complex objects.  
6. **Security and access control** – Fine-grained access control for methods and attributes within objects.  

---

#### **5. What is discretionary access control based on granting and revoking privileges? Explain.**  

Discretionary Access Control (DAC) is a security model where access to objects is determined by the **owner** of the object. Owners can grant or revoke privileges (SELECT, INSERT, UPDATE, DELETE) to other users at their discretion.  

- **Granting privileges** – `GRANT SELECT ON Employee TO user1;`  
- **Revoking privileges** – `REVOKE INSERT ON Employee FROM user1;`  

Privileges can be granted **with grant option**, allowing the grantee to further grant privileges to others.  
DAC is flexible but vulnerable to Trojan horse attacks because users can pass their permissions via programs.  

---

#### **6. Discuss the main heuristics that are applied during query optimization.**  

1. **Perform selection early** – Reduces number of tuples early in processing.  
2. **Perform projection early** – Reduces number of columns, decreasing tuple size.  
3. **Combine selection with Cartesian product to form joins** – Avoids large intermediate results.  
4. **Reorder joins** – Start with most restrictive selections and joins to minimize intermediate relation sizes.  
5. **Use left-deep join trees** – Allows pipelining and efficient use of indexes.  
6. **Avoid redundant expressions** – Eliminate common subexpressions.  
7. **Use equivalence rules** – To transform query into more efficient form.  

---

#### **7. Explain about Join operations of query processing.**  

Join operations combine rows from two or more tables based on a related column. Common join algorithms:  

1. **Nested-loop join** – For each tuple in outer relation, scan inner relation; simple but inefficient for large tables.  
2. **Block nested-loop join** – Processes relations in blocks to reduce I/O.  
3. **Indexed nested-loop join** – Uses index on inner relation’s join attribute.  
4. **Merge join** – Sorts both relations on join key and merges; good if relations are sorted or can be sorted efficiently.  
5. **Hash join** – Hashes both relations on join key; uses hash buckets to find matching tuples; efficient for equality joins.  

Choice depends on size of relations, indexes, memory, and join type (equi-join, natural join, etc.).  

---

#### **8. Why are SQL queries converted into relational algebra?**  

- **Formal foundation** – Relational algebra provides a precise mathematical model for query execution.  
- **Optimization** – Query optimizers transform SQL into relational algebra expressions to apply equivalence rules and choose efficient execution plans.  
- **Intermediate representation** – Acts as a bridge between high-level SQL and low-level execution primitives.  
- **Easier manipulation** – Algebra trees can be reordered, simplified, and restructured to improve performance.  
- **System independence** – Allows DBMS to implement physical operations (join algorithms) independently of SQL syntax.