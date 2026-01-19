# 📘 Unit – V : Data Mining Concepts (3 Hours)

---

## 1. Data Mining Primitives, Languages, and System Architectures

### **Data Mining Primitives**

Primitives define **what, where, and how to mine**:

1. **Task-relevant data** – Dataset or data warehouse to mine.
2. **Kind of knowledge** – Patterns to discover: classification, association, clustering, outliers.
3. **Background knowledge** – Concept hierarchies, metadata, constraints.
4. **Interestingness measures** – Support, confidence, novelty, utility.
5. **Knowledge presentation** – How results are displayed: rules, tables, graphs.

### **Data Mining Languages**

* **DMQL (Data Mining Query Language)** – SQL-like language for specifying data mining tasks.
* Supports: task definition, pattern type, constraints, measures.

### **Data Mining System Architecture**

1. **Data Sources** – Databases, data warehouses, or web data.
2. **Database / Warehouse Server** – Fetches relevant data.
3. **Knowledge Base** – Domain knowledge, concept hierarchies.
4. **Data Mining Engine** – Performs mining: classification, clustering, association, etc.
5. **Pattern Evaluation Module** – Uses interestingness measures to filter patterns.
6. **Graphical User Interface (GUI)** – Enables interaction, visualization, reports.

---

## 2. Concept Description

### **Purpose:**

Summarize data and describe general characteristics of a class or concept.

### **Types of Concept Description**

1. **Characterization** – Generalizes a target class.

   * **Data Generalization** – Aggregates values into higher-level concepts using concept hierarchies.
   * **Summarization-based Characterization** – Aggregates numeric measures (avg, sum, min, max).
   * **Analytical Characterization** – Uses statistical methods to analyze attribute behavior.

2. **Comparison** – Compares a target class with contrasting classes.

   * Identify differences or distinguishing characteristics.

### **Steps in Concept Description**

1. **Data collection** – Select relevant dataset for analysis.
2. **Attribute relevance analysis** – Keep only relevant attributes for mining.
3. **Generalization / Aggregation** – Use concept hierarchies to group values.
4. **Presentation** – Cross-tab, table, graph, or rule form.

---

## 3. Mining Class Comparisons

* **Target class vs Contrasting class**
* Compares classes sharing the same attributes and dimensions.
* **Example:** Graduate vs Undergraduate students in GPA, age, major.
* **Method:**

  1. Collect data for both classes.
  2. Select relevant attributes (e.g., GPA, Major).
  3. Generalize attributes (age → age_range).
  4. Present comparison (percentage, count, graphs, rules).

---

## 4. Mining Descriptive Statistical Measures

* Compute **numeric summaries** on large databases:

  * **Count, Sum, Average, Min, Max**
  * Compare across classes or groups
  * Helps in analytical characterization and decision-making.

---

### ✅ **Exam-ready Summary Table**

| Topic                    | Key Points                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------- |
| Data Mining Primitives   | Task data, pattern type, background knowledge, interestingness measures, presentation |
| Data Mining Languages    | DMQL: define mining tasks, constraints, patterns                                      |
| System Architecture      | Data source → Server → Mining engine → Pattern evaluation → GUI                       |
| Concept Description      | Characterization (generalization, summarization), analytical characterization         |
| Mining Class Comparisons | Compare target vs contrasting classes, attribute selection, generalization            |
| Descriptive Measures     | Statistical summaries: count, sum, avg, min, max                                      |

---
