## Data Discretization

Data discretization is the process of **converting continuous numerical data into discrete intervals (bins or categories)**.
It reduces the number of possible values of an attribute and makes data easier to analyze and mine.

In simple words:

> Large range of numbers → few meaningful groups

Example:
Instead of:

```
Age = 12, 18, 25, 33, 47, 60
```

Convert into:

```
Age Group = Child, Teen, Adult, Middle-aged, Senior
```

---

## Why data discretization is needed?

* Reduces data size
* Improves efficiency of data mining algorithms
* Makes patterns easier to understand
* Useful for classification and association rule mining
* Handles noisy data better

---

## Common Discretization Methods

### 1. Binning Method

Already studied in noisy data handling.

Steps:

1. Sort data
2. Divide into bins
3. Replace values by:

   * Bin mean
   * Bin median
   * Bin boundary

Example:
Data:

```
4, 8, 9, 15, 21, 21, 24, 25
```

Bins:

```
[4,8,9,15], [21,21,24,25]
```

After discretization:

```
[9,9,9,9], [23,23,23,23]
```

---

### 2. Histogram-based Discretization

Similar to binning, but mainly used for data reduction.

Types:

* Equal-width
* Equal-frequency

Example:
Marks (0–100):

```
0–40  → Fail  
41–60 → Pass  
61–80 → Good  
81–100 → Excellent  
```

---

### 3. Entropy-based (Supervised Discretization)

Used when **class labels are known**.

* Choose split points that give maximum information gain
* Used in decision tree algorithms

Example:
Split “Age” to best separate:

```
Buy = Yes  
Buy = No
```

---

### 4. Concept Hierarchy-based Discretization

Replace low-level numeric values by higher-level concepts.

Example hierarchy:

```
Age → Young → Middle → Old
```

Or:

```
City → District → State → Country
```

So:

```
Age = 23 → Young  
Age = 45 → Middle  
Age = 70 → Old
```

---

### 5. Clustering-based Discretization

* Group similar values into clusters
* Each cluster becomes one interval

Example:

```
Salaries:
10k, 12k, 11k → Low  
40k, 42k, 45k → Medium  
90k, 95k → High
```

---

## Difference between Binning and Discretization

| Binning                    | Discretization                        |
| -------------------------- | ------------------------------------- |
| Mainly for noise smoothing | Mainly for converting continuous data |
| Replaces values            | Replaces values with categories       |
| Used in data cleaning      | Used in data transformation           |

---

## One-line exam answer:

> Data discretization is the process of transforming continuous numerical attributes into a finite set of intervals or categories, making data mining more efficient and results more understandable.
