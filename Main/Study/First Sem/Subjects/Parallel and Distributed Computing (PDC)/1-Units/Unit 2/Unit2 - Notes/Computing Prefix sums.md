
## 🧠 Goal:

Given an input array:

$$
[a_1, a_2, \dots, a_n]
$$

Compute **prefix sums**:

$$
S_i = a_1 + a_2 + \dots + a_i \quad \text{for } i = 1 \text{ to } n
$$

---

## 📜 Algorithm Breakdown

```text
Input: [a1, a2, ..., an]
If n == 1:
    S1 ← a[1]
Else
    For j = 0 to log n – 1 do
        For i = 2^j + 1 to n do in parallel
            Pi: 
                Read a[i - 2^j] from shared memory
                a[i] = a[i - 2^j] + a[i]
```

---

### 🔍 Let's Explain Step-by-Step:

#### ✅ 1. **If n == 1:**

* Only one element — the prefix sum is just the element itself.

#### ✅ 2. **Else — The Main Parallel Prefix Sum Logic:**

We loop through **log n levels** (`j = 0 to log n - 1`), and at each level, we **combine partial sums** using a **distance of $2^j$**.

At each stage $j$, processors work **in parallel** to compute:

$$
a[i] = a[i - 2^j] + a[i]
$$

This builds up prefix sums gradually.

==[Expanding on this](Expanding%20on%20this.md)==

---

### 🧠 Example Walkthrough

Let’s say:
Input = \[3, 1, 4, 2] → $n = 4$, so $\log_2 4 = 2$ iterations: $j = 0, 1$

Let’s walk through this.

---

#### 🔁 j = 0:

* $2^0 = 1$
* $i = 2$ to $4$
* So:

| i | a\[i] = a\[i] + a\[i - 1] |
| - | ------------------------- |
| 2 | a\[2] = 1 + 3 = 4         |
| 3 | a\[3] = 4 + 1 = 5         |
| 4 | a\[4] = 2 + 4 = 6         |

Intermediate array: **\[3, 4, 5, 6]**

---

#### 🔁 j = 1:

* $2^1 = 2$
* $i = 3$ to $4$
* So:

| i | a\[i] = a\[i] + a\[i - 2] |
| - | ------------------------- |
| 3 | a\[3] = 5 + 3 = 8         |
| 4 | a\[4] = 6 + 4 = 10        |

Final array: **\[3, 4, 8, 10]**

Which are the **prefix sums**:

* $a_1 = 3$
* $a_1 + a_2 = 4$
* $a_1 + a_2 + a_3 = 8$
* $a_1 + a_2 + a_3 + a_4 = 10$

✅ **Correct result.**

---

## 🧮 Time and Processors (on PRAM):

* **Time:** $\mathcal{O}(\log n)$
* **Processors:** In worst case, up to $n$ per round ⇒ $\mathcal{O}(n)$
* **Work:** $\mathcal{O}(n \log n)$ (can be optimized to $O(n)$ with clever scheduling)

---

## 📌 Summary:

| Concept         | Meaning                                            |
| --------------- | -------------------------------------------------- |
| What is it?     | Parallel prefix sum                                |
| Input           | \[a₁, a₂, ..., aₙ]                                 |
| Output          | \[a₁, a₁+a₂, ..., a₁+...+aₙ]                       |
| Time Complexity | $O(\log n)$                                        |
| Model           | PRAM (likely CREW or EREW if using scratch memory) |
| Pattern         | Recursive doubling using powers of two             |

---

