- XOR problem cannot be solved by *Single Layer Perceptron* because it is *not linearly separable*
- ==TO SOLVE:== Multi Layer Perceptron (**MLP**) - hidden layer
- ==Alternative== : XOR problem using Radial Basis Function (RBF)
---
### Changing the Coordinates of XOR
#### Two Centers
**c1=(0,0) and c2=(1,1)**

#### Formulae
$\varphi_1(x) = \exp(-\|x - c_1\|^2)$
$\varphi_2(x) = \exp(-\|x - c_2\|^2)$

#### To Update
[[U4-Notes/XOR problem using RBF -Numerical Done By Sir]]

---
After this we get the transformed input for the XOR inputs and they can be linearly separable as well.
![](../../../../../../../Images/XOR%20Problem%20with%20Radial%20Basis%20Function.png)

### Exercise
- [Solve the XOR problem using RBF by taking (1,0) and (0,1) as centers](U4-Notes/Solve%20the%20XOR%20problem%20using%20RBF%20by%20taking%20(1,0)%20and%20(0,1)%20as%20centers.md).
- [Solve the XOR problem using RBF such that transform 2D data points into 4D data points by taking each of the data point as center. ](U4-Notes/Solve%20the%20XOR%20problem%20using%20RBF%20such%20that%20transform%202D%20data%20points%20into%204D%20data%20points%20by%20taking%20each%20of%20the%20data%20point%20as%20center.%20.md)

(Hint use the RBF below) 

$$\varphi(x) = \exp(-\|x - c_1\|^2) / 2$$
