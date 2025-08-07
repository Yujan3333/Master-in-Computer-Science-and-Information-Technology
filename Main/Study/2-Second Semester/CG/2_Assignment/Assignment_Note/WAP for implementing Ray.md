### ✅ Concept of a Ray:
- A ray starts from a point and extends infinitely in one direction.

- In computational geometry, rays are often used in algorithms like ray casting (e.g. to determine if a point is inside a polygon).

```python
import math
import matplotlib.pyplot as plt

# Defining a Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Defining a Ray class
class Ray:
    def __init__(self, origin: Point, direction: Point):
        self.origin = origin
        # Normalize direction to unit vector
        dx = direction.x - origin.x
        dy = direction.y - origin.y
        length = math.hypot(dx, dy)
        self.direction = Point(dx / length, dy / length)

    def point_at_distance(self, d):
        """Returns a point at distance d from the origin along the ray"""
        return Point(self.origin.x + d * self.direction.x,
                     self.origin.y + d * self.direction.y)

    def draw(self, length=100):
        """Visualize the ray using matplotlib"""
        end_point = self.point_at_distance(length)
        plt.plot([self.origin.x, end_point.x], [self.origin.y, end_point.y], 'r--', label='Ray')
        plt.plot(self.origin.x, self.origin.y, 'bo', label='Origin')  # origin
        plt.title("Ray Visualization")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.show()


# Define origin and direction point
origin = Point(2, 3)
direction_point = Point(5, 7)

# Create a Ray object
ray = Ray(origin, direction_point)

# Print ray information
print("Ray origin:", origin.x, origin.y)
print("Ray direction unit vector:", ray.direction.x, ray.direction.y)

# Find a point 10 units along the ray
point = ray.point_at_distance(10)
print("Point 10 units along the ray:", point.x, point.y)

# Draw the ray (length = 10 units)
ray.draw(length=10)

```

#### Output
![](../../../../../../Images/Second_Sem_Images/WAP%20for%20implementing%20Ray-fig.png)


## Explanation
### 🔧 Code:

```python
def __init__(self, origin: Point, direction: Point):
    self.origin = origin
    # Normalize direction to unit vector
    dx = direction.x - origin.x
    dy = direction.y - origin.y
    length = math.hypot(dx, dy)
    self.direction = Point(dx / length, dy / length)
```

[Normalize Code Explanation](Normalize%20Code%20Explanation.md)

- Distance vector shows the direction of the ray.

---
