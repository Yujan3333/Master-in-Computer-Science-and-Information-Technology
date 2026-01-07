
# **📌 PageRank Algorithm**

### **What is PageRank?**

**PageRank** is an algorithm developed by **Google** to **rank web pages** based on their importance.

* Pages are considered **important** if **other important pages link to them**.
* It’s like a **voting system**: the more votes (links) a page gets from other pages, the higher its rank.

---

## **🧠 Intuition / Simple Analogy**

Imagine the web as a **network of friends**:

* Each page = a person
* Each link = a recommendation/vote
* A page is important if **important pages link to it**, not just the number of links.

---

## **🔹 PageRank Formula (Simplified)**

The PageRank of a page $P$:

$$
PR(P) = (1-d) + d \sum_{i \in M(P)} \frac{PR(i)}{C(i)}
$$

Where:

| Symbol  | Meaning                              |
| ------- | ------------------------------------ |
| $PR(P)$ | PageRank of page P                   |
| $d$     | Damping factor (usually 0.85)        |
| $M(P)$  | Set of pages linking to P            |
| $PR(i)$ | PageRank of page i that links to P   |
| $C(i)$  | Number of outbound links from page i |

---

### **Step by Step Algorithm**

1. Assign **initial PageRank** to all pages (usually 1.0).
2. For each page, **calculate new PageRank** using the formula above.
3. Repeat **iteratively** until PageRank values **converge** (changes are very small).
4. Rank pages according to their final PageRank.

---

## **🔹 Example**

Suppose we have 3 pages: A, B, C

* A links to B and C
* B links to C
* C links to A

Step 1: Initialize PR(A) = PR(B) = PR(C) = 1
Step 2: Apply formula iteratively until PR stabilizes.

* Pages with **more incoming links from important pages** get higher PR.

---

## **Key Points to Remember**

* **Damping factor (d)**: Accounts for a random user who may jump to any page. Typical value = 0.85
* PageRank **doesn’t just count links**, it considers **quality of links**
* Used in **Google Search ranking**
* Works best on **web-scale link graphs**

---

## **📝 Short Exam Answer**

> PageRank is a link analysis algorithm that ranks web pages by measuring their importance based on the number and quality of links pointing to them. Higher-ranked pages are considered more important.

---
## Some Rules TO BE CONSIDERED
Absolutely! Let’s break these **PageRank rules** into **simple, easy-to-understand points**, Yujan. I’ll also explain **why each rule exists**, so you can remember them for exams.

---

# **PageRank Rules Explained**

---

### 1️⃣ **Links from a page to itself are ignored**

* **Rule:** A page linking to itself does **not** count toward its PageRank.
* **Reason:**

  * Otherwise, a page could artificially boost its own rank.
  * PageRank is supposed to measure importance **from other pages**, not self-promotion.

**Analogy:**

* Think of it like a student giving themselves extra marks — it doesn’t count.

---

### 2️⃣ **Multiple outbound links to the same page are treated as one**

* **Rule:** If page A links to page B multiple times, it counts as **only one link**.
* **Reason:**

  * PageRank is based on the **number of unique references**, not repeated links.
  * Multiple links shouldn’t unfairly boost rank.

**Analogy:**

* A friend recommending the same book 10 times doesn’t make the book 10× better — **one recommendation is enough**.

---

### 3️⃣ **PageRank is initialized to the same value for all pages**

* **Rule:** Initially, all pages have **equal PageRank**.

  * If there are **n pages**, then initial PR = $1/n$.
* **Reason:**

  * We start with a **neutral state**, before iterations distribute rank based on links.

**Example:**

* 5 pages → initial PR = 1/5 = 0.2 for each page.

---

### 4️⃣ **PageRank is divided equally among all outbound links**

* **Rule:** When a page passes its rank to linked pages, the **rank is split equally among all outbound links**.

* **Reason:**

  * Ensures fair distribution.
  * A page with many outgoing links gives **less rank to each link** than a page with few outgoing links.

**Example:**

* Page A has PR = 0.6 and 3 outbound links → each link receives **0.6 ÷ 3 = 0.2**
* Page B has PR = 0.6 and 1 outbound link → the link receives **0.6 ÷ 1 = 0.6**

**Analogy:**

* A student sharing candies: 6 candies among 3 friends → each gets 2 candies. More friends = fewer candies per friend.

---

#### ✅ **Quick Exam Memory Trick**

| Rule                  | Short Reminder       |
| --------------------- | -------------------- |
| Self-links ignored    | Don’t cheat yourself |
| Multiple links = 1    | One vote per page    |
| Initial PR = 1/n      | Start equal          |
| Divide PR among links | Share fairly         |

---

#### 💡 One-line Exam Explanation

> PageRank ignores self-links, counts multiple links to the same page as one, initializes all pages equally (1/n), and distributes a page’s rank **equally among its outbound links** in each iteration.

---
