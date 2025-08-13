
We’re talking about **ordering vertices counterclockwise (CCW)** so that:

1. The polygon’s vertices are in the correct order.
2. Area formulas, triangulation, or plotting work correctly without weird overlaps.

---

## **Why CCW Ordering Matters**

If the vertices are shuffled (e.g., jumping from one corner to another randomly), plotting or triangulating will produce **crossed lines** and **wrong areas**.

Example:

```
(0,0) → (3,3) → (1,0) → (0,3)
```

will make zig-zag connections unless we sort them properly around the shape.

---

## **The Idea**

We sort the vertices based on their **angle from the centroid**.

1. **Find the centroid**
   The centroid is the “average position” of all points:

   $$
   \bar{x} = \frac{\sum x_i}{n}, \quad \bar{y} = \frac{\sum y_i}{n}
   $$

   This gives a point in the middle of the polygon.

2. **Measure each point’s angle from the centroid**
   We use:

   $$
   \theta = \text{atan2}(y_i - \bar{y},\, x_i - \bar{x})
   $$

   `atan2` gives the polar angle between the line from the centroid to the point and the positive x-axis.

   * In Python, `math.atan2(dy, dx)` returns angles in **radians** from `-π` to `π`.
   * Sorting by this angle naturally gives **counterclockwise** order.

3. **Sort by angle**
   If we sort the vertices using the angle values, we loop around the polygon in CCW order.

---

## **Code Example**

```python
import math

def order_counterclockwise(vertices):
    # Step 1: Find centroid
    cx = sum(v[0] for v in vertices) / len(vertices)
    cy = sum(v[1] for v in vertices) / len(vertices)

    # Step 2: Sort by polar angle from centroid
    return sorted(vertices, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

# Example
points = [(0, 0), (2, 1), (4, 0), (3, 3), (1, 3)]
ccw_points = order_counterclockwise(points)
print(ccw_points)
```

---

## **Visual Intuition**

Imagine standing at the centroid and spinning around.

* Each point has a **direction** (angle) from you.
* We arrange them in the order you’d encounter them as you spin **counterclockwise**.

---
