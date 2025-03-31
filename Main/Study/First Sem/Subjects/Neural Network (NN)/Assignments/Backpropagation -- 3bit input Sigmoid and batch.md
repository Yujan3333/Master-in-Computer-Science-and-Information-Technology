```python
#Q6
#Implement Backpropagation algorithm to train an ANN of configuration 3x2x2x1 to achieve majority function with 3-bit data.
#Output of the network must be 1 when there are two or more 1’s in the data.
#(Use sigmoid activation function).
#implementing batch gradient descent method.


# Importing the necessary library for numerical operations
import numpy as np

#Initialize input(XOR)
input_values = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0,], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
target_outputs = np.array([0, 0, 0, 1, 0, 1, 1, 1])

# Initialize parameters
np.random.seed(1) #fix a randomly generated number(provide same random value) in every run. (i.e seed(1))
inputlayer_size = 3
hiddenlayer1_size = 2
hiddenlayer2_size = 2
outputlayer_size = 1

#Initialize weights and bias
Weight_inputlayer_hiddenlayer1 = np.random.uniform(-1, 1, (hiddenlayer1_size, inputlayer_size))
bias_hiddenlayer1 = np.random.uniform(-1, 1, (hiddenlayer1_size, 1))
Weight_hiddenlayer1_hiddenlayer2 = np.random.uniform(-1, 1, (hiddenlayer2_size, hiddenlayer1_size))
bias_hiddenlayer2 = np.random.uniform(-1, 1, (hiddenlayer2_size, 1))
Weight_hiddenlayer2_outputlayer = np.random.uniform(-1, 1, (outputlayer_size, hiddenlayer2_size))
bias_outputlayer = np.random.uniform(-1, 1, (outputlayer_size, 1))
print("weights:")
print(Weight_inputlayer_hiddenlayer1)
print(Weight_hiddenlayer1_hiddenlayer2)
print(Weight_hiddenlayer2_outputlayer)
print("bias:")
print(bias_hiddenlayer1)
print(bias_hiddenlayer2)
print(bias_outputlayer)


#learning rate
learning_rate = 0.5
epochs = 10000
a=1 # Sigmoid slope paramete


#Implement Backpropagation algorithm
#foward phase
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}")

    # Initialize gradient accumulators for batch update at the beginning of each epoch
    d_Weight_hiddenlayer2_outputlayer = np.zeros_like(Weight_hiddenlayer2_outputlayer)
    d_bias_outputlayer = np.zeros_like(bias_outputlayer)
    d_Weight_hiddenlayer1_hiddenlayer2 = np.zeros_like(Weight_hiddenlayer1_hiddenlayer2)
    d_bias_hiddenlayer2 = np.zeros_like(bias_hiddenlayer2)
    d_Weight_inputlayer_hiddenlayer1 = np.zeros_like(Weight_inputlayer_hiddenlayer1)
    d_bias_hiddenlayer1 = np.zeros_like(bias_hiddenlayer1)


# Online learning - process each sample individually
    for i in range(len(input_values)):
# Get current input and target
        x = input_values[i].reshape(-1, 1)
        # Reshape input to column vector (2x1)
        # Gets the i-th input (e.g., [0, 0] at the begining )
        target = np.array([target_outputs[i]]).reshape(-1, 1)
        # Reshape target to column vector (1x1)
        # Gets the i-th input (e.g., [0] at the begining )


        # Forward pass to hidden layer
        # calculate the weighted sum with bias of niddenlayer1 (z = w1*x1 + w2*x2 + bias)
        hiddenlayer1_weighted_sum_with_bias = np.dot(Weight_inputlayer_hiddenlayer1, x) + bias_hiddenlayer1
        # Apply sigmoid activation
        hiddenlayer1_niddenlayer2 = 1 / (1 + np.exp(- a * hiddenlayer1_weighted_sum_with_bias))
        # Forward pass to hiddenlayer2
        # calculate the weighted sum with bias of hiddenlayer2 (z = w1*x1 + w2*x2 + bias)
        hiddenlayer2_weighted_sum_with_bias = np.dot(Weight_hiddenlayer1_hiddenlayer2, hiddenlayer1_niddenlayer2) + bias_hiddenlayer2
        # Apply sigmoid activation
        hiddenlayer2_output = 1 / (1 + np.exp(- a * hiddenlayer2_weighted_sum_with_bias))
        # Forward pass to output layer
        # calculate the weighted sum with bias of output layer(z = w1*x1 + w2*x2 + bias)
        outputlayer_weighted_sum_with_bias = np.dot(Weight_hiddenlayer2_outputlayer, hiddenlayer2_output) + bias_outputlayer
        # Apply sigmoid activation
        predicted_output = 1 / (1 + np.exp(- a * outputlayer_weighted_sum_with_bias))

        # Calculate error (Mean Squared Error)
        error = 0.5 * (target - predicted_output) ** 2
        print(f"Input: {x.T}, Output: {predicted_output[0,0]:.4f}, Target: {target[0,0]}")

        # Backward pass (Backpropagation)
        # Calculate outputlayer error gradient
        output_layer_error_gradient = (target - predicted_output) * ( a * predicted_output * (1 - predicted_output))
        # Calculate hiddenlayer 2 error gradient
        hidden_layer2_error_gradient = np.dot(Weight_hiddenlayer2_outputlayer.T, output_layer_error_gradient) * (a * hiddenlayer2_output * (1 - hiddenlayer2_output))
        # Calculate hiddenlayer 1 error gradient
        hidden_layer1_error_gradient = np.dot(Weight_hiddenlayer1_hiddenlayer2.T, hidden_layer2_error_gradient) * (a * hiddenlayer1_niddenlayer2 * (1 - hiddenlayer1_niddenlayer2))


        # Accumulate gradients for batch update
        d_Weight_hiddenlayer2_outputlayer += np.dot(output_layer_error_gradient, hiddenlayer2_output.T)
        d_bias_outputlayer += output_layer_error_gradient
        d_Weight_hiddenlayer1_hiddenlayer2 += np.dot(hidden_layer2_error_gradient, hiddenlayer1_niddenlayer2.T)
        d_bias_hiddenlayer2 += hidden_layer2_error_gradient
        d_Weight_inputlayer_hiddenlayer1 += np.dot(hidden_layer1_error_gradient, x.T)
        d_bias_hiddenlayer1 += hidden_layer1_error_gradient




        # Average gradients and update weights (batch update)
        batch_size = len(input_values)
        Weight_hiddenlayer2_outputlayer += (learning_rate / batch_size) * d_Weight_hiddenlayer2_outputlayer
        bias_outputlayer += (learning_rate / batch_size) * d_bias_outputlayer
        Weight_hiddenlayer1_hiddenlayer2 += (learning_rate / batch_size) * d_Weight_hiddenlayer1_hiddenlayer2
        bias_hiddenlayer2 += (learning_rate / batch_size) * d_bias_hiddenlayer2
        Weight_inputlayer_hiddenlayer1 += (learning_rate / batch_size) * d_Weight_inputlayer_hiddenlayer1
        bias_hiddenlayer1 += (learning_rate / batch_size) * d_bias_hiddenlayer1





# After training, test the network
print("\nTesting the trained network:")
for i in range(len(input_values)):
    x = input_values[i].reshape(-1, 1)

     # Forward pass only
    hidden_layer1_weighted_sum_with_bias = np.dot(Weight_inputlayer_hiddenlayer1, x) + bias_hiddenlayer1
    hidden_layer1_output = 1 / (1 + np.exp(- a * hidden_layer1_weighted_sum_with_bias))
    hidden_layer2_weighted_sum_with_bias = np.dot(Weight_hiddenlayer1_hiddenlayer2, hidden_layer1_output) + bias_hiddenlayer2
    hidden_layer2_output = 1 / (1 + np.exp(- a * hidden_layer2_weighted_sum_with_bias))
    output_layer_weighted_sum_with_bias = np.dot(Weight_hiddenlayer2_outputlayer, hidden_layer2_output) + bias_outputlayer
    predicted_output = 1 / (1 + np.exp(- a * output_layer_weighted_sum_with_bias))

    # Round to nearest integer (0 or 1)
    predicted_class = 1 if predicted_output > 0.5 else 0
    print(f"Input: {x.T}, Output: {predicted_output[0,0]:.4f}, Predicted: {predicted_class}, Target_output: {target_outputs[i]}")



```

## Tag
#assignment #NN 