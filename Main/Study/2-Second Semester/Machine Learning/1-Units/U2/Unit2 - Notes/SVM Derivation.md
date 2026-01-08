# 🌟 BIG PICTURE (READ THIS FIRST)

**SVM goal in ONE sentence:**

> Find a line/plane that separates +ve and −ve points such that the **closest points of both classes are as far as possible from the boundary**.

Everything you wrote is just a **mathematical way to measure and maximize that distance**.

---

# STAGE 1: Decision Boundary & Classification

## Equation of decision boundary

$$
w^T x + b = 0
$$

### What does this mean?

* This is a **line (2D)** or **plane (3D)** or **hyperplane**
* It divides space into two halves

---

### How classification works

For a new point $x^*$:

* $w^T x^* + b = 0$ → on the boundary
* $w^T x^* + b > 0$ → one side (**+ve class**)
* $w^T x^* + b < 0$ → other side (**−ve class**)

👉 **Sign decides the class**

---

# STAGE 2: Why “Margin” Matters

SVM doesn’t just want correct classification.
It wants **confidence**.

### High confidence = point is far from boundary

So we want:
$$
|w^T x + b| \text{ to be large}
$$

To handle both classes in one formula, we multiply by label $y$:

* $y = +1$ for +ve class
* $y = -1$ for −ve class

So:
$$
y(w^T x + b) \text{ should be large}
$$

👉 This ensures:

* +ve points stay far on +ve side
* −ve points stay far on −ve side

---

# STAGE 3: Geometry — Distance of a Point from Boundary

(**MOST IMPORTANT PART**)

Now we calculate **actual distance**.

---

## Step 3.1: Define vectors

Let:

* $x$ → a data point
* $x'$ → closest point on decision boundary
* $\vec r = x - x'$ → vector from boundary to point

$$
\vec r = x - x'
$$

📌 This vector represents **shortest distance** from point to boundary.

---

## Step 3.2: Direction of shortest distance

Key geometry fact:

> The shortest distance from a point to a plane is **perpendicular** to the plane.

The vector perpendicular to the plane is **$w$**.

So:

* $\vec r$ is **parallel to $w$**

---

## Step 3.3: Express $\vec r$ using $w$

We write:
$$
\vec r = r \cdot \frac{w}{|w|}
$$

Where:

* $r$ = length of vector (actual distance)
* $\frac{w}{|w|}$ = unit vector in direction of $w$

👉 This means:

* direction = $w$
* magnitude = $r$

![](../../../../../../../Images/Second_Sem_Images/SVM%20Derivation.png)

---

# STAGE 4: Use Boundary Condition

Because $x'$ lies on decision boundary:
$$
w^T x' + b = 0
$$

From earlier:
$$
x' = x - \vec r
$$

Substitute:
$$
w^T (x - \vec r) + b = 0
$$

Now substitute $\vec r = r \frac{w}{|w|}$:
$$
w^T \left(x - r \frac{w}{|w|}\right) + b = 0
$$

---

## Step-by-step simplification

$$
w^T x - r \frac{w^T w}{|w|} + b = 0
$$

Since:
$$
w^T w = |w|^2
$$

We get:
$$
w^T x - r |w| + b = 0
$$

---

## Solve for $r$ (distance!)

$$
r = \frac{w^T x + b}{|w|}
$$

🎉 **This is the distance of a point from decision boundary**

---

# STAGE 5: Handle Both Classes Together

For −ve class, distance becomes negative, so we fix it using $y$:

$$
r = \frac{y(w^T x + b)}{|w|}
$$

This is called the **geometric margin**.

📌 It is:

* actual distance
* scale-invariant
* meaningful

---

# STAGE 6: Support Vectors & Margin Width

SVM **scales** parameters such that the closest points satisfy:
$$
y(w^T x + b) = 1
$$

These points are **support vectors**.

Distance of each support vector:
$$
r = \frac{1}{|w|}
$$

There are **two sides**, so:

$$
\text{Total Margin} = \frac{2}{|w|}
$$

---

# STAGE 7: Optimization Objective

SVM wants:
$$
\text{maximize } \frac{2}{|w|}
$$

Equivalent to:
$$
\text{minimize } \frac{|w|^2}{2}
$$

Subject to:
$$
y^i(w^T x^i + b) \ge 1
$$

This is the **hard-margin SVM optimization problem**.

---

# STAGE 8: Functional vs Geometric Margin

### Functional margin:

$$
y(w^T x + b)
$$

❌ Problem:

* Can be increased arbitrarily by scaling $w, b$
* Not meaningful distance

---

### Geometric margin:

$$
\frac{y(w^T x + b)}{|w|}
$$

✅ True distance
✅ Scale independent
✅ Used by SVM

---

# 🧠 FINAL FLOW (REMEMBER THIS)

1. Define decision boundary
2. Decide class using sign
3. Measure distance from boundary
4. Express distance using vectors
5. Identify closest points (support vectors)
6. Maximize margin
7. Form optimization problem

---

# ✨ ONE-LINE INTUITION (EXAM GOLD)

> **SVM finds the separating hyperplane such that the minimum distance of any training point from the hyperplane is maximized.**

---
