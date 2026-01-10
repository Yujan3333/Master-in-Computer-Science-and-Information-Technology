
### 📌 **2081 (C.Sc. 561)**

**Group A:**

1. **Q1:** Fit the logistic regression model through the following data. Show two epochs of training.  


|       | Sample 1 | Sample 2 | Sample 3 | Sample 4 |
| ----: | :------: | :------: | :------: | :------: |
| (x_1) |    0.8   |    0.3   |    0.6   |    0.4   |
| (x_2) |    0.9   |    0.6   |    0.8   |    0.5   |
| Class |     1    |     0    |     1    |     0    |


2. **Q2:** Find SVD of the following matrix:  
   $$[
   \begin{bmatrix}
   3 & 2 & 2 \\
   2 & 3 & -2
   \end{bmatrix}
   ]$$

3. **Q3:** Consider the following Grid world problem. Assume reward of entering a non-goal state is -0.1, transition probability in intended direction is 0.7, transition probabilities in Left or Right direction are 0.15, and Discount Factor (\(\gamma\)) is 1. Show state values for the first iteration of the algorithm.  
   (Grid layout: +1 in top-right, -1 in bottom-right, others blank.)

**Group B:**

4. **Q5:** Consider a query point \(x = 8\) and let \(x^1 = 9\), \(x^2 = 7\), and \(x^3 = 6\) are three points in the training set. Find the cost function for locally weighted linear regression.

5. **Q7:** Consider the data points \(\{(12,8), (10,9), (8,6), (9,7), (11,10), (7,6), (8,6), (10,10)\}\). Select three cluster centers using K-means++ algorithm. Select data point with highest probability as next cluster center.

---

### 📌 **2080 (C.Sc. 561)**

**Group A:**

1. **Q1:** Fit the logistic regression model through the following data. Show two epochs of training.  
   (Same data as 2081 Q1.)

2. **Q2:** Find SVD of the matrix:  
$$   [
   \begin{bmatrix}
   3 & 2 & 2 \\
   2 & 3 & -2
   \end{bmatrix}
   ] $$ 
   (Same as 2081 Q2.)

3. **Q3:** Functional margin in SVM + derive geometric margin + Lagrange duality & KKT conditions.

**Group B:**

4. **Q5:** Locally weighted linear regression cost function (similar setup to 2081 Q5).

5. **Q7:** K-means++ cluster center selection (similar to 2081 Q7).

---

### 📌 **2079 (C.Sc. 561)**

**Group A:**

1. **Q1:** Consider the dataset:  

| Weather | Temperature | Wind Level | Go Out (Class) |
| ------- | ----------- | ---------- | -------------- |
| Sunny   | High        | Low        | No             |
| Sunny   | Normal      | Normal     | Yes            |
| Cloudy  | High        | Normal     | No             |
| Cloudy  | Normal      | High       | Yes            |
| Sunny   | Normal      | High       | No             |
| Rainy   | High        | Normal     | No             |
| Rainy   | Low         | High       | No             |
  
   Find Information gain of each attribute and construct decision tree. Predict class for {Cloudy, Low, Normal}.

2. **Q2:** We have to divide the data points {2, 4, 6, 10, 14, 16, 18} into two clusters using GMM. Estimate parameters after the first iteration.

3. **Q3:** Derive SVM optimization problem.

**Group B:**

4. **Q6:** Consider the confusion matrix:  

| **Predicted \ Actual** | **Apple** | **Orange** | **Mango** |
| ---------------------- | :-------: | :--------: | :-------: |
| **Apple**              |     7     |      8     |     9     |
| **Orange**             |     1     |      2     |     3     |
| **Mango**              |     3     |      2     |     1     |



   Calculate accuracy, weighted avg accuracy, macro/micro precision, recall, F1-score.

---

### 📌 **2078**
*(Not present in the provided files)*

---

### 📌 **2077 (C.Sc. 561)**

**Group B:**

1. **Q4:** Derive the optimization problem for SVM.

2. **Q5:** Explain MDP, policy functions, value functions, value iterations (theoretical but may involve numerical example).

---

### 📌 **Earlier Years (2075–2076) – For Extra Practice**

**2076 Group B:**

1. **Q6:** Write k-means clustering algorithm with an arbitrary example of a training set having two features.

**2075 Group B:**

1. **Q6:** Write k-means clustering algorithm with an arbitrary example of a training set having two features.

---

### ✅ **Summary of Numerical Topics to Practice:**

1. **Logistic Regression Training** (epochs, weight updates)
2. **SVD Calculation** (matrix decomposition)
3. **Decision Tree Construction** (information gain)
4. **GMM Parameter Estimation** (first iteration)
5. **SVM Optimization Derivation**
6. **K-means++ Cluster Center Selection**
7. **Confusion Matrix Metrics** (precision, recall, F1, accuracy)
8. **Locally Weighted Linear Regression Cost**
9. **Grid World RL** (value iteration)
10. **PCA/SVD Low-Rank Approximation** (theory + calculation)

---