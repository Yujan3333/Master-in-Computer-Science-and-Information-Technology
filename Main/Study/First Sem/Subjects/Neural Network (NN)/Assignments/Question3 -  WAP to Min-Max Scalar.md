### Write a python program to implement Min-Max Scalar.

- `self.min = np.min(data, axis=0)` represents column; this argument specifies that the minimum value should be calculated along the first axis (axis 0). In a 2D array, axis 0 represents the rows. So, it will find the minimum value in each *column*
#### Code
```python
import numpy as np

class MinMaxScaler:
    def __init__(self):
        self.min = None
        self.max = None
    
    def fit(self,data):
        '''Getting the required parameters(min,max)'''
        # axis=0:find the minimum value in each column.
        self.min = np.min(data, axis=0)
        self.max = np.max(data, axis=0)

    # Transform data in range(0,1)
    def transform(self,data):
        '''Normalizing the data in range 0 to 1'''
        # Output Data array
        output = np.round((data - self.min) / (self.max - self.min),3)
        return output

    def fit_transform(self, data):
        '''Combining the fit and transform'''
        self.fit(data)
        return self.transform(data)
        

# Sample dataset
data = np.array([[5.9, 75],[5.8, 86],[5.2, 50],[5.4, 55],[6.1, 85],[5.5, 62]])

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

print("Original Data:\n", data)
print("\nScaled Data:\n", scaled_data)


```
##### Output
![](../../../../../Images/Question3%20-%20%20WAP%20to%20Min-Max%20Scalar%20Output.png)

## Tag
#NN