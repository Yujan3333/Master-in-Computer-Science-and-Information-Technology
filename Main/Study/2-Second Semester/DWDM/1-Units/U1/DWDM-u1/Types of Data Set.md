# 📂 Types of Data Sets (Summary)

There are **three main types of data sets**:

```text
1. Record Data
2. Graph Data
3. Ordered Data
```

---

## 1. 📋 Record Data

Data consists of a collection of records (objects), each having a fixed set of attributes.

* Attribute = property of an object
  (also called: variable, field, feature, dimension)
* Object = record, data point, instance, sample, entity

### Types of Record Data:

### a) Data Matrix

* Objects have the same numeric attributes.
* Represented as an $m \times n$ matrix:

  * $m$ rows → objects
  * $n$ columns → attributes
* Each object is a point in multi-dimensional space.
![](../../../../../../../Images/Second_Sem_Images/Types%20of%20Data%20Set-1.png)


---

### b) Document Data

* Each document is represented as a **term vector**.
* Each term is an attribute.
* Value = number of times the term appears in the document.
* Used in text mining and NLP.

![](../../../../../../../Images/Second_Sem_Images/Types%20of%20Data%20Set.png)

---

### c) Transaction Data

* Each record is a transaction containing a set of items.
* Common in market basket analysis.

Example:

```text
T1 → {Milk, Bread, Sugar}
T2 → {Milk, Pen}
```

---

## 2. 🕸️ Graph Data

Data represented using **nodes and edges**.

Used when objects have relationships or structure.

Examples:

* World Wide Web (webpages and links)
* Social Networks (users and connections)
* Information networks

---

## 3. ⏳ Ordered Data

Data where elements are stored in a specific order or sequence.
Each item has an index.

Types:

* **Spatial Data** → geographical positions
* **Temporal Data** → time-based data
* **Sequential Data** → ordered events or transactions
* **Genetic Sequence Data** → DNA sequences

---

## 📝 One-Page Exam Summary

| Type         | Description                        | Examples                             |
| ------------ | ---------------------------------- | ------------------------------------ |
| Record Data  | Fixed attributes per object        | Data matrix, documents, transactions |
| Graph Data   | Nodes and edges with relationships | Web, social networks                 |
| Ordered Data | Data with ordering/index           | Time series, spatial data, DNA       |

---

## 🔑 One-line Definitions

* **Record Data:** Data stored as records with fixed attributes.
* **Graph Data:** Data represented as nodes and edges showing relationships.
* **Ordered Data:** Data arranged in a meaningful sequence or order.
