In your fuzzy system, **clipping** and **scaling** are two different ways of applying the rule firing strength to the output fuzzy set in Mamdani inference.

Here the firing strength of Rule 2 is:

$$\alpha_2=0.7$$

and the consequent/output fuzzy set is:

$$\mu_{GQ}=\left\{\frac{0}{6}+\frac{0.4}{10}+\frac{0.6}{15}+\frac{0.8}{20}+\frac{0.5}{25}+\frac{0.3}{30}+\frac{0}{39}\right\}$$

---

# 1. Clipping (Min Method)

In clipping, we **cut off** all membership values above the firing strength.

Mathematically:

$$\mu'(y)=\min(\mu(y),\alpha)$$

Here:

$$\alpha=0.7$$

So every value greater than 0.7 becomes 0.7.

---

## Original Good Quality Set

$$\mu_{GQ}=\left\{\frac{0}{6}+\frac{0.4}{10}+\frac{0.6}{15}+\frac{0.8}{20}+\frac{0.5}{25}+\frac{0.3}{30}+\frac{0}{39}\right\}$$

---

## Apply Clipping

At point 20:

$$0.8>0.7$$

So it becomes:

$$0.7$$

All other values are already below 0.7, so they stay unchanged.

---

## Clipped Output

$$\mu_{GQ}^{clip}=\left\{\frac{0}{6}+\frac{0.4}{10}+\frac{0.6}{15}+\frac{0.7}{20}+\frac{0.5}{25}+\frac{0.3}{30}+\frac{0}{39}\right\}$$

---

# Visualization Idea

Think of the fuzzy set as a mountain.

* Clipping = cutting the top flat using a horizontal knife at height 0.7.

So:

* anything above 0.7 is removed
* anything below 0.7 remains same

---

# 2. Scaling (Product Method)

In scaling, we multiply every membership value by the firing strength.

Mathematically:

$$\mu'(y)=\alpha\times\mu(y)$$

Here:

$$\alpha=0.7$$

---

## Original Values

| y  | μ(y) |
| -- | ---- |
| 6  | 0    |
| 10 | 0.4  |
| 15 | 0.6  |
| 20 | 0.8  |
| 25 | 0.5  |
| 30 | 0.3  |
| 39 | 0    |

---

## Multiply Each by 0.7

| y  | New μ(y)              |
| -- | --------------------- |
| 6  | $$0\times0.7=0$$      |
| 10 | $$0.4\times0.7=0.28$$ |
| 15 | $$0.6\times0.7=0.42$$ |
| 20 | $$0.8\times0.7=0.56$$ |
| 25 | $$0.5\times0.7=0.35$$ |
| 30 | $$0.3\times0.7=0.21$$ |
| 39 | $$0\times0.7=0$$      |

---

## Scaled Output

$$\mu_{GQ}^{scale}=\left\{\frac{0}{6}+\frac{0.28}{10}+\frac{0.42}{15}+\frac{0.56}{20}+\frac{0.35}{25}+\frac{0.21}{30}+\frac{0}{39}\right\}$$

---

# Main Difference

| Clipping                               | Scaling                            |
| -------------------------------------- | ---------------------------------- |
| Uses min operator                      | Uses multiplication                |
| Only cuts values above firing strength | Reduces every value proportionally |
| Shape mostly same                      | Entire set shrinks vertically      |
| Common in Mamdani                      | Common in product inference        |

---

# In Your Problem

Rule 2 fires with:

$$\alpha_2=0.7$$

So:

* **Clipping:** limit output membership to maximum 0.7
* **Scaling:** multiply whole output fuzzy set by 0.7

That modified fuzzy set is then:

1. Aggregated with other rule outputs
2. Defuzzified using centroid method

to get the final crisp quality value.
