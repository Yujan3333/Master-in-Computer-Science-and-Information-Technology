
## ✅ **Unit 2 Summary: Linear Models for Regression and Classification**

### 🔹 1. **Polynomial Curve Fitting**

* Fit a polynomial function to data.
* Uses **least squares** to find best-fit coefficients.
* Suffers from **overfitting** if degree is too high.

### 🔹 2. **Bayesian Curve Fitting**

* Probabilistic approach to curve fitting.
* Places **priors** over parameters and computes **posterior distribution**.
* Helps handle overfitting by incorporating **model uncertainty**.

### 🔹 3. **Linear Basis Function Models**

* Transform input features using **basis functions** (e.g., polynomials, Gaussians).
* Model becomes linear in transformed space, allowing flexibility.

### 🔹 4. **Bias-Variance Decomposition**

* Splits expected error into:

  * **Bias**: Error from wrong assumptions in model.
  * **Variance**: Error from model’s sensitivity to training data.
  * **Noise**: Irreducible error in the data.

### 🔹 5. **Bayesian Linear Regression**

* Linear regression + Bayesian treatment.
* Predictive distribution is a Gaussian.
* Output includes **mean prediction** and **uncertainty** (variance).

### 🔹 6. **Least Squares for Classification**

* Applies least squares (normally for regression) to classification tasks.
* Not optimal — leads to issues like poor probability estimation.
* Better alternatives exist (e.g., logistic regression).

### 🔹 7. **Logistic Regression for Classification**

* Models the probability of class using a **sigmoid function**.
* Trained using **maximum likelihood estimation**.
* Suitable for binary classification tasks.

### 🔹 8. **Bayesian Logistic Regression**

* Logistic regression + Bayesian treatment.
* Computes posterior distribution over weights.
* Usually solved using **approximations** (like Laplace method), since exact inference is intractable.

---

## 📌 **Important Exam Questions (Theory + Numerical)**

### 🔹 **Short/Conceptual**

1. What is the difference between least squares and Bayesian linear regression?
2. Define bias and variance. Explain bias-variance tradeoff.
3. Explain the role of basis functions in linear models.
4. What are the limitations of least squares for classification?

### 🔹 **Long/Descriptive**

1. Derive the polynomial curve fitting equations and explain overfitting.
2. Explain Bayesian curve fitting with mathematical formulation.
3. Explain logistic regression. Derive the cost function using likelihood.
4. Discuss Bayesian linear regression with derivation of predictive distribution.
5. Explain bias-variance decomposition in detail with graphical intuition.
6. Derive the update rule for weights in logistic regression using gradient descent.

### 🔹 **Numerical**

1. Given a set of points, fit a polynomial using least squares (degree n).
2. Perform bias-variance calculation for a given model setup.
3. Given features and labels, compute logistic regression weights (manually or using gradient steps).

---

