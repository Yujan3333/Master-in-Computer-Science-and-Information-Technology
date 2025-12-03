![](../../../../../../../Images/Second_Sem_Images/Linear%20Regression%20BGD%20-%20Numerical%20Answer.png)

---

# Batch Gradient Descent Example (Two Epochs)

**Data:** $(x,y)=(1,3),(2,5),(3,7),(4,9),\ n=4$
**Initial weights:** $w_0=0, w_1=0$
**Learning rate:** $\alpha=0.1$
**Loss function:** $E=\dfrac{1}{2n}\sum_{i=1}^n (y^{(i)}-\hat y^{(i)})^2,\quad \hat y^{(i)}=w_0+w_1 x^{(i)}$
**BGD update:**
$w_0 \leftarrow w_0 + \alpha\cdot\frac{1}{n}\sum_{i} e^{(i)},\quad w_1 \leftarrow w_1 + \alpha\cdot\frac{1}{n}\sum_{i} e^{(i)}x^{(i)},\quad e^{(i)}=y^{(i)}-\hat y^{(i)}$

---

## Epoch 1

**Predictions:** $\hat y^{(i)}=0$ for all $i$
**Errors:** $e^{(i)} = y^{(i)} - \hat y^{(i)} = [3, 5, 7, 9]$

**Sums:**
$\sum_i e^{(i)} = 3+5+7+9 = 24$
$\sum_i e^{(i)} x^{(i)} = 3\cdot1 + 5\cdot2 + 7\cdot3 + 9\cdot4 = 70$

**Means:**
$\frac{1}{n}\sum_i e^{(i)} = 6.0$
$\frac{1}{n}\sum_i e^{(i)} x^{(i)} = 17.5$

**Updates:**
$w_0 \leftarrow 0 + 0.1 \times 6.0 = 0.6$
$w_1 \leftarrow 0 + 0.1 \times 17.5 = 1.75$

**After Epoch 1:** $w_0 = 0.6,\ w_1 = 1.75$

---

## Epoch 2

**Predictions:**
$\hat y^{(1)} = 0.6 + 1.75\cdot1 = 2.35$
$\hat y^{(2)} = 0.6 + 1.75\cdot2 = 4.10$
$\hat y^{(3)} = 0.6 + 1.75\cdot3 = 5.85$
$\hat y^{(4)} = 0.6 + 1.75\cdot4 = 7.60$

**Errors:**
$e^{(1)} = 0.65,\ e^{(2)} = 0.90,\ e^{(3)} = 1.15,\ e^{(4)} = 1.40$

**Sums:**
$\sum_i e^{(i)} = 4.10$
$\sum_i e^{(i)} x^{(i)} = 11.50$

**Means:**
$\frac{1}{n}\sum_i e^{(i)} = 1.025$
$\frac{1}{n}\sum_i e^{(i)} x^{(i)} = 2.875$

**Updates:**
$w_0 \leftarrow 0.6 + 0.1 \times 1.025 = 0.7025$
$w_1 \leftarrow 1.75 + 0.1 \times 2.875 = 2.0375$

**After Epoch 2:** $w_0 \approx 0.7025,\ w_1 \approx 2.0375$

---

## Remarks

* True perfect fit: $y = 1 + 2x$ $(w_0=1, w_1=2)$
* After 2 BGD epochs with $\alpha=0.1$, we are close: $w_0 \approx 0.7025,\ w_1 \approx 2.0375$
* Convergence can be sped up by increasing $\alpha$ or running more epochs (but too large $\alpha$ may diverge)

---

