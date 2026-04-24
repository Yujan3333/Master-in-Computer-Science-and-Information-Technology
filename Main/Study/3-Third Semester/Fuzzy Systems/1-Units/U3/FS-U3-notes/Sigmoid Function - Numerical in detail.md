
# 📘 Universe of Discourse

$$X={10,20,30,40,50,60,70,80}$$

---

# 🔹 Sigmoid Membership Function

## ✅ Formula

$$f(x;c,\sigma)=\frac{1}{1+e^{-\sigma(x-c)}}$$

## ✅ Parameters (same as before)

$c=50,;\sigma=0.1$

---

# 🔸 Step-by-step Calculations

---

## 👉 For $x=10$

$$\mu(10)=\frac{1}{1+e^{-0.1(10-50)}}$$
$$=\frac{1}{1+e^{-0.1(-40)}}$$
$$=\frac{1}{1+e^{4}}$$
$$=\frac{1}{1+54.6}$$
$$=0.018$$

---

## 👉 For $x=20$

$$\mu(20)=\frac{1}{1+e^{-0.1(20-50)}}$$
$$=\frac{1}{1+e^{3}}$$
$$=\frac{1}{1+20.09}$$
$$=0.047$$

---

## 👉 For $x=30$

$$\mu(30)=\frac{1}{1+e^{-0.1(30-50)}}$$
$$=\frac{1}{1+e^{2}}$$
$$=\frac{1}{1+7.389}$$
$$=0.119$$

---

## 👉 For $x=40$

$$\mu(40)=\frac{1}{1+e^{-0.1(40-50)}}$$
$$=\frac{1}{1+e^{1}}$$
$$=\frac{1}{1+2.718}$$
$$=0.269$$

---

## 👉 For $x=50$

$$\mu(50)=\frac{1}{1+e^{0}}=\frac{1}{2}=0.5$$

---

## 👉 For $x=60$

$$\mu(60)=\frac{1}{1+e^{-1}}$$
$$=\frac{1}{1+0.3679}$$
$$=0.731$$

---

## 👉 For $x=70$

$$\mu(70)=\frac{1}{1+e^{-2}}$$
$$=\frac{1}{1+0.1353}$$
$$=0.881$$

---

## 👉 For $x=80$

$$\mu(80)=\frac{1}{1+e^{-3}}$$
$$=\frac{1}{1+0.0498}$$
$$=0.953$$

---

# 📊 Final Fuzzy Set

$$A_{sigmoid}={(10,0.018),(20,0.047),(30,0.119),(40,0.269),(50,0.5),(60,0.731),(70,0.881),(80,0.953)}$$

---

# 🎯 Key Insight (Exam Line)

* Membership **increases gradually**
* $x=50$ → midpoint ($\mu=0.5$)
* Represents **“High” or “Large”**

---