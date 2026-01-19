## Data Reduction 1: Dimensionality Reduction

Dimensionality reduction means **reducing the number of attributes (features)** in a dataset while keeping the important information. It makes data mining faster, cheaper, and more accurate.

---

### a) Wavelet Transforms

* A wavelet transform converts a data object $X$ into another form $X’$.
* Both $X$ and $X’$ have the same length, but $X’$ can be **truncated** (some small coefficients removed).
* By removing less important parts, we reduce dimensions → **data reduction**.
* It works well for:

  * Data cubes
  * Sparse data
  * Highly skewed data
* Commonly used in:

  * Image compression
  * Signal processing

Simple idea:

> Keep only the important wavelet coefficients and discard the rest.

---

### b) Principal Component Analysis (PCA)

* PCA finds new attributes called **principal components**.
* These components capture **maximum variance (information)** in the data.
* Given:

  * $N$ data points
  * $n$ dimensions
* PCA finds:

  * $k$ principal components, where $k \le n$

So:

> Original data: $N$ points in $n$ dimensions
> Reduced data: $N$ points in $k$ dimensions

Simple idea:

> Replace many correlated attributes with fewer uncorrelated components that keep most information.

Example:
10 features → PCA → 3 principal components

---

### c) Attribute Subset Selection (Feature Selection)

It reduces data by **removing unnecessary attributes**.

Two types of bad attributes:

1. **Redundant attributes**

   * Give the same or similar information
   * Example:

     * Purchase price
     * Sales tax paid
       (Both are related, one can be derived from the other)

2. **Irrelevant attributes**

   * Not useful for the task
   * Example:

     * Student ID for predicting GPA

Simple idea:

> Keep only attributes that really help in prediction or analysis.

---

## Heuristic Methods for Attribute Selection

1. **Step-wise Forward Selection**

   * Start with no attributes
   * Add the best one at each step

2. **Step-wise Backward Elimination**

   * Start with all attributes
   * Remove the worst one at each step

3. **Combined Forward & Backward**

   * Add the best attribute
   * Remove the worst attribute
   * Do both at each step

4. **Decision Tree Induction**

   * Build a decision tree
   * Attributes used in the tree → important
   * Attributes not used → irrelevant

---

## One-line exam summary:

> Dimensionality reduction reduces the number of attributes using techniques like Wavelet Transform, PCA, and Attribute Subset Selection to improve efficiency and maintain important information.
