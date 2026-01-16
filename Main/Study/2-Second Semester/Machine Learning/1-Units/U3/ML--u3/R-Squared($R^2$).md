## **1️⃣ What is R-squared?**

* R-squared is a metric that tells us **how well a regression model explains the variability of the target variable**.
* It is also called the **coefficient of determination**.
* **Range:** 0 to 1 (sometimes negative if the model is really bad)

**Interpretation:**

* R² = 0 → model explains **none** of the variability
* R² = 1 → model explains **all** the variability
* Higher R² → better model fit

---

## **2️⃣ Formula**

R-squared is calculated as:


$$R^2 = 1 - \frac{\sum_{i=1}^{N} (y_i - \hat{y}*i)^2}{\sum*{i=1}^{N} (y_i - \bar{y})^2}$$


Where:

* ($y_i$) = actual value of the i-th observation
* $(\hat{y}_i)$ = predicted value of the i-th observation
* $(\bar{y})$ = mean of actual values
* N = number of observations

---

### **3️⃣ Explanation**

1. Numerator → **Residual Sum of Squares (RSS)** → sum of squared errors
2. Denominator → **Total Sum of Squares (TSS)** → total variation in actual data
3. 1 − (RSS/TSS) → fraction of variance explained by the model

✅ Higher R² means **the model predictions are closer to actual values**.

---
