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
