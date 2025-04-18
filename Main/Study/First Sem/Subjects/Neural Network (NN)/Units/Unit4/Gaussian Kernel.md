### Radial Basis Function Kernel (RBF)
- Also Known as **Gaussian kernel**
- Most widely used Kernel function

It operates by measuring the similarity between data points based on their Euclidean distance in the input space.
##### Gaussian kernel function - formula

$$
k(x, y) = \exp\left( -\frac{\lVert x - y \rVert^2}{2\sigma^2} \right), \text{ where } \sigma \text{ is free parameter}
$$

Where:
- $\lVert x - y \rVert^2$ represents the squared Euclidean distance between the two data points.
- $\sigma$ is a parameter known as the bandwidth or width of the kernel, controlling the smoothness of the decision boundary.


##### Exponential Kernel Function - formula
$$
k(x, y) = \exp\left( -\frac{\lVert x - y \rVert}{2\sigma^2} \right)
$$

---

