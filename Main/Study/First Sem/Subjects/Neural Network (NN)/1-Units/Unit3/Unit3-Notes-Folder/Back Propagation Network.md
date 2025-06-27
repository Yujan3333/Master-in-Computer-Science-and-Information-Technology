
Calculation of the forward phase and backward phase

Calculation the weight and bias Update.

| Aspect            | **Weight Update**                                              | **Bias Update**                                |
| ----------------- | -------------------------------------------------------------- | ---------------------------------------------- |
| Formula           | $w_{ij}^{\text{new}} = w_{ij} + \eta \cdot \delta_j \cdot o_i$ | $b_j^{\text{new}} = b_j + \eta \cdot \delta_j$ |
| Depends on input? | ✅ Yes (uses $o_i$)                                             | ❌ No                                           |
| Applied to        | Each input connection (edge)                                   | Each neuron (node)                             |
| Purpose           | Learns relationship between neurons                            | Shifts the activation function                 |
