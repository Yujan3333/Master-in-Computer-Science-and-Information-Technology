#fuzzy-system #third-semester #old-que #exam-paper-answer 

- [Proper Example fan speed](Proper%20Example%20fan%20speed.md)
# Q2. Construct a Fuzzy Controller with a Set of Fuzzy Rules. Explain How Mamdani Inference is Used with an Example. (10 Marks)

## Introduction

A **Mamdani Fuzzy Controller** is a rule-based control system that uses **IF–THEN fuzzy rules** to make decisions. It converts crisp inputs into fuzzy values, evaluates the rules using fuzzy logic, combines the rule outputs, and finally converts the fuzzy result into a crisp output.

It consists of four main stages:

1. Fuzzification
2. Rule Evaluation (Inference)
3. Aggregation
4. Defuzzification

---

# Example: Fan Speed Controller

Suppose we want to automatically control the **speed of a fan** according to the **room temperature**.

## Input

Room Temperature

## Output

Fan Speed

---

# Step 1: Define Fuzzy Sets

### Input: Temperature

Three fuzzy sets are defined.

* Cold (C)
* Warm (W)
* Hot (H)

Using triangular membership functions:

```text
                 Warm
                  /\
                 /  \
Cold            /    \            Hot
 /\            /      \            /\
/  \__________/        \__________/  \

0     20      30      40        50 °C
```

---

### Output: Fan Speed

Three fuzzy sets.

* Slow
* Medium
* Fast

```text
               Medium
                 /\
                /  \
Slow           /    \           Fast
 /\           /      \           /\
/  \_________/        \_________/  \

0      40      70      100 %
```

---

# Step 2: Construct Rule Base

The controller uses expert knowledge in the form of IF–THEN rules.

| Rule | IF Temperature is | THEN Fan Speed is |
| ---- | ----------------- | ----------------- |
| R1   | Cold              | Slow              |
| R2   | Warm              | Medium            |
| R3   | Hot               | Fast              |

These rules tell the controller how the fan should behave.

---

# Step 3: Fuzzification

Suppose the room temperature is

$$
35^\circ C
$$

Instead of saying

> Temperature is Hot

the fuzzy controller calculates **membership values**.

Assume

$$
\mu_{Warm}(35)=0.5
$$

$$
\mu_{Hot}(35)=0.5
$$

$$
\mu_{Cold}(35)=0
$$

This means

* Temperature is **50% Warm**
* Temperature is **50% Hot**
* Temperature is **not Cold**

---

# Step 4: Mamdani Inference

The controller now checks every rule.

### Rule 1

IF Temperature is Cold

THEN Fan Speed is Slow

Since

$$
\mu_{Cold}=0
$$

Rule 1 does not fire.

---

### Rule 2

IF Temperature is Warm

THEN Fan Speed is Medium

Membership

$$
0.5
$$

Therefore,

Rule 2 fires with strength

$$
0.5
$$

The output fuzzy set **Medium** is clipped at

$$
0.5
$$

---

### Rule 3

IF Temperature is Hot

THEN Fan Speed is Fast

Membership

$$
0.5
$$

Therefore,

Rule 3 also fires with strength

$$
0.5
$$

The output fuzzy set **Fast** is clipped at

$$
0.5
$$

---

# Step 5: Aggregation

Now both outputs are combined.

```text
Medium

      ______
     /      \
____/        \____

Fast

                ______
               /      \
______________/        \____

Aggregation (MAX)

Take the highest membership value at every point.
```

The result is a single fuzzy output.

---

# Step 6: Defuzzification

The combined fuzzy output is converted into a crisp value using the **Centroid Method**.

$$
Fan\ Speed=
\frac{\sum \mu(x)x}
{\sum \mu(x)}
$$

Suppose the final result is

$$
75%
$$

The fan rotates at

**75% speed**.

---

# How Mamdani Inference Works

Mamdani inference uses:

* **AND → MIN**
* **OR → MAX**

For example, consider a new rule:

> IF Temperature is Hot **AND** Humidity is High THEN Fan Speed is Fast.

Suppose

$$
\mu_{Hot}=0.7
$$

$$
\mu_{HighHumidity}=0.5
$$

The firing strength of the rule is

$$
\min(0.7,0.5)=0.5
$$

So the output fuzzy set **Fast** is clipped at **0.5**.

If another rule also suggests **Fast** with membership **0.8**, then during **aggregation**, Mamdani uses **MAX**:

$$
\max(0.5,0.8)=0.8
$$

Thus, the strongest contribution to the **Fast** output is retained.

---

# Working of Mamdani Controller

```text
Room Temperature
        │
        ▼
Fuzzification
(Convert crisp value into fuzzy values)
        │
        ▼
Apply IF–THEN Rules
        │
        ▼
Mamdani Inference
(MIN for AND, MAX for OR)
        │
        ▼
Aggregation
(Combine all rule outputs)
        │
        ▼
Defuzzification
(Centroid Method)
        │
        ▼
Fan Speed
```

---

# Advantages

* Easy to understand.
* Similar to human thinking.
* No exact mathematical model is required.
* Widely used in air conditioners, washing machines, and fan controllers.

---

# Conclusion

A **Mamdani Fuzzy Controller** controls systems using fuzzy IF–THEN rules. It converts crisp inputs into fuzzy values (**fuzzification**), evaluates rules using **MIN (AND)** and **MAX (OR)** operations (**Mamdani inference**), combines the rule outputs (**aggregation**), and finally converts the fuzzy output into a crisp value (**defuzzification**). In the fan speed example, the controller adjusts the fan speed smoothly according to the room temperature instead of making abrupt ON/OFF decisions.
