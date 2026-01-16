
![](../../../../../../../Images/Second_Sem_Images/Locally%20Weighted%20Regression-fig.png)

## Locally Weighted Regression (LWR)

### 1. What is Locally Weighted Regression?

Locally Weighted Regression is a regression technique where **prediction is made using nearby data points** instead of the whole dataset.

> Nearby points influence the prediction more than faraway points.

---

### 2. Key Idea (Most Important)

* There is **no fixed reference point** in advance.
* The **reference point is the query point** (the value of x where we want to predict y).

Example:

* If we want to predict y at x = 2.5
* Then x = 2.5 is the **reference (query) point**

---

### 3. How are “near” and “far” points decided?

* Take **all training points**
* Compute distance of each training point from the query point
* Assign **higher weight to closer points**
* Assign **lower weight to distant points**

No manual selection of points is done.

---

### 4. Weight Function (Concept)

Weights are usually assigned using a **Gaussian kernel**:

$$w^{(i)} = \exp\left(-\frac{(x^{(i)} - x_q)^2}{2\tau^2}\right)$$

Where:

* $x_q$ = query point
* $x^{(i)}$ = training point
* $\tau$ = bandwidth (controls locality)


*The Closer the value of w to 1 nearer it is*
[Value of w(i) in the LWR](Value%20of%20w(i)%20in%20the%20LWR.md)

---

### 5. Role of Bandwidth (τ)

* Small τ → very local → risk of **overfitting**
* Large τ → almost global → risk of **underfitting**

---

### 6. Important Characteristics

* No single global model
* A **new model is fitted for every query point**
* Non-parametric method
* Also called **lazy learning**

---

### 7. Advantages

* Captures local patterns
* Works well for non-linear data
* Flexible and adaptive

---

### 8. Disadvantages

* Computationally expensive
* Slow for large datasets
* Needs to store all training data

---

### 9. Simple Intuition

Think of a **spotlight** centered at the query point:

* Bright near the center → nearby points matter more
* Dim far away → distant points matter less

---

### 10. One-Line Exam Definition

Locally Weighted Regression is a non-parametric regression technique that predicts output by fitting a model to nearby data points, giving higher weight to points closer to the query point.

---

### 11. Exam Tip

Always mention:

* Query point as reference
* Distance-based weighting
* Effect of τ on overfitting and underfitting

---
---

Here is your content **cleanly written in pure LaTeX**, fully **Obsidian / GitHub friendly**, using **only $...$ for math** (no code blocks, no backticks).

---

## 🔹 **Cost / Error Function in Locally Weighted Regression**

In **Locally Weighted Regression**, we minimize a **weighted squared error** instead of ordinary least squares.

The cost function is given by:

$$E = \frac{1}{2n} \sum_{i=1}^{n} w_i \left( y_i - a_0 - a_1 x_i \right)^2$$

---

🔹 **Where:**

$y_i$ = actual output

$a_0 + a_1 x_i$ = predicted output [Confusion in the ith part](Confusion%20in%20the%20ith%20part.md)

$w_i$ = weight of the $i$-th data point

$n$ = number of training samples

---

🔹 **Key Intuition**

Closer points (larger $w_i$) contribute more to the error

Far points (smaller $w_i$) contribute less

---

🔹 **Important Notes (Exam-Oriented)**

This method is called **Weighted Least Squares**

For each query point:

* different weights are assigned
* a different cost function is formed
* a different local model is learned

The factor $\frac{1}{2n}$ is used for **mathematical convenience**

Sometimes the cost function is written as:

$$E = \frac{1}{2} \sum_{i=1}^{n} w_i \left( y_i - a_0 - a_1 x_i \right)^2$$

Both forms are correct

Both give the same optimal solution

---

🔹 **One-Line Exam Statement (Very Safe)**

In locally weighted regression, the cost function is a weighted least squares error where data points closer to the query point are assigned higher weights.

---
