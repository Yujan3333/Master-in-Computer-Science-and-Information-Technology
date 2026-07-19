
# 📘 Universe of Discourse

$$X={10,20,30,40,50,60,70,80}$$

---

# 🔹 Gaussian Membership Function (Your Formula)

## ✅ Given Formula

$$f(x;c,\sigma)=e^{-\frac{(x-c)^2}{\sqrt{2\sigma}}}$$

## ✅ Parameters (same as before)

$c=50,;\sigma=15$

---

# 🔸 Step-by-step Calculations

First compute denominator:
$$\sqrt{2\sigma}=\sqrt{2\times15}=\sqrt{30}=5.477$$

---

## 👉 For $x=10$

$$\mu(10)=e^{-\frac{(10-50)^2}{5.477}}$$
$$=e^{-\frac{(-40)^2}{5.477}}$$
$$=e^{-\frac{1600}{5.477}}$$
$$=e^{-292.1}\approx 0$$

---

## 👉 For $x=20$

$$\mu(20)=e^{-\frac{(-30)^2}{5.477}}$$
$$=e^{-\frac{900}{5.477}}$$
$$=e^{-164.3}\approx 0$$

---

## 👉 For $x=30$

$$\mu(30)=e^{-\frac{(-20)^2}{5.477}}$$
$$=e^{-\frac{400}{5.477}}$$
$$=e^{-73.0}\approx 0$$

---

## 👉 For $x=40$

$$\mu(40)=e^{-\frac{(-10)^2}{5.477}}$$
$$=e^{-\frac{100}{5.477}}$$
$$=e^{-18.26}\approx 1.17\times10^{-8}$$

---

## 👉 For $x=50$

$$\mu(50)=e^{0}=1$$

---

## 👉 For $x=60$

Same as $x=40$ (symmetry):
$$\mu(60)\approx 1.17\times10^{-8}$$

---

## 👉 For $x=70$

$$\mu(70)\approx 0$$

---

## 👉 For $x=80$

$$\mu(80)\approx 0$$

---

# 📊 Final Fuzzy Set

$$A_{gaussian}={(10,0),(20,0),(30,0),(40,1.17\times10^{-8}),(50,1),(60,1.17\times10^{-8}),(70,0),(80,0)}$$

---

# ⚠️ Important Insight (VERY IMPORTANT FOR EXAM)

This formula:

$$e^{-\frac{(x-c)^2}{\sqrt{2\sigma}}}$$

👉 makes the denominator **very small**, so:

* exponent becomes **very large negative**
* values go to **~0 almost everywhere**

### 🔴 Conclusion:

* This behaves almost like a **spike (crisp set)** instead of a smooth fuzzy set
* It is **not the standard Gaussian form**

---

# ✅ What You Can Write in Exam

👉 *“Using the given formula, the membership values decay very rapidly, resulting in near-zero values for most inputs except at the center. This differs from the standard Gaussian function, which provides smoother fuzziness.”*

---

