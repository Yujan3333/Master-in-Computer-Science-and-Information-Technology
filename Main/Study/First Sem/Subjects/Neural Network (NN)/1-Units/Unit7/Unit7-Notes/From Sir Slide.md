RNN have a “memory” which remembers all information about what has been calculated. It uses the same parameters for each input as it performs the same task on all the inputs or hidden states to produce the output. 
> [!info] [Understanding This](Understanding%20This.md) 

Thus, RNN converts the independent activations into dependent activations by providing the same weights and biases to all the layers, thus reducing the complexity of increasing parameters and memorizing each previous outputs by giving each output as input to the next hidden layer (see right part of the figure in next slide).
Hence layers of neural network in right side can be joined together such that the weights and bias of all the hidden layers is the same, into a single recurrent layer.
> [Understanding 2](Understanding%202.md)

