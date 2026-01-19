## Backpropagation Algorithm (for Neural Network)

### Given

* Training set: ${(x,t)}$
* Learning rate: $\eta$
* Activation function: $f(.)$ (usually sigmoid)
  $$f(z)=\frac{1}{1+e^{-z}}$$

---

### Step 1: Initialize

Initialize all weights $w$ and biases $b$ with small random values.

---

### Step 2: Forward Pass

For each training example:

For hidden/output neuron:
$$net_j=\sum_i w_{ij}x_i+b_j$$
$$o_j=f(net_j)$$
![](../../../../../../../Images/Second_Sem_Images/Backpropagation%20Algorithm.png)



---

### Step 3: Compute Error

For output neuron:
$$E=\frac{1}{2}\sum(t_j-o_j)^2$$

Where
$t_j$ = target output
$o_j$ = actual output

![](../../../../../../../Images/Second_Sem_Images/Backpropagation%20Algorithm-1.png)

---

### Step 4: Backward Pass (Error Propagation)

For output layer:
$$\delta_j=o_j(1-o_j)(t_j-o_j)$$

For hidden layer:
$$\delta_j=o_j(1-o_j)\sum_k\delta_kw_{jk}$$

---

### Step 5: Update Weights

Weight update rule:
$$\Delta w_{ij}=\eta\delta_jx_i$$
$$w_{ij}=w_{ij}+\Delta w_{ij}$$

Bias update:
$$b_j=b_j+\eta\delta_j$$

---

### Step 6: Repeat

Repeat Steps 2–5 for all training samples until:

* Error is minimized, or
* Maximum epochs reached.

---

### One-line Exam Definition

> Backpropagation is a supervised learning algorithm that minimizes error by adjusting weights using gradient descent and backward propagation of errors.

---

### Flow (to remember in exam)

1. Initialize weights
2. Forward pass
3. Compute error
4. Backward pass
5. Update weights
6. Repeat until convergence

This is the **standard backpropagation algorithm** expected in exams.
