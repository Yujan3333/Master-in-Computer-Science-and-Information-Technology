When we do a **SELECT** operation in DBMS, our main goal is:

> Find only those records that satisfy the given condition, using the fastest possible way.

Different algorithms are used depending on:

* Whether the file is ordered
* Whether indexes exist
* Whether the condition is simple or complex

---

## 🔹 Search Methods for Simple Selection

Simple selection means only **one condition**, like:

```sql
SELECT * FROM Student WHERE roll = 10;
```

#### 1. **Linear Search (Brute Force)**

* Check every record one by one.
* Works always, but slow.
* Used when no index is available.

Example:
Search 10,000 records → check all 10,000.

---

#### 2. **Binary Search**

* Only works if:

  * File is **ordered**
  * Condition is on a **key attribute**
  * Equality condition (=)
* Much faster than linear search.

Example:
Searching roll = 50 in a sorted file.

---

#### 3. **Using Primary Index or Hash Key (Single Record)**

* Condition: equality on a **key attribute**
* Very fast.
* Directly jumps to the record.

Example:

```sql
WHERE roll = 101
```

---

#### 4. **Using Primary Index (Multiple Records)**

* Condition: `>`, `<`, `>=`, `<=` on key attribute.
* First find the starting point using index.
* Then read all matching records in order.

Example:

```sql
WHERE roll > 50
```

---

#### 5. **Using Clustering Index**

* On **non-key attribute** with many duplicates.
* Records with same value are stored together.
* Good for:

```sql
WHERE department = 'CSE'
```

---

#### 6. **Using Secondary (B+-Tree) Index**

* Can be on key or non-key attribute.
* Supports:

  * Equality
  * Range queries (`>`, `<`, etc.)
* Returns pointers to records.

Example:

```sql
WHERE name = 'Ram'
WHERE age > 20
```

---

#### 7. **Conjunctive Selection using Individual Index**
   Condition with **AND**:

```sql
WHERE dept='CSE' AND age > 20
```

* Use index on one attribute.
* Retrieve records.
* Then check remaining conditions manually.

---

#### 8. **Conjunctive Selection using Composite Index**
   If composite index exists on:

```text
(dept, age)
```

Then directly search:

```sql
WHERE dept='CSE' AND age=21
```

This is very fast.

---

## 🔹 Search Methods for Complex Selection

### S9: Conjunctive Selection by Intersection of Record Pointers

Used when:

* Secondary indexes exist on multiple attributes
* Each index gives **record pointers**

Example:

```sql
WHERE dept='CSE' AND city='Kathmandu'
```

Steps:

1. Use index on `dept` → get list of record pointers.
2. Use index on `city` → get another list.
3. Take **intersection** of both lists.
4. Retrieve only common records.

This avoids scanning unnecessary records.

---

## 🔹 General Rules for SELECT Implementation

1. If only **one condition**:

   * Check if index exists.
   * If yes → use it.
   * If no → use linear search (S1).

2. If **multiple conditions (AND)**:

   * Use the most selective index (which returns fewest records).
   * Or use pointer intersection (S9) if possible.

3. Query optimizer decides:

> Which method is cheapest in terms of I/O and time.

---

## 🔹 Disjunctive Selection (OR condition)

Example:

```sql
WHERE dept='CSE' OR city='Pokhara'
```

Possible strategies:

* Use index on `dept`, get records.
* Use index on `city`, get records.
* Take **union** of both result sets.
* Remove duplicates.

If no index exists → full table scan.

---

## In short (Memory Trick):

| Situation             | Best Method                    |
| --------------------- | ------------------------------ |
| No index              | Linear search                  |
| Ordered key, equality | Binary search                  |
| Key + index           | Primary index                  |
| Non-key, grouped      | Clustering index               |
| Any attribute         | Secondary index                |
| AND conditions        | Use best index or intersection |
| OR conditions         | Use union of results           |
| Composite attributes  | Composite index                |

---

So:

> SELECT algorithms try to **avoid reading the whole file**, and instead use **indexes** and **smart combinations** to reach only the needed records efficiently.
