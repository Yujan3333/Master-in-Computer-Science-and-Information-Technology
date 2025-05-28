#helper class for  layer
import math
import numpy as np

class neuron_layer():

  def __init__(self,number_of_neurons,number_of_inputs_per_neuron,layer_name="hidden layer",activation="sigmoid"):
    if not isinstance(number_of_neurons,int) or number_of_neurons < 1: raise Exception("Number of neurons must be an integer "+self.layer_name)
    if not isinstance(number_of_inputs_per_neuron,int) or number_of_inputs_per_neuron<1 : raise Exception("Number of inputs per neuron must be an integer "+self.layer_name)

    self.layer_name = layer_name

    self.weights = np.random.randn(number_of_neurons, number_of_inputs_per_neuron) * 0.1
    self.biases = np.random.randn(number_of_neurons) * 0.1
    self.number_of_neurons = number_of_neurons
    self.number_of_inputs_per_neuron = number_of_inputs_per_neuron

    if activation == "sigmoid":
      self.activation = lambda x:1/(1+np.exp(-x))
      self.activation_derivative = lambda y:y*(1-y)
    elif activation == "tanh":
      #tanh can cause vanshing gradient if all w=0 or all b =0
      self.activation = lambda x:np.tanh(x)
      self.activation_derivative = lambda y:1 - (y*y)
    else:
      raise Exception("Invalid Activation Function")

  def update_weights(self,delta_weights):
    delta_weights = np.array(delta_weights)
    if self.weights.shape != delta_weights.shape: raise Exception("Shape Mismatch In Neuron " +self.layer_name)
    self.weights = self.weights + delta_weights

  def update_biases(self, delta_biases):
    delta_biases = np.array(delta_biases)
    if self.biases.shape != delta_biases.shape: raise Exception("Shape Mismatch In Neuron " +self.layer_name,self.biases.shape,delta_biases.shape)
    self.biases = self.biases + delta_biases

  def predict_output(self,input:list):
    input = np.array(input)
    if input.shape != (self.number_of_inputs_per_neuron,): raise Exception("Shape Mismatch In Neuron " +self.layer_name)
    return np.array([self.activation(np.dot(w,input)+b) for w,b in zip(self.weights,self.biases)])

  def predict(self,input:list)->dict:
    
    input = np.array(input)
    if input.shape != (self.number_of_inputs_per_neuron,): raise Exception("Shape Mismatch In Neuron " +self.layer_name)

    outputs = np.array([self.activation(np.dot(w,input)+b) for w,b in zip(self.weights,self.biases)])
    derivatives = self.activation_derivative(outputs)
    return {
        "outputs": outputs,
        "derivatives": derivatives,
        "weights":self.weights.copy()
    }

