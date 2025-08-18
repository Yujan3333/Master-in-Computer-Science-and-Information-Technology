### 1. Background: Orientation

For three points $a, b, c$,

$$
\text{orientation}(a, b, c) = 
\begin{cases} 
0 & \text{if collinear} \\ 
1 & \text{if clockwise} \\ 
2 & \text{if counterclockwise} 
\end{cases}
$$

So:

* `o1 = orientation(p1, q1, p2)` tells how $p2$ lies relative to the line $p1q1$.
* `o2 = orientation(p1, q1, q2)` tells how $q2$ lies relative to $p1q1$.
* `o3 = orientation(p2, q2, p1)` tells how $p1$ lies relative to $p2q2$.
* `o4 = orientation(p2, q2, q1)` tells how $q1$ lies relative to $p2q2$.

---

### 2. Improper Intersection Condition

Improper intersection means:
👉 Segments only **touch** at endpoints or **overlap in a straight line** (no actual crossing).

The code checks this by:

```python
if o1 == 0 and self.on_segment(p1, q1, p2): return "Improper Intersection"
if o2 == 0 and self.on_segment(p1, q1, q2): return "Improper Intersection"
if o3 == 0 and self.on_segment(p2, q2, p1): return "Improper Intersection"
if o4 == 0 and self.on_segment(p2, q2, q1): return "Improper Intersection"
```

Each condition means:

* `o1 == 0 and on_segment(p1, q1, p2)` → $p2$ is **collinear** with line $p1q1$, and lies **within segment** $p1q1$. (touches/overlaps)
* `o2 == 0 and on_segment(p1, q1, q2)` → $q2$ is collinear with $p1q1$ and lies on it.
* `o3 == 0 and on_segment(p2, q2, p1)` → $p1$ is collinear with $p2q2$ and lies on it.
* `o4 == 0 and on_segment(p2, q2, q1)` → $q1$ is collinear with $p2q2$ and lies on it.

---

### 🔑 In simple words:

**Improper intersection occurs when:**

1. The segments are collinear at least at one endpoint, AND
2. That endpoint lies on the other segment.

This covers:

* Endpoints touching (like "T-junction" or just meeting at a point).
* Overlapping (part of one lies on the other).

---
