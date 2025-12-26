# UNIT 2: Algorithms for Query Processing and Optimization

---

## 1️⃣ Introduction to Query Processing

### 📘 What slide says (Exam version)

* Query processing deals with **execution of SQL queries**.
* **Query optimization** is the process of choosing the **best execution strategy**.
* Queries have two internal representations:

  * **Query Tree**
  * **Query Graph**

**Exam line:**
Query optimization minimizes query execution cost.

---

### 🧠 Simple explanation (Understand this)

When you write a SQL query, the database **does NOT execute it directly**.
It first:

1. Thinks of **different ways** to execute it
2. Chooses the **fastest and cheapest** way

Think like Google Maps:

* Many routes exist
* DB chooses the **shortest path**

Query Tree = step-by-step plan
Query Graph = relationship view (no order)

---

## 2️⃣ Translating SQL Queries into Relational Algebra

### 📘 Exam version (from slides)

* A **query block** is the basic unit of a SQL query.
* It contains:

  * SELECT
  * FROM
  * WHERE
  * GROUP BY
  * HAVING
* Nested queries are **separate query blocks**.
* Aggregate functions require **extended relational algebra**.
* SQL is translated using:

  * σ (selection)
  * π (projection)

---

### 🧠 Simple explanation

SQL is **high-level** (easy for humans).
Database understands **Relational Algebra** (machine-friendly).

So DB:

* Breaks query into **blocks**
* Converts each block into:

  * Filter (σ)
  * Column selection (π)

Nested query = solve inside query first → use result in outer query.

---

## 3️⃣ Algorithms for External Sorting

### 📘 Exam version

* External sorting is used for **large files** that do not fit in memory.
* Uses **Sort-Merge strategy**.
* Two phases:

  1. Sorting phase → create sorted runs
  2. Merging phase → merge runs
* Important terms:

  * $n_R$ → number of runs
  * $b$ → blocks
  * $n_B$ → buffers
  * $n_P$ → passes

---

### 🧠 Simple explanation

Imagine sorting **1 crore records** but RAM can hold only **1000**.

So DB:

1. Sorts **small chunks** (runs)
2. Saves to disk
3. Merges them slowly

Like sorting exam copies in groups, then merging piles.

---

## 4️⃣ Algorithms for SELECT Operation (MOST IMPORTANT)

### 📘 Exam version (from slides)

Selection retrieves records satisfying a condition.

**Search methods:**

* S1: Linear search
* S2: Binary search (ordered key)
* S3: Primary index / hash (unique)
* S4: Primary index (range)
* S5: Clustering index
* S6: Secondary (B+ tree) index
* S7: Conjunctive using one index
* S8: Conjunctive using Composite index
* S9: Intersection of record pointers

---

### 🧠 Simple explanation

SELECT is just **filtering rows**.

DB asks:

* Is file ordered?
* Is index available?
* Is condition equality or range?

Then it chooses:

* No index → scan everything (slow)
* Index → jump directly (fast)

S1–S9 are just **different shortcuts**.

---

## 5️⃣ Algorithms for JOIN Operations

### 📘 Exam version

Join types:

* Equi join
* Natural join
* Two-way join
* Multi-way join

Join methods:

* J1: Nested loop join
* J2: Index-based join
* J3: Sort-merge join
* J4: Hash join

Performance factors:

* Buffer space
* Join selectivity
* Inner vs outer relation

---

### 🧠 Simple explanation

JOIN = matching rows from two tables.

Bad way:

* Compare every row with every row (nested loop 😖)

Good ways:

* Sort both → merge
* Hash both → match buckets

Hash join is fastest when equality condition exists.

---

## 6️⃣ PROJECT and SET Operations

### 📘 Exam version

PROJECT:

* Removes unwanted attributes
* Removes duplicates if no key exists

Duplicate removal:

1. Sorting
2. Hashing

SET operations:

* UNION
* INTERSECTION
* SET DIFFERENCE
* CARTESIAN PRODUCT

---

### 🧠 Simple explanation

PROJECT = selecting columns
SET = mathematical set operations

Cartesian product = every row with every row
→ **very dangerous** 😅
(DB tries to avoid it)

---

## 7️⃣ Aggregate Operations and Outer Joins

### 📘 Exam version

Aggregate functions:

* MIN, MAX, SUM, COUNT, AVG

Implementation:

* Table scan
* Index-based

GROUP BY:

* Sorting or hashing
* Clustering index improves performance

Outer joins:

* LEFT
* RIGHT
* FULL

---

### 🧠 Simple explanation

Aggregate = calculations on data.

If index exists:

* DB reads only index (fast)

Outer join:

* Normal join removes unmatched rows
* Outer join **keeps them with NULL**

---

## 8️⃣ Combining Operations using Pipelining

### 📘 Exam version

* Avoids storing intermediate results
* Output of one operator passed directly to next
* Also called stream-based processing
* Reduces disk I/O

---

### 🧠 Simple explanation

Instead of:

* SELECT → save
* JOIN → save
* PROJECT → save

DB does:

* SELECT → immediately JOIN → immediately PROJECT

Like water flowing through pipes 🚰

---

## 9️⃣ Heuristic Query Optimization

### 📘 Exam version

Heuristic rules:

1. Apply SELECT early
2. Apply PROJECT early
3. Execute most restrictive operations first

Query tree:

* Leaf nodes = relations
* Internal nodes = operators

---

### 🧠 Simple explanation

Common sense rules:

* Filter early
* Reduce data early
* Smaller data → faster joins

Heuristics = smart guessing (no calculations).

---

## 🔟 Cost-Based Query Optimization

### 📘 Exam version

* Estimates cost of different plans
* Chooses lowest cost
* Cost components:

  * Disk I/O
  * CPU
  * Memory
  * Communication
* Uses catalog statistics

---

### 🧠 Simple explanation

DB **calculates cost** before executing.

Like planning a trip by:

* Distance
* Fuel
* Time

More accurate than heuristics, but slower.

---

## 1️⃣1️⃣ Semantic Query Optimization

### 📘 Exam version

* Uses database constraints
* Rewrites or eliminates queries
* Can detect empty results

---

### 🧠 Simple explanation

DB uses **logic**.

If rule says:
“No employee earns more than manager”

Then query asking that → result is **always empty**
→ DB skips execution entirely 😎

---
