### Write a python program to implement Standard Scalar.

- `axis=0` do operation column-wise.
```python
import numpy as np

class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self,data):
        '''Gets the required parameter(mean and SD)'''
        self.mean = np.mean(data, axis=0)
        self.std = np.std(data, axis=0)
    
    def transform(self,data):
        '''Transforms the data (Normalizes)'''
        return np.round((data - self.mean) / self.std, 3)


    # Applying standard scaling
    def fit_transform(self, data):
        '''Combining fit and transfrom'''
        # calling fit
        self.fit(data)

        #Returning the normalized data
        return self.transform(data)


# Sample dataset
data = np.array([[5.9, 75], [5.8, 86], [5.2, 50], [5.4, 55], [6.1, 85], [5.5, 62]])

# Create a StandardScaler object
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

print("Original Data:\n", data)
print("\nStandardized Data:\n", scaled_data)


```

##### Output
![](../../../../../../../Images/First_Sem_Images/Question4%20-%20WAP%20Standard%20Scalar%20OUTPUT.png)

## Tag
#assignment #NN 