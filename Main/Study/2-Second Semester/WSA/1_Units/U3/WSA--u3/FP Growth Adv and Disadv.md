Here are the **advantages and disadvantages of FP-tree (FP-Growth)** written in **simple, exam-friendly points**.

---

## **Advantages of FP-Tree**

1. **No candidate generation**

   * Unlike Apriori, FP-tree does not generate large candidate itemsets.

2. **Only two database scans**

   * One scan to find frequent items
   * One scan to build FP-tree
     → Faster for large datasets.

3. **Compact data structure**

   * Common prefixes are shared.
   * Reduces memory usage significantly.

4. **Efficient for dense datasets**

   * Performs well when many items are frequent.

5. **Faster mining of frequent patterns**

   * Uses pattern growth with conditional FP-trees instead of repeated scanning.

---

## **Disadvantages of FP-Tree**

1. **Complex to implement**

   * FP-tree structure and mining process are harder to understand and code.

2. **Memory overhead for tree structure**

   * Tree, header table, and node links consume memory.

3. **Not suitable for very sparse data**

   * Few shared prefixes → less compression.

4. **Tree reconstruction cost**

   * Conditional FP-trees must be built recursively, which can be expensive.

5. **Hard to update dynamically**

   * Inserting or deleting transactions requires rebuilding the FP-tree.

---

## **One-Line Exam Summary**

> FP-tree is an efficient structure for mining frequent patterns without candidate generation, but it is complex, memory-intensive, and difficult to update dynamically.
