## Key Characters
-  Uses the L1 norm (*Manhattan distance*)
- Linear decay with distance
- Also called the Laplacian kernel
- Less smooth than Gaussian kernel
- Has sharper peaks at the center points

---
##### Exponential Kernel Function - formula
$$
k(x, y) = \exp\left( -\frac{\lVert x - y \rVert}{2\sigma^2} \right)
$$

---

Where:
- $\lVert x - y \rVert$ represents the squared Euclidean distance between the two data points.
- $\sigma$ is a parameter known as the bandwidth or width of the kernel, controlling the smoothness of the decision boundary.