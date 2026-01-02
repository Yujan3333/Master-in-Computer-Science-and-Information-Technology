# Step-by-Step Derivation of LWR Weight Update Rule

---

## Step 1: Cost Function

The **weighted cost function** in LWR is:

$$
E = \frac{1}{2n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)^2
$$

Where:

* $a_0$ is the intercept, $a_1$ is the slope
* $(x_i, y_i)$ are training points
* $w_i$ is the weight of the $i^{th}$ point based on distance from the query point

**Goal:** Find $a_0$ and $a_1$ that **minimize $E$**.

---

## Step 2: Partial Derivative w.r.t $a_0$

Compute:

$$
\frac{\partial E}{\partial a_0}
$$

Start with:

$$
E = \frac{1}{2n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)^2
$$

Derivative formula for $(f(a_0))^2$:

$$
\frac{d}{da_0} (y_i - a_0 - a_1 x_i)^2 = 2 (y_i - a_0 - a_1 x_i) \cdot \frac{d}{da_0}(y_i - a_0 - a_1 x_i)
$$

Since derivative of $y_i$ and $a_1 x_i$ w.r.t $a_0$ is $0$ and $-1$ respectively:

$$
\frac{d}{da_0}(y_i - a_0 - a_1 x_i) = -1
$$
- First term: $y_i$ → derivative w.r.t $a_0$ is 0 (because $y_i$ is constant w.r.t $a_0$).
- Second term: $-a_0$ → derivative w.r.t $a_0$ is -1.
- Third term: $-a_1 x_i$ → derivative w.r.t $a_0$ is 0 (because $a_1$ and $x_i$ are constants when differentiating w.r.t $a_0$).



So:

$$
\frac{\partial}{\partial a_0} (y_i - a_0 - a_1 x_i)^2 = 2 (y_i - a_0 - a_1 x_i) (-1)
$$

Include weight $w_i$ and factor $1/(2n)$:

$$
\frac{\partial E}{\partial a_0} = \frac{1}{2n} \sum_{i=1}^{n} w_i \cdot 2 (y_i - a_0 - a_1 x_i)(-1)
$$

Simplify constants:

$$
\frac{\partial E}{\partial a_0} = -\frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)
$$

✅ Derivative w.r.t $a_0$ obtained.

---

## Step 3: Partial Derivative w.r.t $a_1$

Compute:

$$
\frac{\partial E}{\partial a_1} = \frac{\partial}{\partial a_1} \left( \frac{1}{2n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)^2 \right)
$$

Derivative of $(y_i - a_0 - a_1 x_i)^2$ w.r.t $a_1$:

$$
\frac{d}{da_1} (y_i - a_0 - a_1 x_i)^2 = 2 (y_i - a_0 - a_1 x_i) \cdot \frac{d}{da_1}(y_i - a_0 - a_1 x_i)
$$

Derivative of $-a_1 x_i$ w.r.t $a_1$ is $-x_i$:

$$
\frac{d}{da_1} (y_i - a_0 - a_1 x_i) = -x_i
$$

So:

$$
\frac{\partial}{\partial a_1} (y_i - a_0 - a_1 x_i)^2 = 2 (y_i - a_0 - a_1 x_i)(-x_i)
$$

Include weight $w_i$ and factor $1/(2n)$:

$$
\frac{\partial E}{\partial a_1} = \frac{1}{2n} \sum_{i=1}^{n} w_i \cdot 2 (y_i - a_0 - a_1 x_i)(-x_i)
$$

Simplify constants:

$$
\frac{\partial E}{\partial a_1} = -\frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i) x_i
$$

✅ Derivative w.r.t $a_1$ obtained.

---

## Step 4: Gradient Descent Update Rule

Gradient descent updates parameters as:

$$
a_0 = a_0 - \alpha \frac{\partial E}{\partial a_0}
$$

$$
a_1 = a_1 - \alpha \frac{\partial E}{\partial a_1}
$$

Substitute derivatives:

$$
a_0 = a_0 - \left(-\alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)\right)
$$

Simplify:

$$
a_0 = a_0 + \alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)
$$

For $a_1$:

$$
a_1 = a_1 - \left(-\alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i) x_i \right)
$$

Simplify:

$$
a_1 = a_1 + \alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i) x_i
$$

---

## Step 5: Explanation

1. **Cost function:** Measures weighted squared error.
2. **Derivative w.r.t $a_0$:** Shows how intercept changes based on weighted error.
3. **Derivative w.r.t $a_1$:** Shows how slope changes, scaled by $x_i$ and weighted by $w_i$.
4. **Gradient descent:** Updates $a_0$ and $a_1$ in direction that reduces weighted error.
5. **Weight effect:** Larger $w_i$ → closer points → more influence on parameter update.

---
