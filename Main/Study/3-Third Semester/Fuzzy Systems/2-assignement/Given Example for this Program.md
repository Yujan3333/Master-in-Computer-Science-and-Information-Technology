
# ✅ 1. Given Example

## 🔹 Fuzzy Relation ( $R(X \to Y)$ )

| (x,y) | μR  |
| ----- | --- |
| (a,c) | 0.7 |
| (a,d) | 0.5 |
| (b,c) | 0.6 |
| (b,d) | 0.2 |

---

## 🔹 Fuzzy Relation ( $S(Y \to Z)$ )

| (y,z) | μS  |
| ----- | --- |
| (c,e) | 0.6 |
| (c,f) | 0.3 |
| (d,e) | 0.8 |
| (d,f) | 0.4 |

---

## 🔹 Fuzzy Set A (for cylindrical)

$$A = {a:0.6,\ b:0.9}$$

---

# ✅ 2. Union (Example with another relation)

Let:

$$R_2(a,c)=0.4,\ (a,d)=0.8,\ (b,c)=0.3,\ (b,d)=0.9$$

---

## 🔹 Formula

$$\mu_{R\cup R_2}=\max(\mu_R,\mu_{R_2})$$

---

## 🔹 Result

| Pair  | Result           |
| ----- | ---------------- |
| (a,c) | max(0.7,0.4)=0.7 |
| (a,d) | max(0.5,0.8)=0.8 |
| (b,c) | max(0.6,0.3)=0.6 |
| (b,d) | max(0.2,0.9)=0.9 |

---

# ✅ 3. X-Projection

## 🔹 Formula

$$\mu_{R_X}(x)=\max_y \mu_R(x,y)$$

---

## 🔹 Calculation

* For (a): max(0.7, 0.5) = **0.7**
* For (b): max(0.6, 0.2) = **0.6**

---

## 🔹 Result

$$R_X = {a:0.7,\ b:0.6}$$

---

# ✅ 4. Y-Projection

## 🔹 Formula

$$\mu_{R_Y}(y)=\max_x \mu_R(x,y)$$

---

## 🔹 Calculation

* For (c): max(0.7, 0.6) = **0.7**
* For (d): max(0.5, 0.2) = **0.5**

---

## 🔹 Result

$$R_Y = {c:0.7,\ d:0.5}$$

---

# ✅ 5. Min–Max Composition

## 🔹 Formula

$$\mu_T(x,z)=\max_y [\min(\mu_R(x,y),\mu_S(y,z))]$$

---

## 🔹 Step-by-Step

### 👉 For (a,e):

* min(0.7, 0.6) = 0.6
* min(0.5, 0.8) = 0.5

max(0.6, 0.5) = **0.6**

---

### 👉 For (a,f):

* min(0.7, 0.3) = 0.3
* min(0.5, 0.4) = 0.4

max = **0.4**

---

### 👉 For (b,e):

* min(0.6, 0.6) = 0.6
* min(0.2, 0.8) = 0.2

max = **0.6**

---

### 👉 For (b,f):

* min(0.6, 0.3) = 0.3
* min(0.2, 0.4) = 0.2

max = **0.3**

---

## 🔹 Final Result

$$T = {(a,e):0.6,\ (a,f):0.4,\ (b,e):0.6,\ (b,f):0.3}$$

---

# ✅ 6. Cylindrical Extension

---

## 🔹 Extension of X

### Formula

$$\mu(x,y)=\mu_A(x)$$

---

## 🔹 Result

| Pair  | Value |
| ----- | ----- |
| (a,c) | 0.6   |
| (a,d) | 0.6   |
| (b,c) | 0.9   |
| (b,d) | 0.9   |

---

## 🔹 Extension of Y (if B = {c:0.5, d:0.7})

| Pair  | Value |
| ----- | ----- |
| (a,c) | 0.5   |
| (b,c) | 0.5   |
| (a,d) | 0.7   |
| (b,d) | 0.7   |

---

# ✅ 7. Quick Code to Test This Example

```python
R = {('a','c'):0.7, ('a','d'):0.5, ('b','c'):0.6, ('b','d'):0.2}
S = {('c','e'):0.6, ('c','f'):0.3, ('d','e'):0.8, ('d','f'):0.4}

from pprint import pprint

# Composition test
def comp(R, S):
    X = ['a','b']
    Y = ['c','d']
    Z = ['e','f']
    T = {}
    for x in X:
        for z in Z:
            vals = []
            for y in Y:
                vals.append(min(R.get((x,y),0), S.get((y,z),0)))
            T[(x,z)] = max(vals)
    return T

pprint(comp(R, S))
```

---

# 🔥 Final (What to Say in Viva)



Say:

> “For each (x,z), we compute min of relation values through intermediate y and then take max. For example, for (a,e), we get 0.6.”
