- [More detailed solution](More%20detailed%20solution.md)
- [How are parameters chosen here](How%20are%20parameters%20chosen%20here.md)

$$X={10,20,30,40,50,60,70,80}$$

---

# 📘 1. Gaussian Membership Function

## ✅ Formula

$$f(x;c,\sigma)=e^{-\frac{(x-c)^2}{\sqrt{2\sigma}}}$$

---

# 📘 2. Sigmoid Membership Function

## ✅ Formula

$$f(x;c,\sigma)=\frac{1}{1+e^{-\sigma(x-c)}}$$

## ✅ Parameters (chosen)

* $c=50$
* $\sigma=0.1$

## ✅ Fuzzy Set (Sigmoid)

| x  | μ(x)  |
| -- | ----- |
| 10 | 0.018 |
| 20 | 0.047 |
| 30 | 0.119 |
| 40 | 0.269 |
| 50 | 0.500 |
| 60 | 0.731 |
| 70 | 0.881 |
| 80 | 0.953 |

## ✅ Representation

$$A_{sigmoid}={(10,0.018),(20,0.047),(30,0.119),(40,0.269),(50,0.5),(60,0.731),(70,0.881),(80,0.953)}$$

👉 Monotonically increasing → represents “High”

---

# 📘 3. Generalized Bell Membership Function

## ✅ Formula

$$f(x;a,b,c)=\frac{1}{1+\left|\frac{x-c}{a}\right|^{2b}}$$

## ✅ Parameters (chosen)

* $a=15$ (width)
* $b=2$ (shape)
* $c=50$ (center)

## ✅ Fuzzy Set (Gbell)

| x  | μ(x)  |
| -- | ----- |
| 10 | 0.020 |
| 20 | 0.165 |
| 30 | 0.558 |
| 40 | 0.941 |
| 50 | 1.000 |
| 60 | 0.941 |
| 70 | 0.558 |
| 80 | 0.165 |

## ✅ Representation

$$A_{gbell}={(10,0.020),(20,0.165),(30,0.558),(40,0.941),(50,1),(60,0.941),(70,0.558),(80,0.165)}$$

👉 Flatter top compared to Gaussian → wider “full membership”

---

# 📊 Final Comparison

| x  | Gaussian | Sigmoid | Gbell |
| -- | -------- | ------- | ----- |
| 10 | 0.029    | 0.018   | 0.020 |
| 20 | 0.135    | 0.047   | 0.165 |
| 30 | 0.411    | 0.119   | 0.558 |
| 40 | 0.801    | 0.269   | 0.941 |
| 50 | 1.000    | 0.500   | 1.000 |
| 60 | 0.801    | 0.731   | 0.941 |
| 70 | 0.411    | 0.881   | 0.558 |
| 80 | 0.135    | 0.953   | 0.165 |

---

# ✅ Final Insight (Exam Line)

* **Gaussian** → smooth symmetric distribution
* **Sigmoid** → increasing trend (used for “High”)
* **Gbell** → adjustable flatness → better control over fuzzy region

---
