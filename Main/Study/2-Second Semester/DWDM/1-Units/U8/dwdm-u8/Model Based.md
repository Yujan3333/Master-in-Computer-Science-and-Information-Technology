Sure! Here’s a **complete, concise, exam-ready 5–mark answer** for **Model-Based Clustering**, combining **statistical** and **neural network approaches** with formulas.

---

## **Model-Based Clustering**

**Definition:**
Model-based clustering assumes that data is generated from a **mixture of underlying models** and assigns points to clusters by estimating model parameters to **maximize data likelihood**.

---

### **1️⃣ Statistical Approach (Gaussian Mixture Model)**

* Each cluster is a **probability distribution**, often Gaussian.
* Probability of a data point:

$$
P(x) = \sum_{i=1}^{k} \pi_i f_i(x|\theta_i)
$$

Where:

* $k$ = number of clusters
* $\pi_i$ = mixing proportion of cluster $i$
* $f_i(x|\theta_i)$ = probability density (Gaussian)
* $\theta_i$ = parameters (mean, covariance)

**Parameter estimation: EM Algorithm**

**E-step (compute membership probabilities):**
$$
\gamma_{ij} = P(C_j|x_i) = \frac{\pi_j f_j(x_i|\theta_j)}{\sum_{l=1}^{k} \pi_l f_l(x_i|\theta_l)}
$$

**M-step (update parameters):**
$$
\mu_j = \frac{\sum_i \gamma_{ij} x_i}{\sum_i \gamma_{ij}}, \quad
\Sigma_j = \frac{\sum_i \gamma_{ij} (x_i-\mu_j)(x_i-\mu_j)^T}{\sum_i \gamma_{ij}}, \quad
\pi_j = \frac{\sum_i \gamma_{ij}}{n}
$$

* Repeat E & M steps until convergence.
* Produces **soft clustering**: points have probabilities of belonging to clusters.

---

### **2️⃣ Neural Network Approach**

Neural network-based clustering uses **competitive learning** and **Self-Organizing Maps (SOM)**.

#### **a) Competitive Learning**

* Neurons represent **cluster centers**.
* For each input, the **closest neuron wins**.
* Update weights:

$$
w_i(t+1) = w_i(t) + \eta(t) , h_{ci}(t) , (x - w_i(t))
$$

Where:

* $w_i$ = neuron weight
* $x$ = input
* $\eta(t)$ = learning rate
* $h_{ci}(t)$ = neighborhood function (1 for winning neuron, less for neighbors)

#### **b) Self-Organizing Map (SOM)**

* Neurons arranged in a **grid** (1D or 2D).
* Preserves **topology**: similar inputs map to **nearby neurons**.
* **Algorithm:**

  1. Initialize neuron weights randomly.
  2. For each input, find **Best Matching Unit (BMU)**.
  3. Update BMU and neighbors using weight update formula.
  4. Decrease learning rate and neighborhood radius over time.
  5. After training, neurons represent clusters; points mapped to same/neighbour neurons belong to same cluster.

**Advantages:**

* Can detect **nonlinear, complex cluster shapes**
* Handles **high-dimensional data**
* Produces a **topological map** for visualization

---

### **3️⃣ Summary Table**

| Approach       | Method                     | Cluster Assignment   | Notes                                  |
| -------------- | -------------------------- | -------------------- | -------------------------------------- |
| Statistical    | EM / GMM                   | Soft (probabilistic) | Probabilistic, Gaussian-based          |
| Neural Network | Competitive Learning / SOM | Hard/soft via BMU    | Preserves topology, nonlinear clusters |

---

### **4️⃣ One-Line Exam Definition**

> Model-based clustering groups data assuming an underlying model; statistical approaches use probability distributions (EM, GMM), while neural network approaches (SOM) use competitive learning to adapt cluster centers.

---

