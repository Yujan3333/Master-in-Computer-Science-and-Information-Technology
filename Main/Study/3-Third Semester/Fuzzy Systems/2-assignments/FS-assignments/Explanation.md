
# ✅ 1. Class: `FuzzyRelation`

```python
class FuzzyRelation:
    def __init__(self, relation_dict):
        self.R = relation_dict
```

### 🔹 What it does

* Stores the fuzzy relation as:

  ```
  {(x,y): μ}
  ```

### 🔹 Concept implemented

$$\mu_R(x,y)\in[0,1]$$

👉 Each key = pair $(x,y)$
👉 Each value = membership

---

# ✅ 2. Display Function

```python
def display(self, name="Relation"):
    for k, v in self.R.items():
        print(f"{k} : {v}")
```

### 🔹 What it does

* Prints all pairs with their membership values

### 🔹 Concept

👉 Shows the fuzzy relation table

---

# ✅ 3. Union

```python
def union(self, other):
    keys = set(self.R.keys()).union(other.R.keys())
    return FuzzyRelation({
        k: max(self.R.get(k, 0), other.R.get(k, 0))
        for k in keys
    })
```

### 🔹 Formula

$$\mu_{R\cup S}(x,y)=\max(\mu_R(x,y),\mu_S(x,y))$$

### 🔹 How code matches formula

* `keys = union(...)` → all possible pairs
* `self.R.get(k,0)` → $\mu_R(x,y)$
* `other.R.get(k,0)` → $\mu_S(x,y)$
* `max(...)` → implements formula

👉 Missing values assumed 0 ✔️

---

# ✅ 4. Intersection

```python
def intersection(self, other):
    return FuzzyRelation({
        k: min(self.R.get(k, 0), other.R.get(k, 0))
        for k in keys
    })
```

### 🔹 Formula

$$\mu_{R\cap S}(x,y)=\min(\mu_R(x,y),\mu_S(x,y))$$

### 🔹 Code mapping

* `min(...)` → directly implements intersection

---

# ✅ 5. Complement

```python
def complement(self):
    return FuzzyRelation({k: 1 - v for k, v in self.R.items()})
```

### 🔹 Formula

$$\mu_{R^c}(x,y)=1-\mu_R(x,y)$$

### 🔹 Code mapping

* `1 - v` → exactly same as formula

---

# ✅ 6. Subset

```python
def is_subset(self, other):
    for k in self.R:
        if self.R[k] > other.R.get(k, 0):
            return False
    return True
```

### 🔹 Formula

$$\mu_R(x,y)\le \mu_S(x,y)$$

### 🔹 Code mapping

* checks: `self.R[k] > other.R[k]`
* if true → violates condition ❌

👉 So relation is NOT subset

---

# ✅ 7. X-Projection

```python
def x_projection(self):
    proj = {}
    for (x, y), v in self.R.items():
        proj[x] = max(proj.get(x, 0), v)
    return proj
```

### 🔹 Formula

$$\mu_{R_X}(x)=\max_{y\in Y}\mu_R(x,y)$$

### 🔹 Code mapping

* loop over all $(x,y)$
* group by `x`
* take max value

👉 exactly “max over y”

---

# ✅ 8. Y-Projection

```python
def y_projection(self):
    proj[y] = max(proj.get(y, 0), v)
```

### 🔹 Formula

$$\mu_{R_Y}(y)=\max_{x\in X}\mu_R(x,y)$$

### 🔹 Code mapping

* group by `y`
* take max across all `x`

---

# ✅ 9. Min–Max Composition

```python
def min_max_composition(self, other):
```

---

### 🔹 Formula

$$\mu_T(x,z)=\max_{y}\left[\min(\mu_R(x,y),\mu_S(y,z))\right]$$

---

### 🔹 Code Breakdown

```python
X = set([x for x, y in self.R])
Y = set([y for x, y in self.R])
Z = set([z for y, z in other.R])
```

👉 Extract domains:

* $X$, $Y$, $Z$

---

```python
for x in X:
    for z in Z:
```

👉 computing for each $(x,z)$

---

```python
for y in Y:
    vals.append(min(self.R.get((x, y), 0),
                    other.R.get((y, z), 0)))
```

👉 inner:
$$\min(\mu_R(x,y),\mu_S(y,z))$$

---

```python
result[(x, z)] = max(vals)
```

👉 outer:
$$\max_y(...)$$

---

✅ So:

* **min inside loop**
* **max outside loop**

---

# ✅ 10. FuzzySet Class (Cylindrical Extension)

---

## 🔹 Extension of X

```python
def cylindrical_extension_X(self, Y):
    return {(x, y): self.A[x] for x in self.A for y in Y}
```

### 🔹 Formula

$$\mu_{A\times Y}(x,y)=\mu_A(x)$$

### 🔹 Code mapping

* copies value of `x` for all `y`

---

## 🔹 Extension of Y

```python
def cylindrical_extension_Y(self, X):
    return {(x, y): self.A[y] for x in X for y in self.A}
```

### 🔹 Formula

$$\mu_{X\times B}(x,y)=\mu_B(y)$$

### 🔹 Code mapping

* copies value of `y` for all `x`

---

# ✅ 11. Input Functions

---

## 🔹 Relation Input

```python
R[(x, y)] = val
```

👉 builds:
$$\mu_R(x,y)$$

---

## 🔹 Validation

```python
if 0 <= val <= 1
```

👉 ensures fuzzy condition ✔️

---

# ✅ 12. Menu System

```python
while True:
```

👉 infinite loop for repeated operations

---

```python
if ch == 1:
```

👉 selects operation

---

```python
R.union(S)
```

👉 calling OOP method instead of function

---

# 🔥 FINAL UNDERSTANDING (VERY IMPORTANT)

| Concept      | Code Logic                      |
| ------------ | ------------------------------- |
| Union        | `max()`                         |
| Intersection | `min()`                         |
| Complement   | `1 - v`                         |
| Subset       | `<= check`                      |
| Projection   | grouping + `max()`              |
| Composition  | nested loops → `min` then `max` |
| Cylindrical  | value copying                   |

---
