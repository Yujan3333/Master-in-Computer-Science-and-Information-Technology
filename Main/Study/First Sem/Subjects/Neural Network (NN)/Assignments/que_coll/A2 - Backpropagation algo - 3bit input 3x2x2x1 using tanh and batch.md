
### OOP Based
```python
#Q8
#Implement Backpropagation algorithm to train an ANN of configuration 3x2x2x1 to achieve majority function with 3-bit data.
#Output of the network must be 1 when there are two or more 1’s in the data.
#(Use tanh activation function).
#implementing batch gradient descent method.

import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size, learning_rate=0.5):
        np.random.seed(1)  # Ensure reproducibility
        self.learning_rate = learning_rate
        
        # Initialize weights and biases
        self.weights_input_hidden1 = np.random.uniform(-1, 1, (hidden_size1, input_size))
        self.bias_hidden1 = np.random.uniform(-1, 1, (hidden_size1, 1))
        
        self.weights_hidden1_hidden2 = np.random.uniform(-1, 1, (hidden_size2, hidden_size1))
        self.bias_hidden2 = np.random.uniform(-1, 1, (hidden_size2, 1))
        
        self.weights_hidden2_output = np.random.uniform(-1, 1, (output_size, hidden_size2))
        self.bias_output = np.random.uniform(-1, 1, (output_size, 1))

    def tanh(self, x):
        return np.tanh(x)

    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2

    def forward_pass(self, x):
        """Performs a forward pass through the network."""
        self.hidden1_input = np.dot(self.weights_input_hidden1, x) + self.bias_hidden1
        self.hidden1_output = self.tanh(self.hidden1_input)
        
        self.hidden2_input = np.dot(self.weights_hidden1_hidden2, self.hidden1_output) + self.bias_hidden2
        self.hidden2_output = self.tanh(self.hidden2_input)
        
        self.output_input = np.dot(self.weights_hidden2_output, self.hidden2_output) + self.bias_output
        self.predicted_output = self.tanh(self.output_input)
        
        return self.predicted_output

    def backward_pass(self, x, target):
        """Performs backpropagation to compute gradients."""
        # Compute error at the output layer
        output_error = (target - self.predicted_output)
        output_gradient = output_error * self.tanh_derivative(self.output_input)
        
        # Compute error at the second hidden layer
        hidden2_error = np.dot(self.weights_hidden2_output.T, output_gradient)
        hidden2_gradient = hidden2_error * self.tanh_derivative(self.hidden2_input)
        
        # Compute error at the first hidden layer
        hidden1_error = np.dot(self.weights_hidden1_hidden2.T, hidden2_gradient)
        hidden1_gradient = hidden1_error * self.tanh_derivative(self.hidden1_input)
        
        return output_gradient, hidden2_gradient, hidden1_gradient
    
    def update_weights(self, x, output_gradient, hidden2_gradient, hidden1_gradient, batch_size):
        """Updates weights and biases using accumulated gradients."""
        self.weights_hidden2_output += (self.learning_rate / batch_size) * np.dot(output_gradient, self.hidden2_output.T)
        self.bias_output += (self.learning_rate / batch_size) * output_gradient
        
        self.weights_hidden1_hidden2 += (self.learning_rate / batch_size) * np.dot(hidden2_gradient, self.hidden1_output.T)
        self.bias_hidden2 += (self.learning_rate / batch_size) * hidden2_gradient
        
        self.weights_input_hidden1 += (self.learning_rate / batch_size) * np.dot(hidden1_gradient, x.T)
        self.bias_hidden1 += (self.learning_rate / batch_size) * hidden1_gradient

    def train(self, input_values, target_outputs, epochs=10000):
        """Trains the network using batch gradient descent."""
        for epoch in range(epochs):
            d_weights_hidden2_output = np.zeros_like(self.weights_hidden2_output)
            d_bias_output = np.zeros_like(self.bias_output)
            d_weights_hidden1_hidden2 = np.zeros_like(self.weights_hidden1_hidden2)
            d_bias_hidden2 = np.zeros_like(self.bias_hidden2)
            d_weights_input_hidden1 = np.zeros_like(self.weights_input_hidden1)
            d_bias_hidden1 = np.zeros_like(self.bias_hidden1)
            
            for i in range(len(input_values)):
                x = input_values[i].reshape(-1, 1)
                target = np.array([target_outputs[i]]).reshape(-1, 1)
                
                self.forward_pass(x)
                output_gradient, hidden2_gradient, hidden1_gradient = self.backward_pass(x, target)
                
                # Accumulate gradients
                d_weights_hidden2_output += np.dot(output_gradient, self.hidden2_output.T)
                d_bias_output += output_gradient
                d_weights_hidden1_hidden2 += np.dot(hidden2_gradient, self.hidden1_output.T)
                d_bias_hidden2 += hidden2_gradient
                d_weights_input_hidden1 += np.dot(hidden1_gradient, x.T)
                d_bias_hidden1 += hidden1_gradient
                
            # Update weights after processing all samples
            batch_size = len(input_values)
            self.update_weights(x, output_gradient, hidden2_gradient, hidden1_gradient, batch_size)
            
            if epoch % 1000 == 0:
                print(f"Epoch {epoch}")

    def test(self, input_values, target_outputs):
        """Tests the trained network."""
        print("\nTesting the trained network:")
        for i in range(len(input_values)):
            x = input_values[i].reshape(-1, 1)
            predicted_output = self.forward_pass(x)
            predicted_class = 1 if predicted_output > 0.5 else 0
            print(f"Input: {x.T}, Output: {predicted_output[0,0]:.4f}, Predicted: {predicted_class}, Target: {target_outputs[i]}")

# Define input and target output
data_inputs = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
target_outputs = np.array([0, 0, 0, 1, 0, 1, 1, 1])

# Initialize and train the neural network
nn = NeuralNetwork(input_size=3, hidden_size1=2, hidden_size2=2, output_size=1)
nn.train(data_inputs, target_outputs)
nn.test(data_inputs, target_outputs)


```

###### Output
![](../../../../../../Images/A2%20-%20Backpropagation%20algo%20-%203bit%20input%203x2x2x1%20using%20tanh%20and%20batch.png)
## Tag
#assignment #NN 