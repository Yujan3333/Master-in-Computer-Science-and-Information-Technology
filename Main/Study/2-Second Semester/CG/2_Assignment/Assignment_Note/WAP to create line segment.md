```python
import math
import matplotlib.pyplot as plt

# Define a Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define a LineSegment class using two points
class LineSegment:
    def __init__(self, p1, p2):
        self.start = p1
        self.end = p2

    def display(self):
        print(f"Line segment from ({self.start.x}, {self.start.y}) to ({self.end.x}, {self.end.y})")

    def length(self):
        return math.sqrt((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)

    def plot(self):
        x_values = [self.start.x, self.end.x]
        y_values = [self.start.y, self.end.y]
        plt.plot(x_values, y_values, marker='o', color='blue', label='Line Segment')
        plt.text(self.start.x, self.start.y, f'({self.start.x}, {self.start.y})', fontsize=9, ha='right')
        plt.text(self.end.x, self.end.y, f'({self.end.x}, {self.end.y})', fontsize=9, ha='left')
        plt.title('Visual Representation of Line Segment')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.legend()
        plt.axis('equal')  # Keep scale equal for x and y
        plt.show()

# Create two points
point1 = Point(1, 2)
point2 = Point(4, 6)

# Create a line segment using the two points
line = LineSegment(point1, point2)

# Display the line segment
line.display()

# Print the length of the line segment
print(f"Length of line segment: {line.length():.2f}")

# Plot the line segment
line.plot()
```

---
