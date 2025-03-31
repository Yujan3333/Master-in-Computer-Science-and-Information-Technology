import numpy as np

BIAS = 1
THRESHOLD = 5

class Neuron:
    def __init__(self,weights,bias,threshold=0):
        '''Initializing neuron with weights, bias, threshold(default is 0)'''
        # Changed the Python List to Array Easier to do calculation(dot prod) in Array
        self.weights = np.array(weights)
        self.bias = bias
        self.threshold = threshold

    
    def predict(self,inputs):
        '''Predicts if neuron will fire or not, depending on calculated weigthed sum and threshold function'''
        # Weighted sum = v in the slides
        # NumPy Library dot products(scalar product) of 1D array
        weighted_sum = np.dot(self.weights,inputs) + self.bias
        if weighted_sum > self.threshold:
            return 1
        return 0

# Prompting Input from the user
no_of_inputs = int(input("Enter the number of inputs of neuron: "))

# List of input(x)
inputs=[]
# List of Weight(w)
weights =[]

# Values of input(x) and weigths(w)
for i in range(0,no_of_inputs):
    x=float(input(f"Enter the value of Input x{i+1}: "))
    w=float(input(f"Enter the value of Weight w{i+1}: "))
    inputs.append(x)
    weights.append(w)

# Creating a object
neuron = Neuron(weights=weights,bias=BIAS,threshold=THRESHOLD)

# Final output of the ANN (y)
output = neuron.predict(inputs=inputs)

if output ==1:
    print(f"Neuron Fired. y={output}")
else:
    print(f"Neuron not Fired. y={output}")
