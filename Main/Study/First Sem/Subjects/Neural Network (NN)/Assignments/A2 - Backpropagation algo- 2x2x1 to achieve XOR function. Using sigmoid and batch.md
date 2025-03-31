### OOP Based
- [Major Difference from online and batch earning in section](#Major%20Difference%20from%20online%20learning%20in%20section)
```python
# Q3
# Implement Backpropagation algorithm to train an ANN of configuration 2x2x1 to achieve XOR function.
# (Use sigmoid activation function)It squashes the O/P in the range of (0,1).
# implement batch gradient descent method.

import numpy as np

class XORNeuralNetwork:
    def __init__(self, input_size=2, hidden_size=2, output_size=1, learning_rate=0.5, epochs=10000, a=1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.a = a  # Sigmoid slope parameter
        
        # Initialize weights and biases
        np.random.seed(1)  # Ensure reproducibility
        self.weights_input_hidden = np.random.uniform(-1, 1, (hidden_size, input_size))
        self.bias_hidden = np.random.uniform(-1, 1, (hidden_size, 1))
        self.weights_hidden_output = np.random.uniform(-1, 1, (output_size, hidden_size))
        self.bias_output = np.random.uniform(-1, 1, (output_size, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-self.a * x))

    def sigmoid_derivative(self, x):
        return self.a * x * (1 - x)

    def train(self, input_data, target_data):
        for epoch in range(self.epochs):
            print(f"\nEpoch {epoch + 1}")
            
            # Initialize accumulators for batch gradient descent
            # Explantion:
            # `np.zeros` Creates a matrix of zeros with the same shape as self.weights_hidden_output.
            d_weights_hidden_output = np.zeros_like(self.weights_hidden_output)
            d_bias_output = np.zeros_like(self.bias_output)
            d_weights_input_hidden = np.zeros_like(self.weights_input_hidden)
            d_bias_hidden = np.zeros_like(self.bias_hidden)
            
            for i in range(len(input_data)):
                x = input_data[i].reshape(-1, 1)
                target = np.array([target_data[i]]).reshape(-1, 1)
                
                # Forward pass
                hidden_input = np.dot(self.weights_input_hidden, x) + self.bias_hidden
                hidden_output = self.sigmoid(hidden_input)
                final_input = np.dot(self.weights_hidden_output, hidden_output) + self.bias_output
                predicted_output = self.sigmoid(final_input)
                
                # Compute error
                print(f"Input: {x.T}, Output: {predicted_output[0,0]:.4f}, Target: {target[0,0]}")
                
                # Backpropagation
                output_error = (target - predicted_output) * self.sigmoid_derivative(predicted_output)
                hidden_error = np.dot(self.weights_hidden_output.T, output_error) * self.sigmoid_derivative(hidden_output)
                
                # Accumulate gradients
                d_weights_hidden_output += np.dot(output_error, hidden_output.T)
                d_bias_output += output_error
                d_weights_input_hidden += np.dot(hidden_error, x.T)
                d_bias_hidden += hidden_error
                
            # Apply batch updates
            batch_size = len(input_data)
            self.weights_hidden_output += (self.learning_rate / batch_size) * d_weights_hidden_output
            self.bias_output += (self.learning_rate / batch_size) * d_bias_output
            self.weights_input_hidden += (self.learning_rate / batch_size) * d_weights_input_hidden
            self.bias_hidden += (self.learning_rate / batch_size) * d_bias_hidden

    def predict(self, x):
        x = x.reshape(-1, 1)
        hidden_input = np.dot(self.weights_input_hidden, x) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)
        final_input = np.dot(self.weights_hidden_output, hidden_output) + self.bias_output
        predicted_output = self.sigmoid(final_input)
        return predicted_output
    
    def test(self, input_data, target_data):
        print("\nTesting the trained network:")
        for i in range(len(input_data)):
            x = input_data[i].reshape(-1, 1)
            predicted_output = self.predict(x)
            predicted_class = 1 if predicted_output > 0.5 else 0
            print(f"Input: {x.T}, Output: {predicted_output[0,0]:.4f}, Predicted: {predicted_class}, Target: {target_data[i]}")

# XOR dataset
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_output = np.array([0, 1, 1, 0])

# Train and test the neural network
nn = XORNeuralNetwork()
nn.train(input_data, target_output)
nn.test(input_data, target_output)

```

#### Major Difference from online and batch learning in section
- Here point to focus is that the updating of weights and biases happens after *each epoch* instead of *each input data*.
```python
    def train(self, input_data, target_data):
        for epoch in range(self.epochs):
            print(f"\nEpoch {epoch + 1}")
            
            # Initialize accumulators for batch gradient descent
            # Explantion:
            # `np.zeros` Creates a matrix of zeros with the same shape as self.weights_hidden_output.
            d_weights_hidden_output = np.zeros_like(self.weights_hidden_output)
            d_bias_output = np.zeros_like(self.bias_output)
            d_weights_input_hidden = np.zeros_like(self.weights_input_hidden)
            d_bias_hidden = np.zeros_like(self.bias_hidden)
            
            for i in range(len(input_data)):
                x = input_data[i].reshape(-1, 1)
                target = np.array([target_data[i]]).reshape(-1, 1)
                
                # Forward pass
                hidden_input = np.dot(self.weights_input_hidden, x) + self.bias_hidden
                hidden_output = self.sigmoid(hidden_input)
                final_input = np.dot(self.weights_hidden_output, hidden_output) + self.bias_output
                predicted_output = self.sigmoid(final_input)
                
                # Compute error
                print(f"Input: {x.T}, Output: {predicted_output[0,0]:.4f}, Target: {target[0,0]}")
                
                # Backpropagation
                output_error = (target - predicted_output) * self.sigmoid_derivative(predicted_output)
                hidden_error = np.dot(self.weights_hidden_output.T, output_error) * self.sigmoid_derivative(hidden_output)
                
                # Accumulate gradients
                d_weights_hidden_output += np.dot(output_error, hidden_output.T)
                d_bias_output += output_error
                d_weights_input_hidden += np.dot(hidden_error, x.T)
                d_bias_hidden += hidden_error
                
            # Apply batch updates
            batch_size = len(input_data)
            self.weights_hidden_output += (self.learning_rate / batch_size) * d_weights_hidden_output
            self.bias_output += (self.learning_rate / batch_size) * d_bias_output
            self.weights_input_hidden += (self.learning_rate / batch_size) * d_weights_input_hidden
            self.bias_hidden += (self.learning_rate / batch_size) * d_bias_hidden
```

## Tag
#assignment #NN 