#fuzzy-system #third-semester 
# Fuzzy Inference Systems (FIS)

A **Fuzzy Inference System (FIS)** is a framework that maps **inputs → outputs** using fuzzy logic.

It consists of:

1. Fuzzification
2. Rule Evaluation
3. Aggregation (if needed)
4. Defuzzification (if needed)

The three most common inference systems are:

1. **Mamdani FIS**
2. **Sugeno FIS (also called TSK)**
3. **Tsukamoto FIS**

> **Important:**
>
> * **TSK = Takagi–Sugeno–Kang**
> * **Sugeno and TSK are the same thing.**
> * Many books simply call it **Sugeno FIS**.

---

# Comparison First

| Feature            | Mamdani     | Sugeno (TSK)                      | Tsukamoto                  |
| ------------------ | ----------- | --------------------------------- | -------------------------- |
| Consequent         | Fuzzy set   | Mathematical function or constant | Fuzzy set (monotonic only) |
| Output             | Fuzzy       | Crisp                             | Crisp                      |
| Defuzzification    | Required    | Not required                      | Not required               |
| Speed              | Slow        | Fast                              | Medium                     |
| Easy to understand | Yes         | Moderate                          | Moderate                   |
| Used in control    | Very common | AI, optimization                  | Industrial control         |

---

# 1. Mamdani Fuzzy Inference System

Developed by **Ebrahim Mamdani** in 1975.

This is the most commonly taught fuzzy inference method.

---

# Rule Structure

General form:

**IF Input is A THEN Output is B**

Example:

```
IF Temperature is High
THEN Fan Speed is Fast
```

Notice that

* High → fuzzy set
* Fast → fuzzy set

Both antecedent and consequent are fuzzy.

---

# Complete Steps

## Step 1: Fuzzification

Convert crisp input into membership values.

Example

Temperature = 32°C

Suppose

Low

$$
\mu_{Low}(32)=0
$$

Medium

$$
\mu_{Medium}(32)=0.3
$$

High

$$
\mu_{High}(32)=0.7
$$

---

## Step 2: Rule Evaluation

Suppose rules

Rule 1

```
IF Temperature is High
THEN Fan is Fast
```

Rule 2

```
IF Temperature is Medium
THEN Fan is Medium
```

Rule firing strengths

Rule 1

$$
\alpha_1=0.7
$$

Rule 2

$$
\alpha_2=0.3
$$

---

## Step 3: Implication

The firing strength modifies the output fuzzy set.

Usually

**Minimum method**

$$
\mu'(y)=\min(\alpha,\mu(y))
$$

**or Product method**

$$
\mu'(y)=\alpha\mu(y)
$$

The output membership function gets clipped or scaled.

---

## Step 4: Aggregation

Combine all rule outputs.

Usually

Maximum operator

$$
\mu(y)=\max(\mu_1,\mu_2,\ldots)
$$

Now one final fuzzy output exists.

---

## Step 5: Defuzzification

Convert fuzzy output to crisp value.

Most common

Centroid

$$
y^*=\frac{\int y\mu(y),dy}{\int\mu(y),dy}
$$

Example

Output

Fan Speed = 78 RPM

---

# Mamdani Flow

```
Input

↓

Fuzzification

↓

Rules

↓

Implication

↓

Aggregation

↓

Defuzzification

↓

Crisp Output
```

---

# Advantages

* Easy to understand
* Human-like reasoning
* Natural linguistic rules

---

# Disadvantages

* Computationally expensive
* Requires defuzzification
* Difficult for optimization

---

# Example

```
IF Temperature is High
AND Humidity is High
THEN Fan Speed is Fast
```

Output "Fast" is a fuzzy set.

---

# 2. Sugeno (TSK) Fuzzy Inference System

Developed by **Michio Sugeno** and **Takagi**, **Kang**.

Unlike Mamdani,

the consequent is **not a fuzzy set.**

It is

* constant
* mathematical equation

---

# Rule Structure

Zero-order Sugeno

```
IF x is A
AND y is B

THEN z = 15
```

Output is constant.

---

First-order Sugeno

```
IF x is A
AND y is B

THEN

z = 2x + 3y + 5
```

Output is a mathematical function.

---

# General Rule

$$
IF\ x\ is\ A_i
\ AND\ y\ is\ B_i
$$

Then

$$
z_i=f_i(x,y)
$$

where

$$
f_i=a_ix+b_iy+c_i
$$

---

# Steps

## Step 1

Fuzzification

Same as Mamdani.

---

## Step 2

Calculate firing strength.

For AND

Minimum

$$
w_i=\min(\mu_A,\mu_B)
$$

or Product

$$
w_i=\mu_A\mu_B
$$

---

## Step 3

Calculate rule output.

Suppose

Rule

```
IF Temperature High

THEN

z=2T+10
```

Temperature

30°C

Then

$$
z=2(30)+10
$$

$$
=70
$$

---

## Step 4

Weighted Average

Final output

