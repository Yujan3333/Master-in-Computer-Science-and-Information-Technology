
### 🔥 **Boltzmann Machine Summary**

A **Boltzmann Machine** is a type of **recurrent neural network** composed of **stochastically activated binary neurons**. It is used for learning patterns and optimizing solutions in binary datasets.

![](../../../../../../../../Images/First_Sem_Images/Boltzman%20Machine.png)

---

### 🔑 **Key Features:**

* **Stochastic Neurons**:
  Each neuron randomly chooses to be active (`1`) or inactive (`0`), based on probability.

* **Recurrent Structure**:
  All neurons are **symmetrically connected**, forming loops (i.e., recurrent connections).

* **Binary States**:
  Neurons can only be in one of two states: `0` (off) or `1` (on).

* **Clamped vs Adaptive Neurons**:

  * *Clamped*: Fixed input values (e.g., known data).
  * *Adaptive*: Learn from data and adjust.

* **Simulated Annealing**:
  If **simulated annealing** is applied to a **discrete Hopfield network**, it becomes a Boltzmann Machine.

* **Learning**:
  It uses a **simple learning algorithm** to **discover hidden features** in binary datasets by adjusting weights.

* **Optimization**:
  The primary goal is to **optimize weights and outputs** for a given problem, similar to energy minimization.

---

### 🧱 **Architecture Highlights:**

* Neurons are arranged in a **2D grid** (conceptually).
* **Weights** between units are **negative values**: `–p` (where `p > 0`)
* **Self-connection weights** (biases) are **positive**: `b` (where `b > 0`)

---

### 📌 **Applications:**

* Feature learning
* Combinatorial optimization
* Generative modeling (especially **Restricted Boltzmann Machines**, RBMs, a simplified variant)

---
