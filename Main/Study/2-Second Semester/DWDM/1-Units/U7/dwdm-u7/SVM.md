## Support Vector Machine (SVM)

SVM is a **supervised learning algorithm** used for **classification and prediction** that finds the **optimal separating hyperplane** between classes.

Main idea:

> Choose the hyperplane that maximizes the **margin** between two classes.

---

For linearly separable data:

Hyperplane:
$$w\cdot x + b = 0$$

Two class boundaries:
$$w\cdot x + b = 1$$
$$w\cdot x + b = -1$$

Margin:
$$\text{Margin}=\frac{2}{|w|}$$

SVM maximizes this margin.

---

Classification rule:
$$y=\text{sign}(w\cdot x + b)$$

Where
$y$ = class label (+1 or −1)

---

For non-linear data → use **Kernel trick**

Common kernels:

1. Linear:
   $$K(x,y)=x\cdot y$$

2. Polynomial:
   $$K(x,y)=(x\cdot y + c)^d$$

3. RBF (Gaussian):
   $$K(x,y)=e^{-\gamma|x-y|^2}$$

4. Sigmoid:
   $$K(x,y)=\tanh(\alpha x\cdot y + c)$$

---

Soft margin (allowing errors):

Objective:
$$\min\frac{1}{2}|w|^2 + C\sum\xi_i$$

Where
$C$ = penalty parameter
$\xi_i$ = slack variables

---

Advantages:

* Works well in high dimensions
* Strong theoretical foundation
* High accuracy

Disadvantages:

* Computationally expensive
* Choice of kernel is critical
* Less interpretable

---

One-line exam definition:

> SVM is a classifier that finds the optimal hyperplane with maximum margin to separate classes, using kernel functions for non-linear data.
