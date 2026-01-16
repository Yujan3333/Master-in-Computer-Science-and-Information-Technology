
# **ICA Cheat Sheet (Independent Component Analysis)**

---

## **1️⃣ Definition**

> ICA extracts **statistically independent hidden sources** from observed mixtures.
> Unlike PCA (uncorrelated), ICA finds **independent** components.

**Mixing model:**

$$
X = A \cdot S
$$

**Recovery (unmixing):**

$$
S = W \cdot X, \quad W = A^{-1}
$$

Where:

| Symbol | Meaning                      |
| ------ | ---------------------------- |
| $X$    | Observed data (mixtures)     |
| $S$    | Independent sources (hidden) |
| $A$    | Mixing matrix (unknown)      |
| $W$    | Unmixing matrix              |

---

## **2️⃣ ICA Algorithm (FastICA / General)**

### **Step 1: Centering**

Subtract mean:

$$
X_{\text{centered}} = X - \text{mean}(X)
$$

### **Step 2: Whitening**

Make components uncorrelated & unit variance:

$$
X_{\text{white}} = V D^{-1/2} V^T X
$$

Where $(V, D)$ are eigenvectors & eigenvalues of covariance of $X$.

### **Step 3: Find independent components**

* Maximize **non-Gaussianity**
* Iteratively update weight vectors $w$:

$$
s = w^T X_{\text{white}}
$$

* Measures of non-Gaussianity:

  * **Kurtosis**
  * **Negentropy**: $J(y) = H(y_{\text{gauss}}) - H(y)$

* Normalize $w$: $|w| = 1$

* Use **deflation** to find next component.

### **Step 4: Recover sources**

$$
S = W \cdot X
$$

---

## **3️⃣ ICA vs PCA**

| Feature      | PCA                     | ICA                     |
| ------------ | ----------------------- | ----------------------- |
| Goal         | Uncorrelated components | Independent components  |
| Sensitive to | Variance                | Higher-order statistics |
| Assumption   | Gaussian                | Non-Gaussian            |
| Mixing       | Orthogonal              | Any invertible matrix   |

---

## **4️⃣ Simple Example (2×2)**

**2 mics recording 2 speakers**:

1. Center signals → zero mean
2. Whiten → remove correlation
3. Find weights $w_1, w_2$ maximizing independence
4. Recover independent signals:

$$
S_1, S_2 = W \cdot X
$$

Result: two separate voices (hidden sources).

---

## **5️⃣ Exam Memory Tips**

* **Model:** $X = A S$, $S = W X$
* **Steps:** Center → Whiten → Maximize non-Gaussianity → Recover $S$
* **ICA ≠ PCA:** ICA = independent, PCA = uncorrelated
* **FastICA trick:** iterative weight vector update + normalization

---
