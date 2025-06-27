#### AND Gate

| Input 1 (x₁) | Input 2 (x₂) | Output (y) |
| ------------ | ------------ | ---------- |
| 0            | 0            | 0          |
| 0            | 1            | 0          |
| 1            | 0            | 0          |
| 1            | 1            | 1          |

---
![](../../../../../../../Images/First_Sem_Images/AND%20Gate%20Neural%20Network.png)

---
**Step Activation Function**
![](../../../../../../../Images/First_Sem_Images/AND%20Activation%20Function.png)

$$\phi(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{otherwise} \end{cases}$$

---
#### Code
```python
import numpy as np

EPOCHS = 10
LEARNING_RATE = 1

# Step function (Activation function)
def step_function(value):

    # Threshold at 0
    return 1 if value >= 0 else 0  

class Perceptron:
    
    def __init__(self, input_size, learning_rate=1):
        # Initialize weights as 0 (Can be Initialized Randomly as well)
        self.weights = np.random.rand(input_size)  # Makes NumPy Array of <input_size>
        # Initialize bias as 0 (Can be Initialized Randomly as well)
        self.bias = np.random.rand()  
        self.learning_rate = learning_rate
    
    def predict(self, inputs):
        """Takes Inputs array to predict the output"""
        weighted_sum = np.dot(inputs, self.weights) + self.bias

        # Returning after calling the Activation Function
        return step_function(weighted_sum)
    
    def train(self, training_inputs, target_outputs, epochs=10):
        """Takes the AND Gate (x1,x2) and y to train """
        for epoch in range(epochs):  # Repeat for multiple epochs

            # print(f"\nEpoch {epoch+1}")
            # print(" ----------------------")
            
            for inputs, target_output in zip(training_inputs, target_outputs):
                prediction = self.predict(inputs)
                error = target_output - prediction  # Calculate (Target Output (t) -  Acutual Output(y))
                
                # print(f"Input: {inputs}, Prediction: {prediction}, Expected: {target_output}, Error: {error}")
                
                # Update weights and bias using perceptron learning rule
                self.weights += self.learning_rate * error * np.array(inputs)
                self.bias += self.learning_rate * error

                # print(f"Updated Weights: {self.weights}, Updated Bias: {self.bias}")

# From AND Gate Table (x1,x2)
training_inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
# From AND Gate Table (y) Outputs
target_outputs = np.array([0, 0, 0, 1])

# Initialize and train perceptron
perceptron = Perceptron(input_size=2, learning_rate=LEARNING_RATE)
perceptron.train(training_inputs=training_inputs, target_outputs=target_outputs, epochs=EPOCHS)

# Testing the trained perceptron
print("\nTesting AND Gate Perceptron:")
for inputs in training_inputs:
    print(f"Input: {inputs}, Predicted Output: {perceptron.predict(inputs)}")

```

##### Output
![](../../../../../../../Images/First_Sem_Images/Question2%20-%20WAP%20to%20train%20AND%20Gate%20Using%20Perceptron%20Algo%20OUTPUT.png)

#### Things Different from Numerical
- Making the weight and bias equals to 0. *Makes the neuron learn the same thing*
- `np.random.rand(input_size)`  -> Makes NumPy Array of <input_size>. Value if from 0 to 1.
- `self.weights = np.zeros(input_size)` -> Makes NumPy Array of 0's of <input_size>. All Value = 0. **BAD PRACTICE**

## Tag
#assignment #NN 