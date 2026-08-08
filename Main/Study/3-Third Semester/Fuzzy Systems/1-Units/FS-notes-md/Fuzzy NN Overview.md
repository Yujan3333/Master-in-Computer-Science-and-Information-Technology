#fuzzy-system #third-semester 

# 1. Why integrate Neural Networks and Fuzzy Systems?

First understand the weaknesses.

## Fuzzy System

**Strengths**

* Human-like reasoning
* Easy to understand
* Uses IF-THEN rules

Example

```
IF temperature is High
THEN fan speed is Fast
```

**Weakness**

It **cannot learn** by itself.

Someone must define

* membership functions
* fuzzy rules
* parameters

---

## Neural Network

**Strengths**

* Learns from data
* Adjusts weights automatically
* Can approximate complex functions

**Weakness**

It is a **black box**.

You don't know why it produced an output.

---

## Hybrid System

Combine both.

```
Neural Network
      +
Fuzzy Logic
      ↓
Fuzzy Neural Network
```

Now we get

* learning ability
* interpretable rules
* robustness
* adaptability

---

# 2. Universal Approximation Theorem

This is a theory question.

It simply says

> A feedforward neural network with at least one hidden layer and nonlinear activation functions can approximate **any continuous function** to any desired accuracy.

Similarly,

A fuzzy inference system can also approximate any continuous function.

That is why both are called

**Universal Approximators**

You don't need to prove it.

Just remember

```
Any continuous function

↓

NN can learn it

↓

Fuzzy System can represent it

↓

Both are Universal Approximators
```

---

# 3. Why use Neural Networks inside Fuzzy Systems?

There are three major reasons.

## (i) Parallel Processing

Suppose we have

```
IF temperature is High THEN speed Fast

IF temperature is Medium THEN speed Medium

IF temperature is Low THEN speed Slow
```

A traditional fuzzy system evaluates one rule after another.

Neural networks evaluate all neurons simultaneously.

So execution becomes much faster.

---

## (ii) Learning

Suppose initial membership function is

```
Low

1
|\
| \
|  \
|___\____
```

Training data says

"No, Low should extend further."

Neural network adjusts it automatically.

```
1
|\
| \
|  \
|   \
|____\____
```

This adjustment happens through **backpropagation**.

---

## (iii) Adaptation

If environment changes

```
Old engine

↓

New engine
```

The fuzzy system doesn't need to be redesigned.

Neural network updates the parameters.

---

# 4. Fuzzy Neural Network (FNN)

A normal neuron computes

$$
y=f\left(\sum w_ix_i\right)
$$

Everything is crisp.

---

A fuzzy neuron uses fuzzy values.

Example

Input

```
Temperature = High (0.7)
```

Weight

```
Importance = 0.9
```

Instead of multiplication,

it may use

```
min

or

max
```

operations.

---

# Characteristics

Instead of

```
Input = number
```

we have

```
Input = fuzzy number
```

Instead of

```
Weight = 0.5
```

we may have

```
Weight = "High"
```

Outputs can also be fuzzy.

---

# 5. Types of Fuzzy Neural Networks

Your notes say

Types 1–7.

The easiest way to remember them is by asking

"What is fuzzy?"

| Type | Input | Weight | Target |
| ---- | ----- | ------ | ------ |
| 1    | Crisp | Crisp  | Crisp  |
| 2    | Fuzzy | Crisp  | Crisp  |
| 3    | Crisp | Fuzzy  | Crisp  |
| 4    | Crisp | Crisp  | Fuzzy  |
| 5    | Fuzzy | Fuzzy  | Crisp  |
| 6    | Fuzzy | Crisp  | Fuzzy  |
| 7    | Fuzzy | Fuzzy  | Fuzzy  |

Usually exams only ask

"Explain classification."

Don't memorize every combination unless your teacher specifically asks.

---

# 6. Regular Fuzzy Neural Network

This is simply

```
Input

↓

Fuzzification

↓

Hidden Layers

↓

Inference

↓

Defuzzification

↓

Output
```

