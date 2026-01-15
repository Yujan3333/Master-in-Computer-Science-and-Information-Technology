
- [What if we have a Clustering Index on the GROUP BY attribute❓](#What%20if%20we%20have%20a%20Clustering%20Index%20on%20the%20GROUP%20BY%20attribute❓)

### Aggregate operators:

* MIN
* MAX
* SUM
* COUNT
* AVG

They can be implemented mainly in two ways:

1. **Table Scan**
2. **Using Index**

---

## 1. Using Table Scan

Scan all tuples of the relation and maintain running values.

Example for:

```sql
SELECT MAX(SALARY)
FROM EMPLOYEE;
```

Algorithm:

* Initialize `max = -∞`
* For each tuple:

  * If `SALARY > max`, update `max`
* At the end, output `max`

Similarly:

* `SUM`: keep running sum
* `COUNT`: increment counter
* `AVG`: compute `SUM / COUNT`

Cost: one full scan of the table.

---

## 2. Using Index

Indexes can make aggregates much faster.

### Example: MAX using an ascending index

If an **ascending B+ tree index** exists on `SALARY`:

To find:

```sql
SELECT MAX(SALARY)
FROM EMPLOYEE;
```

We:

* Start at the root
* Follow the **rightmost pointer** at each internal node
* Reach the rightmost leaf
* The last key in that leaf is the maximum salary

Cost:

* $O(\text{height of index})$
  Much cheaper than a full table scan.

Similarly:

* For `MIN`: follow leftmost pointers

---

## SUM, COUNT, AVG using Index

### (a) Dense Index

Dense index → each record has one index entry.

So:

* Each index entry corresponds to exactly one tuple.
* We can directly compute aggregates by scanning the index:

For example:

```sql
SELECT SUM(SALARY) FROM EMPLOYEE;
```

Algorithm:

* Scan all index entries
* Add up the salary values stored in the index
* COUNT = number of index entries
* AVG = SUM / COUNT

This avoids accessing the actual table.

---

### (b) Non-dense Index

Non-dense index → one index entry points to a *block* of records.

So:

* One index entry may represent many tuples.
* We must account for the number of records in each block.

For example:

* If an index entry points to a block containing 50 records,
  then:

  * COUNT increases by 50
  * SUM increases by sum of salaries of those 50 records

Hence, data blocks must still be accessed to:

* Count actual records
* Add real attribute values

---

## Aggregates with GROUP BY

Example:

```sql
SELECT DEPT, AVG(SALARY)
FROM EMPLOYEE
GROUP BY DEPT;
```

Steps:

1. Partition the relation by group attributes (here `DEPT`) using:

   * Sorting, or
   * Hashing

2. For each group:

   * Compute the aggregate separately:

     * Maintain SUM and COUNT for each group
     * AVG = SUM / COUNT

So:

* Sorting-based grouping:

  * Sort by group attribute(s)
  * Process one group at a time
* Hash-based grouping:

  * Hash tuples by group attribute(s)
  * Each bucket is one group

---

## What if we have a Clustering Index on the GROUP BY attribute❓

This is the **best case**.

Clustering index means:

* Tuples with the same group attribute value are stored **contiguously** on disk.

So for:

```sql
SELECT DEPT, AVG(SALARY)
FROM EMPLOYEE
GROUP BY DEPT;
```

With a clustering index on `DEPT`:

Algorithm:

1. Scan the file in order of `DEPT`
2. All tuples of one department appear together
3. Compute aggregate for the current group
4. When `DEPT` changes:

   * Output result for previous group
   * Reset counters
   * Start for the new group

No sorting or hashing is required.

Cost:

* Just one sequential scan of the file
* Very efficient

---

## Summary Table

| Situation                      | Best Implementation                           |
| ------------------------------ | --------------------------------------------- |
| MIN / MAX                      | Use B+ tree index (leftmost / rightmost path) |
| SUM, COUNT, AVG (no GROUP BY)  | Dense index scan or table scan                |
| SUM, COUNT, AVG with GROUP BY  | Sorting or hashing                            |
| GROUP BY with clustering index | Single sequential scan, no extra cost         |

This is why database optimizers strongly prefer **clustering indexes on GROUP BY attributes** when aggregates are frequent.
