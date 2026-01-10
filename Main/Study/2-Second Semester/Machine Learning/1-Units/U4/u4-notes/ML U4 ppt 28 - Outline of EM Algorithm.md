
### **EM Algorithm Outline**

**Step 1: Initialization**
Initialize the parameters $\mu_k$, $\sigma_k$, and $p_k$, and evaluate the log-likelihood:
$$
\mathcal{L}({\mu_k, \sigma_k, p_k}) = \sum_{i=1}^{n} \log \left( \sum_{k=1}^{K} p_k , \mathcal{N}(x_i \mid \mu_k, \sigma_k^2) \right)
$$

---

**Step 2: E-step**
Evaluate the **posterior probabilities** $\gamma_{z_i}(k)$ using current parameter values:
$$
\gamma_{z_i}(k) = P(z_i = k \mid x_i, \mu_k, \sigma_k, p_k) = \frac{p_k , \mathcal{N}(x_i \mid \mu_k, \sigma_k^2)}{\sum_{j=1}^{K} p_j , \mathcal{N}(x_i \mid \mu_j, \sigma_j^2)}
$$

---

**Step 3: M-step**
Update parameters $\mu_k$, $\sigma_k$, and $p_k$ using $\gamma_{z_i}(k)$:
$$
\mu_k^{\text{new}} = \frac{\sum_{i=1}^{n} \gamma_{z_i}(k) , x_i}{\sum_{i=1}^{n} \gamma_{z_i}(k)}, \quad
\sigma_k^{2,\text{new}} = \frac{\sum_{i=1}^{n} \gamma_{z_i}(k) (x_i - \mu_k^{\text{new}})^2}{\sum_{i=1}^{n} \gamma_{z_i}(k)}, \quad
p_k^{\text{new}} = \frac{1}{n} \sum_{i=1}^{n} \gamma_{z_i}(k)
$$

---

**Step 4: Convergence Check**
Compute the new log-likelihood with updated parameters:
$$
\mathcal{L}^{\text{new}} = \sum_{i=1}^{n} \log \left( \sum_{k=1}^{K} p_k^{\text{new}} , \mathcal{N}(x_i \mid \mu_k^{\text{new}}, \sigma_k^{2,\text{new}}) \right)
$$

If the change in log-likelihood is less than some small $\epsilon$:
$$
|\mathcal{L}^{\text{new}} - \mathcal{L}^{\text{old}}| < \epsilon
$$
stop; otherwise, return to **Step 2**.

---