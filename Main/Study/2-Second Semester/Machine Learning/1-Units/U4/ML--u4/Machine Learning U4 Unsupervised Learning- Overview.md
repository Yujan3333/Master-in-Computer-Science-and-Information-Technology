# 📘 **Unit 4: Unsupervised Learning –  SUMMARY**

---

## ✅ **MOST IMPORTANT TOPICS:**

### 1. **Clustering Basics**
- **Goal**: Group similar objects together
- **Cluster**: Collection of similar objects (within) + dissimilar to other clusters
- **Applications**:
  - Customer segmentation
  - Outlier detection (fraud, crime monitoring)
  - Image compression
  - Document organization

---

### 2. **Distance Metrics – MUST KNOW!**

**Euclidean Distance** (L₂ norm):
$$
d(x,y) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

**Manhattan Distance** (L₁ norm):
$$
d(x,y) = |x_2 - x_1| + |y_2 - y_1|
$$

**Minkowski Distance** (Generalized):
$$
d(x,y) = \left( |x_2 - x_1|^p + |y_2 - y_1|^p \right)^{1/p}
$$
- $p=1$ → Manhattan
- $p=2$ → Euclidean

---

### 3. **Clustering Algorithms – 4 Types**

#### **A. Partitioning Methods**
- **K-Means** (Most important!)
  - Divides data into **k clusters**
  - Each cluster has a **centroid**
  - Minimizes within-cluster variance

#### **B. Hierarchical Methods**
- **Agglomerative** (Bottom-up)
  - Start: each point as separate cluster
  - Merge closest clusters repeatedly
- **Divisive** (Top-down)
  - Start: all points in one cluster
  - Split clusters repeatedly

#### **C. Density-Based Methods** (e.g., DBSCAN)
- Finds arbitrarily shaped clusters
- Continues growing cluster while neighborhood density > threshold
- Good for outlier detection

#### **D. Model-Based Methods** (e.g., GMM)
- Assume data from mixture of probability distributions
- **Gaussian Mixture Models (GMM)** – Soft clustering

---

## 🎯 **K-MEANS ALGORITHM – DETAILED**

### Steps:
1. **Initialize**: Randomly choose k centroids
2. **Assign**: Each point to nearest centroid
   $$ c^{(i)} = \arg\min_j ||x^{(i)} - \mu_j||^2 $$
3. **Update**: Recalculate centroids
   $$ \mu_j = \frac{\sum_{i=1}^m 1\{c^{(i)} = j\} x^{(i)}}{\sum_{i=1}^m 1\{c^{(i)} = j\}} $$
4. **Repeat** until convergence (no reassignments)

### Problem: **Initialization Sensitivity**
- Random centroids → different results
- **Solution**: **K-Means++** (smarter initialization)

---

## 🔧 **K-Means++ Initialization**
1. Pick first centroid randomly
2. For each point, compute distance to nearest chosen centroid
3. Choose next centroid with probability **proportional to distance²**
4. Repeat until k centroids

---

## 📊 **GAUSSIAN MIXTURE MODELS (GMM)**

### Key Points:
- **Soft clustering** (probabilistic assignments)
- Each cluster = Gaussian distribution
- Point can belong to multiple clusters with probabilities

### Probability Formula:
For data point $x_i$:
$$
p(x_i) = p_1 f_1(x_i) + p_2 f_2(x_i) + \dots + p_k f_k(x_i)
$$
Where:
- $p_k$ = mixture weight (probability of component k)
- $f_k(x) = \frac{1}{\sigma_k\sqrt{2\pi}} e^{-\frac{(x-\mu_k)^2}{2\sigma_k^2}}$

### EM Algorithm for GMM:
1. **E-step**: Compute posterior probabilities
   $$ \gamma_{nk} = \frac{p_k f_k(x_n)}{\sum_{j=1}^K p_j f_j(x_n)} $$
2. **M-step**: Update parameters
   $$ \mu_k = \frac{\sum_n \gamma_{nk} x_n}{\sum_n \gamma_{nk}} $$
   $$ \sigma_k^2 = \frac{\sum_n \gamma_{nk} (x_n - \mu_k)^2}{\sum_n \gamma_{nk}} $$
   $$ p_k = \frac{\sum_n \gamma_{nk}}{N} $$

---

## 📉 **DIMENSIONALITY REDUCTION**

### Why Reduce Dimensions?
- Curse of dimensionality
- Visualization
- Remove noise/redundancy
- Faster computation

### Methods:

#### **1. Feature Selection**
- Select subset of original features
- $$ K < N $$ dimensions

#### **2. Feature Extraction**
- Create new features from originals
- **PCA** (Most important!)

---

## 🎯 **PRINCIPAL COMPONENT ANALYSIS (PCA)**

### Steps:
1. **Standardize** data
2. **Covariance Matrix**:
   $$ \text{Cov}(X_i,X_j) = \frac{1}{n-1}\sum_{k=1}^n (x_{ik}-\bar{x}_i)(x_{jk}-\bar{x}_j) $$
3. **Eigenvectors & Eigenvalues** of covariance matrix
4. **Sort** eigenvectors by eigenvalues (descending)
5. **Project** data: $P_{ij} = e_i^T \cdot (x_j - \bar{x})$

### Properties of PCs:
- Linear combinations of original features
- Orthogonal (uncorrelated)
- First PC has max variance

---

## 📝 **SINGULAR VALUE DECOMPOSITION (SVD)**
For matrix $A_{m\times n}$:
$$ A = U S V^T $$
Where:
- $U$: Left singular vectors (m×m)
- $S$: Diagonal matrix of singular values (m×n)
- $V^T$: Right singular vectors (n×n)

Used for: **Low-rank approximation**, LSI (Latent Semantic Indexing)

---

## 🔍 **LATENT SEMANTIC INDEXING (LSI/LSA)**
- Dimensionality reduction for text
- Uses SVD on term-document matrix
- Groups similar words/documents

---

## 🧮 **FACTOR ANALYSIS**
- Explains variance among observed variables
- Finds latent (unobserved) factors
- Steps:
  1. Adequacy test (Bartlett's, KMO)
  2. Determine # factors (eigenvalues > 1)
  3. Interpret factors (loadings)

---

## 🚨 **EXAM FOCUS AREAS:**
1. **K-Means steps & calculations** (manual iteration)
2. **Distance metrics formulas**
3. **GMM vs K-Means** (hard vs soft clustering)
4. **PCA steps & covariance calculation**
5. **Difference between clustering types**
6. **K-Means++ initialization**

---

## 📚 **Quick Comparison Table**

| Method | Type | Key Feature |
|--------|------|-------------|
| **K-Means** | Partitioning | Hard clustering, spherical clusters |
| **GMM** | Model-based | Soft clustering, probabilistic |
| **Hierarchical** | Hierarchical | Tree structure (dendrogram) |
| **DBSCAN** | Density-based | Arbitrary shapes, outlier detection |
| **PCA** | Dim. Reduction | Linear, orthogonal components |

---

## 💡 **Memory Tricks:**
- **K-Means**: "Assign → Update → Repeat"
- **GMM**: "Expectation → Maximization → Repeat"
- **PCA**: "Covariance → Eigen → Project"
- **Hard clustering**: 1 cluster per point
- **Soft clustering**: Probabilities to multiple clusters
