### **1️⃣ Elbow Method**

* Run K-Means for different values of **K**
* Compute **Within-Cluster Sum of Squares (WCSS)** for each K
* Plot **WCSS vs K**
* The point where the decrease in WCSS **starts to slow down (forms an “elbow”)** is chosen as the optimal K

📌 Intuition: After this point, increasing K gives little improvement.

###### Visually
![](../../../../../../Images/Second_Sem_Images/elbow%20method.png)

---

### **2️⃣ [Silhouette Method](Silhouette%20Method.md)**

* Measures how well each data point fits within its cluster
* Silhouette coefficient ranges from **−1 to +1**
* Compute average silhouette score for different values of **K**
* The **K with the highest silhouette score** is considered optimal

📌 Intuition: Higher score = better-defined clusters.

---

### **Exam-ready answer (short)**

> The two mechanisms to find the global value of K in K-Means are the **Elbow method** and the **Silhouette method**.
