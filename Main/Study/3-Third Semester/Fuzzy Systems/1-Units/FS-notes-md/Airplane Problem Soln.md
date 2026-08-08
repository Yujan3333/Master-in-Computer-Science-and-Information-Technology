#fuzzy-system #third-semester 

This is a **Mamdani Fuzzy Inference System** problem. We solve it in the standard order:

1. Fuzzification
2. Rule Evaluation
3. Aggregation
4. Defuzzification (Centroid)

---

# Step 1. Fuzzification

## Input 1: Height

Given

$$
h_0=1000\text{ ft}
$$

From the height membership table,

| Set            | Membership |
| -------------- | ---------: |
| Large (L)      |          1 |
| Medium (M)     |        0.6 |
| Small (S)      |          0 |
| Near Zero (VS) |          0 |

Therefore,

$$
\mu_L(1000)=1
$$

$$
\mu_M(1000)=0.6
$$

$$
\mu_S(1000)=0
$$

$$
\mu_{VS}(1000)=0
$$

---

## Input 2: Vertical Velocity

Given

$$
v_0=-20\text{ ft/s}
$$

From the velocity table,

| Set | Membership |
| --- | ---------: |
| PL  |          0 |
| PS  |          0 |
| Z   |          0 |
| NS  |          0 |
| NL  |          1 |

Therefore,

$$
\mu_{NL}(-20)=1
$$

All others are zero.

---

# Step 2. Find Fired Rules

Only non-zero memberships participate.

Height has

* Large = 1
* Medium = 0.6

Velocity has

* NL = 1

Therefore only two rules fire.

---

## Rule 1

IF

Height = Large

AND

Velocity = NL

THEN

Force = NL

Firing strength

Using Mamdani,

$$
\alpha_1=\min(1,1)=1
$$

Output

$$
NL
$$

---

## Rule 2

IF

Height = Medium

AND

Velocity = NL

THEN

Force = NL

Firing strength

$$
\alpha_2=\min(0.6,1)=0.6
$$

Output

$$
NL
$$

---

All remaining rules contain zero memberships.

So they never fire.

---

# Step 3. Aggregate Outputs

Both rules produce the same output:

$$
NL
$$

The first clips NL at

$$
1
$$

The second clips NL at

$$
0.6
$$

Aggregation uses MAX.

Therefore

$$
\max(1,0.6)=1
$$

Hence the final output fuzzy set is simply the original **Negative Large** membership function.

No other output set contributes.

---

# Step 4. Construct Aggregated Output

The NL membership table is

| Force |   μ |
| ----: | --: |
|   -30 |   1 |
|   -25 |   1 |
|   -20 |   1 |
|   -15 | 0.5 |
|   -10 |   0 |
|    -5 |   0 |
|     0 |   0 |
|     5 |   0 |
|    10 |   0 |
|    15 |   0 |
|    20 |   0 |
|    25 |   0 |
|    30 |   0 |

Since aggregation clipped it at 1, it remains unchanged.

---

# Step 5. Defuzzification (Centroid)

For discrete centroid,

$$
f_0=
\frac{\sum x_i\mu(x_i)}
{\sum \mu(x_i)}
$$

Compute numerator

| Force |   μ | Force × μ |
| ----: | --: | --------: |
|   -30 |   1 |       -30 |
|   -25 |   1 |       -25 |
|   -20 |   1 |       -20 |
|   -15 | 0.5 |      -7.5 |
|   -10 |   0 |         0 |
|    -5 |   0 |         0 |
|     0 |   0 |         0 |
|     5 |   0 |         0 |
|    10 |   0 |         0 |
|    15 |   0 |         0 |
|    20 |   0 |         0 |
|    25 |   0 |         0 |
|    30 |   0 |         0 |

Numerator

$$
=-30-25-20-7.5
$$

$$
=-82.5
$$

Denominator

$$
1+1+1+0.5=3.5
$$

Therefore

$$
f_0=\frac{-82.5}{3.5}
$$

$$
f_0=-23.57
$$

---

# Final Answer

The fuzzy output after aggregation is

$$
\boxed{\text{Negative Large (NL)}}
$$

The defuzzified control force is

$$
\boxed{f_0\approx -23.57}
$$

---

## Final Summary

### Fuzzification

$$
\mu_L(1000)=1,\qquad
\mu_M(1000)=0.6
$$

$$
\mu_{NL}(-20)=1
$$

---

### Fired Rules

| Rule               | Output | Strength |
| ------------------ | ------ | -------: |
| Large AND NL → NL  | NL     |        1 |
| Medium AND NL → NL | NL     |      0.6 |

---

### Aggregation

Using MAX,

$$
\mu_{NL}(x)=1
$$

---

### Defuzzification

$$
f_0=
\frac{\sum x\mu(x)}
{\sum \mu(x)}
=============

 \frac{-82.5}{3.5}
=
-23.57
$$

Therefore, the **Mamdani controller applies a control force of approximately**

$$
\boxed{f_0=-23.57}
$$

to oppose the aircraft's downward motion.
