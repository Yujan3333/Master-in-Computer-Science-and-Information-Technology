# 🔹 Side Effect to Arrays — Definition

A side effect to an array occurs when a statement modifies the contents of the array (any element) in a way that may affect the value read by another statement elsewhere in the program.

---
# 🔹 Table Context

We are analyzing two arrays:

* `A[i]` and `B[j]`
* `i` is the index for `A`, `j` is the index for `B`

We consider **three possibilities** for each index:

1. **UNDEF** → Index has undefined value (never assigned yet)
2. **C1 / C2** → Index has a **known constant** value
3. **NAC** → Index is **Not A Constant** (unknown at compile time, may change)

---

### 1️⃣ Table Rows and Columns

| **A[i]** index | **B[j]** index | Meaning                            |
| -------------- | -------------- | ---------------------------------- |
| UNDEF          | UNDEF          | Both indices unknown               |
| UNDEF          | C2             | i unknown, j constant              |
| UNDEF          | NAC            | i unknown, j not a constant        |
| C1             | UNDEF          | i constant, j unknown              |
| C1             | C2             | i constant, j constant             |
| C1             | NAC            | i constant, j not a constant       |
| NAC            | UNDEF          | i unknown/not constant, j unknown  |
| NAC            | C2             | i unknown/not constant, j constant |
| NAC            | NAC            | both indices unknown/not constant  |

**Your table simplifies this to rows/columns:**

| i\j   | UNDEF       | C2                 | NAC         |
| ----- | ----------- | ------------------ | ----------- |
| UNDEF | Not Aliased | Not Aliased        | Not Aliased |
| C1    | Not Aliased | Aliased if C1 = C2 | Aliased     |
| NAC   | Not Aliased | Aliased            | Aliased     |

---

### 2️⃣ How to Read Each Cell

#### 🔹 Row 1: `i = UNDEF`

* i is undefined → we **cannot assume it equals anything**, but since A[i] and B[j] are **different arrays**, they **cannot alias** regardless of j.
  ✅ **All cells → Not Aliased**

---

#### 🔹 Row 2: `i = C1`

* i is a **known constant**
* j varies:

1. j = UNDEF → j unknown, different array → **Not Aliased**
2. j = C2 → j known constant → **Aliased only if C1 = C2**
3. j = NAC → j unknown/not constant → **Aliased** (conservative assumption)

---

#### 🔹 Row 3: `i = NAC`

* i is unknown/not constant → we **cannot be sure which element of A** is accessed
* j varies:

1. j = UNDEF → different array, assume **Not Aliased**
2. j = C2 → could match unknown i → **Aliased**
3. j = NAC → both unknown → **Aliased**

---

### 3️⃣ Why Aliased vs Not Aliased

* **Different arrays → Not Aliased**, unless index unknown → compiler may be conservative
* **Known constants → Aliased only if constants match**
* **Unknown indices (NAC) → Aliased** (conservative to ensure safety)

---

### 4️⃣ Key Points (Exam-Friendly)

1. **UNDEF** → treat as **definitely not aliased** if arrays differ
2. **Constant index** → aliased only if indices match
3. **NAC** → **conservatively assume alias**, because index may match at runtime
4. Always check **base array first**. Different arrays → usually no alias
5. This table helps **safe constant propagation and optimization** in presence of arrays

---

### 5️⃣ One-Line Takeaway

> *“Two array accesses may alias only if indices are unknown or match known constants; compiler assumes alias if it cannot prove otherwise.”*

---
