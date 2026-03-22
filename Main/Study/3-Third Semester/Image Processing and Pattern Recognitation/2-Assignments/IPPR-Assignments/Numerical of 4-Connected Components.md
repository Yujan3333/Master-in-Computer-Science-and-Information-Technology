- [Confusion in Numerical of 4-Connected Components](Confusion%20in%20Numerical%20of%204-Connected%20Components.md)
# 🔷 Given Binary Image

```
1 1 0 0
1 0 0 1
0 0 1 1
0 0 0 0
```

---

# 🔷 Rule (4-Connectivity)

Check only:

* **Top**
* **Left**

Scan order:
👉 Left → Right, Top → Bottom

---

# 🔷 Step 1: Start Labeling

We start with label = 1

---

## 🔹 Row 1

### Pixel (0,0) = 1

No top, no left
👉 Assign **1**

```
1 _ _ _
_ _ _ _
_ _ _ _
_ _ _ _
```

---

### Pixel (0,1) = 1

Left = 1
👉 Assign **1**

```
1 1 _ _
_ _ _ _
_ _ _ _
_ _ _ _
```

---

### Pixel (0,2), (0,3) = 0 → skip

---

## 🔹 Row 2

### Pixel (1,0) = 1

Top = 1
👉 Assign **1**

```
1 1 0 0
1 _ _ _
_ _ _ _
_ _ _ _
```

---

### Pixel (1,1), (1,2) = 0 → skip

---

### Pixel (1,3) = 1

Top = 0, Left = 0
👉 New label = **2**

```
1 1 0 0
1 0 0 2
_ _ _ _
_ _ _ _
```

---

## 🔹 Row 3

### Pixel (2,0), (2,1) = 0 → skip

---

### Pixel (2,2) = 1

Top = 0, Left = 0
👉 New label = **3**

```
1 1 0 0
1 0 0 2
0 0 3 _
_ _ _ _
```

---

### Pixel (2,3) = 1

Left = 3
👉 Assign **3**

```
1 1 0 0
1 0 0 2
0 0 3 3
_ _ _ _
```

---

## 🔹 Row 4 → all 0 → skip

---

# 🔷 Final Labeled Image

```
1 1 0 0
1 0 0 2
0 0 3 3
0 0 0 0
```

---

# 🔷 Final Answer (Interpretation)

* Label **1** → Top-left component
* Label **2** → Single pixel (right side)
* Label **3** → Bottom-right component

👉 **Total connected components = 3**

---

# 🔥 Quick Memory Trick

For each pixel = 1:

* No neighbor → **new label**
* One neighbor → **copy label**
* Two neighbors → **merge (equivalence)**

---
