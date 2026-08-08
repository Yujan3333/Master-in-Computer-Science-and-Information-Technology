### 1. Sorting, Hashing, and Grouping

Idea:
Group similar records together so aggregation becomes easy.

Explanation:

* Cube computation needs to aggregate tuples that have the same dimension values.
* Sorting or hashing helps bring similar tuples together.
* Grouping reduces repeated scanning of data.

Example:
To compute **total sales by (branch, day, item)**:

* First sort data by *branch*
* Then by *day*
* Then group by *item*
  This makes aggregation faster.

Exam line:

> Sorting, hashing, and grouping reorder data so that tuples with the same dimension values are clustered, making aggregation efficient.

---

### 2. Simultaneous Aggregation and Caching Intermediate Results

Idea:
Reuse already computed results instead of going back to raw data.

Explanation:

* Compute higher-level cuboids from lower-level cuboids.
* Store (cache) intermediate results.
* This reduces expensive disk I/O.

Example:
To compute:

* Sales by **branch**,
  Instead of using the base table, use:
* Sales by **branch and day** cuboid.

Exam line:

> Higher-level aggregates are computed from lower-level aggregates and cached intermediate results to reduce computation and disk access.

---

### 3. Aggregation from the Smallest Child Cuboid

Idea:
Choose the smallest data source to compute faster.

Explanation:

* A parent cuboid may have many child cuboids.
* Always choose the child with fewer records.

Example:
To compute:
$C_{branch}$

Given:

* $C_{branch,year}$ (small, few years)
* $C_{branch,item}$ (large, many items)

Use:

* $C_{branch,year}$ because it is smaller.

Exam line:

> When multiple child cuboids exist, compute a parent cuboid from the smallest child to minimize computation.

---

### 4. Apriori Pruning for Iceberg Cubes

Idea:
If a cell is useless, don’t explore its detailed versions.

Explanation:

* If a cube cell does not satisfy minimum support (e.g., sales < 100),
* Then its more detailed cells will also not satisfy it.
* So we stop computing them.

This saves huge computation.

Example:
If:

```
Sales(branch = A) < 100
```

Then:

```
Sales(branch = A, item = X) < 100
Sales(branch = A, item = Y) < 100
```

So no need to compute them.

Exam line:

> Using the Apriori property, if a cell does not satisfy minimum support, all its descendants are pruned, making iceberg cube computation efficient.

---

### Short Exam Summary

| Technique                    | One-line Meaning                                 |
| ---------------------------- | ------------------------------------------------ |
| Sorting, Hashing, Grouping   | Cluster similar data to make aggregation faster  |
| Caching Intermediate Results | Reuse lower-level cuboids to compute higher ones |
| Smallest Child First         | Use the smallest cuboid for aggregation          |
| Apriori Pruning              | Stop computing useless low-support cells         |

---

Memory trick:

```
Group smart → Reuse results → Choose smallest → Prune useless
```
