#fuzzy-system #third-semester 

---
# 1. Probabilistic Reasoning

### What is it?

Probabilistic reasoning is a method of making decisions when information is uncertain. It uses **probability theory** to estimate how likely an event is.

### Example

A doctor knows that **toothache usually indicates a cavity**, but not always.

Instead of saying

> Toothache → Cavity (always)

we say

> Toothache → Cavity with probability **0.8**

---

# 2. Uncertain Knowledge

### What is it?

Sometimes we do not know everything about a situation because of incomplete information.

Reasons:

* Partial observation
* Sensor errors
* Unexpected events
* Complex environment

### Example

Leaving **90 minutes before a flight** may get you to the airport on time, but traffic is uncertain.

---

# 3. Handling Uncertainty

### What is it?

Instead of saying something is always true, assign a **probability**.

### Example

Instead of

> If toothache then cavity

Use

> If toothache then cavity with probability **0.8**

---

# 4. Decision Making under Uncertainty

### What is it?

Choose the action with the best balance between probability and usefulness (utility).

Decision Theory

$$
\text{Decision Theory}=\text{Probability Theory}+\text{Utility Theory}
$$

### Example

Leave

* 25 min early → 4% chance
* 90 min early → 70%
* 120 min early → 95%

Choose according to how important catching the flight is.

---

# 5. Probability

### What is it?

Probability measures the **chance** that an event occurs.

Range

$$
0\le P(A)\le1
$$

Formula

$$
P(A)=\frac{\text{Favourable outcomes}}{\text{Total outcomes}}
$$

### Example

Probability of drawing an Ace

$$
P=\frac{4}{52}=\frac{1}{13}
$$

---

# 6. Conditional Probability

### What is it?

Probability of an event **given** another event has already happened.

Formula

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

### Example

Probability of cavity if the patient has toothache

$$
P(\text{Cavity}|\text{Toothache})=0.8
$$

---

# 7. Random Variable

### What is it?

A variable whose value depends on a random experiment.

### Example

Coin toss

| Outcome | Random Variable X |
| ------- | ----------------- |
| Head    | 1                 |
| Tail    | 0                 |

---

# 8. Atomic Event

### What is it?

A complete description of one possible outcome.

### Example

Variables

* Cavity = True
* Toothache = False

This combination is one atomic event.

---

# 9. Proposition

### What is it?

A statement that is either true or false.

### Example

"Cavity is true"

or

"Weather is rainy"

---

# 10. Types of Random Variables

### (a) Boolean

Only True or False.

Example

Cavity = True

---

### (b) Discrete

Finite values.

Example

Weather

* Sunny
* Rainy
* Cloudy

---

### (c) Continuous

Infinite values.

Example

Temperature = 21.6°C

---

# 11. Prior Probability

### What is it?

Probability before seeing any evidence.

Example

$$
P(\text{Rain})=0.1
$$

No additional information is used.

---

# 12. Conditional Probability

### What is it?

Probability after some evidence is known.

Example

Probability of cavity when toothache exists

$$
P(\text{Cavity}|\text{Toothache})=0.8
$$

---

# 13. Product Rule

### What is it?

Calculates joint probability.

Formula

$$
P(A\cap B)=P(A|B)P(B)
$$

or

$$
P(A\cap B)=P(B|A)P(A)
$$

### Example

Probability of

* Rain
* Traffic

occurring together.

---

# 14. Joint Probability Distribution

### What is it?

Shows probabilities for **all combinations** of variables.

### Example

Weather and Cavity

| Weather | Cavity | Probability |
| ------- | ------ | ----------- |
| Sunny   | True   | 0.144       |

---

# 15. [Inference using Joint Distribution](Inference%20using%20Joint%20Distribution.md)

### What is it?

Find probability by adding probabilities of relevant atomic events.

### Example

Find

$$
P(\text{Cavity or Toothache})
$$

Add all rows where either event is true.

---

# 16. [Marginalization (Summing Out)](Marginalization%20(Summing%20Out).md)

### What is it?

Remove unwanted variables by adding probabilities.

Formula

$$
P(Y)=\sum P(Y,Z)
$$

### Example

Find

$$
P(\text{Cavity})
$$

by adding all probabilities where cavity is true.

---

# 17. Independence

### What is it?

Two events do not affect each other.

Formula

$$
P(A|B)=P(A)
$$

or

$$
P(A,B)=P(A)P(B)
$$

### Example

Weather is independent of whether you have a cavity.

---

# 18. Bayes' Theorem

### What is it?

Find probability of a cause after observing evidence.

Formula

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

### Example

Patient has stiff neck.

Find probability that the patient has meningitis.

![](../../../../../../Images/Third_Sem_Images/Introduction%20to%20Fuzzy%20Set%20Theory-%20bayes%20ex.png)

---

# 19. Probability vs Fuzzy Logic

| Probability                 | Fuzzy Logic                |
| --------------------------- | -------------------------- |
| Measures chance             | Measures degree            |
| Event either happens or not | Event can partially happen |
| Crisp events                | Vague events               |

### Example

Probability

"There is a 70% chance it will rain."

Fuzzy

"Today's weather is **0.8 Hot**."

---

# 20. Fuzzy Logic

### What is it?

A logic that allows **partial truth** between 0 and 1.

Instead of only

* True
* False

it allows

* 0.2
* 0.6
* 0.9

etc.

### Example

Age 60

Old = 0.8

Young = 0.1

---

# 21. Linguistic Variables

### What is it?

Variables whose values are words instead of numbers.

### Example

Age

Instead of

Age = 65

Use

Age is **Old**

Possible values

* Young
* Middle-aged
* Old

---

# 22. Why Fuzzy Logic?

### What is it?

It helps computers reason like humans using vague information.

### Example

Instead of

Temperature > 30°C

Use

Temperature is **Very Hot**

---

# 23. Real-World Applications of Fuzzy Logic

Examples include:

* Washing machines
* Air conditioners
* Cameras (auto-focus)
* Subway train control
* Robots
* Elevators
* Traffic control

---

# 24. Extension Principle

### What is it?

A rule that extends ordinary mathematical functions to fuzzy sets.

### Example

Rules

* If temperature is **Low** → Fan speed is **Low**
* If temperature is **Medium** → Fan speed is **High**
* If temperature is **High** → Fan speed is **Low**

---

# 25. History of Fuzzy Logic

* Proposed by **Lotfi A. Zadeh** in **1965**
* First industrial applications appeared in Europe.
* Japan widely adopted fuzzy logic in trains and consumer electronics.

---

# 26. First Applications

Examples

* Steam generator control
* Cement kiln control
* Decision support systems
* Water treatment plants
* Hitachi subway system

---

# 27. [Truth or Falsity (Classical Logic)](Truth%20or%20Falsity%20(Classical%20Logic).md)

### What is it?

Classical logic says every statement is either:

* True
* False

There is no middle value.

### Example

Switch

* ON
* OFF

Unlike fuzzy logic, it cannot be "partially ON."
### 2 Laws
#### Principle of Excluded Middle
#### Principle of Non-Contradiction
---

## 📌 Most Important Topics for Exams

1. Probability
2. Conditional Probability
3. Prior Probability
4. Random Variable
5. Joint Probability Distribution
6. Marginalization
7. Independence
8. Bayes' Theorem
9. Fuzzy Logic
10. Probability vs Fuzzy Logic
11. Linguistic Variables
12. Applications of Fuzzy Logic  
