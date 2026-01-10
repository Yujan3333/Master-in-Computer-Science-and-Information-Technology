## **1. Observed Data and Mixture Components**

* Suppose we have **data points**:
  $$
  {x_1, x_2, \dots, x_n}
  $$
* Each data point comes from **one of $K$ clusters (mixture components)**.
* Example: Heights of people; clusters = ${\text{male}, \text{female}}$.

---

## **2. Latent Variables ($z_i$)**

* Each data point ($x_i$) has a **hidden label** ($z_i$) indicating **which cluster it came from**.
* In our example:

  * $z_i = 1 \implies$ male
  * $z_i = 2 \implies$ female
* **Important:** We **do not observe** $z_i$ in the data.
  That’s why it’s called a **latent variable (hidden variable)**.

---

## **3. Probability of a Data Point**

Using the **law of total probability**, the probability of $x_i$ is:
$$
p(x_i) = p_1 f_1(x_i) + p_2 f_2(x_i) + \dots + p_K f_K(x_i)
$$

Where:

* $p_k$ = **mixture weight** or proportion → probability that a randomly chosen point comes from cluster $k$

  * Must satisfy: $p_k \ge 0$ and $\sum_{k=1}^{K} p_k = 1$

* $f_k(x_i)$ = **Gaussian probability density** for cluster $k$:
  $$
  f_k(x) = \frac{1}{\sigma_k \sqrt{2\pi}} , e^{-\frac{(x - \mu_k)^2}{2\sigma_k^2}}
  $$
  Where:

* $\mu_k$ = mean of cluster $k$

* $\sigma_k$ = standard deviation of cluster $k$

---

## **4. What this means intuitively**

1. **Each cluster is modeled as a Gaussian distribution.**

   * Male heights → one Gaussian
   * Female heights → another Gaussian

2. **The mixture probability $p(x_i)$ combines all clusters.**

   * Each cluster contributes to the probability of seeing $x_i$
   * Weighted by $p_k$, which tells us **how common that cluster is**

3. **Latent variables $z_i$** represent the **hidden cluster membership** of each point.

---

### **Simple Example**

Suppose:

* Cluster 1: Male → mean $(\mu_1 = 170)$, std $(\sigma_1 = 5)$
* Cluster 2: Female → mean $(\mu_2 = 160)$, std $(\sigma_2 = 5)$
* Mixture weights: $p_1 = 0.6$, $p_2 = 0.4$

Height $x_i = 165$ → probability:
$$
p(x_i) = 0.6 \cdot f_1(165) + 0.4 \cdot f_2(165)
$$

* $f_1(165)$ → likelihood that 165 comes from male
* $f_2(165)$ → likelihood that 165 comes from female
* $p(x_i)$ → overall probability of seeing 165 in the population

---

### **Key Points for Exam**

* **GMM** = Gaussian Mixture Model → soft clustering
* **Latent variables ($z_i$)** = hidden cluster labels
* **Mixture weights ($p_k$)** = probability that a data point comes from cluster $k$
* **$f_k(x)$** = Gaussian pdf of cluster $k$

---
