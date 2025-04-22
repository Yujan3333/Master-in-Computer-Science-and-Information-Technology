## [Exponential Kernel](Exponential%20Kernel.md)

The Exponential kernel is defined as: K(x, y) = exp(-||x - y|| / σ)

Key characteristics:

- Uses the L1 norm (Manhattan distance)
- Linear decay with distance
- Also called the Laplacian kernel
- Less smooth than Gaussian kernel
- Has sharper peaks at the center points

## [[Gaussian Kernel]]

The Gaussian kernel is defined as: K(x, y) = exp(-||x - y||² / (2σ²))

Key characteristics:

- Uses the L2 norm (Euclidean distance)
- Squared distance in the exponent
- Creates smoother, bell-shaped curves
- More commonly used in practice
- Decays faster as you move away from center

## Visual Comparison
The main difference is in how they decay with distance:
- Exponential kernel: linear decay rate (first-power)
- Gaussian kernel: quadratic decay rate (squared)

==This means:==
- The Gaussian kernel falls off more quickly as you move away from the center
- The Exponential kernel has "fatter tails" and maintains influence over a greater distance