![](../../../../../../Images/Second_Sem_Images/WAP%20to%20calculate%20area%20of%20polygon%20wrt%20to%20arbitrary%20point-1.png)
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20calculate%20area%20of%20polygon%20wrt%20to%20arbitrary%20point-2.png)
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20calculate%20area%20of%20polygon%20wrt%20to%20arbitrary%20point-3.png)

**MEANING**
- Here from the *arbitrary point* triangles are created to each point of polygon and area is added up. Due to the opposite direction some triangle cancel each other out and we get the desired triangle area.
---

### Simplified Code
```python
def triangle_area_from_point(p, a, b):
    # Signed area of triangle formed by points p, a, b
    return 0.5 * ((a[0] - p[0])*(b[1] - p[1]) - (a[1] - p[1])*(b[0] - p[0]))

def polygon_area_from_arbitrary_point(polygon, p):
    n = len(polygon)
    area = 0
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        area += triangle_area_from_point(p, a, b)
    return abs(area)

# Example:
polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]  # Rectangle
arbitrary_point = (1, 1)

area = polygon_area_from_arbitrary_point(polygon, arbitrary_point)
print("Area of polygon w.r.t arbitrary point:", area)

```

### Code With figure
```python
import matplotlib.pyplot as plt

def triangle_area_from_point(p, a, b):
    # Signed area of triangle formed by points p, a, b
    return 0.5 * ((a[0] - p[0])*(b[1] - p[1]) - (a[1] - p[1])*(b[0] - p[0]))

def polygon_area_from_arbitrary_point(polygon, p):
    n = len(polygon)
    area = 0
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        area += triangle_area_from_point(p, a, b)
    return abs(area)

def plot_polygon_and_triangles(polygon, point):
    # Close the polygon for plotting
    polygon_closed = polygon + [polygon[0]]
    xs, ys = zip(*polygon_closed)

    plt.figure(figsize=(8,8))
    plt.fill(xs, ys, 'lightblue', alpha=0.5, edgecolor='blue', linewidth=2)
    plt.plot(xs, ys, 'o-', color='blue', label='Polygon')

    # Plot the arbitrary point p
    plt.plot(point[0], point[1], 'ro', label='Arbitrary Point p')
    plt.text(point[0], point[1], '  p', fontsize=12, color='red')

    # Label polygon vertices
    for i, (x, y) in enumerate(polygon):
        plt.text(x, y, f'  P{i}', fontsize=12, color='navy')

    # Draw triangles from p to each polygon edge
    n = len(polygon)
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        triangle_xs = [point[0], a[0], b[0], point[0]]
        triangle_ys = [point[1], a[1], b[1], point[1]]
        plt.fill(triangle_xs, triangle_ys, alpha=0.3, edgecolor='none', color='orange')

    plt.title("Polygon, Arbitrary Point, and Triangles")
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example polygon with 5 points (pentagon)
polygon = [(1, 1), (4, 2), (5, 5), (3, 6), (0, 4)]
# Arbitrary point outside polygon
arbitrary_point = (6, 1)

area = polygon_area_from_arbitrary_point(polygon, arbitrary_point)
print("Area of polygon w.r.t arbitrary point:", area)

plot_polygon_and_triangles(polygon, arbitrary_point)

```
#### Output
Area of polygon w.r.t arbitrary point: 15.5
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20calculate%20area%20of%20polygon%20wrt%20to%20arbitrary%20point-2-1.png)

---
#### [Explanation of code of arbitrary point polygon](Explanation%20of%20code%20of%20arbitrary%20point%20polygon.md)
