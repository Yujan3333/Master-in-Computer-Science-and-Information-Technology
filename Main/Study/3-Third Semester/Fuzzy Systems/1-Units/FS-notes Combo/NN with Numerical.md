#fuzzy-system #third-semester 

# Topic: Fuzzy with Neural Network

## Basic Idea

In a normal fuzzy system, a human expert designs membership functions manually.

Example:

Temperature:

```
Cold        Warm        Hot

0 -----------50-----------100
```

Membership functions are chosen by humans:

$$[
\mu_{Cold}(30)=0.8
]$$

$$[
\mu_{Hot}(30)=0.1
]$$

The problem:

* How do we decide the shape?
* Where should the boundary be?
* What if we have thousands of data points?

So we use a **Neural Network** to learn these membership functions automatically.

---

# What is Neuro-Fuzzy System?

A Neuro-Fuzzy system combines:

## Fuzzy Logic

Provides:

* linguistic variables
* membership functions
* fuzzy rules

Example:

IF temperature is HIGH
THEN fan speed is FAST

---

## Neural Network

Provides:

* learning ability
* automatic parameter adjustment
* optimization of membership functions

---

So:

$$[
\boxed{\text{Neural Network learns the fuzzy membership functions}}
]$$

---

# What is happening in Example 6.3?

The objective is:

Given some data points:

$$[
(x_1,x_2)
]$$

find their membership values:

$$[
(\mu_{R1},\mu_{R2})
]$$

where:

* (R_1) = fuzzy region/class 1
* (R_2) = fuzzy region/class 2

The neural network learns the relationship:

$$[
(x_1,x_2)
\rightarrow
(\mu_{R1},\mu_{R2})
]$$

---

# Step 1: Data Collection

They have 20 points.

Each point has two features:

$$[
x_1,x_2
]$$

Example:

Point 1:

$$[
x_1=0.05
]$$

$$[
x_2=0.02
]$$

This is the input to the neural network.

---

# Step 2: Create Fuzzy Classes

The data is divided into fuzzy regions:

$$[
R_1
]$$

and

$$[
R_2
]$$

using a clustering technique.

Meaning:

The data naturally forms two groups.

Example:

```
          x2


        R2
      * * *
    *
---------------- x1

 * * *
   R1
```

The clustering algorithm decides:

"This point belongs to R1"

or

"This point belongs to R2"

---

# Step 3: Assign Membership Values

After clustering, every point receives membership values.

Example:

Point 1:

belongs completely to R1:

$$[
\mu_{R1}=1
]
$$
$$[
\mu_{R2}=0
]$$

Another point:

$$[
\mu_{R1}=0
]$$

$$[
\mu_{R2}=1
]$$

These are called:

**Target outputs**

because they are the values the neural network must learn.

---

# Step 4: Build Neural Network

They choose:

$$[
2 \times 3 \times 3 \times 2
]$$

network.

Meaning:

```
Input       Hidden       Hidden       Output

 x1           ○             ○            ○ R1

 x2           ○             ○            ○ R2

              3             3             2
```

---

## Input Layer

Contains:

$$[
x_1,x_2
]$$

Example:

$$[
(0.05,0.02)
]$$

---

## Output Layer

Produces:

$$[
R_1,R_2
]$$

The output values represent membership:

Example:

$$[
O_1=0.75
]$$

means

$$[
\mu_{R1}=0.75
]$$

---

# Step 5: Initialize Weights

Initially the neural network does not know anything.

So random weights are assigned.

Example:

Connection:

$$[
x_1 \rightarrow neuron_1
]$$

has weight:

$$[
w=0.5
]$$

These weights represent how strongly one neuron affects another.

---

# Step 6: Forward Propagation

Now we give one data point.

Example:

$$[
x_1=0.05
]$$

$$[
x_2=0.02
]$$

The information moves forward.

---

Every neuron calculates:

$$[
net=\sum x_iw_i
]$$

Then activation:

$$[
O=\frac{1}{1+e^{-net}}
]$$

This converts the value into range:

$$[
0 \leq O \leq 1
]$$

which is suitable for membership values.

---

# Example Calculation

