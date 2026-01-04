# Question
![](../../../../../../../Images/Second_Sem_Images/Copy%20Example%20of%20Dominator%20Tree.png)

---
# Answer
Perfect question 👍
Let’s **build the dominator tree step-by-step** and then draw it as a **clean ASCII tree** (no images).

---

## 1️⃣ CFG (given, simplified mentally)

Paths from entry:

* `1 → 2 → 3 → 4 → 8`
* `1 → 2 → 5 → 6 → 4 → 8`
* `1 → 2 → 5 → 6 → 7 → 8`

Entry = **1**

---

## 2️⃣ Dominator sets (final result)

```
Dom(1) = {1}
Dom(2) = {1, 2}
Dom(3) = {1, 2, 3}
Dom(5) = {1, 2, 5}
Dom(6) = {1, 2, 5, 6}
Dom(4) = {1, 2, 4}
Dom(7) = {1, 2, 5, 6, 7}
Dom(8) = {1, 2, 8}
```

---

## 3️⃣ Immediate Dominators (key step)

Using **closest strict dominator** rule:

```
idom(2) = 1
idom(3) = 2
idom(5) = 2
idom(6) = 5
idom(4) = 2
idom(7) = 6
idom(8) = 2
```

---

## 4️⃣ Dominator Tree (ASCII Diagram)

```
1
└── 2
    ├── 3
    ├── 4
    ├── 5
    │   └── 6
    │       └── 7
    └── 8
```

---

## 5️⃣ Very Important Insight (EXAM GOLD)

* **Dominator tree ≠ CFG**
* Even though:

  * `4` comes from `3` and `6` in CFG
  * `8` comes from `4` and `7` in CFG

👉 Their **immediate dominator is still `2`**, because **every path** to them must pass through `2`.

---

## 🔑 One-line takeaway

> The dominator tree shows **mandatory control dependence**, not execution order.
