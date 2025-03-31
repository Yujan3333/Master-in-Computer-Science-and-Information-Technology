### OOP Based
```python
# Q1
# Implement Backpropagation to train an ANN with configuration 2x2x1 for XOR function
# Using the sigmoid activation function to keep outputs in range (0,1)
# Implementing online (stochastic) learning

import numpy as np  # Importing the numpy library for numerical operations

# Defining the XORNeuralNetwork class
class XORNeuralNetwork:
    def __init__(self, num_inputs=2, num_hidden=2, num_outputs=1, learning_rate=0.5, activation_factor=1, iterations=10000):
        # Initializing the network parameters
        self.num_inputs = num_inputs  # Number of input neurons (2 for XOR)
        self.num_hidden = num_hidden  # Number of hidden neurons (2)
        self.num_outputs = num_outputs  # Number of output neurons (1 for XOR)
        self.learning_rate = learning_rate  # Learning rate for weight updates
        self.activation_factor = activation_factor  # Factor to control sigmoid steepness
        self.iterations = iterations  # Number of iterations for training (No of epochs)

        # Initialize weights and biases with random values
        np.random.seed(1)  # Set the seed for reproducibility

        ## Initializing weights between the input layer and hidden layer
        # Shape: (num_hidden, num_inputs) -> Each hidden neuron gets weights for all input neurons
        self.weights_input_hidden = np.random.uniform(-1, 1, (num_hidden, num_inputs))

        ## Initializing biases for the hidden layer
        # Shape: (num_hidden, 1) -> Each hidden neuron gets its own bias term
        self.bias_hidden = np.random.uniform(-1, 1, (num_hidden, 1)) 

        ## Initializing weights between the hidden layer and output layer
        # Shape: (num_outputs, num_hidden) -> Each output neuron gets weights from all hidden neurons
        self.weights_hidden_output = np.random.uniform(-1, 1, (num_outputs, num_hidden))

        ## Initializing biases for the output layer
        # Shape: (num_outputs, 1) -> Each output neuron gets its own bias term
        self.bias_output = np.random.uniform(-1, 1, (num_outputs, 1))
    
    def sigmoid(self, x):
        # Sigmoid activation function, squashes input between 0 and 1
        return 1 / (1 + np.exp(-self.activation_factor * x))
    
    def sigmoid_derivative(self, x):
        # Derivative of the sigmoid function, needed for backpropagation
        return x * (1 - x)
    
    def forward_propagation(self, input_vector):
        # Forward propagation to calculate the predicted output

        ## Input to hidden layer
        # Compute the weighted sum of inputs to hidden layer neurons (netinput = Wx + b)
        # net_input(h) = W^(h) * x + b^(h)
        hidden_net_input = np.dot(self.weights_input_hidden, input_vector) + self.bias_hidden 

        ## Activation after applying sigmoid to hidden layer input
        # sigmoid_activation_func(h) = 1 / (1 + exp(-a * net_input(h)))
        # Where 'a' is the activation factor that controls the steepness of the sigmoid function.
        hidden_activation = self.sigmoid(hidden_net_input)  

        ## Forward propagation to output layer
        # Compute the weighted sum of the hidden layer activations
        # Explanation:
        # - `weights_hidden_output`: A matrix containing the weights connecting the hidden layer to the output layer.
        # - `hidden_activation`: The activations (output values) from the hidden layer neurons.
        output_net_input = np.dot(self.weights_hidden_output, hidden_activation) + self.bias_output

        # Apply sigmoid activation function to get the final predicted output
        # Explanation:
        # - `activation_factor`: A scalar value controlling how steep the activation curve is.  
        predicted_output = self.sigmoid(output_net_input)  
        return hidden_activation, predicted_output  # Return hidden activation and predicted output
    
    def backpropagation(self, input_vector, target_vector, hidden_activation, predicted_output):
        # Backpropagation to adjust weights and biases based on error
        output_error = target_vector - predicted_output  # Error in output layer (error=y_true​−y_pred​)

        ## Gradient for output layer
        # (σ′(x)=σ(x)⋅(1−σ(x))) where σ(x)σ(x) is the sigmoid activation function
        output_gradient = output_error * self.sigmoid_derivative(predicted_output)   

        ## Propagate error to hidden layer
        # The error for the hidden layer is calculated by 
        # multiplying the output gradient by the transpose of the weights between the hidden and output layers.
        # Explanation:
        # - `weights_hidden_output.T`: Displays input values in a readable row format.
        hidden_error = np.dot(self.weights_hidden_output.T, output_gradient)  

        hidden_gradient = hidden_error * self.sigmoid_derivative(hidden_activation)  # Gradient for hidden layer
        
        # Update weights and biases using the gradients and learning rate
        self.weights_hidden_output += self.learning_rate * np.dot(output_gradient, hidden_activation.T)  # Update hidden-to-output weights
        self.bias_output += self.learning_rate * output_gradient  # Update output bias
        self.weights_input_hidden += self.learning_rate * np.dot(hidden_gradient, input_vector.T)  # Update input-to-hidden weights
        self.bias_hidden += self.learning_rate * hidden_gradient  # Update hidden bias
    
    def train(self, input_data, target_data):
        # Training the model using backpropagation
        for epoch in range(self.iterations):  # Loop over the number of training iterations
            for sample in range(len(input_data)):  # Loop through each training sample (XOR inputs)

                # Reshape input vector for matrix operations
                # Extract the current input sample and reshape it into a column vector (2x1)
                # Example: [0, 0] -> [[0], [0]]
                input_vector = input_data[sample].reshape(-1, 1)

                # Reshape target vector
                # Extract the corresponding target output and reshape it into a column vector (1x1)
                # Example: 0 -> [[0]]
                target_vector = np.array([target_data[sample]]).reshape(-1, 1)  

                # Perform forward propagation
                hidden_activation, predicted_output = self.forward_propagation(input_vector)  

                # Perform backpropagation to adjust weights
                self.backpropagation(input_vector, target_vector, hidden_activation, predicted_output)  
    
    def predict(self, input_data):
        # Making predictions with the trained model
        predictions = []  # List to store predictions
        for sample in range(len(input_data)):  # Loop through each sample in the input data
            input_vector = input_data[sample].reshape(-1, 1)  # Reshape input vector for matrix operations
            _, predicted_output = self.forward_propagation(input_vector)  # Perform forward propagation to get the predicted output
            predicted_label = 1 if predicted_output > 0.5 else 0  # Convert output to binary (1 or 0) based on threshold
            predictions.append(predicted_label)  # Append prediction to list
        return predictions  # Return list of predictions

# Initialize dataset for XOR function
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Possible input combinations for XOR
target_data = np.array([0, 1, 1, 0])  # Target outputs for XOR

# Create the neural network model and train it
model = XORNeuralNetwork()  # Initialize the XOR neural network
model.train(input_data, target_data)  # Train the model with the XOR dataset

# Test the trained model by making predictions on the XOR inputs
predictions = model.predict(input_data)  # Get predictions from the trained model

# enumerate function loops over a list where i -> Index and pred -> value
for i, pred in enumerate(predictions):  # Loop through predictions and display them
    print(f"Input: {input_data[i]} -> Predicted: {pred} -> Target: {target_data[i]}")  # Print input, predicted, and actual target


```