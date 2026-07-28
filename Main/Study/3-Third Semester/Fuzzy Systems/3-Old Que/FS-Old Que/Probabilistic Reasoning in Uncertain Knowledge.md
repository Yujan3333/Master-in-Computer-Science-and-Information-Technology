#fuzzy-system #third-semester #exam-paper-answer 

# What is Uncertain Knowledge? How is Probabilistic Reasoning Done in Uncertain Knowledge?

## 1. Uncertain Knowledge

### Definition

**Uncertain knowledge** is knowledge in which the truth or outcome is **not known with complete certainty**. It arises because information may be **incomplete, ambiguous, imprecise, or random**.

Instead of saying an event is definitely true or false, we express our **degree of belief** using probabilities.

---

### Examples

* It may rain tomorrow.
* A patient may have dengue based on symptoms.
* An email may be spam.
* A student may pass an exam.

Since the outcome is uncertain, probability is used to represent confidence.

For example,

$$
P(\text{Rain})=0.7
$$

means there is a **70% chance of rain**.

---

## 2. Probabilistic Reasoning

### Definition

**Probabilistic reasoning** is the process of making decisions or drawing conclusions under uncertainty using the **rules of probability**.

It updates our belief about an event whenever new evidence becomes available.

---

## Common Probability Rules Used

### (a) Prior Probability

Initial probability before observing evidence.

Example:

$$
P(\text{Disease})=0.02
$$

There is a **2% chance** that a person has the disease before any test.

---

### (b) Conditional Probability

Probability of an event given that another event has occurred.

$$
P(A|B)
======

\frac{P(A\cap B)}{P(B)}
$$

Example:

If

* 80 out of 100 fever patients have the flu,

then

$$
P(\text{Flu}|\text{Fever})
=

 \frac{80}{100}
=========================
0.8
$$

There is an **80% chance** of flu given fever.

---

### (c) Bayes' Theorem

Used to update probability after obtaining new evidence.

$$
P(A|B)
======

\frac{P(B|A)P(A)}
{P(B)}
$$

where

* $P(A)$ = Prior probability
* $P(B|A)$ = Likelihood
* $P(B)$ = Evidence
* $P(A|B)$ = Posterior probability

---

## Example of Probabilistic Reasoning

Suppose,

* Probability of disease:

$$
P(D)=0.01
$$

* Test correctly detects disease:

$$
P(+|D)=0.95
$$

* False positive rate:

$$
P(+|\overline D)=0.05
$$

If a person's test result is positive, Bayes' theorem is used to compute

$$
P(D|+)
$$

which gives the **updated probability** that the person actually has the disease.

Thus, probabilistic reasoning **updates beliefs based on new evidence**.

---

## Applications

* Medical diagnosis
* Weather forecasting
* Spam email detection
* Machine learning
* Expert systems
* Risk analysis

---

## Advantages

* Handles uncertainty mathematically.
* Produces rational decisions under incomplete information.
* Updates beliefs when new evidence is available.
* Widely used in AI and expert systems.

---

## Limitations

* Requires accurate probability values.
* Probability estimation may be difficult.
* Can become computationally expensive for large problems.

---

# 5-Mark Exam Answer

**Uncertain knowledge** is knowledge where the truth of an event is not known with certainty due to incomplete, ambiguous, or random information. It is represented using **probability values** instead of absolute true or false values.

**Probabilistic reasoning** is the process of reasoning under uncertainty using probability theory. It computes the likelihood of events and updates beliefs when new evidence is obtained. The main tools are **prior probability, conditional probability, and Bayes' theorem**.

Bayes' theorem is

$$
P(A|B)
======

\frac{P(B|A)P(A)}
{P(B)}
$$

where the prior probability is updated to obtain the posterior probability after observing evidence.

**Applications:** medical diagnosis, weather prediction, spam filtering, expert systems, and machine learning.
