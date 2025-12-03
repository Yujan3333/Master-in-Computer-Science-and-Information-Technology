![](../../../../../../../Images/Second_Sem_Images/Linear%20Regression%20SGD%20and%20BGD%20with%20two%20x%20-%20Numerical%20Answer.png)

---
# Answer
We’ll use the **same dataset** and **initial weights**: $w_0=0, w_1=0, w_2=0$ with learning rate $\alpha=0.1$.
SGD updates **after each sample**.

---

## Stochastic Gradient Descent (SGD) – Two Epochs

### Epoch 1

**Step 1 (sample 1: $x_1=1, x_2=1, y=3$)**

Predicted:
$\hat y = 0 + 0\cdot1 + 0\cdot1 = 0$

Error:
$e = 3 - 0 = 3$

Update weights:
$w_0 \leftarrow 0 + 0.1\cdot 3 = 0.3$
$w_1 \leftarrow 0 + 0.1\cdot 3\cdot 1 = 0.3$
$w_2 \leftarrow 0 + 0.1\cdot 3\cdot 1 = 0.3$

**Step 2 (sample 2: $x_1=2, x_2=1, y=5$)**

Predicted:
$\hat y = 0.3 + 0.3\cdot2 + 0.3\cdot1 = 0.3 + 0.6 + 0.3 = 1.2$

Error:
$e = 5 - 1.2 = 3.8$

Update weights:
$w_0 \leftarrow 0.3 + 0.1\cdot3.8 = 0.68$
$w_1 \leftarrow 0.3 + 0.1\cdot3.8\cdot2 = 1.06$
$w_2 \leftarrow 0.3 + 0.1\cdot3.8\cdot1 = 0.68$

**Step 3 (sample 3: $x_1=1, x_2=2, y=2$)**

Predicted:
$\hat y = 0.68 + 1.06\cdot1 + 0.68\cdot2 = 0.68 + 1.06 + 1.36 = 3.10$

Error:
$e = 2 - 3.10 = -1.10$

Update weights:
$w_0 \leftarrow 0.68 + 0.1\cdot(-1.10) = 0.57$
$w_1 \leftarrow 1.06 + 0.1\cdot(-1.10)\cdot1 = 0.95$
$w_2 \leftarrow 0.68 + 0.1\cdot(-1.10)\cdot2 = 0.46$

**Step 4 (sample 4: $x_1=3, x_2=3, y=5$)**

Predicted:
$\hat y = 0.57 + 0.95\cdot3 + 0.46\cdot3 = 0.57 + 2.85 + 1.38 = 4.80$

Error:
$e = 5 - 4.80 = 0.20$

Update weights:
$w_0 \leftarrow 0.57 + 0.1\cdot0.20 = 0.59$
$w_1 \leftarrow 0.95 + 0.1\cdot0.20\cdot3 = 1.01$
$w_2 \leftarrow 0.46 + 0.1\cdot0.20\cdot3 = 0.52$

**After Epoch 1:** $w_0 \approx 0.59,\ w_1 \approx 1.01,\ w_2 \approx 0.52$

---

### Epoch 2

**Step 1 (sample 1)**

Predicted:
$\hat y = 0.59 + 1.01\cdot1 + 0.52\cdot1 = 0.59 + 1.01 + 0.52 = 2.12$

Error:
$e = 3 - 2.12 = 0.88$

Update weights:
$w_0 \leftarrow 0.59 + 0.1\cdot0.88 = 0.678$
$w_1 \leftarrow 1.01 + 0.1\cdot0.88\cdot1 = 1.098$
$w_2 \leftarrow 0.52 + 0.1\cdot0.88\cdot1 = 0.608$

**Step 2 (sample 2)**

Predicted:
$\hat y = 0.678 + 1.098\cdot2 + 0.608\cdot1 = 0.678 + 2.196 + 0.608 = 3.482$

Error:
$e = 5 - 3.482 = 1.518$

Update weights:
$w_0 \leftarrow 0.678 + 0.1\cdot1.518 = 0.8298$
$w_1 \leftarrow 1.098 + 0.1\cdot1.518\cdot2 = 1.4016$
$w_2 \leftarrow 0.608 + 0.1\cdot1.518\cdot1 = 0.7598$

