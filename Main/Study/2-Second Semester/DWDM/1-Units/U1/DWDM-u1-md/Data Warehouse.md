# Data Warehouses

A **data warehouse** is a centralized repository that stores integrated data collected from multiple sources under a unified schema.
It is designed to support **decision making, analysis, and reporting**.

---

## Why Data Warehouses Are Needed

In large organizations (e.g., *AllElectronics*):

* Each branch has its own databases.
* Data are distributed across different locations.
* Analyzing company-wide performance becomes difficult and slow.

With a data warehouse:

* All data are collected in one place.
* Analysis like *sales per item type per branch per quarter* becomes easy and fast.

---

## Definition

> A **data warehouse** is a repository of integrated information, collected from multiple sources, stored under a unified schema, and usually maintained at a single site.

---

## Data Warehouse Construction Process

Data warehouse creation involves:

1. **Data Cleaning**

   * Remove noise and inconsistencies

2. **Data Integration**

   * Combine data from multiple sources

3. **Data Transformation**

   * Convert data into suitable formats

4. **Data Loading**

   * Store data into the warehouse

5. **Data Refreshing**

   * Periodically update the warehouse

---

## Characteristics of Data in a Data Warehouse

- Subject Oriented
- Integrated
- Time Variant
- Non Volatile


Data are:

* **Subject-oriented**

  * Organized around major subjects:

    * Customer
    * Item
    * Supplier
    * Activity

* **Historical**

  * Store data over long periods (e.g., past 6–12 months or more)

* **Summarized**

  * Instead of individual transactions, store aggregated values
  * Example:

    * Total sales per item type per city
    * Total sales per region per quarter

---

## Data Cube

A **data cube** is a multidimensional model for data warehouses.

* Each **dimension** represents an attribute:

  * Time
  * Location
  * Item type

* Each **cell** stores an aggregated value:

  * Count
  * Sum (e.g., sales amount)

---

### Example: AllElectronics Data Cube

Dimensions:

* **Address** → Chicago, New York, Toronto, Vancouver
* **Time** → Q1, Q2, Q3, Q4
* **Item** → Home entertainment, Computer, Phone, Security

Each cell stores:

* **Sales amount (in thousands)**

Example cell:

```
<Vancouver, Q1, Security> = 400
```

Meaning:

* Sales of security items in Vancouver during Q1 = $400,000

---

## OLAP Support

Data warehouses provide natural support for **OLAP (Online Analytical Processing)**.

OLAP allows:

* Fast querying
* Multidimensional analysis
* Viewing data at different levels of detail

---

## OLAP Operations

### 1. Drill-down

Move from summarized data → detailed data
Example:

* Quarter → Month
* Country → City

### 2. Roll-up

Move from detailed data → summarized data
Example:

* City → Country
* Month → Quarter

---

## Example

* Drill-down:

  ```
  Q1 → January, February, March
  ```

* Roll-up:

  ```
  Chicago, New York → USA
  Toronto, Vancouver → Canada
  ```

---

## Multidimensional Data Mining

Also called:

* **Exploratory multidimensional data mining**

Features:

* Performs data mining directly on data cubes
* Explores:

  * Multiple dimensions
  * Different levels of granularity
* Has greater potential to discover:

  * Hidden patterns
  * Valuable knowledge

---

## One-line Exam Summary

> A data warehouse integrates data from multiple sources into a unified, historical, and summarized form using data cubes, enabling OLAP operations like drill-down and roll-up for efficient decision making and advanced data mining.
