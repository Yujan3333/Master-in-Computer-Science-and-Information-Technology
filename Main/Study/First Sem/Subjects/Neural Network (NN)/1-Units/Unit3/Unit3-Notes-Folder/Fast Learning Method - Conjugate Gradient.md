
### **Fast Learning Method: Conjugate Gradient**

* **Problem with Gradient Descent**:

  * Updates along steepest descent (negative gradient).
  * Leads to a **zigzag convergence path** due to orthogonal directions in successive steps.
  * Learning rate is fixed, which may not ensure optimal step size.

---

### **Conjugate Gradient Overview**:

* Improves over gradient descent by minimizing zigzagging and capturing the overall direction toward the minimum.

* **Step Size ($\alpha_k$)**:

  * Adaptively chosen in each iteration by performing a **line search** to minimize the cost function along the current direction.

* **Direction Update Rule**:

  $$
  d_0 = -g_0 \quad (\text{start with steepest descent})
  $$

  $$
  d_k = -g_k + \beta_k d_{k-1}
  $$

  * $\beta_k$: **Conjugate parameter** (ensures new direction is conjugate to previous).

* **Fletcher-Reeves Formula** (to compute $\beta_k$):

  $$
  \beta_k = \frac{g_k^T g_k}{g_{k-1}^T g_{k-1}}
  $$

* **Weight Update**:

  $$
  w_{k+1} = w_k + \alpha_k d_k
  $$

---

### **Advantages**:

* Faster and smoother convergence than gradient descent.
* Reduces zigzag behavior.
* **No need to manually set learning rate**—step size is optimized.

### **Limitation**:

* More effective when the number of parameters is small (computational cost increases with size).

---
