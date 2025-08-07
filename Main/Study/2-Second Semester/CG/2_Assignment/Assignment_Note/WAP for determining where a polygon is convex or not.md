
### Code
```python
# WAP to check whether the polygon is convex or not
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def cross_product_z(a, b, c):
    """Returns the z-component of the cross product of vectors AB and BC"""
    abx = b.x - a.x
    aby = b.y - a.y
    bcx = c.x - b.x
    bcy = c.y - b.y
    return abx * bcy - aby * bcx

def is_convex(polygon):
    n = len(polygon)
    if n < 3:
        return False  # Not a polygon
    
    prev_cross = 0

    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        c = polygon[(i + 2) % n]

        cross = cross_product_z(a, b, c)
        if cross != 0:
            if prev_cross == 0:
                prev_cross = cross
            elif cross * prev_cross < 0:
                return False  # Turn direction changed → not convex

    return True

def plot_polygon(polygon, is_convex_result):
    x = [p.x for p in polygon] + [polygon[0].x]
    y = [p.y for p in polygon] + [polygon[0].y]

    plt.figure()
    plt.plot(x, y, marker='o')
    for i, p in enumerate(polygon):
        plt.text(p.x + 0.1, p.y + 0.1, f"P{i}")
    
    plt.title("Convex Polygon" if is_convex_result else "Non-Convex Polygon")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

# Example polygon points
# polygon = [
#     Point(0, 0),
#     Point(2, 1),
#     Point(4, 0),
#     Point(3, 3),
#     Point(1, 3)
# ]

# Check the polygon points
polygon = [
    Point(0, 0),
    Point(2, 1),
    Point(3, 3),
    Point(1, 4),
    Point(-1, 2)
]

result = is_convex(polygon)
print("Is the polygon convex?", result)

plot_polygon(polygon, result)

```


#### Output
![](../../../../../../Images/Second_Sem_Images/WAP%20for%20determining%20where%20a%20polygon%20is%20convex%20or%20not-fig.png)


---
### Explanation

[Explanation of Polygon Convex Check Logic](Explanation%20of%20Polygon%20Convex%20Check%20Logic.md)