Line: - Line is represented by a pair of points P0 and P1 say, which is extended in both
way to infinity along the segment represented by the pair of points P0 & P1

```python
import matplotlib.pyplot as plt

# Define a Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define a Line class
class Line:
    def __init__(self, P0: Point, P1: Point):
        self.P0 = P0
        self.P1 = P1

    def draw(self, length=10):
        # Calculate direction vector from P0 to P1
        dx = self.P1.x - self.P0.x
        dy = self.P1.y - self.P0.y

        # Normalize the direction vector
        mag = (dx**2 + dy**2) ** 0.5
        dx /= mag
        dy /= mag

        # Calculate two far points along the line in both directions
        x_start = self.P0.x - dx * length
        y_start = self.P0.y - dy * length
        x_end = self.P0.x + dx * length
        y_end = self.P0.y + dy * length

        # Draw the infinite line (dashed green)
        plt.plot([x_start, x_end], [y_start, y_end], 'g--', label='Infinite Line')

        # Draw the segment between P0 and P1 (solid blue)
        plt.plot([self.P0.x, self.P1.x], [self.P0.y, self.P1.y], 'b-', linewidth=3, label='Segment P0P1')

        # Draw points P0 and P1
        plt.plot(self.P0.x, self.P0.y, 'ro', label='P0')
        plt.plot(self.P1.x, self.P1.y, 'mo', label='P1')

        plt.title("Line through points P0 and P1 (Infinite extension)")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid(True)
        plt.gca().set_aspect('equal')
        plt.show()

# Example usage:
P0 = Point(1, 2)
P1 = Point(5, 6)

line = Line(P0, P1)
line.draw(length=15)

```

#### Output
![](../../../../../../Images/Second_Sem_Images/WAP%20for%20implementing%20Line.png)

---
## Explanation

### 1. **Line defined by two points**

* A line in 2D can be uniquely determined by **two distinct points** $P_0 = (x_0, y_0)$ and $P_1 = (x_1, y_1)$.
* The line passes through both points and extends infinitely in both directions beyond them.

---

### 2. **Direction vector**

* From the two points, we create a **direction vector**:

  $$
  \vec{d} = (dx, dy) = (x_1 - x_0, y_1 - y_0)
  $$
* This vector points from $P_0$ to $P_1$.

---

### 3. **Normalization of the direction vector**

* To easily work with the direction vector, we normalize it to a **unit vector** $\vec{u}$:

  $$
  \vec{u} = \frac{\vec{d}}{\|\vec{d}\|} = \left(\frac{dx}{\sqrt{dx^2 + dy^2}}, \frac{dy}{\sqrt{dx^2 + dy^2}}\right)
  $$
* Here, $\|\vec{d}\|$ is the length (magnitude) of the vector $\vec{d}$, calculated by the Pythagorean theorem.

---

### 4. **Extending the line infinitely**

* Since a line is infinite, to visualize it, we pick a large value $L$ (like 10 or 15) and extend in both directions from $P_0$:

  * **Start point of the extended line:**

    $$
    P_{start} = P_0 - L \times \vec{u} = (x_0 - L \times u_x, \; y_0 - L \times u_y)
    $$
  * **End point of the extended line:**

    $$
    P_{end} = P_0 + L \times \vec{u} = (x_0 + L \times u_x, \; y_0 + L \times u_y)
    $$
* This simulates the infinite line passing through $P_0$ and $P_1$.

---

### 5. **Drawing the segment and infinite line**

* The **segment** between $P_0$ and $P_1$ is the finite part:

  * Just connect $P_0$ and $P_1$ directly.
* The **infinite line** is drawn between $P_{start}$ and $P_{end}$ as a dashed line to represent infinite extension beyond the segment.

---

### **Summary:**

| Step                       | Math                     | Purpose                            |
| -------------------------- | ------------------------ | ---------------------------------- |
| Direction vector $\vec{d}$ | $(x_1 - x_0, y_1 - y_0)$ | Points from $P_0$ to $P_1$         |
| Length $\|\vec{d}\|$       | $\sqrt{dx^2 + dy^2}$     | To normalize vector to unit length |
| Unit vector $\vec{u}$      | $\vec{d} / \|\vec{d}\|$  | Direction with length 1            |
| Extended start point       | $P_0 - L \times \vec{u}$ | Extends line backwards from $P_0$  |
| Extended end point         | $P_0 + L \times \vec{u}$ | Extends line forwards from $P_0$   |
