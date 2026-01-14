These are the main physical methods a DBMS uses to implement a **JOIN** between two relations (R) and (S) on condition
(R.A = S.B).

---

### 1. **Nested-loop join (Brute force)**

Idea: Compare every record of (R) with every record of (S).

Algorithm:

* For each tuple (t) in (R)

  * For each tuple (s) in (S)

    * If (t[A] = s[B]), output ((t,s))

Cost:

* If (R) has (n) records and (S) has (m) records → $(O(n \times m))$

Advantages:

* Very simple
* Works even without indexes or sorting

Disadvantages:

* Very slow for large relations

Use when:

* One relation is very small
* No indexes are available

---

### 2. **Single-loop join (Index-based join)**

Idea: Use an index (or hash key) on one of the join attributes, usually on (S.B).

Algorithm:

* For each tuple (t) in (R)

  * Use the index on (S.B) to directly find all tuples (s) such that
    (s[B] = t[A])
  * Output matching pairs

Cost:

* $(O(n \times \text{index access cost}))$

Advantages:

* Much faster than nested-loop join
* Avoids scanning entire (S) for each tuple

Disadvantages:

* Requires an index or hash structure

Use when:

* An index exists on one join attribute

---

3. **Sort-merge join**

Idea: Sort both relations on the join attributes and then merge them like merging two sorted lists.

Algorithm:

1. Sort (R) on (A) and (S) on (B)
2. Scan both files simultaneously:

   * If (R.A < S.B) → move in (R)
   * If (R.A > S.B) → move in (S)
   * If (R.A = S.B) → output all matching pairs

Cost:

* Sorting: $(O(n \log n + m \log m))$
* Merging: $(O(n + m))$

Advantages:

* Very efficient for large datasets
* Each file is scanned only once after sorting

Disadvantages:

* Sorting is expensive if data is not already sorted
* Slightly more complex when attributes are non-keys (duplicates exist)

Use when:

* Files are already sorted
* Or sorting is acceptable

---

4. **Hash join**

Idea: Use hashing to group matching values into the same bucket.

Algorithm:

1. Choose the smaller relation (say (R)) and hash it:

   * For each tuple in (R), compute
     (h(R.A)) and place it in a bucket
2. Scan (S):

   * For each tuple in (S), compute
     (h(S.B))
   * Go to that bucket and match with all tuples of (R) in that bucket

Cost:

* Approximately $(O(n + m))$

Advantages:

* One of the fastest join methods
* No need to sort data

Disadvantages:

* Needs enough memory for hash tables
* Performance depends on good hash function

Use when:

* Large unsorted relations
* Equality joins
* Memory is available

---

### Quick Comparison

| Method      | Speed     | Needs Index | Needs Sorting | Best Use Case             |
| ----------- | --------- | ----------- | ------------- | ------------------------- |
| Nested-loop | Slow      | No          | No            | Small tables              |
| Single-loop | Fast      | Yes         | No            | Indexed join              |
| Sort-merge  | Fast      | No          | Yes           | Sorted data               |
| Hash join   | Very fast | No          | No            | Large data, equality join |

---

In practice:

* **Hash join** and **Sort-merge join** are preferred for large datasets.
* **Index join** is great when indexes exist.
* **Nested-loop join** is mostly used as a fallback or for very small relations.
