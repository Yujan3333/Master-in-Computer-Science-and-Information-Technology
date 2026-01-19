![](../../../../../../../Images/Second_Sem_Images/Architecture%20of%20a%20typical%20data%20mining%20system.png)

## Architecture of Data Mining System

A data mining system is composed of several interconnected components that work together to extract useful knowledge from data.

---

### 1. Database, Data Warehouse, WWW, or Other Information Repository

* Source of data for data mining
* Can include:

  * Databases
  * Data warehouses
  * Spreadsheets
  * Web data
  * Other information repositories
* Data cleaning and data integration are performed here to improve data quality

Purpose:

> Provide raw and preprocessed data for mining.

---

### 2. Database or Data Warehouse Server

* Fetches relevant data based on user requests
* Acts as an interface between data sources and the data mining system
* Handles:

  * Data access
  * Query processing
  * Data retrieval

Purpose:

> Supplies required data efficiently to the mining engine.

---

### 3. Knowledge Base

* Stores domain knowledge
* Guides the mining process
* Helps in evaluating discovered patterns

Contains:

* Concept hierarchies
* Rules
* Constraints
* Metadata

Example:

* City → District → Province
* Age → Young, Adult, Old

Purpose:

> Improves mining accuracy and makes results more meaningful.

---

### 4. Data Mining Engine

* Core component of the system
* Applies mining algorithms

Supports tasks like:

* Association and correlation analysis
* Classification
* Prediction
* Clustering
* Outlier analysis

Purpose:

> Discovers patterns and relationships from data.

---

### 5. Pattern Evaluation Module

* Evaluates mined patterns
* Uses interestingness measures such as:

  * Support
  * Confidence
  * Accuracy
* Filters out unimportant or irrelevant patterns
* Works closely with the data mining engine

Purpose:

> Keeps only useful and interesting knowledge.

---

### One-line Exam Answer:

> The architecture of a data mining system consists of data repositories, database servers, a knowledge base, a data mining engine, and a pattern evaluation module that together support efficient knowledge discovery.
