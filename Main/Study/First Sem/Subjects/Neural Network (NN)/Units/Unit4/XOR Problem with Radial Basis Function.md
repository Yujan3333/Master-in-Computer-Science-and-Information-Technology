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

---
After this we get the transformed input for the XOR inputs and they can be linearly separable as well.
![](../../../../../../Images/XOR%20Problem%20with%20Radial%20Basis%20Function.png)