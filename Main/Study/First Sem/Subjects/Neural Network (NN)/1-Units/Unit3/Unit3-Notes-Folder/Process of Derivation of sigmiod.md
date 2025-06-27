

$$
\frac{dy}{dx} = y(1 - y)
$$

---

## 🔷 Step 1: Define the sigmoid function

Let:

$$
y = \sigma(x) = \frac{1}{1 + e^{-x}}
$$

We want to differentiate this with respect to $x$:

$$
\frac{dy}{dx} = ?
$$

---

## 🔷 Step 2: Use substitution

Let’s make it easier by substituting:

Let:

$$
u = 1 + e^{-x}
\quad \Rightarrow \quad y = \frac{1}{u}
$$

---

### 🔸 Differentiate $y = \frac{1}{u}$ using the chain rule:

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$

We compute each part:

* $\frac{dy}{du} = -\frac{1}{u^2}$
* $\frac{du}{dx} = \frac{d}{dx}(1 + e^{-x}) = -e^{-x}$

So:

$$
\frac{dy}{dx} = -\frac{1}{u^2} \cdot (-e^{-x}) = \frac{e^{-x}}{(1 + e^{-x})^2}
$$

---

## 🔷 Step 3: Now write everything in terms of $y$

Remember:

$$
y = \frac{1}{1 + e^{-x}}
\Rightarrow 1 + e^{-x} = \frac{1}{y}
$$

So:

$$
e^{-x} = \frac{1 - y}{y}
$$

Now plug into our derivative:

$$
\frac{dy}{dx} = \frac{e^{-x}}{(1 + e^{-x})^2}
= \frac{\frac{1 - y}{y}}{\left(\frac{1}{y}\right)^2}
= \frac{1 - y}{y} \cdot y^2 = y(1 - y)
$$

---

## ✅ Final Answer:

$$
\frac{d}{dx} \left( \frac{1}{1 + e^{-x}} \right) = \sigma(x)(1 - \sigma(x)) = y(1 - y)
$$

