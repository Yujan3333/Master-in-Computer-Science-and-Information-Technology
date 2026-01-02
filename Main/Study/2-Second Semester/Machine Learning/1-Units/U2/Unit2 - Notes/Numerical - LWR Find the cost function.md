![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20LWR%20Find%20the%20cost%20function.png)

---

## Given

* Query point: $x = 6$
* Training inputs:
  $x^{(1)} = 5$, $x^{(2)} = 4$, $x^{(3)} = 3$
* Number of training points: $n = 3$

---

## Step 1: Write the general LWR cost function

For locally weighted linear regression, the cost function is:

$$
E = \frac{1}{2n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)^2
$$

Substitute $n = 3$:

$$
E = \frac{1}{6} \sum_{i=1}^{3} w_i (y_i - a_0 - a_1 x_i)^2
$$

---

## Step 2: Write the weight formula

Weights depend on the **distance from the query point** $x = 6$:

$$
w_i = \exp\left(-\frac{(x^{(i)} - x)^2}{2\tau^2}\right)
$$

---

## Step 3: Compute each weight (symbolically)

### For $x^{(1)} = 5$

$$
w_1 = \exp\left(-\frac{(5 - 6)^2}{2\tau^2}\right)
$$

---

### For $x^{(2)} = 4$

$$
w_2 = \exp\left(-\frac{(4 - 6)^2}{2\tau^2}\right)
$$

---

### For $x^{(3)} = 3$

$$
w_3 = \exp\left(-\frac{(3 - 6)^2}{2\tau^2}\right)
$$

---

### Observation

Since:

$$
|5 - 6| < |4 - 6| < |3 - 6|
$$

We get:

$$
w_1 > w_2 > w_3
$$

So the point **closest to the query point has the highest influence**.

---

## Step 4: Substitute values into the cost function

Replace each $x_i$ with its actual value:

$$
E = \frac{1}{6} \Big[
w_1 (y_1 - a_0 - 5a_1)^2

* w_2 (y_2 - a_0 - 4a_1)^2
* w_3 (y_3 - a_0 - 3a_1)^2
  \Big]
  $$

---

## Final Answer (Exam-Ready)

The **locally weighted cost function** for query point $x = 6$ is:

$$
E = \frac{1}{6} \Big[
w_1 (y_1 - a_0 - 5a_1)^2

* w_2 (y_2 - a_0 - 4a_1)^2
* w_3 (y_3 - a_0 - 3a_1)^2
  \Big]
  $$

where:

$$
w_i = \exp\left(-\frac{(x^{(i)} - 6)^2}{2\tau^2}\right)
$$

---