$$
z=
\frac{\sum w_iz_i}
{\sum w_i}
$$

This directly gives the crisp output.

No defuzzification is required.

---

# Example

Rule 1

```
IF Temp High

THEN

z=80
```

Rule 2

```
IF Temp Medium

THEN

z=60
```

Suppose

$$
w_1=0.7
$$

$$
w_2=0.3
$$

Then

$$
z=
\frac{0.7(80)+0.3(60)}
{0.7+0.3}
$$

$$
=74
$$

---

# Why No Defuzzification?

Because every rule already produces a crisp value.

Instead of fuzzy outputs,

weighted averaging directly computes the final crisp output.

---

# Advantages

* Very fast
* Excellent for optimization
* Used in ANFIS
* Easy to train

---

# Disadvantages

* Less intuitive
* Consequents are mathematical equations
* Harder for experts to write manually

---

# 3. Tsukamoto Fuzzy Inference System

Developed by **Yasuhiko Tsukamoto**.

This system is between Mamdani and Sugeno.

---

# Rule Structure

```
IF Temperature High

THEN Fan Speed Fast
```

Looks identical to Mamdani.

BUT

The consequent must be **monotonic**.

---

# What is Monotonic?

Membership only

* always increasing

or

* always decreasing

Never increases then decreases.

Example

Increasing

```
0

|

|     /

|   /

| /

+------------
```

Decreasing

```
1

|\
| \
|  \
|   \

+-----------
```

Triangular membership is **not monotonic**.

---

# Why?

Each firing strength must produce exactly one crisp output.

---

# Steps

## Step 1

Fuzzification

Same.

---

## Step 2

Rule firing

Example

$$
w=0.6
$$

---

## Step 3

Find crisp output from monotonic membership.

Suppose

Fast membership

```
μ=0.6
```

Find

Output

80 RPM

---

## Step 4

Weighted Average

$$
z=
\frac{\sum w_iz_i}
{\sum w_i}
$$

Again,

No defuzzification.

---

# Example

Rule 1

```
IF Temp High

THEN Speed Fast
```

Rule strength

0.7

Fast membership gives

90 RPM

Rule output

90

Rule 2

Strength

0.3

Output

60

Final

$$
z=
\frac{0.7(90)+0.3(60)}
{1}
=81
$$

---

# Why Monotonic?

Because for every firing strength,

there must be one unique crisp value.

If the membership function were triangular, one membership value (e.g., 0.5) could correspond to two different output values, making the rule output ambiguous.

---

# Difference Between Mamdani and Sugeno

| Mamdani                | Sugeno                         |
| ---------------------- | ------------------------------ |
| Output fuzzy set       | Output equation                |
| Needs defuzzification  | No defuzzification             |
| Human readable         | Machine friendly               |
| Slower                 | Faster                         |
| Used in expert systems | Used in ANFIS and optimization |

---

# Difference Between Mamdani and Tsukamoto

| Mamdani                  | Tsukamoto                              |
| ------------------------ | -------------------------------------- |
| Output fuzzy             | Rule output becomes crisp              |
| Any membership           | Only monotonic membership              |
| Defuzzification required | No defuzzification                     |
| Aggregate fuzzy sets     | Weighted average of crisp rule outputs |

---

# Difference Between Sugeno and Tsukamoto

| Sugeno                                       | Tsukamoto                                                                                        |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Consequent is a constant or function         | Consequent is a monotonic fuzzy set                                                              |
| Rule output comes directly from the equation | Rule output is obtained by inverting the monotonic membership function using the firing strength |
| No defuzzification                           | No defuzzification                                                                               |
| Very common in ANFIS                         | Common in industrial control                                                                     |

---

# Inference Rules Summary

| System       | Rule Format                               | Consequent                        | Final Output                                        |
| ------------ | ----------------------------------------- | --------------------------------- | --------------------------------------------------- |
| Mamdani      | IF $x$ is $A$ THEN $y$ is $B$             | Fuzzy set                         | Fuzzy → defuzzified to crisp                        |
| Sugeno (TSK) | IF $x$ is $A$ THEN $z=f(x)$ or constant   | Mathematical function or constant | Crisp (weighted average)                            |
| Tsukamoto    | IF $x$ is $A$ THEN $y$ is $B$ (monotonic) | Monotonic fuzzy set               | Crisp (via inverse membership and weighted average) |

### Exam tip (very important)

Students often confuse **Sugeno** and **TSK**. Remember:

* **Takagi–Sugeno–Kang (TSK) = Sugeno Fuzzy Inference System**
* **Zero-order Sugeno:** consequent is a **constant** (e.g., $z=50$).
* **First-order Sugeno:** consequent is a **linear function** (e.g., $z=ax+by+c$).
* **Mamdani:** fuzzy output + **defuzzification**.
* **Sugeno (TSK):** crisp output from a **weighted average** of rule consequents.
* **Tsukamoto:** each rule produces a crisp output using a **monotonic** consequent membership function, then combines them with a weighted average.
