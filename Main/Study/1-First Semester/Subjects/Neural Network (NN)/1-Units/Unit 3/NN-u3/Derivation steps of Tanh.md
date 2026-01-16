

$$
\frac{d}{dx} \tanh(x) = 1 - \tanh^2(x)
$$

---

## 🔷 Step 1: Define the tanh function

$$
\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$

Let’s call this:

$$
y = \tanh(x) = \frac{a}{b}
\quad \text{where} \quad
a = e^x - e^{-x}, \quad b = e^x + e^{-x}
$$

---

## 🔷 Step 2: Differentiate using the **quotient rule**

The quotient rule says:

$$
\frac{d}{dx} \left( \frac{a}{b} \right) = \frac{a'b - ab'}{b^2}
$$

Now compute:

* $a' = \frac{d}{dx}(e^x - e^{-x}) = e^x + e^{-x}$
* $b' = \frac{d}{dx}(e^x + e^{-x}) = e^x - e^{-x}$

Now plug into the quotient rule:

$$
\frac{dy}{dx} = \frac{(e^x + e^{-x})(e^x + e^{-x}) - (e^x - e^{-x})(e^x - e^{-x})}{(e^x + e^{-x})^2}
$$

---

## 🔷 Step 3: Simplify numerator

Let’s expand both parts:

1. $(e^x + e^{-x})^2 = e^{2x} + 2 + e^{-2x}$
2. $(e^x - e^{-x})^2 = e^{2x} - 2 + e^{-2x}$

Now subtract them:

$$
\text{Numerator} = [e^{2x} + 2 + e^{-2x}] - [e^{2x} - 2 + e^{-2x}] = 4
$$

So the full derivative becomes:

$$
\frac{dy}{dx} = \frac{4}{(e^x + e^{-x})^2}
$$

---

## 🔷 Step 4: Express everything in terms of tanh(x)

We’ll use a trick identity:

$$
\sech(x) = \frac{2}{e^x + e^{-x}} \quad \Rightarrow \quad \sech^2(x) = \frac{4}{(e^x + e^{-x})^2}
$$

So:

$$
\frac{dy}{dx} = \sech^2(x)
$$

And using the identity:

$$
\sech^2(x) = 1 - \tanh^2(x)
$$

---

## ✅ Final Answer:

$$
\frac{d}{dx} \tanh(x) = 1 - \tanh^2(x)
$$

