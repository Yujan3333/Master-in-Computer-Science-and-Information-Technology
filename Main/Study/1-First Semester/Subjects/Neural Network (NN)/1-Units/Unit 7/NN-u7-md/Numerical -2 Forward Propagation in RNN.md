![](../../../../../../../../Images/First_Sem_Images/Numerical%20-2%20-%20feed%20forward%20%20propagation%20in%20RNN.png)


---

## ✅ **Given Parameters**

* Input series: {0.2, 0.4, 0.6, 0.8}
* Initial hidden state:
  $\mathbf{h}_0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$
* Hidden layer: 2 nodes, sigmoid activation
  $\sigma(x) = \frac{1}{1 + e^{-x}}$
* Output layer: 1 node, **linear activation**

### Weight Matrices:

* $W_{hh} = \begin{bmatrix} 0.1 & 0.5 \\ 0.5 & 0.9 \end{bmatrix}$
* $W_{xh} = \begin{bmatrix} 0.6 \\ 0.2 \end{bmatrix}$
* $W_{hy} = \begin{bmatrix} 0.4 & 0.7 \end{bmatrix}$

---

## 🔄 **Time Step-by-Step Calculations**

---

### ⏱ **Time Step 1**: $x_1 = 0.2$

#### Hidden State $h_1$

$$
W_{hh} \cdot h_0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}, \quad
W_{xh} \cdot x_1 = 0.2 \cdot \begin{bmatrix} 0.6 \\ 0.2 \end{bmatrix} = \begin{bmatrix} 0.12 \\ 0.04 \end{bmatrix}
$$

$$
z_1 = \begin{bmatrix} 0.12 \\ 0.04 \end{bmatrix}, \quad
h_1 = \sigma(z_1) \approx \begin{bmatrix} 0.529964 \\ 0.509998 \end{bmatrix}
$$

#### Output $y_1$

$$
y_1 = W_{hy} \cdot h_1 = 0.4 \cdot 0.529964 + 0.7 \cdot 0.509998 = \boxed{0.568992}
$$

---

### ⏱ **Time Step 2**: $x_2 = 0.4$

#### Hidden State $h_2$

$$
W_{hh} \cdot h_1 =
\begin{bmatrix}
0.1 \cdot 0.529964 + 0.5 \cdot 0.509998 \\
0.5 \cdot 0.529964 + 0.9 \cdot 0.509998
\end{bmatrix}
= \begin{bmatrix} 0.307962 \\ 0.723964 \end{bmatrix}
$$

$$
W_{xh} \cdot x_2 = 0.4 \cdot \begin{bmatrix} 0.6 \\ 0.2 \end{bmatrix} = \begin{bmatrix} 0.24 \\ 0.08 \end{bmatrix}
$$

$$
z_2 = \begin{bmatrix} 0.547962 \\ 0.803964 \end{bmatrix}, \quad
h_2 = \sigma(z_2) \approx \begin{bmatrix} 0.633200 \\ 0.690802 \end{bmatrix}
$$

#### Output $y_2$

$$
y_2 = 0.4 \cdot 0.633200 + 0.7 \cdot 0.690802 = \boxed{0.737961}
$$

---

### ⏱ **Time Step 3**: $x_3 = 0.6$

#### Hidden State $h_3$

$$
W_{hh} \cdot h_2 = 
\begin{bmatrix}
0.1 \cdot 0.6332 + 0.5 \cdot 0.6908 \\
0.5 \cdot 0.6332 + 0.9 \cdot 0.6908
\end{bmatrix}
= \begin{bmatrix} 0.40962 \\ 0.93934 \end{bmatrix}
$$

$$
W_{xh} \cdot x_3 = 0.6 \cdot \begin{bmatrix} 0.6 \\ 0.2 \end{bmatrix} = \begin{bmatrix} 0.36 \\ 0.12 \end{bmatrix}
$$

$$
z_3 = \begin{bmatrix} 0.76962 \\ 1.05934 \end{bmatrix}, \quad
h_3 = \sigma(z_3) \approx \begin{bmatrix} 0.683435 \\ 0.742552 \end{bmatrix}
$$

#### Output $y_3$

$$
y_3 = 0.4 \cdot 0.683435 + 0.7 \cdot 0.742552 = \boxed{0.793181}
$$

---

### ⏱ **Time Step 4**: $x_4 = 0.8$

#### Hidden State $h_4$

$$
W_{hh} \cdot h_3 =
\begin{bmatrix}
0.1 \cdot 0.683435 + 0.5 \cdot 0.742552 \\
0.5 \cdot 0.683435 + 0.9 \cdot 0.742552
\end{bmatrix}
= \begin{bmatrix} 0.43861 \\ 1.01033 \end{bmatrix}
$$

$$
W_{xh} \cdot x_4 = 0.8 \cdot \begin{bmatrix} 0.6 \\ 0.2 \end{bmatrix} = \begin{bmatrix} 0.48 \\ 0.16 \end{bmatrix}
$$

$$
z_4 = \begin{bmatrix} 0.91861 \\ 1.17033 \end{bmatrix}, \quad
h_4 = \sigma(z_4) \approx \begin{bmatrix} 0.714746 \\ 0.763187 \end{bmatrix}
$$

#### Output $y_4$

$$
y_4 = 0.4 \cdot 0.714746 + 0.7 \cdot 0.763187 = \boxed{0.819927}
$$

---

## ✅ **Final Summary Table**

| Time Step | Input $x_t$ | Hidden State $h_t$ | Output $y_t$ |
| --------- | ----------- | ------------------ | ------------ |
| 1         | 0.2         | \[0.530, 0.510]    | **0.569**    |
| 2         | 0.4         | \[0.633, 0.691]    | **0.738**    |
| 3         | 0.6         | \[0.683, 0.743]    | **0.793**    |
| 4         | 0.8         | \[0.715, 0.763]    | **0.820**    |

---

### 📌 Conclusion:

The RNN processes the input sequence step-by-step, carrying hidden state forward through time, and ends with a prediction of **approximately 0.820** after seeing input $x_4 = 0.8$.

---
