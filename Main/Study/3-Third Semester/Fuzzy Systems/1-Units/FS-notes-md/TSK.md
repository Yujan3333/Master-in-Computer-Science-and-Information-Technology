#fuzzy-system #third-semester 


# What is TSK (Sugeno) Inference?

**TSK (Takagi–Sugeno–Kang)** is a fuzzy inference method where:

* The **antecedent** is fuzzy (same as Mamdani).
* The **consequent is not a fuzzy set**.
* Instead, the consequent is a **crisp constant or a mathematical function**.

General rule:

$$
\text{IF }x\text{ is }A\text{ AND }y\text{ is }B
\text{ THEN }z=f(x,y)
$$

---

# Difference from Mamdani

Mamdani rule

```text
IF Temperature is High
THEN Fan Speed is Fast
```

Here "Fast" is a **fuzzy set**.

---

TSK rule

```text
IF Temperature is High
THEN Fan Speed = 2T + 10
```

or

```text
IF Temperature is High
THEN Fan Speed = 80
```

Here the consequent is already **crisp**.

---

# Types of TSK

## 1. Zero-order Sugeno

Consequent is a constant.

Example

```text
IF Temperature is High
THEN Fan Speed = 80
```

---

## 2. First-order Sugeno

Consequent is a linear equation.

Example

```text
IF Temperature is High
THEN Fan Speed = 2T + 5
```

---

# General Procedure

Suppose there are two rules.

Rule 1

```text
IF x is Small
AND y is High
THEN z = x + y + 2
```

Rule 2

```text
IF x is Large
AND y is High
THEN z = 2x - y + 5
```

---

## Step 1: Fuzzification

Suppose

$$
x=3,\qquad y=8
$$

Calculate memberships.

Example

$$
\mu_{Small}(3)=0.6
$$

$$
\mu_{Large}(3)=0.4
$$

$$
\mu_{High}(8)=0.8
$$

---

## Step 2: Compute firing strength

Using AND

Rule 1

$$
w_1=\min(0.6,0.8)=0.6
$$

Rule 2

$$
w_2=\min(0.4,0.8)=0.4
$$

---

## Step 3: Evaluate the consequent function

Rule 1

$$
z_1=x+y+2
$$

Substitute

$$
z_1=3+8+2=13
$$

---

Rule 2

$$
z_2=2x-y+5
$$

$$
z_2=6-8+5=3
$$

Notice that each rule immediately produces a **crisp number**.

---

## Step 4: Weighted Average

Combine all rule outputs.

$$
z=
\frac{\sum w_i z_i}
{\sum w_i}
$$

Substitute

$$
z=
\frac{0.6(13)+0.4(3)}
{0.6+0.4}
$$

# $$

9
$$

Final output

$$
z=9
$$

No further processing is needed.

---

# Why is there no defuzzification?

In Mamdani,

each rule outputs a **fuzzy set**.

Example

```text
Rule 1 → Fast
Rule 2 → Medium
```

These fuzzy outputs must be combined and then converted to a crisp value.

---

In TSK,

each rule outputs a **number**.

Example

```text
Rule 1 → 13
Rule 2 → 3
```

Since these are already crisp, we only compute a weighted average.

Therefore,

**weighted average replaces defuzzification.**

---

# Flow of TSK

```text
Crisp Inputs
      │
      ▼
Fuzzification
      │
      ▼
Rule Evaluation
      │
      ▼
Compute firing strength
      │
      ▼
Evaluate consequent functions
      │
      ▼
Weighted Average
      │
      ▼
Final Crisp Output
```

---

# Comparison with Mamdani

| Mamdani                        | TSK (Sugeno)                         |
| ------------------------------ | ------------------------------------ |
| Consequent is a fuzzy set      | Consequent is a constant or function |
| Output of each rule is fuzzy   | Output of each rule is crisp         |
| Need aggregation of fuzzy sets | No aggregation of fuzzy sets         |
| Defuzzification required       | No defuzzification required          |
| Slower                         | Faster                               |

---

# One-line exam definition

**TSK (Takagi–Sugeno–Kang) inference is a fuzzy inference method in which the antecedents are fuzzy, but the consequent of each rule is a crisp constant or mathematical function. The firing strength of each rule is computed from the antecedents, the consequent function is evaluated to obtain a crisp output for each rule, and the final output is obtained by taking the weighted average of all rule outputs.**

---

## The most important thing to remember

The **only major difference** between Mamdani and TSK is the **consequent**:

* **Mamdani:** Consequent = **Fuzzy set** → clip/scale → aggregate → defuzzify.
* **TSK:** Consequent = **Constant or function** → evaluate → weighted average → final crisp output.

That single change is why TSK is computationally faster and does not require a separate defuzzification step.
