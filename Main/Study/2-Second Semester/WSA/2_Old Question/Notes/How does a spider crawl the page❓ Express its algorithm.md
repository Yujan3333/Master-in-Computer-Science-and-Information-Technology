## Q4. How does a spider crawl the page? Express its algorithm.

### 📌 What is a Spider (Web Crawler)?

A **spider** (or web crawler) is an automated program that **browses the web**, downloads web pages, and follows links from one page to another to collect information.

---

## 🧠 How does a spider crawl a web page? (Simple Explanation)

1. The spider starts with a **list of initial URLs** (seed URLs).
2. It **visits one URL**, downloads the page content.
3. It **extracts all hyperlinks** from that page.
4. The extracted links are **added to a list** of URLs to visit.
5. The spider **repeats the process** for new URLs.
6. It avoids revisiting already visited pages.

---

## 🧾 Spider Crawling Algorithm (Step-by-Step)

### **Algorithm: Web Spider Crawling**

1. Initialize a list **URL_List** with seed URLs.
2. Initialize an empty set **Visited_URLs**.
3. While **URL_List is not empty**, do:

   * a. Remove one URL from **URL_List**.
   * b. If URL is not in **Visited_URLs**:

     * i. Download the web page.
     * ii. Store the page content locally.
     * iii. Extract all hyperlinks from the page.
     * iv. Add new hyperlinks to **URL_List**.
     * v. Add the URL to **Visited_URLs**.
4. Stop when **URL_List is empty** or crawling limit is reached.

---

## 🧪 Simple Flow (for understanding)

```
Start → Visit Page → Extract Links → Add New Links → Visit Next Page → Stop
```

---

## 📝 Short Exam Conclusion

> A spider crawls web pages by starting from a set of seed URLs, downloading pages, extracting hyperlinks, and recursively visiting new links while avoiding duplicate visits.

---

### ✅ Marks Tip

* Definition → 1–2 marks
* Working explanation → 2 marks
* Algorithm → 2 marks
