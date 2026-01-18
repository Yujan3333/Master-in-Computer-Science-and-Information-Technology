# 🏢 Data Warehouse – Enterprise Model

The **Enterprise Data Warehouse (EDW) model** is a centralized approach where a single data warehouse is built for the entire organization.

It integrates data from all departments and provides a unified, consistent view of data.

---

## 🔹 Definition

An **Enterprise Data Warehouse** is a centralized repository that stores integrated data from multiple business processes and departments to support decision making at an organizational level.

![](../../../../../../../Images/Second_Sem_Images/Enterprise%20Warehouse.png)


---

## 🔹 Architecture (Simple View)

```text
Operational Databases → ETL → Enterprise Data Warehouse → BI Tools/Reports
```

Where:

* ETL = Extract, Transform, Load
* BI = Business Intelligence

---

## 🔹 Key Features

* Single, centralized warehouse
* Data is integrated and standardized
* Covers all business areas (Sales, HR, Finance, Inventory, etc.)
* Supports long-term historical data
* High data consistency and quality

---

## 🔹 Components

* **Source Systems**

  * OLTP databases
  * ERP, CRM systems
  * Flat files, logs

* **ETL Process**

  * Extract data from sources
  * Transform into common format
  * Load into EDW

* **Enterprise Data Warehouse**

  * Central database
  * Stores cleaned, integrated, historical data

* **Data Marts (optional)**

  * Subsets of EDW for specific departments
  * Example: Finance Mart, Sales Mart

* **Front-End Tools**

  * Reports
  * Dashboards
  * Data mining
  * OLAP

---

## 🔹 Advantages

* Single version of truth
* High data accuracy and consistency
* Better enterprise-wide reporting
* Easier governance and security
* Strong support for strategic decisions

---

## 🔹 Disadvantages

* High initial cost
* Complex to design
* Takes longer to implement
* Requires strong planning

---

## 🔹 Comparison (Exam Tip)

| Model            | Description                          |
| ---------------- | ------------------------------------ |
| Enterprise Model | Top-down, centralized data warehouse |
| Data Mart Model  | Bottom-up, departmental warehouses   |

---

## 🔹 One-line Exam Definition

**Enterprise Data Warehouse Model:**
“A centralized data warehouse architecture that integrates data from all organizational units to provide a consistent and enterprise-wide view for decision making.”
