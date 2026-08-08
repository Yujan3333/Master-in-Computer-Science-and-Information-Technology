#fuzzy-system #third-semester #mamdani-inference-method

We will build a simple **fan speed controller**.

Problem:

> A fuzzy controller decides the **fan speed** based on **temperature**.

Input:

* Temperature (°C)

Output:

* Fan Speed (RPM)

We will use:

* **Mamdani Max-Min inference**
* **Centroid defuzzification**

---

# Step 0: Define Fuzzy Sets

A fuzzy system first needs fuzzy sets.

## Input Variable: Temperature

Universe:

$$
T = [0,40]^\circ C
$$

We define three fuzzy sets:

1. Low temperature (L)
2. Medium temperature (M)
3. High temperature (H)

---

## Temperature Membership Functions

### Low Temperature

| Temperature |  0 |  10 | 20 |
| ----------- | -: | --: | -: |
| Low         |  1 | 0.5 |  0 |

Graphically:

```
Low

μ
1 |\
  | \
0 |__\____
 0  10  20
```

---

### Medium Temperature

| Temperature | 10 | 20 | 30 |
| ----------- | -: | -: | -: |
| Medium      |  0 |  1 |  0 |

```
Medium

μ
1     /\
     /  \
0 ___/____\___
 10 20  30
```

---

### High Temperature

| Temperature | 20 |  30 | 40 |
| ----------- | -: | --: | -: |
| High        |  0 | 0.5 |  1 |

```
High

μ
1       /
       /
0 ____/____
20  30  40
```

---

# Output Variable: Fan Speed

Universe:

$$
F=[0,1000]RPM
$$

We define:

1. Slow
2. Medium
3. Fast

| Fan Speed |  0 | 500 | 1000 |
| --------- | -: | --: | ---: |
| Slow      |  1 |   0 |    0 |

| Fan Speed | 250 | 500 | 750 |
| --------- | --: | --: | --: |
| Medium    |   0 |   1 |   0 |

| Fan Speed | 500 | 1000 |
| --------- | --: | ---: |
| Fast      |   0 |    1 |

---

# Step 1: Create Rule Base

Now we create rules.

Example:

### Rule 1

```
IF Temperature is Low
THEN Fan Speed is Slow
```

### Rule 2

```
IF Temperature is Medium
THEN Fan Speed is Medium
```

### Rule 3

```
IF Temperature is High
THEN Fan Speed is Fast
```

Notice:

Each rule has:

```
ONE antecedent → ONE consequent
```

---

# Step 2: Give Input

Suppose:

$$
Temperature = 25^\circ C
$$

Now we ask:

> How much does 25°C belong to each fuzzy set?

This is called **fuzzification**.

---

# Step 3: Fuzzification

## Low membership

From the Low graph:

At 20°C:

$$
\mu_L(20)=0
$$

After 20:

$$
\mu_L(25)=0
$$

Therefore:

$$
\boxed{\mu_L(25)=0}
$$

---

## Medium membership

Medium triangle:

At 20:

$$
\mu_M(20)=1
$$

At 30:

$$
\mu_M(30)=0
$$

25 is halfway:

$$
\mu_M(25)=0.5
$$

---

## High membership

High starts at 20 and reaches 1 at 40.

At 30:

$$
\mu_H(30)=0.5
$$

Therefore at 25:

$$
\mu_H(25)=0.25
$$

---

So:

| Temperature Set | Membership |
| --------------- | ---------: |
| Low             |          0 |
| Medium          |        0.5 |
| High            |       0.25 |

Meaning:

25°C is:

* not Low
* 50% Medium
* 25% High

---

# Step 4: Rule Evaluation

Now evaluate each rule.

Remember:

For Mamdani:

$$
\text{Firing strength}=\text{membership of antecedent}
$$

---

## Rule 1

```
IF Temperature is Low
THEN Fan is Slow
```

Strength:

$$
\alpha_1=\mu_L(25)
$$

$$
\alpha_1=0
$$

Rule does not fire.

---

## Rule 2

```
IF Temperature is Medium
THEN Fan is Medium
```

Strength:

$$
\alpha_2=\mu_M(25)
$$

$$
\alpha_2=0.5
$$

Rule fires with strength 0.5.

---

## Rule 3

```
IF Temperature is High
THEN Fan is Fast
```

Strength:

$$
\alpha_3=\mu_H(25)
$$

$$
\alpha_3=0.25
$$

Rule fires with strength 0.25.

---

# Step 5: Apply Firing Strength to Output

This is the **Min operation**.

The firing strength clips the output membership function.

---

## Rule 2 Output

Original:

```
Medium fan speed
```

Membership:

```
      /\
     /  \
____/____\____
```

Firing strength:

$$
0.5
$$

So cut the graph at:

$$
\mu=0.5
$$

Output becomes:

```
      ______
     |      |
_____|      |____
```

---

## Rule 3 Output

Original:

```
Fast fan speed
```

Firing strength:

$$
0.25
$$

Clip Fast set at:

$$
\mu=0.25
$$

---

# Step 6: Aggregation (MAX)

Now we have two outputs:

Rule 2:

```
Medium speed clipped at 0.5
```

Rule 3:

```
Fast speed clipped at 0.25
```

Combine them using:

$$
\mu_{output}(x)
===============

\max(\mu_{M}(x),\mu_F(x))
$$

Why?

Because either rule can contribute.

The strongest membership value is kept.

---

The final fuzzy output:

```
Membership


1
|
|
0.5       ______
         /      \
0.25             ______
                /      \
____________________________
0       500       1000

       Fan Speed
```

Now we have **one fuzzy set**.

---

# Step 7: [Defuzzification-Centroid](Defuzzification-Centroid.md)

The controller needs one number.

Use centroid:

$$
FanSpeed=
\frac{\int x\mu(x)dx}
{\int\mu(x)dx}
$$

After calculation:

Assume:

$$
FanSpeed=625RPM
$$

---

# Final Answer

For input:

$$
Temperature=25^\circ C
$$

The controller output is:

$$
\boxed{Fan\ Speed=625RPM}
$$

---

# Why every step was done?

| Step              | Why?                                         |
| ----------------- | -------------------------------------------- |
| Define fuzzy sets | Convert human words into mathematical form   |
| Fuzzification     | Find how much input belongs to each set      |
| Rule evaluation   | Find which rules are active                  |
| Min operation     | Limit the rule's influence                   |
| Clipping          | Modify consequent according to rule strength |
| Aggregation       | Combine all rule opinions                    |
| Defuzzification   | Convert fuzzy answer into one usable number  |

---

The key idea:

**Mamdani does not choose one rule.**

For input 25°C:

```
Rule 2 says:
Fan should be Medium (50% confidence)

Rule 3 says:
Fan should be Fast (25% confidence)
```

Mamdani combines both opinions and produces one final speed.
