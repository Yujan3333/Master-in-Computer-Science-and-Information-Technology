### 1. Full Cube

A **full cube** stores **all cuboids and all their cells**.

* Every possible aggregation is pre-computed
* Fastest query answering
* Requires very large storage

Exam line:

> A full cube contains all the pre-computed cells of all possible cuboids in the data cube.

---

### 2. Iceberg Cube

An **iceberg cube** stores only those cells whose measure value satisfies a given condition
(like minimum support or threshold).

Example:
Store only sales records where
`sales ≥ 100`

* Small in size
* Removes insignificant data
* Useful when we care only about large values

Exam line:

> An iceberg cube contains only those cube cells whose measure values satisfy a given minimum threshold.

---

### 3. Closed Cube

A **closed cube** removes redundant cells.

A cell C is **closed** if:

* There is no more detailed cell D
* Such that D has the **same measure value** as C

Meaning:
If more detailed data gives the same result, higher level data is unnecessary.

Example idea:
If
Sales of *Electronics* = 500
Sales of *Mobile + Laptop + TV* = 500
Then Electronics is **not closed** (because its children give same result).

Exam line:

> A closed cube contains only closed cells, where no descendant cell has the same measure value, thus removing redundancy.

---

4. Cube Shell

Instead of computing all dimensions, compute only cuboids with **few dimensions** (like 3–5).

* Reduces computation cost
* Useful when full cube is too large

Exam line:

> A cube shell is formed by pre-computing only those cuboids that involve a small number of dimensions.

---

Easy comparison:

| Type         | Stores What?                           | Size       | Use                       |
| ------------ | -------------------------------------- | ---------- | ------------------------- |
| Full cube    | All cuboids and all cells              | Very large | Maximum speed             |
| Iceberg cube | Only important cells (threshold-based) | Small      | Focus on significant data |
| Closed cube  | Only non-redundant cells               | Smaller    | Remove redundancy         |
| Cube shell   | Only low-dimension cuboids             | Medium     | Save computation          |

---

One-line memory trick:

* **Full cube** → everything
* **Iceberg cube** → only big values
* **Closed cube** → no redundancy
* **Cube shell** → only small-dimension views
