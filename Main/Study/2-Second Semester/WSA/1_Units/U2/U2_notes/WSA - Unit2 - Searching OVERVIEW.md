
# **Unit 2: Searching (8 hours)**

Unit 2 deals with **how search works** on the web and how to make it smarter. It is not just about typing a word and getting results; it’s about indexing, ranking, analyzing links, and user behavior.

---

## 1️⃣ **Searching with Lucene**

* **Lucene** is a popular **open-source search library**.
* It helps to **index documents** and **search them efficiently**.
* Key idea: Instead of searching all text every time, **preprocess (index) the data** so searches are faster.

**Example:** Google doesn’t scan the whole web live—it uses its index.

---

## 2️⃣ **Why search beyond indexing?**

* Indexing alone is not enough for **smart search**.
* Indexing just finds **keywords**, but doesn’t consider:

  * Document quality
  * Relevance
  * User intent

**Example:** Searching “Apple” → is it the **fruit** or the **company**?

---

## 3️⃣ **Improving search results based on link analysis**

* Links between web pages are **used to measure importance**.
* **Algorithms** like **PageRank** analyze links:

  * Pages with **more inbound links** are usually more important.
  * Links act as “votes of confidence”.

**Example:** Wikipedia pages get high ranking because many sites link to them.

---

## 4️⃣ **Improving search results based on user clicks**

* Click data shows **what users find useful**.

* Algorithms track:

  * Which results users click first
  * How long they stay on the page

* This is called **click-through feedback** or **behavioral relevance**.

**Example:** If most people click result #3 instead of #1, maybe #3 is more relevant.

---

## 5️⃣ **Ranking Word, PDF, and other documents without links**

* Some documents **don’t have links**, like PDFs or Word files.
* For them, ranking relies on:

  * **Keyword frequency**
  * **Document length**
  * **Proximity of search words**
  * **Metadata** (title, author, headings)

**Example:** Searching “machine learning” in PDFs of research papers.

---

## 6️⃣ **Large-scale implementation issues**

* Challenges when search is done on **millions or billions of documents**:

  * Index storage and updates
  * Query speed
  * Ranking computation
  * Handling new/updated pages efficiently

**Example:** Google searches billions of pages in milliseconds.

---

## 7️⃣ **Is what you got what you want?**

* Measures **search quality** using:

  * **Precision**: Fraction of retrieved documents that are relevant
    $$\text{Precision} = \frac{\text{Relevant Retrieved Docs}}{\text{Total Retrieved Docs}}$$
  * **Recall**: Fraction of relevant documents that are retrieved
    $$\text{Recall} = \frac{\text{Relevant Retrieved Docs}}{\text{Total Relevant Docs}}$$

**Example:** High precision but low recall → results are relevant but you missed many.
High recall but low precision → you got most relevant ones, but also lots of junk.

---

## ✅ **Summary of Unit 2**

* **Lucene:** Indexing + fast search
* **Beyond indexing:** Need relevance, not just keyword match
* **Link analysis:** Importance of page based on links (PageRank)
* **User clicks:** Learn from user behavior to improve ranking
* **Documents without links:** Use content + metadata
* **Large-scale issues:** Speed, storage, ranking, updates
* **Precision & Recall:** Measures of search effectiveness

---

### 🧠 **Memory Trick / Story**

* Imagine a library with **millions of books**:

  * 📚 **Lucene = catalog system**
  * 🔗 **Links = recommendations from other books**
  * 👀 **Clicks = which books people read most**
  * 📄 **PDF/Word = uncataloged books**
  * ⏱ **Large-scale = library is huge, how to find fast**
  * 🎯 **Precision & Recall = did I get the right books?**

---

