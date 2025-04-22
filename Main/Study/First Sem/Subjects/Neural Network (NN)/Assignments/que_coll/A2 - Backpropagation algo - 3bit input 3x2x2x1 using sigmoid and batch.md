[A2 Backpropagation -- 3bit input Sigmoid and batch](A2%20Backpropagation%20--%203bit%20input%20Sigmoid%20and%20batch.md)
### OOP Based
```python
#Q6
#Implement Backpropagation algorithm to train an ANN of configuration 3x2x2x1 to achieve majority function with 3-bit data.
#Output of the network must be 1 when there are two or more 1’s in the data.
#(Use sigmoid activation function).
#implementing batch gradient descent method.

import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        np.random.seed(1)  # Fix random seed for reproducibility

        # Initialize layers and parameters
        self.input_size = input_size
        self.hidden_size1 = hidden_size1
        self.hidden_size2 = hidden_size2
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden1 = np.random.uniform(-1, 1, (hidden_size1, input_size))
        self.bias_hidden1 = np.random.uniform(-1, 1, (hidden_size1, 1))

        self.weights_hidden1_hidden2 = np.random.uniform(-1, 1, (hidden_size2, hidden_size1))
        self.bias_hidden2 = np.random.uniform(-1, 1, (hidden_size2, 1))

        self.weights_hidden2_output = np.random.uniform(-1, 1, (output_size, hidden_size2))
        self.bias_output = np.random.uniform(-1, 1, (output_size, 1))

        self.learning_rate = 0.5
        self.a = 1  # Sigmoid slope parameter

    def sigmoid(self, x):
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-self.a * x))

    def forward_pass(self, x):
        """Forward pass through the network."""
        self.hidden1_input = np.dot(self.weights_input_hidden1, x) + self.bias_hidden1
        self.hidden1_output = self.sigmoid(self.hidden1_input)

        self.hidden2_input = np.dot(self.weights_hidden1_hidden2, self.hidden1_output) + self.bias_hidden2
        self.hidden2_output = self.sigmoid(self.hidden2_input)

        self.output_input = np.dot(self.weights_hidden2_output, self.hidden2_output) + self.bias_output
        self.output = self.sigmoid(self.output_input)

        return self.output

    def backward_pass(self, x, target):
        """Backward pass (backpropagation) for weight updates."""
        # Calculate error gradients for output layer
        output_error_gradient = (target - self.output) * (self.a * self.output * (1 - self.output))

        # Calculate error gradients for hidden layer 2
        hidden2_error_gradient = np.dot(self.weights_hidden2_output.T, output_error_gradient) * (self.a * self.hidden2_output * (1 - self.hidden2_output))

        # Calculate error gradients for hidden layer 1
        hidden1_error_gradient = np.dot(self.weights_hidden1_hidden2.T, hidden2_error_gradient) * (self.a * self.hidden1_output * (1 - self.hidden1_output))

        # Accumulate gradients
        self.d_weights_hidden2_output += np.dot(output_error_gradient, self.hidden2_output.T)
        self.d_bias_output += output_error_gradient

        self.d_weights_hidden1_hidden2 += np.dot(hidden2_error_gradient, self.hidden1_output.T)
        self.d_bias_hidden2 += hidden2_error_gradient

        self.d_weights_input_hidden1 += np.dot(hidden1_error_gradient, x.T)
        self.d_bias_hidden1 += hidden1_error_gradient

    def update_weights(self, batch_size):
        """Update weights and biases using the accumulated gradients."""
        self.weights_hidden2_output += (self.learning_rate / batch_size) * self.d_weights_hidden2_output
        self.bias_output += (self.learning_rate / batch_size) * self.d_bias_output

        self.weights_hidden1_hidden2 += (self.learning_rate / batch_size) * self.d_weights_hidden1_hidden2
        self.bias_hidden2 += (self.learning_rate / batch_size) * self.d_bias_hidden2

        self.weights_input_hidden1 += (self.learning_rate / batch_size) * self.d_weights_input_hidden1
        self.bias_hidden1 += (self.learning_rate / batch_size) * self.d_bias_hidden1

    def train(self, inputs, targets, epochs):
        """Train the network using batch gradient descent."""
        for epoch in range(epochs):
            # print(f"\nEpoch {epoch + 1}")

            # Reset gradients
            self.d_weights_hidden2_output = np.zeros_like(self.weights_hidden2_output)
            self.d_bias_output = np.zeros_like(self.bias_output)
            self.d_weights_hidden1_hidden2 = np.zeros_like(self.weights_hidden1_hidden2)
            self.d_bias_hidden2 = np.zeros_like(self.bias_hidden2)
            self.d_weights_input_hidden1 = np.zeros_like(self.weights_input_hidden1)
            self.d_bias_hidden1 = np.zeros_like(self.bias_hidden1)

            # Iterate over all training samples (batch gradient descent)
            for i in range(len(inputs)):
                x = inputs[i].reshape(-1, 1)  # Reshape input to column vector
                target = np.array([targets[i]]).reshape(-1, 1)  # Reshape target to column vector

                # Forward pass
                self.forward_pass(x)

                # Backward pass
                self.backward_pass(x, target)

            # Update weights and biases
            self.update_weights(len(inputs))

    def predict(self, inputs):
        """Predict the output for new inputs."""
        predictions = []
        for x in inputs:
            x = x.reshape(-1, 1)
            output = self.forward_pass(x)
            predictions.append(1 if output > 0.5 else 0)  # Convert to binary (0 or 1)
        return predictions

# XOR Input values and targets
input_values = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
target_outputs = np.array([0, 0, 0, 1, 0, 1, 1, 1])

# Initialize the neural network
nn = NeuralNetwork(input_size=3, hidden_size1=2, hidden_size2=2, output_size=1)

# Train the network
nn.train(input_values, target_outputs, epochs=10000)

# After training, test the network
print("\nTesting the trained network:")
predictions = nn.predict(input_values)

# zip(input_values, predictions, target_outputs) combines the three lists into tuples, where each tuple contains one element from each list.  
# enumerate() adds an index i to each tuple.
for i, (input_data, prediction, target) in enumerate(zip(input_values, predictions, target_outputs)):
    print(f"Input: {input_data}, Predicted: {prediction}, Target: {target}")

```

## Tag
#assignment #NN 