
### ✍️ Logistic Regression – 1 Epoch Summary

![](../../../../../../../../Images/First_Sem_Images/Numerical%20Logistic%20Regression.png)

![](../../../../../../../../Images/First_Sem_Images/Numerical%20Logistic%20Regression-1.png)

**Training Samples:**

```
(0.78, 0.69, 1)
(0.67, 1.00, 1)
(0.00, 0.00, 0)
(0.22, 0.14, 0)
```

**Initial Weights:**

```
w₀ = 0, w₁ = 0, w₂ = 0
```

**Sigmoid Output for all:**

```
ŷ = σ(0) = 0.5
```

**Errors:**

```
Sample 1: -0.5
Sample 2: -0.5
Sample 3:  0.5
Sample 4:  0.5
```

**Gradients (α = 0.1):**

```
∂J/∂w₀ = 0
∂J/∂w₁ = -0.615
∂J/∂w₂ = -0.775
```

**Updated Weights:**

```
w₀ = 0
w₁ = 0.0615
w₂ = 0.0775
```

✅ **New model equation:**

$$
y = 0 + 0.0615x_1 + 0.0775x_2
$$

---

