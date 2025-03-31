#### Default
```python
# Q2
# Implement Backpropagation algorithm to train an ANN of configuration 2x2x1 to achieve XOR function.
# (Use Tanh activation function)It squashes the O/P in the range of (-1,1).
# implement online method.
# Importing the necessary library for numerical operations
import numpy as np

# XOR input and expected output
input_data = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
expected_output = np.array([-1, 1, 1, -1])

# Neural network configuration
np.random.seed(1)  # Ensures reproducibility
num_input = 2
num_hidden = 2
num_output = 1

# Initialize weights and biases
weights_input_hidden = np.random.uniform(-1, 1, (num_hidden, num_input))
bias_hidden = np.random.uniform(-1, 1, (num_hidden, 1))
weights_hidden_output = np.random.uniform(-1, 1, (num_output, num_hidden))
bias_output = np.random.uniform(-1, 1, (num_output, 1))

# Learning parameters
alpha = 0.5
num_epochs = 10000

# Training process
for epoch in range(num_epochs):
    print(f"\nEpoch {epoch + 1}")
    
    for index in range(len(input_data)):
        # Prepare input and expected output
        sample_input = input_data[index].reshape(-1, 1)
        target_value = np.array([expected_output[index]]).reshape(-1, 1)
        
        # Forward propagation
        hidden_layer_input = np.dot(weights_input_hidden, sample_input) + bias_hidden
        hidden_layer_output = np.tanh(hidden_layer_input)
        final_layer_input = np.dot(weights_hidden_output, hidden_layer_output) + bias_output
        predicted_value = np.tanh(final_layer_input)
        
        # Compute error
        loss = 0.5 * (target_value - predicted_value) ** 2
        print(f"Input: {sample_input.T}, Output: {predicted_value[0,0]:.4f}, Target: {target_value[0,0]}")
        
        # Backpropagation
        output_error_gradient = (target_value - predicted_value) * (1 - np.tanh(final_layer_input) ** 2)
        hidden_error_gradient = np.dot(weights_hidden_output.T, output_error_gradient) * (1 - np.tanh(hidden_layer_input) ** 2)
        
        # Update weights and biases
        weights_hidden_output += alpha * np.dot(output_error_gradient, hidden_layer_output.T)
        bias_output += alpha * output_error_gradient
        weights_input_hidden += alpha * np.dot(hidden_error_gradient, sample_input.T)
        bias_hidden += alpha * hidden_error_gradient

# Testing phase
print("\nTesting the trained network:")
for index in range(len(input_data)):
    sample_input = input_data[index].reshape(-1, 1)
    hidden_layer_input = np.dot(weights_input_hidden, sample_input) + bias_hidden
    hidden_layer_output = np.tanh(hidden_layer_input)
    final_layer_input = np.dot(weights_hidden_output, hidden_layer_output) + bias_output
    predicted_value = np.tanh(final_layer_input)
    
    predicted_class = 1 if predicted_value > 0 else -1
    print(f"Input: {sample_input.T}, Output: {predicted_value[0,0]:.4f}, Predicted: {predicted_class}, Target: {expected_output[index]}")

```

#### OOP based
```python
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.5):
        np.random.seed(1)  # Fix seed for reproducibility
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.uniform(-1, 1, (hidden_size, input_size))
        self.bias_hidden = np.random.uniform(-1, 1, (hidden_size, 1))
        
        self.weights_hidden_output = np.random.uniform(-1, 1, (output_size, hidden_size))
        self.bias_output = np.random.uniform(-1, 1, (output_size, 1))
        
        self.learning_rate = learning_rate

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

    def backward(self, x, target):
        """ Backpropagation and weight updates """
        target = np.array([target]).reshape(-1, 1)

        # Compute output error gradient
        output_error = (target - self.output) * self.tanh_derivative(self.output_input)
        
        # Compute hidden layer error gradient
        hidden_error = np.dot(self.weights_hidden_output.T, output_error) * self.tanh_derivative(self.hidden_input)

        # Update weights and biases
        self.weights_hidden_output += self.learning_rate * np.dot(output_error, self.hidden_output.T)
        self.bias_output += self.learning_rate * output_error

        self.weights_input_hidden += self.learning_rate * np.dot(hidden_error, x.T)
        self.bias_hidden += self.learning_rate * hidden_error

    def train(self, inputs, targets, epochs=10000):
        """ Train the neural network using online learning """
        for epoch in range(epochs):
            for i in range(len(inputs)):
                x = inputs[i].reshape(-1, 1)
                target = targets[i]

                # Forward and backward pass
                self.forward(x)
                self.backward(x, target)

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