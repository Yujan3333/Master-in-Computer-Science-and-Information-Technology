#second-semester #DWDM
# 📘 Unit – IV : Data Warehouse and OLAP (6 Hours)

---

## 1. Difference between Operational Database Systems and Data Warehouse

| Aspect     | Operational DB (OLTP)      | Data Warehouse (OLAP)          |
| ---------- | -------------------------- | ------------------------------ |
| Purpose    | Day-to-day transactions    | Decision making & analysis     |
| Data       | Current, detailed          | Historical, summarized         |
| Operations | Insert, Update, Delete     | Read-only, complex queries     |
| Design     | Highly normalized          | Denormalized (Star, Snowflake) |
| Users      | Clerks, operators          | Managers, analysts             |
| Example    | Banking transaction system | Sales analysis system          |

---

## 2. Multidimensional Data Model

* Data is represented in the form of **data cubes**
* Dimensions → Time, Product, Location
* Measures → Sales, Profit, Quantity

Example:

> Sales(Time, Product, Location)

It supports fast analytical queries.

---

## 3. Data Warehouse and OLAP Technology

* Data Warehouse: Central repository for integrated, historical data
* OLAP (Online Analytical Processing):

  * Performs fast analysis on multidimensional data
  * Supports:

    * Summarization
    * Trend analysis
    * Comparisons

---

## 4. OLAP Operations

| Operation  | Meaning                         |
| ---------- | ------------------------------- |
| Slice      | Select one dimension value      |
| Dice       | Select multiple dimensions      |
| Roll-up    | Summarize (detail → general)    |
| Drill-down | Go to detail (general → detail) |
| Pivot      | Rotate cube to change view      |

---

## 5. Types of OLAP Servers

### 1. ROLAP (Relational OLAP)

* Uses relational databases
* Data stored in tables
* Highly scalable
* Slower than MOLAP

### 2. MOLAP (Multidimensional OLAP)

* Uses multidimensional arrays
* Very fast query performance
* Requires large storage
* Less scalable

### 3. HOLAP (Hybrid OLAP)

* Combines ROLAP + MOLAP
* Summary data → MOLAP
* Detailed data → ROLAP
* Balanced performance and storage

---

## 6. Data Warehouse Implementation

Steps:

1. Requirement analysis
2. Data source identification
3. ETL process
4. Schema design (Star / Snowflake)
5. Cube creation
6. OLAP processing
7. User tools and reports

---

## 7. Efficient Computation of Data Cubes

### Cube Materialization

| Type                    | Meaning                     |
| ----------------------- | --------------------------- |
| No Materialization      | Compute on demand           |
| Full Materialization    | Precompute all cuboids      |
| Partial Materialization | Precompute selected cuboids |

---

### Cube Computation Methods

1. **Multiway Array Aggregation**

   * Used for full cube
   * Uses multidimensional arrays
   * Works well for small number of dimensions

2. **BUC (Bottom-Up Construction)**

   * Used for iceberg cubes
   * Uses minimum support
   * Prunes unimportant data

---

## 8. Processing of OLAP Queries

* OLAP queries are:

  * Aggregation based
  * Multidimensional
  * Read-intensive
* Use:

  * Precomputed cubes
  * Indexes
  * Caching
  * Aggregation hierarchies

---

## 9. Indexing OLAP Data

Purpose:

> To speed up query processing

Common Indexing Techniques:

* Bitmap Index
* Join Index
* Star Join Index
* Aggregate Index

---

## 📝 Exam Ready One-Liner

> Unit IV deals with the difference between OLTP and Data Warehouse systems, multidimensional data models, OLAP technology and operations, types of OLAP servers (ROLAP, MOLAP, HOLAP), data warehouse implementation, efficient cube computation, OLAP query processing, and indexing techniques for fast analysis.

---
