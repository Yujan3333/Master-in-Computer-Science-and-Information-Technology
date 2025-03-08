### Write a python program to train perceptron using given training set and predict class for the input (6,82) and (5.3,52) 
![](../../../../../Images/Lab1%20-%20Table.png)

---
#### Code
==Problems==
- Divide by Zero Error in MinMax Scalar when the Min and Max was same.
- Error in Normalizing the incorrect prediction.
	- **Cause:** Using different scaler for training and testing data because the *min and max* was not saved.
```python
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=1, epochs=5):
        self.weights = np.zeros(input_size)  # Initialize weights to zeros
        self.bias = 0                        # Initialize bias to 0
        self.alpha = learning_rate           # Learning rate
        self.epochs = epochs                 # Number of epochs
        self.X_min = None
        self.X_max = None

    def activation_func(self, x):
        """Activation function: Returns 1 for positive, -1 for negative"""
        return 1 if x >= 0 else -1

    def maxmin_normalize(self, X):
        """Normalizing the data between 0 and 1 using Min-Max Scaling with zero-division handling"""
        
        if self.X_min is None or self.X_max is None:
            self.X_min = np.min(X, axis=0)
            self.X_max = np.max(X, axis=0)
        
        # PROBLEM: Division by zero if max and min same
        denominator = self.X_max - self.X_min

        #SOLUTION: Replacing the 0 with 1 to avoid division by zero
        denominator[denominator == 0] = 1  
        
        return np.round((X - self.X_min) / denominator, 3)

    def train(self, X, y):
        """Trains the perceptron using given inputs and target values"""
        # Normalize data before training
        X = self.maxmin_normalize(X)  

        for epoch in range(self.epochs):
            print(f"Epoch {epoch+1}:")
            for i in range(len(X)):
                # Weighted sum
                v = np.dot(X[i], self.weights) + self.bias  

                # Apply activation function
                y_pred = self.activation_func(v)  
                
                # Update weights and bias only if there's a misclassification
                if y_pred != y[i]:
                    weight_update = self.alpha * (y[i] - y_pred) * X[i]
                    bias_update = self.alpha * (y[i] - y_pred)
                    self.weights += weight_update
                    self.bias += bias_update
                print(f"  Sample {i+1}: Weights = {self.weights}, Bias = {self.bias}")

    def predict(self, X):
        """Predicts the class for given input"""
        # PROBLEM: Due to not saving the min and max value of training data scaling problem occured and correct prediction was not made 
        # SOLUTION: Normalize test data using the same scaling as training data
        X = self.maxmin_normalize(X)  
        v = np.dot(X, self.weights) + self.bias
        return "Male" if self.activation_func(v) == 1 else "Female"


# Question Dataset
training_data = np.array([ 
    [5.9, 75], [5.8, 86], [5.2, 50], 
    [5.4, 55], [6.1, 85], [5.5, 62]
])
target_outputs = np.array([1, 1, -1, -1, 1, -1])  # 1 = Male, -1 = Female

# Create and train perceptron
perceptron = Perceptron(input_size=2, learning_rate=1, epochs=5)
perceptron.train(training_data, target_outputs)

# Testing on new inputs
test_data = np.array([[6, 82], [5.3, 52]])

for i, test in enumerate(test_data):
    # Passing to the Perceptron Obj to predict their Gender
    prediction = perceptron.predict(np.array([test]))  
    print(f"Test case {i+1}: {test} → Predicted class: {prediction}")

```
##### Output
```md
Epoch 1:
  Sample 1: Weights = [0. 0.], Bias = 0
  Sample 2: Weights = [0. 0.], Bias = 0
  Sample 3: Weights = [0. 0.], Bias = -2
  Sample 4: Weights = [0. 0.], Bias = -2
  Sample 5: Weights = [2.    1.944], Bias = 0
  Sample 6: Weights = [1.334 1.278], Bias = -2
Epoch 2:
  Sample 1: Weights = [2.89  2.666], Bias = 0
  Sample 2: Weights = [2.89  2.666], Bias = 0
  Sample 3: Weights = [2.89  2.666], Bias = -2
  Sample 4: Weights = [2.89  2.666], Bias = -2
  Sample 5: Weights = [2.89  2.666], Bias = -2
  Sample 6: Weights = [2.89  2.666], Bias = -2
Epoch 3:
  Sample 1: Weights = [2.89  2.666], Bias = -2
  Sample 2: Weights = [2.89  2.666], Bias = -2
  Sample 3: Weights = [2.89  2.666], Bias = -2
  Sample 4: Weights = [2.89  2.666], Bias = -2
  Sample 5: Weights = [2.89  2.666], Bias = -2
  Sample 6: Weights = [2.89  2.666], Bias = -2
Epoch 4:
  Sample 1: Weights = [2.89  2.666], Bias = -2
  Sample 2: Weights = [2.89  2.666], Bias = -2
  Sample 3: Weights = [2.89  2.666], Bias = -2
  Sample 4: Weights = [2.89  2.666], Bias = -2
  Sample 5: Weights = [2.89  2.666], Bias = -2
  Sample 6: Weights = [2.89  2.666], Bias = -2
Epoch 5:
  Sample 1: Weights = [2.89  2.666], Bias = -2
  Sample 2: Weights = [2.89  2.666], Bias = -2
  Sample 3: Weights = [2.89  2.666], Bias = -2
  Sample 4: Weights = [2.89  2.666], Bias = -2
  Sample 5: Weights = [2.89  2.666], Bias = -2
  Sample 6: Weights = [2.89  2.666], Bias = -2
Test case 1: [ 6. 82.] → Predicted class: Male
Test case 2: [ 5.3 52. ] → Predicted class: Female
```