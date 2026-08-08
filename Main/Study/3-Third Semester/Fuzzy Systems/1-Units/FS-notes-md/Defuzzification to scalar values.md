#fuzzy-system #third-semester 
#fuzzy-system #third-semester

# Defuzzification Methods

Defuzzification converts a **fuzzy output set** into a **single crisp value**.

Suppose the fuzzy output is

$$
B=
\left\{
\frac{0.2}{10}
+
\frac{0.5}{20}
+
\frac{0.8}{30}
+
\frac{0.8}{40}
+
\frac{0.3}{50}
\right\}
$$

| Output ($x$)       | 10  | 20  | 30  | 40  | 50  |
| ------------------ | --- | --- | --- | --- | --- |
| Membership ($\mu$) | 0.2 | 0.5 | 0.8 | 0.8 | 0.3 |

---

# 1. Maximum Membership Method (Max Membership)

## Definition

Choose the output value having the **highest membership value**.

$$
x^*
===

\arg\max(\mu(x))
$$

## Example

The maximum membership is

$$
0.8
$$

It occurs at

$$
x=30,;40
$$

The **Maximum Membership Method** selects **the first maximum**.

Therefore,

$$
\boxed{x^*=30}
$$

---

# 2. Mean of Maximum (MOM)

## Definition

If more than one output has the maximum membership, take their average.

$$
x^*
===

\frac{x_1+x_2+\cdots+x_n}{n}
$$

## Example

Maximum membership

$$
0.8
$$

occurs at

$$
30,;40
$$

Therefore,

$$
x^*
===

\frac{30+40}{2}
=
35
$$

Hence,

$$
\boxed{x^*=35}
$$

---

# 3. Weighted Average Method

## Definition

Multiply each output value by its membership, add them, then divide by the sum of memberships.

$$
x^*
===

\frac{\sum x_i\mu(x_i)}
{\sum \mu(x_i)}
$$

## Example

Numerator

$$

10(0.2)
+
20(0.5)
+
30(0.8)
+
40(0.8)
+
50(0.3)
$$

 $$

 2+10+24+32+15

83
$$

Denominator

 $$

 0.2+0.5+0.8+0.8+0.3

2.6
$$

Therefore,

$$
x^*
===

 \frac{83}{2.6}
=
31.92
$$

Hence,

$$
\boxed{x^*\approx31.92}
$$

---

# 4. Centroid Method (Center of Gravity)

## Definition

The centroid method finds the **balance point** (center of gravity) of the fuzzy set.

For discrete fuzzy sets, the formula is the same as the weighted average.

$$
x^*
===

\frac{\sum x_i\mu(x_i)}
{\sum \mu(x_i)}
$$

## Example

Using the same fuzzy set,

Numerator

$$
83
$$

Denominator

$$
2.6
$$

Therefore,

$$
x^*
===

 \frac{83}{2.6}

31.92
$$

Hence,

$$
\boxed{x^*\approx31.92}
$$

**Note:** For **discrete fuzzy sets**, the **Weighted Average** and **Centroid** methods give the same result. For **continuous fuzzy sets**, the centroid method uses integration and may differ.

---

# Quick Comparison

| Method             | Idea                                               | Result  |
| ------------------ | -------------------------------------------------- | ------- |
| Maximum Membership | Choose the output with the highest membership.     | $30$    |
| Mean of Maximum    | Average all outputs having the highest membership. | $35$    |
| Weighted Average   | Weighted mean using memberships.                   | $31.92$ |
| Centroid           | Center of gravity of the fuzzy set.                | $31.92$ |

---

# Remember

* **Maximum Membership:** Highest membership only.
* **Mean of Maximum:** Average of all highest-membership values.
* **Weighted Average:** Uses every membership as a weight.
* **Centroid:** Finds the center of gravity (most commonly used method).
