
```python
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.5, epochs=10000):
        np.random.seed(1)  # Fix seed for reproducibility

        # Initialize weights and biases
        self.weights_input_hidden = np.random.uniform(-1, 1, (hidden_size, input_size))
        self.bias_hidden = np.random.uniform(-1, 1, (hidden_size, 1))
        self.weights_hidden_output = np.random.uniform(-1, 1, (output_size, hidden_size))
        self.bias_output = np.random.uniform(-1, 1, (output_size, 1))
        
        self.learning_rate = learning_rate
        self.epochs = epochs

    def tanh(self, x):
        return np.tanh(x)

    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2  # Derivative of tanh

    def forward(self, x):
        """ Forward propagation """
        self.hidden_input = np.dot(self.weights_input_hidden, x) + self.bias_hidden
        self.hidden_output = self.tanh(self.hidden_input)
        
        self.output_input = np.dot(self.weights_hidden_output, self.hidden_output) + self.bias_output
        self.output = self.tanh(self.output_input)
        
        return self.output

    def backward(self, inputs, targets):
        """ Batch Gradient Descent - Computes gradients over entire dataset """
        d_weights_hidden_output = np.zeros_like(self.weights_hidden_output)
        d_bias_output = np.zeros_like(self.bias_output)
        d_weights_input_hidden = np.zeros_like(self.weights_input_hidden)
        d_bias_hidden = np.zeros_like(self.bias_hidden)
        batch_size = len(inputs)

        for i in range(batch_size):
            x = inputs[i].reshape(-1, 1)
            target = np.array([targets[i]]).reshape(-1, 1)

            # Forward pass
            self.forward(x)

            # Compute output error gradient
            output_error = (target - self.output) * self.tanh_derivative(self.output_input)
            
            # Compute hidden layer error gradient
            hidden_error = np.dot(self.weights_hidden_output.T, output_error) * self.tanh_derivative(self.hidden_input)

            # Accumulate gradients
            d_weights_hidden_output += np.dot(output_error, self.hidden_output.T)
            d_bias_output += output_error
            d_weights_input_hidden += np.dot(hidden_error, x.T)
            d_bias_hidden += hidden_error

        # Update weights and biases with batch gradient descent
        self.weights_hidden_output += (self.learning_rate / batch_size) * d_weights_hidden_output
        self.bias_output += (self.learning_rate / batch_size) * d_bias_output
        self.weights_input_hidden += (self.learning_rate / batch_size) * d_weights_input_hidden
        self.bias_hidden += (self.learning_rate / batch_size) * d_bias_hidden

    def train(self, inputs, targets):
        """ Train the neural network using batch gradient descent """
        for epoch in range(self.epochs):
            self.backward(inputs, targets)

    def predict(self, x):
        """ Predict output for given input """
        x = x.reshape(-1, 1)
        output = self.forward(x)
        return 1 if output > 0 else -1  # Convert tanh output to binary (-1 or 1)

# Initialize XOR dataset
XOR_inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
XOR_targets = np.array([-1, 1, 1, -1])

# Create and train the neural network
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)
nn.train(XOR_inputs, XOR_targets)

# Test the trained network
print("\nTesting the trained network:")
for i in range(len(XOR_inputs)):
    prediction = nn.predict(XOR_inputs[i])
    print(f"Input: {XOR_inputs[i]}, Predicted: {prediction}, Target: {XOR_targets[i]}")

```

###### Output
![](../../../../../../Images/XOR%20Tanh%20batch.png)

## Tag
#assignment #NN 