**Step 3 (sample 3)**

Predicted:
$\hat y = 0.8298 + 1.4016\cdot1 + 0.7598\cdot2 = 0.8298 + 1.4016 + 1.5196 = 3.750$

Error:
$e = 2 - 3.750 = -1.750$

Update weights:
$w_0 \leftarrow 0.8298 + 0.1\cdot(-1.750) = 0.6548$
$w_1 \leftarrow 1.4016 + 0.1\cdot(-1.750)\cdot1 = 1.2266$
$w_2 \leftarrow 0.7598 + 0.1\cdot(-1.750)\cdot2 = 0.4098$

**Step 4 (sample 4)**

Predicted:
$\hat y = 0.6548 + 1.2266\cdot3 + 0.4098\cdot3 = 0.6548 + 3.6798 + 1.2294 = 5.564$

Error:
$e = 5 - 5.564 = -0.564$

Update weights:
$w_0 \leftarrow 0.6548 + 0.1\cdot(-0.564) = 0.5984$
$w_1 \leftarrow 1.2266 + 0.1\cdot(-0.564)\cdot3 = 1.0584$
$w_2 \leftarrow 0.4098 + 0.1\cdot(-0.564)\cdot3 = 0.2370$

**After Epoch 2:** $w_0 \approx 0.598,\ w_1 \approx 1.058,\ w_2 \approx 0.237$

---
---
## Batch Gradient Descent (BGD) – Two Epochs

### Epoch 1:

#### Predictions:
$\hat y^{(i)} = 0$ for all $i$

#### Errors:
$e^{(1)}=3,\ e^{(2)}=5,\ e^{(3)}=2,\ e^{(4)}=5$

#### Compute sums:
$\sum_i e^{(i)} = 3+5+2+5 = 15$

$\sum_i e^{(i)} x_1^{(i)} = 3\cdot1 + 5\cdot2 + 2\cdot1 + 5\cdot3 = 3 + 10 + 2 + 15 = 30$

$\sum_i e^{(i)} x_2^{(i)} = 3\cdot1 + 5\cdot1 + 2\cdot2 + 5\cdot3 = 3 + 5 + 4 + 15 = 27$

#### Means:
$\frac{1}{n}\sum_i e^{(i)} = 15/4 = 3.75$
$\frac{1}{n}\sum_i e^{(i)} x_1^{(i)} = 30/4 = 7.5$
$\frac{1}{n}\sum_i e^{(i)} x_2^{(i)} = 27/4 = 6.75$

#### Update weights:
$w_0 \leftarrow 0 + 0.1 \cdot 3.75 = 0.375$
$w_1 \leftarrow 0 + 0.1 \cdot 7.5 = 0.75$
$w_2 \leftarrow 0 + 0.1 \cdot 6.75 = 0.675$

After Epoch 1: $w_0 = 0.375,\ w_1 = 0.75,\ w_2 = 0.675$

### Epoch 2:

#### New predictions:
$\hat y^{(1)} = 0.375 + 0.75\cdot1 + 0.675\cdot1 = 1.8$
$\hat y^{(2)} = 0.375 + 0.75\cdot2 + 0.675\cdot1 = 2.55$
$\hat y^{(3)} = 0.375 + 0.75\cdot1 + 0.675\cdot2 = 2.475$
$\hat y^{(4)} = 0.375 + 0.75\cdot3 + 0.675\cdot3 = 5.4$

#### Errors:
$e^{(1)} = 3 - 1.8 = 1.2$
$e^{(2)} = 5 - 2.55 = 2.45$
$e^{(3)} = 2 - 2.475 = -0.475$
$e^{(4)} = 5 - 5.4 = -0.4$

#### Sums:
$\sum_i e^{(i)} = 1.2 + 2.45 - 0.475 - 0.4 = 2.775$
$\sum_i e^{(i)} x_1^{(i)} = 1.2\cdot1 + 2.45\cdot2 - 0.475\cdot1 -0.4\cdot3 = 1.2+4.9-0.475-1.2=4.425$
$\sum_i e^{(i)} x_2^{(i)} = 1.2\cdot1 + 2.45\cdot1 -0.475\cdot2 -0.4\cdot3 = 1.2+2.45-0.95-1.2=1.5$

