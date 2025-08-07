
### Code
```python
import matplotlib.pyplot as plt

# Defining the main line segment points
P0 = (1, 1)
P1 = (6, 4)

# Defining 7 test points for each position
test_points = {
    'Origin': P0,
    'Terminus': P1,
    'Between': (3, 2.4),            
    'Behind': (-1, -0.2),           
    'Beyond': (8, 5.2),             
    'Left': (4, 5),                 
    'Right': (4, 1),                
}

# Classification function
def classify_point(P0, P1, P):
    x0, y0 = P0
    x1, y1 = P1
    x, y = P

    dx = x1 - x0
    dy = y1 - y0
    dxp = x - x0
    dyp = y - y0

    cross = dx * dyp - dy * dxp

    if cross > 0:
        return "Left"
    elif cross < 0:
        return "Right"
    else:
        dot = dx * dxp + dy * dyp
        len_sq = dx**2 + dy**2
        if P == P0:
            return "Origin"
        elif P == P1:
            return "Terminus"
        elif dot < 0:
            return "Behind"
        elif dot > len_sq:
            return "Beyond"
        else:
            return "Between"

# Plot setup
plt.figure(figsize=(8, 8))
plt.title("Point Classification ")
plt.grid(True)

# Drawing main line
plt.plot([P0[0], P1[0]], [P0[1], P1[1]], 'k-', linewidth=2, label="Line Segment")

# Drawing dotted line behind
dx = P1[0] - P0[0]
dy = P1[1] - P0[1]
plt.plot([P0[0] - dx, P0[0]], [P0[1] - dy, P0[1]], 'k--', label="Behind")

# Drawing dotted line beyond
plt.plot([P1[0], P1[0] + dx], [P1[1], P1[1] + dy], 'k--', label="Beyond")

# Ploting each test point and labeling it
colors = {
    "Origin": "green",
    "Terminus": "red",
    "Between": "blue",
    "Behind": "purple",
    "Beyond": "orange",
    "Left": "cyan",
    "Right": "magenta"
}

# Looping through all the test points
for label, point in test_points.items():
    x, y = point
    classification = classify_point(P0, P1, point)
    plt.plot(x, y, 'o', color=colors[label], label=f"{label} ({classification})")
    plt.text(x + 0.2, y + 0.2, f"{label}", fontsize=9, color=colors[label])

# Making aspect ratio equal
plt.gca().set_aspect('equal')
plt.legend()
plt.show()

```


#### Output
![](../../../../../../Images/Second_Sem_Images/WAP%20for%20implementing%20point%20line%20classification-fig.png)


---

### Explanation

[Explanation of Math behind the Code of Line Segment](Explanation%20of%20Math%20behind%20the%20Code%20of%20Line%20Segment.md)
[Explanation of cross and dot product](Explanation%20of%20cross%20and%20dot%20product.md)