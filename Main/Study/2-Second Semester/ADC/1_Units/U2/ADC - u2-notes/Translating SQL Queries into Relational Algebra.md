### 2.2 Translating SQL Queries into Relational Algebra (Simple Explanation)

Think of **SQL** as a language we use to *ask* questions to a database, and **Relational Algebra (RA)** as the *mathematical language* that explains *how* those questions are actually processed.

A **Query Block** is the smallest part of an SQL query that can be converted into relational algebra.
It contains:

* `SELECT`
* `FROM`
* `WHERE`
* optionally `GROUP BY` and `HAVING`

If an SQL query has subqueries (nested queries), each of them is treated as a **separate query block**.

Example:

```sql
SELECT name 
FROM Student 
WHERE age > 20;
```

This is one query block.

If we have:

```sql
SELECT name 
FROM Student 
WHERE dept_id IN (SELECT dept_id FROM Department WHERE location='KTm');
```

Now there are **two query blocks**:

1. Outer query
2. Inner query

Each is translated separately into relational algebra.

Why do we translate SQL into Relational Algebra?

1. **Easy to understand complex queries**

   * SQL can become very long and confusing.
   * Relational algebra expresses the same query using simple operators like:

     * Selection (σ)
     * Projection (π)
     * Join (⨝)
   * This makes logic clearer.

2. **Mathematical and formal**

   * Relational algebra has strict rules.
   * This ensures queries are **correct and consistent**.

3. **Standard representation**

   * Different SQL queries that mean the same thing can be converted into the same RA form.
   * This helps DBMS treat them uniformly.

4. **Query optimization**

   * DBMS compares different RA expressions and chooses the fastest one.
   * Example: deciding whether to filter first or join first to reduce data size.

So:

> SQL = What user writes
> Relational Algebra = How DBMS understands and optimizes it

---

### 2.3 Algorithms for External Sorting (Easy Explanation)

External sorting is used when:

> The data is **too large to fit into main memory (RAM)** and is stored on disk.

So we cannot sort everything at once like normal sorting.
We use **Sort-Merge strategy**, which works in **two phases**.

---

### Phase 1: Sorting Phase (Create Sorted Runs)

1. Break the big file into **small chunks** that fit into memory.
2. For each chunk:

   * Read it into memory
   * Sort it
   * Write it back to disk as a **sorted subfile (run)**

If:

* `b` = total number of disk blocks
* `nB` = number of blocks that fit in memory

Then number of initial runs:
$$
nR = \lceil b / nB \rceil
$$

Meaning:

> How many small sorted pieces we will create.

Example:
If `b = 1000` blocks, and memory can hold `nB = 100` blocks:
$$
nR = \lceil 1000/100 \rceil = 10
$$
So we get **10 sorted runs**.

---

### Phase 2: Merging Phase (Combine Runs)

Now we merge these sorted runs step by step until only one fully sorted file remains.

In merging:

* One buffer is used for output.
* Remaining buffers are used to read runs.

So maximum runs merged at once:
$$
dM = \min(nB - 1, nR)
$$

Meaning:

> How many runs we can merge in one pass.

Example:
If `nB = 6`, then:
$$
dM = 6 - 1 = 5
$$
So we can merge **5 runs at a time**.

---

### Number of Merge Passes

Number of passes needed:
$$
nP = \lceil \log_{dM}(nR) \rceil
$$

This tells:

> How many rounds of merging are needed to finish sorting.

Example:
If:

* `nR = 25`
* `dM = 5`

Then:
$$
nP = \lceil \log_5(25) \rceil = \lceil 2 \rceil = 2
$$

So it takes **2 merge passes**.

---

### In short:

| Term               | Meaning                                            |
| ------------------ | -------------------------------------------------- |
| Query Block        | Smallest SQL part converted to relational algebra  |
| Relational Algebra | Mathematical way to represent and optimize queries |
| External Sorting   | Sorting when data is too big for memory            |
| Sorting Phase      | Break data → sort chunks → write sorted runs       |
| Merging Phase      | Combine sorted runs into one                       |
| nR                 | Number of initial sorted runs                      |
| dM                 | How many runs can be merged at once                |
| nP                 | How many merge passes are needed                   |

---

You can remember it like this:

> **Relational Algebra** helps the database *think clearly*.
> **External Sorting** helps the database *handle very large data efficiently*.
