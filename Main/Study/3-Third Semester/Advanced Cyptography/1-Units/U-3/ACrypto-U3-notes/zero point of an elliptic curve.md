#advanced-cryptography #third-semester #elliptic-curve 

Sure! Here's the same explanation using **regular text** with **`$$ ... $$`** math formatting (ideal for Obsidian).

---

# Zero Point of an Elliptic Curve

The **zero point** of an elliptic curve is called the **Point at Infinity**, denoted by

$$
O
$$

It is **not an ordinary point** like $$ (x,y) $$. Instead, it is a special point added to the elliptic curve.

---

## Why is it called the Zero Point?

It behaves exactly like **0 in ordinary arithmetic**.

For normal numbers,

$$
5+0=5
$$

Similarly, for elliptic curves,

$$
P+O=P
$$

where $$P$$ is any point on the curve.

Hence, $$O$$ is called the **identity element** or **zero point**.

---

## Example

Suppose

$$
P=(2,3)
$$

Then,

$$
P+O=(2,3)
$$

The point remains unchanged.

---

## Relation with Inverse Points

If

$$
P=(x,y)
$$

then its inverse is

$$
-P=(x,-y)
$$

Adding a point to its inverse gives the zero point:

$$
P+(-P)=O
$$

This is similar to ordinary arithmetic:

$$
5+(-5)=0
$$

---

## Why is the Zero Point Needed?

Without the point at infinity, point addition would not always satisfy the properties required for cryptography.

The zero point ensures that the set of points forms an **Abelian group**, where every point has:

* An identity element
* An inverse
* Closure under addition

---

## Exam Definition (2 Marks)

**Zero Point (Point at Infinity):** The zero point of an elliptic curve is a special point denoted by

$$
O
$$

It acts as the **identity element** of the elliptic curve group and satisfies

$$
P+O=P
$$

for every point $$P$$ on the curve. It is also called the **point at infinity**.

---

## Easy Way to Remember

| Ordinary Arithmetic | Elliptic Curve            |
| ------------------- | ------------------------- |
| $$0$$               | $$O$$ (Point at Infinity) |
| $$a+0=a$$           | $$P+O=P$$                 |
| $$a+(-a)=0$$        | $$P+(-P)=O$$              |

**Memory Trick:** Think of the **point at infinity** $$O$$ as the **zero** of elliptic curve arithmetic. It plays exactly the same role that **0** plays in ordinary addition.
