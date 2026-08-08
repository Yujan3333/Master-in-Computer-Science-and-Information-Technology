#assignment #fuzzy-system #third-semester 

- [Explanation](FS-assignments/Explanation.md)
- [Given Example for this Program](FS-assignments/Given%20Example%20for%20this%20Program.md)
- [Example- Fuzzy relation program](FS-assignments/Example-%20Fuzzy%20relation%20program.md)
# ✅ 1. Fuzzy Relation – Definition

A fuzzy relation $R$ from $X$ to $Y$ is:

$$\mu_R(x,y)\in[0,1]$$

It assigns a membership value to each pair $(x,y)$.

---

# ✅ 2. Operations on Fuzzy Relations

---

## 🔹 Union

$$\mu_{R\cup S}(x,y)=\max(\mu_R(x,y),\mu_S(x,y))$$

---

## 🔹 Intersection

$$\mu_{R\cap S}(x,y)=\min(\mu_R(x,y),\mu_S(x,y))$$

---

## 🔹 Complement

$$\mu_{R^c}(x,y)=1-\mu_R(x,y)$$

---

## 🔹 Min–Max Composition

For $R(X \rightarrow Y)$ and $S(Y \rightarrow Z)$:

$$\mu_T(x,z)=\max_{y\in Y}\left[\min(\mu_R(x,y),\mu_S(y,z))\right]$$

👉 min inside, max outside

---

## 🔹 Subset

$$\mu_R(x,y)\le \mu_S(x,y)\ \forall(x,y)$$

---

# ✅ 3. Projection

---

## 🔹 X-Projection

$$\mu_{R_X}(x)=\max_{y\in Y}\mu_R(x,y)$$

---

## 🔹 Y-Projection

$$\mu_{R_Y}(y)=\max_{x\in X}\mu_R(x,y)$$

---

# ✅ 4. Cylindrical Extension

---

## 🔹 Extension of X

$$\mu_{A\times Y}(x,y)=\mu_A(x)$$

---

## 🔹 Extension of Y

$$\mu_{X\times B}(x,y)=\mu_B(y)$$

---

# ✅ 5. COMPLETE PYTHON PROGRAM (MENU + USER INPUT)

```python
# ---------- Input Functions ----------

def input_relation():
    n = int(input("Enter number of elements in relation: "))
    R = {}
    print("Enter (x y value):")
    for _ in range(n):
        x, y, val = input().split()
        R[(x, y)] = float(val)
    return R


def input_set():
    n = int(input("Enter number of elements in fuzzy set: "))
    A = {}
    print("Enter (element value):")
    for _ in range(n):
        x, val = input().split()
        A[x] = float(val)
    return A


# ---------- Operations ----------

def union(R, S):
    keys = set(R.keys()).union(S.keys())
    return {k: max(R.get(k, 0), S.get(k, 0)) for k in keys}


def intersection(R, S):
    keys = set(R.keys()).union(S.keys())
    return {k: min(R.get(k, 0), S.get(k, 0)) for k in keys}


def complement(R):
    return {k: 1 - v for k, v in R.items()}


def is_subset(R, S):
    for k in R:
        if R[k] > S.get(k, 0):
            return False
    return True


def min_max_composition(R, S, X, Y, Z):
    T = {}
    for x in X:
        for z in Z:
            vals = []
            for y in Y:
                vals.append(min(R.get((x, y), 0), S.get((y, z), 0)))
            T[(x, z)] = max(vals) if vals else 0
    return T


def x_projection(R):
    proj = {}
    for (x, y), v in R.items():
        proj[x] = max(proj.get(x, 0), v)
    return proj


def y_projection(R):
    proj = {}
    for (x, y), v in R.items():
        proj[y] = max(proj.get(y, 0), v)
    return proj


def cylindrical_extension_X(A, Y):
    return {(x, y): A[x] for x in A for y in Y}


def cylindrical_extension_Y(B, X):
    return {(x, y): B[y] for x in X for y in B}


# ---------- Display ----------

def display_relation(R):
    for k, v in R.items():
        print(f"{k} : {v}")


# ---------- Menu ----------

while True:
    print("\n--- Fuzzy Relation Operations ---")
    print("1. Union")
    print("2. Intersection")
    print("3. Complement")
    print("4. Subset Check")
    print("5. Min-Max Composition")
    print("6. X-Projection")
    print("7. Y-Projection")
    print("8. Cylindrical Extension (X)")
    print("9. Cylindrical Extension (Y)")
    print("0. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        R = input_relation()
        S = input_relation()
        display_relation(union(R, S))

    elif ch == 2:
        R = input_relation()
        S = input_relation()
        display_relation(intersection(R, S))

    elif ch == 3:
        R = input_relation()
        display_relation(complement(R))

    elif ch == 4:
        R = input_relation()
        S = input_relation()
        print("Subset:", is_subset(R, S))

    elif ch == 5:
        print("Enter Relation R (X→Y)")
        R = input_relation()
        print("Enter Relation S (Y→Z)")
        S = input_relation()

        X = list(set([x for x, y in R]))
        Y = list(set([y for x, y in R]))
        Z = list(set([z for y, z in S]))

        result = min_max_composition(R, S, X, Y, Z)
        display_relation(result)

    elif ch == 6:
        R = input_relation()
        print(x_projection(R))

    elif ch == 7:
        R = input_relation()
        print(y_projection(R))

    elif ch == 8:
        A = input_set()
        Y = input("Enter elements of Y (space separated): ").split()
        display_relation(cylindrical_extension_X(A, Y))

    elif ch == 9:
        B = input_set()
        X = input("Enter elements of X (space separated): ").split()
        display_relation(cylindrical_extension_Y(B, X))

    elif ch == 0:
        break

    else:
        print("Invalid choice")
```

---

# 🔥 FINAL EXAM CHEAT SUMMARY

* Union → $\max$
* Intersection → $\min$
* Complement → $1-\mu$
* Composition → $\max(\min())$
* Projection → max across dimension
* Cylindrical → copy values
* Subset → $\le$

---
