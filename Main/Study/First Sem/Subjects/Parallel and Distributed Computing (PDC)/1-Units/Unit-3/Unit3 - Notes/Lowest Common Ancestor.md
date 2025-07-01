
## 🧾 Goal:

To construct a **matrix `A[u, v]`** such that:

* `A[u, v] = u` if **u is an ancestor of v** (or represents a relationship between u and v),
* And for any two **distinct subtrees** of the children of `u`, mark that `u` is the **common ancestor** of all pairs of nodes from different subtrees.

---

## 📌 Notation:

* `T`: a rooted tree
* `l(u)`: the **pre-order number** (or label) of node `u` when first visited
* `r(u)`: the **largest pre-order number** in the **subtree rooted at `u`**
* `[l(u), r(u)]`: the **range of pre-order numbers** for the subtree of node `u`
* `w₁, w₂, ..., w_d(u)`: the children of `u`

---

## 🧠 Step-by-Step Explanation:

### Step 1: Pre-order Numbering

* Perform a **pre-order traversal** of the tree `T`.
* Assign a **unique number** `l(u)` to each node as you visit it.
* After traversing the subtree rooted at `u`, set `r(u)` as the **last number assigned in its subtree**.

Now for every node `u`, `[l(u), r(u)]` is the range of labels in its subtree.

---

### Step 2: Parallel Initialization

```text
For all nodes u of T, do in parallel:
  For all v ∈ [l(u), r(u)], do in parallel:
     A[u, v] = u
```

* This sets `A[u, v] = u` for all nodes `v` that are **descendants of `u`**, including `u` itself.
* It builds an **ancestor map**: node `u` is an ancestor of all `v` in its subtree.

---

### Step 3: Cross-subtree Pairs

```text
For all x ∈ [l(wi), r(wi)] and y ∈ [l(wj), r(wj)], 1 ≤ i ≠ j ≤ d(u), do in parallel:
   A[x, y] = u
```

* For every pair of **distinct child subtrees** of `u`, this sets `A[x, y] = u` for all combinations of `x` and `y` from those subtrees.
* In other words: **for all pairs of nodes from different subtrees of `u`**, `u` is their **lowest common ancestor**.

---

## ✅ Final Result:

Matrix `A` is filled such that:

* `A[u, v] = u` if `v` is in the subtree of `u`
* `A[x, y] = u` if `x` and `y` lie in different subtrees of `u` — so `u` is their LCA

---

## 💡 Use Case:

* This matrix can be used for **fast LCA queries**: just lookup `A[x, y]` to get the **lowest common ancestor** of `x` and `y`.
* Suitable for **parallel computation models** (e.g., PRAM).

---
