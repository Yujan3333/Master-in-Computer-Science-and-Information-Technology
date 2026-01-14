## 2.8 Using Heuristics in Query Optimization

Before executing a query, the DBMS converts it into a **query tree** and improves it using **heuristic rules**.

### Query Tree

* A tree representation of a relational algebra expression.
* Leaf nodes → relations (tables).
* Internal nodes → operators (σ selection, π projection, ⋈ join, etc.).
* Execution is **bottom–up**: leaves → internal nodes → root gives final result.
* Different trees represent different execution strategies for the same query.

### Query Graph

* Nodes → relations (tables).
* Edges → conditions (joins, WHERE predicates).
* Shows **what is connected to what**, not **how to execute**.
* More abstract and simpler than query trees.

Many query trees can be generated for one query.
Goal of heuristic optimization → choose the tree that produces the **smallest intermediate results** and is cheapest to execute.

---

### Heuristic Rules

#### 1. Apply size-reducing operations early

* Perform **selection (σ)** and **projection (π)** before **join (⋈)**.
* Smaller relations → faster joins.

#### 2. Push selections and projections down the tree

* Selection early → reduces number of tuples (rows).
* Projection early → reduces number of attributes (columns).

#### 3. Execute the most restrictive operations first

* Apply conditions that filter out most tuples earlier.
* Quickly reduces intermediate relation sizes.

---

## 2.9 Using Selectivity and Cost Estimates

### Query Execution Plan

Query execution plan = Query tree +

* Access methods (table scan, index scan, etc.)
* Join algorithms (nested loop, hash join, sort-merge join, etc.)

---

### Evaluation Styles

#### 1. Materialized Evaluation

* Each operator stores its output in a temporary table on disk.
* More disk I/O, slower.

#### 2. Pipelined Evaluation

* Output of one operator is directly passed to the next.
* Less disk I/O, faster.

---

### Cost-Based Query Optimization

* Generate many possible execution plans.
* Estimate the cost of each plan.
* Choose the plan with **minimum estimated cost**.

#### Problems

* Cost estimation must be accurate.
* Requires correct statistics.
* Search space becomes huge for complex queries.
* System conditions may change dynamically.

---

### Cost Components

1. Disk I/O cost
2. Storage cost
3. CPU computation cost
4. Memory usage cost
5. Communication cost (in distributed databases)

---

### Catalog Information Used

* Number of records: $r$
* Record size: $R$
* Number of blocks: $b$
* Blocking factor: $bfr$
* Index height: $x$
* Number of index blocks: $b_{I1}$
* Number of distinct values: $d$
* Selectivity: $sl$

Selection cardinality formula:

$$s=sl\times r$$

Meaning:

* $sl$ = fraction of tuples that satisfy a condition
* $r$ = total number of tuples
* $s$ = estimated number of selected tuples

---

## 2.10 Query Optimization in Oracle

Oracle uses two optimizers:

### 1. Rule-Based Optimizer (RBO)

* Uses fixed heuristic rules.
* Does not use statistics.
* Mostly obsolete.

### 2. Cost-Based Optimizer (CBO)

* Uses table and index statistics.
* Estimates cost of each execution plan.
* Chooses plan with minimum cost.
* Developers can use **hints** to influence plan choice.

---

## 2.11 Semantic Query Optimization

Uses **database constraints** and **data meaning** to simplify or avoid query execution.

### Example Query

```sql
SELECT E.LNAME, M.LNAME
FROM EMPLOYEE E, EMPLOYEE M
WHERE E.SUPERSSN = M.SSN
AND E.SALARY > M.SALARY;
```

Given constraint:

> No employee can earn more than their supervisor.

Analysis:

* Condition `E.SALARY > M.SALARY` is impossible.
* The query result is always **empty**.
* DBMS can skip executing the query completely.

Semantic optimization uses:

* Logic
* Theorem proving
* Knowledge of schema constraints

---

## One-Line Summary

* **Heuristic optimization** → applies rules to reduce intermediate data early.
* **Cost-based optimization** → uses statistics and formulas to choose cheapest plan.
* **Semantic optimization** → uses meaning and constraints to eliminate useless queries.
