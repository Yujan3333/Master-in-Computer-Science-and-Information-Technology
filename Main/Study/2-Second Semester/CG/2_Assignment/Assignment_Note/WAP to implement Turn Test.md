```python
# WAP to create a turn test
    
    import matplotlib.pyplot as plt
    
    # Define a Point class
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    # Turn test function
    def turn_test(A, B, C):
        # This is crossproduct of A->B->C 
        # Determinant (B-A) and (C-A)
        val = (B.x - A.x)*(C.y - A.y) - (B.y - A.y)*(C.x - A.x)
    
        if val > 0:
            return "Left Turn"
        elif val < 0:
            return "Right Turn"
        else:
            return "Collinear"
    
    # Plot function
    def plot_points(A, B, C, result):
        x = [A.x, B.x, C.x]
        y = [A.y, B.y, C.y]
    
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, 'bo-', label='Path: A → B → C')  # blue circle with lines
        plt.plot([C.x, A.x], [C.y, A.y], 'r--', alpha=0.3)  # closing the triangle lightly
    
        # Label points
        plt.text(A.x + 0.1, A.y, 'A', fontsize=12, color='blue')
        plt.text(B.x + 0.1, B.y, 'B', fontsize=12, color='blue')
        plt.text(C.x + 0.1, C.y, 'C', fontsize=12, color='blue')
    
        plt.grid(True)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title(f"Turn Test Result: {result}")
        plt.axis('equal')
        plt.legend()
        plt.show()
    
    # Input
    x1, y1 = map(float, input("Enter coordinates of Point A (x y): ").split())
    x2, y2 = map(float, input("Enter coordinates of Point B (x y): ").split())
    x3, y3 = map(float, input("Enter coordinates of Point C (x y): ").split())
    
    # Create Point instances
    A = Point(x1, y1)
    B = Point(x2, y2)
    C = Point(x3, y3)
    
    # Run turn test and display
    result = turn_test(A, B, C)
    print("Turn Test Result:", result)
    
    # Plot the points and result
    plot_points(A, B, C, result)
    

```

--- 
### Output
![WAP to implement Turn Test-1-1.png](WAP%20to%20implement%20Turn%20Test-1-1.png)
![WAP to implement Turn Test-2.png](WAP%20to%20implement%20Turn%20Test-2.png)