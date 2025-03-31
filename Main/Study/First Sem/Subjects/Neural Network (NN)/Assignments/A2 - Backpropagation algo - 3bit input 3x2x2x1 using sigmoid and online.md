### OOP Based
```python
# Q5
#Implement Backpropagation algorithm to train an ANN of configuration 3x2x2x1 to achieve majority function with 3-bit data.
#Output of the network must be 1 when there are two or more 1’s in the data.
#(Use sigmoid activation function).
#implementing and online method.

import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size, learning_rate=0.5):
        """
        Initializes the neural network with random weights and biases.
        :param input_size: Number of neurons in the input layer
        :param hidden_size1: Number of neurons in the first hidden layer
        :param hidden_size2: Number of neurons in the second hidden layer
        :param output_size: Number of neurons in the output layer
        :param learning_rate: Learning rate for weight updates
        """
        self.input_size = input_size
        self.hidden_size1 = hidden_size1
        self.hidden_size2 = hidden_size2
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.a = 1  # Sigmoid activation parameter

        # Set a random seed for reproducibility
        np.random.seed(1)
        
        # Initialize weights and biases for each layer
        self.W1 = np.random.uniform(-1, 1, (hidden_size1, input_size))  # Weights between input and hidden layer 1
        self.b1 = np.random.uniform(-1, 1, (hidden_size1, 1))  # Bias for hidden layer 1
        self.W2 = np.random.uniform(-1, 1, (hidden_size2, hidden_size1))  # Weights between hidden layer 1 and 2
        self.b2 = np.random.uniform(-1, 1, (hidden_size2, 1))  # Bias for hidden layer 2
        self.W3 = np.random.uniform(-1, 1, (output_size, hidden_size2))  # Weights between hidden layer 2 and output
        self.b3 = np.random.uniform(-1, 1, (output_size, 1))  # Bias for output layer

    def sigmoid(self, x):
        """Applies the sigmoid activation function."""
        return 1 / (1 + np.exp(-self.a * x))

    def sigmoid_derivative(self, x):
        """Computes the derivative of the sigmoid function."""
        return self.a * x * (1 - x)

    def forward(self, x):
        """Performs the forward propagation through the network."""
        self.hidden_layer1 = np.dot(self.W1, x) + self.b1
        self.a1 = self.sigmoid(self.hidden_layer1)  # Activation of first hidden layer
        
        self.hidden_layer2 = np.dot(self.W2, self.a1) + self.b2
        self.a2 = self.sigmoid(self.hidden_layer2)  # Activation of second hidden layer
        
        self.output_layer = np.dot(self.W3, self.a2) + self.b3
        self.output = self.sigmoid(self.output_layer)  # Final output
        return self.output

    def backward(self, x, target):
        """Performs the backward propagation (Backpropagation algorithm)."""
        error = target - self.output  # Compute error
        d_output = error * self.sigmoid_derivative(self.output)  # Output layer error gradient
        
        d_hidden2 = np.dot(self.W3.T, d_output) * self.sigmoid_derivative(self.a2)  # Hidden layer 2 error gradient
        d_hidden1 = np.dot(self.W2.T, d_hidden2) * self.sigmoid_derivative(self.a1)  # Hidden layer 1 error gradient

        # Update weights and biases
        self.W3 += self.learning_rate * np.dot(d_output, self.a2.T)
        self.b3 += self.learning_rate * d_output
        self.W2 += self.learning_rate * np.dot(d_hidden2, self.a1.T)
        self.b2 += self.learning_rate * d_hidden2
        self.W1 += self.learning_rate * np.dot(d_hidden1, x.T)
        self.b1 += self.learning_rate * d_hidden1

    def train(self, X, Y, epochs):
        """Trains the neural network using the given dataset."""
        for epoch in range(epochs):
            # print(f"\nEpoch {epoch + 1}")
            for i in range(len(X)):
                x = X[i].reshape(-1, 1)  # Reshape input as column vector
                target = np.array([Y[i]]).reshape(-1, 1)  # Reshape target as column vector
                self.forward(x)  # Forward propagation
                self.backward(x, target)  # Backpropagation and weight update
                # print(f"Input: {x.T}, Output: {self.output[0,0]:.4f}, Target: {target[0,0]}")

    def predict(self, X):
        """Tests the trained model with the given inputs."""
        print("\nTesting the trained network:")
        for i in range(len(X)):
            x = X[i].reshape(-1, 1)
            output = self.forward(x)  # Perform forward pass
            predicted_class = 1 if output > 0.5 else 0  # Round output to 0 or 1
            print(f"Input: {x.T}, Output: {output[0,0]:.4f}, Predicted: {predicted_class}")

# Define input and target data for majority function (3-bit input)
input_values = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0,], [0, 1, 1],
                         [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
target_outputs = np.array([0, 0, 0, 1, 0, 1, 1, 1])  # Output is 1 when at least 2 bits are 1

# Create and train the neural network
nn = NeuralNetwork(input_size=3, hidden_size1=2, hidden_size2=2, output_size=1, learning_rate=0.5)
nn.train(input_values, target_outputs, epochs=10000)

# Test the trained model
nn.predict(input_values)

```
###### Output
![](../../../../../Images/backpropagation%203bit%20sigmoid%20and%20online.png)
## Tag
#assignment #NN 