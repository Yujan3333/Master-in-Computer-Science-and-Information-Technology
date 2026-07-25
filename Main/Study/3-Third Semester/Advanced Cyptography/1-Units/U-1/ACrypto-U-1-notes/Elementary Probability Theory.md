
#advanced-cryptography #third-semester 
# Elementary Probability Theory (5 Marks)

## Definition

**Elementary Probability Theory** is the branch of mathematics that studies the likelihood (chance) of events occurring. It provides rules for calculating the probability of different events.

The probability of an event is always between 0 and 1.

$$
0 \le P(E) \le 1
$$

where:

* $$P(E)=0$$ means the event is impossible.
* $$P(E)=1$$ means the event is certain.

---

## Basic Formula

If all outcomes are equally likely, then

$$
P(E)=\frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
$$

---

## Basic Terminologies

### 1. Experiment

An action that produces an outcome.

**Example:** Tossing a coin.

---

### 2. Sample Space ($S$)

The set of all possible outcomes.

**Example:**

For a coin toss,

$$
S={H,T}
$$

---

### 3. Event ($E$)

A subset of the sample space.

**Example:**

Getting a head,

$$
E={H}
$$

---

## Important Probability Laws

### 1. Probability of the Sample Space

$$
P(S)=1
$$

The total probability of all possible outcomes is 1.

---

### 2. Probability of an Impossible Event

$$
P(\varnothing)=0
$$

---

### 3. Complement Rule

$$
P(E')=1-P(E)
$$

where $E'$ is the complement of $E$.

---

### 4. Addition Rule

For any two events,

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

If $A$ and $B$ are mutually exclusive,

$$
P(A\cup B)=P(A)+P(B)
$$

---

### 5. Multiplication Rule

For independent events,

$$
P(A\cap B)=P(A)\times P(B)
$$

---

## Example

A fair die is rolled.

Sample space:

$$
S={1,2,3,4,5,6}
$$

Find the probability of getting an even number.

Event:

$$
E={2,4,6}
$$

Therefore,

$$
P(E)=\frac{3}{6}=\frac12
$$

---

## Applications in Cryptography

Elementary probability theory is used to:

* Analyze cryptographic algorithms.
* Calculate the probability of successful attacks.
* Study random key generation.
* Analyze collisions in hash functions.
* Prove security properties such as perfect secrecy.

---

## Exam Conclusion

Elementary Probability Theory provides the mathematical foundation for calculating the likelihood of events using probability laws and formulas. It is widely used in cryptography to analyze randomness, keys, and the security of cryptographic systems.
