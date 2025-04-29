#### 1. Initialization
Randomly choose `K` data points from the training set as initial cluster centers:

$μ_1,μ_2,...,μ_K​$

---
#### 2. Sampling
Draw a sample vector `x` from the training set.
##### ==🧠More Info==
Pick one of the data points from the training set
👉`Training data={(1,1),(2,1),(4,3),(5,4)}`
✍️ `x=(2,1)` *is chosen to find which cluster it belongs to?*

---
#### 3. Similarity Matching
Compute the Euclidean distance between x and each cluster center $μ_k$​:

![](../../../../../../Images/Training%20RBF%20Hidden%20Layer%20Using%20K-means.png)

This gives you the **closest cluster center** (winning cluster).

##### ==🧠More Info==
👉 “Find the **closest cluster center** $μ_k$​ to the point x.”
❗ [More on Similarity matching](More%20on%20Similarity%20matching.md)

---
#### 4. Update Cluster Center
Update the winning cluster center using a learning rate α\alphaα:

$\mu_k=μ_k+\alpha(x−\mu_k)$


This makes the center shift slightly toward the new sample.
**Repeat this process for several iterations or until convergence.**

#### 5. Once RBF Centers (µ) are chosen, we need to compute **Sigma (σ)**

Sigma controls the **spread** of the radial basis function (e.g., Gaussian). There are **two common approaches** to compute it:

---

##### 📐 Method 1: Based on maximum distance

$\sigma = \frac{d_{max}}{\sqrt{2K}}$

![](../../../../../../Images/Training%20RBF%20Hidden%20Layer%20Using%20K-means-1.png)

This spreads the RBFs just enough to overlap.

---

##### 📊 Method 2: Based on average distance to all centers

$\sigma = \sqrt{\frac{1}{P} \sum_{k=1}^{P} (x - x_k)^2}$

![](../../../../../../Images/Training%20RBF%20Hidden%20Layer%20Using%20K-means-2.png)

Where:
- $P$ = number of centers
- $x$ = data point / center point 
- $x_k​$ = each center / neighboring point

This gives a more **data-driven estimate** of the spread.

---

### 🧩 Why is **σ** important?

In a [Gaussian RBF](Gaussian%20Kernel.md):

$\phi(x) = \exp\left( -\frac{\|x - \mu\|^2}{2\sigma^2} \right)$

σ determines how "*wide*" or "*narrow*" each Gaussian is:
- **Large σ** → smoother curve, more generalization
- **Small σ** → sharper curve, more sensitive to nearby points

---
---
### [Numerical On RBF Hidden Layer Using K-means](Numerical%20On%20RBF%20Hidden%20Layer%20Using%20K-means.md)
- Consider the XOR problem. Define two RBF centers and calculate the value of sigma for the RBF.