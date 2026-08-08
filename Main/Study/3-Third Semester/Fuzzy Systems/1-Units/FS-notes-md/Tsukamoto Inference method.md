#fuzzy-system #third-semester 


# What is Tsukamoto Inference?

In **Tsukamoto inference**:

* The **antecedents are fuzzy** (same as Mamdani and TSK).
* The **consequent is also a fuzzy set** (like Mamdani).
* **However, the consequent membership function must be monotonic (always increasing or always decreasing).**
* Each rule produces a **crisp output**, and the final output is obtained using a **weighted average**.

---

# General Rule

$$
\text{IF }x\text{ is }A
\text{ AND }y\text{ is }B
\text{ THEN }z\text{ is }C
$$

where

* $A$ and $B$ are fuzzy antecedents.
* $C$ is a **monotonic fuzzy set**.

---

# Why must the consequent be monotonic?

Because after finding the firing strength, we must determine **one unique output value**.

Suppose the firing strength is

$$
\alpha=0.6
$$

We need to find the output value

$$
z
$$

such that

$$
\mu_C(z)=0.6
$$

If the membership function is monotonic, there is only **one** such value.

---

### Monotonic membership function

Increasing

```text
μ

1 |        /
  |      /
  |    /
0 +------------------>
```

or

Decreasing

```text
μ

1 |\
  | \
  |  \
0 +------------------>
```

---

### Non-monotonic (not allowed)

Triangular

```text
μ

1 |    /\
  |   /  \
  |  /    \
0 +------------------>
```

Here,

$$
\mu=0.6
$$

may occur at **two different output values**.

So we wouldn't know which output to choose.

---

# Steps of Tsukamoto Inference

Assume two rules.

Rule 1

```text
IF Temperature is High
THEN Fan Speed is Fast
```

Rule 2

```text
IF Temperature is Medium
THEN Fan Speed is Medium
```

---

## Step 1: Fuzzification

Suppose

$$
T=30^\circ C
$$

Memberships

$$
\mu_{High}=0.7
$$

$$
\mu_{Medium}=0.3
$$

---

## Step 2: Compute firing strength

Rule 1

$$
w_1=0.7
$$

Rule 2

$$
w_2=0.3
$$

---

## Step 3: Find crisp output of each rule

This is the special step in Tsukamoto.

Suppose the consequent "Fast" is monotonic.

For Rule 1

$$
\mu_{Fast}(z_1)=0.7
$$

From the membership function,

suppose this corresponds to

$$
z_1=90
$$

Similarly,

Rule 2

$$
\mu_{Medium}(z_2)=0.3
$$

Suppose

$$
z_2=60
$$

Each rule now has a **crisp output**.

---

## Step 4: Weighted Average

Compute

$$
z=
\frac{\sum w_i z_i}
{\sum w_i}
$$

Substitute

$$
z=
\frac{0.7(90)+0.3(60)}
{0.7+0.3}
$$

$$
=81
$$

Final output

$$
z=81
$$

---

# Why is there no defuzzification?

Each rule already produces a **crisp output**.

So the final output is simply

$$
\frac{\sum w_i z_i}
{\sum w_i}
$$

There is no aggregated fuzzy set to defuzzify.

---

# Flow of Tsukamoto

```text
Crisp Inputs
      │
      ▼
Fuzzification
      │
      ▼
Compute firing strengths
      │
      ▼
Use monotonic consequent to find
one crisp output for each rule
      │
      ▼
Weighted Average
      │
      ▼
Final Crisp Output
```

---

# Comparison with Mamdani

| Mamdani                       | Tsukamoto                         |
| ----------------------------- | --------------------------------- |
| Consequent is any fuzzy set   | Consequent must be monotonic      |
| Each rule outputs a fuzzy set | Each rule outputs a crisp value   |
| Aggregate fuzzy sets          | Weighted average of crisp outputs |
| Defuzzification required      | No defuzzification                |

---

# Comparison with TSK

| TSK                                               | Tsukamoto                                                                |
| ------------------------------------------------- | ------------------------------------------------------------------------ |
| Consequent is a constant or mathematical function | Consequent is a monotonic fuzzy set                                      |
| Crisp output comes from evaluating the function   | Crisp output comes from the inverse of the monotonic membership function |
| Weighted average                                  | Weighted average                                                         |
| No defuzzification                                | No defuzzification                                                       |

---

# Memory Trick

* **Mamdani:** Fuzzy → **Fuzzy** → Defuzzify
* **TSK (Sugeno):** Fuzzy → **Equation** → Weighted Average
* **Tsukamoto:** Fuzzy → **Monotonic Fuzzy Set** → **Inverse Membership** → Weighted Average

---

# One-line exam answer

**Tsukamoto inference is a fuzzy inference method in which the antecedents are fuzzy and the consequent of each rule is a monotonic fuzzy set. The firing strength of each rule is used to obtain a unique crisp output from the monotonic consequent, and the final output is computed as the weighted average of all rule outputs.**
