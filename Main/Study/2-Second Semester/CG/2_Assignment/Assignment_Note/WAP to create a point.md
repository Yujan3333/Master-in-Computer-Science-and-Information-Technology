
```python
import matplotlib.pyplot as plt
   
   # Defining Point
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
   
       def display(self):
           print(f"Point coordinates: ({self.x}, {self.y})")
   
   # Create and display the point
   p1 = Point(3.5, 4.5)
   p1.display()
   
   # 🔽 Plot the point
   plt.figure(figsize=(5, 5))
   plt.plot(p1.x, p1.y, 'ro')  # 'ro' = red circle marker
   plt.text(p1.x + 0.1, p1.y, f'({p1.x}, {p1.y})')  # label the point
   plt.grid(True)
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.title('Plot of a Point')
   plt.xlim(p1.x - 2, p1.x + 2)
   plt.ylim(p1.y - 2, p1.y + 2)
   plt.show()
```

---
### Output
![](../../../../../../Images/Second_Sem_Images/WAP%20to%20create%20a%20point.png)