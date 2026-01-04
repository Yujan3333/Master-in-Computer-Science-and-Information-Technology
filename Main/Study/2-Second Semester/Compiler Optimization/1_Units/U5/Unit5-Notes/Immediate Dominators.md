
# 4️⃣ Immediate Dominator — *The Real Concept*

## 🔹 Intuition (Very Important)

Among all **dominators** of a node $n$:

* some are **far away** (entry node, higher ancestors)
* one is the **closest strict dominator**

👉 That **closest strict dominator** is called the **immediate dominator**.

---

## 🔹 Formal Definition (Clear & Complete)

A node $d$ is the **immediate dominator** of a node $n$ (written as $idom(n)=d$) **if and only if**:

1. $d$ dominates $n$
2. $d \neq n$ (i.e., $d$ is a *strict* dominator)
3. There exists **no other node** $x$ such that
   $d$ dominates $x$ **and** $x$ dominates $n$

### **In simple words:**

> The immediate dominator is the **last dominator before reaching $n$**.

---

## 🔹 Why This Definition Exists

* A node can have **many dominators**
* We want the one **closest to the node in the CFG**
* This allows dominators to form a **tree structure**

---

# 5️⃣ Dominator Tree (Why Immediate Dominator Is Needed)

The **dominator tree** is constructed using immediate dominators:

* Each node’s **parent** = its immediate dominator
* The **entry node** is the root
* Every other node has **exactly one parent**

📌 The dominator tree represents the **control structure hierarchy** of the program.

---

# 6️⃣ Example (Step-by-Step)

### Control Flow Graph (CFG)

```
Entry → A → B → D
        ↓    ↑
        C ----
```

*(Exact layout is not important — the dominance logic is.)*

---

## Step 1: Dominator Sets

```
Dom(Entry) = {Entry}
Dom(A)     = {Entry, A}
Dom(B)     = {Entry, A, B}
Dom(C)     = {Entry, A, C}
Dom(D)     = {Entry, A, D}
```

---

## Step 2: Find Immediate Dominator

### ⭐ Rule to Remember (Very Important)

> $idom(n)$ = the **strict dominator of $n$ with the largest dominator set**

or simply,

> the **closest dominator of $n$**

---

### Example: Immediate Dominator of $B$

```
Dom(B) = {Entry, A, B}
```

Remove $B$:

```
{Entry, A}
```

* $A$ is closer to $B$ than `Entry`

✅ $idom(B) = A$

---

### Example: Immediate Dominator of $D$

```
Dom(D) = {Entry, A, D}
```

Remove $D$:

```
{Entry, A}
```

* Closest dominator is $A$

✅ $idom(D) = A$

---

# 7️⃣ Why Immediate Dominator Is **Unique**

For any node (except the entry node):

* Dominators form a **chain**
* There is exactly **one closest dominator**

📌 Therefore:

> Every node (except the entry node) has **exactly one immediate dominator**.

---

# 8️⃣ Common Student Confusions

### ❌ Wrong Thinking

> “Immediate dominator is the node just before it in code”

❌ **Incorrect**
Textual order does **not** matter — CFG paths do.

---

### ❌ Wrong Thinking

> “Immediate dominator is the parent in the CFG”

❌ **Incorrect**
CFG edges ≠ Dominator tree edges.

---

### ✅ Correct Thinking

> “Immediate dominator is the **last node that must be passed on every path** to the node.”

---

# 9️⃣ Exam-Friendly Definitions (Memorize)

### **Dominator**

> A node $d$ dominates a node $n$ if **every path from the entry node to $n$ passes through $d$**.

---

### **Immediate Dominator**

> A node $d$ is the immediate dominator of $n$ if $d$ dominates $n$ and **no other node lies between $d$ and $n$ that also dominates $n$**.

---

# 🔟 Golden One-Line Intuition ⭐

> **The immediate dominator is the closest mandatory checkpoint before a node.**
