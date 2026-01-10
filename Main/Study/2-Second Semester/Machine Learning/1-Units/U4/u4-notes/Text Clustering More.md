Text clustering is the process of **grouping similar text documents together automatically**, without using any predefined labels.
It is an **unsupervised learning** technique.

In simple words:

> Text clustering puts documents that talk about similar topics into the same group.

---

Example:
Suppose we have these documents:

* D1: Computer Science and Information Technology
* D2: Computer Science and Engineering
* D3: Humanities and Social Science
* D4: Department of Social Science
* D5: Applications of Computer Science

After TF-IDF, we get vectors.
Now clustering algorithms (like **K-means**) look at the distance between these vectors:

* D1, D2, D5 → talk about *Computer/Science* → one cluster
* D3, D4 → talk about *Social Science* → another cluster

So result may be:

Cluster 1 (Technology):

* D1
* D2
* D5

Cluster 2 (Social):

* D3
* D4

---

Why we use text clustering:

* To organize large document collections
* To group news articles by topic
* To cluster research papers
* To improve search engines
* To detect themes in social media

---

Steps in Text Clustering:

1. Collect documents
2. Preprocess text

   * Tokenization
   * Stop word removal
   * Stemming/Lemmatization
3. Convert text into numbers

   * Bag of Words
   * TF-IDF
4. Apply clustering algorithm

   * K-means
   * Hierarchical clustering
   * DBSCAN
5. Analyze clusters

---

Difference from classification:

| Feature       | Text Classification | Text Clustering       |
| ------------- | ------------------- | --------------------- |
| Learning type | Supervised          | Unsupervised          |
| Labels        | Known               | Unknown               |
| Goal          | Predict class       | Discover groups       |
| Example       | Spam / Not Spam     | Group emails by topic |

---

One-line exam definition:

> **Text clustering is an unsupervised technique that groups documents into clusters such that documents in the same cluster are more similar to each other than to those in other clusters.**