Think of it as

```
Fuzzy System

+

Neural Learning
```

---

# 7. AND Neuron

This is important.

Suppose

```
x1=0.4

x2=0.8

w1=0.5

w2=0.7
```

Use

```
S=max

T=min
```

Formula

$$
y
=

T(S(w_1,x_1),S(w_2,x_2))
$$

Step 1

$$
S(w_1,x_1)
==========

\max(0.5,0.4)
=
0.5
$$

Step 2

$$
S(w_2,x_2)
==========
 \max(0.7,0.8)
=
0.8
$$

Step 3

$$
y
=

\min(0.5,0.8)
=
0.5
$$

---

# 8. OR Neuron

Formula

$$
y
=

S(T(w_1,x_1),T(w_2,x_2))
$$

Step 1

$$
\min(0.5,0.4)
=============

0.4
$$

Step 2

$$
\min(0.7,0.8)
=============

0.7
$$

Step 3

$$
\max(0.4,0.7)
=============

0.7
$$

---

Easy memory trick

```
AND

inside → MAX

outside → MIN

OR

inside → MIN

outside → MAX
```

---

# 9. Generation of Membership Functions using Neural Networks

This is probably the hardest topic, but it is actually just **ordinary backpropagation**.

The goal is

```
Training Data

↓

Neural Network

↓

Membership Function
```

Instead of predicting

```
Dog

Cat
```

the network predicts

```
Membership = 0.91

Membership = 0.15
```

---

# Architecture

Your architecture

```
2×3×3×2
```

means

```
2 Input Nodes

↓

3 Hidden Neurons

↓

3 Hidden Neurons

↓

2 Output Neurons
```

Nothing more.

---

# Overall Backpropagation Flow (The Big Picture)

Most students get lost because they only memorize formulas. Instead, remember **why** each step is done.

```
Inputs
(x1,x2)

↓

Forward Pass

↓

Hidden Layer 1 Outputs

↓

Hidden Layer 2 Outputs

↓

Final Outputs

↓

Compare with Target

↓

Compute Error

↓

Backpropagate Error

↓

Update Weights

↓

Repeat Until Error is Small
```

Every numerical question follows this exact sequence.

---

# Step 1: Forward Pass

Take the inputs

```
x1
x2
```

Multiply them by weights, add them, and pass the result through the sigmoid activation.

This gives the outputs of the first hidden layer.

Repeat the same process for the next hidden layer, and finally compute the output layer.

**Purpose:** Produce the network's prediction.

---

# Step 2: Output Error

Compare the predicted output with the desired target.

Conceptually,

```
Error
=
Target
-
Output
```

If the prediction is close to the target, the error is small.

---

# Step 3: Backpropagation

The output layer error is propagated backward to the hidden layers.

Hidden neurons do not have target values, so their errors are computed from the errors of the next layer and the connecting weights.

**Purpose:** Determine how much each hidden neuron contributed to the final error.

---

# Step 4: Weight Update

Every weight is adjusted using

```
New Weight
=
Old Weight
+
Learning Rate
×
Error
×
Input
```

If the error is positive, the weight usually increases.

If the error is negative, the weight usually decreases.

**Purpose:** Reduce the error in the next training iteration.

---

# Complete Learning Cycle

```
Training Data
      │
      ▼
Forward Pass
      │
      ▼
Network Output
      │
      ▼
Compare with Target
      │
      ▼
Compute Error
      │
      ▼
Backpropagate Error
      │
      ▼
Update Weights
      │
      ▼
Repeat Until Error is Small
```

---

## Exam Preparation Priority

If you have limited time, study in this order:

1. **Neural Network + Fuzzy System integration** (theory)
2. **Universal Approximation Theorem**
3. **Fuzzy Neural Networks and their characteristics**
4. **AND and OR fuzzy neurons** (with one solved example each)
5. **Generation of membership functions using NN**
6. **The complete backpropagation numerical** (practice the forward pass, error calculation, backpropagation, and weight updates repeatedly until you can do it without looking at the solution).
