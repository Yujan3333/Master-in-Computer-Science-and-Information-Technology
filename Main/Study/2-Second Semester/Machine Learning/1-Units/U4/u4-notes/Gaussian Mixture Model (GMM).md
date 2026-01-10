# Gaussian Mixture Models (GMM) and EM 
- [ML U4 ppt 25](ML%20ppt%2025.md)
- [ML U4 ppt 28 - Outline of EM Algorithm](ML%20U4%20ppt%2028%20-%20Outline%20of%20EM%20Algorithm.md)

## 1. What is a Gaussian Mixture Model (GMM)?

- A **GMM models data as a mixture of several Gaussian (normal) distributions**.
- Each Gaussian represents a **cluster**.
- It is a **soft clustering method**, meaning:
  - A data point can belong to **multiple clusters with probabilities**, unlike K-Means (hard clustering).  
  - Example: For \(k=3\), a point can belong to \(C_1\) with probability 0.7 and \(C_2\) with 0.3.

## 2. Why Soft Clustering?

| Method                             | Type | Assignment of Points                              |
| ---------------------------------- | ---- | ------------------------------------------------- |
| Partition / Hierarchical / Density | Hard | Each point goes to exactly **one cluster**        |
| Gaussian Mixture Model (GMM)       | Soft | Each point has **probabilities for all clusters** |

## 3. The Model

- Suppose we have \(K\) clusters (mixture components).
- Each data point \(x_i\) is sampled from one of these Gaussian components.

**Latent variable:**

$$
z_i \in \{1, \dots, K\}
$$

- \(z_i\) indicates **which cluster generated \(x_i\)**.
- Usually **not observed**, so it’s a **latent variable**.

**Probability of a data point:**

$$
p(x_i) = \sum_{k=1}^{K} p_k f_k(x_i)
$$

Where:

- \(p_k\) = **mixing proportion** (probability that \(x_i\) belongs to cluster \(k\)), with \(\sum_{k=1}^{K} p_k = 1\)
- \(f_k(x)\) = **Gaussian pdf** of cluster \(k\):

$$
f_k(x) = \frac{1}{\sigma_k \sqrt{2\pi}} \exp\Big(-\frac{(x - \mu_k)^2}{2\sigma_k^2}\Big)
$$

## 4. EM Algorithm for GMM

The **Expectation-Maximization (EM)** algorithm estimates parameters \((\mu_k, \sigma_k^2, p_k)\) when **latent variables exist**.

### Steps

**Step 0: Initialize**

- Choose initial \(\mu_k, \sigma_k, p_k\)
- Evaluate log-likelihood

**Step 1: E-Step (Expectation)**

Compute probability that each point belongs to each cluster:

$$
y_{ik} = P(z_i = k \mid x_i) = \frac{p_k f_k(x_i)}{\sum_{j=1}^{K} p_j f_j(x_i)}
$$

**Step 2: M-Step (Maximization)**

Update parameters using \(y_{ik}\):

$$
N_k = \sum_{i=1}^{n} y_{ik}
$$

$$
\mu_k = \frac{1}{N_k} \sum_{i=1}^{n} y_{ik} x_i
$$

$$
\sigma_k^2 = \frac{1}{N_k} \sum_{i=1}^{n} y_{ik} (x_i - \mu_k)^2
$$

$$
p_k = \frac{N_k}{n}
$$

**Step 3: Convergence**

- Repeat E-Step and M-Step until **log-likelihood changes very little**.

## 5. Example

Data points:

$$
X = \{1,2,3,6,10,11,12\}, \quad K = 2
$$

**Initial parameters:**

$$
\mu_1 = 1, \quad \mu_2 = 10, \quad \sigma_1 = \sigma_2 = 0.8, \quad p_1 = p_2 = 0.5
$$

**Step 1: E-step**

Compute probability for each point \(x_i\) belonging to each cluster:

$$
y_{i1} = \frac{p_1 f_1(x_i)}{p_1 f_1(x_i) + p_2 f_2(x_i)}, \quad
y_{i2} = 1 - y_{i1}
$$

**Step 2: M-step**

Update parameters:

$$
N_1 = \sum_i y_{i1}, \quad N_2 = \sum_i y_{i2}
$$

$$
\mu_1 = \frac{\sum_i y_{i1} x_i}{N_1}, \quad \mu_2 = \frac{\sum_i y_{i2} x_i}{N_2}
$$

$$
\sigma_1^2 = \frac{\sum_i y_{i1} (x_i - \mu_1)^2}{N_1}, \quad
\sigma_2^2 = \frac{\sum_i y_{i2} (x_i - \mu_2)^2}{N_2}
$$

$$
p_1 = \frac{N_1}{n}, \quad p_2 = \frac{N_2}{n}
$$

- Repeat E and M steps **until convergence**.

## 6. Summary – Key Points

- **GMM** = soft clustering using Gaussian distributions
- Each cluster has: \(\mu_k, \sigma_k^2, p_k\)
- **EM Algorithm** = iterative method to estimate these parameters
- **Soft assignments** = probabilities of belonging to each cluster
- Unlike K-Means, **data points can belong to multiple clusters**

**Exam Tip:**

- GMM → Soft clustering, Gaussian distributions
- EM → E-step (probabilities), M-step (update parameters)
- Formulas for **E-step and M-step** are enough for numerical questions
