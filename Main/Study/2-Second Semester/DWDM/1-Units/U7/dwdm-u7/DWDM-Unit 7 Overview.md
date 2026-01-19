## Unit–VII : Classification and Prediction (6 Hrs)

---

## 1. Classification and Prediction

* **Classification** → Predicts **categorical labels**

  * Example: Spam / Not spam, Pass / Fail
* **Prediction** → Predicts **continuous values**

  * Example: House price, Temperature

Model:
$$Y=f(X)$$

Where
$X$ = input attributes
$Y$ = class label or numeric value

---

## 2. Issues in Classification

1. Overfitting
2. Noise and missing values
3. High dimensionality
4. Data imbalance
5. Model interpretability
6. Scalability and efficiency
7. Accuracy vs simplicity tradeoff

---

## 3. Classification by Decision Tree Induction

Uses **information gain** or **gini index**.

### Entropy:

$$
Entropy(S)=-\sum p_i\log_2 p_i
$$

### Information Gain:

$$
Gain(S,A)=Entropy(S)-\sum_{v\in A}\frac{|S_v|}{|S|}Entropy(S_v)
$$

Used in:

* ID3
* C4.5
* CART

---

## 4. Bayesian Classification

Based on **Bayes’ theorem**:

$$
P(C|X)=\frac{P(X|C)P(C)}{P(X)}
$$

Naïve Bayes assumption:
Attributes are conditionally independent.

Classification rule:
$$
Class=\arg\max_C P(C|X)
$$

---

## 5. Classification by Backpropagation (Neural Network)

Uses **error minimization**:

Error:
$$
E=\frac{1}{2}\sum(t-o)^2
$$

Weight update:
$$
\Delta w=\eta\cdot error\cdot input
$$

Where
$\eta$ = learning rate

---

## 6. Classification Based on Association Rules

Uses rules like:

$$
X \Rightarrow Y
$$

With:

Support:
$$
Support(X\Rightarrow Y)=\frac{count(X\cup Y)}{N}
$$

Confidence:
$$
Confidence(X\Rightarrow Y)=\frac{count(X\cup Y)}{count(X)}
$$

High confidence rules are used as classifiers.

---

## 7. Other Classification Methods

1. **k-Nearest Neighbor (k-NN)**
   Distance:
   $$
   d=\sqrt{\sum (x_i-y_i)^2}
   $$

2. **Support Vector Machine (SVM)**
   Finds maximum margin hyperplane.

3. **Rule-Based Classifier**
   Uses IF–THEN rules.

4. [Random Forest](Random%20Forest.md)
   Ensemble of decision trees.

5. [Logistic Regression](../../../../../1-First%20Semester/Subjects/Neural%20Network%20(NN)/1-Units/Unit%202/NN-u2/Logistic%20Regression.md)

   $$
   P=\frac{1}{1+e^{-z}}
   $$

---

### Exam Tip:

For Unit VII, remember:

| Topic          | Key Idea                       |
| -------------- | ------------------------------ |
| Decision Tree  | Entropy, Information Gain      |
| Bayes          | $P(CX)=\frac{P(XC)P(C)}{P(X)}$ |
| Neural Network | Error minimization             |
| Assoc. Rules   | Support, Confidence            |
| k-NN           | Distance-based                 |
| SVM            | Maximum margin                 |
