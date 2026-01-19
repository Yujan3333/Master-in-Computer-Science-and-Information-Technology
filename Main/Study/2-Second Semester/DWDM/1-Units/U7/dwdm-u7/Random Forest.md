## Random Forest
- [Ensemble Technique](../../../../WSA/1_Units/U5/WSA--u5/Ensemble%20Technique.md)

Random Forest is an **ensemble classification method** that builds many decision trees and combines their results.

Final decision:

* Classification → majority voting
* Prediction → average of outputs

---

## Working Principle

1. Draw many bootstrap samples from training data.
2. For each sample, build a decision tree.
3. At each node, select a random subset of features.
4. Choose the best split from those features.
5. Combine all trees for final output.

---

## Classification rule

$$Class=\text{mode}(C_1,C_2,\dots,C_T)$$

Where
$C_i$ = class predicted by tree $i$
$T$ = total number of trees

---

## Prediction rule (regression)

$$\hat{y}=\frac{1}{T}\sum_{i=1}^{T}y_i$$

---

## Feature selection at each split

If total features = $M$
Then randomly choose:

$$m=\sqrt{M}\ (classification)$$
$$m=\frac{M}{3}\ (regression)$$

---

## Why Random Forest is powerful

* Reduces **overfitting**
* High **accuracy**
* Handles large datasets
* Handles missing values
* Works for both classification and prediction

---

## Advantages

* Robust to noise
* Less variance than single decision tree
* High performance
* No need for pruning

---

## Disadvantages

* More computation and memory
* Less interpretable than a single tree

---

## One-line exam definition

> Random Forest is an ensemble classifier that builds multiple decision trees using random sampling and random feature selection, and predicts by majority voting or averaging.
