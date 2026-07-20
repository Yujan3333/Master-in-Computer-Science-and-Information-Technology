**WRONG!**
```
1 1 0 0
1 0 0 2
0 0 2 2
0 0 0 0
```

But here’s **why this is NOT correct for 4-connectivity**:

---

# 🔹 Key Rule: 4-Connectivity

For **4-connected components**, a pixel is connected to its **top, bottom, left, right neighbors ONLY**.

* Diagonal neighbors **do NOT count**.
* Only already-scanned neighbors (top and left) are considered when assigning label.

---

# 🔹 Check Your Example

### Binary Image

```
1 1 0 0
1 0 0 1
0 0 1 1
0 0 0 0
```

---

### Step-by-Step 4-Connected Labeling

1. **Top-left group**

```
1 1
1
```

* Connected horizontally and vertically → **label 1**

---

2. **Pixel (1,3) = 1**

* Its **top neighbor = 0**, **left neighbor = 0**
* So it is **not connected** to any existing labeled pixel → new label = **2**

---

3. **Pixels (2,2) and (2,3) = 1**

* Pixel (2,2): **top = 0, left = 0** → new label = **3**
* Pixel (2,3): **left = 3** → connected to 3 → label = **3**

✅ Notice: (2,2) and (2,3) are **diagonal to (1,3)**, but diagonal **does not count in 4-connectivity**

---

# 🔹 Resulting Labeled Image

```
1 1 0 0
1 0 0 2
0 0 3 3
0 0 0 0
```

---

# 🔹 Why Your Version is Wrong

```
1 1 0 0
1 0 0 2
0 0 2 2
0 0 0 0
```

* You assumed **(2,2) is connected to (1,3)** diagonally → only allowed in **8-connectivity**, NOT 4-connectivity

---

# 🔹 Rule of Thumb

* **4-connected:** up, down, left, right only
* **8-connected:** diagonals allowed
* For exams, **always check your connectivity type**

---
