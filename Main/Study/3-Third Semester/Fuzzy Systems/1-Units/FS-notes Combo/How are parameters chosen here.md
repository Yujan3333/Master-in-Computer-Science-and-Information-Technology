
# 📘 1. General Idea (VERY IMPORTANT)

When choosing parameters, think:

* Where should membership be **maximum (μ = 1)**?
* How **wide** should the fuzzy region be?
* Should it be **gradual or sharp**?

---

# 🔹 2. Gaussian Function Parameters

## Formula

$$f(x;c,\sigma)=e^{-\frac{(x-c)^2}{2\sigma^2}}$$

## 🎯 How to Choose

### ✅ $c$ (center)

* Pick the value where membership should be **1**
* Example:

  * If “medium temperature” → choose middle of domain
  * Here: $c = 50$

---

### ✅ $\sigma$ (spread)

Controls **width**

* Small $\sigma$ → narrow (sharp peak)
* Large $\sigma$ → wide (smooth)

### 🔸 Rule of Thumb

$$\sigma \approx \frac{\text{range}}{4} \text{ to } \frac{\text{range}}{6}$$

For your case:

* Range = $80-10=70$
* So:
  $$\sigma \approx 10 \text{ to } 20$$

👉 That’s why we picked **15**

---

# 🔹 3. Sigmoid Function Parameters

## Formula

$$f(x;c,\sigma)=\frac{1}{1+e^{-\sigma(x-c)}}$$

## 🎯 How to Choose

### ✅ $c$ (threshold point)

* Where membership = **0.5**
* This is the **boundary**

Example:

* “Hot temperature starts around 50” → $c=50$

---

### ✅ $\sigma$ (slope)

* Small → gradual increase
* Large → sharp transition

### 🔸 Rule of Thumb

| σ value | Behavior    |
| ------- | ----------- |
| 0.05    | very smooth |
| 0.1     | normal      |
| 0.5+    | very steep  |

👉 We used **0.1** → smooth transition

---

# 🔹 4. Generalized Bell Function Parameters

## Formula

$$f(x;a,b,c)=\frac{1}{1+\left|\frac{x-c}{a}\right|^{2b}}$$

## 🎯 How to Choose

### ✅ $c$ (center)

Same logic:

* Peak point → $c=50$

---

### ✅ $a$ (width)

* Controls how wide the curve is

### 🔸 Rule of Thumb

$$a \approx \frac{\text{range}}{4}$$

So:
$$a \approx \frac{70}{4}\approx 15$$

---

### ✅ $b$ (shape / flatness)

* Controls **top shape**

| b value | Shape    |
| ------- | -------- |
| 1       | smooth   |
| 2       | normal   |
| 5+      | flat top |

👉 We used **b = 2** (standard exam choice)

---

# 🔥 5. Quick Parameter Selection Strategy (EXAM GOLD)

If nothing is given, do this:

### Step 1: Find range

$$\text{range} = \max - \min$$

### Step 2: Choose center

$$c = \text{middle value}$$

### Step 3: Choose width

* Gaussian: $\sigma \approx \frac{\text{range}}{5}$
* Bell: $a \approx \frac{\text{range}}{4}$

### Step 4: Choose shape

* Sigmoid: $\sigma = 0.1$ (safe default)
* Bell: $b = 2$

---

# 🎯 What to Write in Exam

👉 You can write:

> “Parameters are selected based on the domain range and desired shape. The center $c$ is chosen as the midpoint of the domain, while spread/width parameters are selected proportionally to the range to ensure proper fuzziness.”

---

# ✅ Final Insight

* $c$ → **where peak happens**
* width params ($\sigma$, $a$) → **how wide**
* shape params ($b$, sigmoid $\sigma$) → **how sharp or flat**

---
