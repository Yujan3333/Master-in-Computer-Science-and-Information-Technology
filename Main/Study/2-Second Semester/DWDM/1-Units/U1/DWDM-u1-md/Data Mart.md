# 🗂️ Data Mart as a Model of Data Warehouse

A **Data Mart** is a smaller, focused version of a data warehouse designed for a specific department or business function such as Sales, Finance, HR, or Marketing.

Instead of serving the whole organization, it serves a **particular user group**.

---

## 🔹 Definition

A **Data Mart** is a subject-oriented, department-level data repository that supports decision making for a specific business unit.

---

## 🔹 Simple Architecture

```text
Source Systems → ETL → Data Mart → Reports / Analysis
```

or with EDW:

```text
Source Systems → ETL → Enterprise Data Warehouse → Data Marts → BI Tools
```

---

## 🔹 Characteristics

* Department-specific
* Smaller than an enterprise data warehouse
* Faster to build
* Lower cost
* Easier to manage
* Optimized for analysis and reporting

---

## 📌 Types of Data Marts

There are **three main types** of Data Marts:

---

## 1. Independent Data Mart

* Built directly from operational systems.
* Does NOT depend on an enterprise data warehouse.

```text
Operational DBs → ETL → Independent Data Mart
```

### Advantages

* Quick to implement
* Low initial cost

### Disadvantages

* Data inconsistency
* Data duplication
* No single version of truth

---

## 2. Dependent Data Mart

* Built from an **Enterprise Data Warehouse (EDW)**.
* Most widely recommended model.

```text
Source Systems → ETL → EDW → Dependent Data Mart
```

### Advantages

* High data consistency
* Single version of truth
* Better data quality

### Disadvantages

* Requires EDW first
* Higher setup cost

---

## 3. Hybrid Data Mart

* Combines both independent and dependent approaches.
* Some data comes from EDW, some directly from source systems.

```text
EDW + Operational Systems → ETL → Hybrid Data Mart
```

### Advantages

* Flexible
* Faster access to real-time data

### Disadvantages

* Complex to manage
* Risk of inconsistency

---

## 🧠 Exam Comparison Table

| Type        | Source                    | Dependency   | Consistency | Cost   |
| ----------- | ------------------------- | ------------ | ----------- | ------ |
| Independent | Operational systems       | No EDW       | Low         | Low    |
| Dependent   | Enterprise Data Warehouse | Requires EDW | High        | High   |
| Hybrid      | EDW + Operational systems | Partial      | Medium      | Medium |

---

## 📝 One-line Exam Definitions

* **Data Mart Model:**
  “A departmental-level data warehouse model that stores subject-specific data for faster analysis and reporting.”

* **Independent Data Mart:**
  “A data mart built directly from operational databases without using an enterprise data warehouse.”

* **Dependent Data Mart:**
  “A data mart created from an enterprise data warehouse ensuring consistency and integration.”

* **Hybrid Data Mart:**
  “A data mart that uses both enterprise data warehouse and operational sources.”
