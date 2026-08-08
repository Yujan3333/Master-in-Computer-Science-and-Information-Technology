
## **1️⃣ What is a Search Engine Spider?**

A **spider** (also called a **crawler or bot**) is a **program used by search engines** to:

* Browse the **World Wide Web (WWW)**
* **Collect information** from web pages
* **Index the information** so it can be quickly retrieved when a user searches for a keyword

📌 Example: Googlebot is Google’s spider.

---

## **2️⃣ Spidering Algorithm (Step-by-Step)**

A spider works like this:

1. **Initialize**

   * Start with a **queue of known URLs** (seed pages).

2. **Loop until done**

   * Take the first URL `L` from the queue.
   * **Skip non-HTML pages** (images, PDFs, etc.)
   * **Skip already visited pages**
   * Try to **download the page `P`**

     * If it fails (404 error or blocked by robots.txt), skip
   * **Index the page** (store its content in the search engine)
   * **Extract all links** from the page → new URLs `N`
   * **Add new links to the end of the queue**
   * Repeat the loop until **queue is empty** or **time/page limit reached**

---

## **3️⃣ Focus of a Spider**

Spiders can be **designed with different goals**:

1. **Topic-Directed Spider**

   * Collect pages relevant to a **specific topic**.
   * Example: Collect all pages about “machine learning.”

2. **Link-Directed Spider**

   * Focuses on following **links from important or highly-connected pages**.
   * Example: Start from popular news websites and follow outgoing links to discover new pages.

---

### **Simple Summary for Exam**

* A **spider** automatically fetches and indexes web pages for search engines.
* It works using a **queue-based algorithm**: fetch page → index → extract links → repeat.
* Can be **topic-directed** (focus on subject) or **link-directed** (focus on connected pages).

---
