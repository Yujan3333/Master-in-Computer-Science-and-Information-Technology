## **1. Hashing Overview**

* **Hash function (randomizing function):** maps a record’s hash field value to a disk block address.
* **Hash file:** storage organization created by applying a hash function to records.
* **Main use:** efficient equality searches on a key field.
* **Goal of a good hash function:** uniform distribution to minimize collisions.

---

## **2. Internal Hashing (In-Memory)**

* Uses a **hash table (array of records)** with `M` slots (0 to M-1).

* **Hash function example:**
  $$
  h(K) = K \mod M
  $$
  where `K` is the hash field value.

* **Collision:** occurs if two records map to the same slot.

* **Collision resolution methods:**

  1. **Open addressing:** search sequentially for an empty slot.
  2. **Chaining:** use a pointer to link overflow records.
  3. **Multiple hashing:** apply secondary/tertiary hash functions if collisions occur.

* **Design tips:**

  * Keep the hash table **70–80% full** to reduce overflow.
  * Static internal hashing works well for **fixed-size datasets**, but struggles with dynamic growth/shrinkage.

---

## **3. External Hashing (Disk Files)**

* **Purpose:** handle large datasets stored on disk efficiently.

* **Structure:** divide disk blocks into `M` buckets (`bucket0, bucket1, …, bucketM-1`).

* **Hash key:** one field of the record used to compute bucket.

* **Storage:** one bucket may correspond to **one or multiple blocks**.

* **Operations:**

  * Record with key `K` → stored in bucket `i = h(K)`.
  * Searching by key → direct access via hash function.
  * Collisions → managed using **overflow files** linked to the bucket.

* **Disadvantages of static hashing:**

  1. Fixed number of buckets → problem when file size changes significantly.
  2. Sorted access by key is inefficient → requires extra sorting.

---

## **4. Dynamic Hashing Techniques**

These allow the file to **grow or shrink efficiently**:

1. **Extendible Hashing**

   * Uses a **directory** to manage buckets.
   * Directory can expand/shrink as needed.

2. **Dynamic Hashing**

   * Uses a **tree-structured directory**.
   * Adjusts directory and bucket sizes dynamically to maintain performance.

3. **Linear Hashing**

   * No directory needed.
   * Buckets are split or merged **linearly** as the file grows/shrinks.

> These methods ensure stable performance for large or variable-sized datasets.

---

## **5. Collision Resolution Methods**

1. **Open Addressing:**

   * Search sequentially from the hashed slot to find an empty position.

2. **Chaining:**

   * Overflow records are linked via pointers.
   * New record added to overflow area; main slot points to it.

3. **Multiple Hashing:**

   * Apply a second (or third) hash function if collisions occur.
   * Combine with open addressing if needed.

---

### **Key Takeaways**

* **Hashing is ideal for:** equality searches on key fields.
* **Static hashing:** simple but inflexible.
* **Dynamic hashing:** scalable and maintains performance.
* **Collision handling is essential** to ensure correct and efficient storage.

---
