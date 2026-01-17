# What Is Data Mining?

Data mining is the process of **discovering interesting patterns and useful knowledge from large amounts of data**.

Although the name suggests “mining data,” it is more accurately **knowledge mining from data**, just like gold mining extracts valuable gold from rocks and sand.
Here, data are the raw material, and knowledge is the valuable product.

Other terms with similar meaning:

* Knowledge mining from data
* Knowledge extraction
* Data / pattern analysis
* Data archaeology
* Data dredging

---

## Data Mining vs KDD

Two views exist:

1. **Data mining = KDD**

   * Data mining refers to the entire process of knowledge discovery.

2. **Data mining ⊂ KDD**

   * Data mining is only one step in the larger process called
     **Knowledge Discovery in Databases (KDD)**.

In textbooks and research, the second view is more precise.
In practice and industry, the first view is commonly used.

---

## Knowledge Discovery Process (KDD)

Data mining is a core step in the KDD process.

### Steps in KDD:

1. **Data cleaning**

   * Remove noise and inconsistent data

2. **Data integration**

   * Combine data from multiple sources

3. **Data selection**

   * Retrieve relevant data for analysis

4. **Data transformation**

   * Convert data into suitable form (aggregation, normalization, etc.)

5. **Data mining**

   * Apply intelligent methods to extract patterns

6. **Pattern evaluation**

   * Identify truly interesting and useful patterns

7. **Knowledge presentation**

   * Visualize and present knowledge to users

Steps 1–4 → **Data preprocessing**
Step 5 → **Core mining step**
Steps 6–7 → **Knowledge interpretation and use**

![](../../../../../../../Images/Second_Sem_Images/STEPS%20IN%20KDD.png)

---

## Simple Flow (Exam Friendly)

```
Data → Cleaning & Integration → Selection & Transformation → Data Mining 
→ Pattern Evaluation → Knowledge Presentation → Knowledge
```

---

## Final Definition (Exam Ready)

> **Data mining is the process of discovering interesting patterns and useful knowledge from large volumes of data stored in databases, data warehouses, the Web, or data streams.**

---

## One-line Summary

> Data mining extracts valuable knowledge from massive data, either as a step in KDD or as the complete knowledge discovery process itself.
