#fuzzy-system #third-semester 

# Basic Statistical Methods – Probability 

## Definition

**Probability** is a statistical method used to **measure uncertainty**. It assigns a numerical value between **0 and 1** to indicate how likely an event is to occur. It is one of the fundamental tools for handling uncertainty. The notes explain probability through its basic axioms and simple examples. 

---

# Axioms (Basic Rules) of Probability

According to the notes:

### 1. Probability lies between 0 and 1

$$
0 \le P(A) \le 1
$$

where:

* **0** → Event is impossible (total uncertainty).
* **1** → Event is certain (total certainty).
* **Between 0 and 1** → Represents some degree of certainty or uncertainty.

---

### 2. Meaning of Probability Values

| Probability | Meaning                                |
| ----------- | -------------------------------------- |
| $P(A)=0$    | Event will never occur (impossible).   |
| $P(A)=1$    | Event will definitely occur (certain). |
| $0<P(A)<1$  | Event may occur with some likelihood.  |

---

### 3. Probability Can Be Calculated in Different Ways

The basic formula is:

$$
P(A)=\frac{\text{Number of desired outcomes}}{\text{Total number of outcomes}}
$$

---

# Example 1: Probability of Drawing an Ace

A standard deck has:

* Total cards = **52**
* Number of aces = **4**

Therefore,

$$
P(\text{Ace})=\frac{4}{52}=\frac{1}{13}
$$

---

# Example 2: Probability of Drawing a Spade

A deck contains:

* Total cards = **52**
* Spades = **13**

Therefore,

$$
P(\text{Spade})=\frac{13}{52}=\frac{1}{4}
$$

---

# Conditional Probability

The notes introduce **conditional probability** as:

$$
P(A|B)
$$

It means:

> **The probability that event $A$ occurs, given that event $B$ has already occurred.**

Example:

Suppose a card drawn is **known to be a face card**. Then the probability that it is a **King** is different from the probability of drawing a King from the full deck because we already have additional information.

---

# Probabilistic Logic

The notes state that **probabilistic logic** combines:

* **Probability theory** → Handles uncertainty.
* **Deductive logic** → Uses logical structure for reasoning.

As a result, probabilistic logic is more expressive than traditional true/false logic because conclusions are represented using **probabilities** instead of only Boolean values. 

---

# Limitation

The notes mention one important drawback:

* Combining **probability** and **logic** increases **computational complexity**, making probabilistic logic more difficult to compute.

---

# Key Points

* Probability measures **uncertainty**.
* Probability values always lie between **0 and 1**.
* **0 = impossible**, **1 = certain**.
* Basic probability formula:

$$
P(A)=\frac{\text{Desired outcomes}}{\text{Total outcomes}}
$$

* Conditional probability is written as:

$$
P(A|B)
$$

* Probabilistic logic combines **probability theory** and **deductive logic**.
* A major limitation is **high computational complexity**.

---

# 5-Mark Exam Answer

**Probability** is a statistical method used to measure uncertainty by assigning a value between **0 and 1** to an event. According to the basic axioms, **0** represents an impossible event, **1** represents a certain event, and values between **0 and 1** represent varying degrees of certainty. The basic probability formula is:

$$
P(A)=\frac{\text{Number of desired outcomes}}{\text{Total number of outcomes}}
$$

For example, the probability of drawing an Ace from a standard deck of 52 cards is:

$$
P(\text{Ace})=\frac{4}{52}=\frac{1}{13}
$$

The probability of drawing a Spade is:

$$
P(\text{Spade})=\frac{13}{52}=\frac{1}{4}
$$

The notes also define **conditional probability**, $P(A|B)$, as the probability of event $A$ occurring given that event $B$ has already occurred. They further explain that **probabilistic logic** combines probability theory with deductive logic to reason under uncertainty, although this increases computational complexity. 

---

### Exam Tip

Do not confuse these terms:

* **Probability** → Measures **how likely** an event is.
* **Conditional Probability** → Measures the likelihood of an event **after another event is known to have occurred**.
* **Probabilistic Logic** → Uses **probability + logic** to reason under uncertainty.
