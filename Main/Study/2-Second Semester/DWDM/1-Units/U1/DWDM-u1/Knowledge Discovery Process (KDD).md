![](../../../../../../../Images/Second_Sem_Images/Knowledge%20Discovery%20Process%20(KDD).png)

---
## Knowledge Discovery from Data (KDD)

KDD is the complete process of discovering **useful knowledge** from large amounts of data. It consists of several sequential steps.

---

### 1. Data Cleaning

* First step of KDD
* Removes:

  * Noise
  * Missing values
  * Inconsistent data
* Improves data quality

Example:
Removing duplicate records, correcting wrong ages like `-5` or `500`.

---

### 2. Data Integration

* Combines data from multiple sources into a **single repository** (Data Warehouse)
* Reduces:

  * Redundancy
  * Inconsistency
* Improves:

  * Accuracy
  * Speed of mining

Example:
Merging sales data from:

* Branch A database
* Branch B database
* Online store

---

### 3. Data Selection

* Selects only **relevant data** for the mining task
* Avoids unnecessary data processing

Example:
For stock market prediction:

* Select price, volume, date
* Ignore unrelated customer data

---

### 4. Data Transformation

* Converts data into a suitable format for mining
* Includes:

  * Normalization
  * Aggregation
  * Generalization

Example:

* Daily sales → Monthly sales
* Scaling values between 0 and 1

---

### 5. Data Mining

* Core step of KDD
* Applies intelligent algorithms to find patterns such as:

  * Classification
  * Clustering
  * Association rules
  * Prediction

Example:
Finding:

* Buying patterns
* Customer groups
* Fraud detection rules

---

### 6. Pattern Evaluation

* Finds **interesting and useful patterns**
* Removes unimportant or redundant patterns
* Uses interestingness measures like:

  * Support
  * Confidence
  * Accuracy

---

### 7. Knowledge Presentation

* Presents discovered knowledge in understandable form
* Using:

  * Charts
  * Graphs
  * Tables
  * Reports

Example:
Showing sales trends in bar charts.

---

### Simple Exam Definition:

> KDD is a process of extracting useful and meaningful knowledge from large datasets through cleaning, integration, selection, transformation, mining, evaluation, and presentation.