#### Means:
$\frac{1}{n}\sum_i e^{(i)} = 2.775/4 = 0.69375$
$\frac{1}{n}\sum_i e^{(i)} x_1^{(i)} = 4.425/4 = 1.10625$
$\frac{1}{n}\sum_i e^{(i)} x_2^{(i)} = 1.5/4 = 0.375$

#### Update weights:
$w_0 \leftarrow 0.375 + 0.1 \cdot 0.69375 = 0.444375$
$w_1 \leftarrow 0.75 + 0.1 \cdot 1.10625 = 0.860625$
$w_2 \leftarrow 0.675 + 0.1 \cdot 0.375 = 0.7125$

After Epoch 2: $w_0 \approx 0.4444,\ w_1 \approx 0.8606,\ w_2 \approx 0.7125$

---
---

## Batch Gradient Descent (BGD) – Two Epochs In Tabular

**Initial weights:** $w_0 = 0,\ w_1 = 0,\ w_2 = 0$
**Learning rate:** $\alpha = 0.1$

| Epoch | $\hat y^{(1)}$ | $\hat y^{(2)}$ | $\hat y^{(3)}$ | $\hat y^{(4)}$ | $\sum e^{(i)}$ | $\sum e^{(i)} x_1^{(i)}$ | $\sum e^{(i)} x_2^{(i)}$ | $w_0$  | $w_1$  | $w_2$  |
| ----- | -------------- | -------------- | -------------- | -------------- | -------------- | ------------------------ | ------------------------ | ------ | ------ | ------ |
| 1     | 0              | 0              | 0              | 0              | 15             | 30                       | 27                       | 0.375  | 0.75   | 0.675  |
| 2     | 1.8            | 2.55           | 2.475          | 5.4            | 2.775          | 4.425                    | 1.5                      | 0.4444 | 0.8606 | 0.7125 |

**Notes:**

* $\hat y^{(i)} = w_0 + w_1 x_1^{(i)} + w_2 x_2^{(i)}$
* $e^{(i)} = y^{(i)} - \hat y^{(i)}$
* Weight update (BGD): $w_j \leftarrow w_j + \alpha \frac{1}{n} \sum_i e^{(i)} x_j^{(i)}$, with $x_0^{(i)} = 1$

✅ **After 2 epochs:** $w_0 \approx 0.4444,\ w_1 \approx 0.8606,\ w_2 \approx 0.7125$

---

## Stochastic Gradient Descent (SGD) – Two Epochs In Tabular
 
**Initial weights:** $w_0 = 0,\ w_1 = 0,\ w_2 = 0$
**Learning rate:** $\alpha = 0.1$

| Epoch | Sample | $x_1,x_2,y$ | $\hat y$ | $e$    | $w_0$ | $w_1$ | $w_2$ |
| ----- | ------ | ----------- | -------- | ------ | ----- | ----- | ----- |
| 1     | 1      | 1,1,3       | 0        | 3      | 0.3   | 0.3   | 0.3   |
| 1     | 2      | 2,1,5       | 1.5      | 3.5    | 0.65  | 1.0   | 0.65  |
| 1     | 3      | 1,2,2       | 2.95     | -0.95  | 0.555 | 0.905 | 0.46  |
| 1     | 4      | 3,3,5       | 5.01     | -0.01  | 0.554 | 0.902 | 0.457 |
| 2     | 1      | 1,1,3       | 1.913    | 1.087  | 0.662 | 1.011 | 0.565 |
| 2     | 2      | 2,1,5       | 3.249    | 1.751  | 0.837 | 1.361 | 0.740 |
| 2     | 3      | 1,2,2       | 3.617    | -1.617 | 0.675 | 1.199 | 0.417 |
| 2     | 4      | 3,3,5       | 5.403    | -0.403 | 0.635 | 1.078 | 0.296 |

✅ **After 2 epochs:** $w_0 \approx 0.635,\ w_1 \approx 1.078,\ w_2 \approx 0.296$

---

You can see the **key difference**:

* **BGD:** updates once per epoch → smoother, smaller steps.
* **SGD:** updates after each sample → faster, more “jumpy” but can converge quicker.

---
