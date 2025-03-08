Write a python program to create a neuron and predict its output using the threshold activation function

Things to focus
$$ u_k = \sum_{j=1}^{n} x_j * w_{kj} $$
$$ v_k = u_k + b_k $$
$$ y_k = \varphi(u_k + b_k) = \varphi(v_k) $$
---
Here,
$u_k$ -> Weighted sum of input
$v_k$ -> net input
$y_k$ -> Output
$x_j$ -> Input
$w_{kj}$ -> Weight of *$k^{th}$* neuron
