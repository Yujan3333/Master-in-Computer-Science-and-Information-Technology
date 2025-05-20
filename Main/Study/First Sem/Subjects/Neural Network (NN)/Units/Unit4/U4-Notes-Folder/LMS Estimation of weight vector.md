**Least Mean Square**

- **N**: Number of input samples in the training set.
- **M**: Number of hidden layer neurons (output from the hidden layer).
- **C**: Number of output neurons (i.e., classes in classification).

The output from the hidden layer for input $x_i$ is denoted by  $\phi_j(x_i)$ 

$\phi_j(\mathbf{x}_i) = \phi_{ji}$

![](../../../../../../../Images/LMS%20Estimation%20of%20weight%20vector2.png)
#### matrix
![](../../../../../../../Images/LMS%20Estimation%20of%20weight%20vector1.png)
The meaning of this is that the goal is to find the **weight** ( $w_{kj}$ ) , Such that the neural network produces output close to the desired output values $d_{kj}$ 

---
- $d_{kj}$ = 1 if $x_j$ ∈ $H_k$ (meaning if input $x_j$ belongs to class k)
- $d_{kj}$ = -1 if $x_j$ ∉ $H_k$ (if input $x_j$ doesn't belong to class k)
![](../../../../../../../Images/LMS%20Estimation%20of%20weight%20vector-1.png)

---
This [matrix](#matrix) equation can be written as:
$\varphi_{ji} w_{kj} = d_{ki}, \quad i=1,\dots,N, j=1,\dots,M, k=1,\dots,C$

![](../../../../../../../Images/LMS%20Estimation%20of%20weight%20vector3.png)
 
 ***This is the perfect condition*** 
 
 The equation,
 
  $φ_{ji}·w_{kj} = d_{ki}$ represents the ideal case where the network *perfectly maps* inputs to desired outputs
 
---
#### Error
"*if the network isn't properly trained, this equation won't be satisfied* " it means that in practice, there will be some error between what the network produces and what's desired

$e = \varphi \; w_k - d_k$

![](../../../../../../../Images/LMS%20Estimation%20of%20weight%20vector.png)
Here, 
	$φ \; w_{k}$ represents the actual output from the network for class k
	$d_k$ represents the desired output for class k
	This error will be *minimized* during training using the LMS approach

---
