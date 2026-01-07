# **📌 HITS Algorithm (Hyperlink-Induced Topic Search)**

**HITS** is a **link analysis algorithm** developed by Jon Kleinberg.

It is used to **rank web pages** based on **two types of importance**:

1. **Authority** – How good a page is as a source of information on a topic.
2. **Hub** – How good a page is at pointing to other important pages.

---

## **🧠 Simple Analogy**

* Imagine a **library system**:

  * **Authority page** = a book that **many important books refer to**
  * **Hub page** = a guidebook that **lists lots of important books**

* Good hubs point to good authorities.

* Good authorities are pointed to by good hubs.

---

## **🔹 Key Idea**

* Each page has **two scores**:

  1. **Authority score (a)**
  2. **Hub score (h)**

* Update scores **iteratively**:

$$[
\text{Authority score of page } P = \sum_{\text{pages linking to P}} \text{Hub score of linking page}
]$$

$$[
\text{Hub score of page } P = \sum_{\text{pages P links to}} \text{Authority score of linked page}
]$$

* Repeat until **scores converge**.

---

## **Step by Step HITS Algorithm**

1. Start with a set of pages related to a topic (**root set**)
2. Expand to include pages that link to or are linked from the root set (**base set**)
3. Initialize **hub score = 1** and **authority score = 1** for all pages
4. Iteratively update:

   * Update authority scores based on hubs pointing to it
   * Update hub scores based on authorities it points to
5. Normalize scores after each iteration
6. Repeat until scores **converge**

---

## **Example (Simple)**

Suppose 3 pages: A, B, C

* Links:

  * A → B, C
  * B → C
  * C → A

* Iteration 1:

  * Hub and authority scores all start = 1

* Iteration 2:

  * Authority scores updated based on incoming links (sum of hub scores)
  * Hub scores updated based on outgoing links (sum of authority scores)

* After a few iterations:

  * **Highest authority = most cited page**
  * **Highest hub = best directory page pointing to authorities**

---

## **📝 Key Points for Exam**

* HITS is **topic-specific** (focuses on a subset of pages)
* Uses **authority** and **hub** scores
* Iterative algorithm until scores converge
* Good hub → points to many good authorities
* Good authority → pointed by many good hubs

---

## **One-line Exam Answer**

> HITS algorithm ranks web pages using **hub and authority scores**, where hubs point to many good authorities and authorities are pointed to by good hubs, updated iteratively until convergence.

---
