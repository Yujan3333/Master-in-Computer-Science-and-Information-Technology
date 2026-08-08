
# 📘 Universe of Discourse

$$X={10,20,30,40,50,60,70,80}$$

---

# 🔹 1. Gaussian Membership Function

## ✅ Formula

- [Actual Gaussian Formula- Numerical in detail](Actual%20Gaussian%20Formula-%20Numerical%20in%20detail.md)


$$f(x;c,\sigma)=e^{-\frac{(x-c)^2}{\sqrt{2\sigma}}}$$


---

# 🔹 2. Sigmoid Membership Function

- [Sigmoid Function - Numerical in detail](Sigmoid%20Function%20-%20Numerical%20in%20detail.md)

## ✅ Formula

$$f(x;c,\sigma)=\frac{1}{1+e^{-\sigma(x-c)}}$$

## Parameters:

$c=50,;\sigma=0.1$

---

## 🔸 Step-by-step Calculations

### 👉 For $x=10$

$$\mu(10)=\frac{1}{1+e^{-0.1(10-50)}}$$
$$=\frac{1}{1+e^{-0.1(-40)}}$$
$$=\frac{1}{1+e^{4}}$$
$$=\frac{1}{1+54.6}=0.018$$

---

### 👉 For $x=50$

$$\mu(50)=\frac{1}{1+e^{0}}=\frac{1}{2}=0.5$$

---

### 👉 For $x=80$

$$\mu(80)=\frac{1}{1+e^{-0.1(30)}}$$
$$=\frac{1}{1+e^{-3}}$$
$$=\frac{1}{1+0.0498}=0.953$$

---

## ✅ Final Fuzzy Set

$$A_{sigmoid}={(10,0.018),(20,0.047),(30,0.119),(40,0.269),(50,0.5),(60,0.731),(70,0.881),(80,0.953)}$$

---

# 🔹 3. Generalized Bell Membership Function
- [Bell Function - Numerical in detail](Bell%20Function%20-%20Numerical%20in%20detail.md)

## ✅ Formula

$$f(x;a,b,c)=\frac{1}{1+\left|\frac{x-c}{a}\right|^{2b}}$$

## Parameters:

$a=15,;b=2,;c=50$

---

## 🔸 Step-by-step Calculations

### 👉 For $x=10$

$$\mu(10)=\frac{1}{1+\left|\frac{10-50}{15}\right|^{4}}$$
$$=\frac{1}{1+\left(\frac{-40}{15}\right)^4}$$
$$=\frac{1}{1+(2.67)^4}$$
$$=\frac{1}{1+50.6}=0.020$$

---

### 👉 For $x=40$

$$\mu(40)=\frac{1}{1+\left(\frac{-10}{15}\right)^4}$$
$$=\frac{1}{1+(0.67)^4}$$
$$=\frac{1}{1+0.201}=0.941$$

---

### 👉 For $x=50$

$$\mu(50)=\frac{1}{1+0}=1$$

---

## ✅ Final Fuzzy Set

$$A_{gbell}={(10,0.020),(20,0.165),(30,0.558),(40,0.941),(50,1),(60,0.941),(70,0.558),(80,0.165)}$$

---
