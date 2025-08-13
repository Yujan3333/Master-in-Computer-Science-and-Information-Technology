
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20calculate%20area%20of%20polygon%20wrt%20to%20vertex-from%20notes.png)

---

## **Simple Explanation of the Math**

We have a **convex polygon** with vertices:

$$
V_0, V_1, V_2, \dots, V_{n-1}
$$

listed in **counterclockwise order**.

The trick in the diagram is:

1. Pick a **reference vertex** (here $V_0$).
2. Draw lines from $V_0$ to all other non-adjacent vertices (diagonals).
3. This splits the polygon into **triangles**:

   * Triangle $(V_0, V_1, V_2)$
   * Triangle $(V_0, V_2, V_3)$
   * Triangle $(V_0, V_3, V_4)$
   * ... and so on until $(V_0, V_{n-2}, V_{n-1})$
4. **Add up the areas** of all these triangles → that’s the area of the polygon.

---

### **How to find the area of one triangle**

For triangle with vertices $(x_a, y_a), (x_b, y_b), (x_c, y_c)$:

$$
\text{Area} = \frac{1}{2} \left| x_a(y_b - y_c) + x_b(y_c - y_a) + x_c(y_a - y_b) \right|
$$

---

## **Python Implementation**

This follows exactly what’s in the image: sum the areas of triangles formed with $V_0$ and consecutive vertices.

```python
import math

def cross_product(o, a, b):
    """Cross product of OA x OB vectors (O = origin point)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_convex(vertices):
    """Check if polygon is convex."""
    n = len(vertices)
    if n < 3:
        return False
    sign = None
    for i in range(n):
        o = vertices[i]
        a = vertices[(i + 1) % n]
        b = vertices[(i + 2) % n]
        cp = cross_product(o, a, b)
        if cp != 0:
            current_sign = cp > 0
            if sign is None:
                sign = current_sign
            elif sign != current_sign:
                return False
    return True

def order_counterclockwise(vertices):
    """Order vertices counterclockwise based on centroid."""
    cx = sum(v[0] for v in vertices) / len(vertices)
    cy = sum(v[1] for v in vertices) / len(vertices)
    return sorted(vertices, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

def triangle_area(a, b, c):
    """Area of triangle from 3 vertices."""
    return abs(
        a[0] * (b[1] - c[1]) +
        b[0] * (c[1] - a[1]) +
        c[0] * (a[1] - b[1])
    ) / 2

def convex_polygon_area(vertices):
    """Calculate area via triangulation from V0."""
    if not is_convex(vertices):
        raise ValueError("Polygon is not convex.")
    
    vertices = order_counterclockwise(vertices)
    v0 = vertices[0]
    total_area = 0
    for i in range(1, len(vertices) - 1):
        total_area += triangle_area(v0, vertices[i], vertices[i + 1])
    return total_area

# Example polygon
points = [
    (4, 0),
    (5, 3),
    (3, 5),
    (0, 4),
    (0, 0)
]

try:
    area = convex_polygon_area(points)
    print("Polygon is convex.")
    print("Area:", area)
except ValueError as e:
    print(e)

```

---
==[More Explanation of The Above Code of finding the polygon area of convex polygon](More%20Explanation%20of%20The%20Above%20Code%20of%20finding%20the%20polygon%20area%20of%20convex%20polygon.md)==
