## **User-Based Collaborative Filtering (Summary)**

User-based collaborative filtering is a **recommendation technique** that suggests items to a user based on the **preferences of similar users**.

* First, the system **finds users who have similar rating behavior** to the target user.
* Similarity between users is calculated using measures like **cosine similarity** or **Pearson correlation**.
* Then, the system **predicts unknown ratings** by taking a **weighted average** of ratings given by these similar users.
* Usually, only the **top-k most similar users** are used for making recommendations.
* Idea: *“Users who agreed in the past will agree again in the future.”*

---

### **One-line memory trick 🧠**

> *Tell me what people like you liked, and I’ll tell you what you may like.*

---
