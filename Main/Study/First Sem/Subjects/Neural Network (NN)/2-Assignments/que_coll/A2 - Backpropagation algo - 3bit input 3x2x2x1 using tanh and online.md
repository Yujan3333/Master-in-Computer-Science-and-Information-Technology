### OOP Based
```python
# Q7
#Implement Backpropagation algorithm to train an ANN of configuration 3x2x2x1 to achieve majority function with 3-bit data.
#Output of the network must be 1 when there are two or more 1’s in the data.
#(Use tanh activation function).
#implementing and online method.

import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden1_size, hidden2_size, output_size, learning_rate=0.5, epochs=10000):
        np.random.seed(1)  # Fix random seed for reproducibility
        self.input_size = input_size
        self.hidden1_size = hidden1_size
        self.hidden2_size = hidden2_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.epochs = epochs

        # Initialize weights and biases
        self.W1 = np.random.uniform(-1, 1, (hidden1_size, input_size))
        self.b1 = np.random.uniform(-1, 1, (hidden1_size, 1))
        self.W2 = np.random.uniform(-1, 1, (hidden2_size, hidden1_size))
        self.b2 = np.random.uniform(-1, 1, (hidden2_size, 1))
        self.W3 = np.random.uniform(-1, 1, (output_size, hidden2_size))
        self.b3 = np.random.uniform(-1, 1, (output_size, 1))
    
    def tanh(self, x):
        return np.tanh(x)
    
    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2
    
    def forward(self, x):
        self.z1 = np.dot(self.W1, x) + self.b1
        self.a1 = self.tanh(self.z1)
        
        self.z2 = np.dot(self.W2, self.a1) + self.b2
        self.a2 = self.tanh(self.z2)
        
        self.z3 = np.dot(self.W3, self.a2) + self.b3
        self.output = self.tanh(self.z3)
        return self.output
    
    def backward(self, x, target):
        # Compute output layer error
        output_error = (target - self.output) * self.tanh_derivative(self.output)
        
        # Compute hidden layer errors
        hidden2_error = np.dot(self.W3.T, output_error) * self.tanh_derivative(self.a2)
        hidden1_error = np.dot(self.W2.T, hidden2_error) * self.tanh_derivative(self.a1)
        
        # Update weights and biases
        self.W3 += self.learning_rate * np.dot(output_error, self.a2.T)
        self.b3 += self.learning_rate * output_error
        
        self.W2 += self.learning_rate * np.dot(hidden2_error, self.a1.T)
        self.b2 += self.learning_rate * hidden2_error
        
        self.W1 += self.learning_rate * np.dot(hidden1_error, x.T)
        self.b1 += self.learning_rate * hidden1_error
    
    def train(self, input_values, target_outputs):
        for epoch in range(self.epochs):
            for i in range(len(input_values)):
                x = input_values[i].reshape(-1, 1)
                target = np.array([target_outputs[i]]).reshape(-1, 1)
                
                self.forward(x)
                self.backward(x, target)
                
            # if epoch % 1000 == 0:
            #     print(f"Epoch {epoch+1}/{self.epochs}")
    
    def test(self, input_values, target_outputs):
        print("\nTesting the trained network:")
        for i in range(len(input_values)):
            x = input_values[i].reshape(-1, 1)
            predicted_output = self.forward(x)
            predicted_class = 1 if predicted_output > 0.5 else 0
            print(f"Input: {x.T}, Output: {predicted_output[0,0]:.4f}, Predicted: {predicted_class}, Target: {target_outputs[i]}")

# Define input and target values
input_values = np.array([
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
    [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
])
target_outputs = np.array([0, 0, 0, 1, 0, 1, 1, 1])

# Initialize and train the network
nn = NeuralNetwork(input_size=3, hidden1_size=2, hidden2_size=2, output_size=1)
nn.train(input_values, target_outputs)

# Test the trained network
nn.test(input_values, target_outputs)

```

###### Output
![](../../../../../../Images/A2%20-%20Backpropagation%20algo%20-%203bit%20input%203x2x2x1%20using%20tanh%20and%20online-1.png)

## Tag
#assignment #NN 