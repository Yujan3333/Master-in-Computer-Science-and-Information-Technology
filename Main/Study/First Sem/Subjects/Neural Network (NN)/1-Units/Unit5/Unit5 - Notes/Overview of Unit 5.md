### **Breakdown of the Content**

#### **Statistical Learning Theory**

This framework for machine learning uses statistics and functional analysis to find a predictive function based on data. It focuses on building models to draw conclusions and make predictions.

* **Data Types**: Two main types of data are identified:

  * **Dependent Variable (y)**: A variable whose values rely on other variables, sometimes called a *target variable.*
  * **Independent Variables (x)**: Variables whose values do not depend on others. These are also known as *predictor variables, input variables, explanatory variables, or features.*

* **Statistical Model**: Defines relationships between dependent and independent variables.
  For example:

  * A linear relationship between home size (x) and price (y):

    $$
    y = ax + b
    $$
  * If price depends on size ($x_1$) and number of bathrooms ($x_2$):

    $$
    y = ax_1 + bx_2 + c
    $$

- ==[Further Explanation of Statistical Model Example](Unit5%20-%20Notes/Further%20Explanation%20of%20Statistical%20Model%20Example.md)==

---

#### **Support Vector Machine (SVM)**

SVM is a popular supervised learning algorithm used for both classification and regression problems, though mainly used for classification.

* **Functionality**: SVM takes input data points and outputs a hyperplane (a line in 2D) that optimally separates the data into two classes. This hyperplane acts as a decision boundary.

* **Advantages**: Compared to newer algorithms like neural networks, SVMs provide high speed and good performance with smaller datasets (thousands of samples).

* **Support Vectors**: Data points closest to the hyperplane. They influence the position and orientation of the hyperplane.

* **Optimal Hyperplane**: SVM selects the hyperplane with the largest margin, called the **maximum marginal hyperplane (MMH)**.
  The **margin** is the distance between two planes ($H_1$ and $H_2$) that pass through the support vectors and are parallel to the decision boundary.

* **Types**:

  * **Linear SVM**: Used for linearly separable data points.
  * **Non-linear SVM**: Used when data is not linearly separable.
    It transforms low-dimensional data into high-dimensional linearly separable data using the **[Kernel Trick](../../Unit4/Unit4-Notes-Folder/Kernel%20Methods.md)**, then applies a linear hyperplane in that higher space.

---

#### **Support Vector Regression (SVR)**

SVR applies the same principle as SVM but is used for regression tasks. It aims to approximate a mapping from input space to real numbers.

* **Hyperplane**: The straight line that fits the data in SVR is also referred to as a hyperplane.

* **Key Hyperparameters**:

  * **Hyperplane**: Serves as the decision boundary for predicting continuous outputs.
    Support vectors are the data points closest to this line.
  * **Kernel**: A function that transforms the input data, typically used to find a hyperplane in higher-dimensional space.
  * **Boundary Lines**: Two lines are drawn around the hyperplane at a distance of $\epsilon$ (epsilon), creating a margin.
    The goal is to find the best-fit line with the maximum number of points within this margin.

* **Difference from Other Regression Models**:
  Unlike traditional regression models that minimize the error between real and predicted values, SVR attempts to fit the best line within a threshold value (epsilon margin).

* **Complexity**:
  SVR has more than quadratic time complexity with respect to the number of samples, making it hard to scale to large datasets (above a few thousand samples).

---

#### **Kernel Functions**

Kernel functions use the **kernel trick** to handle non-linear problems using linear classifiers. They do this by mapping training data into a higher-dimensional space where a non-linear decision surface becomes linear.

* **Popular Kernels**:

  * **Linear Kernel**:

    $$
    K(x_1, x_2) = x_1 \cdot x_2
    $$
  * **Polynomial Kernel**:

    $$
    K(x_1, x_2) = (x_1 \cdot x_2 + 1)^d
    $$

    where $d$ is the degree of the polynomial.
  * **Gaussian Kernel**: A type of radial basis function (RBF) kernel.
  * **Exponential Kernel**: Similar to the Gaussian kernel but without squaring the norm.
  * **Laplacian Kernel**: Similar in nature to the exponential kernel.

---
