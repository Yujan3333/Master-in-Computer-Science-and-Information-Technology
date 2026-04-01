# 🔹 Goal

Understand why:

$$e^{-j\pi x}=(-1)^x$$

---

# 🔹 Step 1: Start from Euler’s Formula

$$e^{-j\theta}=\cos\theta - j\sin\theta$$

---

# 🔹 Step 2: Substitute $\theta=\pi x$

$$e^{-j\pi x}=\cos(\pi x)-j\sin(\pi x)$$

---

# 🔹 Step 3: Evaluate for integer $x$

👉 Important property:

* $$\sin(\pi x)=0$$ for all integers $x$
* $$\cos(\pi x)=(-1)^x$$

---

# 🔹 Step 4: Substitute values

$$e^{-j\pi x}=(-1)^x - j(0)$$

---

# 🔹 Final Result

$$e^{-j\pi x}=(-1)^x$$

---

# 🔹 Why $\cos(\pi x)=(-1)^x$?

Check pattern:

| $x$ | $\cos(\pi x)$ | $(-1)^x$ |
| --- | ------------- | -------- |
| 0   | 1             | 1        |
| 1   | -1            | -1       |
| 2   | 1             | 1        |
| 3   | -1            | -1       |

👉 Same pattern ⇒

$$\cos(\pi x)=(-1)^x$$

---

# 🔹 Final Intuition (for viva)

“Since $\sin(\pi x)=0$ and $\cos(\pi x)$ alternates between $+1$ and $-1$, the complex exponential reduces to $(-1)^x$.”

---