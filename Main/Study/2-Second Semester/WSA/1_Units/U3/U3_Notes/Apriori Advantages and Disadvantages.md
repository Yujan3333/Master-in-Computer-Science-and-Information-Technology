Here’s a **clear, exam-friendly summary** of the **advantages and disadvantages of Apriori**:

---

## **Advantages of Apriori**

1. **Simple and Easy to Understand**

   * Conceptually straightforward and easy to implement.

2. **Strong Theoretical Foundation**

   * Based on the **Apriori property**: all subsets of a frequent itemset are also frequent.

3. **Level-wise Candidate Generation**

   * Generates itemsets in a systematic, **level-wise manner**.

4. **Good for Small Datasets**

   * Works well when the number of items and transactions is small.

5. **Foundation for Association Rule Mining**

   * Apriori is widely used as a base for generating **association rules**.

---

## **Disadvantages of Apriori**

1. **Multiple Database Scans**

   * Each iteration scans the whole database → slow for large datasets.

2. **Generates Many Candidate Itemsets**

   * Candidate explosion for large datasets → high computation cost.

3. **Inefficient for Large or Dense Data**

   * Performance degrades with more items or frequent patterns.

4. **Not Memory Efficient**

   * Needs to store many candidate itemsets in memory.

5. **Repeated Counting**

   * Counting support for candidates repeatedly adds overhead.

---

## **One-Line Exam Summary**

> Apriori is simple and theoretically strong but inefficient for large datasets due to multiple scans and candidate generation.

---
