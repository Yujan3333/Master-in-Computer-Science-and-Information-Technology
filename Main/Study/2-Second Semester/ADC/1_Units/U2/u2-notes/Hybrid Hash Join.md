### Hybrid Hash Join

Hybrid hash join is an optimization of **Partitioned Hash Join**.
The main idea is: *we start joining one partition while we are still partitioning*, so we save one extra read/write for that partition.

It has the same two phases, but they slightly overlap.

---

## 1. Partitioning Phase

Assume:

* $R$ = smaller relation
* $S$ = larger relation
* $M$ = number of available buffer blocks

Buffer allocation:

* 1 block for each of $(M-1)$ partitions: $R_2, R_3, \dots, R_M$
* Remaining blocks (say $k$ blocks) are assigned to partition $R_1$

So:

* $R_1$ is treated specially → it is kept mostly in memory
* Other partitions are written to disk as usual

Steps:

1. Scan relation $R$ (smaller one):

   * Hash tuples into $M$ partitions using hash function $h_1$
   * Partitions $R_2, R_3, \dots, R_M$ go to disk
   * Partition $R_1$ is kept in memory using the extra buffers

2. Scan relation $S$:

   * Hash tuples using the same $h_1$
   * For tuples belonging to:

     * $S_1$: directly join them with in-memory $R_1$
     * $S_2, S_3, \dots, S_M$: write them to disk

While scanning $S$, the join of $R_1 \bowtie S_1$ is already being performed.

So by the end of the partitioning phase:

* The result of $R_1 \bowtie S_1$ is already written to disk
* Other partitions are ready for later joining

---

## 2. Joining Phase

Now only $M-1$ partitions remain:

For $i = 2$ to $M$:

1. Load partition $R_i$ into memory
2. Build an in-memory hash table on $R_i$ using hash function $h_2$
3. Scan $S_i$ and probe the hash table
4. Output matching tuples

This requires:

* $M-1$ iterations instead of $M$

Because:

* Partition 1 has already been joined during partitioning

---

## Why Hybrid Hash Join is Better

Compared to Partitioned Hash Join:

| Feature                    | Partitioned Hash Join   | Hybrid Hash Join    |
| -------------------------- | ----------------------- | ------------------- |
| Join start                 | After full partitioning | During partitioning |
| Disk I/O for one partition | Yes                     | No                  |
| Number of join iterations  | $M$                     | $M-1$               |
| Performance                | Good                    | Better              |

Hybrid hash join saves:

* One full write and read of partition 1
* Time by overlapping partitioning and joining

---

## Intuition

Think of it like this:

> Instead of writing all partitions to disk and then starting joins,
> we keep one partition in memory and immediately join it while scanning the other relation.

This makes Hybrid Hash Join faster and more efficient than the normal partitioned hash join.
