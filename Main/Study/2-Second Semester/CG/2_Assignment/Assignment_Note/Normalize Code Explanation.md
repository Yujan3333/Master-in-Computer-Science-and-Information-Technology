
### 🧠 What this does:

This is the **constructor** of the `Ray` class. It runs **automatically** when you create a new `Ray`.

Let’s break it down:

---

### 1. **`self.origin = origin`**

* Saves the starting point (origin) of the ray.
* Example: if `origin = Point(2, 3)`, then the ray starts at (2, 3).

---

### 2. **Direction calculation**

```python
dx = direction.x - origin.x
dy = direction.y - origin.y
```

* These lines calculate how far the direction point is from the origin in both x and y.
* It gives you a **vector** pointing from `origin` to `direction`.

---

### 3. **Normalize the direction (unit vector)**

```python
length = math.hypot(dx, dy)
```

* Calculates the **length of the direction vector** using the Pythagorean theorem:

  $$
  \text{length} = \sqrt{dx^2 + dy^2}
  $$
* `math.hypot(dx, dy)` is a shortcut for this.

---

### 4. **Convert to unit vector**

```python
self.direction = Point(dx / length, dy / length)
```

* Divides both `dx` and `dy` by the length so the vector becomes a **unit vector** (length = 1).
* This means the direction is the same, but the size is fixed to 1.
* This makes it easier to find points at any distance along the ray.

---

### 📌 Why normalize the direction?

Imagine the ray is a flashlight beam. You only care which **way it's pointing**, not how far the direction point was. A **unit vector** is like saying:

> "The ray goes this direction, one step at a time."

---

### 🧾 Example:

```python
origin = Point(2, 3)
direction_point = Point(5, 7)
```

Then:

* `dx = 3` (`5 - 2`)
* `dy = 4` (`7 - 3`)
* `length = 5` (because $\sqrt{3^2 + 4^2} = 5$)
* Unit vector: `(3/5, 4/5) = (0.6, 0.8)`

So the ray moves like:

* 1 unit along the ray = 0.6 units in x and 0.8 units in y.
* **Here this is treated like angle in which the RAY moves**
