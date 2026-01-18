# 🏗️ Components of a Data Warehouse

A typical data warehouse has **four main components**:

---

## 1. **Central Database**

* Acts as the **foundation** of the data warehouse.
* Traditionally: relational databases (on-premise or cloud).
* Modern trend: **in-memory databases** for real-time performance and faster access.
* Stores **integrated, historical, and cleansed data** for analysis.

---

## 2. **Data Integration / ETL Tools**

* Responsible for **Extract, Transform, Load (ETL)** from multiple source systems.
* Tasks include:

  * Data extraction from OLTP or external sources
  * Data transformation and cleaning
  * Loading into the warehouse
* Other approaches: ELT, real-time replication, bulk-load processing, data enrichment.

---

## 3. **Metadata**

* **“Data about data”**
* Provides information about:

  * Source of data
  * Structure and format
  * Usage and meaning
* Types:

  * **Business metadata:** Adds context (e.g., product category, region)
  * **Technical metadata:** Describes how to access and store data

---

## 4. **Data Warehouse Access Tools**

* Tools that allow **users to interact with data** for analysis.
* Examples:

  * Query and reporting tools
  * Application development tools
  * OLAP tools
  * Data mining tools

---

## 📝 Quick Exam-ready Table

| Component              | Purpose                         | Examples                              |
| ---------------------- | ------------------------------- | ------------------------------------- |
| Central Database       | Stores integrated data          | Relational DB, In-memory DB           |
| ETL / Data Integration | Extract, transform, load data   | ETL tools, ELT, replication           |
| Metadata               | Provides information about data | Business metadata, Technical metadata |
| Access Tools           | Allows analysis & reporting     | OLAP, Query/reporting, Data mining    |

---

## 📝 One-line Definition

**Data Warehouse Components:**
“The main components of a data warehouse include a central database for storing data, ETL tools for integration, metadata to describe the data, and access tools for analysis and reporting.”

---
