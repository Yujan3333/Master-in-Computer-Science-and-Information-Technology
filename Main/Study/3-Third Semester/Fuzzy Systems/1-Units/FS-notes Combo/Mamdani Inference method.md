#fuzzy-system #third-semester 

> [!info]+ What is Inference?
> Inference means to reach a particular conclusion based on some evidence associated with a logic


---
### References
- [Example-Mamdani Inference](https://www.youtube.com/watch?v=THAk1O3HBDc)


---

Let's focus **only on the Mamdani Fuzzy Inference System** and understand **why each step exists**.

---

# The Main Idea of Mamdani

Mamdani answers this question:

> **"If several fuzzy rules are true at the same time, how do we combine them to get one final decision?"**

It does **not** invent new rules.

It simply evaluates **all existing rules** and combines their outputs.

---

# Step 0: We already have rules

Suppose we have these rules:

```text
R1: IF Temperature is Low
    THEN Fan Speed is Slow

R2: IF Temperature is Medium
    THEN Fan Speed is Medium

R3: IF Temperature is High
    THEN Fan Speed is Fast
```

Notice:

* 3 rules
* Each rule has **one consequent**.
* There are **not multiple consequents in one rule**.

---

# Step 1: Give an input

Suppose

$$
\text{Temperature} = 28^\circ C
$$

Now ask:

> Which rules are true?

Since fuzzy sets overlap,

28°C may belong to more than one fuzzy set.

Example

| Fuzzy Set | Membership |
| --------- | ---------: |
| Low       |        0.0 |
| Medium    |        0.4 |
| High      |        0.6 |

So,

* Rule 1 → not active
* Rule 2 → active with strength 0.4
* Rule 3 → active with strength 0.6

This is called the **firing strength** (or activation level) of each rule.

---

# Step 2: Each fired rule produces an output

Rule 2 says

```text
IF Temperature is Medium
THEN Fan Speed is Medium
```

Since it fires with strength **0.4**,

the output fuzzy set "Medium Speed" is clipped at 0.4.

Rule 3 says

```text
IF Temperature is High
THEN Fan Speed is Fast
```

Since it fires with strength **0.6**,

the output fuzzy set "Fast Speed" is clipped at 0.6.

Now we have:

* Medium-speed fuzzy set (clipped to 0.4)
* Fast-speed fuzzy set (clipped to 0.6)

These are **two separate output fuzzy sets**.

---

# This is the important question

Now the system has two opinions.

Rule 2 says

> Medium speed

Rule 3 says

> Fast speed

**Which one should the fan actually use?**

We cannot output both.

This is why aggregation is needed.

---

# Step 3: Aggregation

Aggregation combines all output fuzzy sets into **one fuzzy set**.

Usually using the **maximum (max)** operator.

Conceptually:

```text
Output from Rule 2
        +
Output from Rule 3
        ↓
One combined fuzzy output
```

After aggregation, there is only **one** output membership function.

---

# Step 4: Defuzzification

Even after aggregation,

the result is still fuzzy.

The controller cannot use

```text
Medium = 0.4
Fast = 0.6
```

It needs one number.

For example

```text
Fan Speed = 720 RPM
```

So Mamdani computes the centroid:

$$
y^*=\frac{\int y,\mu(y),dy}{\int \mu(y),dy}
$$

This produces one crisp output.

---

# The complete picture

```text
Input
  │
  ▼
Fuzzification
  │
  ▼
Evaluate all rules
  │
  ▼
Rule outputs
(Medium, Fast, ...)
  │
  ▼
Aggregation
(combine all outputs)
  │
  ▼
One fuzzy output
  │
  ▼
Defuzzification
  │
  ▼
One crisp output
```

---

# The most common misunderstanding

Many students think:

> "Inference means one rule has many consequents."

❌ This is **not** how standard Mamdani works.

Instead:

```text
Rule 1 → one consequent
Rule 2 → one consequent
Rule 3 → one consequent
```

The system evaluates **many rules**, so **many rule outputs** are produced.

Those outputs are then aggregated into one fuzzy output.

---

# One sentence to remember for exams

**In Mamdani inference, multiple fuzzy rules may fire simultaneously. Each fired rule generates its own fuzzy output (by clipping or scaling the consequent fuzzy set according to its firing strength), and these outputs are aggregated into a single fuzzy output, which is then defuzzified to obtain the final crisp result.**
