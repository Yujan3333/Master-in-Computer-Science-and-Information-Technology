#fuzzy-system 

## Cylindrical Extension in Fuzzy Set

**Cylindrical extension** means extending a fuzzy set defined on one universe to a higher-dimensional product universe without changing its original membership values.

It is used when combining fuzzy sets on different universes, such as for unions, intersections, or relations on $X\times Y$.

---

## 1. Cylindrical Extension of A over $X\times Y$

Suppose:

* $A$ is a fuzzy set on $X$
* $Y$ is another universe

Then the cylindrical extension of $A$ to $X\times Y$ is written as $A^c$ or sometimes $A\times Y$.

Its membership function is:

$$\mu_{A^c}(x,y)=\mu_A(x)\quad \forall(x,y)\in X\times Y$$

This means membership depends only on $x$, and is repeated for every $y$.

---

## 2. Cylindrical Extension of B over $X\times Y$

If $B$ is a fuzzy set on $Y$, then extension to $X\times Y$ is:

$$\mu_{B^c}(x,y)=\mu_B(y)$$

This depends only on $y$.

---

## Why Called Cylindrical?

Because in geometric view, the membership values are stretched uniformly along the new axis, creating a cylinder-like shape.

---

## Example

Let:

$$X={x_1,x_2},\quad Y={y_1,y_2,y_3}$$

Fuzzy set on $X$:

$$A={(x_1,0.3),(x_2,0.8)}$$

### Cylindrical Extension of $A$ over $X\times Y$

|       | $y_1$ | $y_2$ | $y_3$ |
| ----- | ----- | ----- | ----- |
| $x_1$ | 0.3   | 0.3   | 0.3   |
| $x_2$ | 0.8   | 0.8   | 0.8   |

So:

$$\mu_{A^c}(x_1,y)=0.3,\quad \mu_{A^c}(x_2,y)=0.8$$

for every $y\in Y$.

---

## How Calculated

### For set on $X$:

Copy each $\mu_A(x)$ across all $y\in Y$.

### For set on $Y$:

Copy each $\mu_B(y)$ across all $x\in X$.

---

## Use in Operations

To combine $A$ on $X$ and $B$ on $Y$, first extend both to $X\times Y$, then apply operations:

$$\mu_{A\cap B}(x,y)=\min(\mu_A(x),\mu_B(y))$$

$$\mu_{A\cup B}(x,y)=\max(\mu_A(x),\mu_B(y))$$

---

## 5-Mark Exam Answer

Cylindrical extension is the process of extending a fuzzy set from one universe to a product universe such as $X\times Y$. If $A$ is a fuzzy set on $X$, then its cylindrical extension over $X\times Y$ is defined by:

$$\mu_{A^c}(x,y)=\mu_A(x)$$

for all $(x,y)\in X\times Y$. Similarly, for fuzzy set $B$ on $Y$:

$$\mu_{B^c}(x,y)=\mu_B(y)$$

It is used to perform fuzzy operations between sets defined on different universes.
