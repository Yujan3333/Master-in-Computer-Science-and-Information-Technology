```python
import numpy as np
import cv2
import matplotlib.pyplot as plt

# ---------------- POINT CLASS -----------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, radius=2, color=(0,0,255)):
        global canvas
        cv2.circle(canvas, (int(self.x), int(self.y)), radius, color, -1)

# ---------------- LINE SEGMENT CLASS -----------------
class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def render(self, color=(255,0,0)):
        global canvas
        cv2.line(canvas, (int(self.p1.x), int(self.p1.y)),
                 (int(self.p2.x), int(self.p2.y)), color, 1)

    # orientation test
    def orientation(self, a, b, c):
        val = (b.y - a.y)*(c.x - b.x) - (b.x - a.x)*(c.y - b.y)
        if val == 0: return 0  # collinear
        return 1 if val > 0 else 2  # 1=clockwise, 2=counterclockwise

    # check if point lies on segment
    def on_segment(self, a, b, c):
        return (min(a.x, b.x) <= c.x <= max(a.x, b.x)) and \
               (min(a.y, b.y) <= c.y <= max(a.y, b.y))

    # intersection type
    def intersects(self, other):
        p1, q1 = self.p1, self.p2
        p2, q2 = other.p1, other.p2

        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # First check for improper intersection (touching/overlapping)
        if o1 == 0 and self.on_segment(p1, q1, p2): return "Improper Intersection"
        if o2 == 0 and self.on_segment(p1, q1, q2): return "Improper Intersection"
        if o3 == 0 and self.on_segment(p2, q2, p1): return "Improper Intersection"
        if o4 == 0 and self.on_segment(p2, q2, q1): return "Improper Intersection"

        # Then check proper intersection (crossing)
        if o1 != o2 and o3 != o4:
            return "Proper Intersection"

        return "No Intersection"


# ---------------- POLYGON CLASS -----------------
class Polygon:
    def __init__(self, points):
        self.points = points

    def render(self, color=(0,255,0)):
        global canvas
        pts = np.array([[p.x,p.y] for p in self.points], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(canvas,[pts],True,color,1)

    # Convex polygon inclusion (using cross product direction consistency)
    def point_inclusion_convex(self, point):
        n = len(self.points)       # number of vertices in polygon
        prev = None                # stores "side" information
        for i in range(n):
            a, b = self.points[i], self.points[(i+1)%n] # take each edge (a → b)
            # cross product of (b-a) × (point-a)
            cross = (b.x-a.x)*(point.y-a.y) - (b.y-a.y)*(point.x-a.x)
            if cross != 0:                           # only consider if point is not collinear with edge
                   if prev is None:                  # first non-collinear edge
                       prev = cross > 0              # store True if point is on left side, False if on right
                   elif (cross > 0) != prev:         # if side is different from previous side
                       return False                  # => point is outside
               
        return True

    # Ray casting algorithm
    def point_inclusion_raycast(self, point):
        n = len(self.points)   # number of polygon vertices
        count = 0    # crossing counter
        
        # Loop through all polygon edges
        for i in range(n):
            a, b = self.points[i], self.points[(i+1)%n] # edge from vertex a to vertex b
            # Step 1: Check if the horizontal ray at y=point.y crosses the edge (a → b)
			# This happens if the y-coordinate of 'point' lies between a.y and b.y
            if ((a.y > point.y) != (b.y > point.y)):
            
	            # Step 2: Find x-coordinate where edge (a → b) intersects horizontal line y=point.y
                x_int = a.x + (point.y-a.y)*(b.x-a.x)/(b.y-a.y)

				# Step 3: Count this crossing only if it happens to the RIGHT of the point
                if x_int > point.x:
                    count += 1
        
        # Step 4: Apply even-odd rule:
		# - If number of crossings is odd → point is inside
        # - If number of crossings is even → point is outside            
        return count % 2 == 1
```
---

```python
# reset canvas
screen_x, screen_y = 500, 500
canvas = np.zeros((screen_x, screen_y, 3), dtype=np.uint8)

# Proper intersection
line1 = LineSegment(Point(50,50), Point(200,200))
line2 = LineSegment(Point(50,200), Point(200,50))
line1.render(color=(255, 0, 0))   # red
line2.render(color=(0, 255, 0))   # green
print("line1 and line2 intersection type:", line1.intersects(line2))

# Improper intersection (collinear + endpoint overlap)
line3 = LineSegment(Point(250,100), Point(400,100))
line4 = LineSegment(Point(350,100), Point(450,100))
line1.render(color=(0, 0, 255))   # blue
line2.render(color=(255, 255, 0)) # yellow
print("line3 and line4 intersection type:", line3.intersects(line4))



# ---------------- CONVEX POLYGON (TURN TEST) ----------------
convex_poly = Polygon([Point(50,300), Point(50,400), Point(150,400), Point(150,300)])
convex_poly.render(color=(0,255,255))

# Point inside
pt_inside_convex = Point(100,350)
pt_inside_convex.render(radius=5, color=(0,255,0))
print("Convex polygon (turn test) point inclusion (inside):",
      convex_poly.point_inclusion_convex(pt_inside_convex))

# Point outside
pt_outside_convex = Point(200,350)
pt_outside_convex.render(radius=5, color=(0,0,255))
print("Convex polygon (turn test) point inclusion (outside):",
      convex_poly.point_inclusion_convex(pt_outside_convex))


# ---------------- GENERAL POLYGON (RAY CAST) ----------------
general_poly = Polygon([Point(300,300), Point(350,450), Point(450,400), Point(400,300)])
general_poly.render(color=(255,255,0))

# Point inside
pt_inside_ray = Point(370,370)
pt_inside_ray.render(radius=5, color=(0,255,0))
print("Ray cast polygon (inside point):",
      general_poly.point_inclusion_raycast(pt_inside_ray))

# Point outside
pt_outside_ray = Point(470,470)
pt_outside_ray.render(radius=5, color=(0,0,255))
print("Ray cast polygon (outside point):",
      general_poly.point_inclusion_raycast(pt_outside_ray))


# ---------------- SHOW RESULT ----------------
plt.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
```

---
#### Output
![](../../../../../../Images/Second_Sem_Images/CG%20-%20Lab%204-fig.png)

---
## Explanation
- [Improper Intersection Explanation of Lab4 - CG](Improper%20Intersection%20Explanation%20of%20Lab4%20-%20CG.md)


