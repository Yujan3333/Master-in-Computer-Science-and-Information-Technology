# **Data Preprocessing in Data Mining**

Data preprocessing is the **preparation of raw data** to improve **data quality** for mining.

> *No quality data → No quality mining results.*

---

## **Why Preprocess Data?**

Real-world data is often **dirty**:

| Type         | Description                                   | Example                 |
| ------------ | --------------------------------------------- | ----------------------- |
| Incomplete   | Missing attribute values or entire attributes | Occupation = “ ”        |
| Noisy        | Random errors or outliers                     | Salary = “−10”          |
| Inconsistent | Conflicting data formats or codes             | Rating = 1,2,3 vs A,B,C |

Preprocessing **improves reliability, efficiency, and interpretability** of mining results.

---

## **Major Tasks in Data Preprocessing**

1. **Data Cleaning**

   * Fix missing, noisy, or inconsistent data.
   * Techniques:

     * Fill missing values: global constant, attribute mean, class-based mean, or most probable value.
     * Smooth noisy data: 
	     * [Binning](Binning.md) 
	     * regression
	     * clustering
	     * manual inspection.
     * Correct inconsistencies: unify naming conventions, codes.

2. **Data Integration**

   * Merge data from **multiple sources**: databases, files, or data cubes.
   * Resolves redundancy and inconsistency.

3. **Data Reduction**

   * Reduce data size while maintaining analytical accuracy.
   * Techniques:

     * **[Dimensionality reduction](Dimensionality%20reduction.md)**: reduce number of attributes
     * **Numerosity reduction**: replace large datasets with smaller summaries
     * **Data compression**: reduce storage requirements

4. **Data Transformation & Discretization**

   * Convert data into suitable forms for mining.
   * Examples:

     * **Normalization:** scale values to a standard range
     * **Aggregation:** combine data, e.g., daily → monthly sales
     * **Discretization:** convert continuous values into intervals
     * **Concept hierarchy generation:** create abstraction levels for attributes

5. **Data Mining Primitives**

   * High-level specifications that define **what, where, and how** to mine data.
   * Includes:

     * Task-relevant data
     * Kind of knowledge to be mined
     * Background knowledge
     * Interestingness measures
     * Knowledge presentation

---

## **Handling Missing Data (Incomplete Data)**

**Causes:** Equipment malfunction, human error, misunderstanding, or non-entry.

**Handling Methods:**

1. **Ignore the tuple** – only if class label missing.
2. **Manual fill** – tedious, often infeasible.
3. **Automatic fill**:

   * Global constant (“unknown”)
   * Attribute mean
   * Class-based attribute mean
   * Most probable value

---

## **Handling Noisy Data**

**Definition:** Random errors or variance in measured values.

**Causes:** Faulty instruments, data entry errors, transmission errors, technology limits, inconsistent naming.

**Smoothing Techniques:**

1. **Binning** – group values into bins and smooth by mean/median.
2. **Regression** – fit a model to estimate true values.
3. **Clustering** – replace outliers by cluster averages.
4. **Manual inspection** – combined human-computer review.

---

### ✅ **Quick Exam Summary**

* **Preprocessing**: essential step to improve **data quality** for mining.
* **Key tasks**: Cleaning, Integration, Reduction, Transformation, Discretization, Concept Hierarchies, Mining Primitives.
* **Goal**: Make raw, dirty data **accurate, consistent, and suitable for mining**.

---
