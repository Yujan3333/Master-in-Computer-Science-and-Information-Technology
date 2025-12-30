
## **Creating the Data Asset & Business Information Warehouses**

---

## 1️⃣ Creating the Data Asset

### Meaning (Han & Kamber view):

A **data asset** is a **cleaned, integrated, and transformed collection of data** stored in a data warehouse, designed to support **decision-making, analysis, and data mining**.

📌 The data warehouse converts **raw operational data → valuable information**.

---

## 2️⃣ Business Data Warehouse Design

According to Han & Kamber, **data warehouse design** focuses on modeling data in a way that supports **multidimensional analysis**.

### Key Design Considerations:

1. **Business-driven design**
2. **Subject-oriented modeling**
3. **Multidimensional schema**
4. **Performance and scalability**

---

### a) Identification of Business Processes

* Examples:

  * Sales
  * Inventory
  * Customer management
* Each process becomes a **fact table**

---

### b) Fact Tables

* Central tables in data warehouse
* Contain **measures (numerical values)**
* Example:

  * Sales amount
  * Quantity sold

---

### c) Dimension Tables

* Provide **context** to facts
* Example dimensions:

  * Time
  * Customer
  * Product
  * Location

📌 This structure supports **OLAP operations**.

---

## 3️⃣ Populating the Data Warehouse (ETL Process)

Han & Kamber emphasize **ETL as a core component** of data warehousing.

### a) Data Extraction

* Data collected from:

  * Operational databases
  * Legacy systems
  * External sources

---

### b) Data Transformation

Includes:

* Data cleaning
* Data integration
* Data normalization
* Handling missing values
* Resolving inconsistencies

📌 High data quality is **critical for data mining accuracy**.

---

### c) Data Loading

* Loading transformed data into warehouse
* Types:

  * Initial load
  * Incremental load
* Warehouse data is **non-volatile** (not frequently updated)

---

## 4️⃣ Unlocking the Data Asset for End Users

### Meaning:

Providing **easy and efficient access** to warehouse data for analysis.

### End Users:

* Business analysts
* Managers
* Executives
* Data miners

---

## 5️⃣ Use of Business Information

Han & Kamber categorize business information based on **decision level**.

### a) Strategic Information

* Long-term decisions
* Example:

  * Market expansion
  * Policy planning

---

### b) Tactical Information

* Medium-term decisions
* Example:

  * Department performance analysis

---

### c) Operational Information

* Short-term decisions
* Example:

  * Daily inventory monitoring

---

## 6️⃣ Designing Business Information Warehouses

### Business Information Warehouse (BIW):

* A layer built on top of the data warehouse
* Optimized for:

  * Reporting
  * OLAP
  * Data analysis

📌 Han & Kamber highlight that BIWs enable **fast, interactive querying**.

---

### Design Goals:

* Simple structure
* Multidimensional view
* High performance
* User-friendly access

---

## 7️⃣ Populating Business Information Warehouses

### Process:

1. Data extracted from **central data warehouse**
2. Data aggregated and summarized
3. Data stored in:

   * Data marts
   * OLAP cubes

📌 BIWs store **derived and summarized data**, not raw transactional data.

---

## 8️⃣ User Access to Information

### Access Methods (as per Han & Kamber):

* OLAP tools
* Predefined reports
* Ad-hoc queries
* Visualization tools

### Requirements:

* Minimal technical complexity
* Fast response time
* Flexible querying

---

## 9️⃣ Information Data in Context

Han & Kamber stress that **data alone has limited value**.

### Contextual Information Includes:

* Time dimension
* Comparisons
* Trends
* Aggregations

📌 **Example:**
Sales = 10,000 → low value
Sales = 10,000 **compared with last quarter** → high value

---

## 🔑 Key Exam Keywords (From Han & Kamber)

* Data asset
* ETL process
* Fact table
* Dimension table
* Multidimensional data model
* OLAP
* Data mart
* Non-volatile data

---
