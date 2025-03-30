```python
# Implement Backpropagation to train an ANN with configuration 2x2x1 for XOR function
# Using the sigmoid activation function to keep outputs in range (0,1)
# Implementing online (stochastic) learning

import numpy as np

# Initialize XOR input and target outputs
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_data = np.array([0, 1, 1, 0])

# Setting parameters
np.random.seed(1)  # Ensures consistent random values on each run
num_inputs = 2 # 2 Inputs of XOR
num_hidden = 2 # 2 hidden layers
num_outputs = 1

# Initialize weights and biases
# 2 Biases for hidden and 1 Bias output layer

# Initializing weights between the input layer and hidden layer
# Shape: (num_hidden, num_inputs) -> Each hidden neuron gets weights for all input neurons
weights_input_hidden = np.random.uniform(-1, 1, (num_hidden, num_inputs))

# Initializing biases for the hidden layer
# Shape: (num_hidden, 1) -> Each hidden neuron gets its own bias term
bias_hidden = np.random.uniform(-1, 1, (num_hidden, 1))

# Initializing weights between the hidden layer and output layer
# Shape: (num_outputs, num_hidden) -> Each output neuron gets weights from all hidden neurons
weights_hidden_output = np.random.uniform(-1, 1, (num_outputs, num_hidden))

# Initializing biases for the output layer
# Shape: (num_outputs, 1) -> Each output neuron gets its own bias term
bias_output = np.random.uniform(-1, 1, (num_outputs, 1))


# Learning rate and activation parameter
learning_rate = 0.5
iterations = 10000
activation_factor = 1

# Training using Backpropagation
for epoch in range(iterations):
    print(f"\nEpoch {epoch + 1}")

    for sample in range(len(input_data)):  # Loop through each training sample (XOR inputs)
        # Prepare input and target
        # Extract the current input sample and reshape it into a column vector (2x1)
        # Example: [0, 0] -> [[0], [0]]
        input_vector = input_data[sample].reshape(-1, 1)

        # Extract the corresponding target output and reshape it into a column vector (1x1)
        # Example: 0 -> [[0]]
        target_vector = np.array([target_data[sample]]).reshape(-1, 1)

        # Forward propagation to hidden layer
        # Forward propagation to hidden layer
        # Compute the weighted sum of inputs to hidden layer neurons (netinput = Wx + b)
        # net_input(h) = W^(h) * x + b^(h)
        hidden_net_input = np.dot(weights_input_hidden, input_vector) + bias_hidden

        # Apply the sigmoid activation function to the weighted sum
        # sigmoid_activation_func(h) = 1 / (1 + exp(-a * z^(h)))
        # Where 'a' is the activation factor that controls the steepness of the sigmoid function.
        hidden_activation = 1 / (1 + np.exp(-activation_factor * hidden_net_input))

        # Forward propagation to output layer

        # Compute the weighted sum of the hidden layer activations
        # Explanation:
        # - `weights_hidden_output`: A matrix containing the weights connecting the hidden layer to the output layer.
        # - `hidden_activation`: The activations (output values) from the hidden layer neurons.
        output_net_input = np.dot(weights_hidden_output, hidden_activation) + bias_output

        # Apply sigmoid activation function
        # Explanation:
        # - `activation_factor`: A scalar value controlling how steep the activation curve is.
        predicted_output = 1 / (1 + np.exp(-activation_factor * output_net_input))

        # Compute error (Mean Squared Error)
        loss = 0.5 * (target_vector - predicted_output) ** 2

        # Explanation:
        # - `target_vector`: The actual expected output value.
        # - `predicted_output`: The model's predicted output after forward propagation.
        # - `(target_vector - predicted_output)`: Difference between actual and predicted values.
        # - Squaring this difference ensures positive values (prevents negative errors from canceling out).
        # - Multiplication by 0.5 is a standard convention to simplify gradient calculations in backpropagation.

        # Print the input, predicted output, and actual target
        print(f"Input: {input_vector.T}, Output: {predicted_output[0,0]:.4f}, Target: {target_vector[0,0]}")
        
        # Explanation:
        # - `input_vector.T`: Displays input values in a readable row format.
        # - `predicted_output[0,0]:.4f`: Prints predicted output rounded to 4 decimal places.
        # - `target_vector[0,0]`: Prints the actual expected output.
        # [0,0] -> means 1st row and 1st column of the matrix

        # Backpropagation - compute gradients
        output_gradient = (target_vector - predicted_output) * activation_factor * predicted_output * (1 - predicted_output)
        hidden_gradient = np.dot(weights_hidden_output.T, output_gradient) * activation_factor * hidden_activation * (1 - hidden_activation)

        # Update weights and biases
        weights_hidden_output += learning_rate * np.dot(output_gradient, hidden_activation.T)
        bias_output += learning_rate * output_gradient
        weights_input_hidden += learning_rate * np.dot(hidden_gradient, input_vector.T)
        bias_hidden += learning_rate * hidden_gradient

# Testing the trained model
print("\nTesting the trained network:")
for sample in range(len(input_data)):
    input_vector = input_data[sample].reshape(-1, 1)

    # Forward pass
    hidden_net_input = np.dot(weights_input_hidden, input_vector) + bias_hidden
    hidden_activation = 1 / (1 + np.exp(-activation_factor * hidden_net_input))
    output_net_input = np.dot(weights_hidden_output, hidden_activation) + bias_output
    predicted_output = 1 / (1 + np.exp(-activation_factor * output_net_input))

    # Round the output to nearest integer
    predicted_label = 1 if predicted_output > 0.5 else 0
    print(f"Input: {input_vector.T}, Output: {predicted_output[0,0]:.4f}, Predicted: {predicted_label}, Target_output: {target_data[sample]}")

```

Output
![](../../../../../../Images/Backpropagation%20Sigmoid.png)