First hidden neuron:

Inputs:

$$[
x_1=0.05
]$$

$$[
x_2=0.02
]$$

Weights:

$$[
w_1=0.5
]
$$
$$[
w_2=0.2
]$$

Weighted sum:

$$[
net=(0.05)(0.5)+(0.02)(0.2)
]$$

$$[
=0.025+0.004
]$$

$$[
=0.029
]$$

Sigmoid:

$$[
O=
\frac1{1+e^{-0.029}}
]$$

$$[
O=0.507249
]$$

This becomes input for the next layer.

---

# Step 7: Output Prediction

After passing through all layers:

The network gives:

$$[
O_{R1}=0.666334
]$$

$$[
O_{R2}=0.635793
]$$

But actual membership should be:

$$[
R1=1
]$$

$$[
R2=0
]$$

So the network prediction is wrong.

---

# Step 8: Calculate Error

For R1:

Actual:

$$[
1
]$$

Predicted:

$$[
0.666334
]$$

Error:

$$[
E=1-0.666334
]$$

$$[
E=0.333666
]$$

---

For R2:

Actual:

$$[
0
]$$

Predicted:

$$[
0.635793
]$$

Error:

$$[
E=0-0.635793
]$$

$$[
E=-0.635793
]$$

---

# Step 9: Backpropagation

Now we ask:

"Which weights caused this error?"

The error travels backward.

```
Output error

      ↓

Hidden layer 2

      ↓

Hidden layer 1

      ↓

Input weights
```

Each neuron receives an error value.

Formula:

$$[
E_n=O_n(1-O_n)\sum wE
]$$

This calculates the contribution of each neuron.

---

# Step 10: Weight Adjustment

Now modify weights.

Rule:

$$[
w_{new}=w_{old}+\alpha Ex
]$$

where:

### Learning rate

$$[
\alpha=0.3
]$$

controls how much the weight changes.

Example:

Old:

$$[
w=0.30
]$$

After learning:

$$[
w=0.356960
]$$

The network has improved slightly.

---

# Step 11: Repeat Learning

The same point is passed again.

Again:

1. Forward propagation
2. Calculate error
3. Backpropagate error
4. Update weights

until:

$$[
Error \approx 0
]$$

---

# Step 12: Train All Data

Now use:

```
Point 1

↓

Point 2

↓

Point 3

↓

...

↓

Point 10
```

The network learns from all examples.

---

# Step 13: Testing

Now use unseen points:

Table 6.3.

The network predicts their memberships.

Example:

Input:

$$[
(x_1,x_2)=(0.84,0.82)
]$$

Output:

$$[
\mu_{R1}=0.05
]$$

$$[
\mu_{R2}=0.95
]$$

Meaning:

This point belongs mostly to R2.

---

# Final Result

After training:

The neural network has learned the fuzzy membership function.

Instead of manually defining:

$$[
\mu_{R1}(x_1,x_2)
]$$

and

$$[
\mu_{R2}(x_1,x_2)
]$$

the neural network automatically approximates them.

---

# How this connects to Fuzzy Systems

Normal fuzzy system:

```
Input
 |
Membership Function
 |
Fuzzy Rules
 |
Output
```

Neuro-Fuzzy:

```
Input
 |
Neural Network
 |
Learns Membership Function
 |
Fuzzy Output
```

---

# Whole Example in One Line

**The example trains a multilayer neural network using backpropagation so that it learns the mapping between input data points and their fuzzy membership values, thereby automatically creating fuzzy membership functions for the fuzzy sets R1 and R2.**

---

# Exam Answer Structure

If asked "Explain neural network based membership function generation":

1. Explain problem of manually selecting membership functions.
2. Collect input-output training data.
3. Assign membership values using clustering/expert knowledge.
4. Create neural network architecture.
5. Initialize weights.
6. Perform forward propagation.
7. Calculate error between desired and actual membership.
8. Apply backpropagation.
9. Update weights.
10. Repeat until error minimizes.
11. Test network.
12. Use trained network to predict membership of new data.

This is the complete **Fuzzy + Neural Network (Neuro-Fuzzy membership learning)** process.
