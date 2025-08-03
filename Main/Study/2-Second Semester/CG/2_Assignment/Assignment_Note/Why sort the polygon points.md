
## 🧠 **Why Sort Polygon Points?**

When you have a **set of points** (e.g., vertices of a polygon), they might be **given in random order**.

If you draw lines between points in random order, the polygon will be incorrect — it may self-intersect or look wrong.

So, we **sort the points** in a **clockwise or counter-clockwise order** around a center point (like the centroid) to **draw a proper polygon**.

---

## 🧭 **How to Sort Points Clockwise?**

We sort by **angle** each point makes with the **centroid (center of all points)**.

### Step-by-step:

### ✅ 1. **Find the Centroid (Center Point)**

It is the average of all x and y coordinates.

$$
\text{centroid}_x = \frac{x_1 + x_2 + \cdots + x_n}{n}, \quad \text{centroid}_y = \frac{y_1 + y_2 + \cdots + y_n}{n}
$$

### ✅ 2. **Calculate Angle from Centroid**

Use:

$$
\text{angle} = \text{atan2}(y - \text{centroid}_y, x - \text{centroid}_x)
$$

This gives angle of point relative to the horizontal line from centroid.

### ✅ 3. **Sort Based on Angle**

Sort in **descending order** for clockwise
Sort in **ascending order** for counter-clockwise

---

## 🧑‍💻 Code Explanation (from earlier)

```python
import math

def get_centroid(points):
    x = sum(p.x for p in points) / len(points)
    y = sum(p.y for p in points) / len(points)
    return Point(x, y)
```

👉 This function finds the average `x` and `y` — the **centroid**.

---

```python
def sort_points_clockwise(points):
    centroid = get_centroid(points)

    def angle_from_centroid(p):
        return math.atan2(p.y - centroid.y, p.x - centroid.x)

    return sorted(points, key=angle_from_centroid, reverse=True)
```

* `math.atan2(dy, dx)` gives the **angle** of point `p` relative to centroid
* `sorted(..., reverse=True)` → sorts by angle **clockwise**

---

## 🔍 Example:

If you have these points:

```
A(1,2), B(3,5), C(5,3), D(4,1), E(2,0)
```

After sorting clockwise, you might get:

```
C(5,3), B(3,5), A(1,2), E(2,0), D(4,1)
```

This order can be **used to draw** the polygon cleanly.

---

## 🧾 Summary

> "To construct a proper polygon, the vertices must be ordered either clockwise or counter-clockwise. So we compute the centroid of all points and calculate each point’s angle with respect to this centroid using atan2. Then, we sort points by angle — in descending order for clockwise or ascending for counter-clockwise."

---

