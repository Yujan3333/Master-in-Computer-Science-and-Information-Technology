- Here according to sir there should be sorting of each point of polygon
	- Something related to slope , clockwise, counter-clockwise.
	- [Why sort the polygon points](Why%20sort%20the%20polygon%20points.md)
```python
# WAP to create Polygon with sorting according to the angle.
   
   import math
   import matplotlib.pyplot as plt
   
   # Define a simple Point class
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
   
   # Function to compute the centroid of the polygon
   def get_centroid(points):
       x = sum(p.x for p in points) / len(points)
       y = sum(p.y for p in points) / len(points)
       return Point(x, y)
   
   # Function to sort points in clockwise order based on angle from centroid
   def sort_points_clockwise(points):
       centroid = get_centroid(points)
   
       # Calculating the angle to the centroid
       def angle_from_centroid(p):
           return math.atan2(p.y - centroid.y, p.x - centroid.x)
       # Passing the sorted list based
       return sorted(points, key=angle_from_centroid, reverse=True)
   
   # Function to display the polygon using matplotlib
   def display_polygon(points):
       # Close the polygon by adding the first point again at the end
       x = [p.x for p in points] + [points[0].x]
       y = [p.y for p in points] + [points[0].y]
       
       plt.figure(figsize=(6, 6))
       plt.plot(x, y, 'bo-')  # 'bo-' means blue circle markers with lines
       for i, p in enumerate(points):
           plt.text(p.x, p.y, f"P{i+1}", fontsize=12, ha='right')
       plt.title("Polygon (Clockwise Sorted Vertices)")
       plt.grid(True)
       plt.axis('equal')  # Equal aspect ratio
       plt.show()
   
   
   # Taking the input from the user
   n = int(input("Enter number of vertices in the polygon: "))
   polygon = []
   
   # Take and divide the points to fit into polygon
   for i in range(n):
       x, y = map(float, input(f"Enter x y for Point {i+1}: ").split())
       polygon.append(Point(x, y))
   
   # Sort and display
   sorted_polygon = sort_points_clockwise(polygon)
   display_polygon(sorted_polygon)
   
   
   
   # 1 1  
   # 4 1  
   # 5 3  
   # 4 5  
   # 2 6  
   # 0 4  
   # 0 2  
   
```

---
### Output
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20create%20Polygon-1.png)
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20create%20Polygon-2-1.png)