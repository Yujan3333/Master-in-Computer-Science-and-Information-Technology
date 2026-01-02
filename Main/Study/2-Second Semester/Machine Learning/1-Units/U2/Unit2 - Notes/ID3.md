## ID3 (Iterative Dichotomiser 3)

**ID3** stands for **Iterative Dichotomiser 3**.
It is a decision tree induction algorithm that uses a **top-down greedy approach** to build a decision tree.

At each step, ID3:

* Computes **Information Gain** for every attribute
* Selects the attribute with the **highest information gain** as the splitting attribute

---

## Information Gain

**Information Gain (IG)** measures the **reduction in uncertainty (entropy)** after splitting the dataset on an attribute.

It is calculated by comparing:

* Entropy **before splitting**
* Entropy **after splitting**

---

## Entropy

**Entropy** is a measure of the **homogeneity or impurity** of a dataset.
If all tuples belong to the same class, entropy is **0**.

### Entropy of Dataset $D$ (Equation 1)

$$
Entropy(D) = - \sum_{i=1}^{m} p_i \log_2 p_i
$$

where:

* $m$ = number of classes
* $p_i$ = probability that a tuple in $D$ belongs to class $C_i$

---

### Probability of Class $C_i$ (Equation 2)

$$
p_i = \frac{|C_i|}{|D|}
$$

where:

* $|C_i|$ = number of tuples belonging to class $C_i$
* $|D|$ = total number of tuples in dataset $D$

---

## Entropy After Splitting on Attribute $A$

Suppose attribute $A$ has **$v$ distinct values**
Then dataset $D$ is partitioned into subsets:

$$
{D_1, D_2, \dots, D_v}
$$

### Expected Entropy After Partitioning (Equation 3)

$$
Entropy_A(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times Entropy(D_j)
$$

where:

* $|D_j|$ = number of tuples in partition $D_j$

---

## Information Gain of Attribute $A$

### Information Gain Formula (Equation 4)

$$
Gain(A) = Entropy(D) - Entropy_A(D)
$$

or,

$$
Gain(A) = Entropy(D) - \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times Entropy(D_j)
$$

---

## Attribute Selection Rule in ID3

* Compute **Information Gain** for all attributes
* Choose the attribute with **maximum information gain**
* Split the dataset on that attribute
* Repeat the process recursively until stopping conditions are met

---

### 🔹 One-Line Exam Conclusion

> ID3 constructs a decision tree using a top-down greedy approach by selecting the attribute with the highest information gain, which is based on entropy reduction.

---
