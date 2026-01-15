## Partition Hash Join

Partition hash join is done in **two main phases**:

1. **Partitioning phase**
2. **Joining (Probing) phase**

Let

* $b_R$ = number of disk blocks of relation $R$
* $b_S$ = number of disk blocks of relation $S$
* $b_{RES}$ = number of disk blocks of the join result
* $M$ = number of partitions

---

## 1. Partitioning Phase

Each file $R$ and $S$ is divided into $M$ partitions using the **same hash function** on the join attributes.

$$R\rightarrow R_1,R_2,R_3,\dots,R_M$$
$$S\rightarrow S_1,S_2,S_3,\dots,S_M$$

Property:
If a tuple $r\in R$ matches a tuple $s\in S$, then both must go into the **same partition**:
$$h(r.A)=h(s.B)$$

Memory requirement:

* Minimum number of buffers = $M+1$

  * $M$ buffers → one for each partition
  * 1 buffer → input buffer

Process:

* Read each block of $R$, hash tuples into partitions $R_1,\dots,R_M$
* Read each block of $S$, hash tuples into partitions $S_1,\dots,S_M$
* Each partition is stored as a separate disk sub-file

Cost:

* Reading $R$ and $S$:
  $$b_R+b_S$$

* Writing partitioned files of $R$ and $S$:
  $$b_R+b_S$$

So partitioning phase cost:
$$2(b_R+b_S)$$

---

## 2. Joining (Probing) Phase

There are $M$ iterations, one for each partition pair $(R_i,S_i)$.

Assume:
$$|R_i|<|S_i|$$
so $R_i$ fits in memory.

For iteration $i$:

1. Copy all records of $R_i$ into memory buffers.
2. Build an in-memory hash table on $R_i$.
3. Read blocks of $S_i$ one at a time.
4. For each record in $S_i$, probe the hash table to find matching record(s) from $R_i$.
5. Write matching joined tuples into the result file.

Cost:

* Reading all partitions of $R$ and $S$ once:
  $$b_R+b_S$$

* Writing join result:
  $$b_{RES}$$

So joining phase cost:
$$(b_R+b_S)+b_{RES}$$

---

## Total Cost of Partition Hash Join

$$\text{Total Cost}=2(b_R+b_S)+(b_R+b_S)+b_{RES}$$

$$=3(b_R+b_S)+b_{RES}$$

$$\boxed{3(b_R+b_S)+b_{RES}}$$

---

## In simple words

| Phase        | What happens                               | Disk Cost                    |
| ------------ | ------------------------------------------ | ---------------------------- |
| Partitioning | Read and split $R$ and $S$ into partitions | $2(b_R+b_S)$                 |
| Joining      | Match corresponding partitions             | $(b_R+b_S)$                  |
| Output       | Write join result                          | $b_{RES}$                    |
| **Total**    |                                            | $\boxed{3(b_R+b_S)+b_{RES}}$ |

---

## Why this is efficient

* Each relation is read only **twice**:

  * Once for partitioning
  * Once for joining

* Matching is done only within small partitions.

* Works very well for **large, unsorted files**.

* One of the fastest JOIN algorithms used in DBMS.
