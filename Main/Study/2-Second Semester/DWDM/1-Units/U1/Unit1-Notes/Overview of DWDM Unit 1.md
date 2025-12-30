
# **UNIT – I: Data Warehousing (Exam Notes)**

## 1️⃣ Evolution of Data Warehousing (Historical Context)

### a) Early Data Processing (1960s–1970s)

* Data stored in **files**
* Programs tightly coupled with data
* No integration between departments
* Used mainly for **record keeping**

### b) Database Era (1980s)

* Introduction of **DBMS (Relational Databases)**
* Reduced data redundancy
* Focus on **OLTP (Online Transaction Processing)**
* Examples: Banking transactions, reservations

### c) Decision Support Systems (Late 1980s)

* Managers needed **analysis**, not transactions
* Separate systems for reporting
* Data extracted from operational databases

### d) Data Warehouse Era (1990s–Present)

* Centralized **integrated data repository**
* Supports **OLAP and data mining**
* Enables **strategic decision making**
* Historical and summarized data

📌 **Key Idea:**
Data warehousing evolved to support **better decision making**, not daily operations.

---

## 2️⃣ Data Warehouse – A Brief History

* Term **“Data Warehouse”** popularized by **Bill Inmon**
* Defined as:

> *A subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management decisions.*

### Reasons for emergence:

* Data scattered across departments
* Poor query performance on OLTP systems
* Need for historical analysis
* Growth of business intelligence tools

---

## 3️⃣ Today’s Development Environment

Modern data warehousing environment includes:

* **ETL tools** (Extract, Transform, Load)
* **Data warehouse servers**
* **OLAP tools**
* **Data mining tools**
* **BI dashboards and reporting tools**

### Characteristics:

* High storage capacity
* Parallel processing
* Cloud-based warehouses (e.g., Snowflake, Redshift)

---

## 4️⃣ Principles of Data Warehousing

### Core Principles:

1. **Separation of operational and analytical systems**
2. **Integration of data from multiple sources**
3. **Data consistency and quality**
4. **Support for historical data analysis**
5. **Scalability and performance**

---

## 5️⃣ Types of Data and Their Uses

### a) Operational Data

* Current, detailed data
* Used for daily transactions
* Example: customer order

### b) Historical Data

* Old data stored over time
* Used for trend analysis

### c) Summarized Data

* Aggregated data
* Faster query performance
* Example: monthly sales total

### d) Metadata

* Data about data
* Describes structure, source, and meaning

---

## 6️⃣ Conceptual Data Architecture

### Three-Level Architecture (High Level)

1. **Source Layer**

   * Operational databases
   * External data sources

2. **Data Warehouse Layer**

   * Central data storage
   * Integrated, cleaned data

3. **Presentation Layer**

   * OLAP tools
   * Reports, dashboards

📌 **Purpose:**
Shows *what data exists* and *how it flows*, not how it is physically stored.

---

## 7️⃣ Design Techniques of Data Warehouse

### a) Top-Down Approach (Inmon)

* Build **enterprise data warehouse first**
* Then create data marts
* More consistent but costly

### b) Bottom-Up Approach (Kimball)

* Build **data marts first**
* Integrate later
* Faster and cheaper

### c) Hybrid Approach

* Combination of both

---

## 8️⃣ Introduction to Logical Architecture

Logical architecture explains **how data is organized logically**.

### Components:

* Fact tables
* Dimension tables
* Relationships between them

### Common Logical Models:

* **Star Schema**
* **Snowflake Schema**
* **Fact Constellation**

📌 Logical architecture focuses on:

* Data organization
* Query efficiency
* User understanding

---

## 🔑 Very Important Exam Keywords (Remember!)

* Subject-oriented
* Integrated
* Time-variant
* Non-volatile
* OLTP vs OLAP
* ETL
* Metadata
* Star schema

---
