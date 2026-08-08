# 🧩 Multidimensional Model in Data Warehousing

A **multidimensional model** is a way of organizing data in a data warehouse to support **fast and flexible analysis** from multiple perspectives (dimensions).

It is the basis for **OLAP (Online Analytical Processing)** and **data cubes**.

---

## 🔹 Definition

**Multidimensional Model:**
“A data modeling technique in data warehouses where data is viewed and stored as **facts** and **dimensions**, allowing analysis across multiple dimensions.”

* **Fact:** Numerical measure or metric of interest (e.g., sales, profit, quantity)
* **Dimension:** Perspective or category to analyze the fact (e.g., time, product, region, customer)

---

## 🔹 Structure

**Fact Table:**

* Central table containing **facts (measures)**
* Foreign keys reference dimension tables

**Dimension Tables:**

* Surround fact table
* Contain descriptive attributes for analysis

**Example:**

| Fact Table: Sales |         |            |           |              |
| ----------------- | ------- | ---------- | --------- | ------------ |
| Sale_ID           | Time_ID | Product_ID | Region_ID | Sales_Amount |

| Dimension Table: Product |              |          |
| ------------------------ | ------------ | -------- |
| Product_ID               | Product_Name | Category |

| Dimension Table: Time |      |         |       |
| --------------------- | ---- | ------- | ----- |
| Time_ID               | Year | Quarter | Month |

---

## 🔹 Representation

* Can be visualized as a **data cube**:

  * Each axis = dimension
  * Cells = measures
* Example: `Sales` measured across **Time × Product × Region**

---

## 🔹 Advantages

* Supports **fast multidimensional analysis**

* Enables **OLAP operations**:

  * Roll-up → summarize data
  * Drill-down → detailed view
  * Slice → single dimension view
  * Dice → multiple dimensions view
  * Pivot → rotate cube

* Easy to understand and query for business users

---

## 📝 One-line Exam Definition

**Multidimensional Model:**
“A data warehouse model that organizes data into facts and dimensions to allow analysis from multiple perspectives using a data cube.”

---
