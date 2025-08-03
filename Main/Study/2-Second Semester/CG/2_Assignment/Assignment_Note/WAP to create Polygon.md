- Here according to sir there should be sorting of each point of polygon
	- Something related to slope , clockwise, counter-clockwise.
	- [[Why sort the polygon points]]
```python
import matplotlib.pyplot as plt

# Define the Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define the Polygon class
class Polygon:
    def __init__(self, points):
        # Takes a list of points
        self.points = points

    # Display the points in polygon
    def display(self):
        print("\nPolygon coordinates:")
        for i, point in enumerate(self.points):
            print(f"Point {i+1}: ({point.x}, {point.y})")

    def plot(self):
        # Extracting x and y points from points
        x_coords = [p.x for p in self.points]
        y_coords = [p.y for p in self.points]

        # Close the polygon
        # Connects the last point to the first point of the polygon
        if self.points:
            x_coords.append(self.points[0].x)
            y_coords.append(self.points[0].y)


        # Sets the size of the plot
        plt.figure(figsize=(6, 6))

        # green lines with circle markers
        plt.plot(x_coords, y_coords, 'g-o')

        # Adds labels to each point so you can see their coordinates next to them on the plot.
        for p in self.points:
            plt.text(p.x + 0.1, p.y, f'({p.x}, {p.y})', fontsize=9)


        plt.grid(True)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Polygon Plot")
        plt.axis('equal')
        plt.show()

# Polygon with n-points
n = int(input("Enter the number of points in the polygon: "))

if n > 0:
    # list of points
    points = []
    for i in range(n):
        x = float(input(f"Enter x-coordinate of point {i+1}: "))
        y = float(input(f"Enter y-coordinate of point {i+1}: "))
        # Appends the inputted points to the point list
        points.append(Point(x, y))

    polygon = Polygon(points)
    polygon.display()
    polygon.plot()
else:
    print("A polygon must have at least 1 point.")


# Point 1: (0, 1)
# Point 2: (0.95, 0.31)
# Point 3: (0.59, -0.81)
# Point 4: (-0.59, -0.81)
# Point 5: (-0.95, 0.31)
```

---
### Output
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20create%20Polygon-output.png)
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20create%20Polygon-output-1.png)
