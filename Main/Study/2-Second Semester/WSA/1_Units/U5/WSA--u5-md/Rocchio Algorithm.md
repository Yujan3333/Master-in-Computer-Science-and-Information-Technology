## **Rocchio Algorithm (In Short – Exam Ready)**

**Rocchio Algorithm** is a **relevance feedback algorithm** used in **information retrieval** to improve search results by **updating the query vector** based on **relevant and non-relevant documents**.

### **Idea**

* Move the query **closer to relevant documents**
* Move the query **away from non-relevant documents**

### **Formula**

$$[
\vec{Q}*{new} = \alpha \vec{Q}*{old} + \beta \frac{1}{|D_r|}\sum \vec{D_r} - \gamma \frac{1}{|D_{nr}|}\sum \vec{D_{nr}}
]$$

### **Where**

* $\vec{Q}_{old}$ = original query vector
* $\vec{D_r}$ = relevant documents
* $\vec{D_{nr}}$ = non-relevant documents
* $\alpha, \beta, \gamma$ = tuning parameters

### **Uses**

* Query refinement
* Document classification
* Information retrieval systems

### **One-line Exam Answer**

> Rocchio Algorithm improves query representation by shifting it towards relevant documents and away from non-relevant documents using relevance feedback.
