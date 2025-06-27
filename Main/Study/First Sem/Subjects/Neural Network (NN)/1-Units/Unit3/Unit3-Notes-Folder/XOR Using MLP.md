### Questions
- Realize NOT and NAND function using perceptron.
- Can we realize XNOR function using perceptron? If yes, realize it using perceptron. Otherwise, realize XNOR function using MLP.
- [NOT and NAND Can While XNOR Cannot](NOT%20and%20NAND%20Can%20While%20XNOR%20Cannot.md)



## **XOR Decomposition:**
**XOR(x1,x2) = NOR(AND(x1,x2), NOR(x1,x2))**

This means:
- First layer: Compute AND(x1,x2) and NOR(x1,x2)
- Second layer: Apply NOR to those results

## **MLP Architecture for XOR:**

**Layer 1 (Hidden Layer) - 2 neurons:**
- **Neuron 1:** Implements AND(x1,x2)
  - w11 = 1, w12 = 1, b1 = -1.5
- **Neuron 2:** Implements NOR(x1,x2)  
  - w21 = -1, w22 = -1, b2 = 0.5

**Layer 2 (Output Layer) - 1 neuron:**
- **Output neuron:** Implements NOR of hidden layer outputs
  - w1 = -1, w2 = -1, b = 0.5

## **Weight Matrix Representation:**

**Hidden Layer Weights:**
```
W1 = [[ 1,  1],    # AND neuron
      [-1, -1]]    # NOR neuron

b1 = [-1.5,        # AND bias
       0.5]        # NOR bias
```

**Output Layer Weights:**
```
W2 = [[-1, -1]]    # NOR of hidden outputs

b2 = [0.5]         # Output bias
```

## **Verification:**
- (0,0): AND=0, NOR=1 → NOR(0,1)=0 ✓
- (0,1): AND=0, NOR=0 → NOR(0,0)=1 ✓  
- (1,0): AND=0, NOR=0 → NOR(0,0)=1 ✓
- (1,1): AND=1, NOR=0 → NOR(1,0)=0 ✓

This decomposition shows why XOR requires at least 2 hidden neurons - you need both AND and NOR functions computed simultaneously!