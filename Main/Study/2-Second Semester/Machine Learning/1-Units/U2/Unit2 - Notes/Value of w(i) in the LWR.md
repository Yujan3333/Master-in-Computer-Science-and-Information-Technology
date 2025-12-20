
## ✅ Correct relationship

> **The closer a point is to the query point, the LARGER its weight $w^{(i)}$.**
> **The farther a point is, the SMALLER its weight $w^{(i)}$.**

---

## Why? (Using the formula)

You have the weight function:

$$
w^{(i)} = \exp\left(-\frac{(x^{(i)} - x_q)^2}{2\tau^2}\right)
$$

Now look carefully:

### Case 1: Point is **very close** to query point

* $(x^{(i)} - x_q)^2 \approx 0$
* Exponent $\approx 0$
* $w^{(i)} = e^0 = 1$ (maximum weight)

👉 **Near point → high weight**

---

### Case 2: Point is **far** from query point

* $(x^{(i)} - x_q)^2$ is large
* Exponent is a large negative number
* $w^{(i)} \approx 0$

👉 **Far point → low weight**

---

## Simple Table (Easy to Remember)

| Distance from query point | Weight $w^{(i)}$        |
| ------------------------- | ----------------------- |
| Very near                 | Large (close to 1)      |
| Medium                    | Moderate                |
| Very far                  | Very small (close to 0) |

---

## Intuition (Best way to remember)

Think of **importance** instead of math:

* Near point → **important** → large weight
* Far point → **less important** → small weight

---

## One-Line Exam-Safe Statement ✅

> In locally weighted regression, points closer to the query point are assigned **higher weights**, while distant points receive **lower weights**.

---