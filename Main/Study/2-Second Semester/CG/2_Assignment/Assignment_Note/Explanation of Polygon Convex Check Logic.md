### 🧠 **Basic Idea (in simple terms):**

A **polygon is convex** if:

* All its interior angles are **less than 180°**, and
* As you go around the polygon, it **always turns in the same direction** (either always left or always right at each corner).

---

### 🧮 **Mathematical Approach (using cross product):**

Imagine you are walking along the edges of the polygon. At each corner (vertex), you make a turn.

To check if all turns are the **same direction**, we use the **cross product** of vectors between consecutive edges.

---

### 👉 What’s a vector in this context?

If you have 3 points `A`, `B`, and `C`, then:

* **Vector AB** = B - A
* **Vector BC** = C - B

Then the **cross product of AB and BC** tells us the direction of the turn:

* If cross product is **positive**, it’s a **left turn**.
* If cross product is **negative**, it’s a **right turn**.
* If cross product is **zero**, the points are **collinear** (no turn).

---

### ✅ Convex polygon rule:

If **all cross products have the same sign** (either all positive or all negative), the polygon is **convex**.

If signs **change**, it’s **not convex**.

---

### 📐 Cross Product Formula in 2D:

Let:

$$
\vec{AB} = (x_2 - x_1, y_2 - y_1)
$$

$$
\vec{BC} = (x_3 - x_2, y_3 - y_2)
$$

Then the **cross product** of AB × BC is:

$$
(x_2 - x_1)(y_3 - y_2) - (y_2 - y_1)(x_3 - x_2)
$$

---

### 🧪 Example:

If you walk around the polygon and all turns are **left** (positive cross product), then it’s convex.
