![](../../../../../../../Images/Second_Sem_Images/Architecture%20of%20Data%20Warehouse.png)

## Architecture of a Data Warehouse

A data warehouse architecture shows how data flows from source systems to end users for analysis and decision making.

---

### 1. Data Sources

* Operational databases (OLTP systems)
* Flat files
* Legacy systems
* Web data
* External data sources

```
Sources → 
```

---

### 2. ETL Layer (Extraction, Transformation, Loading)

* **Extraction**

  * Collect data from different sources

* **Transformation**

  * Clean data
  * Remove inconsistencies
  * Convert formats
  * Aggregate and summarize

* **Loading**

  * Load transformed data into the warehouse

```
Sources → ETL →
```

---

### 3. Data Warehouse Storage

Central repository where integrated data is stored.

Features:

* Subject-oriented
* Integrated
* Time-variant
* Non-volatile

Contains:

* Fact tables
* Dimension tables
* Data cubes

```
Sources → ETL → Data Warehouse →
```

---

### 4. Data Marts (Optional Layer)

Department-wise smaller warehouses:

* Sales
* Finance
* HR
* Marketing

Can be:

* Dependent (from Data Warehouse)
* Independent (directly from sources)

```
Sources → ETL → Data Warehouse → Data Marts →
```

---

### 5. OLAP Server

Provides:

* Multidimensional views
* Fast aggregation
* Drill-down, roll-up, slice, dice

Types:

* MOLAP
* ROLAP
* HOLAP

---

### 6. Front-End Tools (Client Layer)

Used by users for:

* Querying
* Reporting
* Dashboards
* Data mining
* Visualization

```
Sources → ETL → Data Warehouse → OLAP → Users
```

---

## Complete Flow Diagram (Text Form)

```
[Data Sources]
      ↓
[ETL Process]
      ↓
[Data Warehouse]
      ↓
[Data Marts]
      ↓
[OLAP Server]
      ↓
[Reports / Analysis / Data Mining]
```

---

## One-line Exam Answer

> The architecture of a data warehouse consists of data sources, ETL processes, centralized warehouse storage, optional data marts, OLAP servers, and front-end tools for analysis and reporting.
