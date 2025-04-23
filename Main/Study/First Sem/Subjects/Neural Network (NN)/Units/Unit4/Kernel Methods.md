### What is Kernel Function?

Kernel Function is used to transform *n-dimensional input to m-dimensional input*, where m is much higher than n then find the dot product in higher dimensional efficiently. 

The main idea to use kernel is: A linear classifier or regression curve in higher dimensions becomes a Non-linear classifier or regression curve in lower dimensions.

![](../../../../../../Images/Kernel%20Methods.png)

---
#### Different Types of Kernel
- linear kernel
- Polynomial Kernel
- [Exponential Kernel](Exponential%20Kernel.md) [Example of Radial Basis Function Kernel]
- [Gaussian Kernel](Gaussian%20Kernel.md) [Example of Radial Basis Function Kernel]

##### [Difference between Exponential Kernel and Gaussian Kernel](Difference%20between%20Exponential%20Kernel%20and%20Gaussian%20Kernel.md)
---
#### [XOR Problem with Radial Basis Function](XOR%20Problem%20with%20Radial%20Basis%20Function.md)
- XOR problem cannot be solved by *Single Layer Perceptron* because it is *not linearly separable*
- 2 Questions from sir.

---
---
### Example from ChatGPT
- **Centers** = teachers in different classrooms.
    
- **Input point** = a student visiting those classrooms.
    
- **Gaussian bump** = how much the student pays attention in each classroom (most attention in the right classroom, less in others).
    
- **Output** = the student’s final grade, which is a mix of what each teacher taught (weights tell you how important each teacher is).

So in plain terms: an RBFNN measures “how close am I to each center?” turns those distances into “how much each neuron responds,” then just adds up those responses to make a prediction.

## Tag
#NN #RBFNN #kernel-function

## Ref
[Kernel Function RBFNN - Geeks](https://www.geeksforgeeks.org/radial-basis-function-kernel-machine-learning/#what-is-kernel-function)