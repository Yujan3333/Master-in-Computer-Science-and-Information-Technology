## **Content-Based Recommender Systems**

### **Definition**

A **content-based recommender system** recommends items to a user **based on the contents/features of the items** and the **user’s own preferences**, rather than relying on other users.

👉 Example features (movies):

* Genre (Action, Romance)
* Actor
* Director
* Story / Keywords

---

## **Key Idea (Very Important)**

> **“Recommend items similar to what the user liked in the past.”**

If a user likes **action movies**, the system recommends **more action movies**, even if no other user exists.

---

## **Why Content-Based Recommendation?**

✔ Personalized (user-specific)
✔ Does **not depend on other users**
✔ **Solves cold-start problem for new users**

### **Cold-Start Problem**

In collaborative filtering, new users have **no ratings**, so recommendations fail.

➡ Content-based systems fix this by:

* Asking user preferences (e.g., likes Action, Sci-Fi)
* Recommending items with **similar content**

---

## **Main Steps in Content-Based Recommender Systems**

### **1️⃣ Item Profile Generation**

This step represents each item using its features.

🔹 Items → Rows
🔹 Features → Columns
🔹 Values → Importance of feature

#### **For Movies**

* Boolean vector
* `1` → feature present
* `0` → feature absent

**Example:**

| Movie | Action | Romance | Comedy |
| ----- | ------ | ------- | ------ |
| M1    | 1      | 0       | 0      |
| M2    | 0      | 1       | 1      |

---

#### **For Text Documents**

* Features are words
* Values are **real numbers**
* Use **TF-IDF**

### **TF-IDF**

* **TF (Term Frequency):** how often a word appears in a document
* **IDF (Inverse Document Frequency):** importance of the word across all documents

👉 Higher TF-IDF = more important feature for that item

---

### **2️⃣ User Profile Generation**

This step builds a profile for each user based on **items they liked or rated**.

🔹 Uses **utility matrix** (User × Item)

#### **Utility Matrix Values**

* `1` → user purchased or liked item
* Ratings (e.g., 1–5 stars)
* Degree of liking

📌 User profile is formed by **combining features of liked items**

---

### **3️⃣ Generating Recommendations**

Now we compare:

* **User profile vector**
* **Item profile vector**

🔹 Use **Cosine Similarity**

### **Cosine Similarity**

Measures similarity between two vectors.

$$[
\text{Cosine Similarity} = \frac{U \cdot I}{|U||I|}
]$$

✔ Value closer to **1** → more similar
✔ Higher similarity → **recommend the item**

📌 Note (for exam):

> Greater the cosine similarity, **more likely the user likes the item**

---

## **Simple Example**

* User likes **Action + Sci-Fi**
* New movie has **Action + Sci-Fi**
  ➡ High cosine similarity
  ➡ Movie is recommended

---

## **Advantages**

✔ Personalized recommendations
✔ Works well for new users
✔ No need for other users’ data

---

## **Limitations (Optional for Exam)**

❌ Overspecialization (same type of items repeatedly)
❌ Needs good feature extraction

---

## **One-Line Exam Summary**

> A content-based recommender system recommends items by matching **item content features** with **user preferences**, using similarity measures like **cosine similarity**, and effectively solves the **cold-start problem for new users**.

---
