### 🔷 Data Cube Computation Methods (Simple + Exam Ready)

Data warehouses store very large data.
OLAP queries must be answered in **seconds**, so cube computation must be **fast and efficient**.

There are mainly **two methods**:

1. **Multiway Array Aggregation (MultiWay)** → used for **full cube**
2. **BUC (Bottom-Up Construction)** → used for **iceberg cube**

---

## 1️⃣ Multiway Array Aggregation (MultiWay)

Used to compute **FULL DATA CUBE**

Idea:
Compute many cuboids **at the same time** using a multidimensional array.

Steps:

1. Store data in an **n-dimensional array**.
2. Divide the array into small parts called **chunks**.
3. Each chunk fits into memory.
4. While scanning one chunk, compute:

   * 3-D cuboid
   * 2-D cuboids
   * 1-D cuboids
     all together (simultaneous aggregation).

That is why it is called **Multiway**.

Example:
For dimensions A, B, C:
MultiWay computes all cuboids:

```
ABC, AB, AC, BC, A, B, C, ()
```

When scanning chunk (a0 b0 c0), it computes:

* a0b0c0 → ABC
* b0c0 → BC
* a0c0 → AC
* a0b0 → AB
  in **one scan**.

✔ Fast
✔ Avoids repeated scanning
❌ Works well only when dimensions are **few**
❌ Memory expensive

Exam line:

> Multiway array aggregation computes the full data cube using multidimensional arrays and chunking, performing simultaneous aggregation on multiple dimensions.

---

## 2️⃣ BUC (Bottom-Up Construction)

Used to compute **Iceberg Cubes** (only frequent cells).

Idea:
Build cube from **top to bottom** using **minimum support pruning**.

Starts from:

```
(*, *, *, *)   ← apex cuboid
```

and goes downward to:

```
(A, B, C, D)
```

Uses **Apriori property**:

> If a cell does not satisfy minimum support, none of its descendants can satisfy it.

Steps:

1. Compute count of all → (*,*,*,*)
2. Partition on first dimension (say A):

   * (a1,*,*,*)
   * (a2,*,*,*)
3. Check each against min_sup:

   * If count < min_sup → prune
   * If count ≥ min_sup → go deeper
4. Partition further on B, then C, then D
5. Continue recursively

If:

```
minsup = 1
```

Then BUC computes the **FULL CUBE**

✔ Best for sparse data
✔ Saves time by pruning
✔ Ideal for iceberg cube
❌ Not best for dense/full cube

Exam line:

> BUC computes iceberg cubes by constructing the cube from the apex downward using minimum support and pruning unpromising partitions.

---

## 🔁 Comparison (For Quick Revision)

| Feature              | MultiWay                       | BUC                       |
| -------------------- | ------------------------------ | ------------------------- |
| Computes             | Full Cube                      | Iceberg Cube              |
| Approach             | Array + chunks                 | Recursive + pruning       |
| Speed                | Very fast for small dimensions | Very fast for sparse data |
| Uses Apriori pruning | ❌ No                           | ✅ Yes                     |
| Memory use           | High                           | Low                       |

---

## 🧠 One-line memory trick:

```
MultiWay → Full cube → Chunk + Array  
BUC → Iceberg cube → Prune + Recursive
```

---

## ✍️ Short Exam Answer

> Data cube computation requires efficient methods due to large data volumes. Two important methods are:
>
> 1. **Multiway Array Aggregation**, which computes the full cube using multidimensional arrays and chunking, performing simultaneous aggregation on many dimensions.
>
> 2. **BUC (Bottom-Up Construction)**, which computes iceberg cubes by starting from the apex cuboid and recursively partitioning dimensions while pruning cells that do not satisfy minimum support using the Apriori property.
