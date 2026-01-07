## **Item-Based Collaborative Filtering (Summary)**

Item-based collaborative filtering is a **recommendation method** that predicts whether a user will like an item based on **similar items the user has already rated**.

* First, the system finds a set **S of items similar** to the target item.
* Similarity between items is calculated using measures like **cosine similarity** or **Pearson correlation**.
* Then, the system uses the **ratings given by the user** to these similar items to **predict the rating** for the target item.
* Usually, only the **top-k most similar items** are considered.
* Similarity is computed between the **columns of the rating matrix**.

---

### **One-line memory trick 🧠**

> *If you liked similar items before, you will like this item too.*

---

### **Quick contrast (for exams)**

* **User-based:** “People like you liked this”
* **Item-based:** “You liked similar items”

---
