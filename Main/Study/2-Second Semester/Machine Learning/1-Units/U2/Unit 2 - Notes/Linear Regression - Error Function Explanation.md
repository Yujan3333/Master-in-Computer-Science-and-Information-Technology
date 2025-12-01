
#### 1️⃣ We Have ( n ) Training Data Points

You collected some data — for example, hours studied vs marks.
Let’s say you have ( n ) such examples.

---

#### 2️⃣ The Error (Cost Function)

Linear regression tries to draw the *best straight line* through the data.

To measure how good or bad the line is, we calculate the **error**:

$$
E = \frac{1}{2n} \sum_{i=1}^{n} (error)^2
$$

Where the error for each data point is:

$$
error = y^{(i)} - \hat{y}^{(i)}
$$

And the predicted value is:

$$
\hat{y}^{(i)} = w_0 + w_1 x^{(i)}
$$

If the prediction is bad → error is large.
If the prediction is good → error is small.

---

#### 3️⃣ Why Square the Error?

Squaring the error:

* makes all errors positive
* punishes larger mistakes more
* makes math easier for gradient descent

---

#### 4️⃣ Updating the Coefficients ( w_0 ) and ( w_1 )

To improve the line, we update:

* ( $w_0$ ) (intercept)
* ( $w_1$ ) (slope)

We use **Gradient Descent**, which means:

> Move step-by-step in the direction that reduces the error the fastest.

Each update makes:

* the line fit the data better
* the error value smaller

---

#### What the formulas mean

In linear regression, we have two things to learn:

* ( $w_0$ ) → the **intercept** (starting value of the line)
* ( $w_1$ ) → the **slope** (tilt of the line)

Gradient Descent slowly improves both so the line fits the data better.

---

##### 1️⃣ Update Rule for ( w_0 )

$$
w_0 := w_0 + \alpha \frac{1}{n} \sum_{i=1}^{n} \big( y^{(i)} - (w_0 + w_1 x^{(i)}) \big)
$$

**In simple words:**

* Look at all errors: ( $y^{(i)} - (w_0 + w_1 x^{(i)})$ )
* Average them
* Move ( w_0 ) a little in that direction
* ($\alpha$ ) = learning rate → controls how big the step is

**Intuition:**

* Predictions too low → increase ( w_0 )
* Predictions too high → decrease ( w_0 )

---

##### 2️⃣ Update Rule for ( w_1 )

$$
w_1 := w_1 + \alpha \frac{1}{n} \sum_{i=1}^{n} \big( y^{(i)} - (w_0 + w_1 x^{(i)}) \big) x^{(i)}
$$

**In simple words:**

* Look at errors again
* Multiply each error by its corresponding ( $x^{(i)}$ )
* Average them
* Move ( w_1 ) in that direction

**Intuition:**

* Slope too small → increase ( w_1 )
* Slope too big → decrease ( w_1 )

---
## [Linear Regression - Explanation of the w_0 and w_1 update rule](Linear%20Regression%20-%20Explanation%20of%20the%20w_0%20and%20w_1%20update%20rule.md)