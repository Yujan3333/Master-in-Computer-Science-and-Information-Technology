#fuzzy-system #third-semester #old-que #exam-paper-answer 

That's an important observation. **This particular question is not actually asking for a numerical solution.** It says:

> **"Construct a fuzzy controller... Illustrate with example. Configure the required rules, fuzzy sets and the inputs for executing the rules."**

This means **you are expected to create your own example**, because the question does not provide any numerical values or membership functions.

If you want to show **how Mamdani inference is executed numerically**, you must make reasonable assumptions. Here's one complete worked example.

---

# Example: Fan Speed Controller (Complete Numerical Example)

## Problem

Design a Mamdani fuzzy controller for a fan.

### Input

Temperature (°C)

### Output

Fan Speed (%)

---

# Step 1: Define Fuzzy Sets

## Input: Temperature

Three triangular membership functions.

### Cold

Triangle:

$$(0,;20,;40)$$

### Warm

Triangle:

$$(20,;40,;60)$$

### Hot

Triangle:

$$(40,;60,;80)$$

---

## Output: Fan Speed

### Slow

$$(0,;25,;50)$$

### Medium

$$(25,;50,;75)$$

### Fast

$$(50,;75,;100)$$

---

# Step 2: Rule Base

Rule 1

> IF Temperature is Cold THEN Fan Speed is Slow

Rule 2

> IF Temperature is Warm THEN Fan Speed is Medium

Rule 3

> IF Temperature is Hot THEN Fan Speed is Fast

---

# Step 3: Given Input

Suppose

$$
Temperature=50^\circ C
$$

Now calculate memberships.

---

# Step 4: Fuzzification

## Cold Membership

Temperature

$$
50>40
$$

Therefore

$$
\mu_{Cold}(50)=0
$$

---

## Warm Membership

Warm triangle

$$(20,;40,;60)$$

Since

$$
40<50<60
$$

Use decreasing side of the triangle.

$$
\mu_{Warm}(50)
\\=

\frac{60-50}{60-40}
$$
$$
\\=\frac{10}{20}
$$

$$
\\=0.5
$$

---

## Hot Membership

Hot triangle

$$(40,;60,;80)$$

Since

$$
40<50<60
$$

Use increasing side.

$$
\mu_{Hot}(50)
\\=

\frac{50-40}{60-40}
$$

$$
\\=\frac{10}{20}
$$

 $$

\\=0.5
$$

---

Now we have

$$
\mu_{Cold}=0
$$

$$
\mu_{Warm}=0.5
$$

$$
\mu_{Hot}=0.5
$$

Meaning

Temperature is

* 0% Cold
* 50% Warm
* 50% Hot

---

# Step 5: Rule Evaluation (Mamdani Inference)

### Rule 1

IF Temperature is **Cold**

THEN Speed is Slow

Firing strength

$$
0
$$

Rule doesn't fire.

---

### Rule 2

IF Temperature is Warm

THEN Speed is Medium

Firing strength

$$
0.5
$$

Output Medium is clipped at

$$
0.5
$$

---

### Rule 3

IF Temperature is Hot

THEN Speed is Fast

Firing strength

$$
0.5
$$

Output Fast is clipped at

$$
0.5
$$

---

# Step 6: Aggregation

Combine Medium and Fast using MAX.

The aggregated output contains:

* Medium clipped at 0.5
* Fast clipped at 0.5

---

# Step 7: Defuzzification

To keep the calculation simple, use the **weighted average of the centers** of the output fuzzy sets.

Centers:

* Medium = 50
* Fast = 75

Weights:

* Medium = 0.5
* Fast = 0.5

Therefore

$$
FanSpeed
\\=

\frac{0.5\times50+0.5\times75}
{0.5+0.5}
$$

$$

\\=\frac{25+37.5}{1}
$$

$$

\\=62.5
$$

---

# Final Answer

The crisp fan speed is

$$
62.5%
$$

---

# Summary Table


| Step            | Result            |
| --------------- | ----------------- |
| Temperature     | $50^\circ C$      |
| Cold            | 0                 |
| Warm            | 0.5               |
| Hot             | 0.5               |
| Rule 1          | Doesn't fire      |
| Rule 2          | Fires with 0.5    |
| Rule 3          | Fires with 0.5    |
| Aggregation     | Medium + Fast     |
| Defuzzification | $62.5%$ Fan Speed |






---
### ⚠️ One important exam note

This **weighted-average defuzzification** is **not the original Mamdani centroid calculation**. The true Mamdani method computes the centroid of the aggregated fuzzy area, which is more involved. However, in many university exams, teachers either:

* stop after showing the **rule firing and aggregation**, or
* allow a simplified weighted-average example unless they explicitly ask for **centroid computation**.

If your teacher expects the **full centroid calculation with clipped triangles and area moments**, I can also show that complete numerical solution step by step.
