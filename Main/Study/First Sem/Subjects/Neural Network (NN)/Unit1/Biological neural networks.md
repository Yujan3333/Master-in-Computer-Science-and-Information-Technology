ANN is inspired by the biological neural networks

Brain is a **highly complex, non-linear, and parallel computation system** that can perform computations **like perception, pattern recognition, motor control** etc. Neuron or nerve cell is the basic structural unit of brain.

#### Nerve Cell
![](../../../../../Images/Biological%20neural%20networks%20Fig.png)
#### Block diagram representation of nervous system 
![](../../../../../Images/Block%20diagram%20representation%20of%20nervous%20system.png)

#### 
![](../../../../../Images/Biological%20neural%20networks-%20Fig%20and%20ANN.png)

A *single layer* of perceptron's alone is unable to solve non-linear classification problems (such as [learning a simple XOR](https://www.quora.com/Why-cant-the-XOR-problem-be-solved-by-a-one-layer-perceptron) function). This problem can only be overcome (more complex relationships in data can only be modeled) by using multiple layers (hidden layers). However, there isn’t a simple, cheap way of training multiple layers of perceptron's, other than randomly nudging all their weights, because there is no way to tell which small set of changes would end up largely affecting other neurons’ outputs down the line.

**To solve the problem** artificial neurons would instead utilize continuous (floating point) values with continuous **activation functions** (more on these functions later). ==More on== [^1]
![](../../../../../Images/Biological%20neural%20networks%20-%20Activation%20Function%20Step%20Function%20and%20Sigmoid%20Function.png)

## ANN VS BNN



## Reference
[^1]: [Biological Vs ANN - Medium](https://medium.com/towards-data-science/the-differences-between-artificial-and-biological-neural-networks-a8b46db828b7)