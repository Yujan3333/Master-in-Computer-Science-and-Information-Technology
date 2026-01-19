## **Five Data Mining Primitives**

Data mining primitives are **high-level specifications** that define **what, where, and how** knowledge is discovered in a dataset. They guide the data mining system and make mining tasks precise.

---

### **1. Task-Relevant Data**

* **Definition:** Specifies the **data subset** that will be mined.
* **Purpose:** Focuses mining on relevant portions, ignoring unnecessary data to improve efficiency.
#### **Examples:**
  * Mining sales trends → select only the **sales transactions** dataset.
  * Predicting student performance → select **exam scores, attendance, and demographic info**.
* Can include: **entire database, warehouse tables, or specific columns/rows**.

---

### **2. Kind of Knowledge to Be Mined**

* **Definition:** Specifies **what type of patterns** or relationships we want to discover.
* **Purpose:** Guides the data mining engine on the **type of analysis**.
#### **Common Types:**
  1. **Classification** – Predict categorical labels (e.g., spam vs. non-spam emails).
  2. **Regression / Prediction** – Predict numeric values (e.g., future sales).
  3. **Association / Correlation** – Discover frequent itemsets and relationships (e.g., “milk → bread”).
  4. **Clustering** – Group similar objects (e.g., customer segmentation).
  5. **Outlier / Anomaly Detection** – Find unusual data points (e.g., fraud detection).
  6. **Characterization / Discrimination** – Summarize and compare classes.

---

### **3. Background Knowledge**

* **Definition:** Domain knowledge or constraints that guide the mining process.
* **Purpose:** Helps **focus the search** and **interpret patterns**.

####  **Forms of Background Knowledge:**
  * **Concept hierarchies:** e.g., city → state → country.
  * **Constraints:** e.g., minimum purchase amount, age > 18.
  * **Metadata or rules** about data meaning.
#### **Example:**
  * Mining sales by region → concept hierarchy helps aggregate from city to state to country.

---

### **4. Interestingness Measures**

* **Definition:** Metrics used to determine which patterns are **useful, meaningful, or surprising**.
* **Purpose:** Filters out trivial or irrelevant patterns.
####  **Common Measures:**
  * **Support:** Frequency of occurrence (e.g., 10% of transactions include milk).
  * **Confidence:** Conditional probability of association (e.g., if milk bought → 60% chance of buying bread).
  * **Lift / Correlation:** Strength of association beyond random chance.
  * **Novelty / Utility:** Pattern usefulness for business decisions.
#### **Example:**
  * Only rules with **support ≥ 5%** and **confidence ≥ 50%** are considered.

---

### **5. Knowledge Presentation**

* **Definition:** How the discovered patterns are **displayed and interpreted** by users.
* **Purpose:** Ensures knowledge is **understandable and actionable**.
#### **Techniques:**
  * **Tables and charts** – simple summaries.
  * **Graphs / Networks** – relationship patterns.
  * **Decision trees** – classification patterns.
  * **OLAP cubes** – multidimensional summarization.
 
#### **Example:**
  * A bar chart showing top-selling products by region.
  * Rules displayed as: “If milk → bread [support=10%, confidence=60%]”.

---

### **Exam-Ready Summary Table**

| Primitive                | Role                                         | Example                                 |
| ------------------------ | -------------------------------------------- | --------------------------------------- |
| Task-relevant data       | Defines **what data** to mine                | Sales transactions table for Q1         |
| Kind of knowledge        | Defines **what patterns** to find            | Association, classification, clustering |
| Background knowledge     | Guides mining using **rules or hierarchies** | City → State → Country                  |
| Interestingness measures | Filters **useful patterns**                  | Support ≥5%, Confidence ≥50%            |
| Knowledge presentation   | Shows results in **interpretable form**      | Charts, decision trees, OLAP cubes      |

---

**One-line exam definition:**

> Data mining primitives are specifications that define **which data to mine, what knowledge to find, what domain knowledge to use, how to measure interestingness, and how to present results**.

---
