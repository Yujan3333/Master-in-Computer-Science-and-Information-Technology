### **Motivation for Pipelining in Query Processing**

When a query is executed, it is usually **translated into a sequence of operations** (selection, join, projection, aggregation, etc.).

---

## **Problem with Traditional Execution**

* Each operation generates a **temporary result** stored on disk.
* These temporary files are:

  * Time-consuming to create
  * Expensive in terms of **I/O**
* For large datasets, writing and reading intermediate results can dominate the query execution time.

---

## **Solution: Pipelining**

**Idea:** Avoid writing intermediate results to disk whenever possible.

* Pass the **output of one operator directly as input** to the next operator.
* Operators process **tuples as they arrive**, rather than waiting for the entire previous operation to finish.
* This is also called **stream-based processing**.

---

### **Example: 2-Way Join with Selections and Projection**

Suppose the query:

```sql
SELECT A, B
FROM R, S
WHERE R.x = S.y AND R.z > 10 AND S.w < 50;
```

1. Operations:

   * Selection on `R` (`R.z > 10`)
   * Selection on `S` (`S.w < 50`)
   * Join `R ⋈ S`
   * Projection (`π A, B`)

2. **Without pipelining:**

   * Execute selection on `R` → write TEMP1
   * Execute selection on `S` → write TEMP2
   * Join TEMP1 and TEMP2 → write TEMP3
   * Project TEMP3 → final result

> Multiple temporary files → costly I/O

3. **With pipelining:**

   * **R tuples satisfying `R.z > 10`** are immediately fed into the join operator.
   * **S tuples satisfying `S.w < 50`** are also streamed into the join.
   * Join results are immediately passed to the projection.
   * No intermediate files are written to disk.

---

### **Advantages of Pipelining**

| Benefit            | Explanation                                          |
| ------------------ | ---------------------------------------------------- |
| Reduces I/O        | Temporary files are minimized or eliminated          |
| Faster execution   | Operators work simultaneously, tuple by tuple        |
| Lower storage cost | No need to allocate space for intermediate results   |
| Stream-based       | Suitable for large datasets and real-time processing |

---

### **Key Idea**

> Operators are chained together in a **pipeline**, allowing data to **flow continuously** from one operation to the next, instead of waiting for the completion of each step.

This is especially effective for:

* **Selections + Joins**
* **Selections + Aggregates**
* Any sequence of operations where results can be **produced tuple-by-tuple**.

---
