# Unit 6: Combining Classifiers (6 Hrs)

*(Based on Algorithms of the Intelligent Web – Marmanis & Babenko)*

---

## 1. Introduction

**Combining classifiers** involves using **multiple classification models together** to improve prediction accuracy, robustness, and reliability over a single classifier.

> Key idea: Multiple weak or diverse classifiers can produce a stronger overall model.

---

## 2. Motivation

Single classifiers have limitations:

* High bias or high variance
* Sensitive to training data
* Limited decision boundaries

Benefits of combining classifiers:

* Improved accuracy
* Reduced overfitting
* More stable predictions

---

## 3. Credit Worthiness – Case Study

Credit worthiness evaluation determines eligibility for credit or loans.

### Input Factors

* Income
* Employment history
* Credit history
* Existing debts

### Why Combine Classifiers?

* Financial decisions are high-risk
* Single model may be unreliable
* Ensemble provides better confidence

---

## 4. Single Classifier

Using a single classifier (e.g., decision tree, neural network):

* Simple to implement
* Faster computation

### Limitations

* May overfit
* Sensitive to noise
* Lower generalization

---

## 5. Comparing Multiple Classifiers

Classifiers include:

* Decision Trees
* Naive Bayes
* Neural Networks
* k-NN

### Comparison Criteria

* Accuracy
* Precision & Recall
* Error rate
* Stability

Observation: Different classifiers perform differently on the same dataset.

---

## 6. Bagging (Bootstrap Aggregating)

### Definition

Trains multiple classifiers on **bootstrap samples** and combines their predictions.

### Steps

1. Generate bootstrap samples from training data
2. Train a classifier on each sample
3. Combine outputs via majority voting (classification)

### Advantages

* Reduces variance
* Works well with unstable classifiers

### Example

* Random Forest uses bagging

---

## 7. Boosting

### Definition

Iterative technique where each classifier focuses on **correcting previous errors**.

### Steps

1. Train initial classifier
2. Increase weight of misclassified instances
3. Train next classifier
4. Repeat until performance improves

### Characteristics

* Reduces bias
* Converts weak learners into strong learners

### Popular Algorithm

* AdaBoost

---

## 8. Bagging vs Boosting

| Aspect        | Bagging          | Boosting         |
| ------------- | ---------------- | ---------------- |
| Focus         | Reduce variance  | Reduce bias      |
| Training      | Parallel         | Sequential       |
| Data sampling | Random bootstrap | Weighted samples |

---

## 9. Advantages

* Higher accuracy
* Robust against noise
* Better generalization

---

## 10. Limitations

* Increased complexity
* Higher computation cost
* Less interpretability

---

## 11. Exam-Oriented Short Answers

**Combining Classifiers:**

> Using multiple classifiers together to improve prediction accuracy.

**Bagging:**

> Ensemble method using bootstrap samples and combining results.

**Boosting:**

> Iterative ensemble method that focuses on misclassified instances to improve accuracy.

---

**End of Unit 6 Notes**
